#!/usr/bin/env python3
"""Build a layout primer to pass as the reference image.

Text alone does not reliably pin a grid — the model falls back to its own
grid prior and returns 2x4 when asked for 4x4. A reference image that IS
the target layout makes image and text reinforce each other, which is how
src/ai/flows/explore-frame.ts pins the cell count.

With a subject image, the subject is tiled COLSxROWS. Without one, flat
cells with crisp shared borders carry the layout on their own.
"""
import argparse, re
from PIL import Image, ImageDraw

SWATCHES = [(232, 236, 244), (208, 216, 232), (244, 238, 226), (220, 228, 214),
            (238, 226, 232), (214, 222, 236), (240, 234, 216), (224, 232, 228)]


def parse_grid(s):
    m = re.fullmatch(r"\s*(\d+)\s*[xX*]\s*(\d+)\s*", s or "")
    if not m:
        raise SystemExit(f"--grid must look like 3x3 (got {s!r})")
    return int(m.group(1)), int(m.group(2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", required=True, help="COLSxROWS, e.g. 4x4")
    ap.add_argument("--out", default="primer.png")
    ap.add_argument("--subject", default="", help="optional image to tile into every cell")
    ap.add_argument("--size", type=int, default=1024)
    ap.add_argument("--green", action="store_true",
                    help="flat #00FF00 cells, for transparent mode")
    args = ap.parse_args()

    cols, rows = parse_grid(args.grid)
    # Square canvas whose side divides evenly by BOTH axes, so no cell is a
    # pixel wider than its neighbour and the model sees a clean lattice.
    step = max(1, args.size // max(cols, rows))
    side = step * max(cols, rows)
    cw, ch = side // cols, side // rows
    canvas = Image.new("RGB", (side, side), (255, 255, 255))

    subject = None
    if args.subject:
        subject = Image.open(args.subject).convert("RGB")
        k = max(cw / subject.width, ch / subject.height)
        subject = subject.resize((max(1, round(subject.width * k)),
                                  max(1, round(subject.height * k))), Image.LANCZOS)
        left = (subject.width - cw) // 2
        top = (subject.height - ch) // 2
        subject = subject.crop((left, top, left + cw, top + ch))

    d = ImageDraw.Draw(canvas)
    for i in range(cols * rows):
        c, r = i % cols, i // cols
        box = (c * cw, r * ch, (c + 1) * cw, (r + 1) * ch)
        if subject is not None:
            canvas.paste(subject, (box[0], box[1]))
        elif args.green:
            d.rectangle(box, fill=(0, 255, 0))
        else:
            d.rectangle(box, fill=SWATCHES[i % len(SWATCHES)])
    if subject is None and args.green:
        # Flat green everywhere would read as one empty frame, so mark the
        # lattice with thin seams the model can count.
        for c in range(1, cols):
            d.line([(c * cw, 0), (c * cw, side)], fill=(255, 255, 255), width=2)
        for r in range(1, rows):
            d.line([(0, r * ch), (side, r * ch)], fill=(255, 255, 255), width=2)

    canvas.save(args.out)
    print(f"{args.out}  {side}x{side}  {cols}x{rows} lattice  cell {cw}x{ch}"
          f"{'  (subject tiled)' if subject is not None else ''}")
    print(f"  pass this as the reference image alongside the prompt")


if __name__ == "__main__":
    main()
