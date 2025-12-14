#!/usr/bin/env python3
"""
build_resume.py — clean-room Markdown -> standalone HTML resume generator (configurable).

This script reads:
  1) a Markdown resume (source of truth)
  2) an optional JSON config file (controls short-view rules and UI defaults)
  3) an HTML template file (contains __DATA_JSON__, __CONFIG_JSON__, __TITLE__ placeholders)

and writes a single, standalone HTML file suitable for GitHub Pages or local viewing.

Usage:
  python build_resume.py resume.md resume.html \
    --config resume.config.json \
    --template resume_template_configurable.html
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "section"


def md_inline(text: str) -> str:
    """Very small, safe inline markdown: **bold**, *em*, `code`, and links [t](u)."""
    t = (text or "").strip()
    # Escape HTML
    t = (
        t.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )

    # Links first to avoid formatting inside URL
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)
    return t


def parse_links_block(lines: List[str]) -> List[Dict[str, str]]:
    links = []
    for ln in lines:
        ln = ln.strip()
        if not ln.startswith("-"):
            continue
        # "- Label: URL" OR "- Label — URL"
        m = re.match(r"-\s*(.+?)(?:\s*[:—-]\s*)(https?://\S+)\s*$", ln)
        if m:
            links.append({"label": m.group(1).strip(), "url": m.group(2).strip()})
        else:
            # "- https://example.com"
            m2 = re.match(r"-\s*(https?://\S+)\s*$", ln)
            if m2:
                links.append({"label": m2.group(1).strip(), "url": m2.group(1).strip()})
    return links


def parse_markdown_resume(md: str) -> Dict[str, Any]:
    """
    Parse the resume markdown into a small JSON model consumed by the template.

    Expected structure (loose):
      # Name
      Location line
      Email line (or anything containing '@')
      (optional bullets before first ## section are ignored for now)
      ## Links
      - Label: URL
      ## Summary
      ...
      ## Work Experience
      ### Role
      **Company**
      Location
      Dates
      (description)
      - bullets
      ...

    The template is designed to be forgiving: most sections are rendered as HTML blobs.
    """
    lines = md.splitlines()

    # Name
    name = ""
    i = 0
    while i < len(lines):
        if lines[i].startswith("# "):
            name = lines[i][2:].strip()
            i += 1
            break
        i += 1

    # Location/email in the next few non-empty lines
    location = ""
    email = ""
    scan = 0
    while i < len(lines) and scan < 12:
        ln = lines[i].strip()
        if ln.startswith("## "):
            break
        if ln and not ln.startswith("-"):
            if "@" in ln and not email:
                email = ln.strip()
            elif not location and "@" not in ln:
                location = ln.strip()
        i += 1
        scan += 1

    # Parse sections
    sections: List[Dict[str, Any]] = []
    cur_title = None
    cur_lines: List[str] = []
    cur_kind = "text"

    def flush():
        nonlocal cur_title, cur_lines, cur_kind, sections
        if not cur_title:
            return
        html = md_block_to_html(cur_lines)
        sections.append({"title": cur_title, "kind": cur_kind, "html": html, "items": []})
        cur_title, cur_lines, cur_kind = None, [], "text"

    # Rewind one line if we stopped at a section header
    # Find the first section header
    start = 0
    for idx, ln in enumerate(lines):
        if ln.startswith("## "):
            start = idx
            break

    for ln in lines[start:]:
        if ln.startswith("## "):
            flush()
            cur_title = ln[3:].strip()
            cur_lines = []
            cur_kind = "links" if cur_title.lower() == "links" else "text"
        else:
            if cur_title is not None:
                cur_lines.append(ln)

    flush()

    # Extract links as structured (also keep HTML in the section)
    links: List[Dict[str, str]] = []
    for sec in sections:
        if sec["title"].lower() == "links":
            links = parse_links_block(sec.get("raw_lines", []) if "raw_lines" in sec else cur_lines)
            # parse_links_block needs original lines; easiest is re-parse from html-less lines:
            links = parse_links_block(md_section_lines(md, "Links"))

    return {
        "name": name,
        "location": location,
        "email": email,
        "links": links,
        "sections": normalize_sections(sections, md),
    }


def md_section_lines(md: str, title: str) -> List[str]:
    """Return raw lines under a '## {title}' heading."""
    lines = md.splitlines()
    inside = False
    out = []
    for ln in lines:
        if ln.startswith("## "):
            inside = (ln[3:].strip().lower() == title.lower())
            continue
        if inside and ln.startswith("## "):
            break
        if inside:
            out.append(ln)
    return out


def normalize_sections(sections: List[Dict[str, Any]], md: str) -> List[Dict[str, Any]]:
    # Re-render Links section from raw lines so it looks nice
    out = []
    for sec in sections:
        if sec["title"].lower() == "links":
            raw = md_section_lines(md, "Links")
            links = parse_links_block(raw)
            items = [f'<li><a href="{escape_attr(l["url"])}" target="_blank" rel="noopener noreferrer">{md_inline(l["label"])}</a></li>' for l in links]
            sec["html"] = "<ul>" + "".join(items) + "</ul>" if items else ""
        out.append(sec)
    return out


def escape_attr(s: str) -> str:
    return (
        (s or "")
        .replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def md_block_to_html(lines: List[str]) -> str:
    """Minimal block markdown: paragraphs, bullets, ### headings, **company** lines."""
    html: List[str] = []
    buf: List[str] = []
    ul_open = False

    def flush_paragraph():
        nonlocal buf, html
        if buf:
            html.append("<p>" + md_inline(" ".join(buf).strip()) + "</p>")
            buf = []

    def close_ul():
        nonlocal ul_open, html
        if ul_open:
            html.append("</ul>")
            ul_open = False

    for raw in lines:
        ln = raw.rstrip()
        if not ln.strip():
            flush_paragraph()
            close_ul()
            continue

        if ln.startswith("### "):
            flush_paragraph()
            close_ul()
            html.append(f"<h3>{md_inline(ln[4:].strip())}</h3>")
            continue

        if ln.strip().startswith("- "):
            flush_paragraph()
            if not ul_open:
                html.append("<ul>")
                ul_open = True
            html.append("<li>" + md_inline(ln.strip()[2:].strip()) + "</li>")
            continue

        # Bold-only company line like **Company**
        if re.match(r"^\*\*.+\*\*\s*$", ln.strip()):
            flush_paragraph()
            close_ul()
            company = ln.strip().strip("*").strip()
            html.append(f"<div class=\"companyline\"><strong>{md_inline(company)}</strong></div>")
            continue

        buf.append(ln.strip())

    flush_paragraph()
    close_ul()
    return "\n".join(html).strip()


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise SystemExit(f"Failed to read JSON config at {path}: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_md", type=Path, help="Markdown resume file")
    ap.add_argument("output_html", type=Path, help="Output standalone HTML file")
    ap.add_argument("--config", type=Path, default=None, help="Optional JSON config (resume.config.json)")
    ap.add_argument("--template", type=Path, default=Path("resume_template_configurable.html"), help="HTML template file")
    args = ap.parse_args()

    md = args.input_md.read_text(encoding="utf-8")
    resume = parse_markdown_resume(md)

    if args.config is not None:
        config = load_json(args.config)
    else:
        config = {
            "ui": {"defaultView": "short", "sidebarTitle": "Navigation"},
            "shortView": {"workExperience": {"jobsToKeep": 3, "bulletsPerJob": 3}},
            "companyDescriptions": {"collapsedByDefault": True},
        }

    template = args.template.read_text(encoding="utf-8")

    out = template
    out = out.replace("__DATA_JSON__", json.dumps(resume, ensure_ascii=False))
    out = out.replace("__CONFIG_JSON__", json.dumps(config, ensure_ascii=False))
    out = out.replace("__TITLE__", resume.get("name") or "Resume")

    args.output_html.write_text(out, encoding="utf-8")
    print(f"Wrote {args.output_html}")


if __name__ == "__main__":
    main()
