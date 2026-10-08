#!/usr/bin/env python3
"""mdBook preprocessor: syntax highlighting at build time with Pygments (~600 languages).

In book.toml:

  [preprocessor.pygments]
  command = "python3 ../../scripts/mdbook_pygments.py"
  after = ["links", "katex"]       # after katex, so a `$` in code is never taken for math

Every fenced code block whose language Pygments knows becomes highlighted HTML with Pygments'
CSS classes (theme/pygments.css colours them). Unknown languages and `mermaid` stay as they are. In session blocks (iex, pycon, console, erl) a
blank line is put between a command's output and the next prompt, so the source needs no spacing.
The book's theme/highlight.js is a stub, so mdBook does not highlight again in the browser.
"""
from __future__ import annotations

import json
import re
import sys

try:
    from pygments import format
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import get_lexer_by_name
    from pygments.token import Generic
    from pygments.util import ClassNotFound
except ImportError:
    sys.exit("mdbook_pygments: Pygments is not installed (python3 -m pip install --user pygments)")

SKIP = {"mermaid"}
FENCE = re.compile(r"^(?P<prefix>(?:[ \t]*>)*[ \t]*)(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
FORMATTER = HtmlFormatter(nowrap=True)


def lexer(info: str):
    lang = re.split(r"[\s,{]", info.strip(), maxsplit=1)[0].lower()
    if not lang or lang in SKIP:
        return None, lang
    try:
        return get_lexer_by_name(lang, tabsize=4, stripnl=False), lang
    except ClassNotFound:
        return None, lang


def space_prompts(tokens):
    """Yield the tokens with a blank line before every session prompt that directly follows output."""
    after_output, at_line_start = False, True
    for ttype, value in tokens:
        if at_line_start:
            if ttype is Generic.Prompt and after_output:
                yield Generic.Output, "\n"
            after_output = ttype is Generic.Output and value.strip() != "" and not value.endswith("\n\n")
        at_line_start = value.endswith("\n")
        yield ttype, value


def render(prefix: str, lang: str, lex, body: list[str]) -> list[str]:
    code = format(space_prompts(lex.get_tokens("\n".join(body) + "\n")), FORMATTER)
    html = f'<pre><code class="language-{lang} hljs">{code}</code></pre>'
    return [prefix + line for line in html.split("\n")]


def process(text: str) -> str:
    lines, out, i = text.split("\n"), [], 0
    while i < len(lines):
        m = FENCE.match(lines[i])
        if not m or (m["fence"][0] == "`" and "`" in m["info"]):
            out.append(lines[i])
            i += 1
            continue
        prefix, fence = m["prefix"], m["fence"]
        close = re.compile(r"^" + re.escape(prefix.rstrip()) + r"[ \t]*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}[ \t]*$")
        j = i + 1
        while j < len(lines) and not close.match(lines[j]):
            j += 1
        lex, lang = lexer(m["info"])
        if lex is None or j == len(lines):          # unknown language or unclosed fence: leave it to mdBook
            out += lines[i:j + 1]
        else:
            body = [l[len(prefix):] if l.startswith(prefix) else l.lstrip(" ") for l in lines[i + 1:j]]
            out += render(prefix, lang, lex, body)
        i = j + 1
    return "\n".join(out)


def walk(node):
    if isinstance(node, dict):
        ch = node.get("Chapter")
        if isinstance(ch, dict) and isinstance(ch.get("content"), str):
            ch["content"] = process(ch["content"])
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0 if sys.argv[2:3] == ["html"] else 1)
    _context, book = json.load(sys.stdin)
    walk(book)
    json.dump(book, sys.stdout)


if __name__ == "__main__":
    main()
