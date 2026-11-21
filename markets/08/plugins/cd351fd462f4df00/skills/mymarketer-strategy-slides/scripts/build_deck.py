#!/usr/bin/env python3
"""Apply the default skin and run the bundled consulting exporter."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='SlideSpec JSON')
    parser.add_argument('output', type=Path, help='Output .pptx')
    parser.add_argument('--node', default='node')
    parser.add_argument('--module-dir', type=Path, help='Directory containing pptxgenjs')
    parser.add_argument('--palette', type=Path, help='Alternative palette defaults')
    parser.add_argument('--overwrite', action='store_true')
    parser.add_argument('--strategy-content-hash', help='Server-returned strategyContentHash for a formal draft')
    args = parser.parse_args()
    out = args.output.resolve()
    if out.suffix.lower() != '.pptx':
        parser.error('output must end in .pptx')
    if out.exists() and not args.overwrite:
        parser.error('output exists; use another path or --overwrite')
    if args.strategy_content_hash and not re.fullmatch(r'[0-9a-f]{64}', args.strategy_content_hash):
        parser.error('strategy-content-hash must be a lowercase SHA-256 returned by the server')
    spec = json.loads(args.input.read_text(encoding='utf-8'))
    if not isinstance(spec, dict) or not isinstance(spec.get('slides'), list) or not spec['slides']:
        parser.error('input must be a SlideSpec object with a nonempty slides array')
    base = json.loads((args.palette or ROOT / 'assets/palette.json').read_text(encoding='utf-8'))
    custom = spec.get('palette', {})
    if not isinstance(base, dict) or not isinstance(custom, dict):
        parser.error('palette must be an object')
    palette = {**base, **custom}  # Explicit deck colors take precedence.
    allowed = {'ink', 'navy', 'muted', 'hair', 'blue', 'cyan', 'rose', 'warning', 'green', 'softYellow', 'softBlue'}
    if any(k not in allowed or not isinstance(v, str) or not re.fullmatch(r'[0-9A-Fa-f]{6}', v) for k, v in palette.items()):
        parser.error('palette requires supported keys and six-digit hex values without #')
    spec['palette'] = palette
    for i, slide in enumerate(spec['slides'], 1):
        if not isinstance(slide, dict) or not isinstance(slide.get('source'), str) or not slide['source'].strip():
            parser.error(f'slide {i}: a nonempty source is required')
    pipeline = ROOT / 'vendor/consulting/pipeline'
    env = os.environ.copy()
    if args.module_dir:
        env['PPTXGENJS_MODULE_DIR'] = str(args.module_dir.resolve())
    out.parent.mkdir(parents=True, exist_ok=True)
    # Build beside the destination for an atomic final replacement; no partial final file.
    with tempfile.TemporaryDirectory(prefix='.strategy-slides-', dir=out.parent) as temp:
        temp = Path(temp)
        source = temp / 'deck.json'
        source.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        raw = temp / 'raw.pptx'
        for script, extra in [('validate_spec.mjs', []), ('export_spec_to_editable_pptx.mjs', [str(raw)])]:
            subprocess.run([args.node, str(pipeline / 'scripts' / script), str(source), *extra], env=env, check=True)
        # Remove upstream demo metadata only. Slide shapes, charts and typography stay unchanged.
        candidate = temp / 'final.pptx'
        with zipfile.ZipFile(raw) as src, zipfile.ZipFile(candidate, 'w', zipfile.ZIP_DEFLATED) as dst:
            for item in src.infolist():
                data = src.read(item.filename)
                if item.filename in ('docProps/core.xml', 'docProps/app.xml'):
                    tree = ET.fromstring(data)
                    for element in tree.iter():
                        tag = element.tag.rsplit('}', 1)[-1]
                        if tag in ('creator', 'lastModifiedBy', 'Company'):
                            element.text = 'MyMarketer Strategy Slides'
                        elif tag == 'subject':
                            element.text = 'Marketing strategy presentation'
                    data = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
                dst.writestr(item, data)
        if args.strategy_content_hash:
            from pptx import Presentation
            from pptx.util import Inches, Pt
            from pptx.dml.color import RGBColor
            presentation = Presentation(candidate)
            frame = presentation.slides[-1].shapes.add_textbox(
                Inches(0.35), presentation.slide_height - Inches(0.2),
                presentation.slide_width - Inches(0.7), Inches(0.15),
            ).text_frame
            frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
            paragraph = frame.paragraphs[0]
            paragraph.text = f'MyMarketer strategy: {args.strategy_content_hash}'
            paragraph.font.size = Pt(6.5)
            paragraph.font.color.rgb = RGBColor.from_string('737373')
            presentation.save(candidate)
        if out.exists() and not args.overwrite:
            parser.error('output appeared during build; refusing to overwrite')
        candidate.replace(out)
    print(out)


if __name__ == '__main__':
    main()
