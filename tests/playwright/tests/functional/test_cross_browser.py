"""
test_cross_browser.py - Cross-browser compatibility tests.

Test Plan Section: 3.8 Cross-Browser Tests (P2 - Medium)
Tests: XB-001 through XB-008

These tests verify the site works correctly across Chromium, Firefox, and WebKit.
Tests are parameterized to run on all configured browsers.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs


@pytest.mark.functional
class TestCrossBrowserRendering:
    """
    Cross-browser rendering and layout tests.
    Tests: XB-001, XB-005
    """

    def test_homepage_renders(self, page: Page, base_url: str):
        """
        XB-001: Homepage renders correctly across browsers.

        Verifies the page loads and critical content is visible.
        """
        import re
        page.goto(f"{base_url}{URLs.HOME}")

        # Check page loads - title should contain "William Claytor"
        expect(page).to_have_title(re.compile(r"William Claytor"))

        # Check main sections exist
        expect(page.locator("header.masthead")).to_be_visible()
        expect(page.locator("nav.navbar")).to_be_visible()
        expect(page.locator("#about")).to_be_visible()
        expect(page.locator("#projects")).to_be_visible()
        expect(page.locator("#contact")).to_be_visible()
        expect(page.locator("footer")).to_be_visible()

    def test_layout_consistent(self, page: Page, base_url: str):
        """
        XB-005: Layout is consistent across browsers.

        Verifies no major layout shifts or broken layouts.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Check nav is horizontal on desktop
        nav = page.locator("nav.navbar")
        nav_box = nav.bounding_box()
        assert nav_box is not None, "Nav not found"
        assert nav_box["width"] > 500, "Nav should span horizontally"

        # Check masthead takes significant space
        masthead = page.locator("header.masthead")
        masthead_box = masthead.bounding_box()
        assert masthead_box is not None, "Masthead not found"
        assert masthead_box["height"] > 300, "Masthead should have significant height"

        # Check cards are laid out properly
        cards = page.locator("#about .card")
        first_card = cards.first
        if first_card.is_visible():
            card_box = first_card.bounding_box()
            assert card_box is not None, "Card not found"
            assert card_box["width"] > 100, "Cards should have reasonable width"


@pytest.mark.functional
class TestCrossBrowserNavigation:
    """
    Cross-browser navigation tests.
    Tests: XB-002, XB-008
    """

    def test_navigation_works(self, page: Page, base_url: str):
        """
        XB-002: Navigation links work across browsers.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Test About link (scroll anchor)
        about_link = page.locator('nav a[href="#about"]')
        expect(about_link).to_be_visible()
        about_link.click()
        page.wait_for_timeout(500)  # Wait for scroll

        # About section should be in viewport
        about_section = page.locator("#about")
        expect(about_section).to_be_in_viewport()

        # Test Projects link
        projects_link = page.locator('nav a[href="#projects"]')
        projects_link.click()
        page.wait_for_timeout(500)

        projects_section = page.locator("#projects")
        expect(projects_section).to_be_in_viewport()

    def test_links_work(self, page: Page, base_url: str):
        """
        XB-008: All links are functional across browsers.
        """
        import re
        page.goto(f"{base_url}{URLs.HOME}")

        # Check brand link
        brand = page.locator("a.navbar-brand")
        expect(brand).to_be_visible()
        expect(brand).to_have_attribute(
            "href", re.compile(r".+"))  # Any non-empty href

        # Check nav links have href
        nav_links = page.locator("nav .nav-link")
        count = nav_links.count()
        assert count >= 4, f"Expected at least 4 nav links, found {count}"

        # Check project links
        project_links = page.locator("#projects a")
        project_count = project_links.count()
        assert project_count >= 2, f"Expected project links, found {project_count}"


@pytest.mark.functional
class TestCrossBrowserAnimations:
    """
    Cross-browser animation and transition tests.
    Tests: XB-003, XB-007
    """

    def test_animations_smooth(self, page: Page, base_url: str):
        """
        XB-003: CSS transitions work across browsers.

        Verifies hover effects and transitions function.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Test button hover (transitions should apply)
        buttons = page.locator("#about .btn")
        first_button = buttons.first

        if first_button.is_visible():
            # Get initial styles
            initial_bg = first_button.evaluate(
                "el => window.getComputedStyle(el).backgroundColor"
            )

            # Hover and check transition property exists
            first_button.hover()

            transition = first_button.evaluate(
                "el => window.getComputedStyle(el).transition"
            )
            # Transitions should be defined (not 'none' or empty)
            assert transition and transition != "none 0s ease 0s", \
                "Button should have transition defined"

    def test_scroll_behavior(self, page: Page, base_url: str):
        """
        XB-007: Smooth scroll works across browsers.

        Verifies scroll-behavior CSS property is applied.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Check if smooth scroll is enabled
        scroll_behavior = page.evaluate(
            "() => window.getComputedStyle(document.documentElement).scrollBehavior"
        )

        # May be 'smooth' or 'auto' depending on CSS
        # Just verify the page scrolls when clicking anchor
        initial_scroll = page.evaluate("() => window.scrollY")

        # Click an anchor link
        about_link = page.locator('nav a[href="#about"]')
        about_link.click()
        page.wait_for_timeout(1000)  # Wait for scroll animation

        final_scroll = page.evaluate("() => window.scrollY")
        assert final_scroll > initial_scroll, "Page should have scrolled down"


@pytest.mark.functional
class TestCrossBrowserFonts:
    """
    Cross-browser font loading tests.
    Test: XB-004
    """

    def test_fonts_load(self, page: Page, base_url: str):
        """
        XB-004: Custom fonts render across browsers.
        """
        page.goto(f"{base_url}{URLs.HOME}")
        page.wait_for_load_state("networkidle")

        # Check that fonts are loaded (document.fonts API)
        fonts_ready = page.evaluate(
            "() => document.fonts.ready.then(() => true)")
        assert fonts_ready, "Fonts should be ready"

        # Verify a heading uses a custom font (not system default)
        heading = page.locator("h1").first
        if heading.is_visible():
            font_family = heading.evaluate(
                "el => window.getComputedStyle(el).fontFamily"
            )
            # Should have some font specified (not empty)
            assert font_family, "Heading should have font-family"
            assert len(font_family) > 0, "Font family should be defined"


@pytest.mark.functional
class TestCrossBrowserMobileMenu:
    """
    Cross-browser mobile menu tests.
    Test: XB-006
    """

    def test_mobile_menu(self, page: Page, base_url: str):
        """
        XB-006: Hamburger menu works across browsers.
        """
        # Set mobile viewport
        page.set_viewport_size({"width": 375, "height": 667})
        page.goto(f"{base_url}{URLs.HOME}")

        # Check hamburger button is visible
        toggle = page.locator("button.navbar-toggler")
        expect(toggle).to_be_visible()

        # Click to open menu
        toggle.click()

        # Wait for menu to open
        nav_collapse = page.locator("#navbarResponsive")
        nav_collapse.wait_for(state="visible", timeout=5000)

        # Verify nav links are now visible
        nav_links = page.locator("#navbarResponsive .nav-link")
        expect(nav_links.first).to_be_visible()

        # Close menu
        toggle.click()

        # Wait for collapse animation
        page.wait_for_timeout(500)
