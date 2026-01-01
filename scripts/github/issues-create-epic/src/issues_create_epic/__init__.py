"""GitHub Epic & Issues Creator - Create epics and child issues from markdown."""

from .create_epic import main, GitHubIssueCreator

__version__ = "0.1.0"
__all__ = ["main", "GitHubIssueCreator"]
