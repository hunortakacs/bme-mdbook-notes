"""Shared helpers: folder layout, state file, coverage table, transcript parsing."""
from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

WORK = "_work"
BOOK = "book"
RESOURCE_NAMES = ("resources", "forrasok", "források", "forras", "anyag", "anyagok", "materials", "sources")
IGNORED_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
OFFICE_EXT = {".pptx", ".ppt", ".odp", ".docx", ".doc", ".odt", ".rtf", ".key"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff"}
ARCHIVE_EXT = {".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar"}
UNIT_HEADER = re.compile(r"^## (s\d+(?:\.\d+)?|all) · (.*)$")
STATUS_LINE = re.compile(r"^<!-- status: (.*?) -->\s*$")


def die(msg: str):
    sys.exit(f"error: {msg}")


def class_dir(arg: str) -> Path:
    p = Path(arg).resolve()
    if not p.is_dir():
        die(f"{arg} is not a folder")
    return p


def work_dir(cdir: Path) -> Path:
    return cdir / WORK


def book_dir(cdir: Path) -> Path:
    return cdir / BOOK


def load_state(cdir: Path) -> dict:
    f = work_dir(cdir) / "state.json"
    if f.exists():
        return json.loads(f.read_text())
    return {"version": 1, "resources": None, "sources": {}}


def save_state(cdir: Path, state: dict):
    work_dir(cdir).mkdir(parents=True, exist_ok=True)
    (work_dir(cdir) / "state.json").write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def resources_dir(cdir: Path, state: dict, override: str | None = None) -> Path:
    if override:
        state["resources"] = override
    if state.get("resources"):
        r = cdir / state["resources"]
        if not r.is_dir():
            die(f"resources folder {r} does not exist")
        return r
    for name in RESOURCE_NAMES:
        if (cdir / name).is_dir():
            state["resources"] = name
            return cdir / name
    die(f"no resources folder in {cdir} (expected one of: {', '.join(RESOURCE_NAMES)}; "
        f"or pass --resources NAME)")


def list_resources(rdir: Path) -> list[Path]:
    out = []
    for p in sorted(rdir.rglob("*")):
        if not p.is_file() or p.name in IGNORED_NAMES:
            continue
        if any(part.startswith(".") for part in p.relative_to(rdir).parts):
            continue
        if p.name.endswith("~") or p.name.startswith("~$"):
            continue
        out.append(p)
    return out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "source"


def classify(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return "pdf"
    if ext == ".ipynb":
        return "notebook"
    if ext in OFFICE_EXT:
        return "office"
    if ext in IMAGE_EXT:
        return "image"
    if ext in ARCHIVE_EXT:
        return "unsupported"
    try:
        data = path.read_bytes()[:200_000]
    except OSError:
        return "unsupported"
    if b"\x00" in data:
        return "unsupported"
    try:
        data.decode("utf-8")
        return "text"
    except UnicodeDecodeError:
        try:
            data[:-4].decode("utf-8")       # the cut may have split a character
            return "text"
        except UnicodeDecodeError:
            pass
    try:
        data.decode("cp1250")
        return "text"
    except UnicodeDecodeError:
        return "unsupported"


# ---------------------------------------------------------------- transcripts

def parse_units(text: str) -> list[dict]:
    """Split a draft/transcript into units. Returns [{id, title, status, lines}]."""
    units, cur, in_fence = [], None, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else UNIT_HEADER.match(line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2), "status": None, "lines": [line]}
            units.append(cur)
            continue
        if cur is None:
            continue
        if cur["status"] is None and not in_fence:
            s = STATUS_LINE.match(line)
            if s:
                cur["status"] = s.group(1).strip()
        cur["lines"].append(line)
    return units


def transcript_head(text: str) -> str:
    out = []
    for line in text.splitlines():
        if UNIT_HEADER.match(line):
            break
        out.append(line)
    return "\n".join(out).rstrip() + "\n\n"


# ------------------------------------------------------------------- coverage

COVERAGE_COLUMNS = ["source", "unit", "title", "disposition"]


def load_coverage(cdir: Path) -> list[dict]:
    f = work_dir(cdir) / "coverage.tsv"
    rows = []
    if f.exists():
        for i, line in enumerate(f.read_text().splitlines()):
            if i == 0 or not line.strip():
                continue
            parts = line.split("\t")
            parts += [""] * (4 - len(parts))
            rows.append(dict(zip(COVERAGE_COLUMNS, parts[:4])))
    return rows


def save_coverage(cdir: Path, rows: list[dict]):
    lines = ["\t".join(COVERAGE_COLUMNS)]
    for r in rows:
        lines.append("\t".join((r.get(c) or "").replace("\t", " ").replace("\n", " ") for c in COVERAGE_COLUMNS))
    work_dir(cdir).mkdir(parents=True, exist_ok=True)
    (work_dir(cdir) / "coverage.tsv").write_text("\n".join(lines) + "\n")


def unit_sort_key(uid: str):
    if uid == "all":
        return (0, 0)
    a, _, b = uid[1:].partition(".")
    return (int(a), int(b or 0))


def chapters_of(disposition: str) -> list[str]:
    d = disposition.strip()
    if not d or d.lower().startswith("cut"):
        return []
    return [c.strip() for c in d.split(",") if c.strip()]


# ----------------------------------------------------------------------- book

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def summary_files(cdir: Path) -> list[str]:
    """Chapter files in SUMMARY.md order (paths relative to book/src)."""
    f = book_dir(cdir) / "src" / "SUMMARY.md"
    if not f.exists():
        return []
    out = []
    for line in f.read_text().splitlines():
        for target in LINK.findall(line):
            target = target.split("#")[0]
            if target.endswith(".md") and target not in out:
                out.append(target)
    return out
