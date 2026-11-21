"""Template-based SAP Cloud Integration iFlow ZIP generator.
Requires a genuine SAP-exported design-time iFlow ZIP, not a runtime JAR.
"""
from __future__ import annotations
import io, json, re, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

BASE = 'src/main/resources/'
FLOW = BASE + 'scenarioflows/integrationflow/'
SAFE_NAME = re.compile(r'^[A-Za-z][A-Za-z0-9_.-]{0,119}$')

class TemplateError(ValueError):
    pass

def check_name(value: str) -> str:
    if not SAFE_NAME.fullmatch(value):
        raise TemplateError('Technical ID must start with a letter and use only letters, digits, _, - or . (max 120 chars)')
    return value

def inspect_template(archive: bytes) -> dict:
    try:
        with zipfile.ZipFile(io.BytesIO(archive)) as z:
            entries = z.namelist()
            if z.testzip() is not None:
                raise TemplateError('Damaged ZIP entry')
            for n in entries:
                if n.startswith('/') or '..' in Path(n).parts or '\\' in n:
                    raise TemplateError('Unsafe ZIP entry')
            models = [n for n in entries if n.startswith(FLOW) and n.endswith('.iflw')]
            if len(models) != 1:
                raise TemplateError('Template must contain exactly one integrationflow .iflw')
            if 'META-INF/MANIFEST.MF' not in entries:
                raise TemplateError('Missing META-INF/MANIFEST.MF')
            xml = z.read(models[0])
            ET.fromstring(xml)
            return {'model': models[0], 'entries': len(entries), 'manifest': z.read('META-INF/MANIFEST.MF').decode('utf-8', 'replace')}
    except zipfile.BadZipFile as exc:
        raise TemplateError('Invalid ZIP file') from exc

def generate(template: bytes, technical_id: str, display_name: str, description: str = '', scripts: dict[str,str] | None = None) -> tuple[bytes, dict]:
    """Rename a SAP design-time model and insert script resources.

    Does not automatically bind scripts to BPMN processing steps. The exported
    template's process and adapter wiring remains the authoritative design.
    """
    technical_id = check_name(technical_id)
    if not display_name.strip() or len(display_name) > 160:
        raise TemplateError('Display name required (max 160 chars)')
    info = inspect_template(template)
    old_path = info['model']
    old_id = Path(old_path).stem
    new_path = FLOW + technical_id + '.iflw'
    scripts = scripts or {}
    for name in scripts:
        if not name.endswith('.groovy') or not SAFE_NAME.fullmatch(name[:-7]):
            raise TemplateError('Script filename must be a safe .groovy name')
    output = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(template), 'r') as src, zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as dest:
        existing = set(src.namelist())
        for entry in src.infolist():
            name = entry.filename
            data = src.read(entry)
            target = new_path if name == old_path else name
            if name == old_path:
                # XML-aware update of project/model properties; preserve SAP extension elements.
                root = ET.fromstring(data)
                for node in root.iter():
                    for attr, val in list(node.attrib.items()):
                        if val == old_id and (attr.endswith('id') or attr.endswith('name') or attr.endswith('value')):
                            node.attrib[attr] = technical_id
                        elif val == old_id + '.iflw':
                            node.attrib[attr] = technical_id + '.iflw'
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            elif name == 'META-INF/MANIFEST.MF':
                text = data.decode('utf-8', 'replace')
                text = re.sub(r'(?m)^(Bundle-SymbolicName:\s*).*$', lambda m:m.group(1)+technical_id, text)
                text = re.sub(r'(?m)^(Bundle-Name:\s*).*$', lambda m:m.group(1)+display_name, text)
                data = text.encode('utf-8')
            elif name == 'metainfo.prop':
                text = data.decode('utf-8', 'replace')
                text = re.sub(r'(?m)^(name\s*=\s*).*$', lambda m:m.group(1)+display_name, text)
                data = text.encode('utf-8')
            if target in [BASE+'script/'+n for n in scripts]:
                continue
            dest.writestr(target, data)
        for name, content in scripts.items():
            dest.writestr(BASE+'script/'+name, '// https://agenticintegrationhub.com/\n'+content)
    result = output.getvalue()
    inspect_template(result)
    return result, {'technical_id':technical_id,'display_name':display_name,'description':description,'template_model':old_id,'output_model':technical_id,'scripts_added':list(scripts), 'warning':'SAP tenant import and BPMN processing-step validation is required; newly added scripts are not automatically wired into process steps.'}
