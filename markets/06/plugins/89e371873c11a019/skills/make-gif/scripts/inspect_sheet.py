#!/usr/bin/env python3
"""Answer one question: is this image a sprite sheet, or a single picture?

It deliberately does NOT report the layout. Cell-similarity scoring picks
the coarsest slice that still looks continuous — it called a real 4x4 sheet
"4x1" — and recovering the true layout would need seam detection. Counting
columns and rows is something you can just LOOK at; deciding whether a
picture is secretly one image is what benefits from a number.

Run this on every generated image BEFORE encoding. The model cannot
reliably tell a grid from a single picture by looking, and the cost of
getting it wrong is a GIF that is either frozen or a jumpy slideshow.

    python3 inspect_sheet.py IMAGE

Exit code 0 = a grid was found (the layout is printed as COLSxROWS).
Exit code 1 = not a grid; regenerate as a sprite sheet.

How it decides: in a real sheet, neighbouring cells show the same subject
a moment apart, so they are SIMILAR. Slicing a single picture into a grid
gives disjoint crops of different parts of a scene, which are wildly
different. Measured over real sheets and single pictures:

    real sheets (4x4, 4x3, controlled)   mean neighbour diff   4.8 - 23.6
    single picture sliced 4x4            mean neighbour diff        68.7
"""
import sys

try:
    from PIL import Image, ImageChops, ImageStat
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")

MAX_SIDE = 6          # 6x6 = 36 frames is past anything useful
GRID_THRESHOLD = 40.0 # below this, neighbouring cells look like one motion
SAMPLE = 96           # compare cells downscaled; shape matters, detail does not


def cells(img, cols, rows):
    cw, ch = img.width // cols, img.height // rows
    out = []
    for r in range(rows):
        for c in range(cols):
            out.append(
                img.crop((c * cw, r * ch, (c + 1) * cw, (r + 1) * ch))
                   .resize((SAMPLE, SAMPLE), Image.BILINEAR)
            )
    return out


def neighbour_diff(frames):
    """Mean difference between consecutive cells. Low = one motion."""
    diffs = [
        ImageStat.Stat(ImageChops.difference(frames[i], frames[i + 1])).mean[0]
        for i in range(len(frames) - 1)
    ]
    return sum(diffs) / len(diffs)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: inspect_sheet.py IMAGE")
    img = Image.open(sys.argv[1]).convert("RGB")

    scored = []
    for cols in range(1, MAX_SIDE + 1):
        for rows in range(1, MAX_SIDE + 1):
            if cols * rows < 4:            # fewer than 4 frames is not an animation
                continue
            if img.width // cols < 24 or img.height // rows < 24:
                continue
            scored.append((neighbour_diff(cells(img, cols, rows)), cols, rows))

    if not scored:
        print("NOT A GRID — image too small to hold frames", file=sys.stderr)
        return 1

    best = min(t[0] for t in scored)

    if best > GRID_THRESHOLD:
        print("NOT_A_GRID")
        print(
            f"NOT A GRID — even the most forgiving slicing leaves neighbouring regions "
            f"differing by {best:.0f}/255, far above {GRID_THRESHOLD:.0f}. This is ONE PICTURE, "
            "not a sheet of frames.\n"
            "Regenerate with a prompt starting \"A NxN grid of TOTAL panels of ...\". "
            "Do NOT pan, zoom or bounce this image — that is not an animation.",
            file=sys.stderr,
        )
        return 1

    print("GRID")
    print(
        f"Looks like a sprite sheet (best neighbour difference {best:.1f}/255). "
        "Now COUNT the columns and rows yourself and pass them as --grid COLSxROWS — "
        "this check cannot tell you the layout, only that frames are present.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
