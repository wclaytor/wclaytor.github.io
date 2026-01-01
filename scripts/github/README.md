# GitHub Scripts Collection

A collection of Python scripts for managing GitHub resources locally. All scripts use [uv](https://docs.astral.sh/uv/) for dependency management with PEP 735 dependency groups.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) - Modern Python package manager
- GitHub CLI (`gh`) installed and authenticated

## Available Scripts

### 1. Issues Sync (`issues-sync/`)
Synchronizes GitHub issues to local markdown documentation.

**Usage:**
```bash
cd scripts/github/issues-sync
uv run issues-sync pull
uv run issues-sync create issue.md
```

**Features:**
- Pull all issues (open and closed)
- Create issues from markdown files
- YAML frontmatter support

**Documentation:** See [issues-sync/README.md](issues-sync/README.md)

### 2. Issues Create Epic (`issues-create-epic/`)
Creates GitHub epics and child issues from structured markdown with YAML frontmatter.

**Usage:**
```bash
cd scripts/github/issues-create-epic
uv run issues-create-epic epic.md --dry-run  # Preview
uv run issues-create-epic epic.md            # Create issues
```

**Features:**
- Smart label management (auto-creates if needed)
- Epic & issue linking with dependencies
- Priority, story points, and sprint tracking
- Dry run mode for previewing changes
- Verbose logging for debugging

**Documentation:** See [issues-create-epic/README.md](issues-create-epic/README.md)

### 3. Pull Requests Sync (`pull-requests-sync/`)
Synchronizes GitHub pull requests to local markdown documentation.

**Usage:**
```bash
cd scripts/github/pull-requests-sync
uv run pull-requests-sync pull
uv run pull-requests-sync pull 69
uv run pull-requests-sync summary
```

**Features:**
- Pull all PRs (open, closed, draft, merged)
- Pull individual PRs by number
- Display PR summary and statistics
- Save changed files list for each PR
- Include review comments

**Documentation:** See [pull-requests-sync/README.md](pull-requests-sync/README.md)

## Feature Comparison

| Feature | Issues Sync | Issues Create Epic | PRs Sync |
|---------|-------------|-------------------|----------|
| **Pull from GitHub** | ✅ All issues | ❌ | ✅ All/single PR |
| **Create on GitHub** | ✅ Single issue | ✅ Epics + children | ❌ (planned) |
| **YAML frontmatter** | ✅ | ✅ | ✅ |
| **Dry run mode** | ❌ | ✅ | ❌ |
| **Label management** | ❌ | ✅ Auto-create | ❌ |
| **Changed files list** | ❌ | ❌ | ✅ |
| **Summary view** | ❌ | ❌ | ✅ |

## Running from Repository Root

All scripts support running from the repo root using uv's `--directory` flag:

```bash
# Issues sync - pull all issues to repo root
uv run --directory ./scripts/github/issues-sync \
  issues-sync pull --output "$PWD"

# Issues create epic - create issues from a file
uv run --directory ./scripts/github/issues-create-epic \
  issues-create-epic "$PWD/docs/features/epic.md" --dry-run

# Pull requests sync - pull all PRs to repo root
uv run --directory ./scripts/github/pull-requests-sync \
  pull-requests-sync -o "$PWD" pull
```

> **Why `$PWD`?** The `--directory` flag changes the working directory before running, so relative paths would resolve from the wrong location. Using `$PWD` converts your paths to absolute before the directory switch.

## Workflow Examples

### Document Complete Feature Development

```bash
# 1. Create epic with child issues (preview first)
uv run --directory ./scripts/github/issues-create-epic \
  issues-create-epic "$PWD/docs/features/feature.md" --dry-run

# 2. Create the actual issues
uv run --directory ./scripts/github/issues-create-epic \
  issues-create-epic "$PWD/docs/features/feature.md"

# 3. Pull the created issues locally
uv run --directory ./scripts/github/issues-sync \
  issues-sync pull --output "$PWD"

# 4. During development, add notes to the issue folder
echo "## Implementation Notes" >> .github/issues/issue-XXXX/implementation.md

# 5. After PR is created, sync it
uv run --directory ./scripts/github/pull-requests-sync \
  pull-requests-sync -o "$PWD" pull

# 6. Commit all documentation together
git add .github/
git commit -m "docs: document feature implementation and review"
```

### Sprint Retrospective

```bash
# Pull all issues and PRs
uv run --directory ./scripts/github/issues-sync \
  issues-sync pull --output "$PWD"
uv run --directory ./scripts/github/pull-requests-sync \
  pull-requests-sync -o "$PWD" pull

# View PR summary
uv run --directory ./scripts/github/pull-requests-sync \
  pull-requests-sync -o "$PWD" summary

# Search across all documentation
grep -r "performance" .github/issues/
grep -r "accessibility" .github/pull-requests/
```

### New Team Member Onboarding

```bash
# Sync all project history
uv run --directory ./scripts/github/issues-sync \
  issues-sync pull --output "$PWD"
uv run --directory ./scripts/github/pull-requests-sync \
  pull-requests-sync -o "$PWD" pull

# Browse locally:
ls -la .github/issues/        # All issues with context
ls -la .github/pull-requests/ # All PRs with reviews

# Search for specific topics
grep -r "architecture" .github/
grep -r "database" .github/
```

## Directory Structure

```
scripts/github/
├── README.md                    # This file
├── issues-sync/
│   ├── pyproject.toml          # uv project config
│   ├── README.md
│   ├── src/issues_sync/
│   │   ├── __init__.py
│   │   └── sync.py
│   └── tests/
├── issues-create-epic/
│   ├── pyproject.toml          # uv project config
│   ├── README.md
│   ├── epic-template.md
│   ├── test-epic.md
│   ├── src/issues_create_epic/
│   │   ├── __init__.py
│   │   └── create_epic.py
│   └── tests/
└── pull-requests-sync/
    ├── pyproject.toml          # uv project config
    ├── README.md
    ├── examples/
    ├── src/pull_requests_sync/
    │   ├── __init__.py
    │   └── sync.py
    └── tests/
```

Output structure created by sync scripts:
```
.github/
├── issues/
│   ├── issue-0001/
│   │   ├── issue-0001.md
│   │   └── implementation.md (manual notes)
│   └── issue-0002/
│       └── issue-0002.md
└── pull-requests/
    ├── pr-0001/
    │   ├── pr-0001.md
    │   └── changed-files.txt
    └── pr-0069/
        ├── pr-0069.md
        └── changed-files.txt
```

## Installation

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Authenticate with GitHub CLI
gh auth login

# That's it! uv handles dependencies automatically when you run scripts
```

No need to manually create virtual environments or install dependencies—uv handles everything automatically based on each script's `pyproject.toml`.

## Best Practices

1. **Regular Syncing**: Run sync scripts regularly to keep documentation current
2. **Commit Documentation**: Commit `.github/` changes to track evolution
3. **Add Context**: Enhance synced docs with implementation notes and decisions
4. **Cross-Reference**: Link between issues and PRs in your notes
5. **Search History**: Use grep/find to discover patterns and past decisions

## Testing

Each script includes a pytest test suite:

```bash
# Test issues sync
cd scripts/github/issues-sync && uv run pytest

# Test issues create epic
cd scripts/github/issues-create-epic && uv run pytest

# Test PR sync
cd scripts/github/pull-requests-sync && uv run pytest
```

## Future Enhancements

### Issues Sync
- [ ] Two-way sync (update GitHub from local changes)
- [ ] Sync issue comments with threading
- [ ] Download issue attachments

### Issues Create Epic
- [ ] Update existing epics with new child issues
- [ ] Interactive mode for issue creation
- [ ] Template library support

### Pull Requests Sync
- [ ] Two-way sync (update PR from local changes)
- [ ] Sync all PR review comments with threading
- [ ] Download PR attachments
- [ ] Generate PR analytics reports
- [ ] Create PRs from local markdown

## Contributing

Contributions welcome! When adding new scripts or features:

1. Follow the existing uv-based project structure
2. Include a `pyproject.toml` with proper dependency groups
3. Add comprehensive README documentation
4. Include pytest tests in `tests/` directory
5. Update this main README

## Related Documentation

- [pip to uv Migration Guide](../../docs/uv/pip-to-uv-migration-guide.md) - How these scripts were migrated
- [Dependency Groups](../../docs/uv/dependency-groups.md) - Pattern used for dev dependencies

## License

These scripts are part of the project repository and follow the same license.
