#!/usr/bin/env python3
"""Create Homey driver-image sizes from one square photo-quality master."""
from pathlib import Path
import argparse
from PIL import Image, ImageOps

SIZES = {
    "small.png": 75,
    "large.png": 500,
    "xlarge.png": 1000,
}

def flatten_to_white(im: Image.Image) -> Image.Image:
    rgba = im.convert("RGBA")
    bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    bg.alpha_composite(rgba)
    return bg.convert("RGB")

def square_on_white(im: Image.Image) -> Image.Image:
    im = ImageOps.exif_transpose(im)
    im = flatten_to_white(im)
    side = max(im.size)
    canvas = Image.new("RGB", (side, side), "white")
    x = (side - im.width) // 2
    y = (side - im.height) // 2
    canvas.paste(im, (x, y))
    return canvas

def main():
    p = argparse.ArgumentParser()
    p.add_argument("master")
    p.add_argument("output_dir")
    args = p.parse_args()
    with Image.open(args.master) as im:
        src = square_on_white(im)
    if src.width < 1000:
        p.error('master must be at least 1000 pixels on its longest side')
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, size in SIZES.items():
        img = src.resize((size, size), Image.Resampling.LANCZOS)
        img.save(out / name, "PNG", optimize=True)

if __name__ == "__main__":
    main()
