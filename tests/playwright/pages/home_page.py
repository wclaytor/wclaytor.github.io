"""
home_page.py - Page object for the main homepage.

This page object encapsulates all interactions with the homepage (index.html),
providing a clean API for tests to verify the site's main landing page.

Sections:
- Masthead (hero area with name and tagline)
- About (headshot, bio, expertise cards)
- Projects (featured projects and experiments)
- Contact (email, social links)
"""

from pages.base_page import BasePage
from playwright.sync_api import Page


class HomePage(BasePage):
    """
    Page object for the main homepage (index.html).
    
    Usage:
        def test_homepage(home_page):
            home_page.goto()
            assert home_page.is_masthead_visible()
            assert "William Claytor" in home_page.get_masthead_title()
    """
    
    @property
    def path(self) -> str:
        return "/"
    
    # =========================================================================
    # Selectors (Private)
    # =========================================================================
    
    # Masthead section
    _MASTHEAD = "header.masthead"
    _MASTHEAD_TITLE = "header.masthead h1"
    _MASTHEAD_TAGLINE = ".masthead-tagline"
    _MASTHEAD_SUBTITLE = ".masthead-subtitle"
    _SCROLL_INDICATOR = "#scrollIndicator"
    
    # About section
    _ABOUT_SECTION = "#about"
    _ABOUT_HERO = ".about-hero"
    _HEADSHOT = ".headshot-img"
    _ABOUT_LEAD = ".about-lead"
    _ABOUT_SUMMARY = ".about-summary"
    _EXPERTISE_SECTION = ".expertise-section"
    _EXPERTISE_CARDS = ".expertise-card"
    _EXPERTISE_HEADING = ".expertise-heading"
    _EXPERTISE_TAGS = ".expertise-tags .tag"
    _VIEW_RESUME_BTN = ".about-cta a"
    
    # Projects section
    _PROJECTS_SECTION = "#projects"
    _PROJECTS_HEADING = "#projects h2"
    _PROJECT_CARDS = "#projects .card"
    _PROJECT_CARD_TITLE = ".card-title"
    _PROJECT_CARD_TEXT = ".card-text"
    _PROJECT_BADGES = ".badge"
    _EXPERIMENTS_SECTION = ".experiments-section"
    _EXPERIMENT_CARDS = ".experiment-card"
    
    # Contact section
    _CONTACT_SECTION = "#contact"
    _EMAIL_CARD = "#contact .card"
    _EMAIL_LINK = "#contact a[href^='mailto:']"
    _SOCIAL_LINKS = ".social a"
    _LINKEDIN_LINK = "a[href*='linkedin.com']"
    _GITHUB_LINK = "a[href*='github.com']"
    
    # Footer
    _FOOTER = "footer.footer"
    
    # =========================================================================
    # Masthead Methods
    # =========================================================================
    
    def is_masthead_visible(self) -> bool:
        """Check if the hero masthead is visible."""
        return self.is_visible(self._MASTHEAD)
    
    def get_masthead_title(self) -> str:
        """Get the main title text (name)."""
        return self.get_text(self._MASTHEAD_TITLE)
    
    def get_tagline(self) -> str:
        """Get the tagline text."""
        return self.get_text(self._MASTHEAD_TAGLINE)
    
    def get_subtitle(self) -> str:
        """Get the subtitle text."""
        return self.get_text(self._MASTHEAD_SUBTITLE)
    
    def is_scroll_indicator_visible(self) -> bool:
        """Check if the scroll indicator is visible."""
        return self.is_visible(self._SCROLL_INDICATOR)
    
    def click_scroll_indicator(self) -> None:
        """Click the scroll-down indicator arrow."""
        self.click(self._SCROLL_INDICATOR)
        self.page.wait_for_timeout(500)  # Wait for smooth scroll
    
    # =========================================================================
    # About Section Methods
    # =========================================================================
    
    def scroll_to_about(self) -> None:
        """Scroll to the About section."""
        self.scroll_to_element(self._ABOUT_SECTION)
    
    def is_about_section_visible(self) -> bool:
        """Check if the About section is visible."""
        return self.is_visible(self._ABOUT_SECTION)
    
    def is_headshot_visible(self) -> bool:
        """Check if the profile headshot is visible."""
        return self.is_visible(self._HEADSHOT)
    
    def get_headshot_alt_text(self) -> str:
        """Get the alt text of the headshot image."""
        return self.page.locator(self._HEADSHOT).get_attribute("alt") or ""
    
    def get_about_lead_text(self) -> str:
        """Get the lead paragraph text."""
        return self.get_text(self._ABOUT_LEAD)
    
    def get_expertise_areas(self) -> list[str]:
        """
        Get list of expertise area headings.
        
        Returns:
            List of expertise area titles (e.g., ["Software Development", ...])
        """
        cards = self.page.locator(self._EXPERTISE_CARDS)
        headings = cards.locator(self._EXPERTISE_HEADING.replace(".", ""))
        return headings.all_text_contents()
    
    def get_expertise_card_count(self) -> int:
        """Get the number of expertise cards."""
        return self.page.locator(self._EXPERTISE_CARDS).count()
    
    def get_expertise_tags(self, card_index: int = 0) -> list[str]:
        """
        Get skill tags from an expertise card.
        
        Args:
            card_index: Index of the card (0-based)
            
        Returns:
            List of tag texts
        """
        card = self.page.locator(self._EXPERTISE_CARDS).nth(card_index)
        tags = card.locator(".tag")
        return tags.all_text_contents()
    
    def is_view_resume_button_visible(self) -> bool:
        """Check if the View Resume button is visible."""
        return self.is_visible(self._VIEW_RESUME_BTN)
    
    def click_view_resume(self) -> None:
        """Click the 'View Full Resume' button."""
        self.click(self._VIEW_RESUME_BTN)
    
    # =========================================================================
    # Projects Section Methods
    # =========================================================================
    
    def scroll_to_projects(self) -> None:
        """Scroll to the Projects section."""
        self.scroll_to_element(self._PROJECTS_SECTION)
    
    def is_projects_section_visible(self) -> bool:
        """Check if the Projects section is visible."""
        return self.is_visible(self._PROJECTS_SECTION)
    
    def get_projects_heading(self) -> str:
        """Get the Projects section heading."""
        return self.get_text(self._PROJECTS_HEADING)
    
    def get_featured_project_titles(self) -> list[str]:
        """
        Get titles of featured projects (non-experiment cards).
        
        Returns:
            List of project titles
        """
        # Get project cards that are NOT in experiments section
        cards = self.page.locator(f"{self._PROJECTS_SECTION} > .container > .row .card:not(.experiment-card)")
        titles = cards.locator(self._PROJECT_CARD_TITLE)
        return titles.all_text_contents()
    
    def get_experiment_project_titles(self) -> list[str]:
        """
        Get titles of experiment projects.
        
        Returns:
            List of experiment project titles
        """
        cards = self.page.locator(self._EXPERIMENT_CARDS)
        titles = cards.locator(".card-title")
        return titles.all_text_contents()
    
    def click_project_by_title(self, title: str) -> None:
        """
        Click on a project card by its title.
        
        Args:
            title: The project title to click
        """
        card_title = self.page.locator(f"{self._PROJECT_CARD_TITLE}:has-text('{title}')")
        card_title.click()
    
    def click_project_view_button(self, title: str) -> None:
        """
        Click the 'View Project' button for a specific project.
        
        Args:
            title: The project title
        """
        card = self.page.locator(f".card:has({self._PROJECT_CARD_TITLE}:has-text('{title}'))")
        card.locator("a:has-text('View Project'), a:has-text('Launch')").first.click()
    
    def is_experiments_section_visible(self) -> bool:
        """Check if the Experiments section is visible."""
        return self.is_visible(self._EXPERIMENTS_SECTION)
    
    # =========================================================================
    # Contact Section Methods
    # =========================================================================
    
    def scroll_to_contact(self) -> None:
        """Scroll to the Contact section."""
        self.scroll_to_element(self._CONTACT_SECTION)
    
    def is_contact_section_visible(self) -> bool:
        """Check if the Contact section is visible."""
        return self.is_visible(self._CONTACT_SECTION)
    
    def get_email_address(self) -> str:
        """
        Get the contact email address.
        
        Returns:
            Email address (without mailto: prefix)
        """
        href = self.page.locator(self._EMAIL_LINK).get_attribute("href")
        return href.replace("mailto:", "") if href else ""
    
    def click_email_link(self) -> None:
        """Click the email link."""
        self.click(self._EMAIL_LINK)
    
    def get_social_links(self) -> list[str]:
        """
        Get all social media profile URLs.
        
        Returns:
            List of social link URLs
        """
        links = self.page.locator(self._SOCIAL_LINKS)
        hrefs = []
        for i in range(links.count()):
            href = links.nth(i).get_attribute("href")
            if href:
                hrefs.append(href)
        return hrefs
    
    def has_linkedin_link(self) -> bool:
        """Check if LinkedIn link is present."""
        return self.page.locator(self._LINKEDIN_LINK).count() > 0
    
    def has_github_link(self) -> bool:
        """Check if GitHub link is present."""
        return self.page.locator(self._GITHUB_LINK).count() > 0
    
    def click_linkedin(self) -> None:
        """Click the LinkedIn link."""
        self.click(self._LINKEDIN_LINK)
    
    def click_github(self) -> None:
        """Click the GitHub link."""
        self.click(self._GITHUB_LINK)
    
    # =========================================================================
    # Footer Methods
    # =========================================================================
    
    def is_footer_visible(self) -> bool:
        """Check if the footer is visible."""
        return self.is_visible(self._FOOTER)
    
    def get_footer_text(self) -> str:
        """Get the footer copyright text."""
        return self.get_text(self._FOOTER)
