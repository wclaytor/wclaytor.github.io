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
