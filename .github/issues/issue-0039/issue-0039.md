---
assignees: []
author: wclaytor
closed_at: null
comment_count: 1
created_at: '2025-12-31T23:00:03Z'
issue_number: 39
labels:
- testing
- smoke-tests
- navigation
milestone: null
state: OPEN
title: 'SM-004: Navigation is visible on all pages'
updated_at: '2025-12-31T23:00:04Z'
---

# Issue #39: SM-004: Navigation is visible on all pages

## Description

**Parent Epic:** #35
**Type:** task
**Priority:** P0
**Story Points:** 3
**Sprint:** 1
**Dependencies:** #36, #37, #38

---

### SM-004: Navigation is visible on all pages

**Description:**
Implement a smoke test that verifies the navigation bar is displayed and visible
on all main pages (homepage, projects, resume).

**Acceptance Criteria:**
- [ ] Test verifies navigation is visible on homepage
- [ ] Test verifies navigation is visible on projects page
- [ ] Test verifies navigation is visible on resume page (if applicable)
- [ ] Navigation contains expected links
- [ ] Test passes consistently (no flakiness)

**Technical Notes:**
- Check for nav element or navigation container
- Verify brand/logo link is present
- Use parameterized tests to check multiple pages efficiently

**Testing Requirements:**
- [ ] Test runs in < 15 seconds (across all pages)
- [ ] Test works across all browsers

---
*Part of #35*

## Comments

### @wclaytor - 2025-12-31T23:00:04Z

Linked to parent epic #35

---

## Notes

_Add your implementation notes, decisions, and documentation here._
