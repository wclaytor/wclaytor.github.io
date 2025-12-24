"""
conftest.py - Shared fixtures and configuration for Playwright tests

This module provides the foundation for all tests, following principles from:
- Kent Beck: Simple, focused fixtures that do one thing well
- Martin Fowler: Separation of concerns and composable design

Usage:
    Fixtures are automatically available to all tests.
    Import page objects from the pages package.
"""

import pytest
from pathlib import Path
from typing import Generator
from playwright.sync_api import Page, Browser, BrowserContext, Playwright


# =============================================================================
# Configuration
# =============================================================================

# Default URLs - can be overridden via command line
LOCAL_URL = "http://localhost:8000"
PRODUCTION_URL = "https://wclaytor.github.io"

# Viewport configurations
VIEWPORTS = {
    "mobile": {"width": 375, "height": 667},
    "tablet": {"width": 768, "height": 1024},
    "desktop": {"width": 1920, "height": 1080},
}

# Paths
TESTS_DIR = Path(__file__).parent
SCREENSHOTS_DIR = TESTS_DIR / "screenshots"
BASELINES_DIR = SCREENSHOTS_DIR / "baselines"
RECORDINGS_DIR = TESTS_DIR / "recordings"


# =============================================================================
# Command Line Options
# =============================================================================

def pytest_addoption(parser: pytest.Parser) -> None:
    """Add custom command line options.
    
    Note: --base-url is already provided by pytest-base-url plugin.
    Use it via: pytest --base-url=http://localhost:8000
    """
    parser.addoption(
        "--production",
        action="store_true",
        default=False,
        help="Run tests against production site",
    )
    parser.addoption(
        "--update-snapshots",
        action="store_true",
        default=False,
        help="Update visual test baselines",
    )


# =============================================================================
# Base Fixtures
# =============================================================================

@pytest.fixture(scope="session")
def base_url(request: pytest.FixtureRequest) -> str:
    """
    Get the base URL for tests.
    
    Priority:
    1. --production flag uses production URL
    2. --base-url option (from pytest-base-url plugin)
    3. Default local URL
    """
    if request.config.getoption("--production"):
        return PRODUCTION_URL
    # Use the base_url from pytest-base-url plugin, or fall back to LOCAL_URL
    url = request.config.getoption("base_url")
    return url if url else LOCAL_URL


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    """
    Configure browser context with recording and viewport settings.
    
    Enables video recording on failure and sets a reasonable default viewport.
    """
    return {
        **browser_context_args,
        "viewport": VIEWPORTS["desktop"],
        "record_video_dir": str(RECORDINGS_DIR / "videos"),
        "record_video_size": {"width": 1280, "height": 720},
    }


# =============================================================================
# Page Object Fixtures
# =============================================================================

@pytest.fixture
def home_page(page: Page, base_url: str):
    """
    Homepage page object fixture.
    
    Usage:
        def test_example(home_page):
            home_page.goto()
            assert home_page.is_masthead_visible()
    """
    from pages.home_page import HomePage
    return HomePage(page, base_url)


@pytest.fixture
def projects_page(page: Page, base_url: str):
    """Projects gallery page object fixture."""
    from pages.projects_page import ProjectsPage
    return ProjectsPage(page, base_url)


@pytest.fixture
def resume_page(page: Page, base_url: str):
    """Resume page object fixture."""
    from pages.resume_page import ResumePage
    return ResumePage(page, base_url)


# =============================================================================
# Viewport Fixtures
# =============================================================================

@pytest.fixture
def mobile_viewport() -> dict:
    """Mobile viewport dimensions (iPhone SE)."""
    return VIEWPORTS["mobile"]


@pytest.fixture
def tablet_viewport() -> dict:
    """Tablet viewport dimensions (iPad)."""
    return VIEWPORTS["tablet"]


@pytest.fixture
def desktop_viewport() -> dict:
    """Desktop viewport dimensions (Full HD)."""
    return VIEWPORTS["desktop"]


@pytest.fixture
def mobile_context(browser: Browser, mobile_viewport: dict) -> Generator[BrowserContext, None, None]:
    """Browser context with mobile viewport."""
    context = browser.new_context(viewport=mobile_viewport)
    yield context
    context.close()


@pytest.fixture
def mobile_page(mobile_context: BrowserContext) -> Generator[Page, None, None]:
    """Page with mobile viewport."""
    page = mobile_context.new_page()
    yield page
    page.close()


@pytest.fixture
def tablet_context(browser: Browser, tablet_viewport: dict) -> Generator[BrowserContext, None, None]:
    """Browser context with tablet viewport."""
    context = browser.new_context(viewport=tablet_viewport)
    yield context
    context.close()


@pytest.fixture
def tablet_page(tablet_context: BrowserContext) -> Generator[Page, None, None]:
    """Page with tablet viewport."""
    page = tablet_context.new_page()
    yield page
    page.close()


# =============================================================================
# Screenshot Fixtures
# =============================================================================

@pytest.fixture
def screenshots_dir() -> Path:
    """Directory for test screenshots."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    return SCREENSHOTS_DIR


@pytest.fixture
def baselines_dir() -> Path:
    """Directory for visual test baselines."""
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    return BASELINES_DIR


@pytest.fixture
def update_snapshots(request: pytest.FixtureRequest) -> bool:
    """Whether to update visual test baselines."""
    return request.config.getoption("--update-snapshots")


# =============================================================================
# Test Hooks
# =============================================================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call):
    """
    Capture screenshot on test failure.
    
    Following Kent Beck's principle: "When a test fails, 
    you want as much information as possible."
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Try to capture a screenshot
        page = item.funcargs.get("page")
        if page:
            try:
                failure_dir = RECORDINGS_DIR / "failures"
                failure_dir.mkdir(parents=True, exist_ok=True)
                screenshot_path = failure_dir / f"{item.name}.png"
                page.screenshot(path=str(screenshot_path))
                print(f"\n📸 Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"\n⚠️ Could not capture screenshot: {e}")


def pytest_configure(config: pytest.Config) -> None:
    """
    Configure pytest environment.
    
    Creates necessary directories and sets up reporting.
    """
    # Ensure directories exist
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)
    (RECORDINGS_DIR / "videos").mkdir(parents=True, exist_ok=True)
    (RECORDINGS_DIR / "failures").mkdir(parents=True, exist_ok=True)
    (RECORDINGS_DIR / "traces").mkdir(parents=True, exist_ok=True)


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """
    Modify test collection to run smoke tests first.
    
    Kent Beck says: "Run the fastest tests first."
    """
    # Sort tests: smoke first, then by name
    def test_priority(item: pytest.Item) -> tuple:
        markers = [marker.name for marker in item.iter_markers()]
        if "smoke" in markers:
            return (0, item.name)
        elif "functional" in markers:
            return (1, item.name)
        elif "visual" in markers:
            return (2, item.name)
        elif "a11y" in markers:
            return (3, item.name)
        else:
            return (4, item.name)
    
    items.sort(key=test_priority)


# =============================================================================
# Utility Fixtures
# =============================================================================

@pytest.fixture
def wait_for_animations(page: Page):
    """
    Helper to wait for CSS animations to complete.
    
    Returns a function that can be called to pause for animations.
    Bootstrap animations typically take 300ms.
    """
    def _wait(duration_ms: int = 300):
        page.wait_for_timeout(duration_ms)
    return _wait


@pytest.fixture
def console_errors(page: Page) -> Generator[list, None, None]:
    """
    Capture JavaScript console errors during test.
    
    Usage:
        def test_no_errors(page, console_errors):
            page.goto(url)
            assert len(console_errors) == 0
    """
    errors: list = []
    
    def handle_console(msg):
        if msg.type == "error":
            errors.append(msg.text)
    
    page.on("console", handle_console)
    yield errors
    page.remove_listener("console", handle_console)
