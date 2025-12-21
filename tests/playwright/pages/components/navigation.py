"""
navigation.py - Component object for the site navigation.

This component represents the main navigation bar that appears
on every page of the site. It handles both desktop and mobile navigation.
"""

from playwright.sync_api import Page


class Navigation:
    """
    Component object for the site navigation bar.
    
    Handles:
    - Desktop navigation links
    - Mobile hamburger menu
    - Brand link
    - Scroll-based navigation (on homepage)
    
    Usage:
        def test_navigation(page):
            nav = Navigation(page)
            assert nav.is_visible()
            nav.click_nav_link("About")
    """
    
    def __init__(self, page: Page) -> None:
        """
        Initialize the navigation component.
        
        Args:
            page: Playwright page object
        """
        self.page = page
    
    # =========================================================================
    # Selectors (Private)
    # =========================================================================
    
    _NAV = "#mainNav"
    _BRAND = ".navbar-brand"
    _TOGGLE = ".navbar-toggler"
    _NAV_COLLAPSE = "#navbarResponsive"
    _NAV_LINKS = ".navbar-nav .nav-link"
    
    # =========================================================================
    # Visibility Methods
    # =========================================================================
    
    def is_visible(self) -> bool:
        """Check if the navigation bar is visible."""
        return self.page.locator(self._NAV).is_visible()
    
    def is_mobile_menu_visible(self) -> bool:
        """
        Check if the mobile menu toggle is visible.
        
        The toggle is only visible on smaller viewports.
        """
        return self.page.locator(self._TOGGLE).is_visible()
    
    def is_menu_expanded(self) -> bool:
        """
        Check if the mobile menu is expanded (open).
        
        Returns:
            True if the menu is currently open
        """
        collapse = self.page.locator(self._NAV_COLLAPSE)
        classes = collapse.get_attribute("class") or ""
        return "show" in classes
    
    # =========================================================================
    # Brand Methods
    # =========================================================================
    
    def get_brand_text(self) -> str:
        """Get the brand/logo text."""
        return self.page.locator(self._BRAND).text_content() or ""
    
    def click_brand(self) -> None:
        """Click the brand link (navigates to homepage)."""
        self.page.locator(self._BRAND).click()
    
    # =========================================================================
    # Navigation Link Methods
    # =========================================================================
    
    def get_nav_links(self) -> list[str]:
        """
        Get all navigation link texts.
        
        Returns:
            List of link texts (e.g., ["About", "Projects", "Contact", "Resume"])
        """
        links = self.page.locator(self._NAV_LINKS)
        return links.all_text_contents()
    
    def click_nav_link(self, link_text: str) -> None:
        """
        Click a navigation link by its text.
        
        Args:
            link_text: The link text to click (e.g., "About")
        """
        # If on mobile and menu is not expanded, open it first
        if self.is_mobile_menu_visible() and not self.is_menu_expanded():
            self.toggle_mobile_menu()
            self.wait_for_menu_animation()
        
        self.page.get_by_role("link", name=link_text).click()
    
    def is_nav_link_visible(self, link_text: str) -> bool:
        """
        Check if a specific nav link is visible.
        
        Args:
            link_text: The link text to check
            
        Returns:
            True if the link is visible
        """
        return self.page.get_by_role("link", name=link_text).is_visible()
    
    # =========================================================================
    # Mobile Menu Methods
    # =========================================================================
    
    def toggle_mobile_menu(self) -> None:
        """Toggle the mobile hamburger menu."""
        self.page.locator(self._TOGGLE).click()
    
    def open_mobile_menu(self) -> None:
        """Open the mobile menu (if closed)."""
        if self.is_mobile_menu_visible() and not self.is_menu_expanded():
            self.toggle_mobile_menu()
            self.wait_for_menu_animation()
    
    def close_mobile_menu(self) -> None:
        """Close the mobile menu (if open)."""
        if self.is_mobile_menu_visible() and self.is_menu_expanded():
            self.toggle_mobile_menu()
            self.wait_for_menu_animation()
    
    def wait_for_menu_animation(self) -> None:
        """
        Wait for the menu open/close animation to complete.
        
        Bootstrap's collapse animation takes ~300ms.
        """
        self.page.wait_for_timeout(350)
    
    # =========================================================================
    # Accessibility Methods
    # =========================================================================
    
    def get_toggle_aria_label(self) -> str:
        """Get the ARIA label of the mobile menu toggle."""
        return self.page.locator(self._TOGGLE).get_attribute("aria-label") or ""
    
    def get_toggle_aria_expanded(self) -> str:
        """Get the aria-expanded state of the toggle."""
        return self.page.locator(self._TOGGLE).get_attribute("aria-expanded") or "false"
    
    def is_keyboard_accessible(self) -> bool:
        """
        Check if all nav links are keyboard accessible.
        
        Returns:
            True if all links can receive focus
        """
        links = self.page.locator(self._NAV_LINKS)
        for i in range(links.count()):
            link = links.nth(i)
            # Check if link is focusable
            if not link.is_visible():
                continue
            link.focus()
            if not link.evaluate("el => document.activeElement === el"):
                return False
        return True
