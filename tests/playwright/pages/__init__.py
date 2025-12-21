"""
Page Object Model package for wclaytor.github.io tests.

This package contains page objects that encapsulate page structure
and provide a clean API for tests to interact with the website.

Following Kent Beck's principle: "Once and only once" - 
selectors and interactions are defined in one place.
"""

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.projects_page import ProjectsPage
from pages.resume_page import ResumePage

__all__ = [
    "BasePage",
    "HomePage",
    "ProjectsPage",
    "ResumePage",
]
