#!/usr/bin/env python3
"""
GitHub Pull Requests Sync Tool
Manages local pull request documentation in .github/pull-requests/ folder
"""

import os
import json
import subprocess
import yaml
import re
from pathlib import Path
from datetime import datetime

# Configuration
PRS_DIR = Path(".github/pull-requests")

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

def ensure_prs_directory():
    """Create the pull requests directory if it doesn't exist."""
    PRS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✓ Pull requests directory ready: {PRS_DIR}")

def pull_all_prs():
    """Pull all pull requests from GitHub and create/update local folders."""
    print("\n📥 Pulling all pull requests from GitHub...")
    
    # Get all PRs (open, closed, merged) as JSON
    prs_json = run_gh_command([
        "pr", "list",
        "--state", "all",
        "--limit", "1000",
        "--json", "number,title,body,state,isDraft,labels,assignees,author,milestone,"
                 "createdAt,updatedAt,closedAt,mergedAt,mergeable,mergeCommit,"
                 "headRefName,baseRefName,url,additions,deletions,changedFiles,"
                 "reviewDecision,latestReviews"
    ])
    
    if not prs_json:
        print("Failed to fetch pull requests")
        return
    
    prs = json.loads(prs_json)
    print(f"Found {len(prs)} pull requests")
    
    for pr in prs:
        create_pr_folder(pr)
    
    print("✓ All pull requests synced")

def get_pr_details(pr_number):
    """Get detailed information about a specific PR."""
    pr_json = run_gh_command([
        "pr", "view", str(pr_number),
        "--json", "number,title,body,state,isDraft,labels,assignees,author,milestone,"
                 "createdAt,updatedAt,closedAt,mergedAt,mergeable,mergeCommit,"
                 "headRefName,baseRefName,url,additions,deletions,changedFiles,"
                 "reviewDecision,latestReviews,reviews,commits,statusCheckRollup,comments"
    ])
    
    if not pr_json:
        return None
    
    return json.loads(pr_json)

def get_pr_files(pr_number):
    """Get the list of files changed in a PR."""
    files_output = run_gh_command([
        "pr", "diff", str(pr_number),
        "--name-only"
    ])
    
    if not files_output:
        return []
    
    return files_output.split('\n')

def get_pr_comments(pr_number):
    """Get all comments on a PR."""
    comments_json = run_gh_command([
        "api",
        f"repos/{{owner}}/{{repo}}/issues/{pr_number}/comments",
        "--paginate",
        "--jq", ".[]"
    ])
    
    if not comments_json:
        return []
    
    # Parse JSON lines (one comment per line)
    comments = []
    for line in comments_json.split('\n'):
        if line.strip():
            try:
                comments.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    
    return comments

def create_pr_folder(pr_data):
    """Create a folder and markdown file for a pull request."""
    pr_number = pr_data['number']
    pr_dir = PRS_DIR / f"pr-{pr_number:04d}"
    pr_dir.mkdir(exist_ok=True)
    
    # Create the markdown file with YAML frontmatter
    pr_file = pr_dir / f"pr-{pr_number:04d}.md"
    
    # Determine PR status
    state = pr_data['state']
    is_merged = pr_data.get('mergedAt') is not None
    if is_merged:
        status = 'MERGED'
    elif state == 'CLOSED':
        status = 'CLOSED'
    elif pr_data.get('isDraft'):
        status = 'DRAFT'
    else:
        status = 'OPEN'
    
    # Prepare frontmatter data
    frontmatter = {
        'pr_number': pr_number,
        'title': pr_data['title'],
        'state': state,
        'status': status,
        'is_draft': pr_data.get('isDraft', False),
        'created_at': pr_data['createdAt'],
        'updated_at': pr_data['updatedAt'],
        'closed_at': pr_data.get('closedAt'),
        'merged_at': pr_data.get('mergedAt'),
        'author': pr_data.get('author', {}).get('login', 'unknown'),
        'labels': [label['name'] for label in pr_data.get('labels', [])],
        'assignees': [assignee['login'] for assignee in pr_data.get('assignees', [])],
        'milestone': pr_data.get('milestone', {}).get('title') if pr_data.get('milestone') else None,
        'head_ref': pr_data.get('headRefName'),
        'base_ref': pr_data.get('baseRefName'),
        'additions': pr_data.get('additions', 0),
        'deletions': pr_data.get('deletions', 0),
        'changed_files': pr_data.get('changedFiles', 0),
        'review_decision': pr_data.get('reviewDecision', ''),
        'url': pr_data.get('url', '')
    }
    
    # Write the PR file
    with open(pr_file, 'w') as f:
        f.write("---\n")
        f.write(yaml.dump(frontmatter, default_flow_style=False, sort_keys=False))
        f.write("---\n\n")
        f.write(f"# PR #{pr_number}: {pr_data['title']}\n\n")
        
        # Status badge
        f.write(f"**Status**: `{status}`")
        if pr_data.get('isDraft'):
            f.write(" 🚧")
        if is_merged:
            f.write(" ✅")
        f.write(f" | **Branch**: `{pr_data.get('headRefName')}` → `{pr_data.get('baseRefName')}`\n\n")
        
        # Stats
        f.write(f"**Changes**: +{pr_data.get('additions', 0)} -{pr_data.get('deletions', 0)} "
                f"across {pr_data.get('changedFiles', 0)} files\n\n")
        
        # Review status
        if pr_data.get('reviewDecision'):
            f.write(f"**Review Decision**: {pr_data['reviewDecision']}\n\n")
        
        # Description
        if pr_data.get('body'):
            f.write("## Description\n\n")
            f.write(pr_data['body'])
            f.write("\n\n")
        
        # Reviews section
        if pr_data.get('latestReviews'):
            f.write("## Latest Reviews\n\n")
            for review in pr_data['latestReviews']:
                reviewer = review.get('author', {}).get('login', 'unknown')
                review_state = review.get('state', 'COMMENTED')
                review_body = review.get('body', '')
                f.write(f"- **{reviewer}**: {review_state}")
                if review_body:
                    f.write(f"\n  > {review_body}")
                f.write("\n")
            f.write("\n")
        
        # Comments section
        comments = pr_data.get('comments', [])
        if not comments:
            # Try fetching comments separately if not included in PR data
            comments = get_pr_comments(pr_number)
        
        if comments:
            f.write("## Comments\n\n")
            for comment in comments:
                author = comment.get('user', {}).get('login', comment.get('author', {}).get('login', 'unknown'))
                created_at = comment.get('created_at', comment.get('createdAt', ''))
                body = comment.get('body', '')
                comment_url = comment.get('html_url', '')
                
                # Format timestamp
                timestamp = created_at
                if timestamp:
                    try:
                        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                        timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        pass
                
                f.write(f"### Comment by @{author}")
                if timestamp:
                    f.write(f" - {timestamp}")
                f.write("\n\n")
                
                if body:
                    f.write(f"{body}\n\n")
                
                if comment_url:
                    f.write(f"[View on GitHub]({comment_url})\n\n")
            
            f.write("---\n\n")
        
        f.write("## Implementation Notes\n\n")
        f.write("_Add your implementation notes, decisions, and documentation here._\n\n")
        
        f.write("## Testing Notes\n\n")
        f.write("_Document testing performed, results, and any issues discovered._\n\n")
        
        f.write("## Review Notes\n\n")
        f.write("_Add code review feedback, suggestions, and action items._\n")
    
    # Get and save changed files list
    files = get_pr_files(pr_number)
    if files and files[0]:  # Check if we got any files
        files_list_file = pr_dir / "changed-files.txt"
        with open(files_list_file, 'w') as f:
            f.write('\n'.join(files))
        print(f"  ✓ Saved {len(files)} changed files")
    
    status_indicator = "✅" if is_merged else ("🚧" if pr_data.get('isDraft') else "📝")
    print(f"  {status_indicator} Created/Updated pr-{pr_number:04d}: {pr_data['title'][:50]}...")

def pull_single_pr(pr_number):
    """Pull a single PR and create/update its folder."""
    print(f"\n📥 Pulling PR #{pr_number}...")
    
    pr_data = get_pr_details(pr_number)
    if not pr_data:
        print(f"Failed to fetch PR #{pr_number}")
        return
    
    create_pr_folder(pr_data)
    print(f"✓ PR #{pr_number} synced")

def show_pr_summary():
    """Show a summary of all PRs in the local directory."""
    if not PRS_DIR.exists():
        print("No pull requests directory found. Run 'pull' first.")
        return
    
    pr_dirs = sorted([d for d in PRS_DIR.iterdir() if d.is_dir() and d.name.startswith('pr-')])
    
    if not pr_dirs:
        print("No pull requests found in local directory.")
        return
    
    print(f"\n📊 Summary of {len(pr_dirs)} pull requests:\n")
    
    status_counts = {'MERGED': 0, 'OPEN': 0, 'DRAFT': 0, 'CLOSED': 0}
    
    for pr_dir in pr_dirs:
        pr_file = pr_dir / f"{pr_dir.name}.md"
        if not pr_file.exists():
            continue
        
        with open(pr_file, 'r') as f:
            content = f.read()
        
        # Parse frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                status = frontmatter.get('status', 'UNKNOWN')
                status_counts[status] = status_counts.get(status, 0) + 1
                
                pr_num = frontmatter.get('pr_number')
                title = frontmatter.get('title', 'Unknown')[:60]
                
                status_icon = {
                    'MERGED': '✅',
                    'OPEN': '📝',
                    'DRAFT': '🚧',
                    'CLOSED': '❌'
                }.get(status, '❓')
                
                print(f"  {status_icon} PR #{pr_num:4d}: {title}")
    
    print(f"\n📈 Status Breakdown:")
    for status, count in sorted(status_counts.items()):
        if count > 0:
            print(f"  {status:8s}: {count}")

def main():
    """Main function with simple CLI."""
    import sys
    
    ensure_prs_directory()
    
    if len(sys.argv) < 2:
        print("\n🔄 GitHub Pull Requests Sync Tool\n")
        print("Usage:")
        print("  python pull-requests-sync.py pull              # Pull all PRs from GitHub")
        print("  python pull-requests-sync.py pull <number>     # Pull specific PR by number")
        print("  python pull-requests-sync.py summary           # Show summary of local PRs")
        print("\nExamples:")
        print("  python pull-requests-sync.py pull              # Sync all PRs")
        print("  python pull-requests-sync.py pull 69           # Sync only PR #69")
        print("  python pull-requests-sync.py summary           # Display PR statistics")
        return
    
    command = sys.argv[1]
    
    if command == "pull":
        if len(sys.argv) > 2:
            # Pull specific PR
            try:
                pr_number = int(sys.argv[2])
                pull_single_pr(pr_number)
            except ValueError:
                print(f"Error: Invalid PR number '{sys.argv[2]}'")
                sys.exit(1)
        else:
            # Pull all PRs
            pull_all_prs()
    elif command == "summary":
        show_pr_summary()
    else:
        print(f"Unknown command: {command}")
        print("Run without arguments to see usage.")
        sys.exit(1)

if __name__ == "__main__":
    main()
