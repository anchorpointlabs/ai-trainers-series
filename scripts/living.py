#!/usr/bin/env python3
"""Living-layer tools for the APL AI Trainer's Series library.

Run from the repo root. Stdlib only. Preserves CRLF line endings.

  python scripts/living.py extract OUT.jsonl          dump every 'What is current' section
  python scripts/living.py apply IN.jsonl             write rewritten sections back (adds the pointer line)
  python scripts/living.py stamp YYYY-MM-DD [ID ...]  set as_at / review_by (+91 days), re-date the heading
  python scripts/living.py scan OUT.jsonl             dated/product mentions OUTSIDE the section
  python scripts/living.py check                      gate: PASS n/n or FAIL with reasons (exit 1)
  python scripts/living.py stale [YYYY-MM-DD]         entries past review_by + register rows older than 35 days
"""
import csv
import datetime as dt
import glob
import json
import os
import re
import sys

# Lookahead, not consume: the match must end BEFORE the \r so a CRLF file is never left with \r\r\n.
HEAD_RE = re.compile(r"^### What is current as of ([A-Z][a-z]+ \d{4})[ \t]*(?=\r?$)", re.M)
NEXT_RE = re.compile(r"^#{2,3} ", re.M)
FM_RE = re.compile(r"\A---\r?\n(.*?\r?\n)---\r?\n", re.S)
POINTER = ("Current models, versions and prices live in the "
           "[Living Register](../concepts/living/register.csv), checked monthly. "
           "This section covers only what changed for this topic.")
# The generic frontier line-up that was pasted into ~180 sections. None of it may survive in a section.
LINEUP_RE = re.compile(r"GPT-6|Claude 5\.5|Gemini 3\.1|Gemini 4|Argon", re.I)
DATED_RE = re.compile(r"November 2026|late 2026|[Ii]n 2026|[Aa]s of [A-Z][a-z]+ 2026|\$\d|per million tokens")
PRODUCT_RE = re.compile(r"\b(?:GPT-\d[\w.]*|Claude \d[\w.]*|Gemini \d[\w.]*|Llama ?\d[\w.]*|Grok ?\d[\w.]*|Qwen[\w.]*|DeepSeek[- ]?V?\d[\w.]*)")
REGISTER = os.path.join("concepts", "living", "register.csv")
REGISTER_COLS = ["vendor", "product", "model_or_version", "status", "key_facts", "source_url", "checked"]
REVIEW_DAYS = 91
REGISTER_MAX_AGE = 35


def entries():
    return sorted(p for p in glob.glob(os.path.join("TSC-*", "*.md"))
                  if os.path.basename(p) != "README.md")


def read(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def write(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def eol(t):
    return "\r\n" if "\r\n" in t else "\n"


def fm_get(t, key):
    m = FM_RE.match(t)
    if not m:
        return None
    km = re.search(r"^%s:[ \t]*(.*?)[ \t]*\r?$" % re.escape(key), m.group(1), re.M)
    return km.group(1) if km else None


def fm_set(t, key, value):
    m = FM_RE.match(t)
    body, nl = m.group(1), eol(t)
    line_re = re.compile(r"^%s:.*?\r?$" % re.escape(key), re.M)
    if line_re.search(body):
        body = line_re.sub("%s: %s" % (key, value), body, count=1)
    else:
        body = body + "%s: %s%s" % (key, value, nl)
    return t[:m.start(1)] + body + t[m.end(1):]


def span(t):
    """(heading_start, body_start, body_end) of the 'What is current' section, or None."""
    heads = list(HEAD_RE.finditer(t))
    if len(heads) != 1:
        return None
    h = heads[0]
    n = NEXT_RE.search(t, h.end())
    return h.start(), h.end(), (n.start() if n else len(t))


def clean(s):
    return s.replace("\r", "").strip()


def cmd_extract(out):
    n = 0
    with open(out, "w", encoding="utf-8") as f:
        for p in entries():
            t = read(p)
            sp = span(t)
            if not sp:
                print("SKIP (no single section):", p)
                continue
            f.write(json.dumps({"id": fm_get(t, "id"), "path": p.replace("\\", "/"),
                                "title": fm_get(t, "title"),
                                "section": clean(t[sp[1]:sp[2]])}, ensure_ascii=False) + "\n")
            n += 1
    print("extracted", n, "sections ->", out)


def cmd_apply(src):
    by_id = {fm_get(read(p), "id"): p for p in entries()}
    done = 0
    with open(src, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            p = by_id.get(r["id"])
            new = clean(r.get("new_section", ""))
            if not p or not new:
                print("REJECT", r.get("id"), "(unknown id or empty new_section)")
                continue
            new = clean(new.replace(POINTER, ""))
            t = read(p)
            nl = eol(t)
            sp = span(t)
            body = (new + "\n\n" + POINTER).replace("\n", nl)
            t = t[:sp[1]] + nl + nl + body + nl + nl + t[sp[2]:]
            write(p, t)
            done += 1
    print("applied", done, "sections")


def cmd_stamp(date, ids):
    d = dt.date.fromisoformat(date)
    review = d + dt.timedelta(days=REVIEW_DAYS)
    month = d.strftime("%B %Y")
    n = 0
    for p in entries():
        t = read(p)
        if ids and fm_get(t, "id") not in ids:
            continue
        t = fm_set(t, "as_at", d.isoformat())
        t = fm_set(t, "review_by", review.isoformat())
        t = HEAD_RE.sub(lambda m: m.group(0).replace(m.group(1), month), t, count=1)
        write(p, t)
        n += 1
    print("stamped", n, "entries as_at", d, "review_by", review)


def cmd_scan(out):
    n = 0
    with open(out, "w", encoding="utf-8") as f:
        for p in entries():
            t = read(p)
            sp = span(t)
            fm = FM_RE.match(t)
            skip_to = fm.end() if fm else 0
            pos = 0
            for i, line in enumerate(t.split("\n"), 1):
                start, pos = pos, pos + len(line) + 1
                if start < skip_to or (sp and sp[0] <= start < sp[2]):
                    continue
                hits = DATED_RE.findall(line) + PRODUCT_RE.findall(line)
                if hits:
                    f.write(json.dumps({"id": fm_get(t, "id"), "path": p.replace("\\", "/"), "line_no": i,
                                        "text": line.strip(), "hits": hits}, ensure_ascii=False) + "\n")
                    n += 1
    print("found", n, "lines with dated/product mentions outside the section ->", out)


def register_rows():
    if not os.path.exists(REGISTER):
        return None
    with open(REGISTER, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def cmd_check():
    fails = []
    files = entries()
    for p in files:
        t = read(p)
        sp = span(t)
        why = []
        if not sp:
            why.append("needs exactly one 'What is current as of' heading")
        else:
            sec = t[sp[1]:sp[2]]
            if POINTER not in sec:
                why.append("pointer line missing")
            if LINEUP_RE.search(sec):
                why.append("frontier line-up still named: " + ", ".join(sorted(set(LINEUP_RE.findall(sec)))))
        for k in ("as_at", "review_by"):
            v = fm_get(t, k)
            try:
                dt.date.fromisoformat(v or "")
            except ValueError:
                why.append("frontmatter %s missing or not YYYY-MM-DD" % k)
        if "\r\r" in t or ("\r\n" in t and t.count("\n") != t.count("\r\n")):
            why.append("mixed line endings")
        if why:
            fails.append((p, why))
    rows = register_rows()
    reg_fail = []
    if rows is None:
        reg_fail.append("register missing: " + REGISTER)
    else:
        if not rows:
            reg_fail.append("register has no rows")
        for i, r in enumerate(rows, 2):
            if list(r.keys()) != REGISTER_COLS:
                reg_fail.append("register header must be: " + ",".join(REGISTER_COLS))
                break
            if not (r["source_url"] or "").startswith("http"):
                reg_fail.append("row %d (%s): source_url must be a vendor URL" % (i, r["product"]))
            if r["status"] not in ("current", "deprecated"):
                reg_fail.append("row %d (%s): status must be current|deprecated" % (i, r["product"]))
            try:
                dt.date.fromisoformat(r["checked"])
            except ValueError:
                reg_fail.append("row %d (%s): checked must be YYYY-MM-DD" % (i, r["product"]))
    for p, why in fails:
        print("FAIL", p.replace("\\", "/"), "|", "; ".join(why))
    for w in reg_fail:
        print("FAIL", w)
    ok = len(files) - len(fails)
    if fails or reg_fail:
        print("FAIL %d/%d entries pass; register problems: %d" % (ok, len(files), len(reg_fail)))
        sys.exit(1)
    print("PASS %d/%d entries; register %d rows" % (ok, len(files), len(rows)))


def cmd_stale(date=None):
    d = dt.date.fromisoformat(date) if date else dt.date.today()
    due = []
    for p in entries():
        t = read(p)
        rb = fm_get(t, "review_by")
        if rb and dt.date.fromisoformat(rb) < d:
            due.append((rb, fm_get(t, "id"), p.replace("\\", "/")))
    for rb, i, p in sorted(due):
        print("ENTRY due", rb, i, p)
    old = []
    for r in register_rows() or []:
        try:
            if (d - dt.date.fromisoformat(r["checked"])).days > REGISTER_MAX_AGE:
                old.append(r)
        except ValueError:
            old.append(r)
    for r in old:
        print("REGISTER row older than %d days:" % REGISTER_MAX_AGE, r["checked"], r["vendor"], r["product"])
    print("as of", d, "-", len(due), "entries due,", len(old), "register rows stale")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(2)
    c = a[0]
    if c == "extract":
        cmd_extract(a[1])
    elif c == "apply":
        cmd_apply(a[1])
    elif c == "stamp":
        cmd_stamp(a[1], set(a[2:]))
    elif c == "scan":
        cmd_scan(a[1])
    elif c == "check":
        cmd_check()
    elif c == "stale":
        cmd_stale(a[1] if len(a) > 1 else None)
    else:
        print(__doc__)
        sys.exit(2)
