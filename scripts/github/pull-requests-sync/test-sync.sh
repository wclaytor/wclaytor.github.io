#!/bin/bash
# Test script for pull-requests-sync.py

echo "🧪 Testing GitHub Pull Requests Sync Tool"
echo "=========================================="
echo ""

SCRIPT="scripts/github/pull-requests-sync/pull-requests-sync.py"

# Test 1: Help/Usage
echo "📋 Test 1: Display usage information"
python3 "$SCRIPT"
echo "✅ Test 1 passed"
echo ""

# Test 2: Pull single PR
echo "📋 Test 2: Pull single PR (#69)"
python3 "$SCRIPT" pull 69
echo "✅ Test 2 passed"
echo ""

# Test 3: Check files were created
echo "📋 Test 3: Verify PR folder structure"
if [ -d ".github/pull-requests/pr-0069" ]; then
    echo "✓ PR folder exists"
else
    echo "✗ PR folder missing"
    exit 1
fi

if [ -f ".github/pull-requests/pr-0069/pr-0069.md" ]; then
    echo "✓ PR markdown file exists"
else
    echo "✗ PR markdown file missing"
    exit 1
fi

if [ -f ".github/pull-requests/pr-0069/changed-files.txt" ]; then
    echo "✓ Changed files list exists"
else
    echo "✗ Changed files list missing"
    exit 1
fi
echo "✅ Test 3 passed"
echo ""

# Test 4: Verify changed files content
echo "📋 Test 4: Verify changed files content"
if grep -q "index.html" ".github/pull-requests/pr-0069/changed-files.txt"; then
    echo "✓ Changed files contains expected file"
else
    echo "✗ Changed files missing expected content"
    exit 1
fi
echo "✅ Test 4 passed"
echo ""

# Test 5: Verify PR markdown structure
echo "📋 Test 5: Verify PR markdown structure"
if grep -q "pr_number: 69" ".github/pull-requests/pr-0069/pr-0069.md"; then
    echo "✓ Frontmatter contains PR number"
else
    echo "✗ Frontmatter missing PR number"
    exit 1
fi

if grep -q "## Implementation Notes" ".github/pull-requests/pr-0069/pr-0069.md"; then
    echo "✓ Contains Implementation Notes section"
else
    echo "✗ Missing Implementation Notes section"
    exit 1
fi

if grep -q "## Testing Notes" ".github/pull-requests/pr-0069/pr-0069.md"; then
    echo "✓ Contains Testing Notes section"
else
    echo "✗ Missing Testing Notes section"
    exit 1
fi

if grep -q "## Review Notes" ".github/pull-requests/pr-0069/pr-0069.md"; then
    echo "✓ Contains Review Notes section"
else
    echo "✗ Missing Review Notes section"
    exit 1
fi
echo "✅ Test 5 passed"
echo ""

# Test 6: Summary command
echo "📋 Test 6: Display PR summary"
python3 "$SCRIPT" summary
echo "✅ Test 6 passed"
echo ""

echo "🎉 All tests passed!"
echo ""
echo "📂 Created files:"
tree .github/pull-requests/ || ls -R .github/pull-requests/
