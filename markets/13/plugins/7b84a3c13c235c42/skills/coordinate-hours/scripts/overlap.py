#!/usr/bin/env python3
"""Find continuous common work windows at minute resolution. No network/writes."""
import json
import re
import sys
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

UTC = timezone.utc
MINUTE = timedelta(minutes=1)


def local_boundary(day, value, zone):
    if not isinstance(value, str) or not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d', value):
        raise ValueError('work times must be HH:MM in 24-hour format')
    naive = datetime.combine(day, time.fromisoformat(value))
    candidates = set()
    for fold in (0, 1):
        aware = naive.replace(tzinfo=zone, fold=fold)
        instant = aware.astimezone(UTC)
        if instant.astimezone(zone).replace(tzinfo=None) == naive:
            candidates.add(instant)
    if len(candidates) != 1:
        raise ValueError('ambiguous or nonexistent local boundary: ' + str(naive) + ' ' + zone.key)
    return candidates.pop()


def participant(raw):
    if not isinstance(raw, dict) or set(raw) - {'name', 'zone', 'start', 'end', 'weekdays'}:
        raise ValueError('participant fields must be name, zone, start, end, weekdays')
    name = raw.get('name')
    if not isinstance(name, str) or not name.strip() or len(name) > 80:
        raise ValueError('participant name must contain 1 to 80 characters')
    if not isinstance(raw.get('zone'), str):
        raise ValueError('each participant needs an IANA zone')
    zone = ZoneInfo(raw['zone'])
    for key in ('start', 'end'):
        value = raw.get(key)
        if not isinstance(value, str) or not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d', value):
            raise ValueError('each participant needs start/end as HH:MM')
    if raw['start'] == raw['end']:
        raise ValueError('start and end must differ; equal endpoints do not mean 24 hours')
    weekdays = raw.get('weekdays', [0, 1, 2, 3, 4])
    if not isinstance(weekdays, list) or not weekdays or any(type(x) is not int or x not in range(7) for x in weekdays):
        raise ValueError('weekdays must be a nonempty list of integers 0 (Monday) through 6')
    return dict(raw, zone=zone, weekdays=set(weekdays))


def window(p, day):
    if day.weekday() not in p['weekdays']:
        return None
    following = day + timedelta(days=1) if p['end'] < p['start'] else day
    start = local_boundary(day, p['start'], p['zone'])
    end = local_boundary(following, p['end'], p['zone'])
    if end <= start:
        raise ValueError('work window has non-positive duration')
    return start, end


def render(instant, people):
    return {'utc': instant.isoformat(), 'local': {p['name']: instant.astimezone(p['zone']).isoformat() for p in people}}


def calculate(data):
    if not isinstance(data, dict) or set(data) - {'start_date', 'end_date', 'anchor', 'participants', 'minimum_minutes'}:
        raise ValueError('invalid overlap input fields')
    first, last = date.fromisoformat(data['start_date']), date.fromisoformat(data['end_date'])
    if not 0 <= (last - first).days <= 92:
        raise ValueError('date range must be ascending and at most 93 inclusive days')
    raw = data.get('participants')
    if not isinstance(raw, list) or not 2 <= len(raw) <= 10:
        raise ValueError('participants must contain 2 to 10 entries')
    people = [participant(p) for p in raw]
    if len(set(p['name'] for p in people)) != len(people):
        raise ValueError('participant names must be unique')
    anchor = next((p for p in people if p['name'] == data.get('anchor')), None)
    if anchor is None:
        raise ValueError('anchor must match a participant name')
    minimum = data.get('minimum_minutes', 60)
    if type(minimum) is not int or not 1 <= minimum <= 1440:
        raise ValueError('minimum_minutes must be an integer from 1 to 1440')
    days = []
    for offset in range((last - first).days + 1):
        day = first + timedelta(days=offset)
        primary = window(anchor, day)
        fragments = []
        if primary:
            candidates = {}
            for p in people:
                if p is anchor:
                    continue
                # Evaluate only local days which can intersect the anchor interval,
                # plus the preceding day for overnight shifts.
                low = primary[0].astimezone(p['zone']).date() - timedelta(days=1)
                high = primary[1].astimezone(p['zone']).date()
                intervals = []
                for i in range((high - low).days + 1):
                    candidate_day = low + timedelta(days=i)
                    # Skip dates whose broad local-day envelope cannot intersect;
                    # this avoids raising for unrelated DST boundaries.
                    envelope_start = datetime.combine(candidate_day, time.min, p['zone']).astimezone(UTC)
                    envelope_end = datetime.combine(candidate_day + timedelta(days=2), time.min, p['zone']).astimezone(UTC)
                    if envelope_start >= primary[1] or envelope_end <= primary[0]:
                        continue
                    candidate = window(p, candidate_day)
                    if candidate and candidate[0] < primary[1] and candidate[1] > primary[0]:
                        intervals.append(candidate)
                candidates[p['name']] = intervals
            cursor = primary[0]
            active = None
            while cursor < primary[1]:
                valid = all(any(a <= cursor and cursor + MINUTE <= b for a, b in candidates[p['name']]) for p in people if p is not anchor)
                if valid and active is None:
                    active = cursor
                if not valid and active is not None:
                    fragments.append((active, cursor)); active = None
                cursor += MINUTE
            if active is not None:
                fragments.append((active, primary[1]))
        spans = []
        for a, b in fragments:
            minutes = int((b - a).total_seconds() // 60)
            spans.append({'start': render(a, people), 'end': render(b, people), 'minutes': minutes, 'meets_minimum': minutes >= minimum})
        days.append({'anchor_start_date': day.isoformat(), 'anchor_is_workday': primary is not None, 'windows': spans,
                     'has_sufficient_overlap': any(w['meets_minimum'] for w in spans)})
    return {'anchor': anchor['name'], 'zones': {p['name']: p['zone'].key for p in people}, 'minimum_minutes': minimum,
            'resolution_minutes': 1, 'days': days,
            'notes': ['Dates and weekdays refer to each work window start in its local zone.',
                      'Overnight windows belong to their start date. Intervals are start-inclusive, end-exclusive.',
                      'Holidays and time off are excluded unless removed from the input date ranges.',
                      'Uses the host IANA time-zone database; future government rule changes may require updated data.']}


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError('usage: overlap.py INPUT.json')
        path = Path(sys.argv[1])
        if path.stat().st_size > 1000000:
            raise ValueError('input exceeds 1 MB')
        print(json.dumps(calculate(json.loads(path.read_text(encoding='utf-8'))), indent=2, allow_nan=False))
    except (ValueError, KeyError, TypeError, OSError, ZoneInfoNotFoundError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
