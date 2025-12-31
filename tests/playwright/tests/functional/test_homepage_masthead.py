"""
test_homepage_masthead.py - Functional tests for the Homepage Masthead section.

Test Plan Section: 3.2.1 Masthead Section
Tests: HP-M-001 through HP-M-005

These tests verify the hero/masthead section of the homepage displays correctly
and that interactive elements (scroll indicator) function properly.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData
from pages.home_page import HomePage


@pytest.mark.functional
class TestHomepageMasthead:
    """
    Functional tests for the Homepage Masthead section.

    The masthead is the hero area at the top of the homepage,
    containing the name, tagline, subtitle, and scroll indicator.
    """

    def test_name_is_displayed(self, page: Page, base_url: str):
        """
        HP-M-001: Name is displayed in masthead.

        Steps: Load homepage
        Expected: "William Claytor" visible in masthead
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()

        # Assert
        assert home_page.is_masthead_visible(), "Masthead should be visible"

        masthead_title = home_page.get_masthead_title()
        assert TestData.MASTHEAD_TITLE.lower() in masthead_title.lower(), \
            f"Expected masthead to contain '{TestData.MASTHEAD_TITLE}', got '{masthead_title}'"

    def test_tagline_is_displayed(self, page: Page, base_url: str):
        """
        HP-M-002: Tagline is displayed.

        Steps: Load homepage
        Expected: "25 Years" mentioned in tagline
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()

        # Assert
        tagline = home_page.get_tagline()
        assert TestData.TAGLINE_CONTAINS in tagline, \
            f"Expected tagline to contain '{TestData.TAGLINE_CONTAINS}', got '{tagline}'"

    def test_subtitle_is_displayed(self, page: Page, base_url: str):
        """
        HP-M-003: Subtitle is displayed.

        Steps: Load homepage
        Expected: "Senior Software Engineer" visible in subtitle
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()

        # Assert
        subtitle = home_page.get_subtitle()
        assert TestData.SUBTITLE_CONTAINS in subtitle, \
            f"Expected subtitle to contain '{TestData.SUBTITLE_CONTAINS}', got '{subtitle}'"

    def test_scroll_indicator_works(self, page: Page, base_url: str):
        """
        HP-M-004: Scroll indicator works.

        Steps: Click scroll indicator
        Expected: Page scrolls to About section
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Verify scroll indicator is visible
        assert home_page.is_scroll_indicator_visible(), \
            "Scroll indicator should be visible"

        # Act
        home_page.click_scroll_indicator()

        # Assert - About section should be in view
        about_section = page.locator("#about")
        expect(about_section).to_be_in_viewport()

    def test_scroll_indicator_keyboard_accessible(self, page: Page, base_url: str):
        """
        HP-M-005: Scroll indicator is keyboard accessible.

        Steps: Tab to indicator, press Enter
        Expected: Page scrolls to About section
        """
        # Arrange
        home_page = HomePage(page, base_url)
        home_page.goto()

        # Find the scroll indicator
        scroll_indicator = page.locator("#scrollIndicator")

        # Act - Focus and activate with keyboard
        scroll_indicator.focus()

        # Verify it can receive focus (has focus state)
        expect(scroll_indicator).to_be_focused()

        # Press Enter to activate
        scroll_indicator.press("Enter")

        # Wait for smooth scroll animation
        page.wait_for_timeout(500)

        # Assert - About section should be in view
        about_section = page.locator("#about")
        expect(about_section).to_be_in_viewport()
