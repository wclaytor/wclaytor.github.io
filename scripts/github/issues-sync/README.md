# GitHub Issues Sync

A Python tool to synchronize GitHub issues with local markdown documentation in your repository.

## Overview

This tool maintains a local mirror of your GitHub issues in `.github/issues/` directory, allowing you to:
- Keep issue documentation alongside your code
- Add implementation notes and decisions to issues
- Track the complete history of issue resolution
- Create new issues from markdown files with YAML frontmatter
- Batch create epics with child issues

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- GitHub CLI (`gh`) installed and authenticated

## Quick Start with uv

The easiest way to use this tool is with [uv](https://docs.astral.sh/uv/). No need to manually create virtual environments or install dependencies—`uv` handles everything automatically.

```bash
# From the issues-sync directory
cd scripts/github/issues-sync
uv run issues-sync pull

# Run tests
uv run pytest
```

### Running from the Repository Root

Use the `--output` flag to specify where the `.github/issues/` folder should be created:

```bash
# From repo root - output issues to the repo root
uv run --directory ./scripts/github/issues-sync \
  issues-sync pull --output "$PWD"

# Create an issue from a file, output to repo root
uv run --directory ./scripts/github/issues-sync \
  issues-sync create "$PWD/docs/features/new-feature.md" --output "$PWD"
```

> **Why `$PWD`?** The `--directory` flag changes the working directory before running, so relative paths would resolve from the wrong location. Using `$PWD` converts your paths to absolute before the directory switch.

### Command-Line Options

```
issues-sync [-h] [-o DIR] {pull,create,epic} ...

Options:
  -h, --help          Show help message
  -o, --output DIR    Output directory for .github/issues/ folder
                      (default: current directory)

Commands:
  pull                Pull all issues from GitHub
  create <file.md>    Create issue from markdown file
  epic <file.md>      Create epic with child issues
```

---

## Alternative: pip Installation

If you prefer pip:

```bash
pip install -e .
issues-sync pull
```

---

## Repository Contents

```
issues-sync/
├── pyproject.toml                    # Project configuration & dependencies
├── src/
│   └── issues_sync/
│       ├── __init__.py
│       └── sync.py                   # Main sync script
├── tests/
│   └── test_sync.py                  # Unit tests
├── README.md                         # Documentation (this file)
```

---

## Usage

### Pull All Issues from GitHub

Sync all issues (open and closed) from your GitHub repository to local folders:

```bash
uv run issues-sync pull
```

This creates the following structure:
```
.github/issues/
├── issue-0001/
│   └── issue-0001.md
├── issue-0002/
│   └── issue-0002.md
└── issue-0003/
    └── issue-0003.md
```

Each markdown file contains:
- YAML frontmatter with issue metadata (number, title, state, labels, assignees, etc.)
- Original issue description
- A section for your implementation notes

### Create a Single Issue

Create a new GitHub issue from a markdown file:

```bash
uv run issues-sync create path/to/issue.md
```

The markdown file should use this format:

```markdown
---
title: Add user authentication system
labels: 
  - enhancement
  - backend
assignees: 
  - "@me"
milestone: "v1.0"
---

## Overview

Your issue description here...

## Requirements

- Requirement 1
- Requirement 2
```

### Create an Epic with Child Issues

Create an epic issue along with multiple child issues from a single file:

```bash
uv run issues-sync epic path/to/epic.md
```

The epic file format uses `---` separators between issues:

```markdown
---
title: "Epic: Implement Feature X"
labels:
  - epic
  - high-priority
---

Epic description here...

---

---
title: "Task: Setup backend"
labels:
  - backend
  - task
---

First child issue description...

---

---
title: "Task: Create frontend"
labels:
  - frontend
  - task
---

Second child issue description...
```

## Features

### Current Features

- ✅ Pull all issues from GitHub to local folders
- ✅ Sync issue comments with author and timestamp
- ✅ Create issues from markdown files with YAML frontmatter
- ✅ Create epics with multiple child issues
- ✅ Preserve issue metadata (labels, assignees, milestones)
- ✅ Support both open and closed issues
- ✅ Automatically create issue folders with standardized naming

### Planned Features

- 🔄 Two-way sync (update GitHub from local changes)
- 📎 Download and store issue attachments
- 🔗 Auto-link related issues
- 📋 Issue templates support

## YAML Frontmatter Options

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `title` | string | Issue title (required) | `"Fix login bug"` |
| `labels` | list | Issue labels | `["bug", "high-priority"]` |
| `assignees` | list | GitHub usernames | `["@me", "teammate"]` |
| `milestone` | string | Milestone name | `"v1.0"` |

## Issue Folder Structure

After pulling issues, each issue gets its own folder:

```
.github/issues/issue-0042/
├── issue-0042.md           # Main issue file with metadata
├── implementation.md       # Your implementation notes (manual)
├── research.md            # Research findings (manual)
└── artifacts/             # Related files (manual)
    ├── diagram.png
    └── test-results.json
```

## Best Practices

1. **Regular Syncing**: Run `pull` regularly to keep local issues up-to-date
2. **Documentation**: Add implementation notes directly in issue folders
3. **Commit History**: Commit issue folders to track decision history
4. **Issue Templates**: Create reusable templates for common issue types
5. **Bulk Operations**: Use epic files for related issues that should be created together

## Examples

### Example 1: Pull and Document

```bash
# Pull latest issues
uv run issues-sync pull

# Add your notes to an issue
echo "## Solution\nImplemented using strategy pattern" >> .github/issues/issue-0042/implementation.md

# Commit your documentation
git add .github/issues/issue-0042/
git commit -m "docs: add implementation notes for issue #42"
```

### Example 2: Create Feature Request

Create `feature.md`:
```markdown
---
title: Add dark mode support
labels:
  - enhancement
  - ui
assignees:
  - "@me"
milestone: "v2.0"
---

Users have requested a dark mode option for better viewing at night.
```

Then run:
```bash
uv run issues-sync create feature.md
```

### Example 3: Create Sprint Backlog

Create `sprint-23.md`:
```markdown
---
title: "Sprint 23 Planning"
labels:
  - epic
  - planning
---

Sprint 23 goals and tasks

---

---
title: "Fix navigation bug"
labels:
  - bug
  - sprint-23
---

Navigation menu doesn't close on mobile

---

---
title: "Update user documentation"
labels:
  - documentation
  - sprint-23
---

Update docs for new features
```

Then run:
```bash
uv run issues-sync epic sprint-23.md
```

## Troubleshooting

### Issue: `gh: command not found`
**Solution**: Install GitHub CLI from https://cli.github.com

### Issue: `uv: command not found`
**Solution**: Install uv from https://docs.astral.sh/uv/getting-started/installation/

### Issue: `gh auth status` shows not authenticated
**Solution**: Run `gh auth login` and follow the prompts

### Issue: Script creates issues in wrong repository
**Solution**: Ensure you're in the correct repository directory, or use `gh repo set-default`

## Contributing

When adding features to this tool:
1. Keep the code simple and focused
2. Add tests to the `tests/` folder
3. Update this README with new functionality
4. Run `uv run pytest` before committing

## License

This script is part of the project repository and follows the same license.

## Related Scripts

- `scripts/github/issues-create-epic/` - Specialized epic creation
- `scripts/linked-in/job-export-parser/` - LinkedIn job posting parser
