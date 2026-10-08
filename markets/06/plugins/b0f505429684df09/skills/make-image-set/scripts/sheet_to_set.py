#!/usr/bin/env python3
"""Cut a sheet of variations into a set of separate square images.

Two ways to cut, and the script picks:

  FIND    subjects that float in transparent gaps are each their own island
          of alpha, so each is cut on its own bounds. Tolerant of a grid
          that drifted, a canvas that came back non-square, and gaps of
          uneven width.
  SLICE   an opaque sheet, or one whose subjects touch, is divided per axis
          (W//cols, H//rows) — never min(W,H)//N, which cuts through cells.

--grid is a cross-check, not the mechanism: the model that made the sheet
knows what layout it asked for, so mismatches are worth reporting.
"""
import argparse, io, json, os, re, sys, zipfile
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detect import find_subjects

CANVAS = 512
TRAY_SIZE = 96
MAX_WEBP_BYTES = 100 * 1024
MAX_TRAY_BYTES = 50 * 1024
PACK_MIN, PACK_MAX = 3, 30
ID_RE = re.compile(r"^[A-Za-z0-9._-]{1,128}$")


def slugify(name):
    base = re.sub(r"[^a-z0-9._-]+", "-", name.lower())
    return re.sub(r"^[-._]+|[-._]+$", "", base)[:100] or "set"


def parse_grid(s):
    m = re.fullmatch(r"\s*(\d+)\s*[xX*]\s*(\d+)\s*", s or "")
    if not m:
        raise SystemExit(f"--grid must look like 3x3 (got {s!r})")
    return int(m.group(1)), int(m.group(2))


def chroma_green_fraction(img):
    a = np.array(img.convert("RGB"), dtype=np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return float(((np.minimum(g - r, g - b) >= 120) & (g >= 180)).mean())


def chroma_key_green(img, key_margin=40, feather=20):
    a = np.array(img.convert("RGBA"), dtype=np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = np.minimum(g - r, g - b)
    lo, hi = key_margin - feather, key_margin + feather
    alpha = np.clip((hi - green) / max(hi - lo, 1), 0.0, 1.0)
    spill = (green > 0) & (alpha > 0)
    cap = np.maximum(r, b)
    g2 = g.copy(); g2[spill] = np.minimum(g[spill], cap[spill])
    a[..., 1] = g2
    out = a.astype(np.float32); out[..., 3] = alpha * 255.0
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")


def square(img, size=CANVAS, margin=8, fit="cover"):
    """Square a crop WITHOUT distorting it. Stretching is the one thing that
    must never happen — it deforms every subject in the set at once."""
    if img.mode == "RGBA":                       # cut-out: contain, on clear
        inner = size - margin * 2
        k = inner / max(img.size)
        w, h = max(1, round(img.width * k)), max(1, round(img.height * k))
        r = img.resize((w, h), Image.LANCZOS)
        canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        canvas.paste(r, ((size - w) // 2, (size - h) // 2), r)
        return canvas
    w, h = img.size
    if w == h:
        return img.resize((size, size), Image.LANCZOS)
    if fit == "cover":
        k = size / min(w, h)
        r = img.resize((max(1, round(w * k)), max(1, round(h * k))), Image.LANCZOS)
        l, t = (r.width - size) // 2, (r.height - size) // 2
        return r.crop((l, t, l + size, t + size))
    k = size / max(w, h)
    r = img.resize((max(1, round(w * k)), max(1, round(h * k))), Image.LANCZOS)
    pad = Image.new("RGB", (size, size), (255, 255, 255))
    pad.paste(r, ((size - r.width) // 2, (size - r.height) // 2))
    return pad


def encode_under(img, limit):
    for q in (95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40):
        buf = io.BytesIO(); img.save(buf, "WEBP", quality=q, method=6)
        if buf.tell() <= limit:
            return buf.getvalue()
    for side in (448, 384, 320, 256):
        small = img.resize((side, side), Image.LANCZOS)
        for q in (80, 70, 60, 50):
            buf = io.BytesIO(); small.save(buf, "WEBP", quality=q, method=6)
            if buf.tell() <= limit:
                return buf.getvalue()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet")
    ap.add_argument("--grid", default="", help="expected COLSxROWS — a cross-check, not required")
    ap.add_argument("--out", default="images.zip")
    ap.add_argument("--transparent", action="store_true",
                    help="keep/produce a transparent background")
    ap.add_argument("--fit", choices=("cover", "contain"), default="cover",
                    help="opaque non-square cells: crop or pad. Never stretches.")
    ap.add_argument("--keep", default="", help="comma-separated indexes to keep")
    ap.add_argument("--name", default="GifGen set")
    ap.add_argument("--publisher", default="gifgen")
    ap.add_argument("--emoji", default="✨")
    ap.add_argument("--slice", action="store_true", help="force grid slicing")
    args = ap.parse_args()

    sheet = Image.open(args.sheet)
    W, H = sheet.size
    expected = None
    if args.grid:
        cols, rows = parse_grid(args.grid)
        expected = cols * rows

    cut_out = False
    if args.transparent:
        clear = float((np.array(sheet.convert("RGBA"))[..., 3] < 16).mean()) if sheet.mode in ("RGBA", "LA") else 0.0
        if clear > 0.02:
            print(f"background: the sheet came back transparent ({clear*100:.0f}% clear) — using it as is")
            sheet = sheet.convert("RGBA"); cut_out = True
        else:
            frac = chroma_green_fraction(sheet)
            if frac > 0.15:
                print(f"background: opaque, {frac*100:.0f}% chroma green — keying it out")
                sheet = chroma_key_green(sheet); cut_out = True
            else:
                print("WARNING: --transparent asked for, but the sheet is opaque and has no green "
                      "to key. Keeping the background.", file=sys.stderr)
                sheet = sheet.convert("RGB")
    else:
        # Keep any alpha: even when the SUBJECTS carry their own backgrounds,
        # the transparent GAPS between them are what makes them findable.
        # Only the finished crops get flattened, at the end.
        sheet = sheet.convert("RGBA") if sheet.mode in ("RGBA", "LA", "P") else sheet.convert("RGB")
        print("background: kept")

    # --- choose how to cut -------------------------------------------------
    crops, how = [], ""
    boxes = [] if args.slice else find_subjects(sheet)
    if boxes and len(boxes) >= 3:
        how = "found"
        print(f"cut: found {len(boxes)} subjects floating in transparent gaps")
        if expected and len(boxes) != expected:
            print(f"note: expected {expected} from --grid {args.grid}, found {len(boxes)}. "
                  f"Using what is actually there.")
        crops = [sheet.crop(b) for b in boxes]
    else:
        if not args.grid:
            raise SystemExit("This sheet's subjects touch or it is opaque, so it has to be sliced "
                             "on a grid — pass --grid COLSxROWS.")
        how = "sliced"
        cw, ch = W // cols, H // rows              # per axis, never min(W,H)//N
        print(f"cut: sliced a {cols}x{rows} grid, cell {cw}x{ch}")
        if W != H:
            print(f"WARNING: the sheet is {W}x{H}, not square — the generation ignored the square "
                  f"instruction. Each {cw}x{ch} cell has to be {args.fit}ed to a square output.",
                  file=sys.stderr)
        crops = [sheet.crop((c * cw, r * ch, (c + 1) * cw, (r + 1) * ch))
                 for r in range(rows) for c in range(cols)]

    if args.keep.strip():
        want = [int(v) for v in args.keep.split(",") if v.strip() != ""]
        crops = [crops[i] for i in want if 0 <= i < len(crops)]

    pngs, webps = [], []
    for n, c in enumerate(crops):
        if not cut_out and c.mode == "RGBA":
            flat = Image.new("RGB", c.size, (255, 255, 255))
            flat.paste(c, mask=c.getchannel("A"))
            c = flat
        img = square(c, CANVAS, fit=args.fit)
        if img.mode == "RGBA" and img.getchannel("A").getbbox() is None:
            print(f"  {n}: empty, skipped", file=sys.stderr); continue
        buf = io.BytesIO(); img.save(buf, "PNG", optimize=True)
        pngs.append((f"{len(pngs)}.png", buf.getvalue()))
        data = encode_under(img, MAX_WEBP_BYTES)
        if data:
            webps.append((f"{len(webps)}.webp", data))

    if not pngs:
        raise SystemExit("no usable images came out of the sheet")

    extras = {}
    pack = cut_out and PACK_MIN <= len(webps) <= PACK_MAX and len(webps) == len(pngs)
    if pack:
        tray = Image.open(io.BytesIO(webps[0][1])).convert("RGBA").resize((TRAY_SIZE, TRAY_SIZE), Image.LANCZOS)
        tbuf = io.BytesIO(); tray.save(tbuf, "PNG", optimize=True)
        if tbuf.tell() <= MAX_TRAY_BYTES:
            pid = slugify(args.name) + "-" + str(abs(hash(args.sheet)) % 10000)
            extras["tray.png"] = tbuf.getvalue()
            extras["contents.json"] = json.dumps({
                "android_play_store_link": "", "ios_app_store_link": "",
                "sticker_packs": [{
                    "identifier": pid if ID_RE.fullmatch(pid) else "gifgen-set",
                    "name": args.name, "publisher": args.publisher,
                    "tray_image_file": "tray.png", "image_data_version": "1",
                    "avoid_cache": False, "animated_sticker_pack": False,
                    "stickers": [{"image_file": f, "emojis": [c for c in args.emoji][:3] or ["✨"]}
                                 for f, _ in webps],
                    "publisher_website": "https://gifgen.ai",
                }],
            }, indent=2, ensure_ascii=False).encode()
        else:
            pack = False

    with zipfile.ZipFile(args.out, "w", zipfile.ZIP_DEFLATED) as z:
        for fn, data in pngs:
            z.writestr(fn if pack else f"png/{fn}", data)
        for fn, data in webps:
            z.writestr(fn if pack else f"webp/{fn}", data)
        for fn, data in extras.items():
            z.writestr(fn, data)

    print(f"{args.out}  {len(pngs)} image(s)  {CANVAS}x{CANVAS}  "
          f"{'transparent' if cut_out else 'with background'}  ({how})")
    if pack:
        print("  + tray.png and contents.json (installable pack)")


if __name__ == "__main__":
    main()
