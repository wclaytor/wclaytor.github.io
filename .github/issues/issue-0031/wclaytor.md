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

---

# From the repository root

python -m http.server 8000

# Then run tests in another terminal

cd tests/playwright && ./run-smoke.sh

---

Please update the script to include the list reporter.

---

We have the run-smoke script to run the smoke tests. Please create corresponding scripts to run the other categories, and a 'run-all' version to run all tests.

-rwxr-xr-x 1 pwuser pwuser 1006 Dec 31 18:24 run-accessibility.sh
-rwxr-xr-x 1 pwuser pwuser 1075 Dec 31 18:24 run-all.sh
-rwxr-xr-x 1 pwuser pwuser 1000 Dec 31 18:24 run-functional.sh
-rwxr-xr-x 1 pwuser pwuser 1002 Dec 31 18:24 run-performance.sh
-rwxr-xr-x 1 pwuser pwuser 989 Dec 30 18:36 run-smoke.sh
-rwxr-xr-x 1 pwuser pwuser 1003 Dec 31 18:24 run-visual.sh

---

We are implementing our testing approach per the test plan. Please become familiar with it and the supporting docs it references.

We have the initial smoke tests in place. Let us proceed with the Functional Tests - Homepage section of the plan.

We want to use an iterative approach where we implement the tests for each section, run them via the corresponding run script (i.e. run-functional), review the results, fix any issues, and then move on to the next section.

Let us start with the 3.2.1 Masthead Section. Please implement those tests per the plan and then we can review them.

---

Nice! At the end of each run, we would like to take the xml test report that we copy to the timestamped folder and create a nicely formatted Markdown version of the test report with a summary and then detailed results.

So we should create a Python script in our utilities folder **using our uv pattern** that converts the XML report into our sweet Markdown report. The default should be to save the Markdown file to the same location as the XML file but should have an output option if the user wants to save it elsewhere.

---

We have our test plan and we have some tests in place. At this point we realize that we need a way to track our progress. We are already using GitHub issues, so we should create an epic for each of the categories in '3. Test Categories' with an issue for each test. We can use our `scripts/github/issues-create-epic` script to create the epics and issues in GitHub. We just need to create the epic Markdown files for each epic. Please create those epic files for each category one at a time. We will review each and then proceed with the next.

uv run --directory ./scripts/github/issues-create-epic \
 issues-create-epic "$PWD/tests/playwright/epics/epic-smoke-tests.md" --dry-run

uv run --directory ./scripts/github/issues-create-epic \
 issues-create-epic "$PWD/scripts/github/issues-create-epic/test-epic.md" --dry-run

---

Let us create a README.md file for each of the test categories that describes what they are, what test files / tests they contain, and the current status of those tests. This should map to the test plan contents for that category.

Please start with the smoke tests.
