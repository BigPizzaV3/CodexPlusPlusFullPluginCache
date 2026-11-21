# Template file transport code

```python
"""Strict local transport only; never calculates or rewrites an Office file."""
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import re


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_resource(body, expected=None):
    data = body.encode('utf-8')
    if len(data) > 8400:
        raise ValueError('Resource too large')
    if expected and (len(data) != expected['resource_bytes'] or sha(data) != expected['resource_sha256']):
        raise ValueError('Incomplete or changed resource')
    match = re.fullmatch(r'# GovTribe template file data\n\n```json\n(.*)\n```\n', body, re.S)
    if not match:
        raise ValueError('Expected one complete JSON resource')
    return json.loads(match.group(1))


def check_index(index):
    if index.get('schema') != 'govtribe.template-base64-index.v1':
        raise ValueError('Wrong index schema')
    count = index['part_count']
    if type(count) is not int or not 1 <= count <= 256 or index['maximum_part_characters'] != 8192:
        raise ValueError('Unsupported part count or size')
    if index['encoding'] != 'base64' or index['encoded_characters'] != 4 * ((index['original']['bytes'] + 2) // 3):
        raise ValueError('Encoding identity mismatch')
    return index


def read_selection(body, descriptor, source_catalog_sha256):
    selection = read_resource(body, descriptor)
    if selection['schema'] != 'govtribe.template-file-selection.v1' or selection['source_catalog_sha256'] != source_catalog_sha256:
        raise ValueError('Wrong selected catalog projection')
    entry_bytes = (json.dumps(selection['catalog_entry'], sort_keys=True, indent=4, ensure_ascii=True) + '\n').encode()
    if sha(entry_bytes) != selection['catalog_entry_sha256']:
        raise ValueError('Changed catalog-entry projection')
    return selection


def match_selection(index, selection, template_id, role):
    if role not in ('master', 'example') or index['source_catalog_sha256'] != selection['source_catalog_sha256']:
        raise ValueError('Wrong catalog or role')
    entry = selection['catalog_entry']
    if entry['id'] != template_id or index['catalog_entry_sha256'] != selection['catalog_entry_sha256']:
        raise ValueError('Wrong selected template')
    if index['original'] != dict(entry[role], template_id=template_id, role=role):
        raise ValueError('Asset does not match selected catalog projection')
    return check_index(index)


def part_records(index, group_bodies=()):
    check_index(index)
    if 'parts' in index:
        if group_bodies or 'groups' in index:
            raise ValueError('Unexpected groups')
        records = index['parts']
    else:
        groups = index['groups']
        if len(groups) != len(group_bodies):
            raise ValueError('Missing or extra group')
        records = []
        for position, (expected, body) in enumerate(zip(groups, group_bodies), 1):
            group = read_resource(body, expected)
            if group['schema'] != 'govtribe.template-base64-group.v1' or group['order'] != position:
                raise ValueError('Wrong group order/schema')
            if group['first_part'] != expected['first_part'] or len(group['parts']) != expected['part_count']:
                raise ValueError('Changed group bounds')
            records.extend(group['parts'])
    if [p['order'] for p in records] != list(range(1, index['part_count'] + 1)):
        raise ValueError('Missing, duplicate or reordered part')
    if len({p['resource'] for p in records}) != len(records):
        raise ValueError('Duplicate resource')
    if sum(p['encoded_characters'] for p in records) != index['encoded_characters']:
        raise ValueError('Changed encoded length')
    return records


def save_part(index, expected, body, staging):
    part = read_resource(body, expected)
    if part['schema'] != 'govtribe.template-base64-part.v1' or part['encoding'] != 'base64' or part['order'] != expected['order']:
        raise ValueError('Wrong part identity')
    payload = part['base64'].encode('ascii')
    if not 0 < len(payload) <= 8192 or len(payload) % 4 or not re.fullmatch(rb'[A-Za-z0-9+/]*={0,2}', payload):
        raise ValueError('Invalid base64 payload')
    if expected['order'] != index['part_count'] and b'=' in payload:
        raise ValueError('Early padding')
    if len(payload) != expected['encoded_characters'] or sha(payload) != expected['payload_sha256']:
        raise ValueError('Changed or truncated payload')
    staging = Path(staging)
    if staging.is_symlink():
        raise ValueError('Symlink staging directory')
    staging.mkdir(parents=True, exist_ok=True)
    target = staging / ('part-%04d.b64' % expected['order'])
    if target.is_symlink():
        raise ValueError('Symlink part')
    if not target.exists():
        with target.open('xb') as stream:
            stream.write(payload)
    if target.read_bytes() != payload:
        raise ValueError('Saved-part readback mismatch')
    return target


def assemble(index, records, staging, output_root):
    check_index(index)
    if [p['order'] for p in records] != list(range(1, index['part_count'] + 1)):
        raise ValueError('Incomplete or reordered assembly')
    chunks = []
    for part in records:
        path = Path(staging) / ('part-%04d.b64' % part['order'])
        if path.is_symlink():
            raise ValueError('Symlink part')
        data = path.read_bytes()
        if len(data) != part['encoded_characters'] or sha(data) != part['payload_sha256']:
            raise ValueError('Saved part changed')
        chunks.append(data)
    encoded = b''.join(chunks)
    if len(encoded) != index['encoded_characters'] or sha(encoded) != index['encoded_sha256']:
        raise ValueError('Encoded file identity mismatch')
    decoded = base64.b64decode(encoded, validate=True)
    original = index['original']
    if len(decoded) != original['bytes'] or sha(decoded) != original['sha256']:
        raise ValueError('Decoded file identity mismatch')
    relative = original['path']
    if not isinstance(relative, str) or '\\' in relative or not relative.startswith('assets/') or any(p in ('', '.', '..') for p in relative.split('/')) or PurePosixPath(relative).is_absolute():
        raise ValueError('Unsafe output path')
    root = Path(output_root).resolve(strict=True)
    target = root / relative
    cursor = root
    for component in PurePosixPath(relative).parts[:-1]:
        cursor = cursor / component
        if cursor.is_symlink():
            raise ValueError('Symlink output ancestor')
        cursor.mkdir(exist_ok=True)
    if root not in target.parent.resolve().parents and target.parent.resolve() != root:
        raise ValueError('Output escapes task root')
    if target.is_symlink():
        raise ValueError('Symlink output')
    if not target.exists():
        with target.open('xb') as stream:
            stream.write(decoded)
    if target.read_bytes() != decoded:
        raise ValueError('Existing or saved output differs')
    return target
```
