"""
test_responsive.py - Functional tests for responsive behavior.

Test Plan Section: 3.5 Responsive Tests (P1 - High)
Tests: RSP-001 through RSP-010

These tests verify the site works correctly across different viewport sizes,
with particular focus on mobile navigation which is a critical user path.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs
from fixtures.test_data import TestData


# Viewport sizes from test plan
MOBILE_VIEWPORT = {"width": 375, "height": 667}  # iPhone SE
TABLET_VIEWPORT = {"width": 768, "height": 1024}  # iPad
DESKTOP_VIEWPORT = {"width": 1920, "height": 1080}  # Desktop HD


@pytest.mark.functional
@pytest.mark.responsive
class TestMobileNavigation:
    """
    Tests for mobile navigation (hamburger menu).

    The mobile menu is a critical user path - if users can't navigate
    on mobile, the site is effectively broken for mobile visitors.
    """

    def test_mobile_menu_toggle_visible(self, page: Page, base_url: str):
        """
        RSP-001: Mobile menu toggle visible.

        At mobile viewport, the hamburger menu toggle should be visible
        and the full navigation links should be hidden.

        Viewport: Mobile (375x667)
        Expected: Hamburger menu visible
        """
        # Set mobile viewport
        page.set_viewport_size(MOBILE_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Hamburger toggle should be visible
        toggle = page.locator(".navbar-toggler")
        expect(toggle).to_be_visible()

        # Full nav links should be collapsed/hidden
        nav_collapse = page.locator("#navbarResponsive")
        expect(nav_collapse).not_to_be_visible()

    def test_mobile_menu_opens(self, page: Page, base_url: str):
        """
        RSP-002: Mobile menu opens.

        Clicking the hamburger toggle should expand the navigation menu.

        Viewport: Mobile (375x667)
        Expected: Click toggle opens menu
        """
        # Set mobile viewport
        page.set_viewport_size(MOBILE_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Click the hamburger toggle
        toggle = page.locator(".navbar-toggler")
        toggle.click()

        # Wait for animation and check menu is visible
        nav_collapse = page.locator("#navbarResponsive")
        expect(nav_collapse).to_be_visible()

        # Nav links should now be visible
        about_link = page.get_by_role("link", name="About")
        expect(about_link).to_be_visible()

    def test_mobile_nav_links_work(self, page: Page, base_url: str):
        """
        RSP-003: Mobile nav links work.

        Users should be able to navigate via the mobile menu.

        Viewport: Mobile (375x667)
        Expected: Can navigate via mobile menu
        """
        # Set mobile viewport
        page.set_viewport_size(MOBILE_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Open mobile menu
        toggle = page.locator(".navbar-toggler")
        toggle.click()

        # Wait for menu to open
        nav_collapse = page.locator("#navbarResponsive")
        expect(nav_collapse).to_be_visible()

        # Click About link
        about_link = page.get_by_role("link", name="About")
        about_link.click()

        # About section should be in viewport
        about_section = page.locator("#about")
        expect(about_section).to_be_in_viewport()

    def test_mobile_menu_can_be_closed(self, page: Page, base_url: str):
        """
        Mobile menu can be opened and closed with the toggle.

        This verifies the hamburger toggle works bidirectionally.
        """
        # Set mobile viewport
        page.set_viewport_size(MOBILE_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        nav_collapse = page.locator("#navbarResponsive")
        toggle = page.locator(".navbar-toggler")

        # Menu should start collapsed
        expect(nav_collapse).not_to_be_visible()

        # Open mobile menu
        toggle.click()

        # Wait for Bootstrap expand animation to fully complete
        # Bootstrap adds 'collapsing' during animation, then 'collapse show' when done
        page.wait_for_selector(
            "#navbarResponsive.collapse.show:not(.collapsing)", timeout=3000)
        expect(nav_collapse).to_be_visible()

        # Click toggle again to close
        toggle.click()

        # Wait for collapse animation to fully complete
        # Element will be hidden, so use state="attached" to wait for class change
        page.wait_for_selector(
            "#navbarResponsive:not(.collapsing)", state="attached", timeout=3000)
        expect(nav_collapse).not_to_be_visible()


@pytest.mark.functional
@pytest.mark.responsive
class TestDesktopNavigation:
    """
    Tests for desktop navigation layout.
    """

    def test_desktop_nav_fully_visible(self, page: Page, base_url: str):
        """
        RSP-005: Desktop layout - full navigation visible.

        At desktop viewport, all navigation links should be visible
        without needing a hamburger menu.

        Viewport: Desktop (1920x1080)
        Expected: Full navigation visible
        """
        # Set desktop viewport
        page.set_viewport_size(DESKTOP_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Hamburger toggle should NOT be visible on desktop
        toggle = page.locator(".navbar-toggler")
        expect(toggle).not_to_be_visible()

        # All nav links in the navbar should be visible
        for link_text in TestData.NAV_LINKS:
            # Target specifically nav links in the navbar
            link = page.locator(f"#mainNav .nav-link:has-text('{link_text}')")
            expect(link).to_be_visible()

    def test_desktop_cards_grid_layout(self, page: Page, base_url: str):
        """
        RSP-007: Cards display in grid on desktop.

        Project cards should display in a grid layout at desktop size.

        Viewport: Desktop (1920x1080)
        Expected: Cards display in grid
        """
        # Set desktop viewport
        page.set_viewport_size(DESKTOP_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to projects section
        page.locator("#projects").scroll_into_view_if_needed()

        # Get project cards
        cards = page.locator(".card").all()
        assert len(cards) >= 2, "Expected at least 2 project cards"

        # Check that cards are side by side (different x positions)
        if len(cards) >= 2:
            box1 = cards[0].bounding_box()
            box2 = cards[1].bounding_box()

            # On desktop, cards should be side by side (different x positions)
            # or at least not directly stacked
            assert box1 is not None and box2 is not None

            # Cards in a row should have similar Y positions
            y_diff = abs(box1["y"] - box2["y"])
            assert y_diff < 50, f"Cards should be in same row on desktop, but Y diff is {y_diff}"


@pytest.mark.functional
@pytest.mark.responsive
class TestMobileLayout:
    """
    Tests for mobile layout behavior.
    """

    def test_mobile_cards_stack_vertically(self, page: Page, base_url: str):
        """
        RSP-006: Cards stack on mobile.

        Project cards should stack vertically at mobile viewport size.

        Viewport: Mobile (375x667)
        Expected: Cards display vertically
        """
        # Set mobile viewport
        page.set_viewport_size(MOBILE_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to projects section
        page.locator("#projects").scroll_into_view_if_needed()

        # Get project cards
        cards = page.locator(".card").all()
        assert len(cards) >= 2, "Expected at least 2 project cards"

        # Check that cards are stacked (similar x positions, different y)
        if len(cards) >= 2:
            box1 = cards[0].bounding_box()
            box2 = cards[1].bounding_box()

            assert box1 is not None and box2 is not None

            # On mobile, cards should be stacked (similar X, different Y)
            # Cards should have similar left positions (stacked)
            x_diff = abs(box1["x"] - box2["x"])
            assert x_diff < 50, f"Cards should have similar X position on mobile, but diff is {x_diff}"

    def test_mobile_headshot_scales(self, page: Page, base_url: str):
        """
        RSP-008: Headshot scales properly on mobile.

        The profile headshot should scale appropriately and not overflow.

        Viewport: Mobile (375x667)
        Expected: Image properly sized within viewport
        """
        # Set mobile viewport
        page.set_viewport_size(MOBILE_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to about section
        page.locator("#about").scroll_into_view_if_needed()

        # Find the headshot image
        headshot = page.locator(
            "img.headshot, img[alt*='William'], img[alt*='headshot']").first
        expect(headshot).to_be_visible()

        # Check image doesn't overflow viewport
        box = headshot.bounding_box()
        assert box is not None
        assert box["width"] <= MOBILE_VIEWPORT["width"], \
            f"Headshot width ({box['width']}) exceeds mobile viewport ({MOBILE_VIEWPORT['width']})"

    def test_mobile_touch_targets_adequate(self, page: Page, base_url: str):
        """
        RSP-010: Touch targets are adequate size on mobile.

        Interactive elements should be at least 44x44px for touch accessibility.

        Viewport: Mobile (375x667)
        Expected: Buttons >= 44x44px
        """
        MIN_TOUCH_SIZE = 44

        # Set mobile viewport
        page.set_viewport_size(MOBILE_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Check hamburger toggle is adequately sized
        toggle = page.locator(".navbar-toggler")
        toggle_box = toggle.bounding_box()
        assert toggle_box is not None
        assert toggle_box["width"] >= MIN_TOUCH_SIZE, \
            f"Toggle width ({toggle_box['width']}) is less than {MIN_TOUCH_SIZE}px"
        assert toggle_box["height"] >= MIN_TOUCH_SIZE, \
            f"Toggle height ({toggle_box['height']}) is less than {MIN_TOUCH_SIZE}px"


@pytest.mark.functional
@pytest.mark.responsive
class TestTabletLayout:
    """
    Tests for tablet layout behavior.
    """

    def test_tablet_layout_renders(self, page: Page, base_url: str):
        """
        RSP-004: Tablet layout renders correctly.

        Content should be properly arranged at tablet viewport.

        Viewport: Tablet (768x1024)
        Expected: Content properly arranged
        """
        # Set tablet viewport
        page.set_viewport_size(TABLET_VIEWPORT)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Main content areas should be visible
        expect(page.locator("#about")).to_be_visible()
        expect(page.locator("#projects")).to_be_visible()
        expect(page.locator("#contact")).to_be_visible()

        # Navigation should work (may be hamburger or full depending on breakpoint)
        nav = page.locator("#mainNav")
        expect(nav).to_be_visible()


@pytest.mark.functional
@pytest.mark.responsive
class TestTextReadability:
    """
    Tests for text readability across viewports.
    """

    @pytest.mark.parametrize("viewport,name", [
        (MOBILE_VIEWPORT, "mobile"),
        (TABLET_VIEWPORT, "tablet"),
        (DESKTOP_VIEWPORT, "desktop"),
    ])
    def test_text_readable_at_viewport(self, page: Page, base_url: str, viewport: dict, name: str):
        """
        RSP-009: Text readable at all viewports.

        Font sizes should be appropriate for the viewport size.

        Expected: Font sizes appropriate (>= 14px for body text)
        """
        MIN_BODY_FONT_SIZE = 14

        # Set viewport
        page.set_viewport_size(viewport)

        # Navigate to homepage
        page.goto(f"{base_url}{URLs.HOME}")

        # Scroll to about section which has body text
        page.locator("#about").scroll_into_view_if_needed()

        # Get computed font size of body text
        bio_text = page.locator("#about p").first
        font_size = bio_text.evaluate(
            "el => parseFloat(window.getComputedStyle(el).fontSize)"
        )

        assert font_size >= MIN_BODY_FONT_SIZE, \
            f"Font size ({font_size}px) is less than {MIN_BODY_FONT_SIZE}px at {name} viewport"
