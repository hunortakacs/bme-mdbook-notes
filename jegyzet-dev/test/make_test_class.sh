#!/usr/bin/env bash
# Builds the synthetic "kvantum" test deck and a copy without page labels,
# then puts both into <target>/kvantum/res/.
#   usage: jegyzet-dev/test/make_test_class.sh <target-folder>
# Needs: pdflatex with beamer, tikz, booktabs, listings, helvet, courier;
#        python3 with pymupdf, numpy, matplotlib, pillow.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
target="$(mkdir -p "$1" && cd "$1" && pwd)"
work="$(mktemp -d)"
cp "$here/deck.tex" "$here/formula.tex" "$work/"
cd "$work"

python3 - <<'PY'
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from PIL import Image, ImageDraw
x = np.linspace(0, 6, 200)
for name, f, t in (("plotA", np.sin, "sin"), ("plotB", np.cos, "cos")):
    plt.figure(figsize=(4, 2.6)); plt.plot(x, f(x)); plt.title(t + "(x)"); plt.grid(True)
    plt.savefig(name + ".png", dpi=120); plt.close()
im = Image.new("RGB", (120, 60), "white"); d = ImageDraw.Draw(im)
d.ellipse((5, 5, 55, 55), fill=(30, 60, 160)); d.text((62, 22), "BME", fill="black"); im.save("logo.png")
PY

latex() { pdflatex -interaction=batchmode "$1" >/dev/null 2>&1 || true; }
latex formula.tex
test -f formula.pdf || { grep -m3 -A2 '^!' formula.log; echo "pdflatex failed, see $work/formula.log"; exit 1; }
# Crop the article page to the formula, as a pasted formula image would be.
python3 -c "
import pymupdf as f
p = f.open('formula.pdf')[0]; r = f.Rect()
for _, b in p.get_bboxlog(): r |= f.Rect(b)
p.get_pixmap(dpi=200, clip=r + (-2, -2, 2, 2)).save('formula.png')"
latex deck.tex; latex deck.tex
test -f deck.pdf || { grep -m3 -A2 '^!' deck.log; echo "pdflatex failed, see $work/deck.log"; exit 1; }

mkdir -p "$target/kvantum/res"
cp deck.pdf "$target/kvantum/res/kvantum-ea03.pdf"
# Same deck as an exporter without page labels would produce it, plus one page
# with two pictures stacked on top of each other (an animation flattened to one page).
python3 - "$target/kvantum/res/kvantum-ea03-export.pdf" <<'PY'
import sys, pymupdf as f
d = f.open("deck.pdf"); d.set_page_labels([])
pg = d.new_page(width=d[0].rect.width, height=d[0].rect.height)
pg.insert_text((30, 40), "Rétegzett animáció egy oldalon", fontsize=14)
r = f.Rect(60, 60, 300, 220)
pg.insert_image(r, filename="plotA.png"); pg.insert_image(r, filename="plotB.png")
d.save(sys.argv[1])
PY
echo "test class written to $target/kvantum/res"
