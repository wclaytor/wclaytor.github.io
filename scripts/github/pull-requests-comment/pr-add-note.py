#!/usr/bin/env python3
"""
GitHub PR Comment Tool
Add developer notes or comments to pull requests
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

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
        print(f"❌ Error running gh command: {e}")
        print(f"Error output: {e.stderr}")
        return None

def get_current_pr():
    """Get the PR number for the current branch."""
    result = run_gh_command([
        "pr", "view",
        "--json", "number",
        "-q", ".number"
    ])
    
    if result:
        return int(result)
    return None

def read_note_file(file_path):
    """Read a developer note file and return its content."""
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"❌ Error: File not found: {file_path}")
        return None
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    return content

def add_comment_to_pr(pr_number, comment_body, repo=None):
    """Add a comment to a pull request."""
    args = [
        "pr", "comment", str(pr_number),
        "--body", comment_body
    ]
    
    if repo:
        args.extend(["--repo", repo])
    
    result = run_gh_command(args)
    
    if result is not None:
        return True
    return False

def format_note_as_comment(note_content):
    """Format a developer note for PR comment with collapsible section."""
    # Find the title from the markdown
    lines = note_content.strip().split('\n')
    title = "Developer Notes"
    
    for line in lines:
        if line.startswith('## '):
            title = line.replace('## ', '').strip()
            break
    
    # Create collapsible comment
    formatted = f"""## 📝 {title}

<details>
<summary>Click to expand developer notes</summary>

{note_content}

</details>

---
*Added via pr-add-note.py on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    return formatted

def find_latest_note(notes_dir=None):
    """Find the most recent developer note file."""
    if notes_dir is None:
        notes_dir = Path("docs/notes")
    else:
        notes_dir = Path(notes_dir)
    
    if not notes_dir.exists():
        return None
    
    # Find all developer.md files
    developer_notes = list(notes_dir.glob("**/*/developer.md"))
    
    if not developer_notes:
        return None
    
    # Sort by modification time (most recent first)
    developer_notes.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    return developer_notes[0]

def main():
    parser = argparse.ArgumentParser(
        description='Add developer notes as comments to GitHub pull requests',
        epilog='Requires gh CLI to be installed and authenticated',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'file',
        nargs='?',
        help='Path to developer note file (markdown). If not specified, uses latest note from docs/notes'
    )
    
    parser.add_argument(
        '--pr',
        type=int,
        help='PR number to comment on. If not specified, uses current branch PR'
    )
    
    parser.add_argument(
        '--repo',
        help='GitHub repo (owner/repo). If not specified, uses current repo'
    )
    
    parser.add_argument(
        '--raw',
        action='store_true',
        help='Post raw note without formatting or collapsible section'
    )
    
    parser.add_argument(
        '--notes-dir',
        help='Directory to search for notes (default: docs/notes)'
    )
    
    args = parser.parse_args()
    
    print("📝 GitHub PR Comment Tool")
    print("=" * 60)
    print()
    
    # Determine PR number
    pr_number = args.pr
    if not pr_number:
        print("🔍 Looking for PR for current branch...")
        pr_number = get_current_pr()
        if not pr_number:
            print("❌ Error: No PR found for current branch and --pr not specified")
            print("   Either checkout a branch with a PR or specify --pr <number>")
            sys.exit(1)
        print(f"✓ Found PR #{pr_number}")
    
    # Determine note file
    note_file = args.file
    if not note_file:
        print("🔍 Looking for latest developer note...")
        note_file = find_latest_note(args.notes_dir)
        if not note_file:
            print("❌ Error: No developer notes found and no file specified")
            print("   Either specify a file path or create a note in docs/notes/")
            sys.exit(1)
        print(f"✓ Found note: {note_file}")
    
    # Read the note
    print(f"📖 Reading note from {note_file}...")
    note_content = read_note_file(note_file)
    if not note_content:
        sys.exit(1)
    
    # Format the comment
    if args.raw:
        comment_body = note_content
    else:
        comment_body = format_note_as_comment(note_content)
    
    # Add comment to PR
    print(f"💬 Adding comment to PR #{pr_number}...")
    success = add_comment_to_pr(pr_number, comment_body, args.repo)
    
    if success:
        print()
        print("=" * 60)
        print(f"✅ Successfully added comment to PR #{pr_number}")
        
        # Show link to PR
        if args.repo:
            pr_url = f"https://github.com/{args.repo}/pull/{pr_number}"
        else:
            pr_url = run_gh_command(["pr", "view", str(pr_number), "--json", "url", "-q", ".url"])
        
        if pr_url:
            print(f"🔗 View PR: {pr_url}")
        print("=" * 60)
    else:
        print()
        print("❌ Failed to add comment to PR")
        sys.exit(1)

if __name__ == "__main__":
    main()
