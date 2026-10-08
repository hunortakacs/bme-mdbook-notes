#!/usr/bin/env python3
"""Record where every unit of every source ends up (_work/coverage.tsv).

  cover.py CLASS_DIR show [SLUG] [--missing]
  cover.py CLASS_DIR set SLUG UNITS DISPOSITION
  cover.py CLASS_DIR set-many FILE         # one "SLUG<TAB>UNITS<TAB>DISPOSITION" per line; - reads stdin
  cover.py CLASS_DIR chapter FILE          # which units feed this chapter
  cover.py CLASS_DIR changed               # chapters added or changed since the last commit
  cover.py CLASS_DIR excerpt FILE [--pending] [-o OUT]
                                           # the source text of the units that feed this chapter;
                                           # --pending: only units of sources not yet finalized

UNITS        all | s3 | s3-s9 | s1,s4-s6,s12   (s4 and ranges also cover variants such as s4.1, s4.2)
DISPOSITION  one or more chapter files relative to book/src, comma separated
             (types/lists.md  or  intro.md,types/atoms.md), or
             "cut: <reason>" for content that is deliberately left out, or
             "types/lists.md; cut: <what>" when the unit is used but part of it is left out
             (a setup cell, raw tool output, an aside).

Every unit needs a disposition before check.py passes. "cut" needs a reason:
admin, duplicate of <unit>, table of contents, installation, link list, ...
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ inside the skill folder
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C


def expand(spec: str, units: list[str]) -> list[str]:
    if spec.strip() == "all":
        return list(units)
    chosen = []
    pos = {u: i for i, u in enumerate(units)}

    def span_of(token):
        """A bare sN stands for all of its variants."""
        if token in pos:
            return pos[token], pos[token]
        idx = [i for i, u in enumerate(units) if u.split(".")[0] == token]
        if not idx:
            C.die(f"unknown unit {token}")
        return idx[0], idx[-1]

    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            lo, _ = span_of(a.strip())
            _, hi = span_of(b.strip())
            if hi < lo:
                C.die(f"range {part} runs backwards")
            chosen += units[lo:hi + 1]
        else:
            lo, hi = span_of(part)
            chosen += units[lo:hi + 1]
    return list(dict.fromkeys(chosen))


def compress(units: list[str], all_units: list[str]) -> str:
    """s1,s2,s3,s7 -> s1-s3,s7 (for display)."""
    pos = {u: i for i, u in enumerate(all_units)}
    idx = sorted(pos[u] for u in units if u in pos)
    out, i = [], 0
    while i < len(idx):
        j = i
        while j + 1 < len(idx) and idx[j + 1] == idx[j] + 1:
            j += 1
        out.append(all_units[idx[i]] if i == j else f"{all_units[idx[i]]}-{all_units[idx[j]]}")
        i = j + 1
    return ",".join(out)


def assign(cdir, by_source, slug, units, disposition) -> str:
    if slug not in by_source:
        C.die(f"unknown source {slug}; known: {', '.join(by_source)}")
    disp = disposition.strip()
    if disp.lower().startswith("cut"):
        reason = disp.partition(":")[2].strip()
        if not reason:
            C.die('a cut needs a reason: "cut: admin"')
        disp = f"cut: {reason}"
    else:
        if ";" in disp:
            reason = C.partial_cut(disp)
            if not reason:
                C.die('after ";" write "cut: <what was left out>": "lists.md; cut: setup cell"')
            disp = f"{','.join(C.chapters_of(disp))}; cut: {reason}"
        src = C.book_dir(cdir) / "src"
        for c in C.chapters_of(disp):
            if not c.endswith(".md"):
                C.die(f"{c} is not a chapter file (paths are relative to book/src and end in .md)")
            if src.exists() and not (src / c).exists():
                print(f"note: {c} does not exist yet")
    ids = [r["unit"] for r in by_source[slug]]
    chosen = set(expand(units, ids))
    for r in by_source[slug]:
        if r["unit"] in chosen:
            r["disposition"] = disp
    return f"{slug}: {len(chosen)} unit(s) -> {disp}"


BOOKKEEPING = __import__("re").compile(r"^<!--\s*(status|flags|figure|header):")


def excerpt(cdir: Path, by_source: dict, chapter: str, pending: bool = False) -> str:
    """Every unit mapped to CHAPTER, in source order: the transcript section of a slide or
    notebook unit, the section of a text source. Partial cuts are noted above the unit."""
    state = C.load_state(cdir)
    by_slug = {e["slug"]: (rel, e) for rel, e in state["sources"].items()}
    rdir = C.resources_dir(cdir, state)
    out = [f"# Sources of {chapter}", ""]
    for slug, rs in by_source.items():
        mine = {r["unit"]: r for r in rs if chapter in C.chapters_of(r["disposition"])}
        if not mine or slug not in by_slug:
            continue
        rel, e = by_slug[slug]
        if pending and e.get("status") == "done":
            continue
        transcript = C.work_dir(cdir) / "sources" / slug / "transcript.md"
        if transcript.exists():
            units = {u["id"]: u["lines"][1:] for u in C.parse_units(transcript.read_text())}
            titles = {u["id"]: u["title"] for u in C.parse_units(transcript.read_text())}
        else:
            tus = C.text_units(rdir / rel, e)
            units = {u["id"]: u["lines"] for u in tus}
            titles = {u["id"]: u["title"] for u in tus}
        for uid in sorted(mine, key=C.unit_sort_key):
            out.append(f"## {rel} {uid} · {titles.get(uid, '')}")
            disp = mine[uid]["disposition"]
            others = [c for c in C.chapters_of(disp) if c != chapter]
            if others:
                out.append(f"(this unit also feeds: {', '.join(others)}; its content may be there instead)")
            cut = C.partial_cut(disp)
            if cut:
                out.append(f"(partly cut on purpose: {cut})")
            body = units.get(uid)
            if body is None:
                body = ["(unit not found in the source)"]
            out += [l for l in body if not BOOKKEEPING.match(l)]
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("class_dir")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sh = sub.add_parser("show")
    sh.add_argument("slug", nargs="?")
    sh.add_argument("--missing", action="store_true")
    st = sub.add_parser("set")
    st.add_argument("slug")
    st.add_argument("units")
    st.add_argument("disposition")
    sm = sub.add_parser("set-many")
    sm.add_argument("file")
    ch = sub.add_parser("chapter")
    ch.add_argument("file")
    sub.add_parser("changed")
    ex = sub.add_parser("excerpt")
    ex.add_argument("file")
    ex.add_argument("--pending", action="store_true", help="only units of sources that are not finalized yet")
    ex.add_argument("-o", "--out")
    args = ap.parse_args()

    cdir = C.class_dir(args.class_dir)
    rows = C.load_coverage(cdir)
    by_source: dict[str, list[dict]] = {}
    for r in rows:
        by_source.setdefault(r["source"], []).append(r)

    if args.cmd == "set":
        msg = assign(cdir, by_source, args.slug, args.units, args.disposition)
        C.save_coverage(cdir, rows)
        print(msg)
        return

    if args.cmd == "set-many":
        text = sys.stdin.read() if args.file == "-" else Path(args.file).read_text()
        msgs = []
        for no, line in enumerate(text.splitlines(), 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 3:
                C.die(f"line {no}: expected SLUG<TAB>UNITS<TAB>DISPOSITION: {line}")
            msgs.append(assign(cdir, by_source, *(p.strip() for p in parts)))
        C.save_coverage(cdir, rows)                    # only after every line was valid
        print("\n".join(msgs))
        return

    if args.cmd == "changed":
        src = C.book_dir(cdir) / "src"
        try:
            out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--", "."],
                                 cwd=src, capture_output=True, text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            C.die("not a git repository (or git is missing): cannot tell what changed")
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=src,
                             capture_output=True, text=True).stdout.strip()
        found = False
        for line in out.splitlines():
            code, path = line[:2], line[3:].split(" -> ")[-1]
            f = (Path(top) / path).resolve()
            if f.suffix != ".md" or f.name == "SUMMARY.md":
                continue
            rel = f.relative_to(src.resolve()).as_posix()
            what = "NEW" if "?" in code or "A" in code else ("REMOVED" if "D" in code else "CHANGED")
            title = ""
            if f.exists():
                title = next((l[2:].strip() for l in f.read_text().splitlines() if l.startswith("# ")), "")
            feeds = [f"{slug} {compress([r['unit'] for r in rs if rel in C.chapters_of(r['disposition'])], [r['unit'] for r in rs])}"
                     for slug, rs in by_source.items() if any(rel in C.chapters_of(r["disposition"]) for r in rs)]
            print(f"{what:<8} {rel:<36} {title}" + (f"   <- {'; '.join(feeds)}" if feeds else ""))
            found = True
        if not found:
            print("no chapter changed since the last commit")
        return

    if args.cmd == "excerpt":
        text = excerpt(cdir, by_source, args.file, args.pending)
        if args.out:
            Path(args.out).write_text(text)
            print(f"{args.out}: {len(text.splitlines())} lines")
        else:
            sys.stdout.write(text)
        return

    if args.cmd == "chapter":
        hit = False
        for slug, rs in by_source.items():
            ids = [r["unit"] for r in rs]
            mine = [r["unit"] for r in rs if args.file in C.chapters_of(r["disposition"])]
            if mine:
                hit = True
                print(f"{slug}: {compress(mine, ids)}")
        if not hit:
            print("no unit is mapped to this chapter")
        return

    total = missing = 0
    for slug, rs in by_source.items():
        if args.slug and slug != args.slug:
            continue
        ids = [r["unit"] for r in rs]
        groups: dict[str, list[str]] = {}
        for r in rs:
            groups.setdefault(r["disposition"].strip() or "(unassigned)", []).append(r["unit"])
        total += len(rs)
        missing += len(groups.get("(unassigned)", []))
        if args.missing and "(unassigned)" not in groups:
            continue
        print(f"{slug}  ({len(rs)} units)")
        for disp, us in groups.items():
            if args.missing and disp != "(unassigned)":
                continue
            print(f"  {compress(us, ids):<28} {disp}")
    print(f"{total - missing} of {total} units assigned" + (f", {missing} missing" if missing else ""))


if __name__ == "__main__":
    main()
