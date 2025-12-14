#!/usr/bin/env python3
"""
GitHub Issues Sync Tool
Manages local issue documentation in .github/issues/ folder
"""

import os
import json
import subprocess
import yaml
import re
from pathlib import Path
from datetime import datetime

# Configuration
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
        "--json", "number,title,body,state,labels,assignees,milestone,createdAt,updatedAt,closedAt,author"
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
        'milestone': issue_data.get('milestone', {}).get('title') if issue_data.get('milestone') else None
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
        f.write("## Notes\n\n")
        f.write("_Add your implementation notes, decisions, and documentation here._\n")
    
    print(f"  ✓ Created/Updated issue-{issue_number:04d}: {issue_data['title'][:50]}...")

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
    if content.startswith('---'):
        # Split on the closing ---
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
        else:
            print("Error: Invalid frontmatter format")
            return None
    else:
        # No frontmatter, use the whole file as body
        frontmatter = {}
        body = content
    
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
    """Main function with simple CLI."""
    import sys
    
    ensure_issues_directory()
    
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python gh_issues_sync.py pull                    # Pull all issues from GitHub")
        print("  python gh_issues_sync.py create <file.md>        # Create issue from markdown file")
        print("  python gh_issues_sync.py epic <epic_file.md>     # Create epic with children")
        print("\nExamples:")
        print("  python gh_issues_sync.py pull")
        print("  python gh_issues_sync.py create new_feature.md")
        print("  python gh_issues_sync.py epic epic_with_tasks.md")
        return
    
    command = sys.argv[1]
    
    if command == "pull":
        pull_all_issues()
    elif command == "create" and len(sys.argv) > 2:
        create_issue_from_file(sys.argv[2])
    elif command == "epic" and len(sys.argv) > 2:
        create_epic_with_children(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()