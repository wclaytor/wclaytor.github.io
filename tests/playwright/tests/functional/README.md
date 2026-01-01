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
| `test_homepage_about.py`                               | 3.2.2 About Section    | ❌ Not Created |
| `test_homepage_projects.py`                            | 3.2.3 Projects Section | ❌ Not Created |
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

| ID       | Test Case                 | Expected Result                          | Status             | Test Location |
| -------- | ------------------------- | ---------------------------------------- | ------------------ | ------------- |
| HP-A-001 | Headshot is visible       | Profile image displayed                  | ❌ Not Implemented | -             |
| HP-A-002 | Headshot has alt text     | Meaningful alt text present              | ❌ Not Implemented | -             |
| HP-A-003 | Bio text is displayed     | Biography paragraphs visible             | ❌ Not Implemented | -             |
| HP-A-004 | Software Development card | Card with relevant skills displayed      | ❌ Not Implemented | -             |
| HP-A-005 | Quality Assurance card    | Card with relevant skills displayed      | ❌ Not Implemented | -             |
| HP-A-006 | Test Automation card      | Card with relevant skills displayed      | ❌ Not Implemented | -             |
| HP-A-007 | View Resume button        | Click navigates to resume page           | ❌ Not Implemented | -             |
| HP-A-008 | View Resume keyboard      | Tab to button, Enter navigates to resume | ❌ Not Implemented | -             |

### 3.2.3 Projects Section

| ID       | Test Case                   | Expected Result                           | Status             | Test Location |
| -------- | --------------------------- | ----------------------------------------- | ------------------ | ------------- |
| HP-P-001 | Section heading visible     | "Featured Projects" heading displayed     | ❌ Not Implemented | -             |
| HP-P-002 | Alpine Resume card          | Card with title, description, badges      | ❌ Not Implemented | -             |
| HP-P-003 | Alpine Resume link          | Click "View Project" navigates to project | ❌ Not Implemented | -             |
| HP-P-004 | Alpine Presentation card    | Card with title, description, badges      | ❌ Not Implemented | -             |
| HP-P-005 | Alpine Presentation link    | Click "View Project" navigates to project | ❌ Not Implemented | -             |
| HP-P-006 | Experiments section         | Experiments section visible               | ❌ Not Implemented | -             |
| HP-P-007 | Background Transformer card | Card with "Experiment" badge              | ❌ Not Implemented | -             |
| HP-P-008 | Dynamic Resume card         | Card with "Experiment" badge              | ❌ Not Implemented | -             |

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
| About (HP-A)    | 8      | 0           | 8               | 0%       |
| Projects (HP-P) | 8      | 0           | 8               | 0%       |
| Contact (HP-C)  | 5      | 0           | 5               | 0%       |
| **Total**       | **26** | **5**       | **21**          | **19%**  |

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

1. Create `test_homepage_about.py` - About section tests (HP-A-001 to HP-A-008)
2. Create `test_homepage_projects.py` - Projects section tests (HP-P-001 to HP-P-008)
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
