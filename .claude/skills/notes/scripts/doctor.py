#!/usr/bin/env python3
"""Check that everything the skill needs is installed. Exit code 1 if something required is missing.

  doctor.py
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path


def version(cmd: str) -> str | None:
    exe = shutil.which(cmd)
    if not exe:
        return None
    try:
        out = subprocess.run([exe, "--version"], capture_output=True, text=True, timeout=20).stdout
    except (OSError, subprocess.SubprocessError):
        return None
    m = re.search(r"(\d+\.\d+\.\d+)", out)
    return m.group(1) if m else "?"


def main():
    ok = True
    rows = []

    try:
        import numpy  # noqa: F401
        try:
            import pymupdf
        except ImportError:
            import fitz as pymupdf
        rows.append(("ok", "python: pymupdf, numpy", getattr(pymupdf, "__version__", "")))
    except ImportError as e:
        ok = False
        pip = "python3 -m pip install --user pymupdf numpy"
        # PEP 668 (Homebrew, newer distro Pythons) refuses plain --user installs.
        if (Path(sysconfig.get_path("stdlib")) / "EXTERNALLY-MANAGED").exists():
            pip += " --break-system-packages   (installs into ~/.local only)"
        rows.append(("MISSING", f"python package ({e.name})", pip))

    v = version("mdbook")
    if v is None:
        ok = False
        rows.append(("MISSING", "mdbook", "cargo install mdbook --locked   (Fedora: sudo dnf install cargo first)"))
    elif tuple(int(x) for x in v.split(".")[:2]) < (0, 5):
        ok = False
        rows.append(("TOO OLD", f"mdbook {v}", "needs 0.5 or newer: cargo install mdbook --locked --force"))
    else:
        rows.append(("ok", "mdbook", v))

    v = version("mdbook-katex")
    if v is None:
        ok = False
        rows.append(("MISSING", "mdbook-katex (math)", "cargo install mdbook-katex --locked"))
    else:
        rows.append(("ok", "mdbook-katex", v))

    v = version("mdbook-mermaid")
    if v is None:
        rows.append(("optional", "mdbook-mermaid (diagrams)", "cargo install mdbook-mermaid --locked"))
    else:
        rows.append(("ok", "mdbook-mermaid", v))

    rows.append(("ok" if shutil.which("git") else "optional", "git", "" if shutil.which("git") else "sudo dnf install git"))
    office = shutil.which("soffice") or shutil.which("libreoffice")
    rows.append(("ok" if office else "optional", "libreoffice (pptx/docx sources)",
                 "" if office else "only needed for non-PDF slides: sudo dnf install libreoffice-impress"))

    for status, what, note in rows:
        print(f"{status:<9} {what:<34} {note}")
    if not ok:
        print("\nInstall what is MISSING, then run this again. ~/.cargo/bin has to be on PATH.")
        sys.exit(1)


if __name__ == "__main__":
    main()
