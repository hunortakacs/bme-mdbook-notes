#!/usr/bin/env python3
"""Create the mdBook for a class, or refresh its theme files.

  new_book.py CLASS_DIR --title "Deklaratív programozás" [--lang hu] [--intro-title Bevezetés]
  new_book.py CLASS_DIR --refresh        # copy the current theme assets into an existing book

Creates CLASS_DIR/book with book.toml, src/SUMMARY.md, src/intro.md and the
theme: syntax highlighting for ~55 languages, line numbers, the reading
progress bar, self-hosted KaTeX styles (math works offline) and, when
mdbook-mermaid is installed, Mermaid diagrams. Chapters already in the book
are never touched.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True   # no __pycache__ inside the skill folder
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C

ASSETS = Path(__file__).resolve().parent.parent / "assets"
INTRO = {"hu": "Bevezetés", "en": "Introduction", "de": "Einleitung"}

BOOK_TOML = '''[book]
title = "{title}"
language = "{lang}"
src = "src"

[build]
create-missing = false

# Math: $inline$ and $$display$$, rendered at build time by mdbook-katex.
[preprocessor.katex]
after = ["links"]
no-css = true            # the stylesheet and fonts are served from src/_katex (works offline)
throw-on-error = false   # a bad formula is shown in red and reported by check.py
{mermaid_pre}
[output.html]
site-url = "/{name}/"     # the hub (hub.py) serves this book under /{name}/
default-theme = "light"
preferred-dark-theme = "navy"
additional-css = ["theme/notes.css"]
additional-js = [{js}]

[output.html.search]
enable = true
limit-results = 30
use-boolean-and = true

[output.html.print]
enable = true

[output.html.playground]
runnable = false
copyable = true
'''


def copy_theme(bdir: Path) -> bool:
    theme = bdir / "theme"
    theme.mkdir(parents=True, exist_ok=True)
    for name in ("highlight.js", "notes.css", "notes.js", "head.hbs"):
        shutil.copyfile(ASSETS / "theme" / name, theme / name)
    weights = theme / "notes-weights.js"
    if not weights.exists():
        weights.write_text("window.NOTES_WEIGHTS = {};\n")
    katex = bdir / "src" / "_katex"
    if katex.exists():
        shutil.rmtree(katex)
    shutil.copytree(ASSETS / "katex", katex)
    mermaid = shutil.which("mdbook-mermaid") is not None
    if mermaid and not (bdir / "mermaid.min.js").exists():
        # `install` drops mermaid.min.js and mermaid-init.js next to book.toml
        subprocess.run(["mdbook-mermaid", "install", str(bdir)], capture_output=True)
        mermaid = (bdir / "mermaid.min.js").exists()
    return mermaid or (bdir / "mermaid.min.js").exists()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("class_dir")
    ap.add_argument("--title")
    ap.add_argument("--lang", default="hu")
    ap.add_argument("--intro-title")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()

    cdir = C.class_dir(args.class_dir)
    bdir = C.book_dir(cdir)
    toml = bdir / "book.toml"

    if args.refresh:
        if not toml.exists():
            C.die(f"{toml} does not exist; create the book first")
        mermaid = copy_theme(bdir)
        text = toml.read_text()
        if mermaid and "[preprocessor.mermaid]" not in text:
            print("mdbook-mermaid is installed now. To enable diagrams add to book.toml:\n"
                  '  [preprocessor.mermaid]\n  command = "mdbook-mermaid"\n'
                  '  and "mermaid.min.js", "mermaid-init.js" to additional-js')
        print(f"theme refreshed in {bdir}")
        return

    if toml.exists():
        C.die(f"{toml} already exists (use --refresh to update the theme)")
    if not args.title:
        C.die("--title is required")
    (bdir / "src").mkdir(parents=True, exist_ok=True)
    toml.write_text('[book]\ntitle = "x"\n')      # mdbook-mermaid install wants a book.toml
    mermaid = copy_theme(bdir)
    js = ['"theme/notes-weights.js"', '"theme/notes.js"']
    mermaid_pre = ""
    if mermaid:
        js += ['"mermaid.min.js"', '"mermaid-init.js"']
        mermaid_pre = '\n# Diagrams: ```mermaid code blocks.\n[preprocessor.mermaid]\ncommand = "mdbook-mermaid"\n'
    # mdbook-mermaid install may have written its own book.toml entries; ours replaces them
    toml.write_text(BOOK_TOML.format(title=args.title.replace('"', '\\"'), lang=args.lang, name=cdir.name,
                                     mermaid_pre=mermaid_pre, js=", ".join(js)))
    intro = args.intro_title or INTRO.get(args.lang, "Introduction")
    (bdir / "src" / "SUMMARY.md").write_text(f"# Summary\n\n[{intro}](intro.md)\n")
    (bdir / "src" / "intro.md").write_text(f"# {intro}\n")
    (bdir / ".gitignore").write_text("book/\n")
    C.work_dir(cdir).mkdir(exist_ok=True)
    print(f"created {bdir}" + ("" if mermaid else "  (mdbook-mermaid not found: diagrams stay images)"))


if __name__ == "__main__":
    main()
