#!/usr/bin/env python3
"""Compose an image for a Wignet e-paper frame, ready to push.

Two jobs, each producing a PNG already at the frame's exact size and
already black-and-white (or in the six Spectra 6 colours), so the platform
has nothing left to guess and the file stays small enough to travel as
base64 inside a tool call:

  compose.py text "Title" "Body text, as long as needed." -o card.png
  compose.py image photo.jpg --fit cover -o photo.png

A photo written with --base64 goes out as a half-size JPEG (about 20 000
characters instead of 60 000) that the platform scales and dithers itself.

Size: pass the frame's *logical* size from get_orientation (e.g. 480x800 for
a portrait frame) with --width/--height; default 800x480. The pushed image
inherits the frame's orientation, and the platform turns it into the panel's
buffer.

Delivering it (pick the first that works where you run):
  --upload <device link>          POST the file to the frame (needs network).
  --base64                        write <out>.b64 for push_content's
                                  image_base64 (no network needed).
  --print-base64                  also print it, to copy into the call.

Only Pillow is required. Fonts ship next to this script (Archivo, SIL OFL).
"""
import argparse
import base64
import hashlib
import io
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid

from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))


def _font_path(name):
    """The skill keeps fonts in ../fonts; a GPT's knowledge files sit flat."""
    for folder in (os.path.join(HERE, "..", "fonts"), HERE):
        path = os.path.join(folder, name)
        if os.path.exists(path):
            return path
    return name


TITLE_FONT = _font_path("ArchivoBlack-Regular.ttf")
BODY_FONT = _font_path("Archivo-Medium.ttf")

# The six inks of a Spectra 6 panel, in the platform's palette order.
SPECTRA6 = [(0, 0, 0), (255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 255, 0)]

# Past this, a base64 copy through a conversation gets slow and error-prone.
BASE64_COMFORT_CHARS = 30_000

# Smallest body text still readable across a room on a 7.5" panel (~100 dpi).
MIN_BODY_PX = 22


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        try:
            return ImageFont.load_default(size=size)
        except TypeError:  # Pillow < 10.1: fixed-size bitmap font
            return ImageFont.load_default()


def wrap(draw, text, face, max_width):
    """Greedy word wrap, paragraph by paragraph; long words are split."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        line = ""
        for word in words:
            candidate = f"{line} {word}".strip()
            if draw.textlength(candidate, font=face) <= max_width:
                line = candidate
                continue
            if line:
                lines.append(line)
            while draw.textlength(word, font=face) > max_width and len(word) > 1:
                cut = len(word)
                while cut > 1 and draw.textlength(word[:cut], font=face) > max_width:
                    cut -= 1
                lines.append(word[:cut])
                word = word[cut:]
            line = word
        lines.append(line)
    return lines


def block_height(face, lines, spacing):
    ascent, descent = face.getmetrics()
    return len(lines) * (ascent + descent) + max(0, len(lines) - 1) * spacing


def fit_text(draw, text, path, max_width, max_height, largest, smallest=10):
    """Largest size at which `text` wraps into the box: (face, lines, spacing)."""
    lo, hi, best = smallest, largest, None
    while lo <= hi:
        size = (lo + hi) // 2
        face = font(path, size)
        lines = wrap(draw, text, face, max_width)
        spacing = size // 4
        # A size that has to cut a word in two is too big, even if it fits.
        whole_words = all(draw.textlength(word, font=face) <= max_width for word in text.split())
        if whole_words and block_height(face, lines, spacing) <= max_height:
            best = (face, lines, spacing, size)
            lo = size + 1
        else:
            hi = size - 1
    if best is None:
        face = font(path, smallest)
        best = (face, wrap(draw, text, face, max_width), smallest // 4, smallest)
    return best


def draw_lines(draw, face, lines, spacing, top, width, margin, align):
    ascent, descent = face.getmetrics()
    y = top
    for line in lines:
        length = draw.textlength(line, font=face)
        x = margin if align == "left" else (width - length) / 2
        draw.text((x, y), line, font=face, fill=0)
        y += ascent + descent + spacing
    return y


def compose_text(title, body, width, height, align="center"):
    """A card: bold title on top, body filling the rest, both auto-sized."""
    canvas = Image.new("L", (width, height), 255)
    draw = ImageDraw.Draw(canvas)
    margin = max(16, min(width, height) // 16)
    inner_w, inner_h = width - 2 * margin, height - 2 * margin
    warnings = []

    title_block = body_block = None
    gap = 0
    if title and body:
        title_block = fit_text(draw, title, TITLE_FONT, inner_w, int(inner_h * 0.35), largest=inner_h // 3)
        gap = margin // 2
        rest = inner_h - block_height(title_block[0], title_block[1], title_block[2]) - gap
        body_block = fit_text(draw, body, BODY_FONT, inner_w, rest,
                              largest=min(title_block[3], inner_h // 4))
    elif title:
        title_block = fit_text(draw, title, TITLE_FONT, inner_w, inner_h, largest=inner_h // 2)
    elif body:
        body_block = fit_text(draw, body, BODY_FONT, inner_w, inner_h, largest=inner_h // 4)
    else:
        raise SystemExit("compose.py text: give a title, a body, or both")

    total = gap
    for block in (title_block, body_block):
        if block:
            total += block_height(block[0], block[1], block[2])
    y = margin + max(0, (inner_h - total) // 2)
    if title_block:
        y = draw_lines(draw, title_block[0], title_block[1], title_block[2], y, width, margin, align) + gap
    if body_block:
        draw_lines(draw, body_block[0], body_block[1], body_block[2], y, width, margin, align)
        if body_block[3] < MIN_BODY_PX:
            warnings.append(f"body text is {body_block[3]}px, hard to read from a distance: shorten it")
    return canvas, warnings


def compose_image(path, width, height, fit="contain"):
    image = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    if fit == "cover":
        return ImageOps.fit(image, (width, height), method=Image.LANCZOS), []
    image.thumbnail((width, height), Image.LANCZOS)
    canvas = Image.new("RGB", (width, height), (255, 255, 255))
    canvas.paste(image, ((width - image.width) // 2, (height - image.height) // 2))
    return canvas, []


def to_panel(image, profile="mono1", mode="dither"):
    """Reduce to what the panel can show, which is also what compresses best."""
    if profile == "spectra6":
        palette = Image.new("P", (1, 1))
        flat = [value for rgb in SPECTRA6 for value in rgb]
        palette.putpalette(flat + [0] * (768 - len(flat)))
        dither = Image.NONE if mode == "threshold" else Image.FLOYDSTEINBERG
        return image.convert("RGB").quantize(palette=palette, dither=dither)
    grey = image.convert("L")
    if mode == "threshold":
        return grey.point(lambda v: 255 if v >= 128 else 0).convert("1", dither=Image.NONE)
    return grey.convert("1")


def png_bytes(image):
    buf = io.BytesIO()
    image.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def compact_bytes(image, profile):
    """A photo for the base64 path: half-size JPEG, reduced by the platform.

    A dithered photo is noise to a compressor (~60 000 base64 characters at
    800x480); the platform scales up and dithers itself, and dithering hides
    the lost resolution, so a half-size JPEG looks the same on the panel for
    about a third of the characters.
    """
    small = image.resize((max(1, image.width // 2), max(1, image.height // 2)), Image.LANCZOS)
    buf = io.BytesIO()
    small.convert("L" if profile == "mono1" else "RGB").save(buf, format="JPEG", quality=60, optimize=True)
    return buf.getvalue()


LINK_RE = re.compile(r"^(https?://[^/?#]+(?:/[^?#]*?)?)/(?:w|api/owner)/([^/?#]+)")
# The MCP connector URL, https://mcp.<domain>/<id>: the API is on app.<domain>.
MCP_LINK_RE = re.compile(r"^(https?)://mcp\.([^/?#]+)/([^/?#]+)/?$")


def upload_url(link):
    """Device link (…/w/<id>) or any owner API URL -> its /image upload URL."""
    mcp = MCP_LINK_RE.match(link.strip())
    if mcp and mcp.group(3) != "mcp":
        return f"{mcp.group(1)}://app.{mcp.group(2)}/api/owner/{mcp.group(3)}/image"
    match = LINK_RE.match(link.strip())
    if not match:
        raise SystemExit(f"--upload: expected the frame's link, https://…/w/<id>, got {link!r}")
    base, device_id = match.group(1), match.group(2)
    return f"{base}/api/owner/{device_id}/image"


def upload(url, data, fields):
    boundary = uuid.uuid4().hex
    parts = []
    for key, value in fields.items():
        if value is not None:
            parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n'.encode())
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="wignet.png"\r\n'
                 "Content-Type: image/png\r\n\r\n".encode() + data + b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode())
    request = urllib.request.Request(url, data=b"".join(parts), method="POST",
                                     headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, json.loads(response.read() or b"{}")
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read() or b"{}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="kind", required=True)
    text = sub.add_parser("text", help="a title and/or body text, auto-sized")
    text.add_argument("title", nargs="?", default="")
    text.add_argument("body", nargs="?", default="")
    text.add_argument("--body-file", help="read the body from a file ('-' for stdin)")
    text.add_argument("--align", choices=("center", "left"), default="center")
    photo = sub.add_parser("image", help="an existing picture, fitted and reduced")
    photo.add_argument("path")
    photo.add_argument("--fit", choices=("contain", "cover"), default="contain")
    for p in (text, photo):
        p.add_argument("--width", type=int, default=800, help="logical width from get_orientation")
        p.add_argument("--height", type=int, default=480, help="logical height from get_orientation")
        p.add_argument("--profile", choices=("mono1", "spectra6"), default="mono1",
                       help="get_capabilities display profile: spectra6 keeps six colours")
        p.add_argument("--mode", choices=("dither", "threshold"),
                       help="dither for photos (image default), threshold for text/logos (text default)")
        p.add_argument("-o", "--output", default="wignet.png")
        p.add_argument("--base64", action="store_true", help="also write <output>.b64")
        p.add_argument("--print-base64", action="store_true", help="print the base64 on stdout, last")
        p.add_argument("--upload", metavar="DEVICE_LINK", help="POST to the frame (needs network)")
        p.add_argument("--orientation", choices=("paysage", "portrait", "paysage_inverse", "portrait_inverse"),
                       help="optional with --upload: the frame's own orientation applies anyway, a different one is refused")
        p.add_argument("--duration", type=int, help="seconds before the frame goes back (with --upload)")
    photo.add_argument("--full", action="store_true",
                       help="with --base64: send the full-size reduced PNG instead of a compact JPEG")
    args = parser.parse_args(argv)

    if args.kind == "text":
        body = args.body
        if args.body_file:
            with (sys.stdin if args.body_file == "-" else open(args.body_file, encoding="utf-8")) as handle:
                body = handle.read().strip()
        image, warnings = compose_text(args.title, body, args.width, args.height, args.align)
        mode = args.mode or "threshold"
    else:
        image, warnings = compose_image(args.path, args.width, args.height, args.fit)
        mode = args.mode or "dither"

    # A photo headed for image_base64 travels as a compact JPEG the platform
    # reduces itself; everything else is reduced here, to the exact pixels.
    compact = (args.kind == "image" and (args.base64 or args.print_base64)
               and not args.upload and not args.full)
    if compact:
        data = compact_bytes(image, args.profile)
        if args.output.lower().endswith(".png"):
            args.output = args.output[:-4] + ".jpg"
    else:
        data = png_bytes(to_panel(image, args.profile, mode))
    with open(args.output, "wb") as handle:
        handle.write(data)
    encoded = base64.b64encode(data).decode()
    summary = {
        "output": os.path.abspath(args.output),
        "size": [args.width, args.height],
        "profile": args.profile,
        "mode": mode,
        "format": "jpeg (compact: the platform scales and reduces it)" if compact else "png",
        "bytes": len(data),
        "base64_chars": len(encoded),
        # Pass it as image_sha256: a mis-copied JPEG is then refused instead
        # of showing up garbled.
        "sha256": hashlib.sha256(data).hexdigest(),
    }
    if len(encoded) > BASE64_COMFORT_CHARS:
        warnings.append(
            f"{len(encoded)} base64 characters is heavy to copy into a tool call: prefer --upload or an "
            "image_url, or simplify (threshold mode, fewer grey areas, less detail)")
    if args.base64 or args.print_base64:
        with open(args.output + ".b64", "w") as handle:
            handle.write(encoded)
        summary["base64_file"] = os.path.abspath(args.output + ".b64")
    if args.upload:
        status, answer = upload(upload_url(args.upload), data, {
            "orientation": args.orientation, "duration_seconds": args.duration,
            # Already reduced here: keep the platform from dithering it twice.
            "mode": "threshold" if args.profile == "mono1" else None,
            "fit": "contain",
        })
        summary["upload"] = {"status": status, "response": answer}
    else:
        summary["next"] = ("push_content with image_base64 = the .b64 content, image_sha256 = sha256, mode = " + mode
                           + " (the frame's orientation applies)")
    if warnings:
        summary["warnings"] = warnings
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.print_base64:
        print(encoded)
    if args.upload and not 200 <= summary["upload"]["status"] < 300:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
