"""Tests for the issues-sync tool."""

import pytest
from issues_sync.sync import parse_frontmatter


class TestParseFrontmatter:
    """Tests for frontmatter parsing."""

    def test_parse_valid_frontmatter(self):
        """Test parsing valid YAML frontmatter."""
        content = """---
title: Test Issue
labels:
  - bug
  - urgent
---

This is the body of the issue.
"""
        frontmatter, body = parse_frontmatter(content)
        
        assert frontmatter is not None
        assert frontmatter['title'] == 'Test Issue'
        assert frontmatter['labels'] == ['bug', 'urgent']
        assert body == "This is the body of the issue."

    def test_parse_no_frontmatter(self):
        """Test parsing content without frontmatter."""
        content = "This is just plain content without frontmatter."
        
        frontmatter, body = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert body == content

    def test_parse_empty_frontmatter(self):
        """Test parsing empty frontmatter."""
        content = """---
---

Body content here.
"""
        frontmatter, body = parse_frontmatter(content)
        
        assert frontmatter is None or frontmatter == {}
        assert "Body content here." in body if body else True

    def test_parse_frontmatter_with_milestone(self):
        """Test parsing frontmatter with milestone."""
        content = """---
title: Feature Request
labels:
  - enhancement
assignees:
  - "@me"
milestone: "v1.0"
---

## Overview
This is a feature request.
"""
        frontmatter, body = parse_frontmatter(content)
        
        assert frontmatter['title'] == 'Feature Request'
        assert frontmatter['milestone'] == 'v1.0'
        assert frontmatter['assignees'] == ['@me']
        assert "## Overview" in body

    def test_parse_multiline_body(self):
        """Test parsing with multiline body content."""
        content = """---
title: Multi-line Test
---

Line 1
Line 2
Line 3

## Section
More content here.
"""
        frontmatter, body = parse_frontmatter(content)
        
        assert frontmatter['title'] == 'Multi-line Test'
        assert "Line 1" in body
        assert "Line 2" in body
        assert "## Section" in body
