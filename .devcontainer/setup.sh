#!/bin/bash

set -e

echo "🚀 Setting up development environment..."

# Install uv package manager (installs to ~/.local/bin)
echo "📦 Installing uv package manager..."
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Verify uv installation
if command -v uv &> /dev/null; then
    echo "✅ uv installed successfully: $(uv --version)"
else
    echo "⚠️  uv installation may need shell restart"
fi

# The Playwright image has no Python of its own. `uv run` downloads whatever a project's
# requires-python needs on demand; this also puts `python`/`python3` on PATH for ad-hoc use.
if ! command -v python3 &> /dev/null; then
    echo "🐍 Installing uv-managed Python as the default python/python3..."
    uv python install --default
fi

# Install the same pinned model CLIs in both variants; login remains a separate user action.
bash .devcontainer/install-model-clis.sh

# Playwright browsers and OS deps are baked into the image (/ms-playwright); only the npm package is needed
echo "🎭 Installing npm dependencies..."
npm ci

# The image's browsers only work with the matching @playwright/test version
IMAGE_PW_VERSION="$(sed -n 's/.*playwright:v\([0-9.]*\)-.*/\1/p' .devcontainer/devcontainer.json)"
PROJECT_PW_VERSION="$(node -p "require('@playwright/test/package.json').version")"
if [ "$IMAGE_PW_VERSION" = "$PROJECT_PW_VERSION" ]; then
    echo "✅ Playwright $PROJECT_PW_VERSION matches the container image"
else
    echo "⚠️  @playwright/test is $PROJECT_PW_VERSION but the image is v$IMAGE_PW_VERSION; update the image tag in .devcontainer/large/devcontainer.json"
fi

# CI reads its Node.js version from .nvmrc; the node feature in devcontainer.json must match it
CI_NODE_VERSION="$(tr -d '[:space:]' < .nvmrc)"
LOCAL_NODE_VERSION="$(node --version | sed 's/^v//')"
if [ "$CI_NODE_VERSION" = "$LOCAL_NODE_VERSION" ]; then
    echo "✅ Node.js $LOCAL_NODE_VERSION matches CI (.nvmrc)"
else
    echo "⚠️  Node.js is $LOCAL_NODE_VERSION but CI uses $CI_NODE_VERSION (.nvmrc); update the node feature version in .devcontainer/devcontainer.json"
fi

# Verify gh CLI
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI available: $(gh --version | head -1)"
else
    echo "⚠️  GitHub CLI not found"
fi

echo ""
echo "✨ Development environment setup complete!"
echo ""
echo "Available tools:"
echo "  • Node.js $(node --version)"
echo "  • Playwright $PROJECT_PW_VERSION (browsers preinstalled)"
echo "  • uv (manages Python for uv projects)"
echo "  • gh (GitHub CLI)"
echo ""
echo "To run a uv project, e.g. issues-sync:"
echo "  • uv run --directory ./scripts/github/issues-sync issues-sync pull"
echo ""
