#!/usr/bin/env python3
"""Triage a PDF (slides or a document) into logical units with a text draft.

For every logical slide it decides whether the text layer alone can be
trusted, or whether a person (Claude) has to look at the rendered page.

What it does
  1. Collapses animation steps (Beamer overlays, exported build steps) into
     logical slides. PDF page labels are used when present, otherwise
     consecutive pages where each one only adds to the previous one are
     merged. A step is only dropped when both its words and its ink are
     contained in a later step, so replaced content is kept.
  2. Learns the slide template (background, logo, header, footer) as the
     per-pixel median of the pages and ignores it.
  3. Flags each slide: math, graphic, image, table, layout, stacked, encoding,
     no-text, annot, variant.
     Flagged slides are rendered to PNG and get status TODO in the draft.
  4. Writes extract.json, draft.md, pages/*.png and figures/*.png.

Usage
  pdf_triage.py triage FILE.pdf --out DIR [--view-all] [--debug]
  pdf_triage.py page   FILE.pdf PAGE -o OUT.png [--width 1400]
  pdf_triage.py crop   FILE.pdf PAGE X0 Y0 X1 Y1 -o OUT.png [--width 1400]
        PAGE is the 1-based physical page; X0..Y1 are fractions (0-1) of the page.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, deque
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:  # older PyMuPDF
    import fitz
import numpy as np

ANALYSIS_WIDTH = 800          # px, resolution of the ink analysis
VIEW_WIDTH = 1280             # px, page renders Claude looks at
FIGURE_WIDTH = 1400           # px, max width of cropped figures
INK_THRESHOLD = 40            # 0-255, difference from template that counts as ink
EDGE_THRESHOLD = 28           # 0-255, gray step that counts as an edge
CELL = 6                      # px, grid cell for connected components

MATH_FONT = re.compile(
    r"(CMMI|CMSY|CMEX|MSAM|MSBM|EUFM|EUSM|RSFS|LMMath|STIX|XITS|Asana|Cambria ?Math|"
    r"Math|Symbol|MT ?Extra|esint|wasy|stmary|bbm|bbold|dsrom|MnSymbol|txsy|pxsy|txex|"
    r"pxex|rtxmi|txmi|pxmi|fourier-m|eurm|eusm|msbm|msam|cmbsy|cmmib)", re.I)
MONO_FONT = re.compile(
    r"(Mono|Courier|Consol|CMTT|LMTT|cmtt|SFTT|Menlo|Inconsolata|Fira ?Code|Source ?Code|"
    r"Typewriter|txtt|pcr|NimbusMon|Hack|JetBrains|Lucida ?Console|Andale|Monaco|"
    r"Liberation ?Mono|Ubuntu ?Mono|Cascadia|Iosevka|BeraMono|Anonymous)", re.I)
MATH_CHARS = set("∑∏∫∮√∞≤≥≠≈≡∝∈∉∋⊂⊃⊆⊇∪∩∧∨¬∀∃∄∅∇∂±∓×÷·∘⊕⊗⊥∥∠→←↔⇒⇐⇔↦⟨⟩⟶⟹⌈⌉⌊⌋ℝℕℤℚℂℙ𝔼ℏ†‖′″"
                 "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩϵϑϕϱ⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉ᵀ⊤⊢⊨≪≫≺≻∼≃≅")
BULLET_CHARS = "•◦▪▫■□●○◆◇▶►▸▹‣⁃∙·–—*➤➢✓✔-"


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def decode_label(label: str) -> str:
    """PyMuPDF returns hex-string labels like '<FEFF0031>' undecoded."""
    m = re.fullmatch(r"<([0-9A-Fa-f]+)>", label or "")
    if not m:
        return label or ""
    raw = bytes.fromhex(m.group(1))
    try:
        if raw.startswith(b"\xfe\xff"):
            return raw[2:].decode("utf-16-be")
        return raw.decode("latin-1")
    except Exception:
        return label


def render(page, width: int, clip=None) -> np.ndarray:
    rect = clip or page.rect
    zoom = width / rect.width
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip, alpha=False,
                          colorspace=fitz.csRGB)
    return np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)


def save_png(page, path: Path, width: int, clip=None):
    rect = clip or page.rect
    zoom = width / rect.width
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip, alpha=False)
    path.parent.mkdir(parents=True, exist_ok=True)
    pix.save(str(path))


def dilate(mask: np.ndarray, r: int = 1) -> np.ndarray:
    out = mask.copy()
    for _ in range(r):
        m = out.copy()
        m[1:, :] |= out[:-1, :]
        m[:-1, :] |= out[1:, :]
        m[:, 1:] |= out[:, :-1]
        m[:, :-1] |= out[:, 1:]
        out = m
    return out


def long_runs(mask: np.ndarray, length: int, axis: int) -> np.ndarray:
    """Pixels of `mask` that belong to a straight run of at least `length` along `axis`."""
    if mask.shape[axis] < length:
        return np.zeros_like(mask)
    m = mask.astype(np.int32)
    c = np.cumsum(m, axis=axis)
    pad = [(0, 0), (0, 0)]
    pad[axis] = (1, 0)
    c = np.pad(c, pad)
    if axis == 0:
        full = (c[length:, :] - c[:-length, :]) == length      # run starts here
        out = np.zeros_like(mask)
        idx = np.argwhere(full)
        for k in range(length):
            out[idx[:, 0] + k, idx[:, 1]] = True
    else:
        full = (c[:, length:] - c[:, :-length]) == length
        out = np.zeros_like(mask)
        idx = np.argwhere(full)
        for k in range(length):
            out[idx[:, 0], idx[:, 1] + k] = True
    return out


def components(active: np.ndarray):
    """8-connected components on a small boolean grid. Yields lists of (row, col)."""
    seen = np.zeros_like(active, dtype=bool)
    rows, cols = active.shape
    for r0, c0 in np.argwhere(active):
        if seen[r0, c0]:
            continue
        comp, q = [], deque([(r0, c0)])
        seen[r0, c0] = True
        while q:
            r, c = q.popleft()
            comp.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and active[rr, cc] and not seen[rr, cc]:
                        seen[rr, cc] = True
                        q.append((rr, cc))
        yield comp


# --------------------------------------------------------------------------
# text layer
# --------------------------------------------------------------------------

def page_segments(page):
    """Text segments (one per PyMuPDF line) with font statistics."""
    type3 = set()                     # bitmap fonts: the text layer is often wrongly encoded
    for f in page.get_fonts(full=True):
        if f[2] == "Type3":
            type3.update((f[3], f[4]))
    flags = fitz.TEXT_PRESERVE_WHITESPACE | fitz.TEXT_MEDIABOX_CLIP
    segs = []
    for block in page.get_text("dict", flags=flags)["blocks"]:
        for line in block.get("lines", []):
            spans = [s for s in line["spans"] if s["text"]]
            for sp in spans:
                if not is_mono(sp):
                    sp["text"] = fix_accents(sp["text"])
            text = "".join(s["text"] for s in spans)
            if not text.strip():
                continue
            if abs(line.get("dir", (1, 0))[0]) < 0.9:      # rotated text: keep, flag later
                rotated = True
            else:
                rotated = False
            n = sum(len(s["text"].strip()) for s in spans) or 1
            mono = sum(len(s["text"].strip()) for s in spans if is_mono(s))
            math = sum(len(s["text"].strip()) for s in spans if MATH_FONT.search(s["font"]))
            size = max(spans, key=lambda s: len(s["text"]))["size"]
            x0, y0, x1, y1 = line["bbox"]
            bad = sum(1 for ch in text if ch == "\ufffd" or "\ue000" <= ch <= "\uf8ff"
                      or (ord(ch) < 32 and ch not in "\t\n"))
            t3 = any(s["font"] in type3 for s in spans)
            segs.append({
                "bad_chars": bad, "type3": t3,
                "bbox": [x0, y0, x1, y1], "text": text, "spans": spans, "size": size,
                "mono": mono / n, "math_chars": math, "rotated": rotated,
                "origin_y": spans[0]["origin"][1] if spans else y1,
            })
    return segs


ACCENTS = {"˝": "\u030b", "´": "\u0301", "`": "\u0300", "¨": "\u0308", "ˆ": "\u0302", "˜": "\u0303",
           "ˇ": "\u030c", "˚": "\u030a", "¯": "\u0304", "˘": "\u0306", "˙": "\u0307", "¸": "\u0327"}
ACCENT_RE = re.compile("([" + "".join(ACCENTS) + "])([A-Za-z])")


def fix_accents(text: str) -> str:
    """Old TeX fonts emit 'accent + letter' as two glyphs (˝o for ő). Compose them."""
    if not any(a in text for a in ACCENTS):
        return text
    text = text.replace("ı", "i") if re.search("[" + "".join(ACCENTS) + "]ı", text) else text
    return ACCENT_RE.sub(lambda m: unicodedata.normalize("NFC", m.group(2) + ACCENTS[m.group(1)]), text)


def seg_signature(seg):
    t = re.sub(r"\d+", "#", seg["text"].strip())
    x0, y0, _, _ = seg["bbox"]
    return (t, round(x0 / 3), round(y0 / 3))


def words_of(segs):
    out = Counter()
    for s in segs:
        for w in re.findall(r"\S+", s["text"]):
            out[w] += 1
    return out


MEASURED_MONO: set = set()        # fonts found to be fixed-width by measuring glyph advances


def is_mono(span):
    return bool(MONO_FONT.search(span["font"]) or (span["flags"] & 8) or span["font"] in MEASURED_MONO)


def measure_fonts(doc, max_pages=60):
    """Find fixed-width fonts by glyph advance, for fonts whose name does not say so."""
    narrow, wide = set("ilj.,:;'|!1It"), set("mwMW@")
    adv = {}
    n = len(doc)
    for i in sorted(set(int(round(x)) for x in np.linspace(0, n - 1, min(n, max_pages)))):
        for block in doc[i].get_text("rawdict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]:
            for line in block.get("lines", []):
                for sp in line["spans"]:
                    chars = sp.get("chars", [])
                    d = adv.setdefault(sp["font"], {"n": [], "w": []})
                    for a, b in zip(chars, chars[1:]):
                        step = (b["origin"][0] - a["origin"][0]) / max(sp["size"], 1)
                        if step <= 0:
                            continue
                        if a["c"] in narrow:
                            d["n"].append(step)
                        elif a["c"] in wide:
                            d["w"].append(step)
    for font, d in adv.items():
        if len(d["n"]) >= 3 and len(d["w"]) >= 2:
            a, b = float(np.median(d["n"])), float(np.median(d["w"]))
            if abs(a - b) / max(a, b) < 0.04:
                MEASURED_MONO.add(font)


REPL_PROMPT = re.compile(r"(iex(\(\d+\))?>|\.\.\.(\(\d+\))?>|>>>|\?-|\$ )")
COMMENT_START = ("#", "//", "%", "--", ";", "/*", "(*")


def is_code_row(row):
    """A row is code when it starts in a monospace font and is mostly code,
    or the rest of it is a comment set in another font."""
    spans = [sp for p in row["parts"] for sp in p["spans"] if sp["text"].strip()]
    if not spans or not is_mono(spans[0]):
        return False
    if row["mono"] > 0.7:
        return True
    rest = "".join(sp["text"] for sp in spans if not is_mono(sp)).strip()
    first_other = next((sp["text"].strip() for sp in spans if not is_mono(sp)), "")
    return first_other.startswith(COMMENT_START) and bool(rest)


def prose_markup(spans):
    """Inline markup for the spans of a prose row; adjacent code spans become one run."""
    colors = Counter()
    for sp in spans:
        if not is_mono(sp):
            colors[sp.get("color")] += len(sp["text"])
    row_color = colors.most_common(1)[0][0] if len(colors) > 1 else None
    runs = []                                   # (kind, text)
    for sp in spans:
        t = sp["text"]
        if not t:
            continue
        if is_mono(sp):
            kind = "code"
        elif not t.strip():
            kind = "space"
        elif sp["flags"] & 1:
            kind = "sup"
        elif sp["flags"] & 16:
            kind = "bold"
        elif row_color is not None and sp.get("color") != row_color and len(t.strip()) > 1:
            kind = "em"
        else:
            kind = "text"
        if runs and runs[-1][0] == kind:
            runs[-1][1] += t
        elif runs and kind == "space" and runs[-1][0] == "code":
            runs[-1][1] += t
        elif runs and kind == "code" and runs[-1][0] == "space" and len(runs) > 1 and runs[-2][0] == "code":
            sp_ = runs.pop()[1]
            runs[-1][1] += sp_ + t
        else:
            runs.append([kind, t])
    out = ""
    wrap = {"code": ("`", "`"), "sup": ("^(", ")"), "bold": ("**", "**"), "em": ("*", "*")}
    for kind, t in runs:
        if kind in wrap and t.strip():
            lead, trail = t[: len(t) - len(t.lstrip())], t[len(t.rstrip()):]
            out += f"{lead}{wrap[kind][0]}{t.strip()}{wrap[kind][1]}{trail}"
        else:
            out += t
    return out


def build_rows(segs, merge_mono=False):
    """Merge segments on the same baseline into rows, left to right.

    Segments separated by a wide gap stay apart unless merge_mono is set and both are code."""
    segs = sorted(segs, key=lambda s: (round(s["origin_y"], 1), s["bbox"][0]))
    rows = []
    for s in segs:
        if rows:
            r = rows[-1]
            same_line = abs(r["origin_y"] - s["origin_y"]) < 0.35 * max(r["size"], s["size"])
            gap = s["bbox"][0] - r["bbox"][2]
            both_mono = r["mono"] > 0.7 and s["mono"] > 0.7
            trailing_comment = r["mono"] > 0.5 and s["text"].strip().startswith(COMMENT_START)
            if same_line and gap > -1 and (((both_mono or trailing_comment) and merge_mono)
                                           or gap < 2.5 * s["size"]):
                r["parts"].append(s)
                r["bbox"][2] = max(r["bbox"][2], s["bbox"][2])
                r["bbox"][1] = min(r["bbox"][1], s["bbox"][1])
                r["bbox"][3] = max(r["bbox"][3], s["bbox"][3])
                n1, n2 = len(r["text"]), len(s["text"])
                r["mono"] = (r["mono"] * n1 + s["mono"] * n2) / max(1, n1 + n2)
                r["text"] += " " + s["text"]
                continue
        rows.append({"bbox": list(s["bbox"]), "origin_y": s["origin_y"], "size": s["size"],
                     "mono": s["mono"], "text": s["text"], "parts": [s]})
    return rows


def order_columns(rows, page_w):
    """Detect a two-column layout. Returns (ordered rows, True if columns were found)."""
    if len(rows) < 4:
        return sorted(rows, key=lambda r: (r["bbox"][1], r["bbox"][0])), False
    best = None
    for c in np.linspace(0.3 * page_w, 0.7 * page_w, 25):
        left = [r for r in rows if r["bbox"][2] < c - 2]
        right = [r for r in rows if r["bbox"][0] > c + 2]
        cross = [r for r in rows if r not in left and r not in right]
        if len(left) < 2 or len(right) < 2:
            continue
        top = max(min(r["bbox"][1] for r in left), min(r["bbox"][1] for r in right))
        bot = min(max(r["bbox"][3] for r in left), max(r["bbox"][3] for r in right))
        if bot - top < 2.0 * np.median([r["size"] for r in rows]):
            continue
        if any(top < (r["bbox"][1] + r["bbox"][3]) / 2 < bot for r in cross):
            continue
        # the right column must really start to the right (not ragged code/indent)
        score = len(left) + len(right)
        if best is None or score > best[0]:
            best = (score, left, right, cross, top, bot)
    if best is None:
        return sorted(rows, key=lambda r: (r["bbox"][1], r["bbox"][0])), False
    _, left, right, cross, top, bot = best
    key = lambda r: (r["bbox"][1], r["bbox"][0])
    above = [r for r in cross if (r["bbox"][1] + r["bbox"][3]) / 2 <= top]
    below = [r for r in cross if (r["bbox"][1] + r["bbox"][3]) / 2 >= bot]
    aligned = sum(1 for r in right if any(abs(r["origin_y"] - l["origin_y"]) < 0.3 * r["size"] for l in left))
    if aligned >= 0.8 * len(right) and np.mean([r["mono"] for r in left + right]) > 0.7:
        return None, True                      # code with an aligned second column: keep rows
    ordered = []
    for group in (above, left, right, below):
        segs = [p for r in group for p in r["parts"]]
        ordered += sorted(build_rows(segs, merge_mono=True), key=key)
    return ordered, True


def code_text(rows):
    """Rebuild a monospace block from positioned rows, keeping indentation and blank lines."""
    widths = []
    for r in rows:
        for p in r["parts"]:
            for sp in p["spans"]:
                t = sp["text"]
                if len(t.strip()) >= 3:
                    widths.append((sp["bbox"][2] - sp["bbox"][0]) / len(t))
    cw = float(np.median(widths)) if widths else rows[0]["size"] * 0.5
    left = min(r["bbox"][0] for r in rows)
    pitches = [b["origin_y"] - a["origin_y"] for a, b in zip(rows, rows[1:])]
    pitch = float(np.median(pitches)) if pitches else rows[0]["size"] * 1.2
    lines, prev = [], None
    for r in rows:
        if prev is not None and pitch > 0:
            for _ in range(int(round((r["origin_y"] - prev["origin_y"]) / pitch)) - 1):
                lines.append("")
        line = ""
        for p in sorted(r["parts"], key=lambda p: p["bbox"][0]):
            col = int(round((p["bbox"][0] - left) / cw))
            t = p["text"].rstrip("\n")
            # leading spaces inside the span are already part of the text
            if len(line) < col:
                line += " " * (col - len(line))
            elif line and not line.endswith(" ") and not t.startswith(" "):
                line += " "
            line += t
        lines.append(line.rstrip())
        prev = r
    return "\n".join(lines)


def side_by_side_code(body: str) -> bool:
    """Two REPL sessions next to each other end up in one block as two columns: a second column
    starts at the same place on two or more lines, and holds a prompt. (Help screens and result
    tables have aligned columns too, but no prompt in them.)"""
    starts, prompts, inside = Counter(), set(), False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        m = re.match(r"^(.*\S)( {3,})(\S.*)$", line) if inside else None
        if m and not m.group(3).startswith(COMMENT_START):
            col = len(m.group(1)) + len(m.group(2))
            starts[col] += 1
            if REPL_PROMPT.match(m.group(3)):
                prompts.add(col)
    return any(n >= 2 and col in prompts for col, n in starts.items())


def is_url_piece(text, links):
    t = text.strip().rstrip(".,;:)")
    return len(t) >= 3 and " " not in t and any(t in l for l in links)


def join_url_rows(rows, links):
    """A monospace URL wrapped onto the next line continues the previous line, it is not code."""
    out = []
    for r in rows:
        spans = [sp for p in r["parts"] for sp in p["spans"] if sp["text"].strip()]
        if out and spans and all(is_mono(sp) for sp in spans) and is_url_piece(r["text"], links):
            last = copy.deepcopy(out[-1])
            lspans = [sp for p in last["parts"] for sp in p["spans"] if sp["text"].strip()]
            if lspans and is_mono(lspans[-1]) and is_url_piece(lspans[-1]["text"].strip() + r["text"].strip(), links):
                lspans[-1]["text"] = lspans[-1]["text"].rstrip() + r["text"].strip()
                last["text"] = last["text"].rstrip() + r["text"].strip()
                out[-1] = last
                continue
        out.append(r)
    return out


def build_draft(rows, markers, links=()):
    """Rows -> markdown-ish text. markers: [(x_center, y_center)] of bullet glyph drawings;
    links: the page's link targets, so that monospace URLs are not taken for code."""
    rows = join_url_rows(rows, links) if links else rows
    item_x = sorted({round(r["bbox"][0]) for r in rows})
    levels = []
    for v in item_x:
        if not levels or v - levels[-1] > 6:
            levels.append(v)

    def level_of(x):
        return max(0, sum(1 for v in levels if v <= x + 3) - 1)

    info = []
    for r in rows:
        x0, y0, x1, y1 = r["bbox"]
        yc = (y0 + y1) / 2
        raw = re.sub(r"\s+", " ", r["text"]).strip()
        bullet = any(abs(my - yc) < 0.6 * r["size"] and 0 < x0 - mx < 3.2 * r["size"] for mx, my in markers)
        char_bullet = raw[:1] in BULLET_CHARS and raw[1:2] == " "
        info.append({"bullet": bullet or char_bullet, "char_bullet": char_bullet,
                     "code": (not bullet) and is_code_row(r) and not is_url_piece(raw, links),
                     "comment": raw.startswith(COMMENT_START)})

    def close(i, j):
        a, b = rows[i], rows[j]
        return 0 <= b["bbox"][1] - a["bbox"][1] and b["bbox"][1] - a["bbox"][3] < 1.3 * a["size"]

    changed = True
    while changed:                              # comment lines and sandwiched lines join the code
        changed = False
        for i, r in enumerate(rows):
            if info[i]["code"] or info[i]["bullet"]:
                continue
            prev_code = i > 0 and info[i - 1]["code"] and close(i - 1, i)
            next_code = i + 1 < len(rows) and info[i + 1]["code"] and close(i, i + 1)
            if (info[i]["comment"] and (prev_code or next_code)) or (prev_code and next_code):
                info[i]["code"] = True
                changed = True

    out, i, base_level, prev = [], 0, None, None
    while i < len(rows):
        r = rows[i]
        if info[i]["code"]:
            j = i
            while j + 1 < len(rows) and info[j + 1]["code"] and \
                    rows[j + 1]["bbox"][1] - rows[j]["bbox"][3] < 2.2 * rows[j]["size"] and \
                    rows[j + 1]["bbox"][1] >= rows[j]["bbox"][1] - 1:
                j += 1
            out += ["", "```", code_text(rows[i:j + 1]), "```", ""]
            prev = None
            i = j + 1
            continue
        text = ""
        for p in r["parts"]:
            text += (" " if text else "") + prose_markup(p["spans"])
        text = re.sub(r"[ \t]+", " ", text).strip()
        x0, y0, x1, y1 = r["bbox"]
        if info[i]["char_bullet"]:
            text = re.sub(r"^\W\s+", "", text, count=1)
        if info[i]["bullet"]:
            lvl = level_of(x0)
            base_level = lvl if base_level is None else min(base_level, lvl)
            out.append(("  " * max(0, lvl - base_level)) + "- " + text)
        elif prev is not None and abs(prev["tx"] - x0) < 3 and y0 - prev["bbox"][3] < 0.9 * r["size"] \
                and out and out[-1]:
            out[-1] = out[-1] + " " + text
        else:
            if out and out[-1] and not out[-1].lstrip().startswith("- "):
                out.append("")
            out.append(text)
        prev = {"tx": x0, "bbox": r["bbox"]}
        i += 1
    text = "\n".join(out)
    text = re.sub(r"`(https?://[^`\s]+?)([.,;:]?)`", r"<\1>\2", text)     # a URL is a link, not code
    text = re.sub(r"<(https?://\S+?)> ?`([^`\s]+?)`",                      # a wrapped tail of the same link
                  lambda m: f"<{m[1]}{m[2]}>" if m[1] + m[2] in links else m[0], text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# --------------------------------------------------------------------------
# page analysis
# --------------------------------------------------------------------------

def template_of(doc, n_sample=48):
    """Per-pixel median of a sample of pages = background, logo, header and footer."""
    n = len(doc)
    if n < 8:
        return None
    idx = sorted(set(int(round(i)) for i in np.linspace(0, n - 1, min(n, n_sample))))
    base = doc[idx[0]].rect
    stack = []
    for i in idx:
        p = doc[i]
        if abs(p.rect.width - base.width) > 1 or abs(p.rect.height - base.height) > 1:
            continue
        stack.append(render(p, ANALYSIS_WIDTH))
    if len(stack) < 6:
        return None
    return np.median(np.stack(stack), axis=0).astype(np.uint8)


def flat_template(img):
    """Fallback template: the dominant colour of the page."""
    q = (img // 8).reshape(-1, 3)
    keys = q[:, 0].astype(np.int32) * 1024 + q[:, 1] * 32 + q[:, 2]
    k = np.bincount(keys).argmax()
    col = np.array([(k // 1024) * 8 + 4, ((k // 32) % 32) * 8 + 4, (k % 32) * 8 + 4], dtype=np.uint8)
    return np.broadcast_to(col, img.shape).copy()


def analyse_page(page, template, debug=False):
    img = render(page, ANALYSIS_WIDTH)
    h, w, _ = img.shape
    tpl = template if template is not None and template.shape == img.shape else flat_template(img)
    scale = w / page.rect.width                              # px per pt
    diff = np.abs(img.astype(np.int16) - tpl.astype(np.int16)).max(axis=2)
    ink = diff > INK_THRESHOLD

    segs = page_segments(page)
    text_mask = np.zeros((h, w), dtype=bool)
    for s in segs:
        x0, y0, x1, y1 = [v * scale for v in s["bbox"]]
        text_mask[max(0, int(y0) - 2):min(h, int(y1) + 3), max(0, int(x0) - 2):min(w, int(x1) + 3)] = True

    gray = img.astype(np.int16).mean(axis=2)
    ex = np.zeros((h, w), dtype=bool)
    ey = np.zeros((h, w), dtype=bool)
    ex[:, 1:] = np.abs(gray[:, 1:] - gray[:, :-1]) > EDGE_THRESHOLD     # vertical edges
    ey[1:, :] = np.abs(gray[1:, :] - gray[:-1, :]) > EDGE_THRESHOLD     # horizontal edges
    run = max(8, int(14 * scale))
    straight = long_runs(ex, run, 0) | long_runs(ey, run, 1)
    near_ink = dilate(ink, 2)
    texture = (ex | ey) & ~dilate(straight, 1) & ~text_mask & near_ink
    resid = ink & ~text_mask

    # thin horizontal rules (table rules): long ink runs with no ink right above and below
    hrun = long_runs(resid, max(20, int(0.2 * w)), 1)
    thin = hrun.copy()
    thin[4:, :] &= ~resid[:-4, :]
    thin[:-4, :] &= ~resid[4:, :]
    rule_rows = np.flatnonzero(thin.sum(axis=1) >= 0.2 * w)
    hrules = []                                  # (y, x0, x1) in pt, one per rule
    for r in rule_rows:
        xs = np.flatnonzero(thin[r])
        if hrules and r / scale - hrules[-1][0] <= 3 / scale + 0.01:
            continue
        hrules.append((r / scale, xs[0] / scale, xs[-1] / scale))

    # connected components of the non-text ink
    gh, gw = h // CELL, w // CELL
    cells = resid[:gh * CELL, :gw * CELL].reshape(gh, CELL, gw, CELL).sum(axis=(1, 3))
    tex_cells = texture[:gh * CELL, :gw * CELL].reshape(gh, CELL, gw, CELL).sum(axis=(1, 3))
    str_cells = (straight & near_ink)[:gh * CELL, :gw * CELL].reshape(gh, CELL, gw, CELL).sum(axis=(1, 3))
    active = cells >= 2
    comps = []
    for comp in components(active):
        rs = [r for r, _ in comp]
        cs = [c for _, c in comp]
        r0, r1, c0, c1 = min(rs), max(rs) + 1, min(cs), max(cs) + 1
        box_pt = [c0 * CELL / scale, r0 * CELL / scale, c1 * CELL / scale, r1 * CELL / scale]
        wpt, hpt = box_pt[2] - box_pt[0], box_pt[3] - box_pt[1]
        tex = int(sum(tex_cells[r, c] for r, c in comp))
        strt = int(sum(str_cells[r, c] for r, c in comp))
        inkpx = int(sum(cells[r, c] for r, c in comp))
        if max(wpt, hpt) <= 20:
            kind = "marker"
        elif tex <= max(40, 0.012 * (wpt + hpt) * 2 * scale * 4):
            kind = "rule" if min(wpt, hpt) <= 6 else "box"
        else:
            kind = "figure"
        comps.append({"bbox": [round(v, 1) for v in box_pt], "kind": kind, "texture": tex,
                      "straight": strt, "ink": inkpx})
    packed = np.packbits(ink)
    return {"segs": segs, "comps": comps, "ink": packed, "ink_shape": ink.shape,
            "ink_count": int(ink.sum()), "resid_count": int(resid.sum()), "hrules": hrules,
            "scale": scale, "thumb": hashlib.sha1(
                (img[::8, ::8] // 32).tobytes()).hexdigest()[:16]}


def is_footnote_mark(mark: str, lower_lines: list[str]) -> bool:
    """A short superscript that also starts a line further down is a footnote or affiliation marker."""
    return (len(mark) <= 2 and (mark.isdigit() or mark in "*†‡§")
            and any(l.startswith(mark) for l in lower_lines if len(l) > len(mark)))


def unpack(a):
    return np.unpackbits(a["ink"])[: a["ink_shape"][0] * a["ink_shape"][1]].reshape(a["ink_shape"]).astype(bool)


def subsumed(a, b, strict_words):
    """True if page a adds nothing over page b (words and ink are contained in b)."""
    wa, wb = a["words"], b["words"]
    missing = sum((wa - wb).values())
    if strict_words:
        if missing:
            return False
    else:
        extra = [w for w in (wa - wb) if not re.fullmatch(r"[\d/.\-–]+", w)]
        if extra:
            return False
    if a["ink_shape"] != b["ink_shape"]:
        return False
    ia, ib = unpack(a), dilate(unpack(b), 2)
    lost = int((ia & ~ib).sum())
    return lost <= max(60, 0.02 * a["ink_count"])


# --------------------------------------------------------------------------
# main triage
# --------------------------------------------------------------------------

def merge_boxes(boxes, gap):
    boxes = [list(b) for b in boxes]
    changed = True
    while changed:
        changed = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if a[0] - gap <= b[2] and b[0] - gap <= a[2] and a[1] - gap <= b[3] and b[1] - gap <= a[3]:
                    boxes[i] = [min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])]
                    del boxes[j]
                    changed = True
                    break
            if changed:
                break
    return boxes


def triage(pdf_path: Path, out: Path, view_all=False, debug=False):
    doc = fitz.open(str(pdf_path))
    n = len(doc)
    out.mkdir(parents=True, exist_ok=True)
    for sub in ("pages", "figures"):
        d = out / sub
        if d.exists():
            for f in d.iterdir():
                f.unlink()

    MEASURED_MONO.clear()
    measure_fonts(doc)
    template = template_of(doc)
    pages = []
    for i in range(n):
        a = analyse_page(doc[i], template, debug)
        a["index"] = i
        a["label"] = decode_label(doc[i].get_label())
        # identifies the same page in another source (prepare.py reports duplicates)
        a["page_hash"] = hashlib.sha1((doc[i].get_text() + a["thumb"]).encode()).hexdigest()[:16]
        pages.append(a)

    # template text: identical text at an identical position on many pages
    sig = Counter()
    for a in pages:
        for s in {seg_signature(s) for s in a["segs"]}:
            sig[s] += 1
    labels = [a["label"] for a in pages]
    # labels only help when consecutive pages share one (animation steps of one slide)
    have_labels = any(labels) and len(set(labels)) > 1 and \
        any(labels[i] == labels[i - 1] for i in range(1, n))
    n_units_guess = len([1 for i in range(n) if i == 0 or labels[i] != labels[i - 1]]) if have_labels else n
    min_rep = max(4, int(0.4 * n))
    sizes = Counter()
    for a in pages:
        for s in a["segs"]:
            sizes[round(s["size"], 1)] += len(s["text"])
    body_size = sizes.most_common(1)[0][0] if sizes else 10.0
    # header/footer zones: small text at a position used on most pages
    zone = Counter()
    for a in pages:
        H = doc[a["index"]].rect.height
        for key in {(round(s["bbox"][1]), round(s["size"] * 2)) for s in a["segs"]
                    if s["size"] <= 0.85 * body_size and (s["bbox"][3] < 0.13 * H or s["bbox"][1] > 0.90 * H)}:
            zone[key] += 1
    zones = {k for k, v in zone.items() if v >= 0.5 * n and n >= 8}
    for a in pages:
        body, header = [], []
        for s in a["segs"]:
            if sig[seg_signature(s)] >= min_rep and n >= 8:
                continue
            if (round(s["bbox"][1]), round(s["size"] * 2)) in zones:
                header.append(s["text"].strip())
                continue
            body.append(s)
        a["body"] = body
        a["header"] = header
        a["words"] = words_of(body)

    # ---- group pages into logical units
    groups = []
    if have_labels:
        for i in range(n):
            if groups and labels[i] == labels[i - 1]:
                groups[-1].append(i)
            else:
                groups.append([i])
        mode = "labels"
    else:
        groups = [[0]] if n else []
        for i in range(1, n):
            prev, cur = pages[i - 1], pages[i]
            if (prev["words"] or prev["resid_count"] > 200) and subsumed(prev, cur, strict_words=False):
                groups[-1].append(i)
            else:
                groups.append([i])
        mode = "heuristic"

    units = []
    for gi, g in enumerate(groups, 1):
        kept = [g[-1]]
        for i in reversed(g[:-1]):
            if not any(subsumed(pages[i], pages[k], strict_words=(mode == "labels")) for k in kept):
                kept.insert(0, i)
        for k, i in enumerate(kept, 1):
            uid = f"s{gi}" if len(kept) == 1 else f"s{gi}.{k}"
            units.append({"id": uid, "page": i, "group": g, "variant": len(kept) > 1})

    # ---- per unit: draft, flags, renders
    result = []
    flagged = Counter()
    for u in units:
        a = pages[u["page"]]
        page = doc[u["page"]]
        W, H = page.rect.width, page.rect.height
        rows = build_rows(a["body"])
        # title: first row near the top that is larger than body text
        title = ""
        a_title_rows = []
        top_rows = sorted(rows, key=lambda r: r["bbox"][1])
        if top_rows:
            t = top_rows[0]
            if t["bbox"][1] < 0.25 * H and (t["size"] >= 1.08 * body_size or t["bbox"][1] < 0.14 * H) \
                    and t["mono"] < 0.5:
                title = re.sub(r"\s+", " ", t["text"]).strip()
                a_title_rows.append(t)
                rows = [r for r in rows if r is not t]
                more = [r for r in rows if abs(r["size"] - t["size"]) < 0.2 and
                        0 <= r["bbox"][1] - t["bbox"][3] < 0.5 * t["size"] and r["mono"] < 0.5]
                for r in more[:1]:
                    title += " " + re.sub(r"\s+", " ", r["text"]).strip()
                    a_title_rows.append(r)
                    rows = [x for x in rows if x is not r]
        ordered, columns = order_columns(rows, W)
        if ordered is None or not columns:
            title_ids = {id(p) for r in a_title_rows for p in r["parts"]}
            rows = build_rows([s for s in a["body"] if id(s) not in title_ids], merge_mono=True)
            ordered = sorted(rows, key=lambda r: (r["bbox"][1], r["bbox"][0]))
        markers = [((c["bbox"][0] + c["bbox"][2]) / 2, (c["bbox"][1] + c["bbox"][3]) / 2)
                   for c in a["comps"] if c["kind"] == "marker"]
        links = sorted({l["uri"] for l in page.get_links() if l.get("uri")})
        body = build_draft(ordered, markers, links)

        flags = []
        text_chars = sum(len(s["text"].strip()) for s in a["body"])
        # symbols inside code (`~>`, `δ` in a string, `≢` in a comment) and footnote markers are not
        # formulas: math evidence counts only where it shows up in the prose of the draft
        prose = re.sub(r"`[^`\n]*`", "", re.sub(r"(?s)```.*?```", "", body))
        math_font_chars = sum(len(t) for s in a["body"] for sp in s["spans"] if MATH_FONT.search(sp["font"])
                              for t in [sp["text"].strip()] if t and t in prose)
        math_uni = sum(1 for ch in prose if ch in MATH_CHARS)
        sup = sum(1 for s in a["body"] for sp in s["spans"] if sp["flags"] & 1 and sp["text"].strip()
                  and not is_footnote_mark(sp["text"].strip(), [t["text"].strip() for t in a["body"]
                                                                if t["bbox"][1] >= s["bbox"][3] - 1]))
        if math_font_chars >= 2 or math_uni >= 2 or sup >= 1:
            flags.append("math")
        figs = [c for c in a["comps"] if c["kind"] == "figure"]
        if figs:
            flags.append("graphic")
        images = [im for im in page.get_image_info(xrefs=True)
                  if im.get("xref", 0) > 0 and (im["bbox"][2] - im["bbox"][0]) > 12
                  and (im["bbox"][3] - im["bbox"][1]) > 12]
        fig_boxes = [c["bbox"] for c in figs]
        real_images = [im for im in images if any(
            not (im["bbox"][2] < b[0] or b[2] < im["bbox"][0] or im["bbox"][3] < b[1] or b[3] < im["bbox"][1])
            for b in fig_boxes)]
        if real_images:
            flags.append("image")
        stacked = False
        for x in range(len(real_images)):
            for y in range(x + 1, len(real_images)):
                A, B = fitz.Rect(real_images[x]["bbox"]), fitz.Rect(real_images[y]["bbox"])
                inter = A & B
                if not inter.is_empty and inter.get_area() > 0.5 * min(A.get_area(), B.get_area()):
                    stacked = True
        if stacked:
            flags.append("stacked")
        free_rules = [r for r in a["hrules"] if not any(
            im["bbox"][0] - 3 <= r[1] and r[2] <= im["bbox"][2] + 3 and im["bbox"][1] - 3 <= r[0] <= im["bbox"][3] + 3
            for im in real_images)]
        if len(free_rules) >= 2:
            flags.append("table")
        if columns or side_by_side_code(body):
            flags.append("layout")
        if any(s["rotated"] for s in a["body"]):
            flags.append("layout")
        if any(s["bad_chars"] or s["type3"] for s in a["body"]):
            flags.append("encoding")
        if text_chars < 15 and a["resid_count"] > 400:
            flags.append("no-text")
        annots = []
        for an in page.annots() or []:
            c = (an.info or {}).get("content", "").strip()
            if c:
                annots.append(c)
        if annots:
            flags.append("annot")
        if u["variant"]:
            flags.append("variant")
        flags = list(dict.fromkeys(flags))
        needs_view = bool(flags) or view_all

        figures = []
        if figs:
            boxes = merge_boxes(fig_boxes, gap=36)
            for k, b in enumerate(sorted(boxes, key=lambda b: (b[1], b[0])), 1):
                bx = list(b)
                for _ in range(6):                  # pull in short labels next to the figure
                    grown = False
                    for r in a["body"]:
                        rb = r["bbox"]
                        if rb[2] - rb[0] > 0.4 * W or id(r) in {id(p) for t in a_title_rows for p in t["parts"]}:
                            continue
                        inside = rb[0] >= bx[0] and rb[2] <= bx[2] and rb[1] >= bx[1] and rb[3] <= bx[3]
                        near = rb[0] < bx[2] + 14 and rb[2] > bx[0] - 14 and rb[1] < bx[3] + 14 and rb[3] > bx[1] - 14
                        if near and not inside:
                            bx = [min(bx[0], rb[0]), min(bx[1], rb[1]), max(bx[2], rb[2]), max(bx[3], rb[3])]
                            grown = True
                    if not grown:
                        break
                clip = fitz.Rect(bx[0] - 5, bx[1] - 5, bx[2] + 5, bx[3] + 5) & page.rect
                if clip.width < 20 or clip.height < 12:
                    continue
                name = f"figures/p{u['page'] + 1:03d}-f{k}.png"
                width = int(min(FIGURE_WIDTH, max(300, clip.width * 3.2)))
                save_png(page, out / name, width, clip)
                figures.append({"file": name,
                                "bbox": [round(clip.x0 / W, 3), round(clip.y0 / H, 3),
                                         round(clip.x1 / W, 3), round(clip.y1 / H, 3)]})
        if stacked:
            for im in real_images:
                try:
                    data = doc.extract_image(im["xref"])
                    name = f"figures/p{u['page'] + 1:03d}-x{im['xref']}.{data['ext']}"
                    (out / "figures").mkdir(exist_ok=True)
                    (out / name).write_bytes(data["image"])
                    figures.append({"file": name, "layer": True})
                except Exception:
                    pass
        view = None
        if needs_view:
            view = f"pages/p{u['page'] + 1:03d}.png"
            save_png(page, out / view, VIEW_WIDTH)
        for f in flags:
            flagged[f] += 1

        fp = hashlib.sha1((title + "\n" + body + "\n" + a["thumb"]).encode()).hexdigest()[:16]
        result.append({
            "id": u["id"], "page": u["page"] + 1,
            "pages": [u["group"][0] + 1, u["group"][-1] + 1], "label": a["label"],
            "title": title, "flags": flags, "view": view, "figures": figures,
            "links": links, "annots": annots, "header": a["header"], "text": body,
            "fingerprint": fp,
            "debug": [c for c in a["comps"] if c["kind"] != "marker"] if debug else None,
        })

    doc.close()
    meta = {"source": pdf_path.name, "kind": "pdf", "physical_pages": n, "units": len(result),
            "grouping": mode, "needs_view": sum(1 for r in result if r["view"]),
            "flags": dict(flagged), "body_font_size": body_size,
            "page_hashes": [a["page_hash"] for a in pages]}
    (out / "extract.json").write_text(json.dumps({"meta": meta, "units": result}, ensure_ascii=False, indent=1))
    (out / "draft.md").write_text(draft_markdown(meta, result))
    return meta, result


def unit_header(u):
    p0, p1 = u["pages"]
    pg = f"p{p0}" if p0 == p1 else f"p{p0}-{p1}"
    title = u["title"] or "(no title)"
    return f"## {u['id']} · {pg} · {title}"


def unit_block(u, status=None):
    lines = [unit_header(u)]
    if status is None:
        status = f"TODO view {u['view']}" if u["view"] else "auto"
    lines.append(f"<!-- status: {status} -->")
    if u["flags"]:
        lines.append(f"<!-- flags: {', '.join(u['flags'])} -->")
    for f in u["figures"]:
        lines.append(f"<!-- figure: {f['file']}{' (raw layer)' if f.get('layer') else ''} -->")
    if u["header"]:
        lines.append(f"<!-- header: {' | '.join(u['header'])} -->")
    for a in u["annots"]:
        lines.append(f"<!-- annotation: {a} -->")
    lines.append("")
    if u["text"]:
        lines.append(u["text"])
        lines.append("")
    if u["links"]:
        lines.append("Links: " + ", ".join(f"<{l}>" for l in u["links"]))
        lines.append("")
    return "\n".join(lines)


def draft_markdown(meta, units):
    head = [f"# {meta['source']}", "",
            f"<!-- {meta['physical_pages']} pages, {meta['units']} units, grouping: {meta['grouping']} -->", ""]
    return "\n".join(head) + "\n" + "\n".join(unit_block(u) for u in units)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("triage")
    t.add_argument("pdf")
    t.add_argument("--out", required=True)
    t.add_argument("--view-all", action="store_true")
    t.add_argument("--debug", action="store_true")
    p = sub.add_parser("page")
    p.add_argument("pdf")
    p.add_argument("page", type=int)
    p.add_argument("-o", "--output", required=True)
    p.add_argument("--width", type=int, default=FIGURE_WIDTH)
    c = sub.add_parser("crop")
    c.add_argument("pdf")
    c.add_argument("page", type=int)
    c.add_argument("box", type=float, nargs=4, metavar=("X0", "Y0", "X1", "Y1"))
    c.add_argument("-o", "--output", required=True)
    c.add_argument("--width", type=int, default=FIGURE_WIDTH)
    args = ap.parse_args()

    if args.cmd == "triage":
        meta, units = triage(Path(args.pdf), Path(args.out), args.view_all, args.debug)
        print(json.dumps(meta, ensure_ascii=False))
        return
    doc = fitz.open(args.pdf)
    if not 1 <= args.page <= len(doc):
        sys.exit(f"page {args.page} out of range (1-{len(doc)})")
    page = doc[args.page - 1]
    clip = None
    if args.cmd == "crop":
        x0, y0, x1, y1 = args.box
        if not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
            sys.exit("box must be fractions with 0 <= X0 < X1 <= 1 and 0 <= Y0 < Y1 <= 1")
        r = page.rect
        clip = fitz.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height, r.x0 + x1 * r.width, r.y0 + y1 * r.height)
    save_png(page, Path(args.output), args.width, clip)
    print(args.output)


if __name__ == "__main__":
    main()
