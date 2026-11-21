#!/usr/bin/env python3
"""Scoped rectangle plan review; no CAD writes, network, building-code certification."""
import argparse
import copy
import hashlib
import html
import json
import math
from pathlib import Path

VERSION = '0.3.1'
EPS = 1e-8  # numerical comparison tolerance, metres; not a construction tolerance
GROUPS = ('floors', 'rooms', 'doors', 'furniture')
ENTITY_KEYS = {
    'floors': {'id', 'rect', 'source', 'label', 'notes', 'provenance', 'rotation_deg'},
    'rooms': {'id', 'rect', 'floor', 'parent_id', 'source', 'label', 'notes', 'provenance', 'rotation_deg'},
    'doors': {'id', 'floor', 'start', 'end', 'connects', 'measurement', 'use_zone', 'source', 'label', 'notes', 'provenance', 'rotation_deg'},
    'furniture': {'id', 'floor', 'room_id', 'rect', 'clearance_rect', 'source', 'label', 'notes', 'provenance', 'rotation_deg'},
}
LOCK_FIELDS = {'rect', 'floor', 'start', 'end', 'connects', 'room_id', 'parent_id', 'clearance_rect', 'use_zone'}


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def box(value):
    return isinstance(value, list) and len(value) == 4 and all(number(x) for x in value) and value[2] > 0 and value[3] > 0


def contains(a, b):
    return a[0] <= b[0] + EPS and a[1] <= b[1] + EPS and a[0] + a[2] + EPS >= b[0] + b[2] and a[1] + a[3] + EPS >= b[1] + b[3]


def intersection(a, b):
    x, y = max(a[0], b[0]), max(a[1], b[1])
    w, h = min(a[0] + a[2], b[0] + b[2]) - x, min(a[1] + a[3], b[1] + b[3]) - y
    return [x, y, w, h] if w > EPS and h > EPS else None


def union_area(rects):
    """Exact sweep for finite axis-aligned rectangles, no raster approximation."""
    xs = sorted({x for r in rects for x in (r[0], r[0] + r[2])})
    total = 0.0
    for left, right in zip(xs, xs[1:]):
        spans = sorted((r[1], r[1] + r[3]) for r in rects if r[0] < right and r[0] + r[2] > left)
        height, end = 0.0, -math.inf
        for low, high in spans:
            height += max(0.0, high - max(low, end))
            end = max(end, high)
        total += (right - left) * height
    return total


def on_boundary(rect, start, end):
    x, y, w, h = rect
    if abs(start[0] - end[0]) <= EPS:
        return (abs(start[0] - x) <= EPS or abs(start[0] - x - w) <= EPS) and min(start[1], end[1]) >= y - EPS and max(start[1], end[1]) <= y + h + EPS
    if abs(start[1] - end[1]) <= EPS:
        return (abs(start[1] - y) <= EPS or abs(start[1] - y - h) <= EPS) and min(start[0], end[0]) >= x - EPS and max(start[0], end[0]) <= x + w + EPS
    return False


def prepare(spec):
    if not isinstance(spec, dict) or type(spec.get('schema_version')) is not int or spec['schema_version'] != 1:
        raise ValueError('SCHEMA_VERSION_REQUIRED')
    if not isinstance(spec.get('revision'), str) or not spec['revision'].strip() or len(spec['revision']) > 128:
        raise ValueError('REVISION_REQUIRED')
    if spec.get('units') not in ('m', 'mm'):
        raise ValueError('UNITS_M_OR_MM_REQUIRED')
    data = copy.deepcopy(spec)
    scale = 0.001 if spec['units'] == 'mm' else 1.0
    entities, skipped, provisional = {}, [], []
    for group in GROUPS:
        items = data.setdefault(group, [])
        if not isinstance(items, list) or len(items) > 2000:
            raise ValueError('INVALID_OR_TOO_MANY_ENTITIES')
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id'].strip() or len(item['id']) > 128 or item['id'] == 'outside' or item['id'] in entities:
                raise ValueError('UNIQUE_ENTITY_ID_REQUIRED')
            entities[item['id']] = item
            if item.get('source') not in ('measured', 'client'):
                provisional.append(item['id'])
            rotation = item.get('rotation_deg', 0)
            if not number(rotation) or abs(rotation) > EPS or set(item) - ENTITY_KEYS[group]:
                skipped.append(item['id'])
            if group != 'doors':
                if not box(item.get('rect')):
                    raise ValueError('FINITE_POSITIVE_RECT_REQUIRED')
                item['rect'] = [v * scale for v in item['rect']]
                if any(not number(v) or abs(v) > 1e6 for v in item['rect']):
                    raise ValueError('GEOMETRY_RANGE_EXCEEDED')
            else:
                for key in ('start', 'end'):
                    p = item.get(key)
                    if not isinstance(p, list) or len(p) != 2 or not all(number(v) for v in p):
                        raise ValueError('FINITE_DOOR_SEGMENT_REQUIRED')
                    item[key] = [v * scale for v in p]
                    if any(abs(v) > 1e6 for v in item[key]):
                        raise ValueError('GEOMETRY_RANGE_EXCEEDED')
                if math.dist(item['start'], item['end']) <= EPS:
                    raise ValueError('POSITIVE_DOOR_SEGMENT_REQUIRED')
                links = item.get('connects')
                if not isinstance(links, list) or len(links) != 2 or not all(isinstance(v, str) for v in links) or links[0] == links[1]:
                    raise ValueError('TWO_DISTINCT_DOOR_ROOMS_REQUIRED')
            for key in ('clearance_rect', 'use_zone'):
                if key in item:
                    if not box(item[key]):
                        raise ValueError('FINITE_USE_ZONE_REQUIRED')
                    item[key] = [v * scale for v in item[key]]
                    if any(abs(v) > 1e6 for v in item[key]):
                        raise ValueError('GEOMETRY_RANGE_EXCEEDED')
    if not data['floors'] or not data['rooms']:
        raise ValueError('FLOOR_AND_ROOMS_REQUIRED')
    floors = {i['id']: i for i in data['floors']}
    rooms = {i['id']: i for i in data['rooms']}
    for item in data['rooms'] + data['doors'] + data['furniture']:
        if item.get('floor') not in floors:
            raise ValueError('UNKNOWN_FLOOR')
    for room in rooms.values():
        seen, node = {room['id']}, room
        while node.get('parent_id') is not None:
            parent = rooms.get(node['parent_id'])
            if not parent or parent['id'] in seen or parent['floor'] != room['floor']:
                raise ValueError('INVALID_PARENT_TREE')
            seen.add(parent['id']); node = parent
    for item in data['furniture']:
        room = rooms.get(item.get('room_id'))
        if not room or room['floor'] != item['floor']:
            raise ValueError('UNKNOWN_FURNITURE_ROOM')
    for item in data['doors']:
        if any(r != 'outside' and (r not in rooms or rooms[r]['floor'] != item['floor']) for r in item['connects']):
            raise ValueError('UNKNOWN_DOOR_ROOM')
    data['units'] = 'm'
    return data, entities, skipped, provisional


def audit(spec, baseline=None):
    report = {'engine_version': VERSION, 'scope': 'axis_aligned_rectangle_spec_only', 'decision': 'INVALID_INPUT', 'issues': [], 'checks': {}, 'metrics': {},
              'native_execution': 'NOT_RUN', 'evidence_level': 'DECLARED_SPEC_GEOMETRY',
              'limitations': ['No native CAD/model or image measurement', 'No continuous door sweep or usable path-width proof', 'No structural/fire/code certification', 'Clear rectangles represent supplied usable spaces; wall/shaft deductions require explicit geometry']}
    try:
        data, entities, skipped, provisional = prepare(spec)
        fingerprint = hashlib.sha256(json.dumps(spec, sort_keys=True, ensure_ascii=False, allow_nan=False, separators=(',', ':')).encode()).hexdigest()
    except (ValueError, TypeError, KeyError, OverflowError):
        report['issues'].append({'code': 'INVALID_SPEC', 'objects': [], 'detail': 'Schema, identifiers, finite geometry, units or references are invalid.'})
        return report
    report.update(revision=data['revision'], spec_sha256=fingerprint, metrics_scope='SUPPORTED_OBJECTS_ONLY')
    checks = report['checks']
    checks.update(codes='UNKNOWN', structure='UNKNOWN', usable_egress='UNKNOWN', continuous_door_sweep='UNKNOWN', native_model='NOT_RUN')
    supported_sections = set(GROUPS) | {'schema_version', 'revision', 'units', 'requirements', 'locks', 'title', 'description', 'provenance', 'project_id'}
    unknown_sections = sorted(k for k, value in data.items() if k not in supported_sections and value)
    report['coverage'] = {'input_counts': {g: len(data[g]) for g in GROUPS}, 'unverified_dimensions': provisional,
                          'unsupported_ids': skipped, 'unsupported_sections': unknown_sections,
                          'algorithm': 'rectangle plane sweep; rectangle intersection; door boundary graph; locked-field diff', 'numerical_epsilon_m': EPS}
    checks['geometry_coverage'] = 'UNKNOWN' if skipped or unknown_sections else 'PASS'
    skipped_set = set(skipped)
    # Children of unsupported containers cannot be measured against invented boundaries.
    changed = True
    while changed:
        before = len(skipped_set)
        for item in entities.values():
            if item.get('floor') in skipped_set or item.get('parent_id') in skipped_set or item.get('room_id') in skipped_set:
                skipped_set.add(item['id'])
        changed = len(skipped_set) != before
    active = lambda g: [i for i in data[g] if i['id'] not in skipped_set]
    floors = {i['id']: i for i in active('floors')}
    rooms = {i['id']: i for i in active('rooms')}
    furniture = active('furniture')
    children = {r: [x for x in rooms.values() if x.get('parent_id') == r] for r in rooms}

    def issue(code, objects, **details):
        report['issues'].append({'id': 'I%03d' % (len(report['issues']) + 1), 'code': code, 'objects': objects, **details})

    def ancestor(a, b):
        node = rooms[b]
        while node.get('parent_id') in rooms:
            if node['parent_id'] == a:
                return True
            node = rooms[node['parent_id']]
        return False

    for room in rooms.values():
        if not contains(floors[room['floor']]['rect'], room['rect']):
            issue('OUTSIDE_FLOOR', [room['id'], room['floor']])
        parent = rooms.get(room.get('parent_id'))
        if parent and not contains(parent['rect'], room['rect']):
            issue('CHILD_OUTSIDE_PARENT', [room['id'], parent['id']])
    values = list(rooms.values())
    for idx, room in enumerate(values):
        for other in values[idx + 1:]:
            if room['floor'] == other['floor'] and not ancestor(room['id'], other['id']) and not ancestor(other['id'], room['id']):
                overlap = intersection(room['rect'], other['rect'])
                if overlap:
                    issue('ROOM_OVERLAP', [room['id'], other['id']], overlap_m2=overlap[2] * overlap[3])
    net = {}
    for room in rooms.values():
        cuts = [intersection(room['rect'], c['rect']) for c in children[room['id']]]
        net[room['id']] = max(0.0, room['rect'][2] * room['rect'][3] - union_area([r for r in cuts if r]))
    union_by_floor = {f: union_area([r['rect'] for r in rooms.values() if r['floor'] == f]) for f in floors}
    report['metrics'].update(room_union_m2=sum(union_by_floor.values()) if rooms else None, room_union_by_floor_m2=union_by_floor, room_net_m2=net)

    for item in furniture:
        room = rooms[item['room_id']]
        if not contains(room['rect'], item['rect']):
            issue('FURNITURE_OUTSIDE_ROOM', [item['id'], room['id']])
        for child in children[room['id']]:
            if intersection(item['rect'], child['rect']):
                issue('FURNITURE_IN_CHILD_ROOM', [item['id'], child['id']])
            if 'clearance_rect' in item and intersection(item['clearance_rect'], child['rect']):
                issue('USE_ZONE_IN_CHILD_ROOM', [item['id'], child['id']])
        if 'clearance_rect' in item and not contains(room['rect'], item['clearance_rect']):
            issue('USE_ZONE_OUTSIDE_ROOM', [item['id'], room['id']])
    for idx, item in enumerate(furniture):
        for other in furniture[idx + 1:]:
            if item['floor'] == other['floor'] and intersection(item['rect'], other['rect']):
                issue('FURNITURE_COLLISION', [item['id'], other['id']])
        zone = item.get('clearance_rect')
        if zone:
            for other in furniture:
                if other['id'] != item['id'] and item['floor'] == other['floor'] and intersection(zone, other['rect']):
                    issue('USE_ZONE_BLOCKED', [item['id'], other['id']])

    graph = {'outside': set(), **{r: set() for r in rooms}}
    widths = {}
    doors_checked = 0
    for door in active('doors'):
        if any(r != 'outside' and r not in rooms for r in door['connects']):
            skipped_set.add(door['id']); continue
        start, end = door['start'], door['end']
        ok = True
        for ref in door['connects']:
            boundaries = [floors[door['floor']]['rect']] if ref == 'outside' else [rooms[ref]['rect']] + [c['rect'] for c in children[ref]]
            ok = ok and any(on_boundary(rect, start, end) for rect in boundaries)
        doors_checked += 1
        if not ok:
            issue('DOOR_NOT_ON_BOUNDARY', [door['id']] + door['connects'])
        else:
            a, b = door['connects']; graph[a].add(b); graph[b].add(a)
        if door.get('measurement') == 'clear':
            widths[door['id']] = math.dist(start, end)
        zone = door.get('use_zone')
        if zone:
            for item in furniture:
                if door['floor'] == item['floor'] and intersection(zone, item['rect']):
                    issue('DOOR_USE_ZONE_BLOCKED', [door['id'], item['id']])
    reachable, pending = {'outside'}, ['outside']
    while pending:
        current = pending.pop()
        for room in graph[current] - reachable:
            reachable.add(room); pending.append(room)
    for room in sorted(set(rooms) - reachable):
        issue('ROOM_NOT_CONNECTED_TO_OUTSIDE', [room])
    checks['door_graph_connectivity'] = 'UNKNOWN' if skipped_set else 'FAIL' if set(rooms) - reachable else 'PASS'
    checks['door_clear_width_measurements'] = 'PASS' if len(widths) == doors_checked else 'UNKNOWN'
    report['metrics']['declared_clear_door_width_m'] = widths
    report['coverage']['checked_counts'] = {'floors': len(floors), 'rooms': len(rooms), 'furniture': len(furniture), 'doors': doors_checked}
    report['coverage']['unsupported_ids'] = sorted(skipped_set)

    requirements = data.get('requirements', {})
    baseline_requirements_changed = False
    if baseline is not None and isinstance(baseline, dict) and 'requirements' in baseline:
        # A candidate cannot relax the accepted brief by omitting/changing fields.
        baseline_requirements_changed = baseline['requirements'] != spec.get('requirements')
        requirements = baseline['requirements']
        if baseline_requirements_changed:
            issue('BASELINE_REQUIREMENTS_CHANGED', [], detail='Re-check against the accepted baseline; a new approved baseline is needed to change requirements.')
    if requirements:
        try:
            if not isinstance(requirements, dict) or set(requirements) - {'source', 'min_room_areas_m2', 'min_clear_door_width_m'}:
                raise ValueError()
            if not isinstance(requirements.get('source'), str) or not requirements['source'].strip():
                raise ValueError()
            if not any(requirements.get(key) for key in ('min_room_areas_m2', 'min_clear_door_width_m')):
                raise ValueError()
            for room, minimum in requirements.get('min_room_areas_m2', {}).items():
                if not number(minimum) or minimum <= 0:
                    raise ValueError()
                if room not in net:
                    checks['project_requirements'] = 'UNKNOWN'; continue
                if net[room] + EPS < minimum:
                    issue('PROJECT_ROOM_AREA', [room], measured_m2=net[room], required_m2=minimum, threshold_source=requirements['source'])
            for door, minimum in requirements.get('min_clear_door_width_m', {}).items():
                if not number(minimum) or minimum <= 0:
                    raise ValueError()
                if door not in widths:
                    checks['project_requirements'] = 'UNKNOWN'; continue
                if widths[door] + EPS < minimum:
                    issue('PROJECT_DOOR_WIDTH', [door], measured_m=widths[door], required_m=minimum, threshold_source=requirements['source'])
            checks.setdefault('project_requirements', 'CHECKED_AGAINST_DECLARED_PROJECT_THRESHOLDS')
        except (AttributeError, TypeError, ValueError):
            checks['project_requirements'] = 'UNKNOWN'

    if baseline is not None:
        try:
            base, old, _, _ = prepare(baseline)
            removed, added = sorted(old.keys() - entities.keys()), sorted(entities.keys() - old.keys())
            modified = sorted(k for k in old.keys() & entities.keys() if old[k] != entities[k])
            report['diff'] = {'baseline_revision': base['revision'], 'added': added, 'removed': removed, 'changed': modified, 'requirements_changed': baseline_requirements_changed}
            checks['locked_elements'] = 'PASS'
            locks = base.get('locks', [])
            if not isinstance(locks, list):
                raise ValueError()
            for lock in locks:
                ref, fields = lock.get('id'), lock.get('fields')
                if ref not in old or not isinstance(fields, list) or not fields or any(f not in LOCK_FIELDS or f not in old[ref] for f in fields):
                    raise ValueError()
                if ref not in entities or any(old[ref][f] != entities[ref].get(f) for f in fields):
                    issue('LOCK_CHANGED', [ref], fields=fields)
                    checks['locked_elements'] = 'FAIL'
        except (ValueError, TypeError, AttributeError, KeyError):
            checks['locked_elements'] = 'UNKNOWN'
    else:
        checks['locked_elements'] = 'UNKNOWN' if data.get('locks') else 'NOT_APPLICABLE'
    incomplete = skipped_set or unknown_sections or provisional or any(checks.get(k) == 'UNKNOWN' for k in ('locked_elements', 'project_requirements'))
    report['decision'] = 'ISSUES_FOUND' if report['issues'] else 'PROVISIONAL_REVIEW' if incomplete else 'SCOPED_REVIEW_NOT_CERTIFIED'
    return report


def svg(spec, report):
    data, _, skipped, _ = prepare(spec)
    skip = set(report.get('coverage', {}).get('unsupported_ids', skipped))
    floors = [f for f in data['floors'] if f['id'] not in skip]
    scale, margin, offset = 65, 30, 70
    width = max([600] + [int(f['rect'][2] * scale + margin * 2) for f in floors])
    height = int(110 + sum(f['rect'][3] * scale + 70 for f in floors))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="CWS scoped rectangle plan review">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<g font-family="sans-serif" font-size="12" fill="#16324f">',
             '<text x="30" y="25">CWS — KIỂM MẶT BẰNG 2D; KHÔNG PHẢI MÔ HÌNH CAD</text>',
             f'<text x="30" y="46">{html.escape(str(report.get("revision", "")))} · {html.escape(report["decision"])} · {len(report["issues"])} issues</text>']
    bad = {obj for issue in report['issues'] for obj in issue['objects']}
    for floor in floors:
        x0, y0, fw, fh = floor['rect']
        def xy(x, y):
            return margin + (x - x0) * scale, offset + (fh - (y - y0)) * scale
        parts.append(f'<text x="30" y="{offset - 12}">Tầng: {html.escape(floor["id"])} · m</text>')
        for group in ('rooms', 'furniture'):
            for item in data[group]:
                if item['floor'] != floor['id'] or item['id'] in skip:
                    continue
                x, y, w, h = item['rect']; sx, sy = xy(x, y + h)
                fill = '#fee2e2' if item['id'] in bad else '#dbeafe' if group == 'rooms' else '#b6c4d6'
                dash = ' stroke-dasharray="4 3"' if item.get('source') not in ('measured', 'client') else ''
                parts.append(f'<rect x="{sx:.3f}" y="{sy:.3f}" width="{w*scale:.3f}" height="{h*scale:.3f}" fill="{fill}" stroke="#334155"{dash}/>')
                label = item.get('label', item['id'])
                parts.append(f'<text x="{sx+5:.3f}" y="{sy+17:.3f}">{html.escape(str(label))}</text>')
        for door in data['doors']:
            if door['floor'] == floor['id'] and door['id'] not in skip:
                sx, sy = xy(*door['start']); ex, ey = xy(*door['end'])
                parts.append(f'<line x1="{sx:.3f}" y1="{sy:.3f}" x2="{ex:.3f}" y2="{ey:.3f}" stroke="#dc2626" stroke-width="5"/>')
        offset += fh * scale + 70
    parts.append('</g></svg>')
    return '\n'.join(parts)


def load_json(path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError('DUPLICATE_JSON_KEY')
            out[key] = value
        return out
    with open(path, encoding='utf-8') as source:
        return json.load(source, object_pairs_hook=unique, parse_constant=lambda _: (_ for _ in ()).throw(ValueError('NONFINITE_JSON')))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('spec')
    parser.add_argument('--baseline')
    parser.add_argument('--report')
    parser.add_argument('--svg')
    args = parser.parse_args()
    try:
        paths = [Path(p) for p in (args.report, args.svg) if p]
        if len({p.resolve() for p in paths}) != len(paths) or any(p.exists() or p.is_symlink() for p in paths):
            raise ValueError('OUTPUT_ALREADY_EXISTS_OR_DUPLICATED')
        spec = load_json(args.spec)
        report = audit(spec, load_json(args.baseline) if args.baseline else None)
        text = json.dumps(report, ensure_ascii=False, allow_nan=False, indent=2)
        picture = svg(spec, report) if args.svg and report['decision'] != 'INVALID_INPUT' else None
        if args.report:
            with open(args.report, 'x', encoding='utf-8') as out:
                out.write(text + '\n')
        if args.svg and picture is not None:
            with open(args.svg, 'x', encoding='utf-8') as out:
                out.write(picture + '\n')
        print(text)
        return 0 if report['decision'] == 'SCOPED_REVIEW_NOT_CERTIFIED' else 2
    except (OSError, ValueError, TypeError, OverflowError):
        print(json.dumps({'decision': 'BLOCKED', 'code': 'INVALID_JSON_INPUT_OR_OUTPUT_PATH'}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
