# wclaytor

We would like the help of our adivors Kent Beck and Martin Fowler to help us create a testing strategy, testing architecture, and high level test plan for the website.

Here is what we know:

- The current version of the website was created as an update to our original site which only had manual exploratory testing.
- We just completed a massive series of updates in short time to meet a deadline. We also did a lot of manual exploratory testing of each update and we are very confident that the basic workflows are working as expected. The site is currently live and we have gotten good feedback from visitors.
- We want to use Playwright with Python and we like using uv for our Python projects.
- We want to use the Page Object Model.
- We want to be able to capture screenshots and use them for snapshot testing.
- We want to be able to capture recordings of our test runs.
- Playwright tests should be located in the `tests/playwright` folder, organized into subfolders based on test type.

---

We are seeing lots of errors when attempting to run the tests.

---

What is

I want to run the smoke tests with the command:

```
uv run pytest tests/smoke -v
```

What is the command to generate a timestamped HTML report in a specific location?

-

To generate a timestamped HTML report in a specific location with pytest, use:

```bash
uv run pytest tests/smoke -v --html=reports/smoke-test-$(date +%Y%m%d-%H%M%S).html --self-contained-html
```

This command:

- Runs smoke tests with verbose output (`-v`)
- Generates an HTML report with timestamp in the filename
- Places it in a `reports/` directory (create it first with `mkdir -p reports`)
- Makes it self-contained (all CSS/JS embedded) for easy sharing

**Note**: You'll need to install `pytest-html`:

```bash
cd tests/playwright
uv add pytest-html
```

**Alternative with a reports directory:**

```bash
# Create reports directory if it doesn't exist
mkdir -p tests/playwright/reports

# Run with timestamped report
uv run pytest tests/smoke -v --html=tests/playwright/reports/smoke-$(date +%Y%m%d-%H%M%S).html --self-contained-html
```

For easier use, you could add this to a Makefile or shell script:

```bash
#!/bin/bash
# filepath: tests/playwright/run_smoke_tests.sh
mkdir -p reports
uv run pytest tests/smoke -v --html=reports/smoke-$(date +%Y%m%d-%H%M%S).html --self-contained-html
```

python -m http.server 8000

cd tests/playwright

uv run pytest tests/smoke -v --html=reports/smoke-$(date +%Y%m%d-%H%M%S).html --self-contained-html

-

The HTML format is good for human users. What format should we use to generate the report to make it easy for Claude and Copilot to ingenst and help us troubleshoot issues?

---

uv run pytest tests/smoke -v --junit-xml=reports/smoke-$(date +%Y%m%d-%H%M%S).xml

-

mkdir -p reports
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
uv run pytest tests/smoke -v \
  --html=reports/smoke-${TIMESTAMP}.html --self-contained-html \
 --junit-xml=reports/smoke-${TIMESTAMP}.xml

---

Let us create a directory for each timestamp and then put the files in that directory, and include any generated screenshots so that each run has a timestamped folder with all the things.

---

# Make the script executable

chmod +x tests/playwright/run_smoke_tests.sh

# Run it

cd tests/playwright
./run_smoke_tests.sh

---

chmod +x ./run-smoke.sh

--

Nice! Please update the script to copy those files rather than move them.

-

Nice! Please update the script to copy those files to a 'test-results' sub-folder of the timestamped folder.

Please add a comment to the PR about our new run-smoke.sh script.

Please update the README to include our new run-smoke.sh script.

---

It appears our devcontainer does not have the gh command line tool. Please add it.

---

We are reviewing the test results. We want to discuss each failure and determine whether the test identified a bug or if the test needs to be updated.
