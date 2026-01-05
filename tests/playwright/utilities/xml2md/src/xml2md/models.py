"""Data models for xml2md test report parsing."""

from dataclasses import dataclass


@dataclass
class TestCase:
    """Represents a single test case result."""

    classname: str
    name: str
    time: float
    status: str  # "passed", "failed", "skipped", "error"
    message: str | None = None
    details: str | None = None


@dataclass
class TestSuite:
    """Represents a test suite with multiple test cases."""

    name: str
    tests: int
    errors: int
    failures: int
    skipped: int
    time: float
    timestamp: str
    hostname: str
    test_cases: list[TestCase]

    @property
    def passed(self) -> int:
        """Calculate number of passed tests."""
        return self.tests - self.errors - self.failures - self.skipped
