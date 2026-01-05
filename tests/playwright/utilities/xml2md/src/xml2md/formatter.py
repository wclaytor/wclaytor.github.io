"""Markdown report formatter for xml2md."""

from datetime import datetime
from pathlib import Path

from .models import TestSuite, TestCase


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.2f}s"
    else:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.1f}s"


def get_status_emoji(status: str) -> str:
    """Get emoji for test status."""
    return {
        "passed": "✅",
        "failed": "❌",
        "error": "💥",
        "skipped": "⏭️",
    }.get(status, "❓")


def generate_markdown(suites: list[TestSuite], xml_path: Path) -> str:
    """
    Generate a Markdown report from test suites.

    Args:
        suites: List of TestSuite objects
        xml_path: Original XML file path (for reference)

    Returns:
        Formatted Markdown string
    """
    lines = []

    # Header
    lines.append("# Test Report")
    lines.append("")

    # Metadata
    timestamp = suites[0].timestamp if suites else datetime.now().isoformat()
    try:
        # Parse and format timestamp
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        formatted_time = dt.strftime("%B %d, %Y at %H:%M:%S %Z")
    except (ValueError, AttributeError):
        formatted_time = timestamp

    lines.append(f"**Generated:** {formatted_time}  ")
    lines.append(f"**Source:** `{xml_path.name}`  ")
    if suites and suites[0].hostname:
        lines.append(f"**Host:** `{suites[0].hostname}`  ")
    lines.append("")

    # Overall Summary
    total_tests = sum(s.tests for s in suites)
    total_passed = sum(s.passed for s in suites)
    total_failed = sum(s.failures for s in suites)
    total_errors = sum(s.errors for s in suites)
    total_skipped = sum(s.skipped for s in suites)
    total_time = sum(s.time for s in suites)

    lines.append("## Summary")
    lines.append("")

    # Status badge
    if total_failed == 0 and total_errors == 0:
        lines.append("🎉 **All tests passed!**")
    else:
        lines.append(
            f"⚠️ **{total_failed + total_errors} test(s) need attention**"
        )
    lines.append("")

    # Summary table
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| ✅ Passed | {total_passed} |")
    lines.append(f"| ❌ Failed | {total_failed} |")
    lines.append(f"| 💥 Errors | {total_errors} |")
    lines.append(f"| ⏭️ Skipped | {total_skipped} |")
    lines.append(f"| **Total** | **{total_tests}** |")
    lines.append(f"| ⏱️ Duration | {format_duration(total_time)} |")
    lines.append("")

    # Pass rate
    if total_tests > 0:
        pass_rate = (total_passed / total_tests) * 100
        lines.append(f"**Pass Rate:** {pass_rate:.1f}%")
        lines.append("")

    # Detailed Results
    lines.append("## Detailed Results")
    lines.append("")

    for suite in suites:
        if len(suites) > 1:
            lines.append(f"### {suite.name}")
            lines.append("")

        # Group tests by class
        tests_by_class: dict[str, list[TestCase]] = {}
        for tc in suite.test_cases:
            # Extract the class name without module path for cleaner display
            class_parts = tc.classname.split(".")
            class_name = class_parts[-1] if class_parts else tc.classname

            if class_name not in tests_by_class:
                tests_by_class[class_name] = []
            tests_by_class[class_name].append(tc)

        for class_name, tests in tests_by_class.items():
            lines.append(f"### {class_name}")
            lines.append("")
            lines.append("| Status | Test | Duration |")
            lines.append("|:------:|------|----------|")

            for tc in tests:
                emoji = get_status_emoji(tc.status)
                # Clean up test name (remove browser suffix like [chromium])
                test_name = tc.name
                if "[" in test_name:
                    test_name = test_name.split("[")[0]
                    browser = tc.name.split("[")[1].rstrip("]")
                    test_name = f"{test_name} `[{browser}]`"

                lines.append(
                    f"| {emoji} | {test_name} | {format_duration(tc.time)} |"
                )

            lines.append("")

        # Failed tests details
        failed_tests = [
            tc for tc in suite.test_cases if tc.status in ("failed", "error")
        ]
        if failed_tests:
            lines.append("## Failures & Errors")
            lines.append("")

            for tc in failed_tests:
                emoji = get_status_emoji(tc.status)
                lines.append(f"### {emoji} {tc.name}")
                lines.append("")
                lines.append(f"**Class:** `{tc.classname}`  ")
                lines.append(f"**Status:** {tc.status.upper()}  ")
                lines.append("")

                if tc.message:
                    lines.append("**Message:**")
                    lines.append("```")
                    lines.append(tc.message)
                    lines.append("```")
                    lines.append("")

                if tc.details:
                    lines.append("**Details:**")
                    lines.append("```")
                    lines.append(tc.details.strip())
                    lines.append("```")
                    lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append("*Generated by xml2md*")

    return "\n".join(lines)
