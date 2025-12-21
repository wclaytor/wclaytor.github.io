"""
resume_page.py - Page object for the resume page.

This page object encapsulates interactions with the resume page,
which displays the full professional resume.
"""

from pages.base_page import BasePage
from playwright.sync_api import Page


class ResumePage(BasePage):
    """
    Page object for the resume page.
    
    Usage:
        def test_resume_page(resume_page):
            resume_page.goto()
            assert resume_page.is_loaded()
            assert "William Claytor" in resume_page.get_name()
    """
    
    @property
    def path(self) -> str:
        return "/assets/resume/william_claytor_resume.html"
    
    # =========================================================================
    # Selectors (Private)
    # =========================================================================
    
    _RESUME_CONTAINER = "body"
    _NAME_HEADING = "h1"
    _CONTACT_INFO = ".contact-info, header"
    _SECTION_HEADINGS = "h2"
    _EXPERIENCE_SECTION = "section, .experience"
    _SKILLS_SECTION = ".skills"
    _EDUCATION_SECTION = ".education"
    
    # =========================================================================
    # Page State Methods
    # =========================================================================
    
    def is_loaded(self) -> bool:
        """
        Check if the resume page is loaded.
        
        Returns:
            True if resume content is present
        """
        return self.is_visible(self._NAME_HEADING)
    
    def has_content(self) -> bool:
        """
        Check if the resume has substantial content.
        
        Returns:
            True if page has expected resume content
        """
        text = self.page.locator(self._RESUME_CONTAINER).text_content() or ""
        # Check for key expected content
        return len(text) > 100 and "claytor" in text.lower()
    
    # =========================================================================
    # Resume Content Methods
    # =========================================================================
    
    def get_name(self) -> str:
        """Get the name from the resume heading."""
        return self.get_text(self._NAME_HEADING)
    
    def get_section_headings(self) -> list[str]:
        """
        Get all section headings from the resume.
        
        Returns:
            List of section heading texts
        """
        headings = self.page.locator(self._SECTION_HEADINGS)
        return headings.all_text_contents()
    
    def has_experience_section(self) -> bool:
        """Check if the resume has an experience section."""
        text = self.page.content().lower()
        return "experience" in text or "work history" in text
    
    def has_skills_section(self) -> bool:
        """Check if the resume has a skills section."""
        text = self.page.content().lower()
        return "skills" in text or "technologies" in text
    
    def has_education_section(self) -> bool:
        """Check if the resume has an education section."""
        text = self.page.content().lower()
        return "education" in text
    
    def get_full_text(self) -> str:
        """
        Get the full text content of the resume.
        
        Returns:
            All text content from the resume
        """
        return self.page.locator(self._RESUME_CONTAINER).text_content() or ""
