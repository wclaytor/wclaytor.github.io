"""
base_page.py - Abstract base class for all page objects.

This module provides common functionality shared by all page objects,
following the DRY principle and enabling consistent test patterns.

Design Philosophy (Kent Beck & Martin Fowler):
- Simple: Only expose what tests actually need
- Clear: Method names describe user actions
- Composable: Pages can use shared components
"""

from abc import ABC, abstractmethod
from typing import Self
from playwright.sync_api import Page, expect, Locator


class BasePage(ABC):
    """
    Abstract base class providing common functionality for all page objects.
    
    Responsibilities:
    - Navigation to the page
    - Common element interactions
    - Screenshot capture
    - Wait strategies
    
    Usage:
        class MyPage(BasePage):
            @property
            def path(self) -> str:
                return "/my-page/"
            
            def do_something(self):
                self.page.locator("#button").click()
    """
    
    def __init__(self, page: Page, base_url: str = "") -> None:
        """
        Initialize the page object.
        
        Args:
            page: Playwright page object
            base_url: Base URL for the site (e.g., "http://localhost:8000")
        """
        self.page = page
        self.base_url = base_url.rstrip("/")
    
    @property
    @abstractmethod
    def path(self) -> str:
        """
        The URL path for this page (e.g., '/projects/').
        
        Must be implemented by subclasses.
        """
        pass
    
    @property
    def url(self) -> str:
        """Full URL for this page (base_url + path)."""
        return f"{self.base_url}{self.path}"
    
    # =========================================================================
    # Navigation
    # =========================================================================
    
    def goto(self) -> Self:
        """
        Navigate to this page.
        
        Returns:
            Self for method chaining
        """
        self.page.goto(self.url)
        self.wait_for_load()
        return self
    
    def wait_for_load(self) -> None:
        """Wait for the page to be fully loaded."""
        self.page.wait_for_load_state("networkidle")
    
    def reload(self) -> Self:
        """Reload the current page."""
        self.page.reload()
        self.wait_for_load()
        return self
    
    # =========================================================================
    # Page Information
    # =========================================================================
    
    def get_title(self) -> str:
        """Get the page title."""
        return self.page.title()
    
    def get_url(self) -> str:
        """Get the current URL."""
        return self.page.url
    
    def is_loaded(self) -> bool:
        """
        Check if this page is currently loaded.
        
        Default implementation checks URL. Override for more specific checks.
        """
        return self.path in self.page.url
    
    # =========================================================================
    # Screenshots
    # =========================================================================
    
    def take_screenshot(self, full_page: bool = True) -> bytes:
        """
        Capture a screenshot of the current page.
        
        Args:
            full_page: If True, capture entire scrollable page
            
        Returns:
            Screenshot as bytes
        """
        return self.page.screenshot(full_page=full_page)
    
    def save_screenshot(self, path: str, full_page: bool = True) -> None:
        """
        Save a screenshot to a file.
        
        Args:
            path: File path to save screenshot
            full_page: If True, capture entire scrollable page
        """
        self.page.screenshot(path=path, full_page=full_page)
    
    # =========================================================================
    # Common Elements
    # =========================================================================
    
    @property
    def navigation(self):
        """
        Get the navigation component.
        
        Returns:
            Navigation component object
        """
        from pages.components.navigation import Navigation
        return Navigation(self.page)
    
    @property
    def footer(self):
        """
        Get the footer component.
        
        Returns:
            Footer component object
        """
        from pages.components.footer import Footer
        return Footer(self.page)
    
    # =========================================================================
    # Utility Methods
    # =========================================================================
    
    def scroll_to_element(self, selector: str) -> None:
        """
        Scroll an element into view.
        
        Args:
            selector: CSS selector for the element
        """
        self.page.locator(selector).scroll_into_view_if_needed()
    
    def click(self, selector: str) -> None:
        """
        Click an element.
        
        Args:
            selector: CSS selector for the element
        """
        self.page.locator(selector).click()
    
    def get_text(self, selector: str) -> str:
        """
        Get text content of an element.
        
        Args:
            selector: CSS selector for the element
            
        Returns:
            Text content of the element
        """
        return self.page.locator(selector).text_content() or ""
    
    def is_visible(self, selector: str) -> bool:
        """
        Check if an element is visible.
        
        Args:
            selector: CSS selector for the element
            
        Returns:
            True if element is visible
        """
        return self.page.locator(selector).is_visible()
    
    def wait_for_selector(self, selector: str, timeout: float = 5000) -> Locator:
        """
        Wait for an element to appear.
        
        Args:
            selector: CSS selector for the element
            timeout: Maximum time to wait in milliseconds
            
        Returns:
            Locator for the element
        """
        locator = self.page.locator(selector)
        locator.wait_for(timeout=timeout)
        return locator
    
    def has_console_errors(self) -> list[str]:
        """
        Check for JavaScript console errors.
        
        Note: This only captures errors that occur after calling this method.
        For comprehensive error checking, use the console_errors fixture.
        
        Returns:
            List of error messages (empty if no errors)
        """
        errors: list[str] = []
        
        def handle_error(msg):
            if msg.type == "error":
                errors.append(msg.text)
        
        self.page.on("console", handle_error)
        return errors
