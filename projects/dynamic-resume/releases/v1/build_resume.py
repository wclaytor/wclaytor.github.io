#!/usr/bin/env python3
"""
build_resume.py — clean-room Markdown -> standalone HTML resume generator.

Usage:
  python build_resume.py resume.md resume.html

Requires these files to be alongside this script:
  - resume_template.html  (contains __NAME__ and __JSON__ placeholders)

The Markdown must follow the same *structure* as the provided example:
  - '# Name' on first line
  - '## Links', '## Summary', '## Work Experience', '## Education', '## Skills'
  - Jobs start with '### <Role Title>' and bullets use '- '.

This is intentionally lightweight (no external deps) so it can run anywhere.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import datetime, html, json, pathlib, re, sys

@dataclass
class BulletGroup:
    heading: Optional[str] = None
    bullets: List[str] = field(default_factory=list)

@dataclass
class Job:
    title: str
    company: str = ""
    location: str = ""
    dates: str = ""
    company_desc: str = ""
    groups: List[BulletGroup] = field(default_factory=list)

@dataclass
class Resume:
    name: str = ""
    contact_lines: List[str] = field(default_factory=list)
    meta_bullets: List[str] = field(default_factory=list)
    links: List[Dict[str, str]] = field(default_factory=list)
    summary: str = ""
    work: List[Job] = field(default_factory=list)
    education_lines: List[str] = field(default_factory=list)
    skills: Dict[str, str] = field(default_factory=dict)

def parse_resume_markdown(md: str) -> Resume:
    lines = md.splitlines()
    i = 0
    res = Resume()

    # Name
    if lines and lines[0].startswith("# "):
        res.name = lines[0][2:].strip()
        i = 1

    # Contact lines until blank
    while i < len(lines) and lines[i].strip() != "":
        res.contact_lines.append(lines[i].strip())
        i += 1

    # Skip blanks
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    # Meta bullets (e.g., citizenship/relocation)
    while i < len(lines) and lines[i].lstrip().startswith("- "):
        res.meta_bullets.append(lines[i].lstrip()[2:].strip())
        i += 1

    def parse_links(start: int):
        links = []
        j = start
        while j < len(lines):
            if lines[j].startswith("## "):
                break
            m = re.match(r"-\s+([^:]+):\s+(.*)$", lines[j].strip())
            if m:
                links.append({"label": m.group(1).strip(), "url": m.group(2).strip()})
            j += 1
        return links, j

    def parse_summary(start: int):
        j = start
        txt = []
        while j < len(lines) and not lines[j].startswith("## "):
            if lines[j].strip() != "":
                txt.append(lines[j].strip())
            j += 1
        return " ".join(txt).strip(), j

    def parse_work(start: int):
        jobs = []
        j = start
        while j < len(lines):
            if lines[j].startswith("## ") and not lines[j].startswith("## Work Experience"):
                break
            if lines[j].startswith("### "):
                title = lines[j][4:].strip()
                job = Job(title=title)
                j += 1

                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                if j < len(lines) and "**" in lines[j]:
                    job.company = re.sub(r"\*\*", "", lines[j]).strip()
                    j += 1
                if j < len(lines) and lines[j].strip() != "":
                    job.location = lines[j].strip()
                    j += 1
                if j < len(lines) and re.search(r"\d{2}/\d{4}", lines[j]):
                    job.dates = lines[j].strip()
                    j += 1

                # Company description paragraph
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                desc = []
                while j < len(lines):
                    line = lines[j].strip()
                    if line == "":
                        j += 1
                        break
                    if line.startswith("**") and line.endswith(":**"):
                        break
                    if line.startswith("---") or line.startswith("### ") or line.startswith("## "):
                        break
                    desc.append(line)
                    j += 1
                job.company_desc = " ".join(desc).strip()

                current = BulletGroup()
                while j < len(lines):
                    line = lines[j].rstrip()
                    if line.startswith("---"):
                        j += 1
                        break
                    if line.startswith("### ") or line.startswith("## "):
                        break
                    m = re.match(r"\*\*(.+?)\:\*\*", line.strip())
                    if m:
                        if current.heading or current.bullets:
                            job.groups.append(current)
                        current = BulletGroup(heading=m.group(1).strip())
                        j += 1
                        continue
                    if line.lstrip().startswith("- "):
                        current.bullets.append(line.lstrip()[2:].strip())
                        j += 1
                        continue
                    j += 1
                if current.heading or current.bullets:
                    job.groups.append(current)

                jobs.append(job)
            else:
                j += 1
        return jobs, j

    def parse_education(start: int):
        j = start
        ed = []
        while j < len(lines) and not lines[j].startswith("## "):
            if lines[j].strip() != "":
                ed.append(lines[j].rstrip())
            j += 1
        return ed, j

    def parse_skills(start: int):
        j = start
        skills = {}
        while j < len(lines) and not lines[j].startswith("## "):
            line = lines[j].strip()
            m = re.match(r"\*\*(.+?)\*\*", line)
            if m:
                key = m.group(1).strip()
                j += 1
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                if j < len(lines) and not lines[j].startswith("**") and not lines[j].startswith("## "):
                    skills[key] = lines[j].strip()
            j += 1
        return skills, j

    while i < len(lines):
        if lines[i].startswith("## Links"):
            i += 1
            res.links, i = parse_links(i)
            continue
        if lines[i].startswith("## Summary"):
            i += 1
            res.summary, i = parse_summary(i)
            continue
        if lines[i].startswith("## Work Experience"):
            i += 1
            res.work, i = parse_work(i)
            continue
        if lines[i].startswith("## Education"):
            i += 1
            res.education_lines, i = parse_education(i)
            continue
        if lines[i].startswith("## Skills"):
            i += 1
            res.skills, i = parse_skills(i)
            continue
        i += 1

    return res

def safe_json_for_script(obj) -> str:
    s = json.dumps(obj, ensure_ascii=False)
    # Prevent accidentally closing the <script> tag.
    return s.replace("</", "<\\/")

def build(resume_md: pathlib.Path, out_html: pathlib.Path, template_html: pathlib.Path) -> None:
    md = resume_md.read_text(encoding="utf-8")
    resume = parse_resume_markdown(md)
    if not resume.name:
        raise SystemExit("Could not parse resume name; expected first line like '# First Last'.")

    data = {
        "name": resume.name,
        "contact": resume.contact_lines,
        "meta": resume.meta_bullets,
        "links": resume.links,
        "summary": resume.summary,
        "work": [
            {
                "title": j.title,
                "company": j.company,
                "location": j.location,
                "dates": j.dates,
                "company_desc": j.company_desc,
                "groups": [{"heading": g.heading, "bullets": g.bullets} for g in j.groups],
            }
            for j in resume.work
        ],
        "education": resume.education_lines,
        "skills": resume.skills,
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
    }

    tpl = template_html.read_text(encoding="utf-8")
    rendered = tpl.replace("__NAME__", html.escape(resume.name)).replace("__JSON__", safe_json_for_script(data))
    out_html.write_text(rendered, encoding="utf-8")

def main(argv: List[str]) -> int:
    if len(argv) < 3:
        print("Usage: python build_resume.py resume.md resume.html", file=sys.stderr)
        return 2

    resume_md = pathlib.Path(argv[1])
    out_html = pathlib.Path(argv[2])
    template_html = pathlib.Path(__file__).with_name("resume_template.html")

    if not template_html.exists():
        print("Error: resume_template.html must be next to build_resume.py", file=sys.stderr)
        return 1

    build(resume_md, out_html, template_html)
    print(f"Wrote {out_html}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
