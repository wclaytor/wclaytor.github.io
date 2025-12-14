#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

def parse_markdown_resume(md: str) -> dict:
    lines = md.splitlines()

    name = ""
    header_lines = []
    header_bullets = []
    email = ""

    i = 0
    while i < len(lines) and not lines[i].startswith("# "):
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        name = lines[i][2:].strip()
        i += 1

    while i < len(lines) and not lines[i].startswith("## "):
        ln = lines[i].strip()
        if ln:
            if ln.startswith("- "):
                header_bullets.append(ln[2:].strip())
            else:
                if re.search(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", ln):
                    email = ln.strip()
                else:
                    header_lines.append(ln)
        i += 1

    header = {"name": name, "lines": header_lines, "email": email, "bullets": header_bullets}

    sections = []
    current = None
    acc = []

    def flush():
        nonlocal current, acc
        if current is None:
            acc = []
            return
        current["raw"] = "\n".join(acc).strip("\n")
        sections.append(current)
        current = None
        acc = []

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("## "):
            flush()
            current = {"title": ln[3:].strip()}
            acc = []
        else:
            if current is not None:
                acc.append(ln)
        i += 1
    flush()

    out_sections = []
    for sec in sections:
        title = sec["title"]
        raw = sec.get("raw", "")

        if title.lower() == "links":
            links = []
            for m in re.finditer(r"^\s*-\s*([^:]+?)\s*:\s*(https?://\S+)\s*$", raw, re.M):
                links.append({"label": m.group(1).strip(), "url": m.group(2).strip()})
            out_sections.append({"title": "Links", "links": links, "body": raw})
            continue

        if title.lower() == "work experience":
            jobs = []
            parts = re.split(r"^\s*###\s+", raw, flags=re.M)
            for p in parts[1:]:
                plines = p.splitlines()
                if not plines:
                    continue
                job_title = plines[0].strip()
                rest = "\n".join(plines[1:]).strip("\n")

                mco = re.search(r"^\s*\*\*(.+?)\*\*\s*$", rest, re.M)
                company = mco.group(1).strip() if mco else ""

                # simplistic location/dates extraction
                location, dates = "", ""
                rlines = [l.strip() for l in rest.splitlines()]
                # find company line index
                start = 0
                for k,l in enumerate(rlines):
                    if re.match(r"^\*\*.+\*\*$", l):
                        start = k + 1
                        break
                next_lines = []
                for k in range(start, len(rlines)):
                    t = rlines[k]
                    if not t:
                        continue
                    if re.match(r"^\*\*.+\*\*:\s*$", t):
                        break
                    if " is " in t and len(t) > 40 and t.endswith("."):
                        break
                    next_lines.append(t)
                    if len(next_lines) >= 2:
                        break
                if len(next_lines) >= 1:
                    location = next_lines[0]
                if len(next_lines) >= 2:
                    dates = next_lines[1]

                company_desc = ""
                mdesc = re.search(r"^\s*([A-Z][^\n]{20,})\s*$", rest, re.M)
                if mdesc and " is " in mdesc.group(1):
                    company_desc = mdesc.group(1).strip()

                groups = []
                for gm in re.finditer(r"^\s*\*\*([^*]+?)\*\*:\s*$", rest, re.M):
                    gtitle = gm.group(1).strip()
                    gs = gm.end()
                    nextm = re.search(r"^\s*\*\*[^*]+?\*\*:\s*$", rest[gs:], re.M)
                    block = rest[gs: gs+nextm.start()] if nextm else rest[gs:]
                    items = [m.group(1).strip() for m in re.finditer(r"^\s*-\s+(.*)\s*$", block, re.M)]
                    groups.append({"title": gtitle, "items": items})

                jobs.append({
                    "title": job_title,
                    "company": company,
                    "location": location,
                    "dates": dates,
                    "companyDescription": company_desc,
                    "groups": groups
                })

            out_sections.append({"title":"Work Experience", "jobs": jobs, "body": raw})
            continue

        out_sections.append({"title": title, "body": raw})

    return {"header": header, "sections": out_sections}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--template", type=Path, default=Path("resume_template_configurable_v3.html"))
    ap.add_argument("--config", type=Path, default=Path("resume.config.json"))
    args = ap.parse_args()

    md = args.markdown.read_text(encoding="utf-8")
    model = parse_markdown_resume(md)
    cfg = json.loads(args.config.read_text(encoding="utf-8")) if args.config.exists() else {}
    payload = {"model": model, "config": cfg}

    tpl = args.template.read_text(encoding="utf-8")
    name = model["header"].get("name") or "Resume"
    html = tpl.replace("__NAME__", name).replace("__JSON__", json.dumps(payload, ensure_ascii=False))
    args.output.write_text(html, encoding="utf-8")
    print(f"Wrote {args.output}")

if __name__ == "__main__":
    main()
