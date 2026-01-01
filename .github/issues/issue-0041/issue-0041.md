---
assignees: []
author: wclaytor
closed_at: null
comment_count: 1
created_at: '2025-12-31T23:00:11Z'
issue_number: 41
labels:
- testing
- smoke-tests
- featured-projects
milestone: null
state: OPEN
title: 'SM-006: Featured projects are accessible'
updated_at: '2025-12-31T23:00:12Z'
---

# Issue #41: SM-006: Featured projects are accessible

## Description

**Parent Epic:** #35
**Type:** task
**Priority:** P0
**Story Points:** 3
**Sprint:** 1
**Dependencies:** #36

---

### SM-006: Featured projects are accessible

**Description:**
Implement a smoke test that verifies the featured projects (Alpine Resume,
Alpine Markdown Presentation) are accessible and their pages load successfully.

**Acceptance Criteria:**
- [ ] Test verifies Alpine Resume project page loads
- [ ] Test verifies Alpine Markdown Presentation project page loads
- [ ] Both pages return successful responses
- [ ] Both pages render their main content
- [ ] Test passes consistently (no flakiness)

**Technical Notes:**
- Alpine Resume URL: `/projects/alpine-resume/` or similar
- Alpine Presentation URL: `/projects/alpine-markdown-presentation/`
- Verify basic content is present on each project page

**Testing Requirements:**
- [ ] Test runs in < 15 seconds
- [ ] Test works across all browsers
- [ ] Test handles potential redirects gracefully

---
*Part of #35*

## Comments

### @wclaytor - 2025-12-31T23:00:12Z

Linked to parent epic #35

---

## Notes

_Add your implementation notes, decisions, and documentation here._
