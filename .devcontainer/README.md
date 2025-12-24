# Dev Container for wclaytor.github.io

This dev container provides a pre-configured environment for developing and testing the portfolio website.

## Features

- **Playwright Pre-installed**: All browser dependencies (Chromium, Firefox, WebKit) are included
- **Python 3.12**: For running Playwright tests
- **Node.js LTS**: For any JavaScript tooling
- **Live Server**: Serve the static site locally for testing

## Getting Started

### VS Code

1. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
3. Select **Dev Containers: Reopen in Container**
4. Wait for the container to build (first time takes a few minutes)

### GitHub Codespaces

Click the "Code" button on GitHub and select "Open with Codespaces".

## Running Tests

Once in the container:

```bash
# Navigate to tests directory
cd tests/playwright

# Run all tests
uv run pytest

# Run smoke tests only
uv run pytest tests/smoke/

# Run with HTML report
uv run pytest --html=report.html

# Run headed (see the browser)
uv run pytest --headed
```

## Starting the Local Server

For testing against the local site:

```bash
# Option 1: Python's built-in server (from project root)
python -m http.server 8000

# Option 2: Use VS Code Live Server extension
# Right-click on index.html → "Open with Live Server"
```

Then run tests:

```bash
cd tests/playwright
uv run pytest --base-url=http://localhost:8000
```

## Included VS Code Extensions

- **Python** - Python language support
- **Pylance** - Python language server
- **Playwright Test** - Playwright test runner integration
- **Tailwind CSS IntelliSense** - CSS utility class autocomplete
- **Prettier** - Code formatting
- **Live Server** - Local development server

## Ports

| Port | Purpose |
|------|---------|
| 8000 | Python HTTP server |
| 5500 | VS Code Live Server |

## Troubleshooting

### Tests fail with "browser not found"
The Playwright image should have all browsers pre-installed. If not:
```bash
playwright install
```

### Permission issues
The container runs as `pwuser`. If you encounter permission issues:
```bash
sudo chown -R pwuser:pwuser .
```

### Updating dependencies
```bash
cd tests/playwright
uv sync
```
