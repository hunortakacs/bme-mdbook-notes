#!/usr/bin/env python3
"""Regression tests for the notes skill's scripts, without Claude in the loop.

  python3 notes-dev/test/test_scripts.py            # all tests
  python3 notes-dev/test/test_scripts.py -k Text    # tests whose name contains "Text"

Each test builds a throw-away class folder in a temporary git repository, runs
the scripts the way a run of the skill does (prepare, simulated transcription,
new_book, cover, check) and checks their reports and files. Needs pymupdf,
mdbook and mdbook-katex (the same as the skill); no LaTeX.
"""
from __future__ import annotations

import base64
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.request
from pathlib import Path

import pymupdf

SKILL = Path(__file__).resolve().parents[2] / ".claude" / "skills" / "notes"
S = SKILL / "scripts"
PNG_1PX = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==")


def run(script: str, *args, check=True) -> str:
    p = subprocess.run([sys.executable, "-B", str(S / script), *map(str, args)],
                       capture_output=True, text=True)
    if check and p.returncode != 0:
        raise AssertionError(f"{script} {' '.join(map(str, args))} failed ({p.returncode}):\n{p.stdout}\n{p.stderr}")
    return p.stdout + p.stderr


def make_pdf(path: Path, slides: list[str]):
    """One page per slide: a title line, then body lines (plain text)."""
    doc = pymupdf.open()
    for text in slides:
        page = doc.new_page(width=360, height=270)
        title, _, body = text.partition("\n")
        page.insert_text((20, 40), title, fontsize=16)
        y = 75
        for line in body.splitlines():
            page.insert_text((24, y), line, fontsize=11)
            y += 16
    doc.save(path)


SLIDES = [
    "Bevezetés\nA tárgy a deklaratív programozásról szól.",
    "Rekurzió\nA rekurzív függvény önmagát hívja.\nMinden hívás egyszerűbb esetre vezet.",
    "Listák\nA lista feje és farka.\nAz üres lista jele [].",
    "Kérdések\nKöszönöm a figyelmet!",
]

NOTES = """# Gyakorlat

Bevezető szöveg.

## Első feladat

```elixir
def hossz([]), do: 0
def hossz([_ | t]), do: 1 + hossz(t)
```

## Második feladat

```elixir
def osszeg([]), do: 0
def osszeg([h | t]), do: h + osszeg(t)
```

<!-- livebook:{"output":true} -->

```
nagyon hosszú kimenet, amit kihagyunk
```
"""


class ClassFolder(unittest.TestCase):
    """A fresh repository with one class folder per test."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="notes-test-"))
        self.root = self.tmp / "repo"
        self.c = self.root / "proba"
        self.res = self.c / "res"
        self.res.mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.email", "t@t"], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "t"], check=True)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # helpers -----------------------------------------------------------------
    def transcript(self, slug: str) -> Path:
        return self.c / "_work" / "sources" / slug / "transcript.md"

    def view_all(self, slug: str):
        """Simulated transcription: every TODO unit becomes viewed."""
        t = self.transcript(slug)
        t.write_text(re.sub(r"<!-- status: TODO view (\S+) -->", r"<!-- status: viewed \1 -->", t.read_text()))

    def coverage(self) -> dict[tuple[str, str], str]:
        rows = (self.c / "_work" / "coverage.tsv").read_text().splitlines()[1:]
        return {(r.split("\t")[0], r.split("\t")[1]): r.split("\t")[3] for r in rows if r.strip()}

    def chapter(self, name: str, text: str):
        f = self.c / "book" / "src" / name
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
        summary = self.c / "book" / "src" / "SUMMARY.md"
        if f"]({name})" not in summary.read_text():
            summary.write_text(summary.read_text() + f"- [{name}]({name})\n")

    def commit(self):
        subprocess.run(["git", "-C", str(self.root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-qm", "x"], check=True)


class PdfLifecycle(ClassFolder):
    def test_new_changed_renamed_removed(self):
        make_pdf(self.res / "ea01.pdf", SLIDES)
        out = run("prepare.py", self.c)
        self.assertIn("NEW       ea01.pdf", out)
        units = json.loads((self.c / "_work/sources/ea01/extract.json").read_text())["units"]
        self.assertEqual([u["id"] for u in units], ["s1", "s2", "s3", "s4"])

        self.view_all("ea01")
        t = self.transcript("ea01")                     # a transcriber's edit in an unchanged unit
        t.write_text(t.read_text().replace("A rekurzív függvény", "A rekurzív függvény (TRANSCRIBED)"))
        run("new_book.py", self.c, "--title", "Próba")
        self.assertIn('site-url = "/proba/"', (self.c / "book/book.toml").read_text())
        self.chapter("rekurzio.md", "# Rekurzió\n\nA rekurzív függvény önmagát hívja. Minden hívás egyszerűbb "
                     "esetre vezet. A lista feje és farka; az üres lista jele `[]`.\n\n"
                     '<p class="sources">Forrás: ea01.pdf (2–3. dia)</p>\n')
        run("cover.py", self.c, "set", "ea01", "s1", "intro.md")
        run("cover.py", self.c, "set", "ea01", "s2-s3", "rekurzio.md")
        run("cover.py", self.c, "set", "ea01", "s4", "cut: questions slide")
        (self.c / "book/src/intro.md").write_text("# Bevezetés\n\nA tárgy a deklaratív programozásról szól.\n\n"
                                                 '<p class="sources">Forrás: ea01.pdf (1. dia)</p>\n')
        out = run("check.py", self.c, "--finalize")
        self.assertIn("0 failure(s)", out)
        self.assertIn("finalized: 1 source(s)", out)
        self.commit()
        self.assertIn("Nothing to do", run("prepare.py", self.c))

        # CHANGED: slide 3 edited, one slide added -> only those are new work, the rest is carried over
        changed = SLIDES[:2] + ["Listák\nA lista feje és farka.\nAz üres lista jele [] (nil nem lista)."] \
            + SLIDES[3:] + ["Összefoglalás\nRekurzió és listák."]
        make_pdf(self.res / "ea01.pdf", changed)
        out = run("prepare.py", self.c)
        self.assertIn("CHANGED   ea01.pdf", out)
        self.assertRegex(out, r"new or changed units: s3, s5")
        cov = self.coverage()
        self.assertEqual(cov[("ea01", "s2")], "rekurzio.md")       # carried over
        self.assertEqual(cov[("ea01", "s3")], "")                  # changed: decide again
        t = self.transcript("ea01").read_text()
        self.assertIn("(TRANSCRIBED)", t.split("## s2")[1].split("## s3")[0])
        self.assertTrue((self.c / "_work/sources/ea01/transcript.prev.md").exists())

        # RENAMED: same bytes under a new name keep everything
        self.view_all("ea01")
        (self.res / "ea01.pdf").rename(self.res / "eloadas01.pdf")
        out = run("prepare.py", self.c)
        self.assertIn("RENAMED   ea01.pdf -> eloadas01.pdf", out)

        # REMOVED: the report names the chapters, the work folder moves to _work/removed
        (self.res / "eloadas01.pdf").unlink()
        out = run("prepare.py", self.c)
        self.assertIn("REMOVED   eloadas01.pdf", out)
        self.assertIn("rekurzio.md", out)
        self.assertTrue((self.c / "_work/removed/ea01").exists())

    def test_duplicate_source_and_force_only(self):
        make_pdf(self.res / "ea01.pdf", SLIDES)
        make_pdf(self.res / "ea01-copy.pdf", SLIDES + ["Extra\nCsak ebben van."])
        out = run("prepare.py", self.c)
        self.assertIn("DUPLICATE ea01-copy.pdf: 4 of 5 units", out)
        cov = self.coverage()
        self.assertEqual(cov[("ea01-copy", "s1")], "cut: duplicate of ea01.pdf s1")
        self.assertEqual(cov[("ea01-copy", "s5")], "")
        self.assertIn("status: duplicate of ea01.pdf s2", self.transcript("ea01-copy").read_text())

        out = run("prepare.py", self.c, "--force", "--view-all", "--only", "ea01")
        self.assertIn("FORCED    ea01.pdf", out)
        self.assertNotIn("FORCED    ea01-copy.pdf", out)
        self.assertNotIn("status: auto", self.transcript("ea01").read_text())

    def test_unsupported_and_image(self):
        (self.res / "anyag.zip").write_bytes(b"PK\x03\x04")
        (self.res / "abra.png").write_bytes(PNG_1PX)
        out = run("prepare.py", self.c)
        self.assertIn("SKIPPED   anyag.zip", out)
        self.assertIn("NEW       abra.png", out)
        self.assertIn("TODO view pages/abra.png", self.transcript("abra").read_text())


class Office(ClassFolder):
    def test_pptx_goes_through_libreoffice(self):
        """A stand-in `soffice` that writes a PDF checks the plumbing; real decks need LibreOffice."""
        bindir = self.tmp / "bin"
        bindir.mkdir()
        fake = bindir / "soffice"
        fake.write_text(f"""#!{sys.executable}
import sys, pymupdf
from pathlib import Path
args = sys.argv[1:]
out = Path(args[args.index("--outdir") + 1]); src = Path(args[-1])
doc = pymupdf.open(); pg = doc.new_page(width=360, height=270)
pg.insert_text((20, 40), "Dia egy", fontsize=16); pg.insert_text((24, 80), "Tartalom", fontsize=11)
doc.save(out / (src.stem + ".pdf"))
""")
        fake.chmod(0o755)
        (self.res / "ea02.pptx").write_bytes(b"PK\x03\x04 not really a deck")
        env = dict(os.environ, PATH=f"{bindir}:{os.environ['PATH']}")
        p = subprocess.run([sys.executable, "-B", str(S / "prepare.py"), str(self.c)],
                           capture_output=True, text=True, env=env)
        self.assertIn("NEW       ea02.pptx  [ea02, office]", p.stdout, p.stderr)
        self.assertIn("1 pages -> 1 units", p.stdout)
        self.assertTrue((self.c / "_work/sources/ea02/converted.pdf").exists())

        # without LibreOffice the source fails with a message, and the others go on
        (self.res / "notes.md").write_text("# A\n\nszöveg\n")
        (self.res / "ea03.pptx").write_bytes(b"PK")
        env = dict(os.environ, PATH="/usr/bin:/bin")
        p = subprocess.run([sys.executable, "-B", str(S / "prepare.py"), str(self.c)],
                           capture_output=True, text=True, env=env)
        self.assertIn("FAILED    ea03.pptx", p.stdout)
        self.assertIn("NEW       notes.md", p.stdout)


class TextSources(ClassFolder):
    def test_sections_partial_cut_and_change(self):
        (self.res / "gy01.livemd").write_text(NOTES)
        (self.res / "khf.exs").write_text("defmodule Khf do\n  def megold(x), do: x * 2 + 1\nend\n")
        out = run("prepare.py", self.c)
        self.assertIn("3 sections", out)
        cov = self.coverage()
        self.assertEqual(sorted(k[1] for k in cov if k[0] == "gy01"), ["s1", "s2", "s3"])
        self.assertIn(("khf", "all"), cov)

        run("new_book.py", self.c, "--title", "Próba")
        self.chapter("rekurzio.md", "# Rekurzió\n\n```elixir\ndef hossz([]), do: 0\ndef hossz([_ | t]), do: 1 + hossz(t)\n"
                     "def osszeg([]), do: 0\ndef osszeg([h | t]), do: h + osszeg(t)\n```\n\n"
                     "```elixir\ndefmodule Khf do\n  def megold(x), do: x * 2 + 1\nend\n```\n\n"
                     '<p class="sources">Forrás: gy01.livemd, khf.exs</p>\n')
        rows = ("gy01\ts1\tcut: introduction to the sheet\n"
                "gy01\ts2\trekurzio.md\n"
                "gy01\ts3\trekurzio.md; cut: long output of the cell\n"
                "khf\tall\trekurzio.md\n")
        out = subprocess.run([sys.executable, "-B", str(S / "cover.py"), str(self.c), "set-many", "-"],
                             input=rows, capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(self.coverage()[("gy01", "s3")], "rekurzio.md; cut: long output of the cell")
        bad = subprocess.run([sys.executable, "-B", str(S / "cover.py"), str(self.c), "set", "gy01", "s3",
                              "rekurzio.md; whatever"], capture_output=True, text=True)
        self.assertNotEqual(bad.returncode, 0)

        out = run("check.py", self.c, "--no-build")
        self.assertIn("0 failure(s)", out)
        self.assertIn("1 of them partly cut", out)
        self.assertIn("all code lines and formulas of the sources appear", out)

        # a dropped line is reported against its section, with the partial-cut note
        ch = self.c / "book/src/rekurzio.md"
        ch.write_text(ch.read_text().replace("def osszeg([h | t]), do: h + osszeg(t)\n", ""))
        out = run("check.py", self.c, "--no-build")
        self.assertIn("gy01 s3 -> rekurzio.md: 1 of 2 code lines not found (partly cut: long output of the cell)", out)

        # judged at --finalize, hidden afterwards
        run("check.py", self.c, "--no-build", "--finalize")
        out = run("check.py", self.c, "--no-build")
        self.assertIn("reviewed in an earlier run are not shown", out)
        self.commit()

        # one section changes, one disappears
        (self.res / "gy01.livemd").write_text(NOTES.replace("h + osszeg(t)", "h + osszeg(t) # összeg")
                                              .split("## Második")[0] + "## Második feladat\n\n"
                                              "```elixir\ndef osszeg([]), do: 0\ndef osszeg([h | t]), do: h + osszeg(t) # összeg\n```\n")
        out = run("prepare.py", self.c)
        self.assertIn("CHANGED   gy01.livemd", out)
        self.assertIn("new or changed sections: s3 (Második feladat)", out)
        (self.res / "gy01.livemd").write_text(NOTES.split("## Második")[0])
        out = run("prepare.py", self.c)
        self.assertIn("sections no longer in the file: s3", out)
        self.assertIn("removed section s3 was used in: rekurzio.md; cut: long output of the cell", out)

    def test_cover_changed_lists_chapters(self):
        (self.res / "gy01.livemd").write_text(NOTES)
        run("prepare.py", self.c)
        run("new_book.py", self.c, "--title", "Próba")
        self.commit()
        self.chapter("rekurzio.md", "# Rekurzió\n\nszöveg\n")
        run("cover.py", self.c, "set", "gy01", "s2", "rekurzio.md")
        out = run("cover.py", self.c, "changed")
        self.assertRegex(out, r"NEW\s+rekurzio\.md\s+Rekurzió\s+<- gy01 s2")


class Notebooks(ClassFolder):
    def test_ipynb_sections_and_figures(self):
        nb = {"metadata": {"kernelspec": {"language": "python"}}, "nbformat": 4, "cells": [
            {"cell_type": "markdown", "source": ["# Bevezetés\n", "Szöveg."]},
            {"cell_type": "code", "source": ["print(1 + 1)"], "outputs": [{"output_type": "stream", "text": ["2\n"]}]},
            {"cell_type": "markdown", "source": ["## Ábra"]},
            {"cell_type": "code", "source": ["plot()"], "outputs": [
                {"output_type": "display_data", "data": {"image/png": base64.b64encode(PNG_1PX).decode()}}]},
        ]}
        (self.res / "labor.ipynb").write_text(json.dumps(nb))
        out = run("prepare.py", self.c)
        self.assertIn("2 units, 1 to view", out)
        t = self.transcript("labor").read_text()
        self.assertIn("## s1 · p1 · Bevezetés\n<!-- status: auto -->", t)
        self.assertIn("```python\nprint(1 + 1)\n```", t)
        self.assertRegex(t, r"## s2 · p1 · Ábra\n<!-- status: TODO view figures/cell004-1\.png -->")
        self.assertTrue((self.c / "_work/sources/labor/figures/cell004-1.png").exists())


class Formulas(ClassFolder):
    def test_formula_missing_from_chapter(self):
        make_pdf(self.res / "ea.pdf", ["Qubit\nAllapot"])
        run("prepare.py", self.c)
        self.view_all("ea")
        t = self.transcript("ea")
        t.write_text(t.read_text().replace("Allapot", "$$\n\\ket{\\psi} = \\alpha\\ket{0} + \\beta\\ket{1}\n$$\n\n"
                                           "ahol $|\\alpha|^2 + |\\beta|^2 = 1$."))
        run("new_book.py", self.c, "--title", "Próba")
        self.chapter("qubit.md", "# Qubit\n\n$$\n\\ket{\\psi} = \\alpha \\ket{0} + \\beta\\ket{1}\n$$\n\n"
                     '<p class="sources">Forrás: ea.pdf (1. dia)</p>\n')
        run("cover.py", self.c, "set", "ea", "s1", "qubit.md")
        out = run("check.py", self.c, "--no-build")
        self.assertIn("1 of 2 formulas not found", out)
        self.assertIn("$|\\alpha|^2 + |\\beta|^2 = 1$", out)


class Hub(ClassFolder):
    def test_build_and_serve(self):
        make_pdf(self.res / "ea01.pdf", SLIDES[:1])
        run("prepare.py", self.c)
        run("new_book.py", self.c, "--title", "Próba tárgy")
        (self.root / "notes-dev").mkdir()                    # folders without a book are ignored
        with socket.socket() as s:
            s.bind(("127.0.0.1", 0))
            port = s.getsockname()[1]
        proc = subprocess.Popen([sys.executable, "-B", str(S / "hub.py"), str(self.root), "serve",
                                 "--port", str(port), "--interval", "0.5"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        try:
            base = f"http://127.0.0.1:{port}"
            for _ in range(120):
                try:
                    urllib.request.urlopen(base + "/", timeout=2)
                    break
                except OSError:
                    time.sleep(0.5)
            hub = urllib.request.urlopen(base + "/").read().decode()
            self.assertIn("Próba tárgy", hub)
            self.assertIn('href="/proba/"', hub)
            self.assertIn("Bevezetés", urllib.request.urlopen(base + "/proba/").read().decode())
            req = urllib.request.Request(base + "/proba")
            opener = urllib.request.build_opener(NoRedirect)
            with self.assertRaises(urllib.error.HTTPError) as r:
                opener.open(req)
            self.assertEqual(r.exception.code, 301)

            # the hub is a tracked mdBook in hub/; only the marked block is generated
            index = self.root / "hub" / "src" / "index.md"
            self.assertIn("[Próba tárgy](/proba/)", index.read_text())
            self.assertTrue((self.root / "hub" / "book.toml").exists())
            self.assertFalse((self.root / ".hub").exists())
            index.write_text(index.read_text().replace("# Notes\n", "# Notes\n\nMy own intro.\n"))
            (self.res.parent / "book" / "book.toml").write_text(
                (self.res.parent / "book" / "book.toml").read_text().replace("Próba tárgy", "Próba tárgy 2"))
            run("hub.py", self.root, "update")                    # the server may have done it already
            text = index.read_text()
            self.assertIn("My own intro.", text)
            self.assertIn("[Próba tárgy 2](/proba/)", text)
            self.assertNotIn("[Próba tárgy](/proba/)", text)
            status = subprocess.run(["git", "-C", str(self.root), "status", "--porcelain", "-uall", "hub"],
                                    capture_output=True, text=True).stdout
            self.assertIn("hub/src/index.md", status)
            self.assertNotIn("hub/book/", status)                 # build output stays out of git

            # a new chapter shows up without a restart
            self.chapter("uj.md", "# Új fejezet\n\nszöveg\n")
            for _ in range(60):
                try:
                    if "Új fejezet" in urllib.request.urlopen(base + "/proba/uj.html").read().decode():
                        break
                except OSError:
                    pass
                time.sleep(0.5)
            else:
                self.fail("the hub did not rebuild the changed book")
        finally:
            proc.terminate()
            proc.wait(10)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


if __name__ == "__main__":
    os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    unittest.main(verbosity=2)
