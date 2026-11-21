#!/usr/bin/env python3
"""Separate a visually reviewed sheet. Requires Pillow; never calls an image API.

Run: python3 split_sheet.py SHEET REVIEW.json NEW_OUTPUT_DIRECTORY
Review format (coordinates measured from the inspected sheet, not guessed):
{"sha256":"<source file SHA-256>", "verdict":"pass", "panels":[
  {"target":"cover", "box":[0,0,512,512], "verdict":"pass",
   "review":"Scene, continuity, anatomy, text and borders checked; no defects."}
]}
Boxes are [left, top, right, bottom]. Targets are cover or existing page IDs.
The review records a prior vision check; this script only validates geometry.
Inspect the resulting JPEGs with vision before uploading their host attachments.
"""
import argparse
import hashlib
import io
import json
import re
from pathlib import Path
from PIL import Image, ImageOps


def split_sheet(source: Path, review: dict, output: Path):
    raw = source.read_bytes()
    if review.get('sha256') != hashlib.sha256(raw).hexdigest() or review.get('verdict') != 'pass':
        raise ValueError('A passing visual review for this exact source file is required.')
    panels = review.get('panels', [])
    if not 1 <= len(panels) <= 9:
        raise ValueError('A sheet must contain one to nine approved targets.')
    if output.exists():
        raise ValueError('Choose a new output directory; existing images are never overwritten.')
    with Image.open(io.BytesIO(raw)) as original:
        if original.width * original.height > 32_000_000:
            raise ValueError('The sheet exceeds 32 megapixels.')
        sheet = ImageOps.exif_transpose(original).convert('RGB')
    targets, boxes, prepared = set(), [], []
    for panel in panels:
        target, box = panel.get('target', ''), panel.get('box', [])
        if not re.fullmatch(r'[a-zA-Z0-9_-]{1,80}', target) or target in targets:
            raise ValueError('Every target must be a unique cover/page ID.')
        if panel.get('verdict') != 'pass' or not str(panel.get('review', '')).strip():
            raise ValueError(f'{target}: record the visual check before cropping.')
        if len(box) != 4 or any(type(x) is not int for x in box):
            raise ValueError(f'{target}: use four integer pixel coordinates.')
        left, top, right, bottom = box
        if not (0 <= left < right <= sheet.width and 0 <= top < bottom <= sheet.height and right-left == bottom-top):
            raise ValueError(f'{target}: the box must be square and inside the sheet.')
        if any(left < r and right > l and top < b and bottom > t for l,t,r,b in boxes):
            raise ValueError(f'{target}: panel boxes must not overlap.')
        targets.add(target); boxes.append(box)
        crop = sheet.crop(box)
        crop.thumbnail((1024,1024), Image.Resampling.LANCZOS)
        for quality in (85,75,65,55):
            data = io.BytesIO()
            crop.save(data, 'JPEG', quality=quality, optimize=True)
            if data.tell() <= 512*1024:
                break
        else:
            raise ValueError(f'{target}: crop is too detailed; prepare a smaller crop.')
        prepared.append((target, data.getvalue(), crop.width))
    output.mkdir(parents=True, exist_ok=False)
    manifest = []
    for target, data, pixels in prepared:
        name = f'{target}.jpg'
        (output/name).write_bytes(data)
        manifest.append({'target':target, 'file':name, 'pixels':pixels, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()})
    (output/'manifest.json').write_text(json.dumps({'sourceSha256':review['sha256'], 'cropVisionReview':'pending', 'images':manifest}, indent=2)+'\n')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('sheet',type=Path); parser.add_argument('review',type=Path); parser.add_argument('output',type=Path)
    args = parser.parse_args()
    try:
        result = split_sheet(args.sheet, json.loads(args.review.read_text()), args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, f'{error}\n')
    print(f'Prepared {len(result)} square JPEGs. Inspect all crops with vision before attachment.')

