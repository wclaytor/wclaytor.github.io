"""
test_site_loads.py - Smoke tests to verify the site is alive.

These are the most critical tests - they verify that the site
loads at all. Run these first on every commit.

Kent Beck: "Run the fast tests first."
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData


@pytest.mark.smoke
class TestSiteLoads:
    """
    Smoke tests to verify critical pages load successfully.

    These tests should:
    - Be fast (< 5 seconds each)
    - Be reliable (never flaky)
    - Catch catastrophic failures
    """

    def test_homepage_loads(self, page: Page, base_url: str):
        """
        SM-001: Homepage loads successfully.

        The most basic test - if this fails, nothing else matters.
        """
        # Act
        response = page.goto(f"{base_url}{URLs.HOME}")

        # Assert
        assert response is not None
        assert response.ok, f"Homepage returned status {response.status}"

        # Check title contains the expected name (not exact match)
        title = page.title()
        assert TestData.HOME_PAGE_TITLE_CONTAINS in title, \
            f"Expected title to contain '{TestData.HOME_PAGE_TITLE_CONTAINS}', got '{title}'"

    def test_projects_page_loads(self, page: Page, base_url: str):
        """
        SM-002: Projects page loads successfully.
        """
        response = page.goto(f"{base_url}{URLs.PROJECTS}")

        assert response is not None
        assert response.ok, f"Projects page returned status {response.status}"

    def test_resume_page_loads(self, page: Page, base_url: str):
        """
        SM-003: Resume page loads successfully.
        """
        response = page.goto(f"{base_url}{URLs.RESUME}")

        assert response is not None
        assert response.ok, f"Resume page returned status {response.status}"

    def test_featured_project_alpine_resume_loads(self, page: Page, base_url: str):
        """
        SM-006a: Alpine Resume project loads.

        Featured projects must be accessible.
        """
        response = page.goto(f"{base_url}{URLs.ALPINE_RESUME}")

        assert response is not None
        assert response.ok, f"Alpine Resume returned status {response.status}"

    def test_featured_project_alpine_presentation_loads(self, page: Page, base_url: str):
        """
        SM-006b: Alpine Markdown Presentation project loads.
        """
        response = page.goto(f"{base_url}{URLs.ALPINE_PRESENTATION}")

        assert response is not None
        assert response.ok, f"Alpine Presentation returned status {response.status}"


@pytest.mark.smoke
class TestNoConsoleErrors:
    """
    Verify pages load without JavaScript errors.

    Console errors indicate broken functionality and should
    never appear on a professional site.
    """

    def test_homepage_no_console_errors(self, page: Page, base_url: str, console_errors: list):
        """
        SM-005: Homepage has no console errors.
        """
        page.goto(f"{base_url}{URLs.HOME}")
        page.wait_for_load_state("networkidle")

        # Filter out expected warnings (like third-party scripts)
        actual_errors = [e for e in console_errors if "error" in e.lower()]

        assert len(
            actual_errors) == 0, f"Console errors found: {actual_errors}"

    def test_projects_page_no_console_errors(self, page: Page, base_url: str, console_errors: list):
        """
        Projects page has no console errors.
        """
        page.goto(f"{base_url}{URLs.PROJECTS}")
        page.wait_for_load_state("networkidle")

        actual_errors = [e for e in console_errors if "error" in e.lower()]

        assert len(
            actual_errors) == 0, f"Console errors found: {actual_errors}"


@pytest.mark.smoke
class TestCriticalContent:
    """
    Verify critical content is present.

    These tests ensure the most important content appears on the page.
    """

    def test_homepage_has_name(self, page: Page, base_url: str):
        """
        The author's name appears on the homepage.

        This is the most important content - visitors need to know
        whose portfolio they're viewing.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Look for the name anywhere on the page
        body_text = page.locator("body").text_content() or ""

        assert "william claytor" in body_text.lower(), \
            "Author name not found on homepage"

    def test_homepage_has_navigation(self, page: Page, base_url: str):
        """
        SM-004: Navigation is visible on the homepage.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        nav = page.locator("#mainNav")

        expect(nav).to_be_visible()

    def test_homepage_has_about_section(self, page: Page, base_url: str):
        """
        Homepage has the About section.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        about = page.locator("#about")

        expect(about).to_be_attached()

    def test_homepage_has_projects_section(self, page: Page, base_url: str):
        """
        Homepage has the Projects section.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        projects = page.locator("#projects")

        expect(projects).to_be_attached()

    def test_homepage_has_contact_section(self, page: Page, base_url: str):
        """
        Homepage has the Contact section.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        contact = page.locator("#contact")

        expect(contact).to_be_attached()
