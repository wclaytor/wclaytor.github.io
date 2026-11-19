# Development Container Configuration

This directory contains the development container (devcontainer) configuration for the project. The devcontainer provides a consistent, reproducible development environment with all necessary tools pre-installed.

## What's Included

### Base Image
- **Python 3.13** - Latest Python version matching project requirements

### Tools & Package Managers
- **uv** - Fast Python package manager and resolver
- **Playwright** - End-to-end testing framework with browser automation
- **gh CLI** - GitHub command-line tool for repository operations
- **Node.js 24.22.2** - Pinned in `devcontainer.json` to match CI, which reads `.nvmrc`, so local npm writes lock files that CI accepts. To upgrade, change both files.

### VS Code Extensions
The devcontainer automatically installs these extensions:
- **ms-python.python** - Python language support
- **ms-python.vscode-pylance** - Fast Python language server
- **ms-python.debugpy** - Python debugging
- **charliermarsh.ruff** - Fast Python linter and formatter
- **ms-playwright.playwright** - Playwright test support
- **GitHub.copilot** - AI pair programmer
- **GitHub.copilot-chat** - AI chat assistant

### VS Code Settings
Pre-configured settings for optimal Python development:
- Python 3.13 as default interpreter
- Pylance language server with basic type checking
- Format on save enabled
- Auto-organize imports on save
- Hidden `__pycache__` and `.pyc` files

## Usage

### Opening in VS Code

1. **Install Prerequisites**:
   - [VS Code](https://code.visualstudio.com/)
   - [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open the Project**:
   - Open the repository folder in VS Code
   - VS Code will detect the `.devcontainer` configuration
   - Click "Reopen in Container" when prompted
   - Or use Command Palette: `Dev Containers: Reopen in Container`

3. **Wait for Setup**:
   - The container will build and run the setup script
   - This may take a few minutes on first run
   - Subsequent starts will be much faster

### Opening in GitHub Codespaces

1. Navigate to the repository on GitHub
2. Click the **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main** (or your branch)
5. Wait for the environment to initialize

## Working with the Environment

### Python Projects with uv

Navigate to any Python project and use uv commands:

```bash
# Navigate to your Python project directory
cd path/to/your/python/project

# Install dependencies
uv sync

# Run the project
uv run your-command

# Run tests
uv run pytest

# Add a new dependency
uv add <package-name>
```

### Playwright Testing

```bash
# Run Playwright tests
npx playwright test

# Run tests in headed mode
npx playwright test --headed

# Run tests in debug mode
npx playwright test --debug

# Open Playwright test runner UI
npx playwright test --ui
```

### GitHub CLI Operations

```bash
# Authenticate (first time only)
gh auth login

# Create an issue
gh issue create

# List pull requests
gh pr list

# View repository status
gh repo view
```

## File Structure

```
.devcontainer/
├── devcontainer.json    # Main devcontainer configuration
├── setup.sh            # Post-creation setup script
└── README.md           # This file
```

## Customization

### Adding Extensions

Edit `devcontainer.json` to add more VS Code extensions:

```json
"extensions": [
    "existing.extension",
    "new.extension-id"
]
```

### Installing Additional Tools

Add commands to `setup.sh`:

```bash
# Example: Install additional tools
echo "Installing custom tool..."
npm install -g your-tool
```

### Modifying VS Code Settings

Update the `settings` section in `devcontainer.json`:

```json
"settings": {
    "your.setting": "value"
}
```

## Troubleshooting

### Container Won't Start
- Ensure Docker Desktop is running
- Check Docker has sufficient resources (CPU, memory)
- Try rebuilding: Command Palette → `Dev Containers: Rebuild Container`

### Tools Not Found
- The setup script runs on container creation
- If tools are missing, rebuild the container
- Check `setup.sh` logs in the terminal

### Git Configuration
- Your local `.gitconfig` is mounted automatically
- SSH keys from your host are available
- GitHub authentication may need `gh auth login`

### Python Packages Not Installing
- Ensure you're in a project directory with `pyproject.toml`
- Run `uv sync` to install dependencies
- Check Python version matches project requirements

## Benefits

✅ **Consistency** - Same environment for all developers
✅ **Portability** - Works on Windows, macOS, and Linux
✅ **Isolation** - Doesn't affect your host system
✅ **Speed** - Pre-configured with all necessary tools
✅ **Reproducibility** - Version-controlled configuration
✅ **Cloud-Ready** - Works with GitHub Codespaces

## Resources

- [VS Code Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [Dev Container Specification](https://containers.dev/)
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Playwright Documentation](https://playwright.dev/)
- [GitHub CLI Documentation](https://cli.github.com/)

## Model CLIs

Setup installs pinned Copilot, Claude and Codex CLIs through the [shared installer](../install-model-clis.sh).
See [model CLI operation and verification](../model-clis.md) for versions, authentication,
isolation controls, and remaining account checks. Both variants require at least 4 GB of
available host memory for Claude Code; the small variant keeps its other resource settings.
