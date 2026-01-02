# Test Plan for wclaytor.github.io

> _"The act of writing tests first, before the code, changes the way we think about the code."_ — Kent Beck

## Document Information

| Field              | Value                                        |
| ------------------ | -------------------------------------------- |
| **Project**        | wclaytor.github.io Portfolio Website         |
| **Version**        | 1.0                                          |
| **Created**        | December 2024                                |
| **Status**         | Draft                                        |
| **Test Framework** | Playwright with Python                       |
| **Influenced By**  | Kent Beck (TDD), Martin Fowler (Refactoring) |

---

## 1. Introduction

### 1.1 Purpose

This test plan defines the testing approach for the wclaytor.github.io portfolio website. The site has been successfully deployed and validated through manual exploratory testing. This plan establishes automated testing to:

1. **Protect** the current working state
2. **Enable** confident future changes
3. **Document** expected behavior as executable specifications

### 1.2 Scope

#### In Scope

- Homepage (`index.html`)
- Projects gallery (`/projects/`)
- Featured projects (Alpine Resume, Alpine Markdown Presentation)
- Experimental projects (Background Transformer, Dynamic Resume)
- Resume page
- Navigation and footer components
- Responsive behavior (mobile, tablet, desktop)
- Accessibility compliance
- Visual appearance

#### Out of Scope

- Third-party dependencies (Bootstrap, Google Fonts)
- External links (LinkedIn, GitHub profiles)
- Performance testing against specific thresholds (future phase)
- Load testing
- Security testing

### 1.3 References

- TESTING_STRATEGY.md - Testing philosophy and approach
- TEST_ARCHITECTURE.md - Technical architecture and patterns
- Site repository: https://github.com/wclaytor/wclaytor.github.io

---

## 2. Test Items

### 2.1 Pages Under Test

| Page                   | URL                                          | Priority | Description                                 |
| ---------------------- | -------------------------------------------- | -------- | ------------------------------------------- |
| Homepage               | `/`                                          | Critical | Main landing page with all sections         |
| Projects               | `/projects/`                                 | High     | Redirect page to main page projects section |
| Alpine Resume          | `/projects/alpine-resume/`                   | High     | Featured PWA project                        |
| Alpine Presentation    | `/projects/alpine-markdown-presentation/`    | High     | Featured PWA project                        |
| Resume                 | `/assets/resume/william_claytor_resume.html` | High     | Resume page                                 |
| Background Transformer | `/projects/alpine-background-transformer/`   | Medium   | Experimental project                        |
| Dynamic Resume         | `/projects/dynamic-resume/`                  | Medium   | Experimental project                        |

### 2.2 Components Under Test

| Component       | Appears On         | Priority |
| --------------- | ------------------ | -------- |
| Navigation      | All pages          | Critical |
| Footer          | All pages          | High     |
| Project Cards   | Homepage, Projects | High     |
| Expertise Cards | Homepage           | Medium   |
| Social Links    | Contact section    | Medium   |

---

## 3. Test Categories

### 3.1 Smoke Tests (P0 - Critical)

**Purpose**: Verify the site is alive and navigable  
**Execution**: Every commit, every deployment  
**Duration Target**: < 1 minute

| ID     | Test Case              | Expected Result                               |
| ------ | ---------------------- | --------------------------------------------- |
| SM-001 | Homepage loads         | HTTP 200, page renders                        |
| SM-002 | Projects page loads    | HTTP 200, page renders                        |
| SM-003 | Resume page loads      | HTTP 200, page renders                        |
| SM-004 | Navigation is visible  | Nav bar displayed on all pages                |
| SM-005 | No console errors      | Zero JavaScript errors                        |
| SM-006 | Featured projects load | Alpine Resume, Alpine Presentation accessible |

### 3.2 Functional Tests - Homepage (P1 - High)

**Purpose**: Verify homepage features work correctly  
**Execution**: Before merge to main  
**Duration Target**: < 3 minutes

#### 3.2.1 Masthead Section

| ID       | Test Case                            | Steps                         | Expected Result                       |
| -------- | ------------------------------------ | ----------------------------- | ------------------------------------- |
| HP-M-001 | Name is displayed                    | Load homepage                 | "William Claytor" visible in masthead |
| HP-M-002 | Tagline is displayed                 | Load homepage                 | "25 Years" mentioned in tagline       |
| HP-M-003 | Subtitle is displayed                | Load homepage                 | "Senior Software Engineer" visible    |
| HP-M-004 | Scroll indicator works               | Click scroll indicator        | Page scrolls to About section         |
| HP-M-005 | Scroll indicator keyboard accessible | Tab to indicator, press Enter | Page scrolls to About section         |

#### 3.2.2 About Section

| ID       | Test Case                 | Steps                | Expected Result                     |
| -------- | ------------------------- | -------------------- | ----------------------------------- |
| HP-A-001 | Headshot is visible       | Scroll to About      | Profile image displayed             |
| HP-A-002 | Headshot has alt text     | Inspect image        | Meaningful alt text present         |
| HP-A-003 | Bio text is displayed     | Scroll to About      | Biography paragraphs visible        |
| HP-A-004 | Software Development card | Scroll to Expertise  | Card with relevant skills displayed |
| HP-A-005 | Quality Assurance card    | Scroll to Expertise  | Card with relevant skills displayed |
| HP-A-006 | Test Automation card      | Scroll to Expertise  | Card with relevant skills displayed |
| HP-A-007 | View Resume button        | Click button         | Navigates to resume page            |
| HP-A-008 | View Resume keyboard      | Tab to button, Enter | Navigates to resume page            |

#### 3.2.3 Projects Section

| ID       | Test Case                   | Steps                 | Expected Result                        |
| -------- | --------------------------- | --------------------- | -------------------------------------- |
| HP-P-001 | Section heading visible     | Scroll to Projects    | "Featured Projects" heading displayed  |
| HP-P-002 | Alpine Resume card          | View Projects section | Card with title, description, badges   |
| HP-P-003 | Alpine Resume link          | Click "View Project"  | Navigates to Alpine Resume             |
| HP-P-004 | Alpine Presentation card    | View Projects section | Card with title, description, badges   |
| HP-P-005 | Alpine Presentation link    | Click "View Project"  | Navigates to presentation project      |
| HP-P-006 | Experiments section         | Scroll past Featured  | Experiments section visible            |
| HP-P-007 | Background Transformer card | View Experiments      | Card displayed with "Experiment" badge |
| HP-P-008 | Dynamic Resume card         | View Experiments      | Card displayed with "Experiment" badge |

#### 3.2.4 Contact Section

| ID       | Test Case               | Steps               | Expected Result                  |
| -------- | ----------------------- | ------------------- | -------------------------------- |
| HP-C-001 | Email displayed         | Scroll to Contact   | Email address visible            |
| HP-C-002 | Email link works        | Click email         | Opens mailto: link               |
| HP-C-003 | LinkedIn link           | Click LinkedIn icon | Opens LinkedIn profile (new tab) |
| HP-C-004 | GitHub link             | Click GitHub icon   | Opens GitHub profile (new tab)   |
| HP-C-005 | Social links accessible | Tab through links   | All links keyboard accessible    |

### 3.3 Functional Tests - Navigation (P1 - High)

| ID      | Test Case               | Steps            | Expected Result              |
| ------- | ----------------------- | ---------------- | ---------------------------- |
| NAV-001 | Brand link visible      | Load any page    | "wclaytor.github.io" visible |
| NAV-002 | Brand link works        | Click brand      | Navigates to homepage        |
| NAV-003 | About link              | Click "About"    | Scrolls to About section     |
| NAV-004 | Projects link           | Click "Projects" | Scrolls to Projects section  |
| NAV-005 | Contact link            | Click "Contact"  | Scrolls to Contact section   |
| NAV-006 | Resume link             | Click "Resume"   | Opens resume page            |
| NAV-007 | Nav sticky on scroll    | Scroll down page | Navigation stays visible     |
| NAV-008 | Nav keyboard accessible | Tab through nav  | All links accessible         |

### 3.4 Functional Tests - Projects Page (P1 - High)

| ID      | Test Case              | Steps                  | Expected Result                     |
| ------- | ---------------------- | ---------------------- | ----------------------------------- |
| PRJ-001 | Page loads             | Navigate to /projects/ | Redirect page renders               |
| PRJ-002 | Meta redirect present  | Check HTML meta tag    | Contains refresh to /#projects      |
| PRJ-003 | Canonical link present | Check HTML link tag    | Points to /#projects                |
| PRJ-004 | Redirect message shown | View page briefly      | "Redirecting to Projects" displayed |
| PRJ-005 | Manual link works      | Click fallback link    | Navigates to /#projects             |
| PRJ-006 | Automatic redirect     | Wait on page           | Redirects to /#projects             |
| PRJ-007 | Spinner animation      | View page briefly      | Loading spinner visible             |

### 3.5 Responsive Tests (P1 - High)

**Viewports**: Mobile (375px), Tablet (768px), Desktop (1920px)

| ID      | Test Case             | Viewport | Expected Result              |
| ------- | --------------------- | -------- | ---------------------------- |
| RSP-001 | Mobile menu toggle    | Mobile   | Hamburger menu visible       |
| RSP-002 | Mobile menu opens     | Mobile   | Click toggle opens menu      |
| RSP-003 | Mobile nav links work | Mobile   | Can navigate via mobile menu |
| RSP-004 | Tablet layout         | Tablet   | Content properly arranged    |
| RSP-005 | Desktop layout        | Desktop  | Full navigation visible      |
| RSP-006 | Cards stack on mobile | Mobile   | Cards display vertically     |
| RSP-007 | Cards grid on desktop | Desktop  | Cards display in grid        |
| RSP-008 | Headshot scales       | All      | Image properly sized         |
| RSP-009 | Text readable         | All      | Font sizes appropriate       |
| RSP-010 | Touch targets         | Mobile   | Buttons >= 44x44px           |

### 3.6 Accessibility Tests (P1 - High)

| ID       | Test Case            | Tool/Method | Expected Result                           |
| -------- | -------------------- | ----------- | ----------------------------------------- |
| A11Y-001 | Skip to content link | Keyboard    | Skip link present and works               |
| A11Y-002 | Heading hierarchy    | axe-core    | Proper h1-h6 structure                    |
| A11Y-003 | Image alt text       | axe-core    | All images have alt text                  |
| A11Y-004 | Color contrast       | axe-core    | WCAG AA compliance                        |
| A11Y-005 | Focus indicators     | Keyboard    | Visible focus on all interactive elements |
| A11Y-006 | ARIA labels          | axe-core    | Proper labels on icons/buttons            |
| A11Y-007 | Form labels          | axe-core    | All inputs labeled                        |
| A11Y-008 | Link purpose         | Manual      | Link text is descriptive                  |
| A11Y-009 | Keyboard navigation  | Keyboard    | All content accessible via keyboard       |
| A11Y-010 | No keyboard traps    | Keyboard    | Can tab through entire page               |

### 3.7 Visual Regression Tests (P2 - Medium)

| ID      | Test Case              | Viewport | Description                 |
| ------- | ---------------------- | -------- | --------------------------- |
| VIS-001 | Homepage masthead      | Desktop  | Hero section appearance     |
| VIS-002 | Homepage about         | Desktop  | About section appearance    |
| VIS-003 | Homepage projects      | Desktop  | Projects section appearance |
| VIS-004 | Homepage contact       | Desktop  | Contact section appearance  |
| VIS-005 | Homepage full          | Desktop  | Full page screenshot        |
| VIS-006 | Homepage full          | Tablet   | Full page at tablet size    |
| VIS-007 | Homepage full          | Mobile   | Full page at mobile size    |
| VIS-008 | Projects page          | Desktop  | Projects gallery appearance |
| VIS-009 | Navigation desktop     | Desktop  | Nav bar appearance          |
| VIS-010 | Navigation mobile open | Mobile   | Mobile menu open state      |
| VIS-011 | Footer                 | Desktop  | Footer appearance           |
| VIS-012 | Expertise cards        | Desktop  | Card styling consistency    |
| VIS-013 | Project cards          | Desktop  | Featured project cards      |
| VIS-014 | Experiment cards       | Desktop  | Experiment badges and cards |

### 3.8 Cross-Browser Tests (P2 - Medium)

**Browsers**: Chromium, Firefox, WebKit (Safari)

| ID     | Test Case         | Browsers | Description             |
| ------ | ----------------- | -------- | ----------------------- |
| XB-001 | Homepage renders  | All      | Page displays correctly |
| XB-002 | Navigation works  | All      | Nav links function      |
| XB-003 | Animations smooth | All      | CSS transitions work    |
| XB-004 | Fonts load        | All      | Custom fonts render     |
| XB-005 | Layout consistent | All      | No layout shifts        |
| XB-006 | Mobile menu       | All      | Hamburger menu works    |
| XB-007 | Scroll behavior   | All      | Smooth scroll works     |
| XB-008 | Links work        | All      | All links functional    |

---

## 4. Test Environment

### 4.1 Local Development

```
URL: http://localhost:8000
Server: Python http.server or Live Server
Purpose: Development testing, visual debugging
```

### 4.2 Production

```
URL: https://wclaytor.github.io
Purpose: Final validation, cross-browser testing
```

### 4.3 Browser Matrix

| Browser         | Version | Platform              | Priority |
| --------------- | ------- | --------------------- | -------- |
| Chrome/Chromium | Latest  | Linux, macOS, Windows | P0       |
| Firefox         | Latest  | Linux, macOS, Windows | P1       |
| Safari/WebKit   | Latest  | macOS, iOS            | P1       |
| Edge            | Latest  | Windows               | P2       |

### 4.4 Device Matrix

| Device     | Viewport  | Priority |
| ---------- | --------- | -------- |
| iPhone SE  | 375x667   | P0       |
| iPad       | 768x1024  | P1       |
| Desktop HD | 1920x1080 | P0       |
| Desktop 4K | 3840x2160 | P2       |

---

## 5. Test Execution

### 5.1 Test Suites

#### Smoke Suite (CI - Every Push)

```bash
uv run pytest tests/smoke -v --tb=short
```

**Tests**: SM-001 through SM-006  
**Duration**: < 1 minute  
**Pass Criteria**: 100% pass

#### Regression Suite (CI - PR to main)

```bash
uv run pytest tests/functional tests/accessibility -v
```

**Tests**: All HP-_, NAV-_, PRJ-_, RSP-_, A11Y-\*  
**Duration**: < 5 minutes  
**Pass Criteria**: 100% pass

#### Visual Suite (CI - PR to main)

```bash
uv run pytest tests/visual -v
```

**Tests**: All VIS-\*  
**Duration**: < 3 minutes  
**Pass Criteria**: No unexpected visual changes

#### Cross-Browser Suite (Weekly / Pre-Release)

```bash
uv run pytest tests/smoke tests/functional --browser chromium --browser firefox --browser webkit
```

**Tests**: XB-001 through XB-008  
**Duration**: < 10 minutes  
**Pass Criteria**: 95% pass (allow minor browser differences)

### 5.2 Test Execution Schedule

| Trigger            | Suites Run                 | Blocking |
| ------------------ | -------------------------- | -------- |
| Push to any branch | Smoke                      | Yes      |
| PR to main         | Smoke, Regression, Visual  | Yes      |
| Merge to main      | Smoke, Regression, Visual  | Yes      |
| Weekly             | Cross-Browser, Full Visual | No       |
| Pre-Release        | All suites                 | Yes      |

---

## 6. Pass/Fail Criteria

### 6.1 Overall Quality Gates

| Gate          | Criteria                          |
| ------------- | --------------------------------- |
| Smoke         | 100% tests pass                   |
| Functional    | 100% tests pass                   |
| Accessibility | Zero critical/serious violations  |
| Visual        | All changes reviewed and approved |
| Cross-Browser | 95% tests pass                    |

### 6.2 Defect Severity

| Severity | Description          | Example                 |
| -------- | -------------------- | ----------------------- |
| Critical | Site unusable        | Page won't load         |
| High     | Major feature broken | Navigation doesn't work |
| Medium   | Feature degraded     | Visual glitch           |
| Low      | Minor issue          | Typo                    |

### 6.3 Release Criteria

Before any release to production:

- [ ] Smoke tests: 100% pass
- [ ] Functional tests: 100% pass
- [ ] Accessibility: No critical/serious violations
- [ ] Visual tests: All changes approved
- [ ] Cross-browser: All major browsers verified
- [ ] Manual review: Homepage verified in browser

---

## 7. Test Data

### 7.1 Constants

```python
# fixtures/test_data.py

# Expected text content
SITE_TITLE = "William Claytor - Senior Software Engineer"
NAME = "William Claytor"
TAGLINE_CONTAINS = "25 Years"
EXPERTISE_AREAS = [
    "Software Development",
    "Quality Assurance",
    "Test Automation"
]

# Expected projects
FEATURED_PROJECTS = [
    "Alpine Resume",
    "Alpine Markdown Presentation"
]
EXPERIMENT_PROJECTS = [
    "Background Transformer",
    "Dynamic Resume"
]

# Contact info
EMAIL = "wclaytor@fastmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/billclaytor/"
GITHUB_URL = "https://github.com/wclaytor"

# Navigation links
NAV_LINKS = ["About", "Projects", "Contact", "Resume"]
```

### 7.2 URLs

```python
# fixtures/urls.py

class URLs:
    HOME = "/"
    PROJECTS = "/projects/"  # Redirects to /#projects
    PROJECTS_SECTION = "/#projects"  # Projects section on main page
    RESUME = "/assets/resume/william_claytor_resume.html"

    # Featured projects
    ALPINE_RESUME = "/projects/alpine-resume/releases/20251214/index.html"
    ALPINE_PRESENTATION = "/projects/alpine-markdown-presentation/index.html"

    # Experiments
    BACKGROUND_TRANSFORMER = "/projects/alpine-background-transformer/index.html"
    DYNAMIC_RESUME = "/projects/dynamic-resume/releases/v2.3/william_claytor_resume.html"
```

---

## 8. Reporting

### 8.1 Test Reports

| Report         | Format | Audience      |
| -------------- | ------ | ------------- |
| Console Output | Text   | Developers    |
| JUnit XML      | XML    | CI/CD         |
| HTML Report    | HTML   | Stakeholders  |
| Screenshots    | PNG    | Visual review |
| Recordings     | WebM   | Debug         |

### 8.2 Metrics to Track

- Test pass rate (target: >99%)
- Test execution time
- Flaky test rate (target: <1%)
- Code coverage (informational only)
- Visual diff rate

---

## 9. Risk Assessment

| Risk                      | Probability | Impact | Mitigation                  |
| ------------------------- | ----------- | ------ | --------------------------- |
| Flaky tests               | Medium      | High   | Proper waits, retry logic   |
| Visual false positives    | Medium      | Medium | Appropriate diff thresholds |
| Cross-browser differences | Medium      | Low    | Document known differences  |
| Test maintenance burden   | Low         | Medium | Page Object Model           |
| CI timeout                | Low         | High   | Parallel execution          |

---

## 10. Appendix

### 10.1 Command Reference

```bash
# Run all tests
uv run pytest

# Run specific category
uv run pytest tests/smoke -v
uv run pytest tests/functional -v
uv run pytest tests/visual -v
uv run pytest tests/accessibility -v

# Run with visible browser
uv run pytest --headed

# Run specific browser
uv run pytest --browser firefox

# Update visual baselines
uv run pytest tests/visual --update-snapshots

# Generate HTML report
uv run pytest --html=report.html

# Run in parallel
uv run pytest -n auto
```

### 10.2 Useful Playwright Commands

```bash
# Install browsers
uv run playwright install

# Open inspector for debugging
uv run playwright codegen https://wclaytor.github.io

# Show trace viewer
uv run playwright show-trace recordings/traces/test_name.zip
```

---

## Approval

| Role        | Name | Date | Signature |
| ----------- | ---- | ---- | --------- |
| Test Lead   |      |      |           |
| Developer   |      |      |           |
| Stakeholder |      |      |           |

---

_"Test until fear transforms into boredom."_ — Kent Beck
