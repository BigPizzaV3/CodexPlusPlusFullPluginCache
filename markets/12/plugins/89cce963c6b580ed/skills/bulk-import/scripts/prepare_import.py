"""Offline CSV preparation. No credentials, network calls or database writes."""
import argparse
import csv
from datetime import date
import hashlib
import io
import json
from pathlib import Path
import re
import unicodedata
import uuid

RESOURCES = ('suppliers', 'products', 'controlled-documents')
CONTROLS = {'source_row_id', 'operation', 'target_id', 'owner_name', 'clear_fields'}

def normal(value):
    return unicodedata.normalize('NFKC', str(value or '')).strip().casefold()

def load_profile(resource):
    if resource not in RESOURCES:
        raise ValueError('Unsupported resource')
    return json.loads((Path(__file__).resolve().parents[1] / 'references' / 'profiles' / (resource + '.json')).read_text(encoding='utf-8'))

def parse_value(name, value, spec):
    types = spec.get('type', 'string')
    types = types if isinstance(types, list) else [types]
    if 'boolean' in types:
        mapped = {'true': True, 'false': False, 'yes': True, 'no': False, '1': True, '0': False}
        if value.casefold() not in mapped:
            raise ValueError(name + ': expected true/false, yes/no or 1/0')
        result = mapped[value.casefold()]
    elif 'integer' in types:
        if not re.fullmatch(r'-?\d+', value):
            raise ValueError(name + ': expected integer')
        result = int(value)
    elif 'object' in types or 'array' in types:
        result = json.loads(value)
        expected = dict if 'object' in types else list
        if not isinstance(result, expected):
            raise ValueError(name + ': wrong JSON type')
    else:
        result = value
    if spec.get('format') == 'uuid':
        try:
            result = str(uuid.UUID(value))
        except (ValueError, AttributeError):
            raise ValueError(name + ': unresolved or invalid UUID') from None
    if spec.get('format') == 'date':
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
            raise ValueError(name + ': date must be YYYY-MM-DD')
        date.fromisoformat(value)
    if 'enum' in spec and result not in spec['enum']:
        raise ValueError(name + ': unsupported value')
    if name == 'contact_email' and not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', value):
        raise ValueError(name + ': check email syntax')
    if isinstance(result, int) and not isinstance(result, bool):
        if 'minimum' in spec and result < spec['minimum']:
            raise ValueError(name + ': below minimum')
        if 'maximum' in spec and result > spec['maximum']:
            raise ValueError(name + ': above maximum')
    return result

def prepare(resource, raw, existing=None, defer_protected=False):
    profile = load_profile(resource)
    text = raw.decode('utf-8-sig')
    reader = csv.DictReader(io.StringIO(text, newline=''))
    headers = reader.fieldnames or []
    if not headers or any(not h or h != h.strip() for h in headers):
        raise ValueError('CSV headers must be nonblank and have no outer whitespace')
    if len(headers) != len(set(headers)):
        raise ValueError('Duplicate CSV headers')
    allowed = set(profile['create']['properties']) | set(profile['update']['properties']) | CONTROLS
    unknown = sorted(set(headers) - allowed)
    if unknown:
        raise ValueError('Unmapped columns: ' + ', '.join(unknown))
    records = []
    complete = False
    organisation = None
    if existing is not None:
        if not isinstance(existing, dict) or existing.get('resource') != resource:
            raise ValueError('Target snapshot resource mismatch')
        organisation = existing.get('organisation_id')
        if not organisation:
            raise ValueError('Target snapshot organisation is required')
        if not isinstance(existing.get('complete'), bool) or not isinstance(existing.get('data'), list):
            raise ValueError('Target snapshot needs boolean complete and data array')
        records = existing['data']
        complete = existing['complete']
        if any(not isinstance(r, dict) or not r.get('id') for r in records):
            raise ValueError('Every target record needs an ID')
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate target record IDs')
        if any(r.get('org_id') not in (None, organisation) for r in records):
            raise ValueError('Target records cross organisation boundary')
    by_id = {r['id']: r for r in records}
    identity = profile['identity_field']
    result = []
    for row_number, source in enumerate(reader, 2):
        if None in source or any(value is None for value in source.values()):
            raise ValueError('Malformed CSV row ' + str(row_number))
        if all(not value.strip() for value in source.values()):
            continue
        values = {k: v.strip() for k, v in source.items()}
        row = {'source_row': row_number, 'source_row_id': values.get('source_row_id') or str(row_number),
               'operation': values.get('operation') or 'create', 'classification': 'invalid',
               'target_id': values.get('target_id') or None, 'payload': {}, 'errors': [],
               'warnings': [], 'deferred_fields': {}, 'preflight_required': []}
        errors = row['errors']
        operation = row['operation']
        if operation not in ('create', 'update'):
            errors.append('Operation must be create or update')
            result.append(row)
            continue
        if row['target_id']:
            try:
                row['target_id'] = str(uuid.UUID(row['target_id']))
            except ValueError:
                errors.append('Invalid target UUID')
        if operation == 'create' and row['target_id']:
            errors.append('Create must not carry target_id')
        schema = profile[operation]
        protected = set(profile['protected_fields'])
        for name, value in values.items():
            if name in CONTROLS or not value:
                continue
            if name in protected:
                row['deferred_fields'][name] = value
                continue
            if name not in schema['properties']:
                errors.append(name + ': not writable for ' + operation)
                continue
            try:
                row['payload'][name] = parse_value(name, value, schema['properties'][name])
            except (ValueError, TypeError, json.JSONDecodeError) as exc:
                errors.append(str(exc))
        if values.get('owner_name') and not row['payload'].get('owner_id'):
            errors.append('owner_name needs an authorised user lookup; no ID was resolved')
        if operation == 'create':
            for required in schema.get('required', []):
                if required not in row['payload'] or row['payload'][required] == '':
                    errors.append(required + ': required')
        try:
            clears = json.loads(values.get('clear_fields') or '[]')
            if not isinstance(clears, list) or any(not isinstance(c, str) for c in clears):
                raise ValueError('clear_fields must be a JSON array of field names')
            if len(clears) != len(set(clears)):
                errors.append('Duplicate clear_fields')
            for name in clears:
                spec = schema['properties'].get(name, {})
                if operation != 'update':
                    errors.append('Explicit clears apply only to updates')
                elif name in protected or 'null' not in spec.get('type', []):
                    errors.append(name + ': clear not permitted')
                elif name in row['payload']:
                    errors.append(name + ': cannot set and clear together')
                else:
                    row['payload'][name] = None
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
        key = normal(values.get(identity))
        matches = [r for r in records if key and normal(r.get(identity)) == key]
        current = by_id.get(row['target_id']) if row['target_id'] else None
        ambiguity = None
        duplicate = None
        if row['target_id']:
            if current is None:
                errors.append('Target ID not verified in the supplied snapshot')
            elif any(r['id'] != current['id'] for r in matches):
                ambiguity = 'ID and identity field point to different records'
        elif len(matches) > 1:
            ambiguity = 'Multiple records match the identity field'
        elif matches:
            current = matches[0]
            if resource == 'controlled-documents':
                ambiguity = 'Document number requires record ID and revision-context review'
            elif normal(values.get('name')) and normal(values.get('name')) != normal(current.get('name')):
                ambiguity = 'Code match has a conflicting name; review identity'
            elif operation == 'create':
                duplicate = 'Create-only row matches an existing record'
            else:
                row['target_id'] = current['id']
        else:
            title = values.get('title') if resource == 'controlled-documents' else values.get('name')
            title_field = 'title' if resource == 'controlled-documents' else 'name'
            if title and any(normal(r.get(title_field)) == normal(title) for r in records):
                ambiguity = 'Name/title match needs explicit identity review'
        if operation == 'update' and not row['target_id'] and not ambiguity:
            errors.append('Update target could not be resolved')
        if current and resource == 'controlled-documents' and current.get('status') == 'approved':
            errors.append('Approved document revision cannot be updated here')
        if row['payload'].get('certification_expiry'):
            if date.fromisoformat(row['payload']['certification_expiry']) < date.today():
                row['warnings'].append('Source certification expiry is in the past; no status change proposed')
        if row['deferred_fields']:
            row['warnings'].append('Protected source decisions remain deferred; they are not imported')
        if errors:
            row['classification'] = 'invalid'
        elif ambiguity:
            row['classification'] = 'ambiguous'
            row['errors'].append(ambiguity)
        elif duplicate:
            row['classification'] = 'duplicate'
            row['warnings'].append(duplicate)
        elif row['deferred_fields'] and not defer_protected:
            row['classification'] = 'deferred'
        elif operation == 'update' and current:
            row['payload'] = {k: v for k, v in row['payload'].items() if current.get(k) != v}
            row['classification'] = 'update' if row['payload'] else 'unchanged'
        else:
            row['classification'] = operation
        if row['classification'] in ('create', 'update'):
            row['preflight_required'] = ['live descriptor', 'verified connection/organisation', 'exact batch approval']
            if not complete:
                row['preflight_required'].append('complete relevant visible target retrieval')
            if operation == 'create':
                row['preflight_required'].append('verify live create defaults')
            if resource == 'suppliers' and operation == 'create':
                row['preflight_required'].append('verify safe prospective supplier default without production trial create')
        row['_source_key'] = key
        row['_source_name'] = normal(values.get('name') or values.get('title'))
        result.append(row)
    # Source collisions must not silently collapse, including duplicate explicit row IDs.
    groups = {}
    for row in result:
        for key in [('row_id', row['source_row_id']),
                    ('target', row['target_id']),
                    ('identity', row.get('_source_key')),
                    ('name_only', row.get('_source_name') if not row.get('_source_key') and not row['target_id'] else None)]:
            if key[1]:
                groups.setdefault(key, []).append(row)
    for key, rows in groups.items():
        if len(rows) > 1:
            for row in rows:
                if row['classification'] != 'invalid':
                    row['classification'] = 'duplicate'
                row['errors'].append('Repeated source ' + key[0] + ' requires review')
    for row in result:
        row.pop('_source_key', None)
        row.pop('_source_name', None)
    counts = {label: sum(r['classification'] == label for r in result)
              for label in ['create', 'update', 'unchanged', 'invalid', 'ambiguous', 'duplicate', 'deferred']}
    return {'format_version': 1, 'resource': resource, 'source_sha256': hashlib.sha256(raw).hexdigest(),
            'organisation_id': organisation, 'snapshot_date': profile['snapshot_date'],
            'mode': 'UNSENT_OFFLINE_PREPARATION', 'ready_to_execute': False,
            'target_completeness_asserted_by_caller': complete,
            'warning': 'No live validation, safe defaults, approval, idempotency or writes are provided by this helper.',
            'counts': counts, 'rows': result}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--resource', required=True, choices=RESOURCES)
    parser.add_argument('--template', action='store_true')
    parser.add_argument('--input', type=Path)
    parser.add_argument('--existing', type=Path)
    parser.add_argument('--defer-protected', action='store_true', help='Prepare ordinary fields while explicitly deferring protected source decisions; user approval still required.')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if any(args.output.resolve() == path.resolve() for path in (args.input, args.existing) if path):
        parser.error('Output must not overwrite a source or target snapshot')
    if args.template:
        if args.input or args.existing:
            parser.error('--template cannot be combined with source/target inputs')
        profile = load_profile(args.resource)
        columns = [n for n in profile['create']['properties'] if n not in profile['protected_fields']]
        buffer = io.StringIO(newline='')
        csv.writer(buffer).writerow(columns)
        args.output.write_text(buffer.getvalue(), encoding='utf-8-sig')
    else:
        if not args.input:
            parser.error('--input is required for preparation')
        existing = json.loads(args.existing.read_text(encoding='utf-8-sig')) if args.existing else None
        plan = prepare(args.resource, args.input.read_bytes(), existing, args.defer_protected)
        args.output.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(str(args.output.resolve()))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, UnicodeError) as exc:
        raise SystemExit('Import preparation failed: ' + str(exc)) from None
