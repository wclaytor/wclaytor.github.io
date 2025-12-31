#!/bin/bash

# Create timestamped directory for test run
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
REPORT_DIR="reports/${TIMESTAMP}"
mkdir -p "${REPORT_DIR}"

echo "Running smoke tests..."
echo "Results will be saved to: ${REPORT_DIR}"

# Run tests with all reports going to the timestamped directory
uv run pytest tests/smoke -v \
  --html="${REPORT_DIR}/report.html" --self-contained-html \
  --junit-xml="${REPORT_DIR}/report.xml" \
  --screenshot=on \
  --video=on \
  --tracing=retain-on-failure \
  2>&1 | tee "${REPORT_DIR}/test-output.txt"

# Copy Playwright artifacts to the report directory
if [ -d "test-results" ]; then
    mkdir -p "${REPORT_DIR}/test-results"
    cp -r test-results/* "${REPORT_DIR}/test-results/" 2>/dev/null || true
fi

echo "Test run complete!"
echo "View HTML report: ${REPORT_DIR}/report.html"
echo "View XML report: ${REPORT_DIR}/report.xml"
echo "View test output: ${REPORT_DIR}/test-output.txt"
echo "Screenshots and videos are in: ${REPORT_DIR}/test-results"