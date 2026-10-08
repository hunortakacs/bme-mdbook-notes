#!/usr/bin/env python3
"""Step 1 of a run: find new and changed sources and prepare them for reading.

  prepare.py CLASS_DIR [--resources NAME] [--force] [--view-all] [--only SLUG ...]

For every file in the class's resources folder it compares the SHA-256 with
_work/state.json and reports NEW / CHANGED / RENAMED / REMOVED / PENDING.
New and changed sources are prepared in _work/sources/<slug>/:

  pdf, office   draft.md + extract.json + pages/*.png + figures/*.png (pdf_triage.py)
  notebook      draft.md with the cells flattened, image outputs in figures/
  image         one unit that has to be looked at
  text          nothing: the file is read as it is

transcript.md is created from draft.md. When a source changed, sections of the
old transcript are carried over for every unit whose content is unchanged, so
only new and changed units need work. _work/coverage.tsv gets one row per unit.

Nothing is marked as done here; check.py --finalize does that.
"""
from __future__ import annotations

import argparse
import base64
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ inside the skill folder
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C


def flatten_notebook(src: Path, out: Path) -> dict:
    nb = json.loads(src.read_text(encoding="utf-8"))
    meta = nb.get("metadata", {})
    lang = (meta.get("kernelspec", {}).get("language") or meta.get("language_info", {}).get("name") or "text").lower()
    out.mkdir(parents=True, exist_ok=True)
    figdir = out / "figures"
    if figdir.exists():
        shutil.rmtree(figdir)
    body, figures = [], []
    for i, cell in enumerate(nb.get("cells", []), 1):
        source = "".join(cell.get("source", [])) if isinstance(cell.get("source"), list) else cell.get("source", "")
        if cell.get("cell_type") == "markdown":
            body += [source.strip(), ""]
            continue
        if cell.get("cell_type") != "code" or not source.strip():
            continue
        body += [f"<!-- cell {i} -->", f"```{lang}", source.rstrip(), "```", ""]
        for k, o in enumerate(cell.get("outputs", []), 1):
            text = None
            if o.get("output_type") == "stream":
                text = "".join(o.get("text", []))
            elif o.get("output_type") == "error":
                text = f"{o.get('ename', 'Error')}: {o.get('evalue', '')}"
            else:
                data = o.get("data", {})
                for mime in ("image/png", "image/jpeg"):
                    if mime in data:
                        figdir.mkdir(exist_ok=True)
                        name = f"figures/cell{i:03d}-{k}.{'png' if mime.endswith('png') else 'jpg'}"
                        raw = data[mime] if isinstance(data[mime], str) else "".join(data[mime])
                        (out / name).write_bytes(base64.b64decode(raw))
                        figures.append({"file": name})
                        body += [f"<!-- figure: {name} (output of cell {i}) -->", ""]
                if "text/plain" in data and not any(m in data for m in ("image/png", "image/jpeg")):
                    t = data["text/plain"]
                    text = t if isinstance(t, str) else "".join(t)
            if text and text.strip():
                lines = text.rstrip().splitlines()
                if len(lines) > 40:
                    lines = lines[:40] + [f"... ({len(lines) - 40} more lines)"]
                body += ["Output:", "```text", *lines, "```", ""]
    text = "\n".join(body).strip()
    unit = {"id": "all", "page": 1, "pages": [1, 1], "label": "", "title": src.name,
            "flags": ["image"] if figures else [], "view": "figures/" if figures else None,
            "figures": figures, "links": [], "annots": [], "header": [], "text": text,
            "fingerprint": C.sha256(src)[:16]}
    return {"meta": {"source": src.name, "kind": "notebook", "units": 1,
                     "needs_view": 1 if figures else 0, "flags": {"image": 1} if figures else {}},
            "units": [unit]}


def image_source(src: Path, out: Path) -> dict:
    (out / "pages").mkdir(parents=True, exist_ok=True)
    view = f"pages/{src.name}"
    shutil.copyfile(src, out / view)
    unit = {"id": "all", "page": 1, "pages": [1, 1], "label": "", "title": src.name, "flags": ["image"],
            "view": view, "figures": [{"file": view}], "links": [], "annots": [], "header": [], "text": "",
            "fingerprint": C.sha256(src)[:16]}
    return {"meta": {"source": src.name, "kind": "image", "units": 1, "needs_view": 1, "flags": {"image": 1}},
            "units": [unit]}


def office_to_pdf(src: Path, out: Path) -> Path | None:
    exe = shutil.which("soffice") or shutil.which("libreoffice")
    if not exe:
        return None
    out.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run([exe, "--headless", "--convert-to", "pdf", "--outdir", str(out), str(src)],
                       check=True, capture_output=True, timeout=300)
    except (subprocess.SubprocessError, OSError):
        return None
    pdf = out / (src.stem + ".pdf")
    if not pdf.exists():
        return None
    target = out / "converted.pdf"
    pdf.replace(target)
    return target


def prepare_source(src: Path, kind: str, out: Path, view_all: bool) -> dict | None:
    """Returns the extract dict, or None for sources that need no preparation."""
    import pdf_triage as T
    if kind == "text":
        return None
    if kind == "notebook":
        data = flatten_notebook(src, out)
    elif kind == "image":
        data = image_source(src, out)
    else:
        pdf = src
        if kind == "office":
            pdf = office_to_pdf(src, out)
            if pdf is None:
                raise RuntimeError("could not convert with LibreOffice (is `soffice` installed?); "
                                   "export the file to PDF and put the PDF in the resources folder")
        meta, units = T.triage(pdf, out, view_all=view_all)
        meta["source"] = src.name
        data = {"meta": meta, "units": units}
        (out / "extract.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
        (out / "draft.md").write_text(T.draft_markdown(meta, units))
        return data
    (out / "extract.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
    (out / "draft.md").write_text(T.draft_markdown(
        {**data["meta"], "physical_pages": 1, "grouping": "-"}, data["units"]))
    return data


def build_transcript(out: Path, data: dict, old: dict | None, view_all: bool = False):
    """Write transcript.md; reuse old sections whose unit content did not change.

    Returns (id map old->new, changed/new unit ids, removed old unit ids)."""
    import pdf_triage as T
    meta = {**data["meta"]}
    meta.setdefault("physical_pages", 1)
    meta.setdefault("grouping", "-")
    head = T.draft_markdown(meta, [])
    tfile = out / "transcript.md"
    if old is None or not tfile.exists():
        tfile.write_text(T.draft_markdown(meta, data["units"]))
        return {}, [u["id"] for u in data["units"]], []
    old_units = {u["id"]: u for u in C.parse_units(tfile.read_text())}
    shutil.copyfile(tfile, out / "transcript.prev.md")
    by_fp = {}
    for u in old["units"]:
        by_fp.setdefault(u["fingerprint"], u["id"])
    idmap, changed, blocks, used = {}, [], [], set()
    for u in data["units"]:
        oid = by_fp.get(u["fingerprint"])
        prev = old_units.get(oid) if oid else None
        reusable = prev is not None and oid not in used and not (prev["status"] or "TODO").startswith("TODO")
        if reusable and view_all and prev["status"] == "auto":
            reusable = False                     # --view-all: every unit gets looked at
        if reusable:
            used.add(oid)
            idmap[oid] = u["id"]
            blocks.append("\n".join([T.unit_header(u)] + prev["lines"][1:]).rstrip() + "\n")
        else:
            if oid and oid not in used:
                used.add(oid)
                idmap[oid] = u["id"]
            if prev is None or (prev["status"] or "TODO").startswith("TODO") or not view_all:
                changed.append(u["id"])
            blocks.append(T.unit_block(u))
    removed = [u["id"] for u in old["units"] if u["id"] not in idmap]
    tfile.write_text(head + "\n".join(blocks))
    return idmap, changed, removed


def mark_duplicates(wdir: Path, sources: dict, fresh_slugs: set[str], coverage: list[dict]) -> list[str]:
    """Mark units of freshly prepared PDFs whose pages all appear in another source.

    Such units get the status `duplicate of <file> <unit>` (nothing to view) and the
    coverage disposition `cut: duplicate of <file> <unit>`. The original is the source
    that is already done, else the one grouped by page labels, else the first by name."""
    extracts = {}
    for rel, e in sources.items():
        f = wdir / "sources" / e["slug"] / "extract.json"
        if e["kind"] in ("pdf", "office") and f.exists():
            data = json.loads(f.read_text())
            if data["meta"].get("page_hashes"):
                extracts[rel] = data
    rank = sorted(extracts, key=lambda rel: (sources[rel].get("status") != "done",
                                             extracts[rel]["meta"].get("grouping") != "labels", rel))
    seen: dict[str, tuple[str, str]] = {}       # page hash -> (original file, unit id)
    report = []
    for rel in rank:
        e, data = sources[rel], extracts[rel]
        hashes = data["meta"]["page_hashes"]
        dup = {}
        if e["slug"] in fresh_slugs:
            for u in data["units"]:
                hits = [seen.get(hashes[i - 1]) for i in range(u["pages"][0], u["pages"][1] + 1)]
                if hits and all(hits):
                    dup[u["id"]] = hits[-1]
        for u in data["units"]:
            for i in range(u["pages"][0], u["pages"][1] + 1):
                seen.setdefault(hashes[i - 1], (rel, u["id"]))
        if not dup:
            continue
        tfile = wdir / "sources" / e["slug"] / "transcript.md"
        lines = tfile.read_text().splitlines()
        cur = None
        for k, line in enumerate(lines):
            m = C.UNIT_HEADER.match(line)
            if m:
                cur = m.group(1)
            elif cur in dup and C.STATUS_LINE.match(line) and line.startswith("<!-- status: TODO"):
                lines[k] = f"<!-- status: duplicate of {dup[cur][0]} {dup[cur][1]} -->"
        tfile.write_text("\n".join(lines) + "\n")
        for r in coverage:
            if r["source"] == e["slug"] and r["unit"] in dup and not r["disposition"].strip():
                orig = dup[r["unit"]]
                r["disposition"] = f"cut: duplicate of {orig[0]} {orig[1]}"
        others = sorted({o for o, _ in dup.values()})
        report.append(f"DUPLICATE {rel}: {len(dup)} of {len(data['units'])} units have every page in "
                      f"{', '.join(others)}; they are marked and need no viewing")
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("class_dir")
    ap.add_argument("--resources", help="name of the resources folder inside the class folder")
    ap.add_argument("--force", action="store_true", help="prepare every source again")
    ap.add_argument("--view-all", action="store_true", help="render every PDF page for viewing")
    ap.add_argument("--only", nargs="+", metavar="SLUG", help="limit --force to these sources")
    args = ap.parse_args()

    cdir = C.class_dir(args.class_dir)
    state = C.load_state(cdir)
    rdir = C.resources_dir(cdir, state, args.resources)
    wdir = C.work_dir(cdir)
    sources = state["sources"]
    coverage = C.load_coverage(cdir)

    current = {}
    for p in C.list_resources(rdir):
        current[p.relative_to(rdir).as_posix()] = p
    hashes = {rel: C.sha256(p) for rel, p in current.items()}

    report, todo = [], []
    # renamed: a missing path whose hash shows up under a new path
    missing = [rel for rel in sources if rel not in current]
    for rel in list(current):
        if rel in sources:
            continue
        for old in missing:
            if old in sources and sources[old]["sha256"] == hashes[rel]:
                sources[rel] = sources.pop(old)
                missing.remove(old)
                report.append(f"RENAMED   {old} -> {rel}")
                break
    for old in missing:
        e = sources.pop(old)
        rows = [r for r in coverage if r["source"] == e["slug"]]
        used = sorted({c for r in rows for c in C.chapters_of(r["disposition"])})
        coverage = [r for r in coverage if r["source"] != e["slug"]]
        sdir = wdir / "sources" / e["slug"]
        if sdir.exists():
            (wdir / "removed").mkdir(exist_ok=True)
            target = wdir / "removed" / e["slug"]
            if target.exists():
                shutil.rmtree(target)
            sdir.replace(target)
        report.append(f"REMOVED   {old} (its content was used in: {', '.join(used) or 'no chapter'}). "
                      f"Ask the user whether those parts should stay in the book.")

    slugs = {e["slug"] for e in sources.values()}
    unchanged = 0
    for rel, path in current.items():
        e = sources.get(rel)
        kind = C.classify(path)
        if e is None:
            slug = base = C.slugify(Path(rel).stem)
            if slug in slugs:
                slug = base = C.slugify(Path(rel).stem + "-" + path.suffix)
            n = 2
            while slug in slugs:
                slug = f"{base}-{n}"
                n += 1
            slugs.add(slug)
            e = sources[rel] = {"slug": slug, "sha256": None, "kind": kind, "status": "pending", "units": 0}
            what = "NEW"
        elif e["sha256"] != hashes[rel]:
            what = "CHANGED"
        elif args.force and e["kind"] != "unsupported" and (not args.only or e["slug"] in args.only):
            what = "FORCED"
        elif e.get("status") != "done" and e["kind"] != "unsupported":
            what = "PENDING"
        else:
            if e["kind"] == "unsupported":
                report.append(f"SKIPPED   {rel} (unsupported file type; tell the user)")
            else:
                unchanged += 1
            continue
        e["kind"] = kind
        if kind == "unsupported":
            e.update(sha256=hashes[rel], status="skipped", units=0)
            report.append(f"SKIPPED   {rel} (unsupported file type; tell the user)")
            continue
        todo.append((what, rel, path, e))

    for what, rel, path, e in todo:
        out = wdir / "sources" / e["slug"]
        kind = e["kind"]
        fresh = what in ("NEW", "CHANGED", "FORCED") or (kind != "text" and not (out / "extract.json").exists())
        info = ""
        if kind == "text":
            units = [{"id": "all", "title": path.name}]
            idmap, changed, removed = {"all": "all"}, [], []
            e["units"] = 1
        else:
            old = None
            if (out / "extract.json").exists():
                old = json.loads((out / "extract.json").read_text())
            if fresh:
                try:
                    data = prepare_source(path, kind, out, args.view_all)
                except Exception as exc:                       # keep going with the other sources
                    report.append(f"FAILED    {rel}: {exc}")
                    e["status"] = "failed"
                    continue
                idmap, changed, removed = build_transcript(out, data, old, args.view_all)
            else:
                data = old
                idmap = {u["id"]: u["id"] for u in data["units"]}
                changed, removed = [], []
            units = data["units"]
            e["units"] = len(units)
            m = data["meta"]
            todo_n = sum(1 for u in C.parse_units((out / "transcript.md").read_text())
                         if (u["status"] or "").startswith("TODO"))
            flags = ", ".join(f"{k} {v}" for k, v in sorted(m.get("flags", {}).items())) or "none"
            pages = f"{m['physical_pages']} pages -> " if "physical_pages" in m else ""
            info = f"{pages}{len(units)} units, {todo_n} to view (flags: {flags})"
            if m.get("grouping") == "heuristic" and m.get("physical_pages", 0) != len(units):
                info += "; animation steps were merged by content, spot-check a few"
        # coverage rows for this source
        old_rows = {r["unit"]: r for r in coverage if r["source"] == e["slug"]}
        back = {new: old_id for old_id, new in idmap.items()}
        new_rows = []
        for u in units:
            prev = old_rows.get(back.get(u["id"]))
            disp = prev["disposition"] if prev else ""
            new_rows.append({"source": e["slug"], "unit": u["id"], "title": u.get("title") or "", "disposition": disp})
        lost = [(uid, old_rows[uid]["disposition"]) for uid in removed if uid in old_rows and old_rows[uid]["disposition"]]
        coverage = [r for r in coverage if r["source"] != e["slug"]] + new_rows
        e["sha256"] = hashes[rel]
        e["status"] = "pending"
        line = f"{what:<9} {rel}  [{e['slug']}, {kind}]"
        if info:
            line += f"\n          {info}"
        if what in ("CHANGED", "FORCED") and (kind == "text" or changed or removed or what == "CHANGED"):
            if kind == "text":
                line += "\n          text file changed: reread it and update the chapters that use it"
            else:
                line += f"\n          new or changed units: {', '.join(changed) or 'none'}"
                if removed:
                    line += f"\n          units no longer in the source: {', '.join(removed)}"
                for uid, disp in lost:
                    line += f"\n          removed unit {uid} was used in: {disp}"
        report.append(line)

    fresh_slugs = {e["slug"] for what, _, _, e in todo if e.get("status") == "pending"}
    report += mark_duplicates(wdir, sources, fresh_slugs, coverage)

    order = {e["slug"]: i for i, e in enumerate(sources.values())}
    coverage.sort(key=lambda r: (order.get(r["source"], 1e9), C.unit_sort_key(r["unit"])))
    C.save_coverage(cdir, coverage)
    C.save_state(cdir, state)

    gi = wdir / ".gitignore"
    if not gi.exists():
        gi.write_text("# rendered pages and crops can be regenerated with prepare.py --force\n"
                      "sources/*/pages/\nsources/*/figures/\nsources/*/converted.pdf\nsources/*/*.prev.*\nremoved/\n")

    pending = sum(1 for e in sources.values() if e.get("status") == "pending")
    unassigned = sum(1 for r in coverage if not r["disposition"].strip())
    print(f"class: {cdir.name}   resources: {rdir.name}/   sources: {len(current)}")
    for line in report:
        print(line)
    print(f"unchanged and done: {unchanged}   pending: {pending}   coverage rows without a chapter: {unassigned}")
    if not pending:
        print("Nothing to do: the book is up to date with the resources.")
    (wdir / "prepare-report.txt").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
