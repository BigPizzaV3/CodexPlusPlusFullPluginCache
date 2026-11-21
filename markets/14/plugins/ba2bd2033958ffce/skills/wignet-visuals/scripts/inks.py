#!/usr/bin/env python3
"""The six Spectra 6 inks, for images that print cleanly on a Wignet frame.

    python3 inks.py palette                              # draw-with values, looks, lightness
    python3 inks.py check design.png                     # exact ink or dithered? + preview
    python3 inks.py photo in.jpg -o out.png --width 800 --height 480 --fit cover
    python3 inks.py preview design.png -o design.real.png
    python3 inks.py fonts                                # recommended fonts on this machine

In Python, next to your drawing code (Pillow):

    from inks import INK, fill_mix, pick_font
    draw.fontmode = "1"                       # no anti-aliasing
    face, name = pick_font("text", 32)        # Arial if present, else the next best
    draw_runs(draw, (x, y), [("High tide at ", face), ("9:12", bold)], INK["black"])
    draw.rectangle(box, fill=INK["red"])      # exact ink value
    fill_mix(image, box, "green", "blue", 8)  # teal: 8/16 blue

`check` and `preview` show an image as the panel will: exact ink pixels
stay, anything else is dithered by the platform's own converter (wgn6.py,
shipped beside this file), then each ink is painted as it really looks.
`photo` converts a photo by matching the inks' real looks instead of the
pure values the platform uses, and writes only exact ink values, which the
platform then passes through untouched. Needs Pillow.
"""
import argparse
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wgn6  # noqa: E402  (the platform's palette and converter)

NAMES = ("black", "white", "green", "blue", "red", "yellow")  # WGN6 code order
INK = {name: wgn6.RGB_PALETTE[code] for code, name in enumerate(NAMES)}
LOOK = {name: wgn6.INK_APPEARANCE[code] for code, name in enumerate(NAMES)}
# Mixes of inks of close lightness, which read as a colour rather than grain.
SMOOTH_MIXES = {"teal": ("green", "blue", 8), "cream": ("white", "yellow", 8),
                "brown": ("red", "green", 8), "plum": ("red", "blue", 8)}
BAYER = ((0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))
_BY_VALUE = {rgb: name for name, rgb in INK.items()}


def _linear(channel):
    channel /= 255
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def lightness(name):
    """CIE L* of an ink as it looks: 0 black .. 100 white."""
    y = luminance(LOOK[name])
    return 116 * y ** (1 / 3) - 16 if y > 0.008856 else 903.3 * y


def contrast(foreground, background):
    """WCAG contrast ratio of two inks as they look (4.5+ for body text)."""
    a, b = sorted((luminance(LOOK[foreground]), luminance(LOOK[background])), reverse=True)
    return (a + 0.05) / (b + 0.05)


HERE = os.path.dirname(os.path.abspath(__file__))
_SHIPPED = os.path.join(HERE, "..", "fonts")
_MAC = "/System/Library/Fonts/"
_MAC_SUP = _MAC + "Supplemental/"
_WIN = "C:/Windows/Fonts/"
_MS_LINUX = "/usr/share/fonts/truetype/msttcorefonts/"  # Microsoft core fonts package
# Where each font usually lives. "path#N" is face N of a collection,
# "path@Name" a named instance of a variable font. The verdicts behind the
# list are in references/typography.md (judged on a Spectra 6 panel).
FONT_FILES = {
    "Arial": [_MAC_SUP + "Arial.ttf", "/Library/Fonts/Arial.ttf", _WIN + "arial.ttf",
              _MS_LINUX + "Arial.ttf", _MS_LINUX + "arial.ttf"],
    "Arial Bold": [_MAC_SUP + "Arial Bold.ttf", "/Library/Fonts/Arial Bold.ttf", _WIN + "arialbd.ttf",
                   _MS_LINUX + "Arial_Bold.ttf", _MS_LINUX + "arialbd.ttf"],
    "Verdana": [_MAC_SUP + "Verdana.ttf", _WIN + "verdana.ttf", _MS_LINUX + "Verdana.ttf",
                _MS_LINUX + "verdana.ttf"],
    "Verdana Bold": [_MAC_SUP + "Verdana Bold.ttf", _WIN + "verdanab.ttf", _MS_LINUX + "Verdana_Bold.ttf",
                     _MS_LINUX + "verdanab.ttf"],
    "Tahoma": [_MAC_SUP + "Tahoma.ttf", _WIN + "tahoma.ttf"],
    "Tahoma Bold": [_MAC_SUP + "Tahoma Bold.ttf", _WIN + "tahomabd.ttf"],
    "Lucida Grande": [_MAC + "LucidaGrande.ttc#0"],
    "Lucida Grande Bold": [_MAC + "LucidaGrande.ttc#1"],
    "Geneva": [_MAC + "Geneva.ttf"],
    "San Francisco": [_MAC + "SFNS.ttf@Regular"],
    "San Francisco Bold": [_MAC + "SFNS.ttf@Bold"],
    # Shipped with this skill (free licence, notice in fonts/): always there.
    "Bitstream Vera": [os.path.join(_SHIPPED, "Vera.ttf")],
    "Bitstream Vera Bold": [os.path.join(_SHIPPED, "VeraBd.ttf")],
    "Archivo Black": [os.path.join(_SHIPPED, "ArchivoBlack-Regular.ttf")],
    "Ubuntu": ["/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
               "/usr/share/fonts/truetype/ubuntu/Ubuntu-Regular.ttf"],
    "Ubuntu Bold": ["/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
                    "/usr/share/fonts/truetype/ubuntu/Ubuntu-Bold.ttf"],
    "PT Sans": ["/usr/share/fonts/truetype/paratype/PTS55F.ttf",
                "/usr/share/fonts/truetype/pt-sans/PT_Sans-Web-Regular.ttf"],
    "PT Sans Bold": ["/usr/share/fonts/truetype/paratype/PTS75F.ttf",
                     "/usr/share/fonts/truetype/pt-sans/PT_Sans-Web-Bold.ttf"],
    "DejaVu Sans": ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                    "/usr/share/fonts/dejavu/DejaVuSans.ttf", "matplotlib:DejaVuSans.ttf"],
    "DejaVu Sans Bold": ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                         "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf", "matplotlib:DejaVuSans-Bold.ttf"],
}
# Best first, per role. Bitstream Vera ships with the skill, so no role ever
# falls through to Pillow's default font.
ROLES = {
    "text": ["Arial", "Verdana", "Tahoma", "Lucida Grande", "San Francisco", "Bitstream Vera",
             "Ubuntu", "PT Sans", "DejaVu Sans"],
    "label": ["Verdana", "Tahoma", "Geneva", "Lucida Grande", "Arial", "Bitstream Vera",
              "Ubuntu", "PT Sans", "DejaVu Sans"],
    "headline": ["Archivo Black", "Arial Bold", "Verdana Bold", "Tahoma Bold", "Lucida Grande Bold",
                 "San Francisco Bold", "Bitstream Vera Bold", "Ubuntu Bold", "PT Sans Bold",
                 "DejaVu Sans Bold"],
}
# Recommended minimum (owner's verdict on the panel): smaller text is hard
# to read. pick_font warns below it; it never refuses.
MIN_TEXT_PX = 16


def font_file(name):
    """(path, face index, variation name) of a font on this machine, or None."""
    for entry in FONT_FILES[name]:
        index, variation = 0, None
        if entry.startswith("matplotlib:"):
            try:
                import matplotlib
            except ImportError:
                continue
            entry = os.path.join(matplotlib.get_data_path(), "fonts", "ttf", entry.split(":", 1)[1])
        if "@" in os.path.basename(entry):
            entry, variation = entry.rsplit("@", 1)
        elif "#" in os.path.basename(entry):
            entry, index = entry.rsplit("#", 1)
            index = int(index)
        if os.path.exists(entry):
            return os.path.abspath(entry), index, variation
    return None


def font_path(name):
    """The file of a font from FONT_FILES on this machine, or None."""
    found = font_file(name)
    return found[0] if found else None


def load_font(name, size):
    """An ImageFont for a FONT_FILES name, or None if this machine lacks it."""
    from PIL import ImageFont
    found = font_file(name)
    if not found:
        return None
    path, index, variation = found
    face = ImageFont.truetype(path, size, index=index)
    if variation:
        face.set_variation_by_name(variation)
    return face


def has_accents(face):
    """Whether a font draws "àéç°" rather than its missing-glyph box."""
    from PIL import Image, ImageDraw

    def glyph(ch):
        image = Image.new("L", (face.size * 2, face.size * 2), 0)
        ImageDraw.Draw(image).text((0, 0), ch, font=face, fill=255)
        return image.tobytes()

    missing = glyph("\U000F0000")  # a private-use character no font draws
    return all(glyph(ch) != missing for ch in "àéç°")


def pick_font(role="text", size=32, bold=False):
    """(ImageFont, name): the best font this machine has for a role.

    Warns under MIN_TEXT_PX, the recommended minimum on the panel.
    """
    if size < MIN_TEXT_PX:
        import warnings
        warnings.warn(f"{size} px is under the recommended {MIN_TEXT_PX} px minimum: "
                      "hard to read on the panel", stacklevel=2)
    names = ROLES[role]
    if bold and role != "headline":
        names = [n + " Bold" for n in names if n + " Bold" in FONT_FILES] + names
    for name in names:
        face = load_font(name, size)
        if face is not None:
            return face, name
    raise RuntimeError("no font found, not even the ones shipped with the skill (fonts/)")


def ink_span(face, text):
    """(left, right) of a text's actual ink, relative to where it is drawn.

    Font metrics hide side bearings: Arial's tabular "1" sits in a box as
    wide as an "8", with blank space on its left.
    """
    from PIL import Image, ImageDraw
    pad = face.size
    image = Image.new("1", (int(face.getlength(text)) + 2 * pad, 2 * pad), 0)
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1"
    draw.text((pad, 0), text, font=face, fill=1)
    box = image.getbbox()
    return (box[0] - pad, box[2] - pad) if box else (0, 0)


def draw_runs(draw, xy, parts, fill):
    """Draw one line mixing weights, e.g. [("Pleine mer à ", regular), ("9 h 12", bold)].

    Word gaps between runs are set from the ink, so a bold figure after a
    space sits as far from the previous word as any other word, whatever its
    side bearings. Returns the x where the line's ink ends.
    """
    x, y = xy
    word_gap = None
    ink_end = None
    for index, (text, face) in enumerate(parts):
        if word_gap is None:  # the ink gap between two words in this face
            n_left, n_right = ink_span(face, "n")
            both_left, both_right = ink_span(face, "n n")
            word_gap = (both_right - both_left) - 2 * (n_right - n_left)
        spaced = index and (text.startswith(" ") or parts[index - 1][0].endswith(" "))
        body = text.strip(" ") if spaced else text
        left, right = ink_span(face, body)
        if spaced and ink_end is not None:
            x = ink_end + word_gap - left
        draw.text((x, y), body, font=face, fill=fill)
        ink_end = x + right
        x += face.getlength(body)
        if text.endswith(" ") and index == len(parts) - 1:
            x += face.getlength(" ")
    return ink_end


def fill_mix(image, box, first, second, sixteenths=8):
    """Fill box (x0, y0, x1, y1, end exclusive) with n/16 of `second`, the rest `first`.

    A 4x4 ordered pattern: 8 is a pixel checkerboard, 4 and 12 spread a
    quarter or three quarters evenly. Exact ink values only, so the panel
    shows exactly this pattern.
    """
    x0, y0, x1, y1 = box
    a, b = INK[first], INK[second]
    pixels = image.load()
    for y in range(max(0, y0), min(image.height, y1)):
        row = BAYER[y % 4]
        for x in range(max(0, x0), min(image.width, x1)):
            pixels[x, y] = b if row[x % 4] < sixteenths else a


def fit(image, width, height, mode="contain"):
    """Scale to (width, height): contain pads with white, cover crops."""
    from PIL import Image
    image = image.convert("RGB")
    scale = (max if mode == "cover" else min)(width / image.width, height / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    resized = image.resize(size, Image.LANCZOS)
    canvas = Image.new("RGB", (width, height), INK["white"])
    canvas.paste(resized, ((width - size[0]) // 2, (height - size[1]) // 2))
    return canvas


def photo(image, width, height, mode="cover"):
    """A photo in exact ink values, matched against the inks' real looks."""
    from PIL import Image
    source = fit(image, width, height, mode)
    palette = Image.new("P", (1, 1))
    looks = [c for name in NAMES for c in LOOK[name]]
    palette.putpalette(looks + looks[3:6] * (256 - len(NAMES)))  # spares = white
    dither = getattr(getattr(Image, "Dither", Image), "FLOYDSTEINBERG", 3)
    quantized = source.quantize(palette=palette, dither=dither)
    codes = bytes(c if c < len(NAMES) else 1 for c in quantized.tobytes())
    out = Image.frombytes("P", quantized.size, codes)
    out.putpalette([c for name in NAMES for c in INK[name]] + [255] * (768 - 3 * len(NAMES)))
    return out.convert("RGB")


def _pixels(image):
    flat = getattr(image, "get_flattened_data", None)  # Pillow 12+; getdata is deprecated
    return list(flat() if flat else image.getdata())


def panel_view(image):
    """(what the panel shows, as it looks; share of exact-ink pixels)."""
    rgb = image.convert("RGB")
    pixels = _pixels(rgb)
    exact = sum(1 for p in pixels if p in _BY_VALUE) / max(1, len(pixels))
    quantized = wgn6.quantize_image(rgb, dither=True)  # exact pixels map to themselves
    return wgn6.appearance_preview(quantized), exact


def check(path, width=None, height=None):
    from PIL import Image
    image = Image.open(path)
    image.load()
    problems = []
    if image.mode in ("RGBA", "LA", "PA") or "transparency" in image.info:
        problems.append("it has transparency: flatten it onto a solid ink background")
    rgb = image.convert("RGB")
    counts = Counter(_pixels(rgb))
    total = rgb.width * rgb.height
    exact = sum(n for value, n in counts.items() if value in _BY_VALUE)
    print(f"{path}: {rgb.width}x{rgb.height}, {100 * exact / total:.1f} % exact ink")
    if width and height and (rgb.width, rgb.height) != (width, height):
        problems.append(f"it is {rgb.width}x{rgb.height}, not the frame's {width}x{height}: "
                        "the platform will rescale it and blur every edge")
    inks = sorted(((n, _BY_VALUE[v]) for v, n in counts.items() if v in _BY_VALUE), reverse=True)
    print("  inks: " + ", ".join(f"{name} {100 * n / total:.1f} %" for n, name in inks))
    off = total - exact
    if off:
        top = ", ".join("#%02X%02X%02X" % v for v, _ in
                        sorted(((v, n) for v, n in counts.items() if v not in _BY_VALUE),
                               key=lambda item: -item[1])[:5])
        print(f"  {100 * off / total:.1f} % of pixels will be dithered (most common: {top})")
        looks = {v for v in counts if v in LOOK.values() and v not in _BY_VALUE}
        if looks:
            problems.append("some areas use an ink's *look* value (e.g. #608050): draw with "
                            "the exact value (INK) instead, it prints solid")
        if 0.001 < off / total < 0.2:
            problems.append("a small share of stray colours usually means anti-aliased text "
                            "or edges (draw.fontmode = \"1\"), or a resized design")
        elif off / total >= 0.2:
            problems.append("large areas are not exact inks (gradients, a photo, colours "
                            "outside the palette): a photo -> `inks.py photo`; a design -> "
                            "redraw those areas in exact inks or fill_mix patterns")
    view, _ = panel_view(image)
    preview_path = os.path.splitext(path)[0] + ".real.png"
    view.save(preview_path)
    print(f"  as the panel shows it: {preview_path}")
    for problem in problems:
        print(f"  ! {problem}")
    if not problems and not off:
        print("  clean: every pixel is an exact ink")
    return not problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("palette", help="the inks, their looks, lightness and text contrast")
    c = sub.add_parser("check", help="how much of an image is exact ink; writes the preview")
    c.add_argument("file")
    c.add_argument("--width", type=int)
    c.add_argument("--height", type=int)
    p = sub.add_parser("photo", help="convert a photo to exact inks, matched on real looks")
    p.add_argument("file")
    p.add_argument("-o", "--output", required=True, help="a .png (never JPEG)")
    p.add_argument("--width", type=int, default=800)
    p.add_argument("--height", type=int, default=480)
    p.add_argument("--fit", choices=("cover", "contain"), default="cover")
    sub.add_parser("fonts", help="which recommended fonts this machine has")
    v = sub.add_parser("preview", help="the image as the panel shows it")
    v.add_argument("file")
    v.add_argument("-o", "--output", required=True)
    args = parser.parse_args(argv)

    if args.command == "palette":
        print("ink     draw with  looks like  lightness  text on it")
        for name in ("black", "white", "red", "yellow", "green", "blue"):
            best = max(("black", "white"), key=lambda fg: contrast(fg, name))
            print(f"{name:7} #%02X%02X%02X    #%02X%02X%02X     {lightness(name):5.0f}"
                  % (INK[name] + LOOK[name]) + f"      {best} ({contrast(best, name):.1f})")
        print("smooth mixes: " + ", ".join(f"{k} = {a} + {b}" for k, (a, b, _) in SMOOTH_MIXES.items()))
        return 0
    from PIL import Image
    if args.command == "fonts":
        from PIL import ImageFont
        print("font                  on this machine")
        for name in FONT_FILES:
            face = load_font(name, 24)
            note = "missing"
            if face is not None:
                note = font_path(name) + ("" if has_accents(face) else "  (NO ACCENTS)")
            print(f"{name:21} {note}")
        for role in ROLES:
            face, name = pick_font(role, 24)
            print(f"{role} -> {name}")
        return 0
    if args.command == "check":
        return 0 if check(args.file, args.width, args.height) else 1
    image = Image.open(args.file)
    image.load()
    if args.command == "photo":
        if args.output.lower().endswith((".jpg", ".jpeg")):
            parser.error("write a .png: JPEG would shift the exact ink values")
        photo(image, args.width, args.height, args.fit).save(args.output)
        print(f"{args.output}: {args.width}x{args.height}, exact inks only, matched on real looks")
        return 0
    view, exact = panel_view(image)
    view.save(args.output)
    print(f"{args.output}: {100 * exact:.1f} % of the source was exact ink")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
