"""Tests for pull_requests_sync."""

import pytest
from pathlib import Path
from pull_requests_sync.sync import ensure_prs_directory


def test_ensure_prs_directory(tmp_path):
    """Test that ensure_prs_directory creates the correct structure."""
    prs_dir = ensure_prs_directory(tmp_path)
    
    expected = tmp_path / ".github" / "pull-requests"
    assert prs_dir == expected
    assert prs_dir.exists()
    assert prs_dir.is_dir()


def test_ensure_prs_directory_idempotent(tmp_path):
    """Test that ensure_prs_directory can be called multiple times."""
    prs_dir1 = ensure_prs_directory(tmp_path)
    prs_dir2 = ensure_prs_directory(tmp_path)
    
    assert prs_dir1 == prs_dir2
    assert prs_dir1.exists()
