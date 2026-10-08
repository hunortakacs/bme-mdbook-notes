#!/usr/bin/env python3
"""A compact map of a class's book, generated from the chapters themselves, for planning.

  bookmap.py CLASS_DIR [--chapter FILE ...]

For every chapter in SUMMARY order: file, title, size in words, its section headings
(## and ###), the terms it defines (bold text), the languages of its code blocks, whether it has
exercises, and the source units that feed it (from coverage.tsv). Nothing is summarised by hand,
so the map cannot go stale: it is regenerated whenever it is read. It shows where new material
belongs; the chapters chosen with it are then read in full.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ inside the skill folder
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C
from cover import compress

FENCE = re.compile(r"^\s*(`{3,}|~{3,})\s*([\w+-]*)")
BOLD = re.compile(r"\*\*([^*\n]{2,60}?)\*\*")


def chapter_map(text: str) -> dict:
    title, heads, terms, langs, in_fence = "", [], [], {}, False
    prose = []
    for line in text.splitlines():
        m = FENCE.match(line)
        if m:
            if not in_fence and m.group(2):
                langs[m.group(2)] = langs.get(m.group(2), 0) + 1
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        elif line.startswith("## "):
            heads.append(line[3:].strip())
        elif line.startswith("### "):
            heads.append("  " + line[4:].strip())
        prose.append(line)
        for t in BOLD.findall(line):
            t = t.strip(" .:,`")
            if t and t not in terms:
                terms.append(t)
    words = len(re.sub(r"<[^>]+>", " ", "\n".join(prose)).split())
    exercises = any(re.search(r"feladat|exercise|megoldás", h, re.I) for h in heads) or "<details>" in text
    return {"title": title, "heads": heads, "terms": terms, "langs": langs, "words": words,
            "exercises": exercises}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("class_dir")
    ap.add_argument("--chapter", nargs="+", metavar="FILE", help="only these chapters")
    args = ap.parse_args()
    cdir = C.class_dir(args.class_dir)
    src = C.book_dir(cdir) / "src"
    files = C.summary_files(cdir)
    if not files:
        C.die("the book has no SUMMARY.md yet")
    if args.chapter:
        files = [f for f in files if f in args.chapter]
    rows = C.load_coverage(cdir)
    by_source: dict[str, list[dict]] = {}
    for r in rows:
        by_source.setdefault(r["source"], []).append(r)
    total = 0
    for f in files:
        p = src / f
        if not p.exists():
            print(f"{f}: (missing file)\n")
            continue
        m = chapter_map(p.read_text())
        total += m["words"]
        depth = f.count("/")
        print(f"{'  ' * depth}{f} · {m['title']} · {m['words']} words"
              + (" · exercises" if m["exercises"] else ""))
        ind = "  " * depth + "    "
        if m["heads"]:
            print(f"{ind}sections: " + " | ".join(h.strip() if not h.startswith("  ") else "› " + h.strip()
                                                    for h in m["heads"]))
        if m["terms"]:
            print(f"{ind}terms: " + ", ".join(m["terms"]))
        if m["langs"]:
            print(f"{ind}code: " + ", ".join(f"{k} {v}" for k, v in sorted(m["langs"].items())))
        feeds = []
        for slug, rs in by_source.items():
            mine = [r["unit"] for r in rs if f in C.chapters_of(r["disposition"])]
            if mine:
                feeds.append(f"{slug} {compress(mine, [r['unit'] for r in rs])}")
        if feeds:
            print(f"{ind}sources: " + "; ".join(feeds))
        print()
    print(f"{len(files)} chapter(s), {total} words")


if __name__ == "__main__":
    main()
