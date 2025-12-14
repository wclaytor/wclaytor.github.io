#!/bin/bash
#
# Alpine Resume - Quick Deploy Script Example
#
# This is an example deployment script that automates the bundle and deploy process.
# Customize the PAGES_REPO path for your environment.
#
# Usage:
#   ./deploy-example.sh

set -e  # Exit on error

# Configuration - UPDATE THIS PATH
PAGES_REPO="${PAGES_REPO:-/path/to/wclaytor.github.io}"

# Check if pages repo path is set and exists
if [ "$PAGES_REPO" = "/path/to/wclaytor.github.io" ]; then
    echo "⚠️  Error: Please set PAGES_REPO environment variable or edit this script"
    echo "   Example: export PAGES_REPO=/path/to/wclaytor.github.io"
    exit 1
fi

if [ ! -d "$PAGES_REPO" ]; then
    echo "❌ Error: GitHub Pages repository not found at: $PAGES_REPO"
    exit 1
fi

# Generate bundle filename with timestamp
BUNDLE_NAME="alpine-resume-$(date +%Y%m%d-%H%M%S).tar.gz"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

echo "🚀 Alpine Resume Deployment"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Step 1: Create bundle
echo "📦 Step 1: Creating deployment bundle..."
cd "$PROJECT_ROOT"
python3 scripts/project/project-bundle/project-bundle.py --output "$BUNDLE_NAME"
echo ""

# Step 2: Copy to GitHub Pages repo
echo "📋 Step 2: Copying bundle to GitHub Pages repository..."
cp "$BUNDLE_NAME" "$PAGES_REPO/"
echo "  ✓ Bundle copied to $PAGES_REPO/$BUNDLE_NAME"
echo ""

# Step 3: Extract bundle
echo "📂 Step 3: Extracting bundle..."
cd "$PAGES_REPO"
python3 "$PROJECT_ROOT/scripts/project/project-bundle/project-bundle-extract.py" \
    --input "$BUNDLE_NAME" \
    --force
echo ""

# Step 4: Git operations
echo "🔄 Step 4: Committing changes..."
git add projects/alpine-resume/
git commit -m "Update Alpine Resume ($(date +%Y-%m-%d))"
echo ""

echo "🚀 Step 5: Pushing to GitHub..."
git push origin main
echo ""

# Cleanup
echo "🧹 Cleaning up..."
rm "$BUNDLE_NAME"
cd "$PROJECT_ROOT"
rm "$BUNDLE_NAME"
echo ""

echo "✅ Deployment complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🌐 Your site will be live at:"
echo "   https://wclaytor.github.io/projects/alpine-resume/"
echo ""
echo "💡 Tip: It may take a few minutes for GitHub Pages to update."
