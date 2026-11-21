"""Application-neutral qualification plans and portable payload receipts.

Receipts record observed tests, not cryptographic proof of good behavior. Archive
hashes cannot be embedded into their own ZIP; payload and transport identity are
therefore deliberately separate.
"""
from __future__ import annotations
import json
import re
from .safety import IterationError, sha, code_path
from .layout import INDEX

PLAN = 'PROGRAM/Automation/QA27.json'
RECEIPT = 'PROGRAM/Automation/RC18.json'
LIFECYCLE = 'PROGRAM/Automation/RT42.py'
PLAN_SCHEMA = 'iteration.check-plan/1'
RECEIPT_SCHEMA = 'iteration.payload-qualification/1'
CATEGORIES = {'startup', 'primary', 'invalid-input', 'boundary', 'startup-refusal',
              'persistence', 'upgrade', 'collision-recovery', 'file-safety',
              'integrations', 'native-dependencies'}
FEATURES = {'persistent-data', 'writes-files', 'backup-restore', 'network', 'native'}
KINDS = {'gui', 'cli', 'local-web', 'game', 'library'}
PATTERN = re.compile(r'[a-z][a-z0-9_.-]{0,63}')


def validate_plan(value: dict) -> dict:
    if not isinstance(value, dict) or value.get('schema') != PLAN_SCHEMA or not isinstance(value.get('kind'), str) or value.get('kind') not in KINDS:
        raise IterationError('Declare an application-appropriate QA27 test plan before delivery.', 'plan_required')
    features = value.get('features', [])
    cases = value.get('cases')
    if (not isinstance(features, list) or len(features) > len(FEATURES) or
            any(type(f) is not str or f not in FEATURES for f in features) or len(set(features)) != len(features)):
        raise IterationError('Unsupported or duplicate feature in check plan.', 'invalid_plan')
    if not isinstance(cases, list) or not 2 <= len(cases) <= 128:
        raise IterationError('Provide 2 to 128 concrete test cases.', 'invalid_plan')
    clean_cases, ids, categories = [], set(), set()
    for c in cases:
        if not isinstance(c, dict) or not isinstance(c.get('id'), str) or not PATTERN.fullmatch(c['id']):
            raise IterationError('Invalid stable test case ID.', 'invalid_plan')
        if c['id'] in ids or c.get('phase') not in ('startup', 'regression') or not isinstance(c.get('category'), str) or c.get('category') not in CATEGORIES:
            raise IterationError('Duplicate or invalid test case.', 'invalid_plan')
        if (c['phase'] == 'startup') != (c['category'] == 'startup'):
            raise IterationError('Startup cases belong to startup phase; other cases to regression.', 'invalid_plan')
        description = c.get('description')
        if not isinstance(description, str) or not 12 <= len(description.strip()) <= 1000:
            raise IterationError('Each test needs a concrete assertion description.', 'invalid_plan')
        ids.add(c['id']); categories.add(c['category'])
        clean_cases.append({k: c[k] for k in ('id','phase','category','description')})
    if type(value.get('continuation', False)) is not bool:
        raise IterationError('continuation must be boolean.', 'invalid_plan')
    continuation = value.get('continuation', False)
    mandatory = {'startup','primary'}
    if 'persistent-data' in features:
        mandatory |= {'persistence','startup-refusal'}
        if continuation:
            mandatory.add('upgrade')
    if 'writes-files' in features: mandatory.add('file-safety')
    if 'backup-restore' in features: mandatory.add('collision-recovery')
    if 'network' in features: mandatory.add('integrations')
    if 'native' in features: mandatory.add('native-dependencies')
    reasons = value.get('not_applicable', {})
    if not isinstance(reasons, dict) or set(reasons) - {'invalid-input','boundary'}:
        raise IterationError('Only inapplicable input/boundary categories may be waived with a reason.', 'invalid_plan')
    for category in ('invalid-input','boundary'):
        if category in categories:
            if category in reasons: raise IterationError('A category cannot be both tested and waived.', 'invalid_plan')
        else:
            reason = reasons.get(category)
            if not isinstance(reason, str) or not 25 <= len(reason.strip()) <= 1000:
                raise IterationError('Test '+category+' or explain specifically why it does not apply.', 'missing_test_category')
    if mandatory - categories:
        raise IterationError('Missing required case categories: '+', '.join(sorted(mandatory-categories)), 'missing_test_category')
    previous = value.get('previous_archive_sha256')
    fixtures = value.get('prior_fixtures', [])
    if 'upgrade' in mandatory:
        if not isinstance(previous, str) or not re.fullmatch(r'[0-9a-f]{64}', previous):
            raise IterationError('Persistent continuation needs the actual previous archive hash.', 'prior_version_required')
        if not isinstance(fixtures, list) or not 1 <= len(fixtures) <= 20:
            raise IterationError('Supply hashed fixtures produced by the actual previous program.', 'prior_version_required')
    else:
        if previous is not None or fixtures:
            raise IterationError('Prior-version evidence only applies to a persistent continuation.', 'invalid_plan')
    normalized_fixtures = []
    for f in fixtures:
        if not isinstance(f, dict) or not isinstance(f.get('path'), str):
            raise IterationError('Invalid prior fixture.', 'invalid_plan')
        normalized_path = code_path(f['path'])
        if not re.fullmatch(r'[0-9a-f]{64}', str(f.get('sha256',''))):
            raise IterationError('Invalid prior fixture hash.', 'invalid_plan')
        normalized_fixtures.append({'path':normalized_path,'sha256':f['sha256']})
    result = {'schema': PLAN_SCHEMA, 'kind': value['kind'], 'features': sorted(features),
              'continuation': continuation, 'cases': clean_cases, 'not_applicable': reasons}
    if previous is not None:
        result.update(previous_archive_sha256=previous, prior_fixtures=normalized_fixtures)
    return result


def verify_plan_files(plan: dict, files: dict[str, bytes]) -> None:
    for fixture in plan.get('prior_fixtures', []):
        if fixture['path'] not in files or sha(files[fixture['path']]) != fixture['sha256']:
            raise IterationError('Prior-version fixture missing or changed.', 'prior_fixture_mismatch')


def payload_digest(files: dict[str, bytes]) -> str:
    """Bind every entry and semantic manifest field except receipt/self-hashes."""
    manifest = json.loads(files[INDEX])
    for key in ('file_sha256', 'release_qualification'):
        manifest.pop(key, None)
    manifest.get('record_index', {}).pop('qualification', None)
    hashes = {p: sha(v) for p, v in files.items() if p not in (INDEX, RECEIPT)}
    hashes[INDEX] = sha(json.dumps(manifest, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode())
    return sha(json.dumps(hashes, sort_keys=True, separators=(',', ':')).encode())


def validate_receipt(files: dict[str, bytes]) -> dict:
    if RECEIPT not in files:
        raise IterationError('Portable qualification receipt is missing.', 'receipt_required')
    try:
        receipt = json.loads(files[RECEIPT])
    except (ValueError, UnicodeError) as exc:
        raise IterationError('Invalid qualification receipt.', 'invalid_receipt') from exc
    if (not isinstance(receipt, dict) or receipt.get('schema') != RECEIPT_SCHEMA or
        receipt.get('status') != 'payload_qualified' or receipt.get('payload_sha256') != payload_digest(files)):
        raise IterationError('Receipt does not qualify this payload.', 'receipt_mismatch')
    evidence = receipt.get('preflight', {})
    if not isinstance(evidence, dict) or evidence.get('status') != 'passed':
        raise IterationError('Receipt has no passed observed preflight.', 'invalid_receipt')
    if evidence.get('payload_sha256') != receipt['payload_sha256']:
        raise IterationError('Receipt evidence is stale.', 'receipt_mismatch')
    return receipt
