"""
test_projects_page.py - Functional tests for the Projects Page.

Test Plan Section: 3.4 Functional Tests - Projects Page (P1 - High)
Tests: PRJ-001 through PRJ-007

These tests verify the /projects/ redirect page functions correctly,
including meta tags, redirect behavior, and fallback link.

Note: The projects page uses meta refresh with content="0" which redirects
immediately. Tests use Playwright's request API to examine the raw HTML.
"""

import pytest
import re
from playwright.sync_api import Page, expect, APIRequestContext

from fixtures.urls import URLs
from fixtures.test_data import TestData


@pytest.fixture
def projects_html(request, base_url: str):
    """Fetch the raw HTML of the projects page without browser rendering."""
    import urllib.request
    with urllib.request.urlopen(f"{base_url}/projects/") as response:
        return response.read().decode('utf-8')


@pytest.mark.functional
class TestProjectsPage:
    """
    Functional tests for the Projects Page (/projects/).

    The projects page is a redirect page that sends users to the
    #projects section of the homepage.
    """

    def test_page_loads(self, page: Page, base_url: str):
        """
        PRJ-001: Page loads.

        Steps: Navigate to /projects/
        Expected: Redirect page renders (or redirects successfully)
        """
        # Navigate to projects - will redirect
        response = page.goto(f"{base_url}/projects/")

        # Either the page loaded or we were redirected - both are valid
        assert response is not None, "Should get a response"
        assert response.ok, f"Response should be OK, got status {response.status}"

    def test_meta_redirect_present(self, projects_html: str):
        """
        PRJ-002: Meta redirect present.

        Steps: Check HTML meta tag
        Expected: Contains refresh to /#projects
        """
        # Check for meta refresh tag in HTML
        assert 'http-equiv="refresh"' in projects_html.lower() or \
               "http-equiv='refresh'" in projects_html.lower(), \
            "Meta refresh tag should exist"
        assert "#projects" in projects_html, \
            "Meta refresh should redirect to #projects"

    def test_canonical_link_present(self, projects_html: str):
        """
        PRJ-003: Canonical link present.

        Steps: Check HTML link tag
        Expected: Points to /#projects
        """
        # Check for canonical link in HTML
        assert 'rel="canonical"' in projects_html.lower() or \
               "rel='canonical'" in projects_html.lower(), \
            "Canonical link should exist"
        assert "#projects" in projects_html, \
            "Canonical link should point to #projects"

    def test_redirect_message_shown(self, projects_html: str):
        """
        PRJ-004: Redirect message shown.

        Steps: View page briefly
        Expected: "Redirecting to Projects" displayed
        """
        # Check for redirect message in HTML
        assert "Redirecting" in projects_html, \
            "Redirect message should be present in HTML"
        assert "redirect-message" in projects_html, \
            "Redirect message container should exist"

    def test_manual_link_works(self, projects_html: str):
        """
        PRJ-005: Manual link works.

        Steps: Click fallback link
        Expected: Navigates to /#projects
        """
        # Check for fallback link in HTML - should contain href to #projects
        assert 'href=' in projects_html and '#projects' in projects_html, \
            "Fallback link to #projects should exist"

        # Also verify it's a clickable link by checking for anchor tag
        assert '<a ' in projects_html.lower(), \
            "Should have anchor tag for fallback link"

    def test_automatic_redirect(self, page: Page, base_url: str):
        """
        PRJ-006: Automatic redirect.

        Steps: Wait on page
        Expected: Redirects to /#projects
        """
        # Navigate and let the redirect happen
        page.goto(f"{base_url}/projects/")
        page.wait_for_load_state("networkidle")

        # Wait for redirect to complete
        page.wait_for_timeout(1000)

        # Should have been redirected
        current_url = page.url

        # Accept valid redirect destinations:
        # - Production URL with #projects
        # - Local URL (base_url)
        # - Any URL with #projects hash
        is_valid = (
            "#projects" in current_url or
            "wclaytor.github.io" in current_url or
            current_url.rstrip("/") == base_url.rstrip("/")
        )
        assert is_valid, \
            f"Should redirect to homepage or #projects, got: {current_url}"

    def test_spinner_animation(self, projects_html: str):
        """
        PRJ-007: Spinner animation.

        Steps: View page briefly
        Expected: Loading spinner visible
        """
        # Check for spinner in HTML
        assert "spinner" in projects_html.lower(), \
            "Spinner element should exist in HTML"

        # Check for spin animation in CSS
        assert "@keyframes spin" in projects_html or "animation" in projects_html, \
            "Spinner animation should be defined"


@pytest.mark.functional
class TestProjectsPageStructure:
    """
    Additional tests for the Projects Page structure and SEO.
    """

    def test_page_has_proper_title(self, projects_html: str):
        """Verify the page has a descriptive title."""
        # Check for title tag
        assert "<title>" in projects_html.lower(), "Page should have a title tag"

        # Extract title content
        title_match = re.search(r'<title>(.*?)</title>',
                                projects_html, re.IGNORECASE)
        assert title_match, "Should be able to extract title"
        title = title_match.group(1)
        assert len(title) > 5, f"Title should be descriptive, got: {title}"

    def test_fallback_link_is_accessible(self, projects_html: str):
        """Verify the fallback link exists for users with JS disabled."""
        # Check that there's a visible fallback link
        assert "click here" in projects_html.lower() or \
               "if you are not redirected" in projects_html.lower(), \
            "Should have fallback instructions for users"

        # Verify it's a proper link
        assert '<a ' in projects_html and 'href=' in projects_html, \
            "Fallback should be a proper anchor element"
