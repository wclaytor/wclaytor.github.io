# Clean-room Markdown → Standalone HTML Resume (Experiment)

This folder contains a **single-file, standalone HTML resume** generated from the Markdown resume:

- Source Markdown: `resume-wclaytor-2025-11.md`
- Output HTML: `resume.html`

The goal was to create a **GitHub Pages–friendly** resume that works locally (double-click open) and meets typical expectations for:
- **Responsive design** (desktop and mobile)
- **Accessibility** (keyboard-friendly, semantic landmarks, readable contrast, focus states, reduced-motion support)
- **Print/PDF export** (good print CSS, no external dependencies)

---

## What this HTML file includes

### 1) Light / dark mode toggle
- Uses CSS variables for theming.
- Defaults to the user’s OS preference (`prefers-color-scheme`).
- Saves the chosen theme to `localStorage` so it persists across visits.

### 2) Search feature
- A search box filters content to only sections that match.
- Matches are highlighted using `<mark>`.
- When a match occurs inside a role, its “Company details” is automatically expanded for context.
- Keyboard shortcut: press `/` to focus the search field.

### 3) Navigation feature
- A sticky left nav on desktop and a “Menu” button on mobile.
- Jump links to the major sections (Home, Summary, Work Experience, Education, Skills).
- The currently visible section is highlighted using an `IntersectionObserver`.

### 4) Company descriptions collapsed by default
- Implemented with native `<details>` / `<summary>` for maximum accessibility and simplicity.
- Defaults to collapsed; users can expand per role.

### 5) Short (≈2-page) view + Full view toggle, with animated transition
- There are two pre-rendered views:
  - **Short view** (“2-page view”) — focused, recruiter-friendly
  - **Full view** — complete career history
- The toggle switches views with a subtle slide/fade transition.
- The chosen view persists via `localStorage`.
- Keyboard shortcut: press `V` to toggle views.

### 6) Print / Save to PDF
- The **Print** button calls `window.print()`.
- Print CSS hides the header + navigation and removes shadows/borders.
- Works well with “Save to PDF” in Chrome/Edge/Safari.

Keyboard shortcut: press `P` to print.

---

## “2-page view” logic (how the short version was derived)

The short view intentionally optimizes for “first screen” readability and a typical recruiter scan:
1. **Keep**: Name, contact links, summary, skills, education.
2. **Keep**: Most recent roles in detail (insightsoftware, Sabbatical, Active911, Puppet).
3. **Condense**: Earlier experience into a single “Earlier career highlights” paragraph rather than listing each job.
4. **Prioritize**: The highest-signal, most unique bullets (AI-assisted workflows, pipeline automation, time savings, scale migrations).

This is a *presentation* decision only: the full view remains available with one click.

If you want a different “2-page” strategy (e.g., include NPR, or keep manager roles), change the short-view content accordingly.

---

## How to use

### Option A: View locally
1. Put `resume.html` somewhere on your computer.
2. Double-click it or open it in any modern browser.

### Option B: Host on GitHub Pages
1. Create a repository.
2. Add `resume.html` (and optionally rename it to `index.html`).
3. Enable GitHub Pages for the repo.
4. Point Pages at the branch/folder containing the HTML.

---

## How users should regard this HTML file

This `resume.html` is meant to be:
- A **presentation layer** that can be linked and shared
- A **print-ready view** for PDF export
- A **clean baseline** (no frameworks, no build system, no external CSS/JS)

It is **not** a replacement for:
- Your canonical Markdown resume (source of truth)
- An ATS-optimized plain-text/PDF version
- A full website (though it can be integrated into one)

---

## Notes on accessibility

Key accessibility choices:
- Skip link (“Skip to resume content”)
- Semantic landmarks: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`
- Keyboard support and visible focus rings (`:focus-visible`)
- Reduced motion support (`prefers-reduced-motion`)
- Native `<details>` for collapsible content

---

## How to recreate this experiment elsewhere

1. Start with the Markdown resume.
2. Decide which parts become:
   - “Short view”
   - “Full view”
3. Use semantic HTML sections and roles.
4. Add minimal JS for:
   - theme toggle (`localStorage`)
   - view toggle (`localStorage`)
   - search filtering + highlighting
   - active nav highlighting

Because the output is a single file, you can diff outputs across implementations easily.

---

## Ideas for future direction

If you want to evolve the project beyond this baseline:
- Auto-generate the short view from tags like `data-importance="high"` in Markdown
- Add per-skill filtering (“show roles that mention Playwright”)
- Add a timeline view for experience
- Export a PDF with consistent pagination using CSS Paged Media tooling

