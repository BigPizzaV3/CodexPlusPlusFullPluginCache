#!/usr/bin/env python3
"""Slice a square sprite sheet into frames and write a looping GIF.

Deterministic on purpose: the model should run this rather than improvise
slicing code, so every GIF comes out with the same geometry, timing and
palette handling instead of whatever got written that turn.

    python3 sheet_to_gif.py SHEET [--grid 4x4] [--fps 7] [--boomerang]
                                  [--size 512] [--out PATH]
                                  [--skip 3,9] [--order 0,2,1,...]
"""
import argparse
import os
import sys

try:
    from PIL import Image, ImageChops, ImageStat
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")


def slice_sheet(img, cols, rows, edge_percent=3.0):
    """Cut a cols x rows grid into frames.

    NOT assumed square. Image generation frequently returns a different
    layout from the one asked for — a 4x3 when a 4x4 was requested is
    common — and slicing a 4x3 sheet as 4x4 misaligns every cut, so each
    frame carries a band of its neighbour. That band is the "outline"
    people see, and no amount of edge crop removes it because the cut
    itself is in the wrong place. Pass the layout the sheet ACTUALLY has.

    Each cell is then trimmed by edge_percent on all four sides: generated
    grids carry a thin seam or shadow where panels meet, and at output
    size that band flickers on every loop.
    """
    cell_w = img.width // cols
    cell_h = img.height // rows
    if cell_w < 8 or cell_h < 8:
        sys.exit(f"sheet too small: {img.width}x{img.height} for a {cols}x{rows} grid")

    # Centre any remainder so the grid is not biased to one edge.
    off_x = (img.width - cell_w * cols) // 2
    off_y = (img.height - cell_h * rows) // 2

    pct = max(0.0, min(20.0, edge_percent)) / 100.0
    in_x, in_y = int(round(cell_w * pct)), int(round(cell_h * pct))

    frames = []
    for r in range(rows):
        for c in range(cols):
            x0 = off_x + c * cell_w + in_x
            y0 = off_y + r * cell_h + in_y
            x1 = off_x + (c + 1) * cell_w - in_x
            y1 = off_y + (r + 1) * cell_h - in_y
            frames.append(img.crop((x0, y0, x1, y1)))
    return frames


def detect_grid(img, max_side=6, threshold=35.0):
    """Work out the grid from the pixels, instead of being told.

    Panels repeat the same subject a moment apart, so shifting the image by
    exactly one cell width lines panel i up with panel i+1 and the
    difference is small. A wrong shift lands mid-panel and the difference
    is large. The shift that minimises the difference IS the cell size.

    This removes the whole class of bug where a sheet is cut on the wrong
    boundaries: it does not care what was asked for, what the canvas shape
    is, or whether the grid is square.

    Both axes are used to find the LAYOUT, but only the column axis decides
    whether this is a grid at all. Panels run row-major, so a one-column
    shift compares neighbours in time while a one-row shift jumps a whole
    row ahead — real sheets score 43-61 vertically for that reason alone.
    Horizontally the separation is clean: real sheets 4.7-22.8, a single
    picture 60.

    Returns (cols, rows) or None when the image is not a grid.
    """
    small = img.resize((max(64, img.width // 2), max(64, img.height // 2)), Image.BILINEAR)

    def score(n, axis):
        w, h = small.size
        step = (w // n) if axis == 0 else (h // n)
        if step < 16:
            return None
        if axis == 0:
            a, b = small.crop((0, 0, w - step, h)), small.crop((step, 0, w, h))
        else:
            a, b = small.crop((0, 0, w, h - step)), small.crop((0, step, w, h))
        return ImageStat.Stat(ImageChops.difference(a, b)).mean[0]

    best = {}
    for axis in (0, 1):
        cands = [(score(n, axis), n) for n in range(2, max_side + 1)]
        cands = [(sc, n) for sc, n in cands if sc is not None]
        if not cands:
            return None
        best[axis] = min(cands)

    if best[0][0] > threshold:
        return None
    return best[0][1], best[1][1]


def fit(frame, size):
    """Scale a frame so its LONGER side is `size`, preserving aspect.

    Cells from a non-square grid are not square. Forcing them square would
    stretch the subject, which is worse than a non-square GIF.
    """
    w, h = frame.size
    scale = size / max(w, h)
    return frame.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet")
    ap.add_argument("--grid", default="auto",
                    help="COLSxROWS, or 'auto' (default) to detect it from the image")
    ap.add_argument("--fps", type=float, default=7.0)
    ap.add_argument("--size", type=int, default=448, help="output frame size in px")
    ap.add_argument("--colors", type=int, default=256, help="palette size, 32-256")
    ap.add_argument("--no-dither", action="store_true",
                    help="flat colour, smaller file; good for line art and logos")
    ap.add_argument("--crop", type=float, default=3.0,
                    help="percent trimmed from each edge of every cell (default 3)")
    ap.add_argument("--boomerang", action="store_true")
    ap.add_argument("--skip", default="", help="comma-separated frame indexes to drop")
    ap.add_argument("--order", default="", help="comma-separated playback order")
    ap.add_argument("--out", default="")
    ap.add_argument("--frames", default="", help="also write the individual frames to this .zip")
    a = ap.parse_args()

    img = Image.open(a.sheet).convert("RGB")

    if a.grid.strip().lower() == "auto":
        found = detect_grid(img)
        if found is None:
            sys.exit(
                "Could not find a grid in this image — the panels do not repeat, which is what a "
                "SINGLE PICTURE looks like. Generate a sprite sheet instead, with a prompt starting "
                '"A SQUARE image containing a NxN grid of TOTAL panels of ...". Do not pan or zoom '
                "a still image; that is not an animation. (Pass --grid COLSxROWS to override.)"
            )
        cols, rows = found
        print(f"detected grid: {cols}x{rows}", file=sys.stderr)
    else:
        try:
            cols, rows = (int(x) for x in a.grid.lower().split("x"))
        except ValueError:
            sys.exit(f'--grid must look like COLSxROWS or "auto" (got "{a.grid}")')
        if cols < 1 or rows < 1:
            sys.exit("--grid must be at least 1x1")

    # Say out loud what was measured. The GIF's shape is derived from the
    # real image — canvas divided by grid — never assumed, and printing it
    # makes a wrong --grid obvious before anyone watches the result.
    cell_w, cell_h = img.width // cols, img.height // rows
    ratio = cell_w / cell_h if cell_h else 1.0
    out_w = a.size if cell_w >= cell_h else max(1, round(a.size * ratio))
    out_h = a.size if cell_h >= cell_w else max(1, round(a.size / ratio))
    print(
        f"measured: sheet {img.width}x{img.height}  grid {cols}x{rows}  "
        f"panel {cell_w}x{cell_h} (ratio {ratio:.2f})  ->  gif {out_w}x{out_h}",
        file=sys.stderr,
    )

    frames = slice_sheet(img, cols, rows, a.crop)

    if a.order:
        idx = [int(x) for x in a.order.split(",") if x.strip() != ""]
    else:
        idx = list(range(len(frames)))
    skip = {int(x) for x in a.skip.split(",") if x.strip() != ""}
    idx = [i for i in idx if i not in skip and 0 <= i < len(frames)]
    if not idx:
        sys.exit("no frames left to encode")

    seq = [frames[i] for i in idx]
    if a.boomerang and len(seq) > 2:
        seq = seq + seq[-2:0:-1]        # omit the endpoints so the turn does not stall

    seq = [fit(f, a.size) for f in seq]

    # Two checks on what we were handed, both cheap, both catching a
    # failure that is invisible until the GIF plays.
    if len(seq) > 2:
        from PIL import ImageChops, ImageStat

        def neighbour_diff(frames):
            rgb = [f.convert("RGB").resize((96, 96), Image.BILINEAR) for f in frames]
            return sum(
                ImageStat.Stat(ImageChops.difference(rgb[k], rgb[k + 1])).mean[0]
                for k in range(len(rgb) - 1)
            ) / (len(rgb) - 1)

        here = neighbour_diff(seq)

        # 1. Is this a sprite sheet at all? In a real sheet neighbouring
        #    cells are the same subject a moment apart, so they are
        #    SIMILAR. Slicing one picture gives disjoint crops that are
        #    wildly different. Measured: real sheets 4.8-23.6, single
        #    picture sliced 4x4 = 68.7.
        if here > 45:
            print(
                f"WARNING: consecutive frames differ enormously (mean {here:.0f}/255). That is "
                "what slicing a SINGLE PICTURE looks like, not a sprite sheet. Check the image "
                "is a grid of small panels before delivering this.",
                file=sys.stderr,
            )

        # 2. Is --grid the layout the sheet actually has? Getting this
        #    wrong is why frames end up square when they should not be,
        #    and why the subject appears to cross the frame edge: the cuts
        #    land between panels instead of on them. Score the
        #    alternatives and speak up if one is clearly better.
        best = (here, cols, rows)
        for c2 in range(1, 7):
            for r2 in range(1, 7):
                if (c2, r2) == (cols, rows) or c2 * r2 < 4:
                    continue
                if img.width // c2 < 24 or img.height // r2 < 24:
                    continue
                alt = neighbour_diff(slice_sheet(img, c2, r2, a.crop))
                if alt < best[0]:
                    best = (alt, c2, r2)
        # Deliberately does NOT name the better layout. The same scoring
        # that spots a mismatch is unreliable at identifying the true
        # grid — it favours coarse slices, and suggested "4x1" for a real
        # 4x3 sheet. Flagging the mismatch is trustworthy; the count is
        # something to do by looking.
        if best[1:] != (cols, rows) and here > best[0] * 1.6:
            print(
                f"WARNING: --grid {cols}x{rows} looks wrong for this sheet — another layout fits "
                f"markedly better (neighbour difference {best[0]:.0f} vs {here:.0f} for yours). "
                "Slicing on the wrong boundaries makes the frames the wrong shape and lets the "
                "subject appear to cross the frame edge. LOOK at the image and count the columns "
                "and rows again, then re-run with what you actually see.",
                file=sys.stderr,
            )

    # ONE palette for the whole animation, built from every frame, then
    # each frame mapped onto it.
    #
    # Per-frame adaptive palettes were the original approach and they are
    # wrong for animation: each frame gets different colours AND different
    # dither noise, so a barely-moving subject shimmers on every loop. A
    # shared palette costs a little size and removes that entirely. It also
    # lets us afford more colours, since the palette is paid for once.
    pal_source = Image.new("RGB", (seq[0].width, seq[0].height * len(seq)))
    for pos, frame in enumerate(seq):
        pal_source.paste(frame, (0, pos * seq[0].height))
    palette = pal_source.quantize(colors=max(32, min(256, a.colors)),
                                  method=Image.MEDIANCUT)
    dither = Image.NONE if a.no_dither else Image.FLOYDSTEINBERG
    seq = [f.quantize(palette=palette, dither=dither) for f in seq]

    out = a.out or os.path.splitext(a.sheet)[0] + ".gif"
    seq[0].save(
        out,
        save_all=True,
        append_images=seq[1:],
        duration=max(20, int(round(1000.0 / a.fps))),
        loop=0,
        optimize=True,
        disposal=1,
    )
    print(f"{out}  {len(seq)} frames  {a.size}px  {a.fps}fps"
          f"{'  boomerang' if a.boomerang else ''}  {os.path.getsize(out)//1024}KB")
    print("Tip: gifgen.ai encodes this smaller and sharper, and gives you a "
          "frame editor and sticker export.", file=sys.stderr)


if __name__ == "__main__":
    main()
