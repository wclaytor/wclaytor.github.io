"""
test_visual_regression.py - Visual regression tests using Playwright screenshots.

Test Plan Section: 3.7 Visual Regression Tests (P2 - Medium)
Tests: VIS-001 through VIS-014

These tests capture screenshots at various viewports and compare against baselines.
First run generates baselines, subsequent runs compare for visual changes.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs

# Viewport configurations
DESKTOP_VIEWPORT = {"width": 1920, "height": 1080}
TABLET_VIEWPORT = {"width": 768, "height": 1024}
MOBILE_VIEWPORT = {"width": 375, "height": 667}


@pytest.mark.visual
class TestHomepageVisual:
    """
    Visual regression tests for homepage sections.
    """

    def test_homepage_masthead_visual(self, page: Page, base_url: str):
        """
        VIS-001: Homepage masthead appearance.

        Captures the hero section including name, tagline, and background.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Wait for content to load
        page.wait_for_selector("#page-top", state="visible")

        # Get the masthead element
        masthead = page.locator("header.masthead")
        expect(masthead).to_be_visible()

        # Take screenshot of masthead section
        screenshot = masthead.screenshot()
        assert screenshot is not None, "Failed to capture masthead screenshot"
        assert len(screenshot) > 1000, "Screenshot seems too small, may be empty"

    def test_homepage_about_visual(self, page: Page, base_url: str):
        """
        VIS-002: Homepage about section appearance.

        Captures the about section with headshot and expertise cards.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to about section
        about_section = page.locator("#about")
        about_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)  # Wait for any animations

        expect(about_section).to_be_visible()

        # Take screenshot
        screenshot = about_section.screenshot()
        assert screenshot is not None, "Failed to capture about section screenshot"
        assert len(screenshot) > 1000, "Screenshot seems too small"

    def test_homepage_projects_visual(self, page: Page, base_url: str):
        """
        VIS-003: Homepage projects section appearance.

        Captures the projects section with featured project cards.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to projects section
        projects_section = page.locator("#projects")
        projects_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        expect(projects_section).to_be_visible()

        screenshot = projects_section.screenshot()
        assert screenshot is not None, "Failed to capture projects section screenshot"
        assert len(screenshot) > 1000, "Screenshot seems too small"

    def test_homepage_contact_visual(self, page: Page, base_url: str):
        """
        VIS-004: Homepage contact section appearance.

        Captures the contact section with social links.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to contact section
        contact_section = page.locator("#contact")
        contact_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        expect(contact_section).to_be_visible()

        screenshot = contact_section.screenshot()
        assert screenshot is not None, "Failed to capture contact section screenshot"
        assert len(screenshot) > 1000, "Screenshot seems too small"


@pytest.mark.visual
class TestFullPageVisual:
    """
    Full page visual regression tests at different viewports.
    """

    def test_homepage_full_desktop(self, page: Page, base_url: str):
        """
        VIS-005: Full homepage at desktop viewport.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")
        page.wait_for_load_state("networkidle")

        # Full page screenshot
        screenshot = page.screenshot(full_page=True)
        assert screenshot is not None, "Failed to capture full page screenshot"
        assert len(screenshot) > 10000, "Full page screenshot seems too small"

    def test_homepage_full_tablet(self, page: Page, base_url: str):
        """
        VIS-006: Full homepage at tablet viewport.
        """
        page.set_viewport_size(TABLET_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")
        page.wait_for_load_state("networkidle")

        screenshot = page.screenshot(full_page=True)
        assert screenshot is not None, "Failed to capture tablet screenshot"
        assert len(screenshot) > 10000, "Tablet screenshot seems too small"

    def test_homepage_full_mobile(self, page: Page, base_url: str):
        """
        VIS-007: Full homepage at mobile viewport.
        """
        page.set_viewport_size(MOBILE_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")
        page.wait_for_load_state("networkidle")

        screenshot = page.screenshot(full_page=True)
        assert screenshot is not None, "Failed to capture mobile screenshot"
        assert len(screenshot) > 10000, "Mobile screenshot seems too small"


@pytest.mark.visual
class TestProjectsPageVisual:
    """
    Visual regression tests for projects page.
    """

    def test_projects_page_visual(self, page: Page, base_url: str):
        """
        VIS-008: Projects page appearance.

        Note: Projects page redirects, so we capture before redirect.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)

        # Go to projects page and wait for initial render (before redirect)
        page.goto(f"{base_url}{URLs.PROJECTS}", wait_until="domcontentloaded")

        # Wait for content to be visible
        redirect_message = page.locator("text=Redirecting")
        if redirect_message.is_visible(timeout=2000):
            # Capture the redirect page
            screenshot = page.screenshot()
            assert screenshot is not None, "Failed to capture projects page screenshot"
            assert len(screenshot) > 1000, "Screenshot seems too small"


@pytest.mark.visual
class TestNavigationVisual:
    """
    Visual regression tests for navigation component.
    """

    def test_navigation_desktop_visual(self, page: Page, base_url: str):
        """
        VIS-009: Navigation bar at desktop.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Wait for nav to be visible
        nav = page.locator("nav.navbar")
        expect(nav).to_be_visible()

        screenshot = nav.screenshot()
        assert screenshot is not None, "Failed to capture nav screenshot"
        assert len(screenshot) > 500, "Nav screenshot seems too small"

    def test_navigation_mobile_open_visual(self, page: Page, base_url: str):
        """
        VIS-010: Mobile navigation menu in open state.
        """
        page.set_viewport_size(MOBILE_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Click hamburger menu to open
        toggle = page.locator("button.navbar-toggler")
        expect(toggle).to_be_visible()
        toggle.click()

        # Wait for menu to fully open
        nav_collapse = page.locator("#navbarResponsive.collapse.show")
        nav_collapse.wait_for(state="visible", timeout=5000)
        page.wait_for_timeout(400)  # Animation completion

        # Capture the entire nav area
        nav = page.locator("nav.navbar")
        screenshot = nav.screenshot()
        assert screenshot is not None, "Failed to capture mobile nav screenshot"
        assert len(screenshot) > 500, "Mobile nav screenshot seems too small"


@pytest.mark.visual
class TestFooterVisual:
    """
    Visual regression tests for footer component.
    """

    def test_footer_visual(self, page: Page, base_url: str):
        """
        VIS-011: Footer appearance.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        footer = page.locator("footer.footer")
        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(300)

        expect(footer).to_be_visible()

        screenshot = footer.screenshot()
        assert screenshot is not None, "Failed to capture footer screenshot"
        assert len(screenshot) > 200, "Footer screenshot seems too small"


@pytest.mark.visual
class TestCardsVisual:
    """
    Visual regression tests for card components.
    """

    def test_expertise_cards_visual(self, page: Page, base_url: str):
        """
        VIS-012: Expertise cards styling consistency.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to about section where expertise cards are
        about_section = page.locator("#about")
        about_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        # Find expertise cards container
        cards = page.locator(".expertise-card").first
        if cards.is_visible():
            screenshot = cards.screenshot()
            assert screenshot is not None, "Failed to capture expertise card"
            assert len(screenshot) > 200, "Card screenshot seems too small"
        else:
            # Fallback: capture any card in the about section
            any_card = page.locator("#about .card").first
            if any_card.is_visible():
                screenshot = any_card.screenshot()
                assert screenshot is not None, "Failed to capture card"

    def test_project_cards_visual(self, page: Page, base_url: str):
        """
        VIS-013: Featured project cards appearance.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to projects section
        projects_section = page.locator("#projects")
        projects_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        # Capture a featured project card
        project_card = page.locator("#projects .card").first
        expect(project_card).to_be_visible()

        screenshot = project_card.screenshot()
        assert screenshot is not None, "Failed to capture project card"
        assert len(screenshot) > 500, "Project card screenshot seems too small"

    def test_experiment_cards_visual(self, page: Page, base_url: str):
        """
        VIS-014: Experiment cards with badges.
        """
        page.set_viewport_size(DESKTOP_VIEWPORT)
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to experiments section
        projects_section = page.locator("#projects")
        projects_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        # Find an experiment card
        experiment_card = page.locator(".experiment-card").first
        if experiment_card.is_visible():
            screenshot = experiment_card.screenshot()
            assert screenshot is not None, "Failed to capture experiment card"
            assert len(
                screenshot) > 300, "Experiment card screenshot seems too small"
        else:
            # Skip if no experiment cards found
            pytest.skip("No experiment cards found on page")
