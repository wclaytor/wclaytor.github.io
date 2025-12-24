# Test Report Analysis Prompt

## Context

You are reviewing Playwright test results for the wclaytor.github.io portfolio website. The test suite includes smoke tests that verify critical functionality like page loading, navigation, content presence, and accessibility features.

## Your Task

Analyze the provided test report XML file and create a comprehensive `report-analysis.md` file in the same directory as the report.

## Analysis Requirements

For each test failure, provide:

### 1. Root Cause Analysis

- Identify whether the failure is a **bug in the application** or a **test implementation issue**
- Examine the actual code (HTML, CSS, JavaScript) to understand the site's behavior
- Compare expected vs actual behavior
- Determine if the test assertion is correct

### 2. Impact Assessment

Include:

- **Severity:** Critical, High, Medium, Low
- **Type:** Bug vs Test Issue
- **User Impact:** How does this affect real users?
- **SEO Impact:** Any search engine implications?

### 3. Recommendations

Provide:

- Specific code fixes with examples
- Multiple options when applicable (mark the recommended approach)
- Explanation of why each approach is valid
- Consider both quick fixes and optimal solutions

### 4. For Passing Tests

Summarize what functionality is verified and working correctly

## Report Structure

Create a markdown file with these sections:

```markdown
# Test Report Analysis

**Date:** [Current Date]
**Report:** [Report Directory Name]
**Branch:** [Current Branch]
**Pull Request:** [Link if applicable]

## Executive Summary

- Total pass/fail statistics
- Overall verdict (bugs vs test issues)
- Key findings

## Test Failures

For each failure:

- Test name and location
- Failure details (error message)
- Root cause analysis
- Impact assessment
- Recommendations with code examples

## Passed Tests Summary

- Categorized list of passing tests
- What functionality is verified

## Recommendations

### Immediate Actions

### Test Improvements

### Site Enhancements (Optional)

## Conclusion

- Overall assessment
- Next steps
- Status of site functionality

## Test Execution Details

- Platform, duration, environment
- Performance notes
```

## Analysis Guidelines

### When It's a Bug

Signs of application bugs:

- Broken links (404 errors)
- Console errors that shouldn't exist
- Missing required content
- Accessibility violations
- Performance issues
- Incorrect functionality

**Action:** Recommend fixing the application code first

### When It's a Test Issue

Signs of test problems:

- Overly strict assertions (e.g., exact URL match when both work)
- Wrong assertion method (e.g., exact match instead of substring)
- Ambiguous selectors (e.g., multiple elements match)
- Test assumptions don't match reality
- Test data outdated

**Action:** Recommend updating the test code

### Investigation Steps

1. **Read the test code** - understand what it's trying to verify
2. **Examine the application code** - see what actually exists
3. **Check test data/fixtures** - verify assumptions are current
4. **Consider user perspective** - would a real user encounter this issue?
5. **Think about intent** - what was the test supposed to catch?

## Code Examples

Provide concrete, copy-paste ready code examples:

```python
# ❌ Before (failing test)
expect(page).to_have_url(f"{base_url}/")

# ✅ After (fixed test)
# Accept both "/" and "/index.html" as valid homepage URLs
assert page.url in [f"{base_url}/", f"{base_url}/index.html"], \
    f"Expected homepage, got {page.url}"
```

## Output Location

Create the analysis file in the same directory as the report:

- Input: `/path/to/reports/YYYYMMDD-HHMMSS/report.xml`
- Output: `/path/to/reports/YYYYMMDD-HHMMSS/report-analysis.md`

## Tone and Style

- **Professional but accessible** - technical accuracy without jargon
- **Specific and actionable** - concrete fixes, not vague suggestions
- **Balanced** - acknowledge what works well, not just problems
- **Educational** - explain why, not just what
- **Practical** - focus on realistic solutions

## Key Principles

1. **Assume competence** - tests and code were written with good intent
2. **Context matters** - consider project goals and constraints
3. **Multiple perspectives** - suggest alternatives when appropriate
4. **Evidence-based** - cite specific code and line numbers
5. **User-focused** - prioritize real-world impact

## Quality Checklist

Before completing, verify:

- ✅ Analyzed all failures (not just summarized)
- ✅ Examined actual application code, not just test code
- ✅ Provided specific recommendations with code examples
- ✅ Assessed user impact for each issue
- ✅ Summarized passing tests
- ✅ Included overall verdict (bugs vs test issues)
- ✅ Specified next steps
- ✅ Created file in correct location

## Example Usage

```bash
# User provides report.xml file
# You analyze it using this prompt
# You create report-analysis.md with comprehensive findings
```

---

**Remember:** The goal is to help the team quickly understand test results, distinguish bugs from test issues, and know exactly what to fix next.
