# Web Application Testing Tutorial

**Skill:** webapp-testing  
**Duration:** 30-45 minutes  
**Level:** Beginner to Intermediate  

> **What you'll learn:** How to use Playwright to test and automate local web applications, capture screenshots, discover elements, debug UI behavior, and verify frontend functionality.

---

## Phase 1: Foundation

### What is the webapp-testing Skill?

The **webapp-testing** skill is your toolkit for interacting with and testing web applications using Playwright. Think of it as having a robot that can:

- **Visit web pages** (both local files and running servers)
- **Click buttons and fill forms** like a real user would
- **Take screenshots** to capture what the page looks like
- **Find elements** on a page (buttons, links, inputs)
- **Capture console logs** to debug JavaScript issues
- **Verify functionality** works correctly

### When Should You Use This Skill?

✅ **Use webapp-testing when you need to:**
- Verify your website looks and works correctly
- Automate repetitive testing tasks
- Debug UI issues by capturing screenshots
- Discover what elements exist on a dynamic page
- Test forms, navigation, and interactive features
- Capture console errors from JavaScript

❌ **Don't use this skill when you:**
- Need to run backend unit tests (use pytest instead)
- Want to test APIs directly (use requests/httpx)
- Only need to validate static HTML syntax (use validators)

### Prerequisites Check

Before we begin, let's make sure you have what you need:

**Required:**
- Python 3.8 or higher
- Playwright installed (`pip install playwright`)
- Playwright browsers installed (`playwright install chromium`)

**Let's verify your setup:**

```bash
# Check Python version
python --version

# Verify Playwright is installed
python -c "from playwright.sync_api import sync_playwright; print('✅ Playwright ready!')"
```

If you see an error, install Playwright first:
```bash
pip install playwright
playwright install chromium
```

### Your First Success: A Simple Screenshot

Let's start with the simplest possible example - taking a screenshot of a webpage. Create a file called `first_test.py`:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch a headless Chrome browser
    browser = p.chromium.launch(headless=True)
    
    # Open a new page
    page = browser.new_page()
    
    # Visit a website (using Python docs as example)
    page.goto('https://www.python.org')
    
    # Take a screenshot
    page.screenshot(path='/tmp/python_org.png')
    print('✅ Screenshot saved to /tmp/python_org.png')
    
    # Always close the browser when done
    browser.close()
```

Run it:
```bash
python first_test.py
```

**🎉 Congratulations!** You just automated a browser. Open `/tmp/python_org.png` to see the captured page.

**Checkpoint:** Do you have a screenshot file? If yes, you're ready to continue!

---

## Phase 2: Core Concepts

Now that you've got the basics, let's explore the essential patterns you'll use 80% of the time.

### Concept 1: The Decision Tree

The webapp-testing skill uses a decision tree to determine the best approach:

```
Is it static HTML?
├─ Yes → Read HTML file directly, use file:// URL
│
└─ No (dynamic webapp) → Is the server already running?
    ├─ No → Use with_server.py helper
    │
    └─ Yes → Use reconnaissance-then-action pattern
```

Let's explore each scenario.

### Concept 2: Testing Static HTML Files

For static HTML files (no JavaScript framework, no server needed), you can open them directly with `file://` URLs.

**Example: Testing Your Portfolio's HTML**

```python
from playwright.sync_api import sync_playwright
import os

# Get the absolute path to your HTML file
html_path = os.path.abspath('index.html')
file_url = f'file://{html_path}'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # Set a specific viewport size (good for consistency)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    
    # Navigate to local HTML file
    page.goto(file_url)
    
    # Take a screenshot
    page.screenshot(path='/tmp/my_page.png', full_page=True)
    print(f'✅ Screenshot of {html_path} saved!')
    
    browser.close()
```

**Key Points:**
- Use `os.path.abspath()` to get the full path
- Prefix with `file://` for local files
- `full_page=True` captures the entire scrollable page

**🔧 Try it yourself:** Modify this script to capture a screenshot of your `index.html` file.

### Concept 3: Discovering Elements

Before you can interact with a page, you need to know what's on it. The **reconnaissance-then-action** pattern is your friend:

1. Navigate to the page
2. Wait for it to load completely
3. Discover what elements exist
4. Then take action

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Navigate and WAIT for JavaScript to finish loading
    page.goto('http://localhost:3000')  # Your app URL
    page.wait_for_load_state('networkidle')  # ⚠️ CRITICAL for dynamic apps!
    
    # Discover all buttons
    buttons = page.locator('button').all()
    print(f"Found {len(buttons)} buttons:")
    for i, button in enumerate(buttons):
        text = button.inner_text() if button.is_visible() else "[hidden]"
        print(f"  [{i}] {text}")
    
    # Discover all links
    links = page.locator('a[href]').all()
    print(f"\nFound {len(links)} links:")
    for link in links[:5]:  # Show first 5
        text = link.inner_text().strip()
        href = link.get_attribute('href')
        print(f"  - '{text}' → {href}")
    
    # Discover input fields
    inputs = page.locator('input, textarea, select').all()
    print(f"\nFound {len(inputs)} input fields:")
    for inp in inputs:
        name = inp.get_attribute('name') or inp.get_attribute('id') or "[unnamed]"
        input_type = inp.get_attribute('type') or 'text'
        print(f"  - {name} ({input_type})")
    
    # Take a visual reference screenshot
    page.screenshot(path='/tmp/discovery.png', full_page=True)
    
    browser.close()
```

**⚠️ Common Pitfall:** Forgetting `page.wait_for_load_state('networkidle')` 

On dynamic pages (React, Vue, etc.), the HTML loads first, then JavaScript populates the content. If you inspect too early, you'll find nothing!

❌ **Wrong:**
```python
page.goto('http://localhost:3000')
buttons = page.locator('button').all()  # Often empty!
```

✅ **Right:**
```python
page.goto('http://localhost:3000')
page.wait_for_load_state('networkidle')  # Wait for JS to finish
buttons = page.locator('button').all()  # Now they're there!
```

### Concept 4: Interacting with Elements

Once you've discovered elements, you can interact with them:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:3000')
    page.wait_for_load_state('networkidle')
    
    # Click a button (multiple selector strategies)
    page.click('text=Submit')           # By visible text
    page.click('button.primary')         # By CSS class
    page.click('#submit-btn')            # By ID
    page.click('role=button[name="Go"]') # By ARIA role
    
    # Fill form fields
    page.fill('#name', 'John Doe')
    page.fill('input[type="email"]', 'john@example.com')
    page.fill('textarea', 'This is my message')
    
    # Select from dropdown
    page.select_option('select#country', 'US')
    
    # Check a checkbox
    page.check('input[type="checkbox"]')
    
    # Wait for something to appear after an action
    page.wait_for_selector('.success-message')
    
    browser.close()
```

**Selector Cheat Sheet:**

| Selector | Example | When to Use |
|----------|---------|-------------|
| `text=` | `text=Submit` | Visible button/link text |
| `#id` | `#submit-btn` | Element has an ID |
| `.class` | `.btn-primary` | Element has a class |
| `[attr]` | `[data-testid="login"]` | Element has an attribute |
| `role=` | `role=button` | Accessibility role |

**Tip:** When writing tests, prefer `data-testid` attributes - they're stable and won't break when styling changes.

### Concept 5: Capturing Console Logs

Debugging JavaScript issues? Capture what's logged to the browser console:

```python
from playwright.sync_api import sync_playwright

console_logs = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Set up console log capture BEFORE navigating
    def handle_console(msg):
        log_entry = f"[{msg.type}] {msg.text}"
        console_logs.append(log_entry)
        print(f"Console: {log_entry}")
    
    page.on("console", handle_console)
    
    # Now navigate and interact
    page.goto('http://localhost:3000')
    page.wait_for_load_state('networkidle')
    
    # Trigger some action that might log
    page.click('text=Load Data')
    page.wait_for_timeout(2000)  # Wait for async operations
    
    browser.close()

# Review captured logs
print(f"\n📋 Captured {len(console_logs)} console messages")
for log in console_logs:
    print(f"  {log}")
```

**Console message types:**
- `log` - Regular console.log()
- `warning` - console.warn()
- `error` - console.error() ← Pay attention to these!
- `info` - console.info()

### Concept 6: Using the with_server.py Helper

When you need to start a server for testing, use the bundled helper script. **Always run `--help` first!**

```bash
python scripts/with_server.py --help
```

**Single server (e.g., frontend only):**
```bash
python scripts/with_server.py \
  --server "npm run dev" \
  --port 5173 \
  -- python your_test_script.py
```

**Multiple servers (e.g., backend + frontend):**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_test_script.py
```

The helper:
1. Starts your server(s)
2. Waits for them to be ready
3. Runs your test script
4. Shuts down servers when done

Your test script stays simple - just Playwright logic:

```python
# your_test_script.py - no server management needed!
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.goto('http://localhost:5173')  # Server is already running!
    page.wait_for_load_state('networkidle')
    
    # Your test logic here...
    page.screenshot(path='/tmp/test_result.png')
    
    browser.close()
```

---

## Phase 3: Practical Application

Let's apply what you've learned to test this actual portfolio website.

### Project: Testing Your Homepage

Let's create a comprehensive test script for the homepage:

```python
#!/usr/bin/env python3
"""
Homepage Test Script
Tests the main index.html of the portfolio site
"""
from playwright.sync_api import sync_playwright
import os

# Configuration
HTML_FILE = os.path.abspath('index.html')
FILE_URL = f'file://{HTML_FILE}'
OUTPUT_DIR = '/tmp/homepage_tests'

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

def test_homepage():
    """Run all homepage tests"""
    console_errors = []
    test_results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # Capture console errors
        def capture_console(msg):
            if msg.type == 'error':
                console_errors.append(msg.text)
        page.on("console", capture_console)
        
        # Navigate to homepage
        page.goto(FILE_URL)
        
        # TEST 1: Page loads successfully
        title = page.title()
        test_results.append(('Page has title', bool(title)))
        print(f"✓ Page title: {title}")
        
        # TEST 2: Take desktop screenshot
        page.screenshot(path=f'{OUTPUT_DIR}/desktop.png', full_page=True)
        test_results.append(('Desktop screenshot captured', True))
        print(f"✓ Desktop screenshot saved")
        
        # TEST 3: Check navigation exists
        nav_links = page.locator('nav a, header a').all()
        test_results.append(('Has navigation links', len(nav_links) > 0))
        print(f"✓ Found {len(nav_links)} navigation links")
        
        # TEST 4: Check for main content sections
        main_content = page.locator('main, .main-content, #content').first
        has_content = main_content.is_visible() if main_content else False
        test_results.append(('Has main content area', has_content))
        
        # TEST 5: Check for proper heading structure
        h1_elements = page.locator('h1').all()
        test_results.append(('Has h1 heading', len(h1_elements) > 0))
        print(f"✓ Found {len(h1_elements)} h1 elements")
        
        # TEST 6: Mobile viewport test
        page.set_viewport_size({'width': 375, 'height': 667})
        page.wait_for_timeout(500)  # Allow for responsive adjustments
        page.screenshot(path=f'{OUTPUT_DIR}/mobile.png', full_page=True)
        test_results.append(('Mobile screenshot captured', True))
        print(f"✓ Mobile screenshot saved")
        
        # TEST 7: Tablet viewport test
        page.set_viewport_size({'width': 768, 'height': 1024})
        page.wait_for_timeout(500)
        page.screenshot(path=f'{OUTPUT_DIR}/tablet.png', full_page=True)
        test_results.append(('Tablet screenshot captured', True))
        print(f"✓ Tablet screenshot saved")
        
        # TEST 8: Check for console errors
        test_results.append(('No console errors', len(console_errors) == 0))
        if console_errors:
            print(f"⚠️ Console errors found: {console_errors}")
        else:
            print(f"✓ No console errors")
        
        browser.close()
    
    # Summary
    print("\n" + "="*50)
    print("TEST RESULTS SUMMARY")
    print("="*50)
    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)
    
    for name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}: {name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    print(f"Screenshots saved to: {OUTPUT_DIR}/")
    
    return passed == total

if __name__ == '__main__':
    success = test_homepage()
    exit(0 if success else 1)
```

**Save this as `test_homepage.py` and run it:**
```bash
python test_homepage.py
```

**What this tests:**
1. Page loads with a title
2. Desktop view screenshot
3. Navigation links exist
4. Main content area exists  
5. Proper heading structure (h1)
6. Mobile responsive screenshot
7. Tablet responsive screenshot
8. No JavaScript console errors

### Enhancing Your Tests

Now let's add more sophisticated checks:

```python
def test_accessibility_basics(page):
    """Check basic accessibility requirements"""
    results = []
    
    # Check all images have alt text
    images = page.locator('img').all()
    images_with_alt = [img for img in images if img.get_attribute('alt')]
    results.append((
        'All images have alt text',
        len(images_with_alt) == len(images)
    ))
    
    # Check for skip link (accessibility best practice)
    skip_link = page.locator('a[href="#main"], a[href="#content"], .skip-link').first
    results.append((
        'Has skip navigation link',
        skip_link.is_visible() if skip_link else False
    ))
    
    # Check color contrast (basic - look for very light text)
    # Note: For full contrast checking, use axe or similar tools
    
    # Check that interactive elements are keyboard accessible
    buttons = page.locator('button, [role="button"]').all()
    for btn in buttons:
        has_focus = btn.evaluate('el => el.tabIndex >= 0 || el.tagName === "BUTTON"')
        if not has_focus:
            results.append(('Button keyboard accessible', False))
            break
    else:
        results.append(('Buttons keyboard accessible', True))
    
    return results
```

### Debugging Common Issues

**Issue: "Page looks empty in screenshot"**

This usually means JavaScript hasn't finished loading:

```python
# ❌ Problem
page.goto('http://localhost:3000')
page.screenshot(path='empty.png')  # Blank!

# ✅ Solution
page.goto('http://localhost:3000')
page.wait_for_load_state('networkidle')  # Wait for JS
page.screenshot(path='full.png')  # Now it works!
```

**Issue: "Can't find element that I can see on the page"**

The element might be in a shadow DOM or iframe:

```python
# Check if element is in an iframe
frame = page.frame_locator('iframe').first
button = frame.locator('button')

# Or the selector might be wrong - print what's actually there
print(page.content())  # See the raw HTML
```

**Issue: "Click doesn't work"**

Element might not be visible or clickable:

```python
# Wait for element to be visible AND enabled
page.wait_for_selector('button.submit:visible', state='visible')
page.click('button.submit')

# Or scroll it into view first
page.locator('button.submit').scroll_into_view_if_needed()
page.click('button.submit')
```

**Issue: "Test passes locally but fails in CI"**

Usually a timing issue:

```python
# Add explicit waits
page.wait_for_selector('.loaded-content')

# Or increase timeout
page.click('button', timeout=10000)  # 10 second timeout
```

---

## Phase 4: Next Steps

### Advanced Features to Explore

**1. Visual Regression Testing**
Compare screenshots to catch unexpected changes:
```python
# Take baseline
page.screenshot(path='baseline.png')

# Later, compare with current
page.screenshot(path='current.png')
# Then use image comparison tools
```

**2. Network Request Interception**
Mock API responses or monitor requests:
```python
page.route('**/api/**', lambda route: route.fulfill(
    status=200,
    body='{"data": "mocked"}'
))
```

**3. Multi-Browser Testing**
Test in different browsers:
```python
for browser_type in [p.chromium, p.firefox, p.webkit]:
    browser = browser_type.launch()
    # Run tests...
```

**4. Authenticated Testing**
Handle login flows:
```python
# Save authenticated state
context = browser.new_context(storage_state='auth.json')
```

### Reference: Quick Command Lookup

| Task | Code |
|------|------|
| Take screenshot | `page.screenshot(path='file.png')` |
| Full page screenshot | `page.screenshot(path='file.png', full_page=True)` |
| Click element | `page.click('selector')` |
| Fill input | `page.fill('selector', 'value')` |
| Get text | `page.locator('selector').inner_text()` |
| Wait for element | `page.wait_for_selector('selector')` |
| Wait for network | `page.wait_for_load_state('networkidle')` |
| Get all elements | `page.locator('selector').all()` |
| Check visibility | `page.locator('selector').is_visible()` |
| Get attribute | `page.locator('selector').get_attribute('attr')` |
| Set viewport | `page.set_viewport_size({'width': 375, 'height': 667})` |

### Where to Get Help

- **Playwright Docs:** https://playwright.dev/python/
- **Skill Examples:** Check `.claude/skills/webapp-testing/examples/`
- **Common Patterns:** See the decision tree in SKILL.md

---

## Summary

You've learned how to:

✅ Set up Playwright for web testing  
✅ Choose the right approach (static vs dynamic)  
✅ Discover elements on a page  
✅ Interact with forms and buttons  
✅ Capture screenshots at different viewports  
✅ Debug console errors  
✅ Use the with_server.py helper  
✅ Build comprehensive test scripts  

**Your Homework:** Create a test script that:
1. Tests your portfolio at mobile, tablet, and desktop sizes
2. Verifies all navigation links work
3. Checks for console errors
4. Captures screenshots for visual review

Happy testing! 🧪
