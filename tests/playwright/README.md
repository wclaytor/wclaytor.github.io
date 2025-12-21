# Playwright Tests for wclaytor.github.io

Automated end-to-end tests for the wclaytor.github.io portfolio website using Playwright with Python and the Page Object Model pattern.

## Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

### Setup

```bash
# Navigate to the test directory
cd tests/playwright

# Install dependencies
uv sync

# Install Playwright browsers
uv run playwright install
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run smoke tests only (fastest, most critical)
uv run pytest tests/smoke -v

# Run with visible browser
uv run pytest --headed

# Run specific test file
uv run pytest tests/smoke/test_site_loads.py -v

# Run against production
uv run pytest --production

# Run against custom URL
uv run pytest --base-url https://wclaytor.github.io
```

## Test Categories

| Category | Command | Purpose |
|----------|---------|---------|
| Smoke | `pytest tests/smoke` | Critical path - must always pass |
| Functional | `pytest tests/functional` | Feature verification |
| Visual | `pytest tests/visual` | Visual regression |
| Accessibility | `pytest tests/accessibility` | WCAG compliance |
| Performance | `pytest tests/performance` | Performance checks |

## Project Structure

```
tests/playwright/
├── pages/                    # Page Object Model classes
│   ├── base_page.py         # Abstract base class
│   ├── home_page.py         # Homepage
│   ├── projects_page.py     # Projects gallery
│   ├── resume_page.py       # Resume page
│   └── components/          # Reusable components
│       ├── navigation.py
│       └── footer.py
├── tests/                    # Test files by category
│   ├── smoke/               # Critical path tests
│   ├── functional/          # Feature tests
│   ├── visual/              # Visual regression
│   ├── accessibility/       # A11y tests
│   └── performance/         # Performance tests
├── fixtures/                 # Test data
│   ├── urls.py              # URL constants
│   └── test_data.py         # Expected values
├── screenshots/             # Visual test artifacts
│   └── baselines/           # Expected screenshots
├── recordings/              # Test recordings
├── conftest.py              # Pytest configuration
└── pyproject.toml           # Dependencies
```

## Documentation

- **[TESTING_STRATEGY.md](TESTING_STRATEGY.md)** - Testing philosophy and approach
- **[TEST_ARCHITECTURE.md](TEST_ARCHITECTURE.md)** - Technical architecture and patterns
- **[TEST_PLAN.md](TEST_PLAN.md)** - Detailed test cases and coverage

## Running a Local Server

Tests run against a local server by default (`http://localhost:8000`):

```bash
# From the repository root
python -m http.server 8000

# Then run tests in another terminal
cd tests/playwright
uv run pytest tests/smoke -v
```

## Visual Testing

Update visual baselines when intentional changes are made:

```bash
# Update all baselines
uv run pytest tests/visual --update-snapshots

# Update specific baseline
uv run pytest tests/visual/test_homepage_visual.py --update-snapshots
```

## Debugging

```bash
# Run with visible browser and slow motion
uv run pytest --headed --slowmo 500

# Open Playwright inspector
PWDEBUG=1 uv run pytest tests/smoke/test_site_loads.py

# Generate test code interactively
uv run playwright codegen http://localhost:8000

# View trace from failed test
uv run playwright show-trace recordings/traces/test_name.zip
```

## CI/CD Integration

Tests are designed to run in CI pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run Playwright Tests
  run: |
    cd tests/playwright
    uv sync
    uv run playwright install --with-deps
    uv run pytest tests/smoke -v
```

## Contributing

1. Follow the Page Object Model pattern
2. Add tests to the appropriate category folder
3. Use descriptive test names that explain the behavior
4. Update test data in `fixtures/` when adding new assertions

## Philosophy

> *"Make it work, make it right, make it fast."* — Kent Beck

These tests protect the quality we've already achieved and enable confident future changes. See [TESTING_STRATEGY.md](TESTING_STRATEGY.md) for our full testing philosophy.