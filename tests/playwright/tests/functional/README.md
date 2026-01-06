# Functional Tests (P1 - High)

> _"The tests are the executable specification."_ — Martin Fowler

## Overview

Functional tests verify that all features work correctly. These tests cover the homepage sections (Masthead, About, Projects, Contact), site-wide components (Navigation), and the Projects redirect page.

**Purpose**: Verify site features work correctly  
**Execution**: Before merge to main  
**Duration Target**: < 5 minutes  
**Pass Criteria**: 100% pass required

## Test Files

| File                                                   | Section                       | Status         |
| ------------------------------------------------------ | ----------------------------- | -------------- |
| [test_homepage_masthead.py](test_homepage_masthead.py) | 3.2.1 Masthead Section        | ✅ Implemented |
| [test_homepage_about.py](test_homepage_about.py)       | 3.2.2 About Section           | ✅ Implemented |
| [test_homepage_projects.py](test_homepage_projects.py) | 3.2.3 Projects Section        | ✅ Implemented |
| [test_homepage_contact.py](test_homepage_contact.py)   | 3.2.4 Contact Section         | ✅ Implemented |
| [test_navigation.py](test_navigation.py)               | 3.3 Navigation (P1 - High)    | ✅ Implemented |
| [test_projects_page.py](test_projects_page.py)         | 3.4 Projects Page (P1 - High) | ✅ Implemented |
| [test_homepage_contact.py](test_homepage_contact.py)   | 3.2.4 Contact Section         | ✅ Implemented |
| [test_navigation.py](test_navigation.py)               | 3.3 Navigation (P1 - High)    | ✅ Implemented |

## Test Coverage Status

### 3.2.1 Masthead Section

| ID       | Test Case                            | Expected Result                          | Status         | Test Location                                                                                |
| -------- | ------------------------------------ | ---------------------------------------- | -------------- | -------------------------------------------------------------------------------------------- |
| HP-M-001 | Name is displayed                    | "William Claytor" visible in masthead    | ✅ Implemented | `test_homepage_masthead.py::TestHomepageMasthead::test_name_is_displayed`                    |
| HP-M-002 | Tagline is displayed                 | "25 Years" mentioned in tagline          | ✅ Implemented | `test_homepage_masthead.py::TestHomepageMasthead::test_tagline_is_displayed`                 |
| HP-M-003 | Subtitle is displayed                | "Senior Software Engineer" visible       | ✅ Implemented | `test_homepage_masthead.py::TestHomepageMasthead::test_subtitle_is_displayed`                |
| HP-M-004 | Scroll indicator works               | Page scrolls to About section            | ✅ Implemented | `test_homepage_masthead.py::TestHomepageMasthead::test_scroll_indicator_works`               |
| HP-M-005 | Scroll indicator keyboard accessible | Tab to indicator, Enter scrolls to About | ✅ Implemented | `test_homepage_masthead.py::TestHomepageMasthead::test_scroll_indicator_keyboard_accessible` |

### 3.2.2 About Section

| ID       | Test Case                 | Expected Result                          | Status         | Test Location                                                                     |
| -------- | ------------------------- | ---------------------------------------- | -------------- | --------------------------------------------------------------------------------- |
| HP-A-001 | Headshot is visible       | Profile image displayed                  | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_headshot_is_visible`             |
| HP-A-002 | Headshot has alt text     | Meaningful alt text present              | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_headshot_has_alt_text`           |
| HP-A-003 | Bio text is displayed     | Biography paragraphs visible             | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_bio_text_is_displayed`           |
| HP-A-004 | Software Development card | Card with relevant skills displayed      | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_software_development_card`       |
| HP-A-005 | Quality Assurance card    | Card with relevant skills displayed      | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_quality_assurance_card`          |
| HP-A-006 | Test Automation card      | Card with relevant skills displayed      | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_test_automation_card`            |
| HP-A-007 | View Resume button        | Click navigates to resume page           | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_view_resume_button`              |
| HP-A-008 | View Resume keyboard      | Tab to button, Enter navigates to resume | ✅ Implemented | `test_homepage_about.py::TestHomepageAbout::test_view_resume_keyboard_accessible` |

### 3.2.3 Projects Section

| ID       | Test Case                   | Expected Result                           | Status         | Test Location                                                                       |
| -------- | --------------------------- | ----------------------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| HP-P-001 | Section heading visible     | "Featured Projects" heading displayed     | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_section_heading_visible`     |
| HP-P-002 | Alpine Resume card          | Card with title, description, badges      | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_alpine_resume_card`          |
| HP-P-003 | Alpine Resume link          | Click "View Project" navigates to project | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_alpine_resume_link`          |
| HP-P-004 | Alpine Presentation card    | Card with title, description, badges      | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_alpine_presentation_card`    |
| HP-P-005 | Alpine Presentation link    | Click "View Project" navigates to project | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_alpine_presentation_link`    |
| HP-P-006 | Experiments section         | Experiments section visible               | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_experiments_section_visible` |
| HP-P-007 | Background Transformer card | Card with "Experiment" badge              | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_background_transformer_card` |
| HP-P-008 | Dynamic Resume card         | Card with "Experiment" badge              | ✅ Implemented | `test_homepage_projects.py::TestHomepageProjects::test_dynamic_resume_card`         |

### 3.2.4 Contact Section

| ID       | Test Case               | Expected Result                        | Status         | Test Location                                                                 |
| -------- | ----------------------- | -------------------------------------- | -------------- | ----------------------------------------------------------------------------- |
| HP-C-001 | Email displayed         | Email address visible                  | ✅ Implemented | `test_homepage_contact.py::TestHomepageContact::test_email_displayed`         |
| HP-C-002 | Email link works        | Click opens mailto: link               | ✅ Implemented | `test_homepage_contact.py::TestHomepageContact::test_email_link_works`        |
| HP-C-003 | LinkedIn link           | Click opens LinkedIn profile (new tab) | ✅ Implemented | `test_homepage_contact.py::TestHomepageContact::test_linkedin_link`           |
| HP-C-004 | GitHub link             | Click opens GitHub profile (new tab)   | ✅ Implemented | `test_homepage_contact.py::TestHomepageContact::test_github_link`             |
| HP-C-005 | Social links accessible | Tab through links works                | ✅ Implemented | `test_homepage_contact.py::TestHomepageContact::test_social_links_accessible` |

### Coverage Summary

| Section             | Total  | Implemented | Not Implemented | Coverage |
| ------------------- | ------ | ----------- | --------------- | -------- |
| Masthead (HP-M)     | 5      | 5           | 0               | 100%     |
| About (HP-A)        | 8      | 8           | 0               | 100%     |
| Projects (HP-P)     | 8      | 8           | 0               | 100%     |
| Contact (HP-C)      | 5      | 5           | 0               | 100%     |
| Navigation (NAV)    | 8      | 8           | 0               | 100%     |
| Projects Page (PRJ) | 7      | 7           | 0               | 100%     |
| **Total**           | **41** | **41**      | **0**           | **100%** |

---

## 3.3 Navigation Section

### Test Coverage

| ID      | Test Case               | Expected Result                        | Status         | Test Location                                                      |
| ------- | ----------------------- | -------------------------------------- | -------------- | ------------------------------------------------------------------ |
| NAV-001 | Brand link visible      | "wclaytor.github.io" visible           | ✅ Implemented | `test_navigation.py::TestNavigation::test_brand_link_visible`      |
| NAV-002 | Brand link works        | Click brand navigates to homepage      | ✅ Implemented | `test_navigation.py::TestNavigation::test_brand_link_works`        |
| NAV-003 | About link              | Click scrolls to About section         | ✅ Implemented | `test_navigation.py::TestNavigation::test_about_link`              |
| NAV-004 | Projects link           | Click scrolls to Projects section      | ✅ Implemented | `test_navigation.py::TestNavigation::test_projects_link`           |
| NAV-005 | Contact link            | Click scrolls to Contact section       | ✅ Implemented | `test_navigation.py::TestNavigation::test_contact_link`            |
| NAV-006 | Resume link             | Click opens resume page                | ✅ Implemented | `test_navigation.py::TestNavigation::test_resume_link`             |
| NAV-007 | Nav sticky on scroll    | Navigation stays visible when scrolled | ✅ Implemented | `test_navigation.py::TestNavigation::test_nav_sticky_on_scroll`    |
| NAV-008 | Nav keyboard accessible | All links accessible via keyboard      | ✅ Implemented | `test_navigation.py::TestNavigation::test_nav_keyboard_accessible` |

### test_navigation.py

Tests the navigation component that appears on all pages.

#### `TestNavigation`

| Test                           | Test Plan ID | Description                                    |
| ------------------------------ | ------------ | ---------------------------------------------- |
| `test_brand_link_visible`      | NAV-001      | Verifies brand link "wclaytor.github.io" shown |
| `test_brand_link_works`        | NAV-002      | Click brand scrolls to top of page             |
| `test_about_link`              | NAV-003      | Click About scrolls to About section           |
| `test_projects_link`           | NAV-004      | Click Projects scrolls to Projects section     |
| `test_contact_link`            | NAV-005      | Click Contact scrolls to Contact section       |
| `test_resume_link`             | NAV-006      | Click Resume navigates to resume page          |
| `test_nav_sticky_on_scroll`    | NAV-007      | Nav has fixed position when page scrolled      |
| `test_nav_keyboard_accessible` | NAV-008      | All nav links can receive keyboard focus       |

#### `TestNavigationAllPages`

| Test                              | Description                            |
| --------------------------------- | -------------------------------------- |
| `test_nav_visible_on_homepage`    | Verifies nav is visible on homepage    |
| `test_nav_visible_on_resume_page` | Verifies nav/page loads on resume page |
| `test_all_nav_links_present`      | Verifies all expected nav links exist  |

---

## 3.4 Projects Page Section

### Test Coverage

| ID      | Test Case              | Expected Result                     | Status         | Test Location                                                          |
| ------- | ---------------------- | ----------------------------------- | -------------- | ---------------------------------------------------------------------- |
| PRJ-001 | Page loads             | Redirect page renders               | ✅ Implemented | `test_projects_page.py::TestProjectsPage::test_page_loads`             |
| PRJ-002 | Meta redirect present  | Contains refresh to /#projects      | ✅ Implemented | `test_projects_page.py::TestProjectsPage::test_meta_redirect_present`  |
| PRJ-003 | Canonical link present | Points to /#projects                | ✅ Implemented | `test_projects_page.py::TestProjectsPage::test_canonical_link_present` |
| PRJ-004 | Redirect message shown | "Redirecting to Projects" displayed | ✅ Implemented | `test_projects_page.py::TestProjectsPage::test_redirect_message_shown` |
| PRJ-005 | Manual link works      | Navigates to /#projects             | ✅ Implemented | `test_projects_page.py::TestProjectsPage::test_manual_link_works`      |
| PRJ-006 | Automatic redirect     | Redirects to /#projects             | ✅ Implemented | `test_projects_page.py::TestProjectsPage::test_automatic_redirect`     |
| PRJ-007 | Spinner animation      | Loading spinner visible             | ✅ Implemented | `test_projects_page.py::TestProjectsPage::test_spinner_animation`      |

### test_projects_page.py

Tests the /projects/ redirect page that sends users to the homepage #projects section.

#### `TestProjectsPage`

| Test                          | Test Plan ID | Description                                    |
| ----------------------------- | ------------ | ---------------------------------------------- |
| `test_page_loads`             | PRJ-001      | Verifies page loads or redirects successfully  |
| `test_meta_redirect_present`  | PRJ-002      | Verifies meta refresh tag exists for redirect  |
| `test_canonical_link_present` | PRJ-003      | Verifies canonical link points to #projects    |
| `test_redirect_message_shown` | PRJ-004      | Verifies "Redirecting" message in HTML         |
| `test_manual_link_works`      | PRJ-005      | Verifies fallback link to #projects exists     |
| `test_automatic_redirect`     | PRJ-006      | Verifies page automatically redirects          |
| `test_spinner_animation`      | PRJ-007      | Verifies loading spinner exists with animation |

#### `TestProjectsPageStructure`

| Test                               | Description                                  |
| ---------------------------------- | -------------------------------------------- |
| `test_page_has_proper_title`       | Verifies page has descriptive title          |
| `test_fallback_link_is_accessible` | Verifies fallback link for JS-disabled users |

---

## Test Details

### test_homepage_masthead.py

Tests the hero/masthead section at the top of the homepage.

#### `TestHomepageMasthead`

| Test                                        | Test Plan ID | Description                                     |
| ------------------------------------------- | ------------ | ----------------------------------------------- |
| `test_name_is_displayed`                    | HP-M-001     | Verifies "William Claytor" appears in masthead  |
| `test_tagline_is_displayed`                 | HP-M-002     | Verifies "25 Years" appears in tagline          |
| `test_subtitle_is_displayed`                | HP-M-003     | Verifies "Senior Software Engineer" in subtitle |
| `test_scroll_indicator_works`               | HP-M-004     | Click scroll indicator scrolls to About section |
| `test_scroll_indicator_keyboard_accessible` | HP-M-005     | Tab + Enter on scroll indicator works           |

**Page Object**: Uses `HomePage` page object from `pages/home_page.py`

### test_homepage_about.py

Tests the About section of the homepage including headshot, bio, expertise cards, and resume button.

#### `TestHomepageAbout`

| Test                                   | Test Plan ID | Description                                  |
| -------------------------------------- | ------------ | -------------------------------------------- |
| `test_headshot_is_visible`             | HP-A-001     | Verifies profile headshot image is displayed |
| `test_headshot_has_alt_text`           | HP-A-002     | Verifies headshot has meaningful alt text    |
| `test_bio_text_is_displayed`           | HP-A-003     | Verifies biography paragraphs are visible    |
| `test_software_development_card`       | HP-A-004     | Verifies Software Development expertise card |
| `test_quality_assurance_card`          | HP-A-005     | Verifies Quality Assurance expertise card    |
| `test_test_automation_card`            | HP-A-006     | Verifies Test Automation expertise card      |
| `test_view_resume_button`              | HP-A-007     | Click View Resume navigates to resume page   |
| `test_view_resume_keyboard_accessible` | HP-A-008     | Tab + Enter on View Resume button works      |

**Page Object**: Uses `HomePage` page object from `pages/home_page.py`

### test_homepage_projects.py

Tests the Projects section of the homepage including featured projects and experiments.

#### `TestHomepageProjects`

| Test                               | Test Plan ID | Description                                           |
| ---------------------------------- | ------------ | ----------------------------------------------------- |
| `test_section_heading_visible`     | HP-P-001     | Verifies "Featured Projects" heading is displayed     |
| `test_alpine_resume_card`          | HP-P-002     | Verifies Alpine Resume card with badges               |
| `test_alpine_resume_link`          | HP-P-003     | Click View Project navigates to Alpine Resume         |
| `test_alpine_presentation_card`    | HP-P-004     | Verifies Alpine Presentation card with badges         |
| `test_alpine_presentation_link`    | HP-P-005     | Click View Project navigates to Alpine Presentation   |
| `test_experiments_section_visible` | HP-P-006     | Verifies Experiments section is visible               |
| `test_background_transformer_card` | HP-P-007     | Verifies Background Transformer with Experiment badge |
| `test_dynamic_resume_card`         | HP-P-008     | Verifies Dynamic Resume with Experiment badge         |

**Page Object**: Uses `HomePage` page object from `pages/home_page.py`

### test_homepage_contact.py

Tests the Contact section of the homepage including email and social media links.

#### `TestHomepageContact`

| Test                           | Test Plan ID | Description                                       |
| ------------------------------ | ------------ | ------------------------------------------------- |
| `test_email_displayed`         | HP-C-001     | Verifies email address is displayed               |
| `test_email_link_works`        | HP-C-002     | Verifies mailto: link is correctly formed         |
| `test_linkedin_link`           | HP-C-003     | Verifies LinkedIn link with accessibility         |
| `test_github_link`             | HP-C-004     | Verifies GitHub link with accessibility           |
| `test_social_links_accessible` | HP-C-005     | Verifies all social links are keyboard accessible |

**Page Object**: Uses `HomePage` page object from `pages/home_page.py`

## Running the Tests

### Run all homepage functional tests

```bash
cd tests/playwright
uv run pytest tests/functional -v --tb=short
```

### Run only masthead tests

```bash
uv run pytest tests/functional/test_homepage_masthead.py -v
```

### Run with timing info

```bash
uv run pytest tests/functional -v --durations=0
```

### Run specific test

```bash
uv run pytest tests/functional/test_homepage_masthead.py::TestHomepageMasthead::test_name_is_displayed -v
```

### Run against production

```bash
uv run pytest tests/functional -v --base-url https://wclaytor.github.io
```

## Implementation Notes

### Page Object Pattern

The homepage tests use the Page Object pattern with `HomePage` class:

```python
from pages.home_page import HomePage

def test_example(self, page: Page, base_url: str):
    home_page = HomePage(page, base_url)
    home_page.goto()
    assert home_page.is_masthead_visible()
```

### Test Data

Test data is centralized in `fixtures/test_data.py`:

```python
class TestData:
    MASTHEAD_TITLE = "William Claytor"
    TAGLINE_CONTAINS = "25 Years"
    SUBTITLE_CONTAINS = "Senior Software Engineer"
```

## Pending Work

### High Priority (P1)

1. ~~Create `test_homepage_about.py` - About section tests (HP-A-001 to HP-A-008)~~ ✅ Complete
2. ~~Create `test_homepage_projects.py` - Projects section tests (HP-P-001 to HP-P-008)~~ ✅ Complete
3. ~~Create `test_homepage_contact.py` - Contact section tests (HP-C-001 to HP-C-005)~~ ✅ Complete
4. ~~Create `test_navigation.py` - Navigation tests (NAV-001 to NAV-008)~~ ✅ Complete
5. ~~Create `test_projects_page.py` - Projects Page tests (PRJ-001 to PRJ-007)~~ ✅ Complete

**🎉 All Functional Tests Complete! (46/46 tests - 41/41 test plan items - 100% Coverage)**

### Next Sections (per TEST_PLAN.md)

6. Create Responsive tests (RSP-001 to RSP-010) - Section 3.5
7. Create Accessibility tests (A11Y-001 to A11Y-010) - Section 3.6
8. Create Visual Regression tests (VIS-001 to VIS-014) - Section 3.7
9. Create Cross-Browser tests (XB-001 to XB-008) - Section 3.8

### Implementation Approach

- Follow existing pattern from `test_homepage_masthead.py`
- Extend `HomePage` page object with new locators and methods
- Add test data constants to `fixtures/test_data.py`

## GitHub Issue Tracking

Homepage functional tests will be tracked in GitHub under:

- **Epic**: Epic: Functional Tests - Homepage (P1 - High)
- **Labels**: `epic`, `testing`, `functional-tests`, `homepage`, `P1-high`

## References

- [TEST_PLAN.md](../../TEST_PLAN.md) - Section 3.2-3.4 Functional Tests
- [TESTING_STRATEGY.md](../../TESTING_STRATEGY.md) - Testing philosophy
- [TEST_ARCHITECTURE.md](../../TEST_ARCHITECTURE.md) - Technical architecture
- [pages/home_page.py](../../pages/home_page.py) - HomePage page object
