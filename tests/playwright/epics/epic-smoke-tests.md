---
epic:
  title: "Epic: Smoke Tests (P0 - Critical)"
  labels: ["epic", "testing", "smoke-tests", "P0-critical"]
  milestone: ""
  description: |
    Implement smoke tests to verify the site is alive and navigable.

    ## Context
    Smoke tests are the first line of defense in our testing strategy. They provide 
    rapid feedback on whether the site's core functionality is working. These tests 
    run on every commit and deployment.

    ## Success Criteria
    - [ ] All 6 smoke tests implemented and passing
    - [ ] Test execution time < 1 minute
    - [ ] Tests integrated into CI pipeline
    - [ ] Zero false positives after 10 consecutive runs

    ## Scope

    **In Scope**:
    - Homepage load verification
    - Projects page load verification
    - Resume page load verification
    - Navigation visibility check
    - Console error detection
    - Featured projects accessibility

    **Out of Scope**:
    - Detailed functional testing (covered in other epics)
    - Visual regression testing
    - Performance benchmarks

    ## References
    - [TEST_PLAN.md](../TEST_PLAN.md) - Section 3.1 Smoke Tests
    - [TESTING_STRATEGY.md](../TESTING_STRATEGY.md)
---

# Smoke Tests - Development Tickets

## Phase 1: Core Smoke Tests

---

ticket:
id: SM-001
title: Homepage loads successfully
type: task
priority: P0
points: 2
sprint: 1
labels: ["testing", "smoke-tests", "homepage"]
assignee: ""
dependencies: []

---

### SM-001: Homepage loads successfully

**Description:**
Implement a smoke test that verifies the homepage loads successfully with HTTP 200
status and the page renders without critical errors.

**Acceptance Criteria:**

- [ ] Test navigates to homepage URL
- [ ] Test verifies HTTP 200 response (or page loaded successfully)
- [ ] Test confirms page title is present
- [ ] Test confirms main content container is visible
- [ ] Test passes consistently (no flakiness)

**Technical Notes:**

- Use Playwright's `page.goto()` with appropriate wait strategies
- Consider using `expect(page).to_have_title()` for title verification
- Verify the masthead section is visible as a basic render check

**Testing Requirements:**

- [ ] Test runs in < 10 seconds
- [ ] Test works across all browsers (Chromium, Firefox, WebKit)

---

ticket:
id: SM-002
title: Projects page loads successfully
type: task
priority: P0
points: 2
sprint: 1
labels: ["testing", "smoke-tests", "projects"]
assignee: ""
dependencies: []

---

### SM-002: Projects page loads successfully

**Description:**
Implement a smoke test that verifies the projects page (`/projects/`) loads
successfully and renders without critical errors.

**Acceptance Criteria:**

- [ ] Test navigates to `/projects/` URL
- [ ] Test verifies page loaded successfully
- [ ] Test confirms page title or heading is present
- [ ] Test confirms projects listing container is visible
- [ ] Test passes consistently (no flakiness)

**Technical Notes:**

- Use similar pattern to SM-001
- Verify the projects section heading is visible

**Testing Requirements:**

- [ ] Test runs in < 10 seconds
- [ ] Test works across all browsers

---

ticket:
id: SM-003
title: Resume page loads successfully
type: task
priority: P0
points: 2
sprint: 1
labels: ["testing", "smoke-tests", "resume"]
assignee: ""
dependencies: []

---

### SM-003: Resume page loads successfully

**Description:**
Implement a smoke test that verifies the resume page loads successfully and
renders without critical errors.

**Acceptance Criteria:**

- [ ] Test navigates to resume page URL
- [ ] Test verifies page loaded successfully
- [ ] Test confirms resume content is visible
- [ ] Test passes consistently (no flakiness)

**Technical Notes:**

- Resume URL: `/assets/resume/william_claytor_resume.html`
- Verify main resume container is visible

**Testing Requirements:**

- [ ] Test runs in < 10 seconds
- [ ] Test works across all browsers

---

ticket:
id: SM-004
title: Navigation is visible on all pages
type: task
priority: P0
points: 3
sprint: 1
labels: ["testing", "smoke-tests", "navigation"]
assignee: ""
dependencies: ["SM-001", "SM-002", "SM-003"]

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

ticket:
id: SM-005
title: No console errors on page load
type: task
priority: P0
points: 3
sprint: 1
labels: ["testing", "smoke-tests", "console-errors"]
assignee: ""
dependencies: ["SM-001"]

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

ticket:
id: SM-006
title: Featured projects are accessible
type: task
priority: P0
points: 3
sprint: 1
labels: ["testing", "smoke-tests", "featured-projects"]
assignee: ""
dependencies: ["SM-001"]

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
