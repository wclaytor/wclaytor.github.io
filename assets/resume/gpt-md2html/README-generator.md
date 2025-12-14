# Clean-room Markdown → Standalone HTML Resume (Generator Variant)

This folder contains a **no-dependencies** “clean room” experiment that turns a Markdown resume into a **single, standalone HTML file** suitable for:

- GitHub Pages
- local viewing (double-click the file)
- printing to PDF

It’s designed to be **accessible**, **mobile-friendly**, and **easy to regenerate** whenever the Markdown changes.

## Files

- `build_resume.py` — the generator script
- `resume_template.html` — the standalone HTML template (CSS + JS included) with two placeholders:
  - `__NAME__` (for the page title / header)
  - `__JSON__` (the parsed resume data embedded as JSON)
- `resume-from-markdown.html` — example output generated from the provided resume (your generated artifact)

## How to generate

From the directory containing these files:

```bash
python build_resume.py resume.md resume.html
```

Where:
- `resume.md` is your Markdown resume
- `resume.html` is the output file you can host or open locally

### GitHub Pages

Commit `resume.html` into your repo and enable GitHub Pages for that branch/folder. The file is fully self-contained (no external assets).

## Features in the HTML

### Light / Dark mode
- Toggle in the toolbar
- Preference stored in `localStorage`

### Full vs Two-page view (with animated transition)
- Toolbar toggle switches between:
  - **Full**: renders everything in your Markdown
  - **Two-page**: a compact “recruiter skim” view derived automatically
- View preference stored in `localStorage`

**Two-page derivation logic (the key experiment):**
1. Keep the **newest 3 Work Experience entries** (top 3 jobs as listed in Markdown).
   - This includes your sabbatical if it appears among the newest 3.
2. For each retained job, keep **at most 3 bullets per group** (e.g., “Automation & Innovation”, “Leadership…”).
3. Replace the remaining (older) roles with a single **Earlier Experience** line listing the remaining company names.

This intentionally prioritizes:
- recent impact
- readability
- consistent “2-page-ish” density without hand-curation

If you want a different short-view policy, the logic lives in the HTML’s `buildShortModel()` function (search for that name in the generated output / template).

### Search
- Type to filter the page to matching sections and highlight occurrences with `<mark>`
- Press `/` to focus search
- `Esc` clears when search is focused

### Navigation
- Desktop left nav + mobile “Menu”
- “Home” button scrolls to the **true top of the page** (implemented via `window.scrollTo({top: 0})`)

### Company descriptions collapsed by default
Company descriptions are rendered in an accessible:

- `<details>`
- `<summary>Company overview</summary>`

This is keyboard accessible and screen-reader friendly.

### Print / PDF
- Toolbar “Print”
- Print CSS removes nav/toolbar and prints a clean single-column resume

## Accessibility notes

The template was designed with:
- semantic structure (real headings, lists)
- keyboard focus styles (`:focus-visible`)
- skip link (“Skip to content”)
- accessible toggles (`aria-pressed`, `aria-expanded`)
- prefers-reduced-motion support (transitions disable automatically)

## How users should regard the HTML file

Think of the HTML as a **presentation layer** and the Markdown as the **source of truth**:

- Edit the Markdown
- Re-run `build_resume.py`
- Commit/ship the generated HTML

The generated HTML contains no external dependencies and should behave consistently on GitHub Pages and locally.

---

If you want a “pure runtime” approach (HTML fetches `resume.md` and parses it in-browser), that can also be done, but it typically requires hosting (local `file://` fetches can be blocked by browser security rules). This generator approach avoids that issue entirely.
