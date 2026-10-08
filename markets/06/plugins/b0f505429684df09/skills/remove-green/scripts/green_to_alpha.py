#!/usr/bin/env python3
"""Remove a chroma-green background from an image the user already has.

Works on a single image or, with --grid, on a sheet that gets sliced into
separate cut-outs. The key always runs on the WHOLE image before any
slicing, so cells from one sheet share a matte.
"""
import argparse, io, os, re, sys, zipfile
import numpy as np
from PIL import Image


def chroma_green_fraction(img):
    """Fraction that is CHROMA green, not merely greenish.

    Grass, foliage and olive skin all score on greenness alone. Real
    #00FF00 backing is separated by being both very green AND very bright
    in the green channel, which natural greens never are.
    """
    a = np.array(img.convert("RGB"), dtype=np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = np.minimum(g - r, g - b)
    return float(((green >= 120) & (g >= 180)).mean())


def chroma_key_green(img, key_margin=40, feather=20, despill=True):
    a = np.array(img.convert("RGBA"), dtype=np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = np.minimum(g - r, g - b)
    lower, upper = key_margin - feather, key_margin + feather
    alpha = np.clip((upper - green) / max(upper - lower, 1), 0.0, 1.0)
    if despill:
        spill = (green > 0) & (alpha > 0)
        cap = np.maximum(r, b)
        g2 = g.copy(); g2[spill] = np.minimum(g[spill], cap[spill])
        a[..., 1] = g2
    out = a.astype(np.float32)
    out[..., 3] = alpha * 255.0
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA"), alpha


def parse_grid(s):
    m = re.fullmatch(r"\s*(\d+)\s*[xX*]\s*(\d+)\s*", s or "")
    if not m:
        raise SystemExit(f"--grid must look like 3x3 (got {s!r})")
    return int(m.group(1)), int(m.group(2))


def trim_and_pad(img, size, margin=8):
    bbox = img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        img = img.crop(bbox)
    inner = size - margin * 2
    k = inner / max(img.size)
    w, h = max(1, round(img.width * k)), max(1, round(img.height * k))
    img = img.resize((w, h), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.paste(img, ((size - w) // 2, (size - h) // 2), img)
    return canvas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--out", default="", help="output file (.png) or .zip when --grid is used")
    ap.add_argument("--grid", default="", help="slice a sheet too, e.g. 4x4")
    ap.add_argument("--square", type=int, default=0, help="trim and pad each result to NxN")
    ap.add_argument("--key-margin", type=int, default=40,
                    help="higher keeps more of the subject, lower removes more green")
    ap.add_argument("--feather", type=int, default=20, help="softness of the edge")
    ap.add_argument("--no-despill", action="store_true", help="keep green reflections on the subject")
    ap.add_argument("--force", action="store_true", help="run even when there is no green screen to remove")
    args = ap.parse_args()

    src = Image.open(args.image)

    already = src.mode in ("RGBA", "LA") and float((np.array(src.convert("RGBA"))[..., 3] < 16).mean()) > 0.02
    frac = chroma_green_fraction(src)

    # Refuse rather than hand back a broken cut-out. Keying an image with no
    # green screen eats whatever happens to be greenish — grass, foliage,
    # olive skin — and the damage looks like a rendering fault.
    if already and frac < 0.05:
        raise SystemExit("This image already has a transparent background — there is no green "
                         "screen to remove. Nothing to do.")
    if frac < 0.05 and not args.force:
        raise SystemExit(f"Only {frac:.1%} of this image is chroma green, so there is no green "
                         f"screen here to remove. If the background is a different colour or a "
                         f"real scene, this tool cannot remove it. (--force overrides.)")

    keyed, alpha = chroma_key_green(src, args.key_margin, args.feather, not args.no_despill)
    removed = float((alpha < 0.5).mean())
    print(f"removed {removed*100:.1f}% of the image  (was {frac*100:.1f}% chroma green)")
    if removed > 0.95:
        print("WARNING: nearly everything was removed — was the subject itself green? "
              "Try a higher --key-margin.", file=sys.stderr)

    if args.grid:
        cols, rows = parse_grid(args.grid)
        W, H = keyed.size
        cw, ch = W // cols, H // rows        # per-axis, never min(W,H)//N
        out = args.out or "cutouts.zip"
        n = 0
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for i in range(cols * rows):
                c, r = i % cols, i // cols
                cell = keyed.crop((c * cw, r * ch, (c + 1) * cw, (r + 1) * ch))
                if cell.getchannel("A").getbbox() is None:
                    print(f"  cell {i}: empty after keying, skipped", file=sys.stderr); continue
                if args.square:
                    cell = trim_and_pad(cell, args.square)
                buf = io.BytesIO(); cell.save(buf, "PNG", optimize=True)
                z.writestr(f"{n}.png", buf.getvalue()); n += 1
        print(f"{out}  {n} cut-out(s)  from a {cols}x{rows} sheet  cell {cw}x{ch}")
    else:
        result = trim_and_pad(keyed, args.square) if args.square else keyed
        out = args.out or (os.path.splitext(args.image)[0] + "-cutout.png")
        result.save(out, "PNG", optimize=True)
        print(f"{out}  {result.size[0]}x{result.size[1]}  transparent PNG  {os.path.getsize(out)//1024}KB")


if __name__ == "__main__":
    main()
