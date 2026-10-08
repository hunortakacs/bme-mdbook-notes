#!/usr/bin/env python3
"""Build the whole site for static hosting: the hub at the root, every book under /<class>/.

  build_site.py ROOT OUT [--base PATH] [--install DIR]

ROOT     the repository root (holds hub/ and the class folders)
OUT      output folder; it is emptied first
--base   the URL path the site is served under, e.g. /notes/ (default: the path of
         $READTHEDOCS_CANONICAL_URL when it is set, otherwise /). Only mdBook's 404 page uses it;
         every other link is relative, so the site works under any prefix.
--install DIR  first download the pinned tools (static release binaries of mdbook,
         mdbook-katex, mdbook-mermaid) into DIR and use them. For a fresh build machine
         (Cloudflare Pages, CI); locally the installed tools are used.

The build is what the hub serves locally: each book exactly as committed (theme, word weights
and all), no checks and no changes to the repository.
"""
from __future__ import annotations

import argparse
import io
import os
import shutil
import subprocess
import sys
import tarfile
import urllib.parse
import urllib.request
from pathlib import Path

# The versions the books are tested with (notes-dev/DEVELOPMENT.md, "Versions"). All three are
# static (musl) release binaries, so a build machine needs nothing but Python. mdbook-katex 0.10.0
# has no binary release; its 0.10.0-alpha binary renders the books byte for byte like 0.10.0.
MDBOOK = "0.5.4"
MERMAID = "0.17.1"
KATEX = "0.10.0-alpha"
RELEASES = {
    "mdbook": f"https://github.com/rust-lang/mdBook/releases/download/v{MDBOOK}/"
              f"mdbook-v{MDBOOK}-x86_64-unknown-linux-musl.tar.gz",
    "mdbook-mermaid": f"https://github.com/badboy/mdbook-mermaid/releases/download/v{MERMAID}/"
                      f"mdbook-mermaid-v{MERMAID}-x86_64-unknown-linux-musl.tar.gz",
    "mdbook-katex": f"https://github.com/lzanini/mdbook-katex/releases/download/{KATEX}-binaries/"
                    f"mdbook-katex-v{KATEX}-x86_64-unknown-linux-musl.tar.gz",
}


def install(dest: Path) -> dict:
    bindir = dest / "bin"
    bindir.mkdir(parents=True, exist_ok=True)
    for name, url in RELEASES.items():
        if (bindir / name).exists():
            continue
        print(f"downloading {name}: {url}", flush=True)
        with urllib.request.urlopen(url, timeout=120) as r:
            data = r.read()
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            member = next(m for m in tar.getmembers() if Path(m.name).name == name and m.isfile())
            member.name = name
            tar.extract(member, bindir)
        (bindir / name).chmod(0o755)
    env = dict(os.environ)
    env["PATH"] = f"{bindir}{os.pathsep}{env.get('PATH', '')}"
    return env


def build(book: Path, out: Path, site_url: str, env: dict):
    env = dict(env)
    env["MDBOOK_OUTPUT__HTML__SITE_URL"] = site_url        # mdBook config override: output.html.site-url
    print(f"building {book} -> {out}", flush=True)
    p = subprocess.run(["mdbook", "build", str(book), "--dest-dir", str(out)],
                       env=env, capture_output=True, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stdout + p.stderr)
        sys.exit(f"mdbook build failed for {book}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("out")
    ap.add_argument("--base")
    ap.add_argument("--install", metavar="DIR")
    args = ap.parse_args()

    root, out = Path(args.root).resolve(), Path(args.out).resolve()
    base = args.base
    if base is None:
        canonical = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
        base = urllib.parse.urlparse(canonical).path if canonical else "/"
    base = "/" + base.strip("/") + "/" if base.strip("/") else "/"

    env = install(Path(args.install).resolve()) if args.install else dict(os.environ)
    if not shutil.which("mdbook", path=env.get("PATH")):
        sys.exit("mdbook is not installed (use --install DIR)")

    hub = root / "hub"
    if not (hub / "book.toml").exists():
        sys.exit(f"{hub}/book.toml does not exist: the hub is the site's root page")
    books = sorted(d.name for d in root.iterdir()
                   if d.is_dir() and not d.name.startswith(".") and (d / "book" / "book.toml").exists())
    if out.exists():
        shutil.rmtree(out)
    build(hub, out, base, env)
    for name in books:
        build(root / name / "book", out / name, f"{base}{name}/", env)
    print(f"site built in {out}: hub + {len(books)} book(s) ({', '.join(books) or 'none'}), base {base}")


if __name__ == "__main__":
    main()
