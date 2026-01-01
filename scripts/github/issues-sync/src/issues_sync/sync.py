#!/usr/bin/env python3
"""
GitHub Issues Sync Tool
Manages local issue documentation in .github/issues/ folder
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

# Configuration - can be overridden via --output flag
ISSUES_DIR = Path(".github/issues")


def set_issues_dir(output_path: str | None) -> None:
    """Set the issues directory based on output path."""
    global ISSUES_DIR
    if output_path:
        ISSUES_DIR = Path(output_path) / ".github" / "issues"
    else:
        ISSUES_DIR = Path(".github/issues")


def run_gh_command(args):
    """Run a gh CLI command and return the output."""
    try:
        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running gh command: {e}")
        print(f"Error output: {e.stderr}")
        return None


def ensure_issues_directory():
    """Create the issues directory if it doesn't exist."""
    ISSUES_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✓ Issues directory ready: {ISSUES_DIR}")


def pull_all_issues():
    """Pull all issues from GitHub and create/update local folders."""
    print("\n📥 Pulling all issues from GitHub...")
    
    # Get all issues (open and closed) as JSON
    issues_json = run_gh_command([
        "issue", "list",
        "--state", "all",
        "--limit", "1000",
        "--json", "number,title,body,state,labels,assignees,milestone,createdAt,updatedAt,closedAt,author,comments"
    ])
    
    if not issues_json:
        print("Failed to fetch issues")
        return
    
    issues = json.loads(issues_json)
    print(f"Found {len(issues)} issues")
    
    for issue in issues:
        create_issue_folder(issue)
    
    print("✓ All issues synced")


def create_issue_folder(issue_data):
    """Create a folder and markdown file for an issue."""
    issue_number = issue_data['number']
    issue_dir = ISSUES_DIR / f"issue-{issue_number:04d}"
    issue_dir.mkdir(exist_ok=True)
    
    # Create the markdown file with YAML frontmatter
    issue_file = issue_dir / f"issue-{issue_number:04d}.md"
    
    # Get comments
    comments = issue_data.get('comments', [])
    
    # Prepare frontmatter data
    frontmatter = {
        'issue_number': issue_number,
        'title': issue_data['title'],
        'state': issue_data['state'],
        'created_at': issue_data['createdAt'],
        'updated_at': issue_data['updatedAt'],
        'closed_at': issue_data.get('closedAt'),
        'author': issue_data.get('author', {}).get('login', 'unknown'),
        'labels': [label['name'] for label in issue_data.get('labels', [])],
        'assignees': [assignee['login'] for assignee in issue_data.get('assignees', [])],
        'milestone': issue_data.get('milestone', {}).get('title') if issue_data.get('milestone') else None,
        'comment_count': len(comments)
    }
    
    # Write the issue file
    with open(issue_file, 'w') as f:
        f.write("---\n")
        f.write(yaml.dump(frontmatter, default_flow_style=False))
        f.write("---\n\n")
        f.write(f"# Issue #{issue_number}: {issue_data['title']}\n\n")
        if issue_data.get('body'):
            f.write("## Description\n\n")
            f.write(issue_data['body'])
            f.write("\n\n")
        
        # Write comments section
        if comments:
            f.write("## Comments\n\n")
            for comment in comments:
                author = comment.get('author', {}).get('login', 'unknown')
                created_at = comment.get('createdAt', '')
                body = comment.get('body', '')
                
                f.write(f"### @{author} - {created_at}\n\n")
                f.write(body)
                f.write("\n\n---\n\n")
        
        f.write("## Notes\n\n")
        f.write("_Add your implementation notes, decisions, and documentation here._\n")
    
    comment_info = f" ({len(comments)} comments)" if comments else ""
    print(f"  ✓ Created/Updated issue-{issue_number:04d}: {issue_data['title'][:50]}...{comment_info}")
    
    print(f"  ✓ Created/Updated issue-{issue_number:04d}: {issue_data['title'][:50]}...")


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content.
    
    Returns:
        tuple: (frontmatter_dict, body_content) or (None, None) if invalid
    """
    if content.startswith('---'):
        # Split on the closing ---
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return frontmatter, body
        else:
            return None, None
    else:
        # No frontmatter, use the whole file as body
        return {}, content


def create_issue_from_file(filepath):
    """Create a GitHub issue from a markdown file with YAML frontmatter."""
    filepath = Path(filepath)
    
    if not filepath.exists():
        print(f"Error: File {filepath} does not exist")
        return None
    
    print(f"\n📤 Creating issue from {filepath}...")
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Parse YAML frontmatter
    frontmatter, body = parse_frontmatter(content)
    if frontmatter is None:
        print("Error: Invalid frontmatter format")
        return None
    
    # Extract title from frontmatter or first heading
    title = frontmatter.get('title')
    if not title:
        # Try to extract from first markdown heading
        match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        if match:
            title = match.group(1)
            # Remove the title from body to avoid duplication
            body = body.replace(match.group(0), '').strip()
        else:
            print("Error: No title found in frontmatter or content")
            return None
    
    # Build the gh issue create command
    cmd = ["issue", "create", "--title", title]
    
    if body:
        cmd.extend(["--body", body])
    
    # Add optional fields from frontmatter
    if 'labels' in frontmatter:
        labels = frontmatter['labels']
        if isinstance(labels, str):
            labels = [labels]
        for label in labels:
            cmd.extend(["--label", label])
    
    if 'assignees' in frontmatter:
        assignees = frontmatter['assignees']
        if isinstance(assignees, str):
            assignees = [assignees]
        for assignee in assignees:
            cmd.extend(["--assignee", assignee])
    
    if 'milestone' in frontmatter:
        cmd.extend(["--milestone", frontmatter['milestone']])
    
    # Create the issue
    result = run_gh_command(cmd)
    if result:
        print(f"✓ Issue created: {result}")
        # Extract issue number from the URL
        match = re.search(r'/issues/(\d+)', result)
        if match:
            issue_number = int(match.group(1))
            # Now pull this specific issue to create its folder
            issue_json = run_gh_command([
                "issue", "view", str(issue_number),
                "--json", "number,title,body,state,labels,assignees,milestone,createdAt,updatedAt,closedAt,author"
            ])
            if issue_json:
                issue_data = json.loads(issue_json)
                create_issue_folder(issue_data)
        return result
    else:
        print("Failed to create issue")
        return None


def create_epic_with_children(epic_file):
    """Create an epic issue with child issues from a single markdown file."""
    filepath = Path(epic_file)
    
    if not filepath.exists():
        print(f"Error: File {filepath} does not exist")
        return
    
    print(f"\n🎯 Creating epic with children from {filepath}...")
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split the file into sections by looking for epic and children markers
    sections = re.split(r'^---\s*$', content, flags=re.MULTILINE)
    
    if len(sections) < 2:
        print("Error: File should have at least an epic section")
        return
    
    # First section should be the epic
    epic_section = sections[0].strip()
    
    # Parse epic frontmatter
    if epic_section.startswith('---'):
        parts = epic_section.split('---', 2)
        if len(parts) >= 3:
            epic_frontmatter = yaml.safe_load(parts[1])
            epic_body = parts[2].strip()
        else:
            epic_frontmatter = {}
            epic_body = epic_section
    else:
        epic_frontmatter = {}
        epic_body = epic_section
    
    # Create the epic
    epic_title = epic_frontmatter.get('title', 'Epic')
    epic_frontmatter['labels'] = epic_frontmatter.get('labels', [])
    if 'epic' not in epic_frontmatter['labels']:
        epic_frontmatter['labels'].append('epic')
    
    # Create temporary file for epic
    epic_temp = Path('/tmp/epic_temp.md')
    with open(epic_temp, 'w') as f:
        f.write('---\n')
        f.write(yaml.dump(epic_frontmatter, default_flow_style=False))
        f.write('---\n\n')
        f.write(epic_body)
    
    # Create the epic issue
    epic_url = create_issue_from_file(epic_temp)
    if not epic_url:
        print("Failed to create epic")
        return
    
    # Extract epic issue number
    epic_match = re.search(r'/issues/(\d+)', epic_url)
    epic_number = int(epic_match.group(1)) if epic_match else None
    
    print(f"✓ Epic created: #{epic_number} - {epic_title}")
    
    # Process child issues
    for i, section in enumerate(sections[1:], 1):
        section = section.strip()
        if not section:
            continue
        
        # Parse child frontmatter
        if section.startswith('---'):
            parts = section.split('---', 2)
            if len(parts) >= 3:
                child_frontmatter = yaml.safe_load(parts[1])
                child_body = parts[2].strip()
            else:
                child_frontmatter = {}
                child_body = section
        else:
            child_frontmatter = {}
            child_body = section
        
        # Add reference to epic in the body
        if epic_number:
            child_body = f"Parent Epic: #{epic_number}\n\n{child_body}"
        
        # Create temporary file for child
        child_temp = Path(f'/tmp/child_temp_{i}.md')
        with open(child_temp, 'w') as f:
            f.write('---\n')
            f.write(yaml.dump(child_frontmatter, default_flow_style=False))
            f.write('---\n\n')
            f.write(child_body)
        
        # Create the child issue
        child_url = create_issue_from_file(child_temp)
        if child_url:
            child_match = re.search(r'/issues/(\d+)', child_url)
            child_number = int(child_match.group(1)) if child_match else None
            child_title = child_frontmatter.get('title', f'Child {i}')
            print(f"  ✓ Child created: #{child_number} - {child_title}")


def main():
    """Main function with argparse CLI."""
    parser = argparse.ArgumentParser(
        description="Synchronize GitHub issues with local markdown documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  issues-sync pull
  issues-sync pull --output /path/to/repo
  issues-sync create new_feature.md
  issues-sync epic epic_with_tasks.md
"""
    )
    
    parser.add_argument(
        "-o", "--output",
        metavar="DIR",
        help="Output directory for .github/issues/ folder (default: current directory)"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Pull command
    pull_parser = subparsers.add_parser("pull", help="Pull all issues from GitHub")
    pull_parser.add_argument(
        "-o", "--output",
        metavar="DIR",
        help="Output directory for .github/issues/ folder"
    )
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create issue from markdown file")
    create_parser.add_argument("file", help="Markdown file with issue content")
    create_parser.add_argument(
        "-o", "--output",
        metavar="DIR",
        help="Output directory for .github/issues/ folder"
    )
    
    # Epic command
    epic_parser = subparsers.add_parser("epic", help="Create epic with child issues")
    epic_parser.add_argument("file", help="Markdown file with epic and child issues")
    epic_parser.add_argument(
        "-o", "--output",
        metavar="DIR",
        help="Output directory for .github/issues/ folder"
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Set the output directory
    set_issues_dir(args.output)
    ensure_issues_directory()
    
    if args.command == "pull":
        pull_all_issues()
    elif args.command == "create":
        create_issue_from_file(args.file)
    elif args.command == "epic":
        create_epic_with_children(args.file)


if __name__ == "__main__":
    main()
