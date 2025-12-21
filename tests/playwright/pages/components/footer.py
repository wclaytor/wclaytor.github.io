"""
footer.py - Component object for the site footer.

This component represents the footer that appears at the bottom
of every page.
"""

from playwright.sync_api import Page


class Footer:
    """
    Component object for the site footer.
    
    Usage:
        def test_footer(page):
            footer = Footer(page)
            assert footer.is_visible()
            assert "William Claytor" in footer.get_copyright_text()
    """
    
    def __init__(self, page: Page) -> None:
        """
        Initialize the footer component.
        
        Args:
            page: Playwright page object
        """
        self.page = page
    
    # =========================================================================
    # Selectors (Private)
    # =========================================================================
    
    _FOOTER = "footer.footer"
    _COPYRIGHT = "footer.footer"
    _YEAR_SPAN = "#current-year"
    
    # =========================================================================
    # Visibility Methods
    # =========================================================================
    
    def is_visible(self) -> bool:
        """Check if the footer is visible."""
        return self.page.locator(self._FOOTER).is_visible()
    
    def scroll_into_view(self) -> None:
        """Scroll the footer into view."""
        self.page.locator(self._FOOTER).scroll_into_view_if_needed()
    
    # =========================================================================
    # Content Methods
    # =========================================================================
    
    def get_copyright_text(self) -> str:
        """
        Get the copyright text from the footer.
        
        Returns:
            Full copyright text
        """
        return self.page.locator(self._COPYRIGHT).text_content() or ""
    
    def get_current_year(self) -> str:
        """
        Get the dynamically rendered current year.
        
        Returns:
            Year string (e.g., "2024")
        """
        return self.page.locator(self._YEAR_SPAN).text_content() or ""
    
    def contains_author_name(self) -> bool:
        """Check if the footer contains the author's name."""
        text = self.get_copyright_text().lower()
        return "william claytor" in text
    
    def contains_copyright_symbol(self) -> bool:
        """Check if the footer contains a copyright notice."""
        text = self.get_copyright_text()
        return "©" in text or "copyright" in text.lower()
