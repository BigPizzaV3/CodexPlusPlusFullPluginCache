#!/usr/bin/env python3
"""Rebuild the approved fictional diagrams with the shared consulting engine.

The example modules contain fixed fictional copy. They are deliberately excluded
from the normal SlideSpec template registry, so case data cannot silently turn
into the sample's claims. No engine is duplicated in the distributed source tree.
"""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
P = 'http://schemas.openxmlformats.org/presentationml/2006/main'


def apply_highground(deck, geometry):
    """Replace every named Venn placeholder before publishing the output file."""
    ns = {'a': A, 'p': P}
    g = json.loads(geometry.read_text(encoding='utf-8'))
    updated = deck.with_suffix('.geometry.pptx')
    count = 0
    with zipfile.ZipFile(deck) as src, zipfile.ZipFile(updated, 'w', zipfile.ZIP_DEFLATED) as dst:
        for info in src.infolist():
            data = src.read(info.filename)
            if re.fullmatch(r'ppt/slides/slide\d+\.xml', info.filename):
                xml = ET.fromstring(data)
                changed = False
                for shape in xml.findall('.//p:sp', ns):
                    name = shape.find('p:nvSpPr/p:cNvPr', ns)
                    if name is None or name.get('name') != 'highground-region':
                        continue
                    props = shape.find('p:spPr', ns)
                    preset = props.find('a:prstGeom', ns)
                    if preset is None:
                        raise ValueError('highground placeholder geometry is missing')
                    index = list(props).index(preset)
                    props.remove(preset)
                    custom = ET.Element(f'{{{A}}}custGeom')
                    for tag in ('avLst', 'gdLst', 'ahLst', 'cxnLst'):
                        ET.SubElement(custom, f'{{{A}}}{tag}')
                    ET.SubElement(custom, f'{{{A}}}rect', {'l': '0', 't': '0', 'r': 'r', 'b': 'b'})
                    paths = ET.SubElement(custom, f'{{{A}}}pathLst')
                    path = ET.SubElement(paths, f'{{{A}}}path', {'w': '100000', 'h': '100000'})
                    for k, (x, y) in enumerate(g['points']):
                        step = ET.SubElement(path, f'{{{A}}}' + ('moveTo' if k == 0 else 'lnTo'))
                        ET.SubElement(step, f'{{{A}}}pt', {
                            'x': str(round((x - g['x']) / g['w'] * 100000)),
                            'y': str(round((y - g['y']) / g['h'] * 100000)),
                        })
                    ET.SubElement(path, f'{{{A}}}close')
                    props.insert(index, custom)
                    count += 1
                    changed = True
                if changed:
                    data = ET.tostring(xml, encoding='utf-8', xml_declaration=True)
            dst.writestr(info, data)
    if count != 1:
        raise ValueError(f'expected one highground region, found {count}')
    updated.replace(deck)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('example', choices=('frameworks', 'marketing'))
    parser.add_argument('output', type=Path)
    parser.add_argument('--node', default='node')
    parser.add_argument('--module-dir', type=Path)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    out = args.output.resolve()
    if out.suffix.lower() != '.pptx':
        parser.error('output must end in .pptx')
    if out.exists() and not args.overwrite:
        parser.error('output exists; use another path or --overwrite')
    out.parent.mkdir(parents=True, exist_ok=True)
    examples = ROOT / 'assets/examples'
    # Overlay only the trusted bundled samples into a temporary copy of the
    # existing engine. Normal build_deck.py never exposes fixed-copy templates.
    with tempfile.TemporaryDirectory(prefix='.diagram-examples-', dir=out.parent) as temp:
        temp = Path(temp)
        engine = temp / 'engine'
        shutil.copytree(ROOT / 'vendor', engine / 'vendor')
        shutil.copytree(ROOT / 'assets/logo', engine / 'assets/logo')
        shutil.copyfile(ROOT / 'assets/palette.json', engine / 'assets/palette.json')
        (engine / 'assets/examples').mkdir()
        shutil.copyfile(examples / 'venn-geometry.json', engine / 'assets/examples/venn-geometry.json')
        (engine / 'scripts').mkdir()
        shutil.copyfile(ROOT / 'scripts/build_deck.py', engine / 'scripts/build_deck.py')
        pipeline = engine / 'vendor/consulting/pipeline'
        for module in (examples / 'archetypes').glob('*.mjs'):
            shutil.copyfile(module, pipeline / 'scripts/archetypes' / module.name)
        schema_path = pipeline / 'slide-spec/schema.json'
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        schema['$defs']['slide']['properties']['template']['enum'].extend(
            ['marketing_3c', 'marketing_stp', 'marketing_kpi', 'marketing_extended'])
        schema_path.write_text(json.dumps(schema, ensure_ascii=False), encoding='utf-8')
        candidate = temp / 'example.pptx'
        cmd = [sys.executable, str(engine / 'scripts/build_deck.py'),
               str(examples / f'{args.example}.json'), str(candidate), '--node', args.node]
        if args.module_dir:
            cmd.extend(['--module-dir', str(args.module_dir.resolve())])
        subprocess.run(cmd, check=True)
        if args.example == 'frameworks':
            apply_highground(candidate, examples / 'venn-geometry.json')
        if out.exists() and not args.overwrite:
            parser.error('output appeared during build; refusing to overwrite')
        candidate.replace(out)
    print(out)


if __name__ == '__main__':
    main()
