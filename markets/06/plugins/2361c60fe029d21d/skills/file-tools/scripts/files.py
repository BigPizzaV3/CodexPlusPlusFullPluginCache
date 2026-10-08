"""FileStation's local file operations. No network calls; never overwrite files."""
import argparse
import csv
import io
import json
from pathlib import Path
import sys

MAX_BYTES = 50 * 1024 * 1024
MAX_PAGES = 500


def input_path(raw):
    path = Path(raw).resolve(strict=True)
    if not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError('Input must be a file no larger than 50 MiB.')
    return path


def save_new(raw, data):
    path = Path(raw).absolute()
    if path.exists() or path.is_symlink():
        raise ValueError('Output already exists. Choose a new filename.')
    if not path.parent.is_dir():
        raise ValueError('Output directory must already exist.')
    try:
        with path.open('xb') as stream:
            stream.write(data)
    except FileExistsError:
        raise ValueError('Output already exists. Choose a new filename.') from None
    return {'output': str(path), 'bytes': len(data)}


def read_pdf(raw):
    from pypdf import PdfReader
    path = input_path(raw)
    reader = PdfReader(path)
    if reader.is_encrypted:
        raise ValueError('Encrypted PDFs are unsupported. Use an authorized decrypted copy.')
    if not 1 <= len(reader.pages) <= MAX_PAGES:
        raise ValueError('PDF must contain 1–500 pages.')
    return reader


def page_indexes(spec, count):
    indexes = []
    for part in spec.split(','):
        bounds = part.strip().split('-')
        if len(bounds) not in (1, 2) or any(not b.isascii() or not b.isdigit() for b in bounds):
            raise ValueError('Use one-based pages such as 1,3-5.')
        first, last = int(bounds[0]), int(bounds[-1])
        if first < 1 or last < first or last > count:
            raise ValueError('Page range is outside the document or reversed.')
        indexes.extend(range(first - 1, last))
        if len(indexes) > MAX_PAGES:
            raise ValueError('Choose no more than 500 pages.')
    if len(set(indexes)) != len(indexes):
        raise ValueError('Duplicate pages are not accepted; use distinct ranges.')
    return indexes


def pdf_operation(args):
    from pypdf import PdfWriter, PdfReader
    writer = PdfWriter()
    if args.operation == 'merge':
        total = 0
        for raw in args.inputs:
            reader = read_pdf(raw)
            total += len(reader.pages)
            if total > MAX_PAGES:
                raise ValueError('Merged PDF would exceed 500 pages.')
            for page in reader.pages:
                writer.add_page(page)
    else:
        reader = read_pdf(args.input)
        if args.operation == 'text':
            text = '\n\n'.join(f'--- Page {i + 1} ---\n{page.extract_text() or ""}' for i, page in enumerate(reader.pages))
            result = save_new(args.output, text.encode('utf-8'))
            return {**result, 'pages': len(reader.pages), 'note': 'Selectable text only; OCR was not performed.'}
        indexes = page_indexes(args.pages, len(reader.pages))
        if args.operation == 'extract':
            for index in indexes:
                writer.add_page(reader.pages[index])
        else:
            for index, page in enumerate(reader.pages):
                copied = writer.add_page(page)
                if index in indexes:
                    copied.rotate(args.degrees)
    # Copy only pages; do not copy document-level actions or attachments.
    buffer = io.BytesIO()
    writer.write(buffer)
    data = buffer.getvalue()
    verified = PdfReader(io.BytesIO(data))
    if len(verified.pages) != len(writer.pages):
        raise ValueError('Output page-count verification failed.')
    result = save_new(args.output, data)
    return {**result, 'pages': len(verified.pages), 'note': 'Review appearance, forms, links and signatures. Page copying is not a sanitization guarantee.'}


def csv_to_json(args):
    with input_path(args.input).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.reader(stream)
        headers = next(reader, None)
        if not headers or any(not h.strip() for h in headers) or len(set(headers)) != len(headers):
            raise ValueError('CSV requires unique, non-empty column names.')
        rows = []
        for row in reader:
            if len(row) != len(headers):
                raise ValueError('CSV row width does not match its header.')
            rows.append(dict(zip(headers, row)))
    payload = json.dumps(rows, ensure_ascii=False, indent=2).encode('utf-8')
    return {**save_new(args.output, payload), 'records': len(rows), 'note': 'CSV cell values remain strings; leading zeros are preserved.'}


def json_format(args):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate JSON keys would lose data.')
            result[key] = value
        return result
    def reject_constant(value):
        raise ValueError('Non-standard JSON number: ' + value)
    value = json.loads(input_path(args.input).read_text(encoding='utf-8-sig'), object_pairs_hook=pairs, parse_constant=reject_constant)
    return save_new(args.output, (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8'))


def image_operation(args):
    from PIL import Image, ImageOps
    Image.MAX_IMAGE_PIXELS = 25_000_000
    with Image.open(input_path(args.input)) as source:
        if getattr(source, 'n_frames', 1) != 1:
            raise ValueError('Animated or multi-frame images are unsupported.')
        if source.width * source.height > Image.MAX_IMAGE_PIXELS:
            raise ValueError('Image exceeds 25 megapixels.')
        image = ImageOps.exif_transpose(source)
        if image.mode not in ('RGB', 'RGBA', 'L', 'LA'):
            image = image.convert('RGBA' if 'transparency' in image.info else 'RGB')
        if args.width:
            image.thumbnail((args.width, args.height), Image.Resampling.LANCZOS)
        if args.format == 'JPEG':
            if image.mode in ('RGBA', 'LA') or 'transparency' in image.info:
                rgba = image.convert('RGBA')
                background = Image.new('RGB', image.size, 'white')
                background.paste(rgba, mask=rgba.getchannel('A'))
                image = background
            else:
                image = image.convert('RGB')
        if args.format == 'WEBP' and image.mode not in ('RGB', 'RGBA'):
            image = image.convert('RGBA' if image.mode == 'LA' else 'RGB')
        # Strip metadata from the exported image.
        clean = Image.new(image.mode, image.size)
        clean.paste(image)
        buffer = io.BytesIO()
        clean.save(buffer, format=args.format)
        data = buffer.getvalue()
        with Image.open(io.BytesIO(data)) as check:
            check.load()
            width, height = check.size
    return {**save_new(args.output, data), 'width': width, 'height': height, 'note': 'Aspect ratio preserved; no upscaling. JPEG uses white behind transparent pixels. Metadata removed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='operation', required=True)
    merge = commands.add_parser('merge')
    merge.add_argument('inputs', nargs='+')
    merge.add_argument('--output', required=True)
    for name in ('extract', 'rotate', 'text', 'csv-to-json', 'json-format', 'image'):
        cmd = commands.add_parser(name)
        cmd.add_argument('input')
        cmd.add_argument('--output', required=True)
        if name in ('extract', 'rotate'):
            cmd.add_argument('--pages', required=True)
        if name == 'rotate':
            cmd.add_argument('--degrees', type=int, choices=(90, 180, 270), required=True)
        if name == 'image':
            cmd.add_argument('--format', choices=('PNG', 'JPEG', 'WEBP'), required=True)
            cmd.add_argument('--width', type=int)
            cmd.add_argument('--height', type=int)
    args = parser.parse_args()
    try:
        if args.operation in ('merge', 'extract', 'rotate', 'text'):
            result = pdf_operation(args)
        elif args.operation == 'csv-to-json':
            result = csv_to_json(args)
        elif args.operation == 'json-format':
            result = json_format(args)
        else:
            if (args.width is None) != (args.height is None) or (args.width is not None and not (1 <= args.width <= 10000 and 1 <= args.height <= 10000)):
                raise ValueError('Provide both width and height between 1 and 10000, or neither.')
            result = image_operation(args)
        print(json.dumps(result, ensure_ascii=False))
    except Exception as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
