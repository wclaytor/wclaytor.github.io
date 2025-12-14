# GitHub Epic & Issues Creator

## Overview

The `create-epic.py` script creates GitHub issues from structured markdown files with YAML frontmatter. It automatically handles label creation, issue linking, and epic management using the GitHub CLI (`gh`).

## Features

✨ **Smart Label Management**: Automatically creates labels if they don't exist  
🔗 **Epic & Issue Linking**: Creates epics with linked child issues  
📊 **Dependency Tracking**: References dependencies between issues  
🎯 **Priority & Sprint Management**: Tracks priority, story points, and sprint assignments  
🔍 **Dry Run Mode**: Preview changes before creating actual issues  
📝 **Verbose Logging**: Optional detailed output for debugging  
🏠 **Current Repo Support**: Works with current repository or specify any repo  

## Prerequisites

### 1. GitHub CLI (gh)

The script requires GitHub CLI to be installed and authenticated:

```bash
# Check if gh is installed
gh --version

# If not installed, see: https://cli.github.com/

# Authenticate with GitHub
gh auth login
```

**Note**: GitHub Codespaces come with `gh` pre-installed and authenticated.

### 2. Python 3

Python 3.6 or higher is required:

```bash
python3 --version
```

### 3. Python Dependencies

Install required packages:

```bash
pip install pyyaml
```

## Quick Start

### 1. Preview (Dry Run)

Test your markdown file without creating issues:

```bash
# Using current repository
python3 scripts/github/issues-create-epic/create-epic.py test-epic.md --dry-run

# Or specify a repository
python3 scripts/github/issues-create-epic/create-epic.py test-epic.md --repo owner/repo --dry-run
```

### 2. Create Issues

Once satisfied with the preview, create the actual issues:

```bash
# Using current repository
python3 scripts/github/issues-create-epic/create-epic.py test-epic.md

# Or specify a repository
python3 scripts/github/issues-create-epic/create-epic.py test-epic.md --repo owner/repo
```

### 3. Verbose Mode

For detailed debugging information:

```bash
python3 scripts/github/issues-create-epic/create-epic.py test-epic.md --verbose
```

## Command Line Options

```
usage: create-epic.py [-h] [--repo REPO] [--dry-run] [-v] file

positional arguments:
  file         Path to markdown file with tickets

optional arguments:
  -h, --help   Show help message and exit
  --repo REPO  GitHub repo (owner/repo). If not specified, uses current repo.
  --dry-run    Preview without creating issues
  -v, --verbose Show detailed command output
```

## Input File Format

The script expects a markdown file with YAML frontmatter blocks. See `test-epic.md` for a complete example.

### Epic Frontmatter

Define the parent epic issue:

```yaml
---
epic:
  title: "Epic: Your Epic Title"
  labels: ["epic", "feature"]
  milestone: "Sprint 1"  # Optional
  description: |
    Epic description goes here.
    Can be multi-line.
    
    Success Criteria:
    - Criterion 1
    - Criterion 2
---
```

### Child Issue (Ticket) Frontmatter

Define child issues linked to the epic:

```yaml
---
ticket:
  id: TICKET-001
  title: Issue Title
  type: task
  priority: P1
  points: 3
  sprint: 1
  labels: ["feature", "backend"]
  assignee: "username"  # Optional, use GitHub username
  dependencies: ["TICKET-000"]  # Optional, references other ticket IDs
---

### TICKET-001: Issue Title

**Description:**
Detailed description of the issue.

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2

**Technical Notes:**
Additional implementation details.
```

### Complete Example Structure

```markdown
---
epic:
  title: "Epic: Feature Implementation"
  labels: ["epic"]
  description: |
    Description of the epic
---

# Feature Development Tickets

---
ticket:
  id: FEAT-001
  title: Backend API
  type: task
  priority: P1
  points: 5
  sprint: 1
  labels: ["backend"]
  assignee: ""
  dependencies: []
---

### FEAT-001: Backend API

Implementation details here...

---
ticket:
  id: FEAT-002
  title: Frontend UI
  type: task
  priority: P2
  points: 3
  sprint: 1
  labels: ["frontend"]
  assignee: ""
  dependencies: ["FEAT-001"]
---

### FEAT-002: Frontend UI

Implementation details here...
```

## Expected Output

### Successful Run

```
🔍 Verifying GitHub CLI installation and authentication...
✅ GitHub CLI verified and authenticated

============================================================
GitHub Epic & Issues Creator
============================================================

📖 Reading and parsing test-epic.md
  ✓ Found epic: Epic: Test Epic for Script Validation
  ✓ Found 2 ticket(s)

🎯 Creating Epic: Epic: Test Epic for Script Validation
  ✓ Created label: epic
  ✓ Created label: test
  ✅ Created Epic: #47
  🔗 URL: https://github.com/owner/repo/issues/47

📋 Creating 2 ticket(s)...

[1/2]
📝 Creating TEST-001: First Test Child Issue
  ✓ Created label: child-issue
  ✅ Created: #48

[2/2]
📝 Creating TEST-002: Second Test Child Issue
  ✅ Created: #49

🔄 Updating Epic #47 with ticket links...
  ✅ Updated epic with 2 ticket links

============================================================
✅ Summary
============================================================
  Epic: #47
  Tickets created: 2

  Created Issues:
    TEST-001 → #48
    TEST-002 → #49

  🔗 View Epic: https://github.com/<current-repo>/issues/47
============================================================
```

### Dry Run Output

```
============================================================
GitHub Epic & Issues Creator
============================================================

📖 Reading and parsing test-epic.md
  ✓ Found epic: Epic: Test Epic for Script Validation
  ✓ Found 2 ticket(s)

🎯 Creating Epic: Epic: Test Epic for Script Validation
  [DRY RUN] Would create epic with title: Epic: Test Epic for Script Validation

📋 Creating 2 ticket(s)...

[1/2]
📝 Creating TEST-001: First Test Child Issue
  [DRY RUN] Would create ticket TEST-001

[2/2]
📝 Creating TEST-002: Second Test Child Issue
  [DRY RUN] Would create ticket TEST-002

🔄 Updating Epic #999 with ticket links...
  [DRY RUN] Would update epic with 2 ticket links

============================================================
✅ Summary
============================================================
  Epic: Not created
  Tickets created: 2

  Created Issues:
    TEST-001 → #1000
    TEST-002 → #1001
============================================================
```

## What the Script Does

1. **Verifies Prerequisites**: Checks that `gh` CLI is installed and authenticated
2. **Loads Existing Labels**: Caches existing repository labels
3. **Parses Input File**: Extracts epic and ticket data from markdown with YAML frontmatter
4. **Creates Labels**: Automatically creates any missing labels
5. **Creates Epic Issue**: Creates the parent epic with description and metadata
6. **Creates Child Issues**: Creates linked child issues with:
   - Reference to parent epic
   - Type, priority, story points, sprint info
   - Dependencies (with issue numbers for already-created tickets)
   - Full markdown content
7. **Links Issues**: Adds comments linking child issues to the epic
8. **Updates Epic**: Updates the epic description with a checklist of all child issues
9. **Provides Summary**: Shows all created issues with their numbers

## Features Demonstrated

### Test File (`test-epic.md`)

The included test file demonstrates:

1. ✅ **Epic Creation**: Creates a parent epic issue
2. ✅ **Child Issue Creation**: Creates 2 linked child issues
3. ✅ **Automatic Label Creation**: Creates labels that don't exist
4. ✅ **Dependency Tracking**: TEST-002 depends on TEST-001
5. ✅ **Metadata Management**: Priority, points, sprint information
6. ✅ **Bi-directional Linking**: Epic links to children, children link to epic
7. ✅ **Issue Checklist**: Epic contains checklist of all child issues

## Verifying Created Issues

Use the GitHub CLI to inspect created issues:

```bash
# List recent issues
gh issue list --limit 10

# View the epic issue
gh issue view 47

# View in browser
gh issue view 47 --web

# View a child issue
gh issue view 48

# List issues with specific label
gh issue list --label test

# Search for issues
gh issue list --search "TEST-001"
```

## Troubleshooting

### ❌ "gh CLI is not authenticated"

**Solution**: 
```bash
gh auth login
```

### ❌ "gh CLI is not installed"

**Solution**: Install from https://cli.github.com/
```bash
# macOS
brew install gh

# Windows
winget install --id GitHub.cli

# Linux
# See https://github.com/cli/cli/blob/trunk/docs/install_linux.md
```

### ❌ "No module named 'yaml'"

**Solution**:
```bash
pip install pyyaml
```

### ❌ "File not found"

**Solution**: Verify the path to your markdown file is correct
```bash
# Use absolute or relative path
python3 scripts/github/issues-create-epic/create-epic.py ./test-epic.md
```

### ❌ Rate Limiting Errors

**Solution**: The script includes delays between issue creation. If you still hit rate limits, wait a few minutes and try again.

### 🐛 Script Errors

**Solution**: Use verbose mode to see detailed output
```bash
python3 scripts/github/issues-create-epic/create-epic.py test-epic.md --verbose
```

## Advanced Usage

### Working with Different Repositories

```bash
# Create issues in a different repository
python3 create-epic.py epic.md --repo owner/different-repo

# Preview for different repository
python3 create-epic.py epic.md --repo owner/different-repo --dry-run
```

### Creating Your Own Epic Files

1. Copy `test-epic.md` as a template
2. Update the epic frontmatter with your epic details
3. Update ticket frontmatters with your ticket details
4. Update ticket content with your implementation details
5. Run in dry-run mode to validate
6. Create the actual issues

### Best Practices

1. **Always dry-run first**: Validate your input file before creating issues
2. **Use descriptive ticket IDs**: Make them easy to reference (e.g., `AUTH-001`, `UI-002`)
3. **Organize by sprint**: Group tickets by sprint in your markdown file
4. **Include acceptance criteria**: Clear criteria make tickets actionable
5. **Set dependencies carefully**: Only add dependencies that truly block work
6. **Use consistent labels**: Establish label conventions for your team
7. **Version control your epic files**: Track changes to your planning documents

## Script Compatibility

- ✅ **Works with GitHub Codespaces**: Pre-installed `gh` CLI
- ✅ **Works with older gh versions**: Compatible with gh CLI versions that don't support `--json` on `issue create`
- ✅ **Works locally**: Install `gh` CLI and authenticate
- ✅ **Cross-platform**: Works on macOS, Linux, and Windows

## Improvements in Current Version

✨ **Recent enhancements**:

1. **Automatic Label Creation**: No need to manually create labels first
2. **Optional --repo Parameter**: Defaults to current repository
3. **Improved Logging**: Clean, informative output with progress indicators
4. **Better Error Messages**: Shows relevant errors without verbose help text
5. **Verbose Mode**: Optional detailed debugging output
6. **Compatibility**: Works with gh CLI versions in GitHub Codespaces
7. **Smart Caching**: Caches existing labels to avoid duplicate API calls

## Example Workflow

```bash
# 1. Create your epic markdown file
cp test-epic.md my-feature-epic.md
nano my-feature-epic.md  # Edit with your details

# 2. Validate with dry run
python3 scripts/github/issues-create-epic/create-epic.py my-feature-epic.md --dry-run

# 3. Create the issues
python3 scripts/github/issues-create-epic/create-epic.py my-feature-epic.md

# 4. View the epic
gh issue view <epic-number> --web

# 5. Track progress
gh issue list --milestone "Sprint 1"
```

## Getting Help

```bash
# Show help
python3 scripts/github/issues-create-epic/create-epic.py --help

# GitHub CLI help
gh issue create --help
gh issue list --help
gh issue view --help
```

## Additional Resources

- [GitHub CLI Manual](https://cli.github.com/manual/)
- [GitHub Issues Documentation](https://docs.github.com/en/issues)
- [gh-cli-issues.md](../../docs/github/gh-cli-issues.md) - Comprehensive gh CLI guide

---

**Pro Tip**: Keep your epic markdown files in version control alongside your code. This creates a historical record of your planning and makes it easy to recreate or update issues as needed.

## Prerequisites

1. **GitHub CLI (gh)**: Must be installed and authenticated
   ```bash
   # Install gh CLI (if not already installed)
   # See: https://cli.github.com/
   
   # Authenticate with GitHub
   gh auth login
   ```

2. **Python 3**: Required to run the script
   ```bash
   python3 --version  # Should be 3.6 or higher
   ```

3. **Required Python packages**: PyYAML
   ```bash
   pip install pyyaml
   ```

## Test Input File Format

The script expects a markdown file with YAML frontmatter blocks. See `test-epic.md` for a complete example.

### Epic Frontmatter

```yaml
---
epic:
  title: "Epic: Your Epic Title"
  labels: ["epic", "feature"]
  milestone: "Sprint 1"
  description: |
    Epic description goes here.
    Can be multi-line.
---
```

### Child Issue (Ticket) Frontmatter

```yaml
---
ticket:
  id: TICKET-001
  title: Issue Title
  type: task
  priority: P1
  points: 3
  sprint: 1
  labels: ["feature", "backend"]
  assignee: "username"
  dependencies: ["TICKET-000"]  # Optional, references other ticket IDs
---

### TICKET-001: Issue Title

**Description:**
Detailed description of the issue.

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
```

## Usage

### 1. Dry Run (Preview Mode)

Test your input file without creating actual issues:

```bash
python3 scripts/create-epic.py test-epic.md \
  --repo wclaytor/{REPO} \
    --dry-run
    ``````

Expected output:
```
📚 Parsing test-epic.md
🎯 Creating Epic: Epic: Test Epic for Script Validation
  [DRY RUN] Would create epic with title: Epic: Test Epic for Script Validation

📋 Creating 2 tickets...
📝 Creating TEST-001: First Test Child Issue
  [DRY RUN] Would create ticket TEST-001
  [DRY RUN] Would link #1000 to epic #999
📝 Creating TEST-002: Second Test Child Issue
  [DRY RUN] Would create ticket TEST-002
  [DRY RUN] Would link #1001 to epic #999
🔄 Updating Epic #999 with ticket links...
  [DRY RUN] Would update epic with ticket links

✅ Summary:
  - Epic: #999
  - Tickets created: 2
```

### 2. Create Actual Issues

Once satisfied with the dry run, create real issues:

```bash
python3 scripts/create-epic.py test-epic.md \
  --repo wclaytor/{REPO}
```

Expected output:
```
📚 Parsing test-epic.md
🎯 Creating Epic: Epic: Test Epic for Script Validation
  ✅ Created Epic: #123

📋 Creating 2 tickets...
📝 Creating TEST-001: First Test Child Issue
  ✅ Created: #124
📝 Creating TEST-002: Second Test Child Issue
  ✅ Created: #125
🔄 Updating Epic #123 with ticket links...
  ✅ Updated Epic with 2 ticket links

✅ Summary:
  - Epic: #123
  - Tickets created: 2

🔗 View Epic: https://github.com/wclaytor/{REPO}/issues/123
```

### 3. Verify Issues Were Created

Use the `gh` CLI to verify the issues:

```bash
# List recent issues
gh issue list --repo wclaytor/{REPO} --limit 10

# View the epic issue
gh issue view 123 --repo wclaytor/{REPO}

# View a child issue
gh issue view 124 --repo wclaytor/{REPO}

# View issues with specific label
gh issue list --repo wclaytor/{REPO} --label test
```

## Test File Description

The `test-epic.md` file contains:

1. **One Epic**: "Test Epic for Script Validation"
   - Title: "Epic: Test Epic for Script Validation"
   - Labels: epic, test
   - Description with success criteria

2. **Two Child Issues**:
   - **TEST-001**: First Test Child Issue
     - Type: task
     - Priority: P1
     - Points: 2
     - Labels: test, child-issue
     - No dependencies
   
   - **TEST-002**: Second Test Child Issue
     - Type: task
     - Priority: P2
     - Points: 3
     - Labels: test, child-issue
     - Depends on: TEST-001

## Features Demonstrated

1. **Epic Creation**: Creates a parent epic issue
2. **Child Issue Creation**: Creates linked child issues
3. **Dependency Tracking**: TEST-002 depends on TEST-001
4. **Labels**: Issues are tagged with appropriate labels
5. **Metadata**: Priority, points, sprint information
6. **Linking**: Epic is updated with links to all child issues
7. **Cross-referencing**: Child issues link back to the epic

## Getting Help

```bash
# Show help
python3 scripts/github/issues-create-epic/create-epic.py --help

# GitHub CLI help
gh issue create --help
gh issue list --help
gh issue view --help
```

## Additional Resources

- [GitHub CLI Manual](https://cli.github.com/manual/)
- [GitHub Issues Documentation](https://docs.github.com/en/issues)
- [gh-cli-issues.md](../../docs/github/gh-cli-issues.md) - Comprehensive gh CLI guide

---

**Pro Tip**: Keep your epic markdown files in version control alongside your code. This creates a historical record of your planning and makes it easy to recreate or update issues as needed.
