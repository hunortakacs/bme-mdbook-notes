#!/usr/bin/env python3
"""Last step of a run: verify that nothing was lost and that the book builds.

  check.py CLASS_DIR [--no-build] [--finalize] [--all]

  1 sources      every file in res/ was prepared and has not changed since
  2 transcripts  every unit is present and none is still marked TODO
  3 coverage     every unit points to a chapter or carries a reason for the cut
  4 book         SUMMARY and files agree; code blocks have a language and are
                 not empty; links and images resolve; chapters name their sources
  5 content      (warnings) code lines and formulas of a unit that do not appear in its chapter
  6 build        mdbook build; formula errors; languages without highlighting

FAIL lines must be fixed. WARN lines must be read and either fixed or judged
to be fine. --finalize marks the pending sources as done, only when nothing failed.
--all prints every item of a list instead of the first 20.
Exit code: 0 ok, 1 failures.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import statistics
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ inside the skill folder
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C
from cover import compress

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
IMG = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|<img[^>]+src=[\"']([^\"']+)[\"']")
MARKERS = re.compile(r"\b(TODO|FIXME|XXX)\b|<!--\s*(status|flags|figure):")
PROMPT = re.compile(r"^(iex(\(\d+\))?>|\.\.\.(\(\d+\))?>|>>>|\.\.\.|\$|>|In \[\d*\]:|\?-|\|\s*\?-)\s*")


class Report:
    def __init__(self):
        self.fails = 0
        self.warns = 0

    def section(self, name):
        print(f"\n== {name}")

    def ok(self, msg):
        print(f"  ok    {msg}")

    def fail(self, msg, items=()):
        self.fails += 1
        print(f"  FAIL  {msg}")
        self._items(items)

    def warn(self, msg, items=()):
        self.warns += 1
        print(f"  WARN  {msg}")
        self._items(items)

    cap = 20

    def _items(self, items):
        items = list(items)
        shown = items if self.cap is None else items[:self.cap]
        for it in shown:
            print(f"          {it}")
        if len(items) > len(shown):
            print(f"          ... and {len(items) - len(shown)} more (--all shows them)")


def split_code(text: str):
    """Returns (prose lines with numbers, code blocks [{line, lang, body}], problems)."""
    prose, blocks, problems = [], [], []
    cur = None
    for no, line in enumerate(text.splitlines(), 1):
        m = FENCE.match(line)
        if cur is None:
            if m:
                cur = {"line": no, "mark": m.group(2), "lang": m.group(3).strip(), "body": []}
            else:
                prose.append((no, line))
        else:
            if m and m.group(2)[0] == cur["mark"][0] and len(m.group(2)) >= len(cur["mark"]) and not m.group(3).strip():
                blocks.append(cur)
                cur = None
            else:
                cur["body"].append(line)
    if cur is not None:
        problems.append(f"line {cur['line']}: code block is never closed")
        blocks.append(cur)
    return prose, blocks, problems


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s)


def code_norm(s: str) -> str:
    """norm(), plus the output details that differ between language versions only:
    Elixir charlists 'abc' / ~c"abc", and the numbers in #Function<...>."""
    s = norm(s)
    s = re.sub(r'~c"((?:[^"\\]|\\.)*)"', r"'\1'", s)
    return re.sub(r"#Function<[^>]*>", "#Function<>", s)


def code_lines(lines: list[str]) -> list[str]:
    out, inside = [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        if inside:
            t = PROMPT.sub("", line.strip())
            if len(norm(t)) >= 10:
                out.append(t)
    return out


MATH = re.compile(r"\$\$(.+?)\$\$|(?<![\\$])\$(?!\s)([^$\n]+?)(?<![\s\\])\$", re.S)


def formulas(lines: list[str]) -> list[str]:
    """LaTeX formulas ($...$ and $$...$$) outside code fences and inline code."""
    prose, inside = [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        if not inside and not line.startswith("<!--"):
            prose.append(re.sub(r"`[^`]*`", "", line))
    return [(a or b).strip() for a, b in MATH.findall("\n".join(prose)) if (a or b).strip()]


def math_norm(f: str) -> str:
    """Spacing, sizing and roman-font spellings do not change a formula."""
    f = re.sub(r"\\(displaystyle|textstyle|left|right|big|Big|bigg|Bigg)(?![a-zA-Z])", "", f)
    f = re.sub(r"\\(mathrm|operatorname|textrm)\{([^{}]*)\}", r"\2", f)
    f = re.sub(r"\\[,;:! ]|\\quad|\\qquad|~", "", f)
    return re.sub(r"\s+", "", f).rstrip(".,;")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("class_dir")
    ap.add_argument("--no-build", action="store_true")
    ap.add_argument("--finalize", action="store_true")
    ap.add_argument("--all", action="store_true", help="print every item of a list")
    args = ap.parse_args()

    cdir = C.class_dir(args.class_dir)
    state = C.load_state(cdir)
    wdir, bdir = C.work_dir(cdir), C.book_dir(cdir)
    src = bdir / "src"
    R = Report()
    if args.all:
        R.cap = None
    sources = state["sources"]
    by_slug = {e["slug"]: (rel, e) for rel, e in sources.items()}

    # ---------------------------------------------------------------- 1 sources
    R.section("1 sources")
    rdir = C.resources_dir(cdir, state)
    current = {p.relative_to(rdir).as_posix(): p for p in C.list_resources(rdir)}
    stale = [rel for rel in current if rel not in sources]
    changed = [rel for rel, p in current.items() if rel in sources and sources[rel]["sha256"] != C.sha256(p)]
    gone = [rel for rel in sources if rel not in current]
    failed = [rel for rel, e in sources.items() if e.get("status") == "failed"]
    skipped = [rel for rel, e in sources.items() if e.get("kind") == "unsupported"]
    if stale or changed or gone:
        R.fail(f"{rdir.name}/ changed since prepare.py ran; run prepare.py again",
               [f"new: {r}" for r in stale] + [f"changed: {r}" for r in changed] + [f"removed: {r}" for r in gone])
    if failed:
        R.fail("sources that could not be prepared", failed)
    if skipped:
        R.warn("unsupported files are not in the book (the user has to know)", skipped)
    if not (stale or changed or gone or failed):
        R.ok(f"{len(current)} files, all prepared")

    # ------------------------------------------------------------ 2 transcripts
    R.section("2 transcripts")
    transcripts = {}
    bad = False
    for rel, e in sources.items():
        if e["kind"] in ("text", "unsupported") or e.get("status") == "failed":
            continue
        sdir = wdir / "sources" / e["slug"]
        if not (sdir / "extract.json").exists() or not (sdir / "transcript.md").exists():
            R.fail(f"{e['slug']}: extract.json or transcript.md is missing; run prepare.py --force")
            bad = True
            continue
        want = [u["id"] for u in json.loads((sdir / "extract.json").read_text())["units"]]
        units = C.parse_units((sdir / "transcript.md").read_text())
        transcripts[e["slug"]] = units
        have = [u["id"] for u in units]
        if have != want:
            lost = [u for u in want if u not in have]
            extra = [u for u in have if u not in want]
            R.fail(f"{e['slug']}: transcript units differ from the source"
                   + (f"; missing {compress(lost, want)}" if lost else "")
                   + (f"; unknown {', '.join(extra)}" if extra else "")
                   + ("" if lost or extra else "; order changed"))
            bad = True
        todo = [u["id"] for u in units if (u["status"] or "TODO").startswith("TODO")]
        if todo:
            R.fail(f"{e['slug']}: {len(todo)} unit(s) not looked at yet: {compress(todo, have)}")
            bad = True
        empty = [u["id"] for u in units if not (u["status"] or "").startswith("TODO")
                 and not any(l.strip() and not l.startswith("<!--") for l in u["lines"][1:])]
        if empty:
            R.warn(f"{e['slug']}: units with an empty transcript (fine only for blank or purely decorative slides): "
                   f"{compress(empty, have)}")
    if not bad:
        R.ok(f"{len(transcripts)} transcripts complete")

    # --------------------------------------------------------------- 3 coverage
    R.section("3 coverage")
    rows = C.load_coverage(cdir)
    chapters = C.summary_files(cdir)
    by_source: dict[str, list[dict]] = {}
    for r in rows:
        by_source.setdefault(r["source"], []).append(r)
    bad = False
    chapter_units: dict[str, list[tuple[str, str]]] = {}
    for rel, e in sources.items():
        if e["kind"] == "unsupported" or e.get("status") == "failed":
            continue
        rs = by_source.get(e["slug"], [])
        ids = [r["unit"] for r in rs]
        want = None
        if e["slug"] in transcripts:
            want = [u["id"] for u in transcripts[e["slug"]]]
        elif e["kind"] == "text" and rel in current:
            want = [u["id"] for u in C.text_units(current[rel], e)]
        if want is not None:
            lost = [u for u in want if u not in ids]
            if lost:
                R.fail(f"{e['slug']}: units without a coverage row: {compress(lost, want)}; run prepare.py")
                bad = True
        elif not rs:
            R.fail(f"{e['slug']}: no coverage row; run prepare.py")
            bad = True
        missing = [r["unit"] for r in rs if not r["disposition"].strip()]
        if missing:
            R.fail(f"{e['slug']}: {len(missing)} unit(s) have no chapter and no cut reason: {compress(missing, ids)}")
            bad = True
        for r in rs:
            d = r["disposition"].strip()
            if d.lower().startswith("cut") and not d.partition(":")[2].strip():
                R.fail(f"{e['slug']} {r['unit']}: cut without a reason")
                bad = True
            if C.partial_cut(d) == "":
                R.fail(f"{e['slug']} {r['unit']}: after ';' only `cut: <what was left out>` may follow")
                bad = True
            for c in C.chapters_of(d):
                chapter_units.setdefault(c, []).append((e["slug"], r["unit"]))
                if c not in chapters:
                    R.fail(f"{e['slug']} {r['unit']}: points to {c}, which is not in SUMMARY.md")
                    bad = True
    if not bad:
        cut = sum(1 for r in rows if r["disposition"].lower().startswith("cut"))
        part = sum(1 for r in rows if C.partial_cut(r["disposition"]))
        R.ok(f"{len(rows)} units: {len(rows) - cut} in chapters ({part} of them partly cut), {cut} cut with a reason")

    # ------------------------------------------------------------------- 4 book
    R.section("4 book")
    known = json.loads((ASSETS / "theme" / "highlight-languages.json").read_text())
    known_langs = set(known) | {a for v in known.values() for a in v} | {"mermaid", "text", "txt", "plain"}
    chapter_text = {}
    if not (src / "SUMMARY.md").exists():
        R.fail("book/src/SUMMARY.md does not exist; run new_book.py")
    else:
        problems, unknown_langs = [], {}
        on_disk = {p.relative_to(src).as_posix() for p in src.rglob("*.md")
                   if p.name != "SUMMARY.md" and not any(part.startswith("_") for part in p.relative_to(src).parts)}
        for c in chapters:
            if not (src / c).exists():
                problems.append(f"SUMMARY.md lists {c}, which does not exist")
        for c in sorted(on_disk - set(chapters)):
            problems.append(f"{c} is not listed in SUMMARY.md")
        for c in chapters:
            f = src / c
            if not f.exists():
                continue
            text = f.read_text()
            chapter_text[c] = text
            prose, blocks, probs = split_code(text)
            problems += [f"{c}: {p}" for p in probs]
            h1 = [no for no, line in prose if line.startswith("# ")]
            if not h1 or h1[0] > 3:
                problems.append(f"{c}: does not start with a '# ' title")
            if len(h1) > 1:
                problems.append(f"{c}: more than one '# ' title (lines {', '.join(map(str, h1))})")
            for b in blocks:
                lang = b["lang"].split(",")[0].split()[0] if b["lang"] else ""
                if not lang:
                    problems.append(f"{c}: line {b['line']}: code block without a language")
                elif lang not in known_langs:
                    unknown_langs.setdefault(lang, []).append(f"{c}:{b['line']}")
                if not any(l.strip() for l in b["body"]):
                    problems.append(f"{c}: line {b['line']}: empty code block")
            for no, line in prose:
                m = MARKERS.search(line)
                if m:
                    problems.append(f"{c}: line {no}: leftover marker '{m.group(0)}'")
                for a, b2 in IMG.findall(line):
                    target = (a or b2).split("#")[0]
                    if target and not re.match(r"^[a-z]+:", target) and not (f.parent / target).exists():
                        problems.append(f"{c}: line {no}: image {target} does not exist")
                for target in C.LINK.findall(re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)):
                    target = target.split("#")[0]
                    if target.endswith(".md") and not (f.parent / target).exists():
                        problems.append(f"{c}: line {no}: link to {target}, which does not exist")
            dollars = len(re.findall(r"(?<!\\)\$\$", "\n".join(l for _, l in prose)))
            if dollars % 2:
                problems.append(f"{c}: odd number of $$ (a display formula is not closed)")
            for slug in sorted({s for s, _ in chapter_units.get(c, [])}):
                name = Path(by_slug[slug][0]).name
                if name not in text:
                    problems.append(f"{c}: uses {slug} but does not name its source file {name}")
        if problems:
            R.fail(f"{len(problems)} problem(s) in the book", problems)
        else:
            R.ok(f"{len(chapters)} chapters, structure and code blocks fine")
        if unknown_langs:
            R.warn("code block languages the highlighter does not know (use a known name or `text`)",
                   [f"{k}: {', '.join(v[:4])}" for k, v in unknown_langs.items()])
        unused = [c for c in chapters if c not in chapter_units and c in chapter_text
                  and len(chapter_text[c].split()) > 120]
        if unused and rows:
            R.warn("chapters that no source unit points to (written without a source?)", unused)

    # ---------------------------------------------------------------- 5 content
    R.section("5 content (warnings to read)")
    # code of text sources is checked too: fenced blocks of Markdown-like files, every line of code files
    units_of = dict(transcripts)
    for rel, e in sources.items():
        if e["kind"] == "text" and rel in current:
            units_of[e["slug"]] = []
            for tu in C.text_units(current[rel], e):
                text = "\n".join(tu["lines"])
                if any(l.lstrip().startswith("```") for l in tu["lines"]):
                    # untagged fences hold outputs and prose (Livebook); only tagged ones are code
                    _, blocks, _ = split_code(text)
                    code = [l for b in blocks if b["lang"] and b["lang"] not in ("text", "output")
                            for l in ["```"] + b["body"] + ["```"]]
                elif current[rel].suffix.lower() in C.MARKDOWN_EXT:
                    code = []
                else:
                    code = ["```"] + tu["lines"] + ["```"]
                units_of[e["slug"]].append({"id": tu["id"], "lines": [""] + code})
    reviewed = set(state.get("reviewed_lines", []))
    notes, lost_keys, hidden = [], [], 0
    for slug, units in units_of.items():
        disp = {r["unit"]: r["disposition"] for r in by_source.get(slug, [])}
        for u in units:
            targets = [c for c in C.chapters_of(disp.get(u["id"], "")) if c in chapter_text]
            if not targets:
                continue
            hay = code_norm("\n".join(PROMPT.sub("", l.strip()) for c in targets for l in chapter_text[c].splitlines()))
            lines = code_lines(u["lines"])
            lost = []
            for l in lines:
                if code_norm(l) in hay:
                    continue
                key = hashlib.sha1(f"{slug}\t{u['id']}\t{norm(l)}".encode()).hexdigest()[:12]
                lost_keys.append(key)
                if key in reviewed:
                    hidden += 1
                else:
                    lost.append(l)
            if lost:
                pc = C.partial_cut(disp.get(u["id"], ""))
                notes.append(f"{slug} {u['id']} -> {', '.join(targets)}: {len(lost)} of {len(lines)} code lines not found"
                             + (f" (partly cut: {pc})" if pc else ""))
                notes += [f"    {l[:110]}" for l in lost[:4]]
            src_f = [f for f in formulas(u["lines"]) if len(math_norm(f)) >= 3]
            if src_f:
                book_math = "\n".join(math_norm(f) for c in targets for f in formulas(chapter_text[c].splitlines()))
                missing_f = []
                for f in src_f:
                    if math_norm(f) in book_math:
                        continue
                    key = hashlib.sha1(f"{slug}\t{u['id']}\tf:{math_norm(f)}".encode()).hexdigest()[:12]
                    lost_keys.append(key)
                    if key in reviewed:
                        hidden += 1
                    else:
                        missing_f.append(f)
                if missing_f:
                    notes.append(f"{slug} {u['id']} -> {', '.join(targets)}: {len(missing_f)} of {len(src_f)} "
                                 f"formulas not found (compare them symbol by symbol)")
                    notes += [f"    ${f[:110]}$" for f in missing_f[:4]]
    if notes:
        R.warn("content of a unit that was not found in its chapter. Corrected or rewritten code is fine; "
               "a dropped example is not", notes)
    else:
        R.ok("all code lines and formulas of the sources appear in their chapters")
    if hidden:
        print(f"          ({hidden} line(s) reviewed in an earlier run are not shown)")

    # ------------------------------------------------------------------ 6 build
    R.section("6 build")
    if args.no_build:
        print("  skipped")
    elif not (bdir / "book.toml").exists():
        R.fail("book/book.toml does not exist; run new_book.py")
    elif not shutil.which("mdbook"):
        R.fail("mdbook is not installed; run doctor.py")
    else:
        weights = {}
        for c, text in chapter_text.items():
            key = re.sub(r"(^|/)README\.md$", r"\1index.html", c)
            key = re.sub(r"\.md$", ".html", key)
            weights[key] = max(1, len(text.split()))
        if weights:
            weights["__default"] = int(statistics.median(weights.values()))
        (bdir / "theme").mkdir(exist_ok=True)
        (bdir / "theme" / "jegyzet-weights.js").write_text(
            "// generated by check.py: words per chapter, for the progress bar\n"
            "window.JEGYZET_WEIGHTS = " + json.dumps(weights, ensure_ascii=False, sort_keys=True) + ";\n")
        p = subprocess.run(["mdbook", "build", str(bdir)], capture_output=True, text=True)
        output = re.sub(r"\x1b\[[0-9;]*m", "", p.stdout + p.stderr).splitlines()
        # preprocessors built against an older mdBook patch release say so on every build
        log = [l for l in output if re.search(r"\b(ERROR|WARN|Warning|error)\b", l)
               and not re.search(r"was built against (version|mdbook v)", l)]
        if p.returncode != 0:
            R.fail("mdbook build failed", output[-25:])
        else:
            if log:
                R.warn("mdbook build messages", log)
            out = bdir / "book"
            errors, raw = [], []
            for f in sorted(out.rglob("*.html")):
                if f.name in ("print.html", "toc.html", "404.html"):
                    continue
                t = f.read_text(errors="replace")
                for m in re.finditer(r'class="katex-error"[^>]*title="([^"]*)"', t):
                    errors.append(f"{f.relative_to(out)}: {html.unescape(m.group(1))[:160]}")
                main = t.split("<main>", 1)[-1].split("</main>", 1)[0]
                main = re.sub(r"<pre.*?</pre>|<code.*?</code>|<span class=\"katex.*?</span></span></span>", "", main, flags=re.S)
                if re.search(r"\$\$|\\begin\{(align|equation|pmatrix|cases)", main):
                    raw.append(str(f.relative_to(out)))
            if errors:
                R.fail(f"{len(errors)} formula(s) KaTeX could not render", errors)
            if raw:
                R.warn("pages that still show raw LaTeX (unclosed $$ or math inside HTML?)", raw)
            if not errors and not log:
                R.ok(f"book built: {out / 'index.html'}")

    # ----------------------------------------------------------------- finalize
    print(f"\n{R.fails} failure(s), {R.warns} warning(s)")
    if args.finalize:
        if R.fails:
            print("not finalized: fix the failures first")
        else:
            n = 0
            for e in sources.values():
                if e.get("status") == "pending":
                    e["status"] = "done"
                    n += 1
            # the section 5 lines that are missing now were read and judged; later runs hide them
            state["reviewed_lines"] = sorted(set(lost_keys))
            C.save_state(cdir, state)
            print(f"finalized: {n} source(s) marked as done")
    sys.exit(1 if R.fails else 0)


if __name__ == "__main__":
    main()
