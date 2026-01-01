# Smoke Tests (P0 - Critical)

> _"Run the fast tests first."_ — Kent Beck

## Overview

Smoke tests verify that the site is alive and navigable. They are the first line of defense in our testing strategy, providing rapid feedback on whether the site's core functionality is working.

**Purpose**: Verify the site is alive and navigable  
**Execution**: Every commit, every deployment  
**Duration Target**: < 1 minute  
**Pass Criteria**: 100% pass required

## Test Files

| File                                                       | Description                               |
| ---------------------------------------------------------- | ----------------------------------------- |
| [test_site_loads.py](test_site_loads.py)                   | Verifies critical pages load successfully |
| [test_critical_navigation.py](test_critical_navigation.py) | Verifies navigation functionality         |

## Test Coverage Status

### Test Plan Mapping

| ID     | Test Case              | Expected Result                               | Status         | Test Location                                                                                                                                                        |
| ------ | ---------------------- | --------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SM-001 | Homepage loads         | HTTP 200, page renders                        | ✅ Implemented | `test_site_loads.py::TestSiteLoads::test_homepage_loads`                                                                                                             |
| SM-002 | Projects page loads    | HTTP 200, page renders                        | ✅ Implemented | `test_site_loads.py::TestSiteLoads::test_projects_page_loads`                                                                                                        |
| SM-003 | Resume page loads      | HTTP 200, page renders                        | ✅ Implemented | `test_site_loads.py::TestSiteLoads::test_resume_page_loads`                                                                                                          |
| SM-004 | Navigation is visible  | Nav bar displayed on all pages                | ✅ Implemented | `test_site_loads.py::TestCriticalContent::test_homepage_has_navigation`, `test_critical_navigation.py::TestNavigationVisible`                                        |
| SM-005 | No console errors      | Zero JavaScript errors                        | ✅ Implemented | `test_site_loads.py::TestNoConsoleErrors`                                                                                                                            |
| SM-006 | Featured projects load | Alpine Resume, Alpine Presentation accessible | ✅ Implemented | `test_site_loads.py::TestSiteLoads::test_featured_project_alpine_resume_loads`, `test_site_loads.py::TestSiteLoads::test_featured_project_alpine_presentation_loads` |

### Coverage Summary

| Metric               | Value |
| -------------------- | ----- |
| **Total Test Cases** | 6     |
| **Implemented**      | 6     |
| **Not Implemented**  | 0     |
| **Coverage**         | 100%  |

## Test Details

### test_site_loads.py

Contains three test classes:

#### `TestSiteLoads`

Verifies critical pages load successfully.

| Test                                              | Test Plan ID | Description                                           |
| ------------------------------------------------- | ------------ | ----------------------------------------------------- |
| `test_homepage_loads`                             | SM-001       | Homepage returns HTTP 200 and contains expected title |
| `test_projects_page_loads`                        | SM-002       | Projects page returns HTTP 200                        |
| `test_resume_page_loads`                          | SM-003       | Resume page returns HTTP 200                          |
| `test_featured_project_alpine_resume_loads`       | SM-006a      | Alpine Resume project is accessible                   |
| `test_featured_project_alpine_presentation_loads` | SM-006b      | Alpine Markdown Presentation is accessible            |

#### `TestNoConsoleErrors`

Verifies pages load without JavaScript errors.

| Test                                   | Test Plan ID | Description                         |
| -------------------------------------- | ------------ | ----------------------------------- |
| `test_homepage_no_console_errors`      | SM-005       | Homepage has no console errors      |
| `test_projects_page_no_console_errors` | SM-005       | Projects page has no console errors |

#### `TestCriticalContent`

Verifies critical content is present.

| Test                                 | Test Plan ID | Description                       |
| ------------------------------------ | ------------ | --------------------------------- |
| `test_homepage_has_name`             | -            | Author's name appears on homepage |
| `test_homepage_has_navigation`       | SM-004       | Navigation is visible on homepage |
| `test_homepage_has_about_section`    | -            | About section exists              |
| `test_homepage_has_projects_section` | -            | Projects section exists           |
| `test_homepage_has_contact_section`  | -            | Contact section exists            |

### test_critical_navigation.py

Contains three test classes:

#### `TestNavigationVisible`

Verifies navigation is visible on all critical pages.

| Test                                             | Test Plan ID | Description                                      |
| ------------------------------------------------ | ------------ | ------------------------------------------------ |
| `test_navigation_visible_on_page` (parametrized) | SM-004       | Navigation visible on Homepage and Projects page |

#### `TestNavigationLinks`

Verifies navigation links work correctly.

| Test                                    | Test Plan ID | Description                               |
| --------------------------------------- | ------------ | ----------------------------------------- |
| `test_brand_link_goes_home`             | NAV-002      | Brand link navigates to homepage          |
| `test_about_link_scrolls_to_section`    | NAV-003      | About link scrolls to About section       |
| `test_projects_link_scrolls_to_section` | NAV-004      | Projects link scrolls to Projects section |
| `test_contact_link_scrolls_to_section`  | NAV-005      | Contact link scrolls to Contact section   |
| `test_resume_link_opens_resume`         | NAV-006      | Resume link opens resume page             |

#### `TestKeyboardNavigation`

Verifies basic keyboard navigation works.

| Test                        | Test Plan ID | Description                            |
| --------------------------- | ------------ | -------------------------------------- |
| `test_can_tab_to_nav_links` | NAV-008      | Navigation links reachable via Tab key |
| `test_skip_link_exists`     | A11Y-001     | Skip to content link exists            |

## Running the Tests

### Run all smoke tests

```bash
cd tests/playwright
uv run pytest tests/smoke -v --tb=short
```

### Run with timing info

```bash
uv run pytest tests/smoke -v --durations=0
```

### Run specific test file

```bash
uv run pytest tests/smoke/test_site_loads.py -v
uv run pytest tests/smoke/test_critical_navigation.py -v
```

### Run specific test class

```bash
uv run pytest tests/smoke/test_site_loads.py::TestSiteLoads -v
```

### Run against production

```bash
uv run pytest tests/smoke -v --base-url https://wclaytor.github.io
```

## GitHub Issue Tracking

Smoke tests are tracked in GitHub under:

- **Epic**: [Epic: Smoke Tests (P0 - Critical)](https://github.com/wclaytor/wclaytor.github.io/issues)
- **Labels**: `epic`, `testing`, `smoke-tests`, `P0-critical`

## References

- [TEST_PLAN.md](../../TEST_PLAN.md) - Section 3.1 Smoke Tests
- [TESTING_STRATEGY.md](../../TESTING_STRATEGY.md) - Testing philosophy
- [TEST_ARCHITECTURE.md](../../TEST_ARCHITECTURE.md) - Technical architecture
