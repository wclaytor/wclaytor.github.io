"""
test_homepage_contact.py - Functional tests for the Homepage Contact section.

Test Plan Section: 3.2.4 Contact Section
Tests: HP-C-001 through HP-C-005

These tests verify the Contact section of the homepage displays correctly,
including email address, email link, and social media links (LinkedIn, GitHub).
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData
from pages.home_page import HomePage


@pytest.mark.functional
class TestHomepageContact:
    """
    Functional tests for the Homepage Contact section.

    The Contact section contains:
    - Email address and mailto link
    - Social media links (LinkedIn, GitHub)
    """

    def test_email_displayed(self, page: Page, base_url: str):
        """
        HP-C-001: Email address is displayed.

        Steps: Load homepage, scroll to Contact section
        Expected: Email address is visible
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_contact()

        # Assert
        assert home_page.is_contact_section_visible(), \
            "Contact section should be visible"

        email = home_page.get_email_address()
        assert email, "Email address should be displayed"
        assert "@" in email, f"Should be a valid email format, got: '{email}'"
        assert TestData.EMAIL == email, \
            f"Expected email '{TestData.EMAIL}', got: '{email}'"

    def test_email_link_works(self, page: Page, base_url: str):
        """
        HP-C-002: Email link works.

        Steps: Load homepage, click email link
        Expected: Link has correct mailto: href
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_contact()

        # Assert - Verify the mailto link is correctly formed
        email_link = page.locator(f"a[href^='mailto:']")
        expect(email_link).to_be_visible()

        href = email_link.get_attribute("href")
        assert href is not None, "Email link should have href attribute"
        assert href.startswith("mailto:"), \
            f"Email link should be a mailto: link, got: '{href}'"
        assert TestData.EMAIL in href, \
            f"Email link should contain '{TestData.EMAIL}', got: '{href}'"

    def test_linkedin_link(self, page: Page, base_url: str):
        """
        HP-C-003: LinkedIn link works.

        Steps: Load homepage, verify LinkedIn link
        Expected: LinkedIn link opens profile (new tab)
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_contact()

        # Assert
        assert home_page.has_linkedin_link(), \
            "LinkedIn link should be present"

        linkedin_link = page.locator("a[href*='linkedin.com']")
        expect(linkedin_link).to_be_visible()

        # Verify the href points to LinkedIn
        href = linkedin_link.get_attribute("href")
        assert href is not None, "LinkedIn link should have href"
        assert "linkedin.com" in href, \
            f"LinkedIn link should point to linkedin.com, got: '{href}'"

        # Verify accessibility label is present
        aria_label = linkedin_link.get_attribute("aria-label")
        assert aria_label is not None, \
            "LinkedIn link should have aria-label for accessibility"

    def test_github_link(self, page: Page, base_url: str):
        """
        HP-C-004: GitHub link works.

        Steps: Load homepage, verify GitHub link
        Expected: GitHub link opens profile (new tab)
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_contact()

        # Assert
        assert home_page.has_github_link(), \
            "GitHub link should be present"

        github_link = page.locator("a[href*='github.com']")
        expect(github_link).to_be_visible()

        # Verify the href points to GitHub
        href = github_link.get_attribute("href")
        assert href is not None, "GitHub link should have href"
        assert "github.com" in href, \
            f"GitHub link should point to github.com, got: '{href}'"

        # Verify accessibility label is present
        aria_label = github_link.get_attribute("aria-label")
        assert aria_label is not None, \
            "GitHub link should have aria-label for accessibility"

    def test_social_links_accessible(self, page: Page, base_url: str):
        """
        HP-C-005: Social links are keyboard accessible.

        Steps: Load homepage, tab through social links
        Expected: All social links are keyboard accessible
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_contact()

        # Get all social links
        social_links = page.locator(".social a")
        link_count = social_links.count()

        assert link_count >= 2, \
            f"Should have at least 2 social links, found: {link_count}"

        # Verify each social link can receive focus
        for i in range(link_count):
            link = social_links.nth(i)

            # Focus the link
            link.focus()

            # Verify it received focus
            expect(link).to_be_focused()

            # Verify it has an accessible name (aria-label or text content)
            aria_label = link.get_attribute("aria-label")
            text_content = link.text_content()
            assert aria_label or text_content, \
                f"Social link {i} should have accessible name (aria-label or text)"
