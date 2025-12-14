#!/usr/bin/env python3
"""
build_resume.py
---------------
Offline generator: Markdown resume + config JSON -> standalone HTML (GitHub Pages / local friendly).

Usage:
  python build_resume.py resume.md resume.html --config resume.config.json

Notes:
- No runtime fetch (works from file://).
- Output is a single HTML file (CSS/JS inline).
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any, Optional


@dataclass
class Link:
    label: str
    url: str


@dataclass
class Job:
    role: str = ""
    company: str = ""
    location: str = ""
    dates: str = ""
    description: str = ""
    bullets: List[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["bullets"] = self.bullets or []
        d["kind"] = "job"
        return d


@dataclass
class Section:
    title: str
    kind: str
    html: str = ""
    items: List[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if self.items is None:
            d["items"] = []
        return d


def escape_html(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def md_inline_to_html(text: str) -> str:
    """
    Minimal inline Markdown:
    - **bold**
    - *italic*
    - `code`
    - [label](url)
    """
    t = escape_html(text)

    # links first (avoid conflict with emphasis)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" rel="noopener">\1</a>', t)

    # code
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)

    # bold / italic
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)
    return t


def md_block_to_html(lines: List[str]) -> str:
    """
    Minimal block Markdown renderer for the non-Work sections:
    - paragraphs
    - unordered lists
    - horizontal rule (---)
    """
    out: List[str] = []
    buf: List[str] = []

    def flush_paragraph():
        nonlocal buf
        if buf:
            out.append("<p>" + md_inline_to_html(" ".join(buf).strip()) + "</p>")
            buf = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip():
            flush_paragraph()
            i += 1
            continue

        if line.strip() == "---":
            flush_paragraph()
            out.append("<hr />")
            i += 1
            continue

        m_ul = re.match(r"^\s*-\s+(.*)$", line)
        if m_ul:
            flush_paragraph()
            items = []
            while i < len(lines):
                m2 = re.match(r"^\s*-\s+(.*)$", lines[i].rstrip())
                if not m2:
                    break
                items.append("<li>" + md_inline_to_html(m2.group(1).strip()) + "</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        # default: paragraph line
        buf.append(line.strip())
        i += 1

    flush_paragraph()
    return "\n".join(out)


def parse_resume(md_text: str) -> Dict[str, Any]:
    lines = md_text.splitlines()

    name = ""
    location = ""
    email = ""
    links: List[Link] = []
    sections: List[Section] = []

    # Extract name from first H1
    for ln in lines:
        if ln.startswith("# "):
            name = ln[2:].strip()
            break

    # Rough header parsing: look for a line like "Bel Air, MD | Tucson, AZ" then email
    for idx, ln in enumerate(lines[:25]):
        if "|" in ln and "http" not in ln and "##" not in ln and "claytor" not in ln:
            location = ln.strip()
        if "@" in ln and " " not in ln and ln.strip().count("@") == 1:
            email = ln.strip()

    # Split top-level sections by "## "
    cur_title = None
    cur_lines: List[str] = []
    for ln in lines:
        if ln.startswith("## "):
            if cur_title:
                sections.append(_parse_section(cur_title, cur_lines))
            cur_title = ln[3:].strip()
            cur_lines = []
        else:
            if cur_title:
                cur_lines.append(ln)
    if cur_title:
        sections.append(_parse_section(cur_title, cur_lines))

    # Extract Links section into structured links if present
    for s in list(sections):
        if s.title.lower() == "links":
            # parse "- Label: url"
            for ln in s.html.splitlines():
                pass  # html already rendered; instead parse from original lines:
            # We'll re-parse from s._raw if we had it; but we don't. Keep simple by scanning md_text.
            block = _extract_section_block(md_text, "Links")
            for ln in block.splitlines():
                m = re.match(r"^\s*-\s+([^:]+):\s*(\S+)\s*$", ln)
                if m:
                    links.append(Link(label=m.group(1).strip(), url=m.group(2).strip()))
            # Remove Links section from main sections; we render it in the header card
            sections.remove(s)
            break

    return {
        "name": name,
        "location": location,
        "email": email,
        "links": [asdict(l) for l in links],
        "sections": [s.to_dict() for s in sections],
    }


def _extract_section_block(md_text: str, title: str) -> str:
    # naive extraction of lines between "## title" and next "## "
    pat = re.compile(rf"^##\s+{re.escape(title)}\s*$", re.MULTILINE)
    m = pat.search(md_text)
    if not m:
        return ""
    start = m.end()
    rest = md_text[start:]
    m2 = re.search(r"^##\s+", rest, re.MULTILINE)
    end = start + (m2.start() if m2 else len(rest))
    return md_text[start:end].strip("\n")


def _parse_section(title: str, raw_lines: List[str]) -> Section:
    if title.lower() == "work experience":
        return _parse_work_experience(title, raw_lines)
    # Everything else: minimal markdown blocks
    html = md_block_to_html([ln for ln in raw_lines if not ln.strip().startswith("<!--")])
    return Section(title=title, kind="text", html=html, items=[])


def _parse_work_experience(title: str, raw_lines: List[str]) -> Section:
    jobs: List[Job] = []

    # Split by "### " role headings
    current_role = None
    cur: List[str] = []

    def flush():
        nonlocal current_role, cur
        if current_role:
            jobs.append(_parse_job(current_role, cur))
        current_role = None
        cur = []

    for ln in raw_lines:
        if ln.startswith("### "):
            flush()
            current_role = ln[4:].strip()
        else:
            if current_role is not None:
                cur.append(ln.rstrip())

    flush()

    return Section(title=title, kind="work", html="", items=[j.to_dict() for j in jobs])


def _parse_job(role: str, lines: List[str]) -> Job:
    # Expected pattern (from your resume):
    # **Company**
    # Location
    # 05/2023 – 12/2025
    # [optional blank]
    # Company description sentence(s).
    # Then bullets grouped under subheadings.
    company = ""
    location = ""
    dates = ""
    description_lines: List[str] = []
    bullets: List[str] = []

    i = 0

    # company line
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip().startswith("**") and lines[i].strip().endswith("**"):
        company = lines[i].strip().strip("*").strip()
        i += 1

    # location line
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(("**", "-", "####", "###")):
        location = lines[i].strip()
        i += 1

    # dates line
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and re.search(r"\d{2}/\d{4}", lines[i]):
        dates = lines[i].strip()
        i += 1

    # description until first heading/bullet
    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith(("**", "####", "- ")):
            break
        if ln:
            description_lines.append(ln)
        i += 1

    # bullets: include subheadings as bold labels inside list items (rendered inline)
    while i < len(lines):
        ln = lines[i].rstrip()
        m = re.match(r"^\s*-\s+(.*)$", ln)
        if m:
            bullets.append(md_inline_to_html(m.group(1).strip()))
        i += 1

    return Job(
        role=role,
        company=company,
        location=location,
        dates=dates,
        description=" ".join(description_lines).strip(),
        bullets=bullets,
    )


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_md", type=Path)
    ap.add_argument("output_html", type=Path)
    ap.add_argument("--template", type=Path, default=Path("resume_template_configurable.html"))
    ap.add_argument("--config", type=Path, default=Path("resume.config.json"))
    args = ap.parse_args()

    md_text = args.input_md.read_text(encoding="utf-8")
    model = parse_resume(md_text)

    config = json.loads(args.config.read_text(encoding="utf-8"))

    template = load_template(args.template)
    title = model.get("name") or "Resume"
    html = template.replace("__TITLE__", title)
    html = html.replace("__DATA_JSON__", json.dumps(model, ensure_ascii=False))
    html = html.replace("__CONFIG_JSON__", json.dumps(config, ensure_ascii=False))

    args.output_html.write_text(html, encoding="utf-8")
    print(f"Wrote {args.output_html}")


if __name__ == "__main__":
    main()
