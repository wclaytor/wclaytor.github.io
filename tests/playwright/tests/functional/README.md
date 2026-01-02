# Functional Tests - Homepage (P1 - High)

> _"The tests are the executable specification."_ — Martin Fowler

## Overview

Functional tests for the homepage verify that all features work correctly. These tests cover the four main sections of the homepage: Masthead, About, Projects, and Contact.

**Purpose**: Verify homepage features work correctly  
**Execution**: Before merge to main  
**Duration Target**: < 3 minutes  
**Pass Criteria**: 100% pass required

## Test Files

| File                                                   | Section                | Status         |
| ------------------------------------------------------ | ---------------------- | -------------- |
| [test_homepage_masthead.py](test_homepage_masthead.py) | 3.2.1 Masthead Section | ✅ Implemented |
| [test_homepage_about.py](test_homepage_about.py)       | 3.2.2 About Section    | ✅ Implemented |
| [test_homepage_projects.py](test_homepage_projects.py) | 3.2.3 Projects Section | ✅ Implemented |
| `test_homepage_contact.py`                             | 3.2.4 Contact Section  | ❌ Not Created |

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

| ID       | Test Case               | Expected Result                        | Status             | Test Location |
| -------- | ----------------------- | -------------------------------------- | ------------------ | ------------- |
| HP-C-001 | Email displayed         | Email address visible                  | ❌ Not Implemented | -             |
| HP-C-002 | Email link works        | Click opens mailto: link               | ❌ Not Implemented | -             |
| HP-C-003 | LinkedIn link           | Click opens LinkedIn profile (new tab) | ❌ Not Implemented | -             |
| HP-C-004 | GitHub link             | Click opens GitHub profile (new tab)   | ❌ Not Implemented | -             |
| HP-C-005 | Social links accessible | Tab through links works                | ❌ Not Implemented | -             |

### Coverage Summary

| Section         | Total  | Implemented | Not Implemented | Coverage |
| --------------- | ------ | ----------- | --------------- | -------- |
| Masthead (HP-M) | 5      | 5           | 0               | 100%     |
| About (HP-A)    | 8      | 8           | 0               | 100%     |
| Projects (HP-P) | 8      | 8           | 0               | 100%     |
| Contact (HP-C)  | 5      | 0           | 5               | 0%       |
| **Total**       | **26** | **21**      | **5**           | **81%**  |

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
3. Create `test_homepage_contact.py` - Contact section tests (HP-C-001 to HP-C-005)

### Implementation Approach

- Follow existing pattern from `test_homepage_masthead.py`
- Extend `HomePage` page object with new locators and methods
- Add test data constants to `fixtures/test_data.py`

## GitHub Issue Tracking

Homepage functional tests will be tracked in GitHub under:

- **Epic**: Epic: Functional Tests - Homepage (P1 - High)
- **Labels**: `epic`, `testing`, `functional-tests`, `homepage`, `P1-high`

## References

- [TEST_PLAN.md](../../TEST_PLAN.md) - Section 3.2 Functional Tests - Homepage
- [TESTING_STRATEGY.md](../../TESTING_STRATEGY.md) - Testing philosophy
- [TEST_ARCHITECTURE.md](../../TEST_ARCHITECTURE.md) - Technical architecture
- [pages/home_page.py](../../pages/home_page.py) - HomePage page object
