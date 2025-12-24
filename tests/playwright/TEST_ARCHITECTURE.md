# Test Architecture for wclaytor.github.io

> *"The goal of software architecture is to minimize the human resources required to build and maintain the required system."* — Robert C. Martin
>
> Informed by Kent Beck's simplicity principles and Martin Fowler's refactoring patterns

## Overview

This document describes the test architecture for the wclaytor.github.io portfolio website. Our architecture follows the **Page Object Model (POM)** pattern, which provides a clean separation between test logic and page interactions.

---

## Directory Structure

```
tests/playwright/
│
├── pyproject.toml           # Project dependencies and configuration
├── pytest.ini               # Pytest settings
├── conftest.py              # Global fixtures and configuration
├── README.md                # Quick start guide
├── TESTING_STRATEGY.md      # Strategy document (this project's philosophy)
├── TEST_ARCHITECTURE.md     # This document
├── TEST_PLAN.md             # Detailed test cases
│
├── pages/                   # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py         # Abstract base class for all pages
│   ├── home_page.py         # Homepage (index.html)
│   ├── projects_page.py     # Projects gallery (/projects/)
│   ├── resume_page.py       # Resume page
│   └── components/          # Reusable component objects
│       ├── __init__.py
│       ├── navigation.py    # Site navigation component
│       ├── footer.py        # Site footer component
│       └── project_card.py  # Project card component
│
├── tests/                   # Test files organized by category
│   ├── __init__.py
│   ├── smoke/               # Critical path tests (run first, always)
│   │   ├── __init__.py
│   │   ├── test_site_loads.py
│   │   └── test_critical_navigation.py
│   ├── functional/          # Feature-specific tests
│   │   ├── __init__.py
│   │   ├── test_navigation.py
│   │   ├── test_homepage.py
│   │   ├── test_projects.py
│   │   ├── test_resume.py
│   │   └── test_contact.py
│   ├── visual/              # Visual regression tests
│   │   ├── __init__.py
│   │   ├── test_homepage_visual.py
│   │   ├── test_projects_visual.py
│   │   └── test_responsive_visual.py
│   ├── accessibility/       # WCAG compliance tests
│   │   ├── __init__.py
│   │   └── test_a11y.py
│   └── performance/         # Performance tests
│       ├── __init__.py
│       └── test_lighthouse.py
│
├── fixtures/                # Test data and reusable fixtures
│   ├── __init__.py
│   ├── urls.py              # URL constants
│   └── test_data.py         # Test data constants
│
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── screenshot_utils.py  # Screenshot comparison helpers
│   ├── a11y_utils.py        # Accessibility testing helpers
│   └── wait_utils.py        # Custom wait conditions
│
├── screenshots/             # Visual test artifacts
│   ├── baselines/           # Expected screenshots (committed to git)
│   │   ├── desktop/
│   │   ├── tablet/
│   │   └── mobile/
│   └── actual/              # Actual screenshots (gitignored)
│       └── .gitkeep
│
└── recordings/              # Test recordings (gitignored)
    └── .gitkeep
```

---

## Page Object Model Design

### Design Principles

Following Kent Beck's XP principles:

1. **Simple Design**: Page objects expose only what tests need
2. **Once and Only Once**: Selectors defined in one place
3. **Communication**: Method names describe user actions, not implementation

Following Martin Fowler's patterns:

1. **Encapsulation**: Hide page structure from tests
2. **Fluent Interface**: Enable readable test chains
3. **Composition**: Build complex behaviors from simple components

### Base Page Class

```python
"""
base_page.py - Foundation for all page objects

Kent Beck would say: "The simplest thing that could possibly work"
Martin Fowler would say: "Delegate, delegate, delegate"
"""

from abc import ABC, abstractmethod
from playwright.sync_api import Page, expect
from typing import Self


class BasePage(ABC):
    """
    Abstract base class providing common functionality for all page objects.
    
    Responsibilities:
    - Navigation to the page
    - Common element interactions
    - Screenshot capture
    - Accessibility checks
    """
    
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url
        
    @property
    @abstractmethod
    def path(self) -> str:
        """The URL path for this page (e.g., '/projects/')"""
        pass
    
    @property
    def url(self) -> str:
        """Full URL for this page"""
        return f"{self.base_url}{self.path}"
    
    def goto(self) -> Self:
        """Navigate to this page"""
        self.page.goto(self.url)
        self.wait_for_load()
        return self
    
    def wait_for_load(self) -> None:
        """Wait for the page to be fully loaded"""
        self.page.wait_for_load_state("networkidle")
    
    def get_title(self) -> str:
        """Get the page title"""
        return self.page.title()
    
    def take_screenshot(self, name: str, full_page: bool = True) -> bytes:
        """Capture a screenshot of the current page"""
        return self.page.screenshot(full_page=full_page)
    
    def check_accessibility(self) -> dict:
        """Run accessibility audit using axe-core"""
        # Inject axe-core and run audit
        # Returns violations dict
        pass
    
    # Common navigation (delegated to Navigation component)
    @property
    def navigation(self):
        from pages.components.navigation import Navigation
        return Navigation(self.page)
    
    @property
    def footer(self):
        from pages.components.footer import Footer
        return Footer(self.page)
```

### Example Page Object

```python
"""
home_page.py - Page object for the homepage

This class encapsulates all interactions with the homepage,
following the "tell, don't ask" principle.
"""

from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class HomePage(BasePage):
    """
    Page object for the main homepage (index.html).
    
    Sections:
    - Masthead (hero area)
    - About section
    - Projects section
    - Contact section
    """
    
    @property
    def path(self) -> str:
        return "/"
    
    # Selectors (private - hidden from tests)
    _MASTHEAD = "header.masthead"
    _MASTHEAD_TITLE = "header.masthead h1"
    _MASTHEAD_TAGLINE = ".masthead-tagline"
    _SCROLL_INDICATOR = "#scrollIndicator"
    
    _ABOUT_SECTION = "#about"
    _HEADSHOT = ".headshot-img"
    _ABOUT_LEAD = ".about-lead"
    _EXPERTISE_CARDS = ".expertise-card"
    _VIEW_RESUME_BTN = "a:has-text('View Full Resume')"
    
    _PROJECTS_SECTION = "#projects"
    _PROJECT_CARDS = ".card"
    _EXPERIMENTS_SECTION = ".experiments-section"
    
    _CONTACT_SECTION = "#contact"
    _EMAIL_LINK = "a[href^='mailto:']"
    _SOCIAL_LINKS = ".social a"
    
    # Public methods (what tests can do)
    
    def is_masthead_visible(self) -> bool:
        """Check if the hero masthead is visible"""
        return self.page.locator(self._MASTHEAD).is_visible()
    
    def get_masthead_title(self) -> str:
        """Get the main title text"""
        return self.page.locator(self._MASTHEAD_TITLE).text_content()
    
    def get_tagline(self) -> str:
        """Get the tagline text"""
        return self.page.locator(self._MASTHEAD_TAGLINE).text_content()
    
    def click_scroll_indicator(self) -> None:
        """Click the scroll-down indicator"""
        self.page.locator(self._SCROLL_INDICATOR).click()
    
    def scroll_to_about(self) -> None:
        """Scroll to the About section"""
        self.page.locator(self._ABOUT_SECTION).scroll_into_view_if_needed()
    
    def is_headshot_visible(self) -> bool:
        """Check if the profile headshot is visible"""
        return self.page.locator(self._HEADSHOT).is_visible()
    
    def get_expertise_areas(self) -> list[str]:
        """Get list of expertise area titles"""
        cards = self.page.locator(self._EXPERTISE_CARDS)
        return [card.locator("h4").text_content() for card in cards.all()]
    
    def click_view_resume(self) -> None:
        """Click the 'View Full Resume' button"""
        self.page.locator(self._VIEW_RESUME_BTN).click()
    
    def scroll_to_projects(self) -> None:
        """Scroll to the Projects section"""
        self.page.locator(self._PROJECTS_SECTION).scroll_into_view_if_needed()
    
    def get_featured_project_titles(self) -> list[str]:
        """Get titles of featured projects"""
        return self.page.locator(f"{self._PROJECTS_SECTION} .card-title").all_text_contents()
    
    def click_project(self, project_name: str) -> None:
        """Click on a specific project card"""
        self.page.locator(f".card-title:has-text('{project_name}')").click()
    
    def scroll_to_contact(self) -> None:
        """Scroll to the Contact section"""
        self.page.locator(self._CONTACT_SECTION).scroll_into_view_if_needed()
    
    def get_email_address(self) -> str:
        """Get the contact email address"""
        href = self.page.locator(self._EMAIL_LINK).get_attribute("href")
        return href.replace("mailto:", "") if href else ""
    
    def get_social_links(self) -> list[str]:
        """Get all social media profile URLs"""
        links = self.page.locator(self._SOCIAL_LINKS)
        return [link.get_attribute("href") for link in links.all()]
```

### Component Objects

```python
"""
navigation.py - Navigation component shared across pages

This component represents the site's main navigation bar,
which appears on every page.
"""

from playwright.sync_api import Page, expect


class Navigation:
    """
    Component object for the site navigation.
    
    Used by all page objects to interact with navigation.
    """
    
    def __init__(self, page: Page):
        self.page = page
    
    # Selectors
    _NAV = "#mainNav"
    _BRAND = ".navbar-brand"
    _TOGGLE = ".navbar-toggler"
    _NAV_LINKS = ".navbar-nav .nav-link"
    
    def is_visible(self) -> bool:
        """Check if navigation is visible"""
        return self.page.locator(self._NAV).is_visible()
    
    def get_brand_text(self) -> str:
        """Get the brand/logo text"""
        return self.page.locator(self._BRAND).text_content()
    
    def click_brand(self) -> None:
        """Click the brand link (navigate home)"""
        self.page.locator(self._BRAND).click()
    
    def get_nav_links(self) -> list[str]:
        """Get all navigation link texts"""
        return self.page.locator(self._NAV_LINKS).all_text_contents()
    
    def click_nav_link(self, link_text: str) -> None:
        """Click a navigation link by its text"""
        self.page.get_by_role("link", name=link_text).click()
    
    def is_mobile_menu_visible(self) -> bool:
        """Check if mobile menu toggle is visible"""
        return self.page.locator(self._TOGGLE).is_visible()
    
    def toggle_mobile_menu(self) -> None:
        """Toggle the mobile menu"""
        self.page.locator(self._TOGGLE).click()
    
    def wait_for_menu_animation(self) -> None:
        """Wait for menu open/close animation"""
        self.page.wait_for_timeout(300)  # Bootstrap animation duration
```

---

## Test Organization

### Test Categories and Markers

```python
# pytest markers defined in pytest.ini
markers = [
    "smoke: Critical path tests that must pass",
    "functional: Feature-specific tests",
    "visual: Visual regression tests",
    "a11y: Accessibility tests",
    "performance: Performance tests",
    "slow: Tests that take longer than 10 seconds",
    "flaky: Known flaky tests (quarantined)",
]
```

### Example Test Structure

```python
"""
test_homepage.py - Functional tests for the homepage

Following Kent Beck's test structure:
- Arrange: Set up the test conditions
- Act: Perform the action being tested
- Assert: Verify the expected outcome
"""

import pytest
from pages.home_page import HomePage


class TestHomepageMasthead:
    """Tests for the homepage masthead/hero section"""
    
    def test_masthead_displays_name(self, home_page: HomePage):
        """
        Visitors see the site owner's name prominently displayed.
        
        This is the first thing visitors see - it must be correct!
        """
        # Arrange
        home_page.goto()
        
        # Act
        title = home_page.get_masthead_title()
        
        # Assert
        assert "william claytor" in title.lower()
    
    def test_tagline_communicates_experience(self, home_page: HomePage):
        """Tagline clearly states professional experience"""
        home_page.goto()
        
        tagline = home_page.get_tagline()
        
        assert "25 years" in tagline.lower()
    
    def test_scroll_indicator_navigates_to_about(self, home_page: HomePage):
        """Clicking scroll indicator takes user to About section"""
        home_page.goto()
        
        home_page.click_scroll_indicator()
        
        # Verify About section is now in view
        about = home_page.page.locator("#about")
        expect(about).to_be_in_viewport()


class TestHomepageAbout:
    """Tests for the About section"""
    
    def test_headshot_is_visible(self, home_page: HomePage):
        """Professional headshot is displayed"""
        home_page.goto()
        home_page.scroll_to_about()
        
        assert home_page.is_headshot_visible()
    
    def test_expertise_areas_are_displayed(self, home_page: HomePage):
        """All three expertise areas are shown"""
        home_page.goto()
        home_page.scroll_to_about()
        
        expertise = home_page.get_expertise_areas()
        
        assert "Software Development" in expertise
        assert "Quality Assurance" in expertise
        assert "Test Automation" in expertise
    
    def test_view_resume_button_works(self, home_page: HomePage, resume_page):
        """View Resume button navigates to resume page"""
        home_page.goto()
        home_page.scroll_to_about()
        
        home_page.click_view_resume()
        
        assert resume_page.is_loaded()


class TestHomepageProjects:
    """Tests for the Projects section"""
    
    def test_featured_projects_displayed(self, home_page: HomePage):
        """Featured projects are shown with titles"""
        home_page.goto()
        home_page.scroll_to_projects()
        
        projects = home_page.get_featured_project_titles()
        
        assert len(projects) >= 2
        assert "Alpine Resume" in projects
        assert "Alpine Markdown Presentation" in projects
    
    def test_project_card_links_work(self, home_page: HomePage):
        """Clicking a project card navigates to the project"""
        home_page.goto()
        home_page.scroll_to_projects()
        
        home_page.click_project("Alpine Resume")
        
        # Should navigate away from homepage
        assert "/projects/alpine-resume" in home_page.page.url


class TestHomepageContact:
    """Tests for the Contact section"""
    
    def test_email_is_displayed(self, home_page: HomePage):
        """Contact email is displayed"""
        home_page.goto()
        home_page.scroll_to_contact()
        
        email = home_page.get_email_address()
        
        assert "@" in email
        assert "wclaytor" in email
    
    def test_social_links_are_present(self, home_page: HomePage):
        """LinkedIn and GitHub links are present"""
        home_page.goto()
        home_page.scroll_to_contact()
        
        links = home_page.get_social_links()
        
        assert any("linkedin.com" in link for link in links)
        assert any("github.com" in link for link in links)
```

---

## Fixtures Design

### conftest.py Structure

```python
"""
conftest.py - Shared fixtures for all tests

Kent Beck says: "Set up the test fixtures as simply as possible"
Martin Fowler says: "A fixture is a known starting point for tests"
"""

import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from pages.home_page import HomePage
from pages.projects_page import ProjectsPage
from pages.resume_page import ResumePage


# Configuration
BASE_URL = "http://localhost:8000"  # Local dev server
LIVE_URL = "https://wclaytor.github.io"  # Production site


@pytest.fixture(scope="session")
def base_url(request) -> str:
    """Base URL for tests - can be overridden via command line"""
    return request.config.getoption("--base-url", default=BASE_URL)


@pytest.fixture
def home_page(page: Page, base_url: str) -> HomePage:
    """Homepage page object fixture"""
    return HomePage(page, base_url)


@pytest.fixture
def projects_page(page: Page, base_url: str) -> ProjectsPage:
    """Projects page object fixture"""
    return ProjectsPage(page, base_url)


@pytest.fixture
def resume_page(page: Page, base_url: str) -> ResumePage:
    """Resume page object fixture"""
    return ResumePage(page, base_url)


# Viewport fixtures for responsive testing
@pytest.fixture
def mobile_viewport() -> dict:
    return {"width": 375, "height": 667}


@pytest.fixture
def tablet_viewport() -> dict:
    return {"width": 768, "height": 1024}


@pytest.fixture
def desktop_viewport() -> dict:
    return {"width": 1920, "height": 1080}


@pytest.fixture
def mobile_page(browser: Browser, mobile_viewport: dict) -> Page:
    """Page with mobile viewport"""
    context = browser.new_context(viewport=mobile_viewport)
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def tablet_page(browser: Browser, tablet_viewport: dict) -> Page:
    """Page with tablet viewport"""
    context = browser.new_context(viewport=tablet_viewport)
    page = context.new_page()
    yield page
    context.close()


# Screenshot comparison fixture
@pytest.fixture
def screenshot_dir(tmp_path) -> str:
    """Directory for test screenshots"""
    return str(tmp_path / "screenshots")


# Hooks for test reporting
def pytest_runtest_makereport(item, call):
    """Capture screenshots on test failure"""
    if call.when == "call" and call.excinfo is not None:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"recordings/failures/{item.name}.png"
            page.screenshot(path=screenshot_path)
```

---

## Visual Testing Architecture

### Baseline Management

```
screenshots/baselines/
├── desktop/
│   ├── home_masthead.png
│   ├── home_about.png
│   ├── home_projects.png
│   ├── home_contact.png
│   └── projects_gallery.png
├── tablet/
│   ├── home_masthead.png
│   └── ...
└── mobile/
    ├── home_masthead.png
    └── ...
```

### Visual Test Example

```python
"""
test_homepage_visual.py - Visual regression tests for homepage
"""

import pytest
from playwright.sync_api import Page, expect


class TestHomepageVisual:
    """Visual regression tests for the homepage"""
    
    @pytest.mark.visual
    def test_masthead_visual(self, page: Page, base_url: str):
        """Masthead section matches baseline"""
        page.goto(base_url)
        
        masthead = page.locator("header.masthead")
        
        expect(masthead).to_have_screenshot(
            "home_masthead.png",
            max_diff_pixels=100,  # Allow minor antialiasing differences
        )
    
    @pytest.mark.visual
    @pytest.mark.parametrize("viewport_name,viewport", [
        ("desktop", {"width": 1920, "height": 1080}),
        ("tablet", {"width": 768, "height": 1024}),
        ("mobile", {"width": 375, "height": 667}),
    ])
    def test_full_page_responsive(
        self, browser, base_url: str, viewport_name: str, viewport: dict
    ):
        """Full page visual at different viewports"""
        context = browser.new_context(viewport=viewport)
        page = context.new_page()
        
        page.goto(base_url)
        page.wait_for_load_state("networkidle")
        
        expect(page).to_have_screenshot(
            f"home_full_{viewport_name}.png",
            full_page=True,
            max_diff_pixel_ratio=0.01,
        )
        
        context.close()
```

---

## Recording Configuration

### playwright.config.py equivalent in conftest.py

```python
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context with recording options"""
    return {
        **browser_context_args,
        "record_video_dir": "recordings/videos/",
        "record_video_size": {"width": 1280, "height": 720},
    }


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch configuration"""
    return {
        "slow_mo": 100,  # Slow down for better recordings
    }
```

### Trace Configuration

```python
# Enable tracing for debugging
@pytest.fixture
def trace_on_failure(context: BrowserContext, request):
    """Enable tracing and save on test failure"""
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    
    yield
    
    if request.node.rep_call.failed:
        trace_path = f"recordings/traces/{request.node.name}.zip"
        context.tracing.stop(path=trace_path)
    else:
        context.tracing.stop()
```

---

## Best Practices Summary

### DO

- ✅ Use descriptive test names that explain the behavior
- ✅ Keep tests independent and isolated
- ✅ Use page objects to encapsulate page structure
- ✅ Prefer role-based and accessible selectors
- ✅ Use Playwright's auto-waiting
- ✅ Keep visual baselines in version control
- ✅ Document test intent in docstrings

### DON'T

- ❌ Use `time.sleep()` - use Playwright's waiting
- ❌ Expose selectors in test files
- ❌ Create tests that depend on each other
- ❌ Test implementation details
- ❌ Ignore flaky tests - fix or remove them
- ❌ Commit recordings to git (except baselines)

---

## References

- Playwright Python Documentation: https://playwright.dev/python/
- Page Object Pattern: https://martinfowler.com/bliki/PageObject.html
- pytest Documentation: https://docs.pytest.org/
- Kent Beck's Test-Driven Development principles
- Martin Fowler's Refactoring patterns
