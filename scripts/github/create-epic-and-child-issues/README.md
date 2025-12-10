# create-epic-and-child-issues.py

A Python script that creates a GitHub epic issue and multiple related child issues based on the BOFH site review findings.

## Features

- 🔥 Creates an epic issue with comprehensive tracking
- 📋 Creates 10 child issues with proper labels and priorities
- 🏷️ Automatically creates/ensures all necessary labels exist
- 🎨 Color-codes labels for easy visual identification
- 🔍 Dry-run mode for testing before execution
- ✅ Summary report of created issues

## Prerequisites

1. **GitHub CLI (gh)** must be installed and authenticated:
   ```bash
   # Install gh (if not already installed)
   # On Ubuntu/Debian:
   sudo apt install gh
   
   # On macOS:
   brew install gh
   
   # Authenticate
   gh auth login
   ```

2. **Python 3.10+** (uses modern type hints)

3. **Repository access**: Must be run from within the repository or have proper git remote configured

## Usage

```bash
# Dry run (recommended first)
python scripts/github/create-epic-and-child-issues.py --dry-run

# Actually create the issues
python scripts/github/create-epic-and-child-issues.py
```

## What It Creates

**Epic Issue:**
- Title: "Epic: BOFH Site Improvements 🔥"
- Labels: `epic`, `enhancement`, `technical-debt`
- Contains overview, implementation order, and success metrics

**Child Issues (10):**
1. **fix: Add missing meta description, author, and SEO tags** (priority-high, quick-win)
2. **feat: Add Open Graph and Twitter Card meta tags** (priority-high)
3. **fix: Correct email link href/display mismatch** (priority-critical, bug)
4. **feat: Create Open Graph image for social sharing** (priority-medium)
5. **fix: Correct copyright date format in footer** (priority-low, quick-win)
6. **feat: Add compelling tagline to masthead** (priority-medium, content)
7. **chore: Remove unused sb-forms-latest.js script** (priority-medium, quick-win)
8. **security: Add integrity attributes to external CDN scripts** (priority-medium)
9. **chore: Evaluate self-hosting vs CDN for critical assets** (priority-low)
10. **chore: Run comprehensive Lighthouse audit** (priority-medium, quality)

## Labels Created

The script automatically creates/ensures these labels exist:

| Label | Color | Usage |
|-------|-------|-------|
| `epic` | Purple | Epic tracking issues |
| `enhancement` | Light blue | New features |
| `technical-debt` | Light purple | Code quality improvements |
| `seo` | Green | SEO-related issues |
| `quick-win` | Light blue | Easy, high-impact tasks |
| `priority-critical` | Red | Must fix immediately |
| `priority-high` | Orange | Fix soon |
| `priority-medium` | Yellow | Normal priority |
| `priority-low` | Green | Nice to have |
| `bug` | Red | Something broken |
| `content` | Teal | Content changes |
| `performance` | Purple | Performance improvements |
| `security` | Red | Security issues |
| `reliability` | Dark teal | Stability improvements |
| `quality` | Blue | Quality assurance |
| `testing` | Light blue | Testing-related |
| `design` | Light purple | Design changes |

## Dry Run Mode

Always test with `--dry-run` first:

```bash
python scripts/github/create-epic-and-child-issues.py --dry-run
```

This will:
- Show what commands would be executed
- Display issue titles and labels
- Preview body content (first 200 characters)
- Not create any actual issues

## Example Output

```
🔥 BOFH Epic Issue Creator 🔥

============================================================
This script will create:
  - 1 Epic issue
  - 10 child issues
============================================================

Proceed? (y/N): y

============================================================
Checking/creating labels...
✅ Label 'epic' ready
✅ Label 'enhancement' ready
...

============================================================
Creating issue: Epic: BOFH Site Improvements 🔥
Labels: epic, enhancement, technical-debt
✅ Created: https://github.com/wclaytor/wclaytor.github.io/issues/1

============================================================
Creating issue: fix: Add missing meta description, author, and SEO tags
Labels: seo, quick-win, priority-high
✅ Created: https://github.com/wclaytor/wclaytor.github.io/issues/2

...

============================================================
📊 SUMMARY
============================================================

✅ Epic created: https://github.com/wclaytor/wclaytor.github.io/issues/1

✅ Created 10 child issues:
   - fix: Add missing meta description, author, and SEO tags
     https://github.com/wclaytor/wclaytor.github.io/issues/2
   ...

============================================================
🔥 BOFH EPIC CREATION COMPLETE 🔥
Now go fix those issues before the BOFH notices...
```

## Customization

To customize the issues:

1. Edit the `CHILD_ISSUES` list in the script
2. Modify issue titles, bodies, labels, or priorities
3. Update the `EPIC_BODY` for the epic description
4. Add or change labels in the `label_colors` dictionary

## Error Handling

If issue creation fails:
- Check that `gh` is authenticated: `gh auth status`
- Verify repository access: `gh repo view`
- Check for network connectivity
- Review error messages in the output

## References

- Based on: [BOFH Site Review](/assets/docs/reviews/bofh-site-review.md)
- Uses: [GitHub CLI](https://cli.github.com/)
- Epic methodology: [Epic Issues in GitHub](https://docs.github.com/en/issues/tracking-your-work-with-issues)

## Contributing

When adding new scripts:

1. Follow the same structure and documentation style
2. Include dry-run mode for destructive operations
3. Add comprehensive docstrings
4. Update this README with usage instructions
5. Use type hints for better code clarity

## License

These scripts are part of the wclaytor.github.io repository and follow the same license.
