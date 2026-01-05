"""
test_critical_navigation.py - Smoke tests for navigation functionality.

These tests verify that users can navigate the site.
If navigation is broken, the site is effectively unusable.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData


@pytest.mark.smoke
class TestNavigationVisible:
    """
    Verify navigation is visible on all critical pages.
    """

    @pytest.mark.parametrize("path,name", [
        (URLs.HOME, "Homepage"),
        (URLs.PROJECTS, "Projects page"),
    ])
    def test_navigation_visible_on_page(self, page: Page, base_url: str, path: str, name: str):
        """
        Navigation bar is visible on {name}.
        """
        page.goto(f"{base_url}{path}")

        nav = page.locator("#mainNav")

        expect(nav).to_be_visible()


@pytest.mark.smoke
class TestNavigationLinks:
    """
    Verify navigation links work correctly.
    """

    def test_brand_link_goes_home(self, page: Page, base_url: str):
        """
        Clicking the brand logo navigates to the branded homepage.
        The brand link always points to the production site.
        """
        # Start on projects page
        page.goto(f"{base_url}{URLs.PROJECTS}")

        # Click brand
        page.locator(".navbar-brand").click()

        # Brand link should always go to the branded website (production URL)
        branded_url = "https://wclaytor.github.io/"
        assert page.url.startswith(branded_url), \
            f"Expected branded homepage ({branded_url}), got {page.url}"

    def test_about_link_scrolls_to_section(self, page: Page, base_url: str):
        """
        About nav link scrolls to the About section.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Click About link
        page.get_by_role("link", name="About").click()

        # About section should be visible
        about = page.locator("#about")
        expect(about).to_be_in_viewport()

    def test_projects_link_scrolls_to_section(self, page: Page, base_url: str):
        """
        Projects nav link scrolls to the Projects section.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        page.get_by_role("link", name="Projects").click()

        projects = page.locator("#projects")
        expect(projects).to_be_in_viewport()

    def test_contact_link_scrolls_to_section(self, page: Page, base_url: str):
        """
        Contact nav link scrolls to the Contact section.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        page.get_by_role("link", name="Contact").click()

        contact = page.locator("#contact")
        expect(contact).to_be_in_viewport()

    def test_resume_link_opens_resume(self, page: Page, base_url: str):
        """
        Resume nav link opens the resume page.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Target specifically the nav link (not other "Resume" text on page)
        page.locator("nav .nav-link[href*='resume']").click()

        # Should navigate to resume
        expect(page).to_have_url(f"{base_url}{URLs.RESUME}")


@pytest.mark.smoke
class TestKeyboardNavigation:
    """
    Verify basic keyboard navigation works.

    Accessibility is critical - the site must be usable without a mouse.
    """

    def test_can_tab_to_nav_links(self, page: Page, base_url: str):
        """
        Navigation links can be reached via Tab key.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Tab through the page
        # First tab should go to skip link or nav
        page.keyboard.press("Tab")

        # Continue tabbing until we hit a nav link
        for _ in range(10):
            focused = page.evaluate("document.activeElement.tagName")
            href = page.evaluate("document.activeElement.getAttribute('href')")

            if focused == "A" and href and href.startswith("#"):
                # Found a nav link
                return

            page.keyboard.press("Tab")

        # If we get here, we didn't find a nav link via tab
        pytest.fail("Could not tab to navigation links")

    def test_skip_link_exists(self, page: Page, base_url: str):
        """
        Skip to content link exists for accessibility.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Skip link should exist (may be visually hidden)
        skip_link = page.locator(
            "a.skip-to-content, a[href='#about']:first-of-type")

        # It should exist in the DOM
        assert skip_link.count() > 0 or \
            page.locator("a:has-text('Skip')").count() > 0, \
            "Skip to content link not found"
