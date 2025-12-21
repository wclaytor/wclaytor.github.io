"""
projects_page.py - Page object for the projects gallery.

This page object encapsulates interactions with the projects listing page
(/projects/index.html), which showcases all available projects.
"""

from pages.base_page import BasePage
from playwright.sync_api import Page


class ProjectsPage(BasePage):
    """
    Page object for the projects gallery page (/projects/).
    
    Usage:
        def test_projects_page(projects_page):
            projects_page.goto()
            assert projects_page.is_showcase_visible()
    """
    
    @property
    def path(self) -> str:
        return "/projects/"
    
    # =========================================================================
    # Selectors (Private)
    # =========================================================================
    
    _MASTHEAD = "header.masthead"
    _MASTHEAD_TITLE = "header.masthead h1"
    _MASTHEAD_SUBTITLE = "header.masthead h2"
    
    _SHOWCASE_SECTION = "#showcase"
    _PROJECT_ROWS = ".projects-section .row"
    _PROJECT_TITLE = ".project-text h4"
    _PROJECT_DESCRIPTION = ".project-text p"
    _PROJECT_LINK = ".project-text a.btn"
    
    # Specific projects
    _ALPINE_RESUME_SECTION = ".project-text:has(h4:has-text('Alpine Resume'))"
    _ALPINE_PRESENTATION_SECTION = ".project-text:has(h4:has-text('Alpine Markdown Presentation'))"
    
    # =========================================================================
    # Masthead Methods
    # =========================================================================
    
    def is_masthead_visible(self) -> bool:
        """Check if the masthead is visible."""
        return self.is_visible(self._MASTHEAD)
    
    def get_masthead_title(self) -> str:
        """Get the masthead title."""
        return self.get_text(self._MASTHEAD_TITLE)
    
    def get_masthead_subtitle(self) -> str:
        """Get the masthead subtitle."""
        return self.get_text(self._MASTHEAD_SUBTITLE)
    
    # =========================================================================
    # Showcase Section Methods
    # =========================================================================
    
    def is_showcase_visible(self) -> bool:
        """Check if the showcase section is visible."""
        return self.is_visible(self._SHOWCASE_SECTION)
    
    def scroll_to_showcase(self) -> None:
        """Scroll to the showcase section."""
        self.scroll_to_element(self._SHOWCASE_SECTION)
    
    def get_project_titles(self) -> list[str]:
        """
        Get all project titles.
        
        Returns:
            List of project titles
        """
        titles = self.page.locator(self._PROJECT_TITLE)
        return titles.all_text_contents()
    
    def get_project_count(self) -> int:
        """Get the number of projects displayed."""
        return self.page.locator(self._PROJECT_TITLE).count()
    
    # =========================================================================
    # Alpine Resume Project
    # =========================================================================
    
    def is_alpine_resume_visible(self) -> bool:
        """Check if Alpine Resume project is visible."""
        return self.page.locator(self._ALPINE_RESUME_SECTION).count() > 0
    
    def get_alpine_resume_description(self) -> str:
        """Get the Alpine Resume project description."""
        section = self.page.locator(self._ALPINE_RESUME_SECTION)
        return section.locator("p").text_content() or ""
    
    def click_alpine_resume_link(self) -> None:
        """Click the Alpine Resume 'Visit Site' button."""
        section = self.page.locator(self._ALPINE_RESUME_SECTION)
        section.locator("a.btn").click()
    
    # =========================================================================
    # Alpine Markdown Presentation Project
    # =========================================================================
    
    def is_alpine_presentation_visible(self) -> bool:
        """Check if Alpine Markdown Presentation is visible."""
        return self.page.locator(self._ALPINE_PRESENTATION_SECTION).count() > 0
    
    def get_alpine_presentation_description(self) -> str:
        """Get the Alpine Presentation project description."""
        section = self.page.locator(self._ALPINE_PRESENTATION_SECTION)
        return section.locator("p").text_content() or ""
    
    def click_alpine_presentation_link(self) -> None:
        """Click the Alpine Presentation 'Visit Site' button."""
        section = self.page.locator(self._ALPINE_PRESENTATION_SECTION)
        section.locator("a.btn").click()
    
    # =========================================================================
    # Generic Project Methods
    # =========================================================================
    
    def click_project_by_title(self, title: str) -> None:
        """
        Click on a project by its title.
        
        Args:
            title: The project title
        """
        section = self.page.locator(f".project-text:has(h4:has-text('{title}'))")
        section.locator("a.btn").click()
    
    def get_project_description(self, title: str) -> str:
        """
        Get a project's description by title.
        
        Args:
            title: The project title
            
        Returns:
            Project description text
        """
        section = self.page.locator(f".project-text:has(h4:has-text('{title}'))")
        return section.locator("p").text_content() or ""
