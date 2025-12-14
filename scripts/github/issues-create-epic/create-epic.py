#!/usr/bin/env python3
"""
GitHub Issue Creator from Markdown with YAML Frontmatter
Reusable script for creating GitHub issues from structured markdown documents.
Uses GitHub CLI (gh) for API interactions.
"""

import subprocess
import sys
import re
import yaml
import json
import argparse
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)


class GitHubIssueCreator:
    def __init__(self, repo: Optional[str] = None, dry_run: bool = False, verbose: bool = False):
        """
        Initialize the GitHub Issue Creator.
        
        Args:
            repo: Repository in format "owner/repo". If None, uses current repo.
            dry_run: If True, don't actually create issues
            verbose: If True, show detailed command output
        """
        self.repo = repo
        self.dry_run = dry_run
        self.verbose = verbose
        self.created_issues = {}  # Map ticket IDs to issue numbers
        self.existing_labels = set()  # Cache of existing labels
        self.existing_milestones = {}  # Cache of existing milestones (title -> number)
        
        # Set logging level
        if verbose:
            logger.setLevel(logging.DEBUG)
        
        if not dry_run:
            self._verify_gh_cli()
            self._load_existing_labels()
            self._load_existing_milestones()
    
    def _verify_gh_cli(self):
        """Verify that gh CLI is installed and authenticated."""
        logger.info("🔍 Verifying GitHub CLI installation and authentication...")
        
        try:
            # Check if gh is installed
            result = subprocess.run(
                ['gh', '--version'],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                logger.error("❌ Error: gh CLI is not installed")
                logger.error("Please install it from: https://cli.github.com/")
                sys.exit(1)
            
            if self.verbose:
                version_line = result.stdout.split('\n')[0]
                logger.debug(f"  ✓ Found: {version_line}")
            
            # Check authentication
            result = subprocess.run(
                ['gh', 'auth', 'status'],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                logger.error("❌ Error: Not authenticated with GitHub")
                logger.error("Please run: gh auth login")
                sys.exit(1)
            
            if self.verbose:
                logger.debug("  ✓ Authenticated with GitHub")
                
            logger.info("✅ GitHub CLI verified and authenticated\n")
            
        except FileNotFoundError:
            logger.error("❌ Error: gh CLI is not installed")
            logger.error("Please install it from: https://cli.github.com/")
            sys.exit(1)
    
    def _load_existing_labels(self):
        """Load existing labels from the repository to cache."""
        if self.verbose:
            logger.debug("  Loading existing labels...")
        
        args = ['label', 'list', '--json', 'name', '-q', '.[].name']
        
        if self.repo:
            args.extend(['--repo', self.repo])
        
        try:
            result = subprocess.run(
                ['gh'] + args,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                self.existing_labels = set(result.stdout.strip().split('\n'))
                if self.verbose:
                    logger.debug(f"  Found {len(self.existing_labels)} existing labels")
        except subprocess.CalledProcessError:
            if self.verbose:
                logger.debug("  Could not load labels (may need to create them)")
    
    def _load_existing_milestones(self):
        """Load existing milestones from the repository to cache."""
        if self.verbose:
            logger.debug("  Loading existing milestones...")
        
        args = ['api', 'repos/{owner}/{repo}/milestones', '--jq', '.[].title']
        
        if self.repo:
            args.extend(['--repo', self.repo])
        
        try:
            result = subprocess.run(
                ['gh'] + args,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                milestone_titles = result.stdout.strip().split('\n')
                # Get milestone numbers too
                args_with_number = ['api', 'repos/{owner}/{repo}/milestones', '--jq', r'.[] | "\(.title)|\(.number)"']
                if self.repo:
                    args_with_number.extend(['--repo', self.repo])
                
                result = subprocess.run(
                    ['gh'] + args_with_number,
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                for line in result.stdout.strip().split('\n'):
                    if '|' in line:
                        title, number = line.rsplit('|', 1)
                        self.existing_milestones[title] = int(number)
                
                if self.verbose:
                    logger.debug(f"  Found {len(self.existing_milestones)} existing milestones")
        except subprocess.CalledProcessError:
            if self.verbose:
                logger.debug("  Could not load milestones (may need to create them)")
    
    def _ensure_milestone_exists(self, milestone: str) -> Optional[int]:
        """Create a milestone if it doesn't exist and return its number."""
        if milestone in self.existing_milestones:
            return self.existing_milestones[milestone]
        
        if self.verbose:
            logger.debug(f"  Creating milestone: {milestone}")
        
        # Create milestone with due date 30 days from now
        args = ['api', 'repos/{owner}/{repo}/milestones', '-f', f'title={milestone}', '--jq', '.number']
        
        if self.repo:
            args.extend(['--repo', self.repo])
        
        try:
            result = subprocess.run(
                ['gh'] + args,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                milestone_number = int(result.stdout.strip())
                self.existing_milestones[milestone] = milestone_number
                logger.info(f"  ✓ Created milestone: {milestone}")
                return milestone_number
        except subprocess.CalledProcessError as e:
            if self.verbose:
                logger.debug(f"  Milestone creation failed: {milestone}")
            # Add to cache anyway in case it already exists
            return None
        
        return None
    
    def _ensure_label_exists(self, label: str):
        """Create a label if it doesn't exist."""
        if label in self.existing_labels:
            return
        
        if self.verbose:
            logger.debug(f"  Creating label: {label}")
        
        args = ['label', 'create', label, '--force']
        
        if self.repo:
            args.extend(['--repo', self.repo])
        
        try:
            subprocess.run(
                ['gh'] + args,
                capture_output=True,
                text=True,
                check=True
            )
            self.existing_labels.add(label)
            logger.info(f"  ✓ Created label: {label}")
        except subprocess.CalledProcessError as e:
            if self.verbose:
                logger.debug(f"  Label creation failed (may already exist): {label}")
            # Add to cache anyway in case it already exists
            self.existing_labels.add(label)
    
    def _run_gh_command(self, args: List[str], capture_output: bool = True) -> Optional[str]:
        """
        Run a gh command and return the output.
        
        Args:
            args: Command arguments (excluding 'gh')
            capture_output: Whether to capture and return output
            
        Returns:
            Command output as string, or None on error
        """
        cmd = ['gh'] + args
        
        if self.verbose:
            logger.debug(f"  → Running: {' '.join(cmd)}")
        
        if self.dry_run:
            logger.info(f"  [DRY RUN] Would run: {' '.join(cmd)}")
            return None
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=capture_output,
                text=True,
                check=True
            )
            
            output = result.stdout.strip() if capture_output else None
            
            if self.verbose and output:
                logger.debug(f"  ← Output: {output[:100]}..." if len(output) > 100 else f"  ← Output: {output}")
            
            return output
            
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Command failed: {' '.join(cmd)}")
            if e.stderr:
                # Extract just the error message, not the full help text
                error_lines = e.stderr.split('\n')
                for line in error_lines:
                    if line.strip() and not line.startswith('Usage:') and not line.startswith('Flags:'):
                        logger.error(f"  Error: {line.strip()}")
                    if line.startswith('Usage:'):
                        break
            return None
    
    def _extract_issue_number_from_url(self, url: str) -> Optional[int]:
        """Extract issue number from GitHub issue URL."""
        match = re.search(r'/issues/(\d+)$', url)
        if match:
            return int(match.group(1))
        return None
    
    def parse_markdown_with_frontmatter(self, file_path: str) -> Dict[str, Any]:
        """Parse markdown file with YAML frontmatter blocks."""
        logger.info(f"📖 Reading and parsing {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract epic frontmatter
        epic_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        epic_data = {}
        if epic_match:
            epic_yaml = epic_match.group(1)
            epic_data = yaml.safe_load(epic_yaml).get('epic', {})
            logger.info(f"  ✓ Found epic: {epic_data.get('title', 'Untitled')}")
        
        # Extract all ticket frontmatters and content
        tickets = []
        pattern = r'---\nticket:(.*?)\n---\n(.*?)(?=---\nticket:|$)'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for yaml_content, markdown_content in matches:
            ticket_data = yaml.safe_load(f"ticket:{yaml_content}")['ticket']
            ticket_data['content'] = markdown_content.strip()
            tickets.append(ticket_data)
        
        logger.info(f"  ✓ Found {len(tickets)} ticket(s)")
        
        if self.verbose:
            for ticket in tickets:
                logger.debug(f"    - {ticket['id']}: {ticket['title']}")
        
        logger.info("")
        
        return {
            'epic': epic_data,
            'tickets': tickets
        }
    
    def create_epic(self, epic_data: Dict[str, Any]) -> int:
        """Create the epic issue."""
        logger.info(f"🎯 Creating Epic: {epic_data['title']}")
        
        # Ensure labels exist
        if epic_data.get('labels') and not self.dry_run:
            for label in epic_data['labels']:
                self._ensure_label_exists(label)
        
        # Ensure milestone exists
        if epic_data.get('milestone') and not self.dry_run:
            self._ensure_milestone_exists(epic_data['milestone'])
        
        body = f"{epic_data['description']}\n\n## Child Issues\n*Will be updated with ticket links*"
        
        # Build gh issue create command (without --json for compatibility)
        args = [
            'issue', 'create',
            '--title', epic_data['title'],
            '--body', body
        ]
        
        # Add repo if specified
        if self.repo:
            args.extend(['--repo', self.repo])
            if self.verbose:
                logger.debug(f"  Using repository: {self.repo}")
        
        # Add labels
        if epic_data.get('labels'):
            for label in epic_data['labels']:
                args.extend(['--label', label])
            if self.verbose:
                logger.debug(f"  Adding labels: {', '.join(epic_data['labels'])}")
        
        # Add milestone
        if epic_data.get('milestone'):
            args.extend(['--milestone', epic_data['milestone']])
            if self.verbose:
                logger.debug(f"  Adding milestone: {epic_data['milestone']}")
        
        if self.dry_run:
            logger.info(f"  [DRY RUN] Would create epic with title: {epic_data['title']}")
            return 999
        
        # Run command and get URL
        output = self._run_gh_command(args)
        
        if output:
            issue_number = self._extract_issue_number_from_url(output)
            if issue_number:
                logger.info(f"  ✅ Created Epic: #{issue_number}")
                logger.info(f"  🔗 URL: {output}\n")
                return issue_number
        
        logger.error(f"  ❌ Failed to create epic")
        sys.exit(1)
    
    def create_ticket(self, ticket: Dict[str, Any], epic_number: int) -> int:
        """Create a single ticket issue."""
        ticket_id = ticket['id']
        title = f"{ticket_id}: {ticket['title']}"
        
        logger.info(f"📝 Creating {ticket_id}: {ticket['title']}")
        
        # Ensure labels exist
        if ticket.get('labels') and not self.dry_run:
            for label in ticket['labels']:
                self._ensure_label_exists(label)
        
        # Ensure milestone exists
        if ticket.get('milestone') and not self.dry_run:
            self._ensure_milestone_exists(ticket['milestone'])
        
        # Build the issue body
        body_parts = [
            f"**Parent Epic:** #{epic_number}",
            f"**Type:** {ticket.get('type', 'task')}",
            f"**Priority:** {ticket.get('priority', 'P2')}",
            f"**Story Points:** {ticket.get('points', '?')}",
            f"**Sprint:** {ticket.get('sprint', '?')}",
        ]
        
        # Add dependencies with links
        if ticket.get('dependencies'):
            deps = []
            for dep_id in ticket['dependencies']:
                if dep_id in self.created_issues:
                    deps.append(f"#{self.created_issues[dep_id]}")
                else:
                    deps.append(f"{dep_id} (not yet created)")
            body_parts.append(f"**Dependencies:** {', '.join(deps)}")
        
        body_parts.append(f"\n---\n\n{ticket['content']}")
        body_parts.append(f"\n---\n*Part of #{epic_number}*")
        
        body = "\n".join(body_parts)
        
        # Build gh issue create command (without --json for compatibility)
        args = [
            'issue', 'create',
            '--title', title,
            '--body', body
        ]
        
        # Add repo if specified
        if self.repo:
            args.extend(['--repo', self.repo])
        
        # Add labels
        if ticket.get('labels'):
            for label in ticket['labels']:
                args.extend(['--label', label])
            if self.verbose:
                logger.debug(f"  Adding labels: {', '.join(ticket['labels'])}")
        
        # Add milestone
        if ticket.get('milestone'):
            args.extend(['--milestone', ticket['milestone']])
        
        # Add assignee
        if ticket.get('assignee'):
            args.extend(['--assignee', ticket['assignee']])
        
        if self.dry_run:
            logger.info(f"  [DRY RUN] Would create ticket {ticket_id}")
            self.created_issues[ticket_id] = 1000 + len(self.created_issues)
            return self.created_issues[ticket_id]
        
        # Run command and get URL
        output = self._run_gh_command(args)
        
        if output:
            issue_number = self._extract_issue_number_from_url(output)
            if issue_number:
                self.created_issues[ticket_id] = issue_number
                logger.info(f"  ✅ Created: #{issue_number}")
                if self.verbose:
                    logger.debug(f"  🔗 URL: {output}")
                logger.info("")
                return issue_number
        
        logger.error(f"  ❌ Failed to create ticket {ticket_id}")
        return None
    
    def update_epic_with_tickets(self, epic_number: int):
        """Update the epic with links to all created tickets."""
        logger.info(f"🔄 Updating Epic #{epic_number} with ticket links...")
        
        if self.dry_run:
            logger.info(f"  [DRY RUN] Would update epic with {len(self.created_issues)} ticket links")
            return
        
        # Get current epic body
        view_args = ['issue', 'view', str(epic_number), '--json', 'body', '-q', '.body']
        
        # Add repo if specified
        if self.repo:
            view_args.insert(3, '--repo')
            view_args.insert(4, self.repo)
        
        current_body = self._run_gh_command(view_args)
        
        if not current_body:
            logger.error(f"  ❌ Failed to retrieve epic body")
            return
        
        # Build ticket list with task checkboxes
        ticket_list = []
        for ticket_id, issue_number in sorted(self.created_issues.items()):
            ticket_list.append(f"- [ ] #{issue_number} - {ticket_id}")
        
        # Update body
        updated_body = current_body.replace(
            "*Will be updated with ticket links*",
            "\n".join(ticket_list)
        )
        
        # Update the issue
        edit_args = [
            'issue', 'edit', str(epic_number),
            '--body', updated_body
        ]
        
        # Add repo if specified
        if self.repo:
            edit_args.extend(['--repo', self.repo])
        
        result = subprocess.run(
            ['gh'] + edit_args,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            logger.info(f"  ✅ Updated epic with {len(self.created_issues)} ticket links\n")
        else:
            logger.error(f"  ❌ Failed to update epic")
            if result.stderr:
                logger.error(f"  Error: {result.stderr}")
    
    def link_issue_to_epic(self, issue_number: int, epic_number: int, ticket_id: str):
        """
        Create a link between a child issue and the epic using GitHub's issue references.
        This uses a comment to establish the relationship.
        """
        if self.dry_run:
            return
        
        if self.verbose:
            logger.debug(f"  Linking #{issue_number} to epic #{epic_number}")
        
        # Add a comment to the child issue referencing the epic
        comment_body = f"Linked to parent epic #{epic_number}"
        
        comment_args = [
            'issue', 'comment', str(issue_number),
            '--body', comment_body
        ]
        
        # Add repo if specified
        if self.repo:
            comment_args.extend(['--repo', self.repo])
        
        self._run_gh_command(comment_args)
    
    def create_issues_from_file(self, file_path: str):
        """Main method to create all issues from a markdown file."""
        logger.info(f"{'='*60}")
        logger.info(f"GitHub Epic & Issues Creator")
        logger.info(f"{'='*60}\n")
        
        data = self.parse_markdown_with_frontmatter(file_path)
        
        # Create epic
        epic_number = None
        if data.get('epic'):
            epic_number = self.create_epic(data['epic'])
        
        # Create tickets
        if data['tickets']:
            logger.info(f"📋 Creating {len(data['tickets'])} ticket(s)...\n")
            for i, ticket in enumerate(data['tickets'], 1):
                logger.info(f"[{i}/{len(data['tickets'])}]")
                issue_number = self.create_ticket(ticket, epic_number)
                if issue_number and epic_number:
                    self.link_issue_to_epic(issue_number, epic_number, ticket['id'])
        
        # Update epic with ticket links
        if epic_number and self.created_issues:
            self.update_epic_with_tickets(epic_number)
        
        # Summary
        logger.info(f"{'='*60}")
        logger.info(f"✅ Summary")
        logger.info(f"{'='*60}")
        if epic_number:
            logger.info(f"  Epic: #{epic_number}")
        else:
            logger.info(f"  Epic: Not created")
        logger.info(f"  Tickets created: {len(self.created_issues)}")
        
        if self.created_issues:
            logger.info(f"\n  Created Issues:")
            for ticket_id, issue_number in sorted(self.created_issues.items()):
                logger.info(f"    {ticket_id} → #{issue_number}")
        
        if not self.dry_run and epic_number:
            repo_part = f"/{self.repo}" if self.repo else "/<current-repo>"
            logger.info(f"\n  🔗 View Epic: https://github.com{repo_part}/issues/{epic_number}")
        
        logger.info(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Create GitHub issues from structured markdown using gh CLI',
        epilog='Requires gh CLI to be installed and authenticated (gh auth login)',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('file', help='Path to markdown file with tickets')
    parser.add_argument('--repo', help='GitHub repo (owner/repo). If not specified, uses current repo.')
    parser.add_argument('--dry-run', action='store_true', help='Preview without creating issues')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed command output')
    
    args = parser.parse_args()
    
    # Verify file exists
    if not Path(args.file).exists():
        logger.error(f"❌ Error: File not found: {args.file}")
        sys.exit(1)
    
    # Create issues
    creator = GitHubIssueCreator(args.repo, args.dry_run, args.verbose)
    creator.create_issues_from_file(args.file)


if __name__ == '__main__':
    main()
