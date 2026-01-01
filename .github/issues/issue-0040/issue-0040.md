---
assignees: []
author: wclaytor
closed_at: null
comment_count: 1
created_at: '2025-12-31T23:00:07Z'
issue_number: 40
labels:
- testing
- smoke-tests
- console-errors
milestone: null
state: OPEN
title: 'SM-005: No console errors on page load'
updated_at: '2025-12-31T23:00:09Z'
---

# Issue #40: SM-005: No console errors on page load

## Description

**Parent Epic:** #35
**Type:** task
**Priority:** P0
**Story Points:** 3
**Sprint:** 1
**Dependencies:** #36

---

### SM-005: No console errors on page load

**Description:**
Implement a smoke test that captures browser console output and verifies there
are zero JavaScript errors on page load for critical pages.

**Acceptance Criteria:**
- [ ] Test captures console messages during page load
- [ ] Test filters for error-level messages
- [ ] Test fails if any JavaScript errors are detected
- [ ] Test passes for homepage, projects page
- [ ] Test passes consistently (no flakiness)

**Technical Notes:**
- Use Playwright's `page.on('console')` event listener
- Filter for `error` type messages
- Consider allowing warnings but failing on errors
- May need to ignore specific third-party errors if unavoidable

**Testing Requirements:**
- [ ] Test runs in < 15 seconds
- [ ] Test properly distinguishes errors from warnings
- [ ] Test report includes any captured errors for debugging

---
*Part of #35*

## Comments

### @wclaytor - 2025-12-31T23:00:08Z

Linked to parent epic #35

---

## Notes

_Add your implementation notes, decisions, and documentation here._
