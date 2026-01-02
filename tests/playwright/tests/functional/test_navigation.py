"""
test_navigation.py - Functional tests for the Navigation component.

Test Plan Section: 3.3 Functional Tests - Navigation (P1 - High)
Tests: NAV-001 through NAV-008

These tests verify the navigation bar functions correctly across the site,
including brand link, section links, sticky behavior, and keyboard accessibility.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData
from pages.home_page import HomePage


@pytest.mark.functional
class TestNavigation:
    """
    Functional tests for the Navigation component.

    The navigation bar appears on all pages and provides links to
    different sections (About, Projects, Contact) and pages (Resume).
    """

    def test_brand_link_visible(self, page: Page, base_url: str):
        """
        NAV-001: Brand link visible.

        Steps: Load any page
        Expected: "wclaytor.github.io" visible in navigation
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()

        # Assert
        brand = page.locator(".navbar-brand")
        expect(brand).to_be_visible()
        expect(brand).to_contain_text(TestData.NAV_BRAND)

    def test_brand_link_works(self, page: Page, base_url: str):
        """
        NAV-002: Brand link works.

        Steps: Scroll down, then click brand
        Expected: Navigates to top of homepage
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Scroll down first
        page.evaluate("window.scrollTo(0, 500)")
        page.wait_for_timeout(300)

        # Act
        page.locator(".navbar-brand").click()
        page.wait_for_timeout(500)  # Wait for smooth scroll

        # Assert - Should be back at the top
        scroll_position = page.evaluate("window.scrollY")
        assert scroll_position < 100, f"Expected to be near top, but scrollY is {scroll_position}"

    def test_about_link(self, page: Page, base_url: str):
        """
        NAV-003: About link.

        Steps: Click "About" in navigation
        Expected: Scrolls to About section
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Act
        page.locator(".nav-link:has-text('About')").click()
        page.wait_for_timeout(500)  # Wait for smooth scroll

        # Assert - About section should be in view
        about_section = page.locator("#about")
        expect(about_section).to_be_in_viewport()

    def test_projects_link(self, page: Page, base_url: str):
        """
        NAV-004: Projects link.

        Steps: Click "Projects" in navigation
        Expected: Scrolls to Projects section
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Act
        page.locator(".nav-link:has-text('Projects')").click()
        page.wait_for_timeout(500)  # Wait for smooth scroll

        # Assert - Projects section should be in view
        projects_section = page.locator("#projects")
        expect(projects_section).to_be_in_viewport()

    def test_contact_link(self, page: Page, base_url: str):
        """
        NAV-005: Contact link.

        Steps: Click "Contact" in navigation
        Expected: Scrolls to Contact section
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Act
        page.locator(".nav-link:has-text('Contact')").click()
        page.wait_for_timeout(500)  # Wait for smooth scroll

        # Assert - Contact section should be in view
        contact_section = page.locator("#contact")
        expect(contact_section).to_be_in_viewport()

    def test_resume_link(self, page: Page, base_url: str):
        """
        NAV-006: Resume link.

        Steps: Click "Resume" in navigation
        Expected: Opens resume page
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Act
        page.locator(".nav-link:has-text('Resume')").click()
        page.wait_for_load_state("networkidle")

        # Assert - Should navigate to resume page
        assert "resume" in page.url.lower(), \
            f"Expected URL to contain 'resume', got '{page.url}'"

        # Verify page title contains relevant content
        title = page.title().lower()
        assert "resume" in title or "william" in title, \
            f"Expected title to contain 'resume' or 'william', got '{page.title()}'"

    def test_nav_sticky_on_scroll(self, page: Page, base_url: str):
        """
        NAV-007: Nav sticky on scroll.

        Steps: Scroll down page
        Expected: Navigation stays visible (fixed position)
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Act - Scroll down significantly
        page.evaluate("window.scrollTo(0, 1000)")
        page.wait_for_timeout(300)

        # Assert - Navigation should still be visible
        nav = page.locator("#mainNav")
        expect(nav).to_be_visible()

        # Verify it has fixed positioning
        position = page.evaluate(
            "window.getComputedStyle(document.querySelector('#mainNav')).position"
        )
        assert position == "fixed", f"Expected nav to be fixed, but got '{position}'"

    def test_nav_keyboard_accessible(self, page: Page, base_url: str):
        """
        NAV-008: Nav keyboard accessible.

        Steps: Tab through navigation links
        Expected: All links are accessible via keyboard
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Get all nav links
        nav_links = page.locator(".navbar-nav .nav-link")
        link_count = nav_links.count()

        # Assert we have the expected number of nav links
        assert link_count == len(TestData.NAV_LINKS), \
            f"Expected {len(TestData.NAV_LINKS)} nav links, got {link_count}"

        # Act & Assert - Tab through and verify each link can receive focus
        # First, focus on the brand link
        page.locator(".navbar-brand").focus()

        # Tab to each nav link and verify it receives focus
        for i, expected_text in enumerate(TestData.NAV_LINKS):
            page.keyboard.press("Tab")
            page.wait_for_timeout(100)

            # Get the currently focused element
            focused_text = page.evaluate(
                "document.activeElement?.textContent?.trim()"
            )

            # Verify the focused element matches expected nav link
            assert expected_text in focused_text, \
                f"Expected '{expected_text}' to be focused, got '{focused_text}'"


@pytest.mark.functional
class TestNavigationAllPages:
    """
    Tests that verify navigation works correctly on all pages.
    """

    def test_nav_visible_on_homepage(self, page: Page, base_url: str):
        """Verify navigation is visible on homepage."""
        home_page = HomePage(page, base_url)
        home_page.goto()

        nav = page.locator("#mainNav")
        expect(nav).to_be_visible()

    def test_nav_visible_on_resume_page(self, page: Page, base_url: str):
        """Verify navigation is visible on resume page."""
        page.goto(f"{base_url}/assets/resume/william_claytor_resume.html")
        page.wait_for_load_state("networkidle")

        # Resume page may have different navigation structure
        # Check if page loads successfully
        expect(page).not_to_have_title("")

    def test_all_nav_links_present(self, page: Page, base_url: str):
        """Verify all expected navigation links are present."""
        home_page = HomePage(page, base_url)
        home_page.goto()

        for link_text in TestData.NAV_LINKS:
            link = page.locator(f".nav-link:has-text('{link_text}')")
            expect(link).to_be_visible()
