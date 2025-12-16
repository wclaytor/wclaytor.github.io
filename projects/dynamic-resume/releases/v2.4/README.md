# Dynamic Resume v2.3

A **zero-dependency** Markdown-to-HTML resume generator that creates a **single, standalone HTML file** suitable for GitHub Pages, local viewing, printing to PDF, and professional portfolio sites. Built for accessibility, mobile-first design, and easy regeneration.

## Files

- `build_resume.py` — Python generator script
- `resume_template_configurable.html` — HTML template with embedded CSS + JavaScript
- `william-claytor-resume.md` — Example Markdown resume
- `test.html` — Generated output for testing

## Quick Start

```bash
python build_resume.py resume.md output.html
```

Optional custom config:

```bash
python build_resume.py resume.md output.html --config custom.config.json
```

## Features

### Theme Toggle
- Cycles through Auto → Dark → Light
- Auto respects system preferences
- Stored in localStorage

### Content Views
- **Short**: Recent 3 positions, top 3 bullets each, earlier experience summarized
- **Full**: Complete resume with all details
- Smooth animated transitions

### Navigation
- Desktop sidebar, mobile drawer
- Home scrolls to top
- Active section highlighting

### Links Section
- Format: "Label — URL" with clickable links
- Removed from header for cleaner design

### Print/PDF Ready
- Clean layout with hidden controls
- Optimized for printing

## Accessibility

- Semantic HTML5
- Full keyboard navigation
- Screen reader support
- WCAG color contrast
- Reduced motion support
- Mobile-first responsive

## Deployment

### GitHub Pages
```bash
python build_resume.py resume.md index.html
# Commit and enable GitHub Pages
```

### Local
Double-click the HTML file. Works offline.

## Philosophy

Markdown is the source of truth. Edit Markdown, regenerate HTML, deploy. Never edit generated HTML directly.

## v2.3 Updates

- Navigation: Home as first nav item
- Links: Fixed rendering, "Label — URL" format  
- UI: Removed search (use browser Ctrl+F)
- View button: Clear "Content: Short/Full" labels
- Cleaner toolbar with essential controls only

---

**Zero dependencies** • **Fully accessible** • **Print-ready**
