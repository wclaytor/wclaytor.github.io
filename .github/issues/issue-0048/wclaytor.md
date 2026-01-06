# wclaytor

# From the repository root

python -m http.server 8000

# Then run tests in another terminal

cd tests/playwright && ./run-smoke.sh
cd tests/playwright && ./run-functional.sh

cd tests/playwright && ./run-all.sh

---

We are working on adding test coverage per the test plan. We want to add one section at a time, then pause and review before moving on to the next. Please continue where we left off.

-

Nice! Please proceed with the next section.

---

We would like a new index.html page for the projects folder that redirectsmain page: https://wclaytor.github.io/#projects

Nice! Please update the test plan to reflect this change.

--

Why is the code implemented in the init file?!?!

-

Yes, please refactor this into a proper package structure.

---

Users love the Markdown report! They requested that when there is a test failure that we link to the test file in the details section like so:

File: [test_critical_navigation.py](../../tests/smoke/test_critical_navigation.py)

I have updated the previous report to show exactly how this should look. Please update the script to include this when generating the report.

---

We have one test failure. In this case the test should be updated. This is the brand link so it should always link to the branded website regardless of what host we are testing on.

---

Nice! We have the latest test report from our full run. Please create a TEST_STATUS.md file that provides the current status of our test suite relative to the test plan so that we know what we have done, where we stand, and what we have left to do.

---

Nice! What is next?

-

Thanks! Please proceed with your recommendation.

---

The issue is that there is an animation as the menu expands and contracts. It works fine if you wait and then click it again. But if you do a true double click it won't work. The test should wait until it has expanded before trying to close it.

---

Nice! Let us continue implementing the remaining tests so that we can close this PR with a full test suite and results. We will continue to pause and create issues if we find them. Then we will resolve those issues in the future in separate PRs.

-

We have just run the tests after the previous update. Please verify that the test status doc is up to date.

Please proceed.
