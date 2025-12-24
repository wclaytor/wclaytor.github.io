# Testing Strategy for wclaytor.github.io

> *"Make it work, make it right, make it fast."* — Kent Beck
>
> *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."* — Martin Fowler

## Executive Summary

This document outlines our testing strategy for the wclaytor.github.io portfolio website, drawing on principles from Test-Driven Development (TDD), Extreme Programming (XP), and modern testing best practices championed by Kent Beck and Martin Fowler.

Our approach recognizes that we're starting from a working, live website that has been validated through manual exploratory testing. We're not building tests to find bugs—we're building tests to **protect the quality we've already achieved** and **enable confident future changes**.

---

## Testing Philosophy

### From Kent Beck: The TDD Mindset

Kent Beck teaches us that tests serve multiple purposes:

1. **Tests as Documentation**: Tests tell the story of what the system does
2. **Tests as Safety Net**: Tests catch regressions before users do
3. **Tests as Design Feedback**: Difficult-to-test code often indicates design problems
4. **Tests as Confidence**: Good tests give you courage to refactor

For our portfolio site, we embrace the principle of **"tests as executable specifications"**. Each test should clearly describe an expected behavior that matters to users.

### From Martin Fowler: The Refactoring Safety Net

Martin Fowler's work on refactoring emphasizes that **tests enable change**. Without tests, every change is risky. With good tests, we can:

- Confidently update designs and styles
- Add new projects without breaking existing ones
- Refactor code knowing we haven't broken user-facing behavior
- Deploy with confidence

### The Testing Pyramid Applied

Following the testing pyramid concept, our strategy prioritizes:

```
        /\
       /  \      E2E Tests (Playwright)
      /----\     - Critical user journeys
     /      \    - Cross-browser validation
    /--------\   
   /          \  Integration Tests
  /   Visual   \ - Component interactions
 /   Snapshot   \- Page layouts
/----------------\
     Accessibility & Performance
     (Built into E2E tests)
```

---

## Testing Principles

### 1. Test Behavior, Not Implementation

```python
# ❌ Testing implementation
def test_navbar_has_correct_class():
    assert page.locator("nav").get_attribute("class") == "navbar navbar-expand-lg"

# ✅ Testing behavior
def test_navigation_links_are_visible():
    """Users can see and access navigation links."""
    assert page.get_by_role("link", name="About").is_visible()
    assert page.get_by_role("link", name="Projects").is_visible()
```

### 2. Tests Should Be Independent

Each test should be able to run in isolation. No test should depend on another test's state or execution order.

### 3. Tests Should Be Fast

A slow test suite is an unused test suite. We aim for:
- Individual tests: < 5 seconds
- Full smoke suite: < 2 minutes
- Full regression suite: < 10 minutes

### 4. Tests Should Be Deterministic

A test that sometimes passes and sometimes fails is worse than no test. We avoid flaky tests through:
- Proper wait strategies (never `time.sleep()`)
- Playwright's auto-waiting capabilities
- Stable selectors (prefer accessibility attributes)

### 5. Tests Should Be Readable

Following Martin Fowler's emphasis on readable code:

```python
def test_visitor_can_view_resume():
    """
    Given: A visitor is on the homepage
    When: They click the 'View Full Resume' button
    Then: They are taken to the resume page
    And: The resume content is displayed
    """
    home_page.goto()
    home_page.click_view_resume()
    
    assert resume_page.is_loaded()
    assert resume_page.has_content()
```

---

## Test Categories

### 1. Smoke Tests (Critical Path)

**Purpose**: Verify the site is basically functional  
**When to Run**: Every commit, every deployment  
**Duration**: < 1 minute

Smoke tests answer: "Is the site alive and navigable?"

### 2. Functional Tests

**Purpose**: Verify features work as expected  
**When to Run**: Before merge to main  
**Duration**: < 5 minutes

Functional tests answer: "Do the features work correctly?"

### 3. Visual Regression Tests

**Purpose**: Catch unintended visual changes  
**When to Run**: Before merge to main, after style changes  
**Duration**: < 3 minutes

Visual tests answer: "Does the site still look right?"

### 4. Accessibility Tests

**Purpose**: Ensure the site is usable by everyone  
**When to Run**: Before merge to main  
**Duration**: < 2 minutes

Accessibility tests answer: "Can all users access this site?"

### 5. Cross-Browser Tests

**Purpose**: Verify consistent behavior across browsers  
**When to Run**: Before release, weekly  
**Duration**: < 10 minutes

Cross-browser tests answer: "Does this work everywhere?"

### 6. Performance Tests (Lighthouse)

**Purpose**: Monitor site performance  
**When to Run**: Weekly, after major changes  
**Duration**: < 5 minutes

Performance tests answer: "Is the site fast enough?"

---

## Test Architecture

### Page Object Model (POM)

Following the Page Object pattern recommended by both Beck (as a way to reduce test duplication) and Fowler (as a refactoring-friendly design):

```
tests/playwright/
├── pages/                    # Page Object classes
│   ├── base_page.py         # Common page functionality
│   ├── home_page.py         # Homepage interactions
│   ├── projects_page.py     # Projects listing
│   ├── resume_page.py       # Resume page
│   └── components/          # Reusable component objects
│       ├── navigation.py
│       └── footer.py
├── tests/                    # Test files organized by type
│   ├── smoke/               # Critical path tests
│   ├── functional/          # Feature tests
│   ├── visual/              # Snapshot tests
│   ├── accessibility/       # A11y tests
│   └── cross_browser/       # Browser-specific tests
├── fixtures/                 # Test data and fixtures
├── screenshots/             # Visual test baselines
│   └── baselines/
├── recordings/              # Test run recordings
├── conftest.py              # Pytest fixtures and configuration
├── pytest.ini               # Pytest configuration
└── pyproject.toml           # Project dependencies (uv)
```

### Why Page Object Model?

Kent Beck would approve because:
- **Reduces duplication**: Selectors and actions defined once
- **Improves readability**: Tests read like user stories
- **Enables refactoring**: Change selectors in one place

Martin Fowler would approve because:
- **Separation of concerns**: Tests describe WHAT, pages describe HOW
- **Maintainability**: When UI changes, only page objects need updating
- **Composability**: Pages can be composed from components

---

## Visual Testing Strategy

### Snapshot Testing Approach

We capture screenshots at key points:

1. **Full Page Snapshots**: Capture entire pages at multiple viewports
2. **Component Snapshots**: Capture specific components (navigation, cards, footer)
3. **State Snapshots**: Capture different states (hover, focus, mobile menu open)

### Viewport Matrix

```python
VIEWPORTS = {
    "mobile": {"width": 375, "height": 667},      # iPhone SE
    "tablet": {"width": 768, "height": 1024},     # iPad
    "desktop": {"width": 1920, "height": 1080},   # Full HD
}
```

### Visual Diff Threshold

- **Allowed difference**: 0.1% (to account for anti-aliasing differences)
- **Review required**: Any difference > 0.1%
- **Auto-fail**: Any difference > 5%

---

## Recording Strategy

### When to Record

1. **Test Failures**: Always capture video on failure
2. **Visual Tests**: Capture video for visual regression analysis
3. **On Demand**: Optional recording for debugging

### Recording Configuration

```python
# Record video only on failure
use: {
    video: "retain-on-failure",
    screenshot: "only-on-failure",
    trace: "retain-on-failure"
}
```

### Storage and Cleanup

- Recordings stored in `tests/playwright/recordings/`
- Automatic cleanup of recordings older than 7 days
- Failed test recordings kept for 30 days

---

## Continuous Integration

### Test Execution Strategy

```yaml
# Suggested CI workflow
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  smoke:
    # Always run smoke tests first
    runs-on: ubuntu-latest
    steps:
      - run: uv run pytest tests/playwright/tests/smoke -v

  functional:
    needs: smoke
    # Only run if smoke passes
    steps:
      - run: uv run pytest tests/playwright/tests/functional -v

  visual:
    needs: smoke
    # Run visual tests in parallel
    steps:
      - run: uv run pytest tests/playwright/tests/visual -v

  cross-browser:
    needs: [functional, visual]
    # Run cross-browser only if others pass
    strategy:
      matrix:
        browser: [chromium, firefox, webkit]
```

---

## Quality Gates

### Before Merge

All PRs must pass:
- [ ] Smoke tests (all browsers)
- [ ] Functional tests (chromium)
- [ ] Visual regression tests (no unexpected changes)
- [ ] Accessibility tests (no new violations)

### Before Release

Additionally:
- [ ] Full cross-browser test suite
- [ ] Performance audit (Lighthouse > 90)
- [ ] Manual review of visual diffs

---

## Metrics and Reporting

### Test Coverage Goals

| Area | Target Coverage |
|------|-----------------|
| Critical paths (smoke) | 100% |
| Navigation | 100% |
| All linked pages load | 100% |
| Responsive breakpoints | 3 viewports |
| Accessibility | WCAG AA |

### Success Metrics

- **Test Reliability**: < 1% flaky tests
- **Test Speed**: Full suite < 10 minutes
- **Defect Escape Rate**: 0 bugs reported by users that tests should have caught
- **Maintenance Burden**: < 1 hour/week maintaining tests

---

## Getting Started

### Prerequisites

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize the project
cd tests/playwright
uv sync

# Install Playwright browsers
uv run playwright install
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run smoke tests only
uv run pytest tests/smoke -v

# Run with visible browser
uv run pytest --headed

# Run specific test file
uv run pytest tests/functional/test_navigation.py -v

# Update visual baselines
uv run pytest tests/visual --update-snapshots
```

---

## Maintenance Guidelines

### Adding New Tests

1. **Identify the behavior** to test (user story)
2. **Create or update** the page object if needed
3. **Write the test** in the appropriate category
4. **Run locally** with `--headed` to verify
5. **Update baselines** if visual test

### Handling Flaky Tests

1. **Quarantine**: Move to a `@pytest.mark.flaky` category
2. **Investigate**: Use trace and video to understand
3. **Fix or Remove**: Flaky tests erode trust—fix them or delete them

### Updating Visual Baselines

When intentional visual changes are made:

```bash
# Update all baselines
uv run pytest tests/visual --update-snapshots

# Update specific baseline
uv run pytest tests/visual/test_homepage.py --update-snapshots

# Review changes in git diff before committing
git diff tests/playwright/screenshots/
```

---

## References

- Kent Beck, *Test-Driven Development: By Example*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- Martin Fowler, [Testing Strategies in a Microservice Architecture](https://martinfowler.com/articles/microservice-testing/)
- Playwright Documentation: https://playwright.dev/python/
- pytest Documentation: https://docs.pytest.org/

---

*"I'm not a great programmer; I'm just a good programmer with great habits."* — Kent Beck

This testing strategy embodies that philosophy: we build good habits through consistent, well-designed tests that protect our work and enable confident change.
