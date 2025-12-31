"""Tests for issues_create_epic."""

import pytest
from issues_create_epic import GitHubIssueCreator


def test_creator_initialization_dry_run():
    """Test that creator initializes correctly in dry run mode."""
    creator = GitHubIssueCreator(dry_run=True)
    assert creator.dry_run is True
    assert creator.created_issues == {}


def test_extract_issue_number_from_url():
    """Test extracting issue number from GitHub URL."""
    creator = GitHubIssueCreator(dry_run=True)
    
    # Valid URL
    url = "https://github.com/owner/repo/issues/42"
    assert creator._extract_issue_number_from_url(url) == 42
    
    # Invalid URL
    assert creator._extract_issue_number_from_url("not a url") is None
    assert creator._extract_issue_number_from_url("https://github.com/owner/repo") is None
