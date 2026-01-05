"""JUnit XML parser for xml2md."""

import xml.etree.ElementTree as ET
from pathlib import Path

from .models import TestCase, TestSuite


def parse_junit_xml(xml_path: Path) -> list[TestSuite]:
    """
    Parse a JUnit XML report file.

    Args:
        xml_path: Path to the JUnit XML file

    Returns:
        List of TestSuite objects
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    suites = []

    # Handle both <testsuites> wrapper and direct <testsuite>
    if root.tag == "testsuites":
        suite_elements = root.findall("testsuite")
    else:
        suite_elements = [root]

    for suite_elem in suite_elements:
        test_cases = []

        for case_elem in suite_elem.findall("testcase"):
            # Determine test status
            status = "passed"
            message = None
            details = None

            failure = case_elem.find("failure")
            error = case_elem.find("error")
            skipped = case_elem.find("skipped")

            if failure is not None:
                status = "failed"
                message = failure.get("message", "")
                details = failure.text
            elif error is not None:
                status = "error"
                message = error.get("message", "")
                details = error.text
            elif skipped is not None:
                status = "skipped"
                message = skipped.get("message", "")

            test_case = TestCase(
                classname=case_elem.get("classname", ""),
                name=case_elem.get("name", ""),
                time=float(case_elem.get("time", 0)),
                status=status,
                message=message,
                details=details,
            )
            test_cases.append(test_case)

        suite = TestSuite(
            name=suite_elem.get("name", "pytest"),
            tests=int(suite_elem.get("tests", 0)),
            errors=int(suite_elem.get("errors", 0)),
            failures=int(suite_elem.get("failures", 0)),
            skipped=int(suite_elem.get("skipped", 0)),
            time=float(suite_elem.get("time", 0)),
            timestamp=suite_elem.get("timestamp", ""),
            hostname=suite_elem.get("hostname", ""),
            test_cases=test_cases,
        )
        suites.append(suite)

    return suites
