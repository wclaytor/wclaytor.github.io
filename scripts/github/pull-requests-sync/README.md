# GitHub Pull Requests Sync

A Python script to synchronize GitHub pull requests with local markdown documentation in your repository.

## Overview

This script maintains a local mirror of your GitHub pull requests in `.github/pull-requests/` directory, allowing you to:
- Keep PR documentation alongside your code
- Add implementation, testing, and review notes to PRs
- Track the complete history of PR reviews and changes
- Quickly reference past PRs and their decisions
- Document lessons learned and patterns discovered

## Prerequisites

- Python 3.6+
- GitHub CLI (`gh`) installed and authenticated
- PyYAML library

## Installation

1. Ensure GitHub CLI is installed and authenticated:
```bash
gh auth status
```

2. Install required Python package:
```bash
pip install pyyaml
```

## Usage

### Pull All Pull Requests from GitHub

Sync all PRs (open, closed, draft, merged) from your GitHub repository to local folders:

```bash
python scripts/github/pull-requests-sync/pull-requests-sync.py pull
```

This creates the following structure:
```
.github/pull-requests/
├── pr-0001/
│   ├── pr-0001.md
│   └── changed-files.txt
├── pr-0069/
│   ├── pr-0069.md
│   └── changed-files.txt
└── pr-0100/
    ├── pr-0100.md
    └── changed-files.txt
```

Each markdown file contains:
- YAML frontmatter with PR metadata (number, title, state, status, labels, assignees, etc.)
- Original PR description
- Latest review comments
- Sections for implementation, testing, and review notes
- A `changed-files.txt` with the list of files modified in the PR

### Pull a Single Pull Request

Sync a specific PR by number:

```bash
python scripts/github/pull-requests-sync/pull-requests-sync.py pull 69
```

This is useful when you want to update documentation for a specific PR without pulling all PRs.

### Show Summary

Display a summary of all PRs in your local directory:

```bash
python scripts/github/pull-requests-sync/pull-requests-sync.py summary
```

Output example:
```
📊 Summary of 15 pull requests:

  ✅ PR #  69: Implement expandable/collapsible sections with Alpine.js (S2-008)
  📝 PR #  70: Add theme customization feature
  🚧 PR #  71: WIP: Refactor navigation component
  ❌ PR #  68: Update dependencies (closed without merge)

📈 Status Breakdown:
  CLOSED  : 2
  DRAFT   : 3
  MERGED  : 8
  OPEN    : 2
```

## File Structure

```
scripts/github/pull-requests-sync/
├── pull-requests-sync.py   # Main sync script
├── README.md               # This file
└── examples/
    └── pr-template.md      # Example PR documentation template
```

## Features

### Current Features

- ✅ Pull all PRs from GitHub to local folders
- ✅ Pull individual PRs by number
- ✅ Preserve PR metadata (labels, assignees, milestones, reviews)
- ✅ Support all PR states (open, closed, draft, merged)
- ✅ Save list of changed files for each PR
- ✅ Display PR summary and statistics
- ✅ Include review comments in documentation
- ✅ Track additions/deletions and file changes

### Planned Features

- 🔄 Two-way sync (update GitHub from local changes)
- 💬 Sync all PR review comments with threading
- 📎 Download and store PR attachments
- 🔗 Auto-link related issues and PRs
- 📊 Generate PR analytics and reports
- 🏷️ Custom tagging and organization

## PR Folder Structure

After pulling a PR, each gets its own folder:

```
.github/pull-requests/pr-0069/
├── pr-0069.md              # Main PR file with metadata
├── changed-files.txt       # List of files changed in this PR
├── implementation.md       # Additional implementation notes (manual)
├── review-summary.md       # Review summary and decisions (manual)
└── artifacts/              # Related files (manual)
    ├── screenshots/
    ├── benchmarks/
    └── test-results/
```

## YAML Frontmatter Fields

Each PR markdown file includes the following metadata:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `pr_number` | integer | PR number | `69` |
| `title` | string | PR title | `"Implement collapsible sections"` |
| `state` | string | GitHub state | `"OPEN"`, `"CLOSED"` |
| `status` | string | Detailed status | `"MERGED"`, `"DRAFT"`, `"OPEN"`, `"CLOSED"` |
| `is_draft` | boolean | Draft status | `true`, `false` |
| `created_at` | datetime | Creation timestamp | `"2025-11-12T18:29:37Z"` |
| `updated_at` | datetime | Last update timestamp | `"2025-11-12T20:15:00Z"` |
| `closed_at` | datetime | Close timestamp (if closed) | `"2025-11-13T10:00:00Z"` |
| `merged_at` | datetime | Merge timestamp (if merged) | `"2025-11-13T10:00:00Z"` |
| `author` | string | GitHub username of author | `"wclaytor"` |
| `labels` | list | PR labels | `["enhancement", "sprint-2"]` |
| `assignees` | list | GitHub usernames | `["wclaytor", "teammate"]` |
| `milestone` | string | Milestone name | `"v1.0"` |
| `head_ref` | string | Source branch | `"feature/collapsible"` |
| `base_ref` | string | Target branch | `"main"` |
| `additions` | integer | Lines added | `1678` |
| `deletions` | integer | Lines deleted | `4` |
| `changed_files` | integer | Number of files changed | `5` |
| `review_decision` | string | Review status | `"APPROVED"`, `"CHANGES_REQUESTED"` |
| `url` | string | GitHub URL | `"https://github.com/..."` |

## Best Practices

1. **Regular Syncing**: Run `pull` regularly to keep local PRs up-to-date
2. **Document Reviews**: Add review notes directly in PR folders
3. **Track Decisions**: Document important technical decisions made during PR review
4. **Commit History**: Commit PR folders to track review and decision history
5. **Post-Merge Notes**: After merging, add lessons learned and follow-up items
6. **Link to Issues**: Cross-reference related issues in PR documentation

## Examples

### Example 1: Pull and Document

```bash
# Pull latest PRs
python scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Add your review notes to a PR
echo "## Review Comments\n\n- Great implementation of Alpine.js patterns\n- Consider extracting to component" >> .github/pull-requests/pr-0069/review-summary.md

# Commit your documentation
git add .github/pull-requests/pr-0069/
git commit -m "docs: add review notes for PR #69"
```

### Example 2: Track Specific PR During Development

```bash
# You're working on PR #69, pull just that PR to update your docs
python scripts/github/pull-requests-sync/pull-requests-sync.py pull 69

# Review the changed files
cat .github/pull-requests/pr-0069/changed-files.txt

# Add implementation notes
cat >> .github/pull-requests/pr-0069/pr-0069.md << 'EOF'

## Key Implementation Details

- Used Alpine.js `x-data` and `x-show` for state management
- LocalStorage persists section states across page loads
- Added ARIA attributes for accessibility
- Print styles force all sections expanded
EOF
```

### Example 3: Generate PR Report

```bash
# Get a quick overview of all PRs
python scripts/github/pull-requests-sync/pull-requests-sync.py summary

# Pull all PRs for complete analysis
python scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Now you can grep through all PR documentation
grep -r "accessibility" .github/pull-requests/

# Find all PRs that modified a specific file
grep -l "index.html" .github/pull-requests/*/changed-files.txt
```

## Use Cases

### Code Review Tracking
Document detailed review feedback, suggestions, and decisions that aren't captured in GitHub comments.

### Post-Merge Documentation
After merging, add:
- What worked well
- What could be improved
- Follow-up tasks identified
- Lessons learned

### Historical Reference
Quickly find:
- When a feature was implemented
- Why certain decisions were made
- Who reviewed and approved changes
- What files were modified

### Sprint Retrospectives
Review all PRs from a sprint to identify:
- Common issues or patterns
- Areas for improvement
- Successful practices to continue

### Onboarding
Help new team members understand:
- Code evolution and history
- Review standards and expectations
- Common patterns and practices
- Major architectural decisions

## Troubleshooting

### Issue: `gh: command not found`
**Solution**: Install GitHub CLI from https://cli.github.com

### Issue: `No module named 'yaml'`
**Solution**: Install PyYAML: `pip install pyyaml`

### Issue: `gh auth status` shows not authenticated
**Solution**: Run `gh auth login` and follow the prompts

### Issue: Script creates PRs from wrong repository
**Solution**: Ensure you're in the correct repository directory, or use `gh repo set-default`

### Issue: No changed files listed
**Solution**: Some very old or special PRs may not return file lists. The script will create the PR folder but skip the changed-files.txt.

## Integration with Issues Sync

This script pairs well with the `issues-sync` script:

```bash
# Sync both issues and PRs
python scripts/github/issues-sync/issues-sync.py pull
python scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Now you have complete documentation of your project's history
tree .github/
```

## Contributing

When adding features to this script:
1. Keep the script simple and focused
2. Add examples to the documentation
3. Update this README with new functionality
4. Test with various PR states (open, draft, merged, closed)

## License

This script is part of the project repository and follows the same license.

## Related Scripts

- `scripts/github/issues-sync/` - Sync GitHub issues to local folders
- `scripts/github/pr-analytics/` - Generate PR analytics and reports
- `scripts/github/pr-templates/` - PR template management
