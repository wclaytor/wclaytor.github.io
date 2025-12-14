# GitHub Scripts Collection

A collection of Python scripts for managing GitHub resources locally.

## Available Scripts

### 1. Issues Sync (`issues-sync/`)
Synchronizes GitHub issues to local markdown documentation.

**Usage:**
```bash
python scripts/github/issues-sync/issues-sync.py pull
python scripts/github/issues-sync/issues-sync.py create issue.md
python scripts/github/issues-sync/issues-sync.py epic epic.md
```

**Features:**
- Pull all issues (open and closed)
- Create issues from markdown files
- Create epics with child issues
- YAML frontmatter support

**Documentation:** See `issues-sync/README.md`

### 2. Pull Requests Sync (`pull-requests-sync/`)
Synchronizes GitHub pull requests to local markdown documentation.

**Usage:**
```bash
python scripts/github/pull-requests-sync/pull-requests-sync.py pull
python scripts/github/pull-requests-sync/pull-requests-sync.py pull 69
python scripts/github/pull-requests-sync/pull-requests-sync.py summary
```

**Features:**
- Pull all PRs (open, closed, draft, merged)
- Pull individual PRs by number
- Display PR summary and statistics
- Save changed files list for each PR
- Include review comments

**Documentation:** See `pull-requests-sync/README.md`

## Comparison

| Feature | Issues Sync | PRs Sync |
|---------|-------------|----------|
| **Pull all from GitHub** | ✅ | ✅ |
| **Pull single item** | ❌ | ✅ |
| **Create on GitHub** | ✅ (single & epic) | ❌ (planned) |
| **YAML frontmatter** | ✅ | ✅ |
| **Changed files list** | ❌ | ✅ |
| **Review comments** | ❌ | ✅ |
| **Summary view** | ❌ | ✅ |
| **Status tracking** | ✅ | ✅ |

## Workflow Examples

### Document Complete Feature Development

```bash
# 1. Create issue from template
python scripts/github/issues-sync/issues-sync.py create feature.md

# 2. Pull the created issue
python scripts/github/issues-sync/issues-sync.py pull

# 3. During development, add notes to the issue folder
echo "## Implementation Notes" >> .github/issues/issue-XXXX/implementation.md

# 4. After PR is created, sync it
python scripts/github/pull-requests-sync/pull-requests-sync.py pull

# 5. Add PR review notes
echo "## Review Feedback" >> .github/pull-requests/pr-YYYY/review-notes.md

# 6. Commit all documentation together
git add .github/
git commit -m "docs: document feature implementation and review"
```

### Sprint Retrospective

```bash
# Pull all issues and PRs
python scripts/github/issues-sync/issues-sync.py pull
python scripts/github/pull-requests-sync/pull-requests-sync.py pull

# View PR summary
python scripts/github/pull-requests-sync/pull-requests-sync.py summary

# Search across all documentation
grep -r "performance" .github/issues/
grep -r "accessibility" .github/pull-requests/

# Find all sprint-2 related work
grep -l "sprint-2" .github/issues/*/issue-*.md
grep -l "sprint-2" .github/pull-requests/*/pr-*.md
```

### New Team Member Onboarding

```bash
# Sync all project history
python scripts/github/issues-sync/issues-sync.py pull
python scripts/github/pull-requests-sync/pull-requests-sync.py pull

# New team member can now browse:
ls -la .github/issues/        # All issues with context
ls -la .github/pull-requests/ # All PRs with reviews

# Search for specific topics
grep -r "architecture" .github/
grep -r "database" .github/
```

## Directory Structure

```
.github/
├── issues/
│   ├── issue-0001/
│   │   ├── issue-0001.md
│   │   ├── implementation.md (manual)
│   │   └── research.md (manual)
│   └── issue-0002/
│       └── issue-0002.md
└── pull-requests/
    ├── pr-0001/
    │   ├── pr-0001.md
    │   ├── changed-files.txt
    │   └── review-summary.md (manual)
    └── pr-0069/
        ├── pr-0069.md
        └── changed-files.txt
```

## Prerequisites

All scripts require:
- Python 3.6+
- GitHub CLI (`gh`) installed and authenticated
- PyYAML: `pip install pyyaml`

## Installation

```bash
# Authenticate with GitHub CLI
gh auth login

# Install Python dependencies
pip install pyyaml

# Make scripts executable (optional)
chmod +x scripts/github/issues-sync/issues-sync.py
chmod +x scripts/github/pull-requests-sync/pull-requests-sync.py
```

## Best Practices

1. **Regular Syncing**: Run sync scripts regularly to keep documentation current
2. **Commit Documentation**: Commit `.github/` changes to track evolution
3. **Add Context**: Enhance synced docs with implementation notes and decisions
4. **Cross-Reference**: Link between issues and PRs in your notes
5. **Search History**: Use grep/find to discover patterns and past decisions

## Testing

Each script includes a test suite:

```bash
# Test issues sync
./scripts/github/issues-sync/test-sync.sh

# Test PR sync
./scripts/github/pull-requests-sync/test-sync.sh
```

## Future Enhancements

### Issues Sync
- [ ] Two-way sync (update GitHub from local changes)
- [ ] Sync issue comments with threading
- [ ] Download issue attachments
- [ ] Issue templates support

### Pull Requests Sync
- [ ] Two-way sync (update PR from local changes)
- [ ] Sync all PR review comments with threading
- [ ] Download PR attachments
- [ ] Generate PR analytics reports
- [ ] Create PRs from local markdown (like issues)

## Contributing

Contributions welcome! When adding new scripts or features:

1. Follow existing patterns and structure
2. Include comprehensive README documentation
3. Add example files in `examples/` directory
4. Create test script for validation
5. Update this main README

## License

These scripts are part of the project repository and follow the same license.
