#!/usr/bin/env python3
"""Overview for the coordinator: which classes have work, without reading any class material.

  status.py ROOT [CLASS ...]

A class is a folder of ROOT that contains a res/ folder (or the input folder recorded in its
state). For each class it prints one line: files that are new, changed or removed since the
last run (by SHA-256 only, nothing is prepared or written), sources prepared but not finished,
open findings, uncommitted changes in the class folder, and whether the book exists.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ inside the skill folder
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C


def class_status(cdir: Path) -> dict:
    state = C.load_state(cdir)
    rdir = C.resources_dir(cdir, state)
    sources = state["sources"]
    known = {e["sha256"] for e in sources.values()}
    new = changed = 0
    current, unknown_hashes = set(), set()
    for p in C.list_resources(rdir):
        rel = p.relative_to(rdir).as_posix()
        current.add(rel)
        e = sources.get(rel)
        h = C.sha256(p)
        if e is None:
            unknown_hashes.add(h)
            if h not in known:             # a rename is not new work
                new += 1
        elif e["sha256"] != h:
            changed += 1
    removed = sum(1 for rel, e in sources.items()
                  if rel not in current and e["sha256"] not in unknown_hashes)
    pending = sum(1 for rel, e in sources.items() if rel in current and e.get("status") == "pending")
    findings = C.work_dir(cdir) / "findings.md"
    open_findings = findings.read_text().count("· open ·") if findings.exists() else 0
    dirty = ""
    try:
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "."], cwd=cdir,
                               capture_output=True, text=True).stdout.strip()
    except OSError:
        pass
    return {"new": new, "changed": changed, "removed": removed, "pending": pending,
            "open": open_findings, "dirty": bool(dirty),
            "book": (C.book_dir(cdir) / "book.toml").exists()}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("classes", nargs="*")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if args.classes:
        dirs = [root / c for c in args.classes]
        for d in dirs:
            if not d.is_dir():
                C.die(f"{d} is not a folder")
    else:
        dirs = sorted(d for d in root.iterdir()
                      if d.is_dir() and not d.name.startswith(".")
                      and ((d / "res").is_dir() or (d / "_work" / "state.json").exists()))
    if not dirs:
        print("no class folders (a class folder contains res/)")
        return
    for d in dirs:
        s = class_status(d)
        work = s["new"] + s["changed"] + s["removed"] + s["pending"]
        parts = [f"{k} {s[k]}" for k in ("new", "changed", "removed", "pending") if s[k]]
        if s["open"]:
            parts.append(f"{s['open']} open finding(s)")
        if s["dirty"]:
            parts.append("uncommitted changes")
        if not s["book"]:
            parts.append("no book yet")
        verdict = "WORK " if work else "ok   "
        print(f"{verdict} {d.name:<16} " + (", ".join(parts) if parts else "current"))


if __name__ == "__main__":
    main()
