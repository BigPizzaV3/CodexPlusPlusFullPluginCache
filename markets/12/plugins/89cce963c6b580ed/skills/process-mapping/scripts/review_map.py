"""Offline process-map difference and impact review. Never connects or writes."""
import argparse
import copy
import json
from pathlib import Path

FIELDS = ('parent_id', 'level', 'name', 'description', 'owner_id', 'department',
          'revision_status', 'review_date', 'position', 'metadata')
LEVELS = {'department': None, 'macro_process': 'department', 'procedure': 'macro_process',
          'work_instruction': 'procedure'}
STRUCTURAL = {'parent_id', 'level', 'revision_status'}

def index_snapshot(snapshot, label):
    if not isinstance(snapshot, dict) or not isinstance(snapshot.get('data'), list):
        raise ValueError(label + ': expected snapshot envelope with data array')
    if not snapshot.get('organisation_id'):
        raise ValueError(label + ': organisation_id required')
    if not isinstance(snapshot.get('complete'), bool):
        raise ValueError(label + ': boolean complete required')
    result = {}
    for record in snapshot['data']:
        if not isinstance(record, dict) or not isinstance(record.get('id'), str) or not record['id']:
            raise ValueError(label + ': each record needs a stable string ID')
        if record['id'] in result:
            raise ValueError(label + ': duplicate record IDs')
        if record.get('org_id') not in (None, snapshot['organisation_id']):
            raise ValueError(label + ': cross-organisation record')
        result[record['id']] = record
    return result

def children_of(identifier, records):
    visited = {identifier}
    pending = [identifier]
    while pending:
        parent = pending.pop()
        for record in records.values():
            if record.get('parent_id') == parent and record['id'] not in visited:
                visited.add(record['id'])
                pending.append(record['id'])
    return sorted(visited - {identifier})

def review(baseline, proposed, current):
    base = index_snapshot(baseline, 'baseline')
    want = index_snapshot(proposed, 'proposal')
    live = index_snapshot(current, 'current')
    org = baseline['organisation_id']
    if proposed['organisation_id'] != org or current['organisation_id'] != org:
        raise ValueError('Snapshots belong to different organisations')
    scope = baseline.get('scope_ids')
    if not isinstance(scope, list) or any(i not in base for i in scope) or len(scope) != len(set(scope)):
        raise ValueError('Baseline needs unique explicit scope_ids present in data')
    issues = []
    if not all(s['complete'] for s in (baseline, proposed, current)):
        issues.append('Snapshot incomplete; do not infer absence or upload a replacement')
    operations = []
    retained_detail = {}
    effective = copy.deepcopy(live)
    for identifier, desired in want.items():
        extra = {k: copy.deepcopy(v) for k, v in desired.items()
                 if k not in FIELDS and k not in ('id', 'org_id', 'links', 'created_at', 'updated_at')}
        if extra:
            retained_detail[identifier] = extra
        if identifier not in base:
            if identifier in live:
                issues.append(identifier + ': appeared after baseline; identity review required')
                continue
            if not identifier.startswith('local:'):
                issues.append(identifier + ': new nodes require local: planning IDs')
                continue
            fields = {k: copy.deepcopy(v) for k, v in desired.items() if k in FIELDS}
            if not fields.get('name'):
                issues.append(identifier + ': new node needs name')
            if fields.get('parent_id') in base and fields['parent_id'] not in scope:
                issues.append(identifier + ': new node parent is outside approved scope')
            effective[identifier] = {'id': identifier, **fields}
            operations.append({'id': identifier, 'operation': 'create', 'fields': fields,
                               'review_required': ['resolve actual parent/record UUIDs after creation']})
            continue
        before = base[identifier]
        patch = {k: copy.deepcopy(desired[k]) for k in FIELDS if k in desired and desired[k] != before.get(k)}
        if not patch:
            continue
        if identifier not in scope:
            issues.append(identifier + ': change is outside approved scope')
            continue
        if identifier not in live:
            issues.append(identifier + ': target disappeared or is inaccessible')
            continue
        now = live[identifier]
        conflicting = [k for k, v in patch.items() if now.get(k) != before.get(k) and now.get(k) != v]
        structural = bool(set(patch) & STRUCTURAL)
        # External changes to a target's structural context must be reviewed even for a narrative patch.
        structural_context = [k for k in ('parent_id', 'level') if now.get(k) != before.get(k)]
        if structural_context and not all(k in patch and patch[k] == now.get(k) for k in structural_context):
            conflicting += ['structural context: ' + ', '.join(structural_context)]
        dependencies_changed = children_of(identifier, base) != children_of(identifier, live) or before.get('links', []) != now.get('links', [])
        if structural and dependencies_changed:
            conflicting.append('children or links changed since baseline')
        # If an external editor already made the approved exact change, it is not another write.
        actual_patch = {k: v for k, v in patch.items() if now.get(k) != v}
        if conflicting:
            issues.append(identifier + ': concurrent conflict: ' + ', '.join(conflicting))
        elif actual_patch:
            effective[identifier].update(actual_patch)
        operations.append({'id': identifier, 'operation': 'update' if actual_patch else 'already_applied',
                           'fields': actual_patch, 'conflicts': conflicting,
                           'before': {k: before.get(k) for k in actual_patch},
                           'descendants': children_of(identifier, live),
                           'links': copy.deepcopy(now.get('links', [])),
                           'review_required': ['related processes/native associations not discoverable from these snapshots',
                                               'meaning/identity continuity and linked history'] if structural else
                                              (['meaning/identity continuity with linked history']
                                               if now.get('links') and set(actual_patch) & {'name', 'description'} else [])})
    for identifier in sorted(set(base) - set(want)):
        if identifier in scope:
            operations.append({'id': identifier, 'operation': 'omitted_preserve',
                               'fields': {}, 'review_required': ['omission is not retirement authority']})
    for identifier, record in effective.items():
        parent = record.get('parent_id')
        level = record.get('level')
        if parent and parent not in effective:
            issues.append(identifier + ': missing/inaccessible parent')
        if level not in LEVELS:
            issues.append(identifier + ': legacy/unknown level needs explicit review')
        elif level == 'department' and parent:
            issues.append(identifier + ': department cannot have a process parent in this model')
        elif level != 'department' and (not parent or effective.get(parent, {}).get('level') != LEVELS[level]):
            issues.append(identifier + ': parent level inconsistent with proposed hierarchy')
        seen = {identifier}
        cursor = parent
        while cursor and cursor in effective:
            if cursor in seen:
                issues.append(identifier + ': hierarchy cycle')
                break
            seen.add(cursor)
            cursor = effective[cursor].get('parent_id')
    return {'format_version': 1, 'mode': 'UNSENT_OFFLINE_IMPACT_REVIEW', 'organisation_id': org,
            'ready_to_execute': False, 'native_versioning': False, 'issues': sorted(set(issues)),
            'operations': operations,
            'supporting_detail_retained_outside_native_fields': retained_detail,
            'effective_records_for_review': list(effective.values()),
            'limits': ['No network, permission checks, full impact discovery, concurrency lock or database writes.',
                       'Caller-provided complete flags and source records are not verified by this helper.',
                       'Local IDs are planning references, not submitted UUIDs.',
                       'Final content agreement, impact decisions and exact upload approval are still required.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for arg in ('baseline', 'proposal', 'current', 'output'):
        parser.add_argument('--' + arg, required=True, type=Path)
    args = parser.parse_args()
    if any(args.output.resolve() == path.resolve() for path in (args.baseline, args.proposal, args.current)):
        parser.error('Output must not overwrite an input snapshot')
    read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
    result = review(read(args.baseline), read(args.proposal), read(args.current))
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(str(args.output.resolve()))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit('Map review failed: ' + str(exc)) from None
