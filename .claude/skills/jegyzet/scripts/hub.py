#!/usr/bin/env python3
"""One entry point for all class books: an mdBook that lists them, and a server for all of it.

  hub.py ROOT build                       # build the hub page and every class book once
  hub.py ROOT serve [--host H] [--port P] # serve / (the hub) and /<class>/ (each book);
                                          # rebuilds a book when its sources change
  hub.py ROOT install-service [--port P]  # run `serve` as a systemd user service

ROOT is the repository with one folder per class (ROOT/<class>/book/book.toml).
The hub is generated in ROOT/.hub (not in git); each class book is built into
its own <class>/book/book, the same place check.py builds it.
"""
from __future__ import annotations

import argparse
import functools
import html
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ inside the skill folder

ASSETS = Path(__file__).resolve().parent.parent / "assets"
HUB = ".hub"
TITLE = "Jegyzetek"


def log(msg: str):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def mdbook() -> str:
    exe = shutil.which("mdbook") or str(Path.home() / ".cargo" / "bin" / "mdbook")
    if not Path(exe).exists():
        sys.exit("error: mdbook not found (cargo install mdbook --locked; ~/.cargo/bin on PATH)")
    return exe


def classes(root: Path) -> list[str]:
    return sorted(p.parent.parent.name for p in root.glob("*/book/book.toml")
                  if not p.parent.parent.name.startswith((".", "_")))


def book_title(cdir: Path) -> str:
    m = re.search(r'(?m)^title\s*=\s*"((?:[^"\\]|\\.)*)"', (cdir / "book" / "book.toml").read_text())
    return m.group(1).replace('\\"', '"') if m else cdir.name


def class_info(cdir: Path) -> dict:
    summary = cdir / "book" / "src" / "SUMMARY.md"
    chapters = len(re.findall(r"(?m)^\s*- \[", summary.read_text())) if summary.exists() else 0
    state = cdir / "_work" / "state.json"
    sources = pending = 0
    if state.exists():
        st = json.loads(state.read_text()).get("sources", {})
        sources = sum(1 for e in st.values() if e.get("kind") != "unsupported")
        pending = sum(1 for e in st.values() if e.get("status") == "pending")
    try:
        when = subprocess.run(["git", "log", "-1", "--format=%cs", "--", "book"], cwd=cdir,
                              capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        when = ""
    if not when:
        when = time.strftime("%Y-%m-%d", time.localtime(signature(cdir)[0] or time.time()))
    return {"name": cdir.name, "title": book_title(cdir), "chapters": chapters,
            "sources": sources, "pending": pending, "updated": when}


def signature(cdir: Path) -> tuple[float, int]:
    """Changes when anything the book is built from changes."""
    bdir = cdir / "book"
    files = [bdir / "book.toml"]
    for sub in ("src", "theme"):
        if (bdir / sub).exists():
            files += [p for p in (bdir / sub).rglob("*") if p.is_file()]
    files += [p for p in bdir.glob("*.js")]
    mt = max((p.stat().st_mtime for p in files if p.exists()), default=0.0)
    return mt, len(files)


HUB_CSS = """
/* The hub is a single page: no sidebar. */
#mdbook-sidebar, #mdbook-sidebar-toggle, #mdbook-sidebar-resize-handle { display: none !important; }
#mdbook-sidebar-toggle-anchor:checked ~ .page-wrapper { transform: none !important; margin-inline-start: 0 !important; }
main table { margin-inline: 0; }
"""


def hub_markdown(infos: list[dict]) -> str:
    lines = [f"# {TITLE}", ""]
    if not infos:
        lines += ["Még nincs jegyzet. Egy tárgy könyvét a `/jegyzet <tárgy>` paranccsal lehet elkészíteni, "
                  "ha a tárgy mappájában van `resources/` mappa.", ""]
        return "\n".join(lines)
    lines += ["| Tárgy | Fejezetek | Források | Frissítve |", "|---|---:|---:|---|"]
    for i in infos:
        note = " (frissítés folyamatban)" if i["pending"] else ""
        lines.append(f"| [{i['title']}](/{i['name']}/){note} | {i['chapters']} | {i['sources']} | {i['updated']} |")
    return "\n".join(lines) + "\n"


def write_hub(root: Path, infos: list[dict]) -> bool:
    """Write the hub's mdBook sources. Returns True when something changed."""
    hub = root / HUB
    (hub / "src").mkdir(parents=True, exist_ok=True)
    (hub / "theme").mkdir(exist_ok=True)
    files = {
        hub / "book.toml": (f'[book]\ntitle = "{TITLE}"\nlanguage = "hu"\nsrc = "src"\n\n'
                            '[output.html]\ndefault-theme = "light"\npreferred-dark-theme = "navy"\n'
                            'additional-css = ["theme/jegyzet.css"]\n\n'
                            '[output.html.search]\nenable = false\n\n[output.html.print]\nenable = false\n'),
        hub / "src" / "SUMMARY.md": f"# Summary\n\n[{TITLE}](index.md)\n",
        hub / "src" / "index.md": hub_markdown(infos),
        hub / "theme" / "jegyzet.css": (ASSETS / "theme" / "jegyzet.css").read_text() + HUB_CSS,
    }
    changed = False
    for f, text in files.items():
        if not f.exists() or f.read_text() != text:
            f.write_text(text)
            changed = True
    return changed or not (hub / "book" / "index.html").exists()


def build(book_dir: Path) -> bool:
    """Build an mdBook into its book/ folder without a window where the pages are missing."""
    out = book_dir / "book"
    tmp = book_dir / ".book-building"
    if tmp.exists():
        shutil.rmtree(tmp)
    p = subprocess.run([mdbook(), "build", str(book_dir), "-d", str(tmp)], capture_output=True, text=True)
    if p.returncode != 0 or not (tmp / "index.html").exists():
        log(f"build failed: {book_dir}\n{p.stderr[-2000:]}")
        shutil.rmtree(tmp, ignore_errors=True)
        return False
    old = book_dir / ".book-old"
    if old.exists():
        shutil.rmtree(old)
    if out.exists():
        out.rename(old)
    tmp.rename(out)
    shutil.rmtree(old, ignore_errors=True)
    return True


def build_all(root: Path) -> dict[str, tuple[float, int]]:
    sigs = {}
    for name in classes(root):
        log(f"building {name}")
        build(root / name / "book")
        sigs[name] = signature(root / name)
    write_hub(root, [class_info(root / n) for n in classes(root)])
    build(root / HUB)
    return sigs


def watch(root: Path, sigs: dict, interval: float):
    hub_state = None
    while True:
        time.sleep(interval)
        try:
            names = classes(root)
            for name in names:
                sig = signature(root / name)
                if sigs.get(name) != sig:
                    log(f"{name} changed, rebuilding")
                    if build(root / name / "book"):
                        sigs[name] = sig
            infos = [class_info(root / n) for n in names]
            if infos != hub_state:
                hub_state = infos
                if write_hub(root, infos):
                    build(root / HUB)
        except Exception as exc:                 # keep serving whatever happens to one build
            log(f"watch error: {exc}")


class Handler(SimpleHTTPRequestHandler):
    """/ is the hub, /<class>/... is that class's built book."""

    def __init__(self, *a, root: Path, **kw):
        self.root = root
        super().__init__(*a, directory=str(root / HUB / "book"), **kw)

    def book_of(self, path: str):
        """(class name, rest of the path) when the path is inside a class book."""
        seg = path.split("?", 1)[0].split("#", 1)[0].split("/")
        if len(seg) > 1 and seg[1] and re.fullmatch(r"[\w.-]+", seg[1]) and not seg[1].startswith(".") \
                and (self.root / seg[1] / "book" / "book.toml").exists():
            return seg[1], "/" + "/".join(seg[2:]) if len(seg) > 2 else None
        return None, None

    def translate_path(self, path):
        name, rest = self.book_of(path)
        if name is None:
            return super().translate_path(path)
        saved = self.directory
        self.directory = str(self.root / name / "book" / "book")
        try:
            return super().translate_path(rest or "/")
        finally:
            self.directory = saved

    def do_GET(self):
        name, rest = self.book_of(self.path)
        if name is not None and rest is None:          # /dekla -> /dekla/
            self.send_response(301)
            self.send_header("Location", f"/{name}/")
            self.end_headers()
            return
        super().do_GET()

    do_HEAD = do_GET

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


def serve(root: Path, host: str, port: int, interval: float):
    sigs = build_all(root)
    threading.Thread(target=watch, args=(root, sigs, interval), daemon=True).start()
    server = ThreadingHTTPServer((host, port), functools.partial(Handler, root=root))
    log(f"serving {len(sigs)} book(s) on http://{host}:{port}/")
    server.serve_forever()


UNIT = """[Unit]
Description=Jegyzet hub: all class books on http://{host}:{port}/
After=network.target

[Service]
Type=simple
ExecStart={python} {script} {root} serve --host {host} --port {port}
Environment=PATH={cargo}:/usr/local/bin:/usr/bin:/bin
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
"""


def install_service(root: Path, host: str, port: int):
    unit_dir = Path.home() / ".config" / "systemd" / "user"
    unit_dir.mkdir(parents=True, exist_ok=True)
    python = "/usr/bin/python3" if Path("/usr/bin/python3").exists() else sys.executable
    unit = unit_dir / "jegyzet.service"
    unit.write_text(UNIT.format(host=host, port=port, python=python, script=Path(__file__).resolve(),
                                root=root, cargo=Path.home() / ".cargo" / "bin"))
    for cmd in (["daemon-reload"], ["enable", "--now", "jegyzet.service"], ["restart", "jegyzet.service"]):
        subprocess.run(["systemctl", "--user", *cmd], check=True)
    print(f"installed {unit}\nrunning: http://{host}:{port}/\n"
          "status: systemctl --user status jegyzet   log: journalctl --user -u jegyzet -f\n"
          "to keep it running while logged out: loginctl enable-linger $USER")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("cmd", choices=["build", "serve", "install-service"])
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=3000)
    ap.add_argument("--interval", type=float, default=2.0, help="seconds between change checks")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        sys.exit(f"error: {root} is not a folder")
    if args.cmd == "build":
        build_all(root)
    elif args.cmd == "serve":
        serve(root, args.host, args.port, args.interval)
    else:
        install_service(root, args.host, args.port)


if __name__ == "__main__":
    main()
