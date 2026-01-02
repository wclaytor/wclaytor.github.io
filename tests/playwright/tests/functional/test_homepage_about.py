"""
test_homepage_about.py - Functional tests for the Homepage About section.

Test Plan Section: 3.2.2 About Section
Tests: HP-A-001 through HP-A-008

These tests verify the About section of the homepage displays correctly,
including the headshot, bio text, expertise cards, and View Resume button.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData
from pages.home_page import HomePage


@pytest.mark.functional
class TestHomepageAbout:
    """
    Functional tests for the Homepage About section.

    The About section contains the headshot, bio paragraphs,
    expertise cards (Software Development, Quality Assurance, Test Automation),
    and the View Resume call-to-action button.
    """

    def test_headshot_is_visible(self, page: Page, base_url: str):
        """
        HP-A-001: Headshot is visible.

        Steps: Load homepage, scroll to About section
        Expected: Profile image is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Assert
        assert home_page.is_headshot_visible(), \
            "Headshot image should be visible in the About section"

    def test_headshot_has_alt_text(self, page: Page, base_url: str):
        """
        HP-A-002: Headshot has alt text.

        Steps: Load homepage, inspect headshot image
        Expected: Meaningful alt text is present
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Assert
        alt_text = home_page.get_headshot_alt_text()
        assert alt_text, "Headshot should have alt text"
        assert len(alt_text) > 10, \
            f"Alt text should be meaningful, got: '{alt_text}'"
        # Should contain the name for proper identification
        assert "William" in alt_text or "Claytor" in alt_text, \
            f"Alt text should identify the person, got: '{alt_text}'"

    def test_bio_text_is_displayed(self, page: Page, base_url: str):
        """
        HP-A-003: Bio text is displayed.

        Steps: Load homepage, scroll to About section
        Expected: Biography paragraphs are visible
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Assert
        lead_text = home_page.get_about_lead_text()
        assert lead_text, "About lead paragraph should have text"
        assert len(lead_text) > 50, \
            f"Bio text should be substantial, got {len(lead_text)} characters"

    def test_software_development_card(self, page: Page, base_url: str):
        """
        HP-A-004: Software Development expertise card.

        Steps: Load homepage, scroll to Expertise section
        Expected: Card with relevant skills is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Assert
        expertise_areas = home_page.get_expertise_areas()
        assert "Software Development" in expertise_areas, \
            f"Software Development card should be present, got: {expertise_areas}"

        # Verify the card has appropriate skill tags
        # Software Development is the first card (index 0)
        tags = home_page.get_expertise_tags(card_index=0)
        assert len(tags) > 0, "Software Development card should have skill tags"
        # Check for at least one expected skill
        expected_skills = TestData.DEV_SKILLS
        found_skills = [tag for tag in tags if tag in expected_skills]
        assert len(found_skills) > 0, \
            f"Expected skills from {expected_skills}, found: {tags}"

    def test_quality_assurance_card(self, page: Page, base_url: str):
        """
        HP-A-005: Quality Assurance expertise card.

        Steps: Load homepage, scroll to Expertise section
        Expected: Card with relevant skills is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Assert
        expertise_areas = home_page.get_expertise_areas()
        assert "Quality Assurance" in expertise_areas, \
            f"Quality Assurance card should be present, got: {expertise_areas}"

        # Verify the card has appropriate skill tags
        # Quality Assurance is the second card (index 1)
        tags = home_page.get_expertise_tags(card_index=1)
        assert len(tags) > 0, "Quality Assurance card should have skill tags"
        # Check for at least one expected skill
        expected_skills = TestData.QA_SKILLS
        found_skills = [tag for tag in tags if tag in expected_skills]
        assert len(found_skills) > 0, \
            f"Expected skills from {expected_skills}, found: {tags}"

    def test_test_automation_card(self, page: Page, base_url: str):
        """
        HP-A-006: Test Automation expertise card.

        Steps: Load homepage, scroll to Expertise section
        Expected: Card with relevant skills is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Assert
        expertise_areas = home_page.get_expertise_areas()
        assert "Test Automation" in expertise_areas, \
            f"Test Automation card should be present, got: {expertise_areas}"

        # Verify the card has appropriate skill tags
        # Test Automation is the third card (index 2)
        tags = home_page.get_expertise_tags(card_index=2)
        assert len(tags) > 0, "Test Automation card should have skill tags"
        # Check for at least one expected skill
        expected_skills = TestData.AUTOMATION_SKILLS
        found_skills = [tag for tag in tags if tag in expected_skills]
        assert len(found_skills) > 0, \
            f"Expected skills from {expected_skills}, found: {tags}"

    def test_view_resume_button(self, page: Page, base_url: str):
        """
        HP-A-007: View Resume button works.

        Steps: Load homepage, scroll to About, click View Resume button
        Expected: Navigates to resume page
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Verify button is visible
        assert home_page.is_view_resume_button_visible(), \
            "View Resume button should be visible"

        # Click the button
        home_page.click_view_resume()

        # Assert - Should navigate to resume page
        page.wait_for_load_state("domcontentloaded")
        assert URLs.RESUME in page.url or "resume" in page.url.lower(), \
            f"Should navigate to resume page, but URL is: {page.url}"

    def test_view_resume_keyboard_accessible(self, page: Page, base_url: str):
        """
        HP-A-008: View Resume button is keyboard accessible.

        Steps: Load homepage, tab to View Resume button, press Enter
        Expected: Navigates to resume page
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_about()

        # Find the View Resume button/link
        resume_btn = page.locator(".about-cta a")
        expect(resume_btn).to_be_visible()

        # Focus the button
        resume_btn.focus()

        # Verify it can receive focus
        expect(resume_btn).to_be_focused()

        # Press Enter to activate
        resume_btn.press("Enter")

        # Wait for navigation
        page.wait_for_load_state("domcontentloaded")

        # Assert - Should navigate to resume page
        assert URLs.RESUME in page.url or "resume" in page.url.lower(), \
            f"Should navigate to resume page, but URL is: {page.url}"
