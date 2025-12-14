# GitHub PR Comment Tool

Add developer notes or comments to GitHub pull requests directly from the command line.

## Features

- 🤖 **Auto-detect PR**: Automatically finds the PR for your current branch
- 📝 **Auto-find notes**: Automatically uses the latest developer note from `docs/notes/`
- 🎨 **Formatted output**: Wraps notes in collapsible sections for clean PR comments
- 🔧 **Flexible**: Supports manual PR number and file path specification
- 📦 **Raw mode**: Post notes without formatting

## Prerequisites

- [GitHub CLI (`gh`)](https://cli.github.com/) installed and authenticated
- Python 3.6+

## Installation

The script is ready to use. Make it executable:

```bash
chmod +x scripts/github/pull-requests-comment/pr-add-note.py
```

## Usage

### Basic Usage

From a branch with an active PR, add the latest developer note:

```bash
./scripts/github/pull-requests-comment/pr-add-note.py
```

This will:
1. Find the PR for your current branch
2. Locate the most recent `developer.md` file in `docs/notes/`
3. Format it as a collapsible comment
4. Post it to the PR

### Specify a Note File

Add a specific note file to the current PR:

```bash
./scripts/github/pull-requests-comment/pr-add-note.py path/to/note.md
```

### Specify PR Number

Add a note to a specific PR:

```bash
./scripts/github/pull-requests-comment/pr-add-note.py --pr 45
```

### Specify Both

Add a specific note to a specific PR:

```bash
./scripts/github/pull-requests-comment/pr-add-note.py path/to/note.md --pr 45
```

### Raw Mode

Post the note without formatting or collapsible section:

```bash
./scripts/github/pull-requests-comment/pr-add-note.py --raw
```

### Different Repository

Add a note to a PR in a different repository:

```bash
./scripts/github/pull-requests-comment/pr-add-note.py --pr 45 --repo owner/repo
```

### Custom Notes Directory

Search for notes in a different directory:

```bash
./scripts/github/pull-requests-comment/pr-add-note.py --notes-dir path/to/notes
```

## Command-Line Options

```
positional arguments:
  file                  Path to developer note file (markdown).
                       If not specified, uses latest note from docs/notes

optional arguments:
  -h, --help           Show this help message and exit
  --pr PR              PR number to comment on.
                       If not specified, uses current branch PR
  --repo REPO          GitHub repo (owner/repo).
                       If not specified, uses current repo
  --raw                Post raw note without formatting or collapsible section
  --notes-dir DIR      Directory to search for notes (default: docs/notes)
```

## Examples

### Example 1: Quick Comment

You've just finished working on PR #45 and created a developer note. Add it to the PR:

```bash
# From the PR branch
./scripts/github/pull-requests-comment/pr-add-note.py
```

Output:
```
📝 GitHub PR Comment Tool
============================================================

🔍 Looking for PR for current branch...
✓ Found PR #45
🔍 Looking for latest developer note...
✓ Found note: docs/notes/2025/12/2025.12.06/developer.md
📖 Reading note from docs/notes/2025/12/2025.12.06/developer.md...
💬 Adding comment to PR #45...

============================================================
✅ Successfully added comment to PR #45
🔗 View PR: https://github.com/wclaytor/william-claytor/pull/45
============================================================
```

### Example 2: Add Specific Note to Different PR

```bash
./scripts/github/pull-requests-comment/pr-add-note.py docs/notes/2025/12/2025.12.05/developer.md --pr 42
```

### Example 3: Raw Note for Another Repo

```bash
./scripts/github/pull-requests-comment/pr-add-note.py note.md --pr 10 --repo another-user/another-repo --raw
```

## Output Format

By default, the script formats notes as collapsible sections in PR comments:

```markdown
## 📝 [Note Title]

<details>
<summary>Click to expand developer notes</summary>

[Your note content]

</details>

---
*Added via pr-add-note.py on 2025-12-07 10:30:00*
```

This keeps PR conversations clean while preserving detailed technical notes.

## Integration with Workflow

### Typical Workflow

1. Work on a feature in a PR branch
2. Create developer notes in `docs/notes/YYYY/MM/YYYY.MM.DD/developer.md`
3. Run `./scripts/github/pull-requests-comment/pr-add-note.py` to add notes to PR
4. Push changes

### Automation

You can integrate this into your git workflow:

```bash
# Add to .git/hooks/pre-push or a custom script
#!/bin/bash

# Check if there are new notes
if [[ -f "docs/notes/$(date +%Y/%m/%Y.%m.%d)/developer.md" ]]; then
    echo "Adding developer notes to PR..."
    ./scripts/github/pull-requests-comment/pr-add-note.py
fi
```

## Note File Discovery

The script looks for developer notes in this order:

1. If a file path is provided as an argument, use that file
2. Otherwise, search `docs/notes/` (or `--notes-dir`) for all `developer.md` files
3. Sort by modification time (most recent first)
4. Use the most recently modified note

This means the script will automatically use your latest work without manual specification.

## Error Handling

The script provides clear error messages:

- **No PR found**: Checkout a branch with a PR or use `--pr`
- **No note found**: Create a note in `docs/notes/` or specify a file path
- **File not found**: Check the file path
- **gh CLI error**: Ensure gh CLI is installed and authenticated

## Troubleshooting

### "No PR found for current branch"

**Solution**: Either checkout the PR branch or specify `--pr <number>`

```bash
# Checkout PR branch
gh pr checkout 45

# Or specify PR number
./pr-add-note.py --pr 45
```

### "No developer notes found"

**Solution**: Create a developer note or specify the file path

```bash
# Create a note first
mkdir -p docs/notes/$(date +%Y/%m/%Y.%m.%d)
vim docs/notes/$(date +%Y/%m/%Y.%m.%d)/developer.md

# Or specify existing file
./pr-add-note.py path/to/note.md
```

### "Error running gh command"

**Solution**: Install and authenticate GitHub CLI

```bash
# Install gh CLI (macOS)
brew install gh

# Install gh CLI (Linux)
sudo apt install gh

# Authenticate
gh auth login
```

## Related Scripts

- **`pull-requests-sync.py`**: Sync PR metadata to local `.github/pull-requests/` folders
- **`issues-sync.py`**: Manage GitHub issues locally

## Development

### Testing

Test the script without posting to GitHub:

```bash
# View what would be posted (dry run)
./pr-add-note.py --help
```

### Adding Features

The script is designed to be easily extensible. Key functions:

- `get_current_pr()`: Detect current PR
- `find_latest_note()`: Find most recent developer note
- `format_note_as_comment()`: Format note for PR comment
- `add_comment_to_pr()`: Post comment via gh CLI

## License

MIT License - See repository LICENSE.md

## Contributing

Contributions welcome! Please follow the project's contribution guidelines.

---

**Part of the william-claytor project workflow tools**
