"""
test_homepage_projects.py - Functional tests for the Homepage Projects section.

Test Plan Section: 3.2.3 Projects Section
Tests: HP-P-001 through HP-P-008

These tests verify the Projects section of the homepage displays correctly,
including featured projects (Alpine Resume, Alpine Presentation) and
experimental projects (Background Transformer, Dynamic Resume).
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData
from pages.home_page import HomePage


@pytest.mark.functional
class TestHomepageProjects:
    """
    Functional tests for the Homepage Projects section.

    The Projects section contains:
    - Featured Projects: Alpine Resume, Alpine Markdown Presentation
    - Experiments: Background Transformer, Dynamic Resume
    """

    def test_section_heading_visible(self, page: Page, base_url: str):
        """
        HP-P-001: Section heading is visible.

        Steps: Load homepage, scroll to Projects section
        Expected: "Featured Projects" heading is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Assert
        assert home_page.is_projects_section_visible(), \
            "Projects section should be visible"

        heading = home_page.get_projects_heading()
        assert "Featured Projects" in heading, \
            f"Expected 'Featured Projects' heading, got: '{heading}'"

    def test_alpine_resume_card(self, page: Page, base_url: str):
        """
        HP-P-002: Alpine Resume card is displayed.

        Steps: Load homepage, view Projects section
        Expected: Card with title, description, and badges is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Assert
        project_titles = home_page.get_featured_project_titles()
        assert "Alpine Resume" in project_titles, \
            f"Alpine Resume should be in featured projects, got: {project_titles}"

        # Verify card has badges
        alpine_resume_card = page.locator(
            ".card:has(.card-title:has-text('Alpine Resume'))")
        badges = alpine_resume_card.locator(".badge")
        assert badges.count() >= 2, \
            f"Alpine Resume card should have badges, found: {badges.count()}"

    def test_alpine_resume_link(self, page: Page, base_url: str):
        """
        HP-P-003: Alpine Resume link works.

        Steps: Click "View Project" on Alpine Resume card
        Expected: Navigates to Alpine Resume project page
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Click the View Project button
        home_page.click_project_view_button("Alpine Resume")

        # Wait for navigation
        page.wait_for_load_state("domcontentloaded")

        # Assert - Should navigate to Alpine Resume project
        assert "alpine-resume" in page.url.lower(), \
            f"Should navigate to Alpine Resume project, but URL is: {page.url}"

    def test_alpine_presentation_card(self, page: Page, base_url: str):
        """
        HP-P-004: Alpine Markdown Presentation card is displayed.

        Steps: Load homepage, view Projects section
        Expected: Card with title, description, and badges is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Assert
        project_titles = home_page.get_featured_project_titles()
        assert "Alpine Markdown Presentation" in project_titles, \
            f"Alpine Markdown Presentation should be in featured projects, got: {project_titles}"

        # Verify card has badges
        presentation_card = page.locator(
            ".card:has(.card-title:has-text('Alpine Markdown Presentation'))")
        badges = presentation_card.locator(".badge")
        assert badges.count() >= 2, \
            f"Alpine Presentation card should have badges, found: {badges.count()}"

    def test_alpine_presentation_link(self, page: Page, base_url: str):
        """
        HP-P-005: Alpine Markdown Presentation link works.

        Steps: Click "View Project" on Alpine Presentation card
        Expected: Navigates to Alpine Presentation project page
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Click the View Project button
        home_page.click_project_view_button("Alpine Markdown Presentation")

        # Wait for navigation
        page.wait_for_load_state("domcontentloaded")

        # Assert - Should navigate to Alpine Presentation project
        assert "alpine-markdown-presentation" in page.url.lower(), \
            f"Should navigate to Alpine Presentation project, but URL is: {page.url}"

    def test_experiments_section_visible(self, page: Page, base_url: str):
        """
        HP-P-006: Experiments section is visible.

        Steps: Load homepage, scroll past Featured Projects
        Expected: Experiments section is visible
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Scroll a bit more to ensure experiments are in view
        experiments = page.locator(".experiments-section")
        experiments.scroll_into_view_if_needed()

        # Assert
        assert home_page.is_experiments_section_visible(), \
            "Experiments section should be visible"

        # Verify "Experiments" heading is present
        experiments_heading = page.locator(".experiments-section h3")
        expect(experiments_heading).to_contain_text("Experiments")

    def test_background_transformer_card(self, page: Page, base_url: str):
        """
        HP-P-007: Background Transformer card is displayed.

        Steps: Load homepage, view Experiments section
        Expected: Card with "Experiment" badge is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Assert
        experiment_titles = home_page.get_experiment_project_titles()
        assert "Background Transformer" in experiment_titles, \
            f"Background Transformer should be in experiments, got: {experiment_titles}"

        # Verify the Experiment badge
        transformer_card = page.locator(
            ".experiment-card:has(.card-title:has-text('Background Transformer'))")
        experiment_badge = transformer_card.locator(
            ".badge:has-text('Experiment')")
        expect(experiment_badge).to_be_visible()

    def test_dynamic_resume_card(self, page: Page, base_url: str):
        """
        HP-P-008: Dynamic Resume card is displayed.

        Steps: Load homepage, view Experiments section
        Expected: Card with "Experiment" badge is displayed
        """
        # Arrange
        home_page = HomePage(page, base_url)

        # Act
        home_page.goto()
        home_page.scroll_to_projects()

        # Assert
        experiment_titles = home_page.get_experiment_project_titles()
        assert "Dynamic Resume" in experiment_titles, \
            f"Dynamic Resume should be in experiments, got: {experiment_titles}"

        # Verify the Experiment badge
        resume_card = page.locator(
            ".experiment-card:has(.card-title:has-text('Dynamic Resume'))")
        experiment_badge = resume_card.locator(".badge:has-text('Experiment')")
        expect(experiment_badge).to_be_visible()
