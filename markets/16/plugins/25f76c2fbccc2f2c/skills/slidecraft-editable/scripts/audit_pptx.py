"""Audit native PPTX content and text editability using the standard library."""
import argparse
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main','c':'http://schemas.openxmlformats.org/drawingml/2006/chart'}

def normalize(text):
    return ' '.join(text.split())

def audit(filename, expect):
    errors, report = [], []
    with zipfile.ZipFile(filename) as z:
        bad = z.testzip()
        if bad:
            errors.append('Corrupt ZIP member: '+bad)
        names = sorted((s for s in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',s)),key=lambda s:int(re.search(r'(\d+)\.xml$',s).group(1)))
        if expect.get('slideCount') is not None and len(names) != expect['slideCount']:
            errors.append('Unexpected slide count')
        for i,name in enumerate(names,1):
            root = ET.fromstring(z.read(name))
            objects = [s for s in root.findall('.//p:sp',NS) if s.findall('.//a:t',NS)]
            texts = [' '.join(''.join(t.text or '' for t in p.findall('.//a:t',NS)) for p in s.findall('.//a:p',NS)) for s in objects]
            alltext = normalize(' '.join(texts))
            body = [s.find('p:txBody/a:bodyPr',NS) for s in objects]
            noauto = sum(b is not None and b.find('a:noAutofit',NS) is not None for b in body)
            row = {'slide':i,'nativeTextBoxes':len(objects),'nativeTables':len(root.findall('.//a:tbl',NS)),'nativeCharts':len(root.findall('.//c:chart',NS)),'pictures':len(root.findall('.//p:pic',NS)),'textBoxesWithoutAutofit':noauto}
            report.append(row)
            for rule in expect.get('slides',[]):
                if rule.get('slide') != i:
                    continue
                if rule.get('nativeText') and not objects:
                    errors.append(f'Slide {i}: no native text')
                if rule.get('noAutofit') and noauto != len(objects):
                    errors.append(f'Slide {i}: text has unspecified or automatic font fitting')
                for field in ['nativeTables','nativeCharts']:
                    if field in rule and row[field] < rule[field]:
                        errors.append(f'Slide {i}: missing {field}')
                for text in rule.get('requiredTexts',[]):
                    if normalize(text) not in alltext:
                        errors.append(f'Slide {i}: missing native text: {text}')
        actual = {r['slide'] for r in report}
        for rule in expect.get('slides',[]):
            if rule.get('slide') not in actual:
                errors.append('Expected slide does not exist')
    return {'passed':not errors,'slides':report,'errors':errors}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pptx')
    parser.add_argument('--expect')
    args = parser.parse_args()
    if args.expect:
        with open(args.expect,encoding='utf-8') as f:
            expect = json.load(f)
    else:
        expect = {}
    result = audit(args.pptx,expect)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(0 if result['passed'] else 1)
