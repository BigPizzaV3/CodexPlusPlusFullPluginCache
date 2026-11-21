"""Normalize media names, check image contracts, and restore exact slide dimensions."""
import argparse
import hashlib
import json
import posixpath
import zipfile
from pathlib import Path, PurePosixPath
from lxml import etree as ET

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS = {'p': P, 'a': A, 'r': R}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

def resolve(part, target):
    return posixpath.normpath(target.lstrip('/') if target.startswith('/') else posixpath.join(posixpath.dirname(part), target))

def inspect(filename, contracts):
    errors, checked = [], []
    with zipfile.ZipFile(filename) as z:
        if z.testzip():
            errors.append('Corrupt package')
        media = [n for n in z.namelist() if n.startswith('ppt/media/') and not n.endswith('/')]
        stems = [PurePosixPath(n).stem.casefold() for n in media]
        if len(stems) != len(set(stems)):
            errors.append('Ambiguous media basenames')
        for c in contracts:
            part = f"ppt/slides/slide{c['slide']}.xml"
            relpart = f"ppt/slides/_rels/slide{c['slide']}.xml.rels"
            root = ET.fromstring(z.read(part))
            rels = {r.get('Id'): resolve(part, r.get('Target')) for r in ET.fromstring(z.read(relpart))}
            matches = []
            for pic in root.findall('.//p:pic', NS):
                off = pic.find('p:spPr/a:xfrm/a:off', NS)
                ext = pic.find('p:spPr/a:xfrm/a:ext', NS)
                if off is None or ext is None:
                    continue
                actual = [int(off.get('x')), int(off.get('y')), int(ext.get('cx')), int(ext.get('cy'))]
                expected = [round(c[k] * 9525) for k in ('x', 'y', 'w', 'h')]
                # contain-fit changes the encoded frame: accept center and smaller size.
                if abs(actual[0]+actual[2]/2-expected[0]-expected[2]/2)>19050 or abs(actual[1]+actual[3]/2-expected[1]-expected[3]/2)>19050:
                    continue
                if actual[2]>expected[2]+19050 or actual[3]>expected[3]+19050:
                    continue
                blip = pic.find('.//a:blip', NS)
                target = rels.get(blip.get('{'+R+'}embed')) if blip is not None else None
                if target and target in z.namelist():
                    matches.append(hashlib.sha256(z.read(target)).hexdigest())
            passed = c['sha256'] in matches
            checked.append({'slide':c['slide'], 'role':c.get('role','image'), 'passed':passed})
            if not passed:
                errors.append(f"Slide {c['slide']}: original {c.get('role','image')} bytes missing at expected position")
        size = ET.fromstring(z.read('ppt/presentation.xml')).find('p:sldSz', NS)
    return {'passed': not errors, 'errors': errors, 'imageContracts': checked, 'slideSizeEmu': [int(size.get('cx')), int(size.get('cy'))]}

def normalize(source, output, size):
    if Path(output).exists():
        raise ValueError('Output already exists')
    with zipfile.ZipFile(source) as z, zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as out:
        media = [n for n in z.namelist() if n.startswith('ppt/media/') and not n.endswith('/')]
        renames = {n: f'ppt/media/slidecraft_asset_{i:03d}{PurePosixPath(n).suffix}' for i,n in enumerate(media,1)}
        for name in z.namelist():
            data = z.read(name)
            if name.endswith('.rels'):
                root = ET.fromstring(data)
                part = posixpath.join(posixpath.dirname(posixpath.dirname(name)), posixpath.basename(name)[:-5])
                for rel in root:
                    if rel.get('TargetMode') == 'External':
                        continue
                    target = resolve(part, rel.get('Target',''))
                    if target in renames:
                        rel.set('Target', posixpath.relpath(renames[target], posixpath.dirname(part)))
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            elif name == '[Content_Types].xml':
                root = ET.fromstring(data)
                for node in root:
                    target = node.get('PartName','').lstrip('/')
                    if target in renames:
                        node.set('PartName','/'+renames[target])
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            elif name == 'ppt/presentation.xml' and size:
                root = ET.fromstring(data)
                node = root.find('p:sldSz', NS)
                node.set('cx', str(size[0])); node.set('cy', str(size[1]))
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            out.writestr(renames.get(name,name), data)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source'); p.add_argument('--output'); p.add_argument('--size'); p.add_argument('--contracts')
    args = p.parse_args()
    size = [int(n) for n in args.size.split(',')] if args.size else None
    if args.output:
        normalize(args.source, args.output, size)
    contracts = json.loads(Path(args.contracts).read_text()) if args.contracts else []
    result = inspect(args.output or args.source, contracts)
    print(json.dumps(result))
    raise SystemExit(0 if result['passed'] else 1)
