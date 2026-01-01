# xml2md

Convert JUnit XML test reports to beautiful Markdown reports.

## Installation

This utility follows the uv pattern with PEP 735 dependency groups:

```bash
cd tests/playwright/utilities/xml2md
uv sync
```

## Usage

### Basic Usage

Convert an XML report to Markdown (saves to same location):

```bash
uv run xml2md report.xml
# Creates report.md in the same directory
```

### Custom Output

Specify a custom output path:

```bash
# Output to a specific file
uv run xml2md report.xml -o custom-report.md

# Output to a directory (keeps original filename)
uv run xml2md report.xml -o results/
```

### From Project Root

Run from anywhere using the `--directory` flag:

```bash
uv run --directory ./tests/playwright/utilities/xml2md xml2md path/to/report.xml
```

## Output Format

The generated Markdown report includes:

### Summary Section

- Overall pass/fail status with emoji indicators
- Test counts table (passed, failed, errors, skipped)
- Total duration
- Pass rate percentage

### Detailed Results

- Tests grouped by test class
- Status emoji for each test (✅ ❌ 💥 ⏭️)
- Individual test durations
- Browser/platform info extracted from test names

### Failures & Errors

- Detailed failure messages
- Stack traces and error details
- Easy-to-read code blocks

## Example Output

```markdown
# Test Report

**Generated:** December 31, 2025 at 19:27:43 UTC  
**Source:** `report.xml`  
**Host:** `3d88d89257f0`

## Summary

🎉 **All tests passed!**

| Metric      | Count  |
| ----------- | ------ |
| ✅ Passed   | 5      |
| ❌ Failed   | 0      |
| 💥 Errors   | 0      |
| ⏭️ Skipped  | 0      |
| **Total**   | **5**  |
| ⏱️ Duration | 17.27s |

**Pass Rate:** 100.0%
```

## Development

Run tests:

```bash
uv run pytest
```

## Integration

This utility is designed to be called from test runner scripts to automatically generate Markdown reports after each test run. See `run-functional.sh` for an example.
