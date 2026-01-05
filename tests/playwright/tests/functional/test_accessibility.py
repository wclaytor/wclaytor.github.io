"""
test_accessibility.py - Accessibility tests using axe-core.

Test Plan Section: 3.6 Accessibility Tests (P1 - High)
Tests: A11Y-001 through A11Y-010

These tests verify WCAG 2.1 AA compliance using the axe-core engine.
"""

import pytest
from playwright.sync_api import Page, expect

from fixtures.urls import URLs

# axe-core CDN URL
AXE_CORE_URL = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.8.4/axe.min.js"


def inject_axe(page: Page) -> None:
    """Inject axe-core into the page for accessibility testing."""
    # Check if axe is already loaded
    is_loaded = page.evaluate("() => typeof window.axe !== 'undefined'")
    if not is_loaded:
        # Inject axe-core from CDN
        page.add_script_tag(url=AXE_CORE_URL)
        # Wait for axe to be available
        page.wait_for_function(
            "() => typeof window.axe !== 'undefined'", timeout=10000)


def run_axe(page: Page, context: str = None, options: dict = None) -> dict:
    """
    Run axe-core analysis on the page.

    Args:
        page: Playwright page object
        context: Optional CSS selector to limit analysis scope
        options: Optional axe-core options

    Returns:
        dict with 'violations', 'passes', 'incomplete', 'inapplicable'
    """
    inject_axe(page)

    # Build the axe.run() call
    if context and options:
        script = f"() => axe.run('{context}', {options})"
    elif context:
        script = f"() => axe.run('{context}')"
    elif options:
        script = f"() => axe.run(document, {options})"
    else:
        script = "() => axe.run()"

    # Run axe and return results
    return page.evaluate(script)


def format_violations(violations: list) -> str:
    """Format axe violations for readable error messages."""
    if not violations:
        return "No violations found"

    messages = []
    for v in violations:
        impact = v.get('impact', 'unknown')
        description = v.get('description', 'No description')
        help_url = v.get('helpUrl', '')
        nodes = v.get('nodes', [])

        msg = f"\n[{impact.upper()}] {description}"
        if help_url:
            msg += f"\n  Help: {help_url}"

        for node in nodes[:3]:  # Limit to first 3 nodes
            target = node.get('target', ['unknown'])[0]
            failure = node.get('failureSummary', '')
            msg += f"\n  Element: {target}"
            if failure:
                msg += f"\n    {failure[:200]}"

        if len(nodes) > 3:
            msg += f"\n  ... and {len(nodes) - 3} more elements"

        messages.append(msg)

    return "\n".join(messages)


@pytest.mark.a11y
@pytest.mark.functional
class TestAccessibilityHomepage:
    """
    Accessibility tests for the homepage.

    Uses axe-core to detect WCAG 2.1 violations.
    """

    @pytest.mark.xfail(
        reason="Known issue: Color contrast violations (#64a19d text-primary needs darker color). See: #50",
        strict=False
    )
    def test_no_critical_violations(self, page: Page, base_url: str):
        """
        Homepage has no critical accessibility violations.

        Critical violations prevent users from accessing content entirely.

        KNOWN ISSUES:
        - text-primary (#64a19d) has contrast ratio 2.94 (needs 3:1 for large text)
        - text-black-50 (#808080) has contrast ratio 3.94 (needs 4.5:1)
        - btn-primary buttons have insufficient contrast
        """
        page.goto(f"{base_url}{URLs.HOME}")

        results = run_axe(page)
        violations = results.get('violations', [])

        # Filter for critical and serious violations only
        critical = [v for v in violations if v.get(
            'impact') in ['critical', 'serious']]

        assert len(critical) == 0, \
            f"Found {len(critical)} critical/serious accessibility violations:" + \
            format_violations(critical)

    @pytest.mark.xfail(
        reason="Known issue: Heading hierarchy skips levels (h1 → h3 → h4). See: #50",
        strict=False
    )
    def test_heading_hierarchy(self, page: Page, base_url: str):
        """
        A11Y-002: Heading hierarchy is correct.

        Pages should have a proper h1-h6 structure without skipping levels.

        KNOWN ISSUES:
        - expertise-title uses h3 after h1 (skips h2)
        - Card titles use h4/h5 without proper h2/h3 parents
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Run axe with specific rules for headings
        results = run_axe(
            page, options='{ runOnly: ["heading-order", "empty-heading", "page-has-heading-one"] }')
        violations = results.get('violations', [])

        assert len(violations) == 0, \
            f"Heading hierarchy issues found:" + format_violations(violations)

    def test_images_have_alt_text(self, page: Page, base_url: str):
        """
        A11Y-003: All images have alt text.

        Images must have meaningful alternative text for screen readers.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Run axe with image-related rules
        results = run_axe(
            page, options='{ runOnly: ["image-alt", "input-image-alt", "role-img-alt"] }')
        violations = results.get('violations', [])

        assert len(violations) == 0, \
            f"Images missing alt text:" + format_violations(violations)

    @pytest.mark.xfail(
        reason="Known issue: Color contrast violations (#64a19d text-primary needs darker color). See: #50",
        strict=False
    )
    def test_color_contrast(self, page: Page, base_url: str):
        """
        A11Y-004: Color contrast meets WCAG AA standards.

        Text must have sufficient contrast against its background.
        Ratio: 4.5:1 for normal text, 3:1 for large text.

        KNOWN ISSUES:
        - text-primary (#64a19d) ratio: 2.94 (needs 3:1)
        - text-black-50 (#808080) ratio: 3.94 (needs 4.5:1)
        - btn-primary white on #64a19d: 2.94 (needs 4.5:1)
        - Footer text-white-50 on black: 5.31 (needs 7:1 for AAA)
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Run axe with contrast rules
        results = run_axe(
            page, options='{ runOnly: ["color-contrast", "color-contrast-enhanced"] }')
        violations = results.get('violations', [])

        # Filter for actual contrast failures (not just warnings)
        contrast_failures = [v for v in violations if v.get('impact') in [
            'critical', 'serious']]

        assert len(contrast_failures) == 0, \
            f"Color contrast violations:" + \
            format_violations(contrast_failures)

    def test_aria_labels(self, page: Page, base_url: str):
        """
        A11Y-006: ARIA labels are proper.

        Interactive elements should have proper ARIA labels.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Run axe with ARIA-related rules
        results = run_axe(
            page, options='{ runOnly: ["aria-allowed-attr", "aria-hidden-focus", "aria-required-attr", "aria-roles", "aria-valid-attr-value", "aria-valid-attr"] }')
        violations = results.get('violations', [])

        assert len(violations) == 0, \
            f"ARIA label issues:" + format_violations(violations)

    def test_link_purpose(self, page: Page, base_url: str):
        """
        A11Y-008: Link text is descriptive.

        Links should have text that describes their purpose.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Run axe with link-related rules
        results = run_axe(
            page, options='{ runOnly: ["link-name", "link-in-text-block"] }')
        violations = results.get('violations', [])

        assert len(violations) == 0, \
            f"Link accessibility issues:" + format_violations(violations)


@pytest.mark.a11y
@pytest.mark.functional
class TestAccessibilityKeyboard:
    """
    Keyboard accessibility tests.
    """

    def test_focus_indicators_visible(self, page: Page, base_url: str):
        """
        A11Y-005: Focus indicators are visible.

        Interactive elements must show visible focus when tabbed to.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Tab to first interactive element
        page.keyboard.press("Tab")

        # Get the focused element
        focused = page.evaluate("""() => {
            const el = document.activeElement;
            if (!el || el === document.body) return null;
            
            const styles = window.getComputedStyle(el);
            const outlineWidth = parseInt(styles.outlineWidth) || 0;
            const outlineStyle = styles.outlineStyle;
            const boxShadow = styles.boxShadow;
            
            return {
                tag: el.tagName,
                hasOutline: outlineWidth > 0 && outlineStyle !== 'none',
                hasBoxShadow: boxShadow && boxShadow !== 'none',
                outlineStyle: outlineStyle,
                outlineWidth: outlineWidth
            };
        }""")

        assert focused is not None, "No element received focus on Tab"

        # Check that there's some visible focus indicator
        has_focus_indicator = focused.get(
            'hasOutline') or focused.get('hasBoxShadow')
        assert has_focus_indicator, \
            f"Element {focused.get('tag')} has no visible focus indicator"

    def test_no_keyboard_traps(self, page: Page, base_url: str):
        """
        A11Y-010: No keyboard traps.

        Users should be able to tab through the entire page without getting stuck.
        """
        page.goto(f"{base_url}{URLs.HOME}")

        # Track visited elements to detect loops
        visited_elements = []
        max_tabs = 100  # Safety limit

        for i in range(max_tabs):
            page.keyboard.press("Tab")

            # Get current focused element identifier
            current = page.evaluate("""() => {
                const el = document.activeElement;
                if (!el) return 'none';
                return el.tagName + ':' + (el.id || el.className || el.textContent?.slice(0, 20));
            }""")

            # If we've cycled back to an element we saw early, we've completed a cycle
            if current in visited_elements[:10]:
                # Successfully cycled through the page
                return

            visited_elements.append(current)

            # Check if we're stuck on the same element
            if len(visited_elements) >= 5:
                last_five = visited_elements[-5:]
                if len(set(last_five)) == 1:
                    pytest.fail(
                        f"Keyboard trap detected on element: {current}")

        # If we hit max_tabs, something might be wrong
        pytest.fail(f"Could not complete tab cycle after {max_tabs} tabs")


@pytest.mark.a11y
@pytest.mark.functional
class TestAccessibilityResume:
    """
    Accessibility tests for the resume page.
    """

    @pytest.mark.xfail(
        reason="Known issue: Resume may have inherited color contrast violations. See: #50",
        strict=False
    )
    def test_resume_no_critical_violations(self, page: Page, base_url: str):
        """
        Resume page has no critical accessibility violations.
        """
        page.goto(f"{base_url}{URLs.RESUME}")

        results = run_axe(page)
        violations = results.get('violations', [])

        # Filter for critical and serious violations only
        critical = [v for v in violations if v.get(
            'impact') in ['critical', 'serious']]

        assert len(critical) == 0, \
            f"Found {len(critical)} critical/serious violations on resume:" + \
            format_violations(critical)


@pytest.mark.a11y
@pytest.mark.functional
class TestAccessibilityProjects:
    """
    Accessibility tests for project pages.
    """

    @pytest.mark.xfail(
        reason="Known issue: Skip link color contrast violation. See: #50",
        strict=False
    )
    def test_alpine_resume_no_critical_violations(self, page: Page, base_url: str):
        """
        Alpine Resume project has no critical accessibility violations.
        """
        page.goto(f"{base_url}{URLs.ALPINE_RESUME}")

        results = run_axe(page)
        violations = results.get('violations', [])

        # Filter for critical and serious violations only
        critical = [v for v in violations if v.get(
            'impact') in ['critical', 'serious']]

        assert len(critical) == 0, \
            f"Found {len(critical)} critical/serious violations:" + \
            format_violations(critical)

    def test_alpine_presentation_no_critical_violations(self, page: Page, base_url: str):
        """
        Alpine Markdown Presentation has no critical accessibility violations.
        """
        page.goto(f"{base_url}{URLs.ALPINE_PRESENTATION}")

        results = run_axe(page)
        violations = results.get('violations', [])

        # Filter for critical and serious violations only
        critical = [v for v in violations if v.get(
            'impact') in ['critical', 'serious']]

        assert len(critical) == 0, \
            f"Found {len(critical)} critical/serious violations:" + \
            format_violations(critical)
