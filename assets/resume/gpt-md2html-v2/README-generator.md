# Resume Clean-Room Generator (Configurable)

This folder contains a **clean-room** implementation for generating a polished, accessible **standalone HTML resume** from a Markdown source file.

## What you get

- `build_resume.py` — offline generator (Markdown + config JSON -> single HTML file)
- `resume_template_configurable.html` — HTML template with **inline CSS/JS** (no dependencies)
- `resume.config.json` — configuration for UI + “short view” logic
- Your `resume.md` — the source of truth

The output HTML:
- Works on **GitHub Pages** (static hosting)
- Works **locally** by double-clicking the file (no `fetch()`)
- Supports **light/dark** (system/light/dark cycle)
- Includes **search**, **sticky nav**, **Home** (scroll-to-top)
- Collapses company descriptions by default (accessible `<details>/<summary>`)
- Has a **Short vs Full** view toggle with an animated transition
- Respects **prefers-reduced-motion**
- Is keyboard accessible and includes a “Skip to content” link

## How to use

1. Put these files in a folder:
   - `resume.md`
   - `resume_template_configurable.html`
   - `resume.config.json`
   - `build_resume.py`

2. Run:

```bash
python build_resume.py resume.md resume.html --config resume.config.json --template resume_template_configurable.html
```

3. Open `resume.html` in a browser (or publish it to GitHub Pages).

## Configuration

All behavior is controlled in `resume.config.json`. Key areas:

### UI

```json
"ui": {
  "defaultTheme": "system",
  "enableThemeToggle": true,
  "enableSearch": true,
  "enableNav": true,
  "enableViewToggle": true,
  "defaultView": "short",
  "rememberView": true,
  "rememberTheme": true,
  "collapseCompanyDescriptionsByDefault": true,
  "smoothScroll": true
}
```

- `defaultView`: `"short"` (2-page-ish) or `"full"`
- `rememberView` / `rememberTheme`: persists preference in `localStorage`
- `collapseCompanyDescriptionsByDefault`: controls `<details>` open/closed

### Short view logic (“2-page version”)

This generator creates **two view models** inside the HTML:
- **Full**: everything parsed from Markdown
- **Short**: derived from Full using this config block:

```json
"shortView": {
  "workExperience": { "jobsToKeep": 3, "bulletsPerJob": 3 },
  "sections": { "include": ["Summary","Work Experience","Skills","Education","Links"] },
  "earlierExperience": { "enabled": true, "label": "Earlier Experience", "format": "inline", "maxCompanies": 8 }
}
```

Derivation rules (implemented client-side in the template):
1. Keep the newest `jobsToKeep` roles in **Work Experience**.
2. For each, keep only the first `bulletsPerJob` bullets.
3. Remaining roles are summarized into a final “Earlier Experience” row (company names only).
4. Only sections in `sections.include` render in Short view.

This approach is intentionally simple and repeatable. If you want a different definition of “2 pages”
(e.g., keep all roles but fewer bullets, or always keep the Sabbatical), you only change:
- `resume.config.json` values, or
- the `buildShortModel()` function in the template.

### Search

```json
"search": {
  "minQueryLength": 2,
  "highlightMatches": true,
  "fields": ["Summary","Work Experience","Skills","Education"]
}
```

- Filters cards and highlights matches using `<mark>`.

## How to regard the resulting HTML

- Treat `resume.html` as a **compiled artifact** (like a build output).
- Treat `resume.md` + `resume.config.json` + `resume_template_configurable.html` as your **source**.
- If you update your Markdown resume, just re-run the generator.

## Notes / limitations

- The Markdown parser is intentionally minimal (bold/italic/code/links, paragraphs, lists).
- Work Experience parsing expects a structure similar to your resume (role heading `###`, company line `**Company**`, etc.).
- If your Markdown changes shape dramatically, you may need to adjust the parsing heuristics in `build_resume.py`.

