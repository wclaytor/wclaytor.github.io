#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

md = Path(sys.argv[1]).read_text()
out = Path(sys.argv[2])

lines = md.splitlines()
name = lines[0][2:]
i = 1
header_lines=[]; bullets=[]; email=""
while i<len(lines) and not lines[i].startswith("## "):
    l=lines[i].strip()
    if l.startswith("- "): bullets.append(l[2:])
    elif "@" in l: email=l
    elif l: header_lines.append(l)
    i+=1

sections=[]
cur=None; acc=[]
def flush():
    global cur, acc
    if cur:
        cur["body"]="\n".join(acc)
        sections.append(cur)
    cur=None; acc=[]
while i<len(lines):
    if lines[i].startswith("## "):
        flush()
        cur={"title":lines[i][3:]}
    else:
        acc.append(lines[i])
    i+=1
flush()

model={"header":{"name":name,"lines":header_lines,"email":email,"bullets":bullets},"sections":sections}
html = Path("resume_template_configurable_v4.html").read_text()
html = html.replace("__NAME__", name).replace("__JSON__", json.dumps({"model":model,"config":{}}))
out.write_text(html)
