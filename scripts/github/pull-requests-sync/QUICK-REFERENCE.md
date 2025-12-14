# Pull Requests Sync - Quick Reference

## 🚀 Quick Start

```bash
# Pull all PRs from GitHub
python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Pull specific PR
python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull 69

# Show summary
python3 scripts/github/pull-requests-sync/pull-requests-sync.py summary
```

## 📁 What Gets Created

```
.github/pull-requests/
└── pr-0069/
    ├── pr-0069.md              # Full PR details with frontmatter
    └── changed-files.txt       # List of modified files
```

## 📝 PR Markdown Structure

Each `pr-XXXX.md` file contains:

1. **YAML Frontmatter** - All metadata (number, title, state, author, labels, etc.)
2. **Status Header** - Visual status with branch info and change stats
3. **Description** - Original PR description
4. **Latest Reviews** - Most recent review comments
5. **Implementation Notes** - Empty section for your notes
6. **Testing Notes** - Empty section for test documentation
7. **Review Notes** - Empty section for review feedback

## 🎯 Common Use Cases

### Document PR Review
```bash
# Pull the PR
python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull 69

# Add your review notes
cat >> .github/pull-requests/pr-0069/pr-0069.md << 'EOF'

### Review Comments
- Excellent Alpine.js patterns
- Consider extracting reusable component
- Add unit tests for edge cases
EOF

# Commit
git add .github/pull-requests/pr-0069/
git commit -m "docs: add review notes for PR #69"
```

### Find PRs That Modified Specific Files
```bash
# Pull all PRs
python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Search for PRs that modified index.html
grep -l "index.html" .github/pull-requests/*/changed-files.txt

# Output shows which PR folders contain that file
```

### Track Feature Development History
```bash
# Pull all PRs
python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Search for feature-related PRs
grep -r "collapsible" .github/pull-requests/*/pr-*.md

# Review implementation decisions
grep -A 5 "Implementation Notes" .github/pull-requests/pr-0069/pr-0069.md
```

### Generate Sprint Report
```bash
# Pull all PRs
python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Get summary
python3 scripts/github/pull-requests-sync/pull-requests-sync.py summary

# Find sprint-specific PRs
grep -l "sprint-2" .github/pull-requests/*/pr-*.md

# Count merged vs open
grep -c "status: MERGED" .github/pull-requests/*/pr-*.md
grep -c "status: OPEN" .github/pull-requests/*/pr-*.md
```

## 📊 Status Indicators

| Emoji | Status | Description |
|-------|--------|-------------|
| ✅ | MERGED | PR successfully merged |
| 📝 | OPEN | PR open and ready for review |
| 🚧 | DRAFT | PR in draft/WIP state |
| ❌ | CLOSED | PR closed without merging |

## 🔍 Frontmatter Fields Reference

```yaml
pr_number: 69                    # PR number
title: "Feature name"            # PR title
state: OPEN                      # GitHub state (OPEN/CLOSED)
status: DRAFT                    # Detailed status
is_draft: true                   # Draft flag
created_at: '2025-11-12T...'    # Creation timestamp
updated_at: '2025-11-12T...'    # Last update
closed_at: null                  # Close timestamp
merged_at: null                  # Merge timestamp
author: copilot-swe-agent        # Author username
labels: [enhancement]            # PR labels
assignees: [wclaytor]           # Assignees
milestone: "Sprint 2"            # Milestone
head_ref: feature/branch         # Source branch
base_ref: main                   # Target branch
additions: 1678                  # Lines added
deletions: 4                     # Lines deleted
changed_files: 5                 # Files changed
review_decision: APPROVED        # Review status
url: https://github.com/...      # PR URL
```

## 🛠️ Advanced Usage

### Sync on Schedule (Cron)
```bash
# Add to crontab to sync daily at 9am
0 9 * * * cd /path/to/repo && python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull
```

### Combine with Issues Sync
```bash
# Sync both issues and PRs
python3 scripts/github/issues-sync/issues-sync.py pull
python3 scripts/github/pull-requests-sync/pull-requests-sync.py pull

# Now search across both
grep -r "authentication" .github/
```

### Generate Markdown Report
```bash
# Create a report of all merged PRs
echo "# Merged PRs" > pr-report.md
find .github/pull-requests -name "pr-*.md" -exec grep -l "status: MERGED" {} \; | while read file; do
    title=$(grep "^title:" "$file" | cut -d: -f2-)
    echo "- $title" >> pr-report.md
done
```

## 🧪 Testing

Run the test suite:
```bash
./scripts/github/pull-requests-sync/test-sync.sh
```

## 💡 Tips

1. **Pull regularly** - Keep local docs in sync with GitHub
2. **Add notes inline** - Enhance the generated markdown with your insights
3. **Commit documentation** - Track your notes in git for history
4. **Search often** - Use grep/find to discover patterns
5. **Cross-reference** - Link between PRs and issues in your notes
6. **Review changed files** - Use changed-files.txt to understand impact

## 🆘 Troubleshooting

**Issue**: Permission denied
```bash
chmod +x scripts/github/pull-requests-sync/pull-requests-sync.py
```

**Issue**: gh not found
```bash
# Install GitHub CLI
# macOS: brew install gh
# Linux: See https://cli.github.com
gh auth login
```

**Issue**: Module 'yaml' not found
```bash
pip install pyyaml
```

**Issue**: No PRs found
```bash
# Check you're in correct repo
gh repo view

# Verify authentication
gh auth status
```

## 📚 See Also

- Full Documentation: `scripts/github/pull-requests-sync/README.md`
- Issues Sync: `scripts/github/issues-sync/README.md`
- GitHub Scripts Overview: `scripts/github/README.md`
