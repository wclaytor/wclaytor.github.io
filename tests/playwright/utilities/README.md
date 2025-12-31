# Utilities

This is where our test utilities go! Each utility is a standalone uv project that could be dropped into any other uv-based environment. We collect them here as a toolbox to help us manage our tests.

## Available Utilities

### xml2md

Convert JUnit XML test reports to beautiful Markdown reports.

```bash
# Basic usage
uv run --directory ./utilities/xml2md xml2md report.xml

# Custom output
uv run --directory ./utilities/xml2md xml2md report.xml -o custom.md
```

See [xml2md/README.md](xml2md/README.md) for full documentation.

## Creating New Utilities

Each utility follows the uv pattern with PEP 735 dependency groups:

1. Create a new directory: `utilities/my-utility/`
2. Initialize with `uv init --lib`
3. Add dependencies with `uv add` and `uv add --dev`
4. Create your script in `src/my_utility/__init__.py`
5. Add a `README.md` with usage instructions
