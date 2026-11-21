"""Independent checks on the actual CSV ZIP delivered to a user."""
from __future__ import annotations

import calendar
import csv
import io
import json
import re
import uuid
import zipfile
from collections import defaultdict
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP, localcontext
from pathlib import Path
from zoneinfo import ZoneInfo

from converter import MAX_FILE, PURPOSES, SCALES, amount_minor, date_evidence, digest, month_of

EXPENSE_COLUMNS = ['source_key', 'source_dataset', 'kind', 'original_minor', 'original_currency',
                   'original_scale', 'date_precision', 'date', 'purpose', 'note', 'original_category',
                   'source_location', 'home_minor', 'home_currency', 'rate', 'rate_date', 'rate_source', 'rate_policy']
TABLES = {
    'expenses.csv': EXPENSE_COLUMNS,
    'coverage.csv': ['source_dataset', 'start_month', 'end_month', 'currency', 'status'],
    'decisions.csv': ['source_key', 'disposition', 'rule', 'reason'],
    'totals.csv': ['currency', 'scale', 'minor_units'],
}
INSTANT_PATTERN = r'\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.[0-9]{1,9})?(?:Z|[+-](?:0\d|1[0-4]):[0-5]\d)'


def checked_integer(text):
    if not isinstance(text, str) or not re.fullmatch(r'-?\d+', text):
        raise ValueError('Invalid integer amount')
    value = int(text)
    if not -(2 ** 63) <= value < 2 ** 63:
        raise ValueError('Amount exceeds supported range')
    return value


def restore_text(value):
    if value.startswith("'"):
        rest = value[1:]
        if rest.startswith("'") or rest.lstrip().startswith(('=', '+', '-', '@')):
            return rest
    return value


def unique_json(pairs):
    output = {}
    for key, value in pairs:
        if key in output:
            raise ValueError('Duplicate JSON field')
        output[key] = value
    return output


def read_archive(path):
    path = Path(path)
    if path.stat().st_size > MAX_FILE:
        raise ValueError('Archive exceeds limit')
    with zipfile.ZipFile(path) as archive:
        info = archive.infolist()
        if len(info) > 10_000 or sum(i.file_size for i in info) > MAX_FILE:
            raise ValueError('Expanded archive exceeds limit')
        members = {}
        for entry in info:
            if entry.filename in members:
                raise ValueError('Duplicate archive member')
            if entry.flag_bits & 1 or entry.compress_type not in {0, 8}:
                raise ValueError('Unsupported ZIP encoding')
            if entry.file_size > 25 * 1024 * 1024:
                raise ValueError('Archive member exceeds limit')
            members[entry.filename] = entry
        manifest = json.loads(archive.read('manifest.json'), object_pairs_hook=unique_json)
        if manifest.get('schema') != 'PaceCSVArchive' or manifest.get('version') != 8 or manifest.get('contents') != 'expenses':
            raise ValueError('Expected a Pace expense ZIP')
        if set(manifest.get('files', [])) != set(TABLES) or set(manifest.get('checksums', {})) != set(TABLES):
            raise ValueError('Required expense tables do not match')
        tables = {}
        for name, columns in TABLES.items():
            data = archive.read(name)
            if digest(data) != manifest['checksums'][name]:
                raise ValueError('Expense table checksum changed')
            reader = csv.DictReader(io.StringIO(data.decode('utf-8-sig')), strict=True)
            if reader.fieldnames != columns:
                raise ValueError('Expense table columns do not match')
            rows = list(reader)
            if len(rows) > 100_000 or any(None in r or any(v is None for v in r.values()) for r in rows):
                raise ValueError('Malformed expense table')
            tables[name] = rows
    return manifest, tables


def validate_archive(path):
    manifest, tables = read_archive(path)
    uuid.UUID(manifest['packageID'])
    zone = ZoneInfo(manifest['timeZone'])
    target = manifest['targetCurrency']
    if SCALES.get(target) != 2 or manifest.get('calendar') != 'gregorian':
        raise ValueError('Unsupported target currency or calendar')
    if manifest.get('throughDate'):
        date.fromisoformat(manifest['throughDate'])
    sources = manifest['sources']
    source_ids = {s['id'] for s in sources}
    if not 1 <= len(sources) <= 100 or len(source_ids) != len(sources):
        raise ValueError('Invalid source scopes')
    for source in sources:
        for key, maximum in [('id', 512), ('name', 4096), ('format', 128)]:
            if not source.get(key) or len(source[key].encode()) > maximum:
                raise ValueError('Invalid source metadata')
    for key in ['converterVersion', 'ruleVersion']:
        if not manifest.get(key) or len(manifest[key].encode()) > 128:
            raise ValueError('Invalid converter version')
    decisions = {}
    for row in tables['decisions.csv']:
        key = restore_text(row['source_key'])
        if not key or len(key.encode()) > 512 or key in decisions or row['disposition'] not in {'included', 'held', 'excluded'}:
            raise ValueError('Invalid expense decision')
        if not row['rule'] or len(row['rule'].encode()) > 512 or not row['reason'] or len(row['reason'].encode()) > 4096:
            raise ValueError('Invalid decision reason')
        decisions[key] = row
    rows = tables['expenses.csv']
    if not isinstance(manifest['recordCount'], int) or isinstance(manifest['recordCount'], bool) or len(rows) != manifest['recordCount'] or len(rows) > 50_000:
        raise ValueError('Expense count does not match')
    original_totals = defaultdict(int)
    keys, held, months, ready = set(), set(), set(), 0
    monthly_sources = defaultdict(set)
    source_sums = defaultdict(int)
    missing = defaultdict(set)
    dated_total, monthly_total, estimates = 0, 0, 0
    for row in rows:
        key = restore_text(row['source_key'])
        scope = restore_text(row['source_dataset'])
        if key in keys or key not in decisions or scope not in source_ids or not key or len(key.encode()) > 512:
            raise ValueError('Invalid or competing expense identity')
        keys.add(key)
        currency, scale = row['original_currency'], int(row['original_scale'])
        if SCALES.get(currency) != scale:
            raise ValueError('Currency scale does not match')
        value = checked_integer(row['original_minor'])
        if row['kind'] not in {'expense', 'refund'} or (value <= 0 if row['kind'] == 'expense' else value >= 0):
            raise ValueError('Expense direction does not match')
        if row['purpose'] and row['purpose'] not in PURPOSES:
            raise ValueError('Unknown Pace category')
        for field, maximum in [('note', 16384), ('original_category', 4096), ('source_location', 4096)]:
            if len(restore_text(row[field]).encode()) > maximum:
                raise ValueError('Expense text exceeds limit')
        precision = row['date_precision']
        if precision not in {'instant', 'civilDate', 'month'}:
            raise ValueError('Unknown date precision')
        when = date_evidence(row['date'], precision)
        if precision == 'instant':
            if not re.fullmatch(INSTANT_PATTERN, row['date']):
                raise ValueError('Instant requires a timezone')
        elif when['value'] != row['date']:
            raise ValueError('Date value does not match its precision')
        home_fields = ['home_minor', 'home_currency', 'rate', 'rate_date', 'rate_source', 'rate_policy']
        if any(row[f] for f in home_fields):
            if not all(row[f] for f in home_fields) or row['home_currency'] != target:
                raise ValueError('Conversion evidence is incomplete')
            rate = Decimal(row['rate'])
            if (not re.fullmatch(r'[0-9]+(?:\.[0-9]+)?', row['rate']) or len(row['rate'].encode()) > 80
                    or not restore_text(row['rate_source']).strip() or len(restore_text(row['rate_source']).encode()) > 512
                    or not rate.is_finite() or rate <= 0 or row['rate_policy'] not in {'transactionDate', 'periodAverage', 'userApproved'}):
                raise ValueError('Invalid conversion rate')
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', row['rate_date']):
                raise ValueError('Invalid reference date')
            date.fromisoformat(row['rate_date'])
            if precision == 'month' and row['rate_policy'] == 'transactionDate':
                raise ValueError('Monthly total cannot have a recovered transaction rate')
            with localcontext() as context:
                context.prec = 38
                expected = int((Decimal(value) / 10 ** scale * rate * 100).quantize(Decimal(1), rounding=ROUND_HALF_UP))
            home = checked_integer(row['home_minor'])
            if home != expected or (currency == target and (home != value or rate != 1)):
                raise ValueError('Converted amount does not match')
            estimates += 1
        else:
            home = value if currency == target else None
        original_totals[(currency, scale)] += value
        if decisions[key]['disposition'] == 'excluded':
            continue
        if decisions[key]['disposition'] == 'held' or not row['purpose'] or home is None:
            held.add(key)
            missing[scope].add(month_of(when, zone.key))
            continue
        ready += home
        month = month_of(when, zone.key)
        months.add(month)
        monthly_sources[month].add(scope)
        source_sums[(month, scope)] += home
        if precision == 'month':
            monthly_total += home
        else:
            dated_total += home
    totals = {}
    for row in tables['totals.csv']:
        key = (row['currency'], int(row['scale']))
        if key in totals:
            raise ValueError('Duplicate currency total')
        totals[key] = checked_integer(row['minor_units'])
    if dict(original_totals) != totals:
        raise ValueError('Original amounts do not reconcile')
    month_scopes = defaultdict(list)
    for row in tables['coverage.csv']:
        if restore_text(row['source_dataset']) not in source_ids or row['currency'] not in SCALES or row['status'] not in {'complete', 'partial', 'unknown', 'confirmedZero'}:
            raise ValueError('Invalid month evidence')
        if not re.fullmatch(r'\d{4}-\d{2}', row['start_month']) or not re.fullmatch(r'\d{4}-\d{2}', row['end_month']):
            raise ValueError('Invalid month value')
        date.fromisoformat(row['start_month'] + '-01'); date.fromisoformat(row['end_month'] + '-01')
        if row['start_month'] > row['end_month']:
            raise ValueError('Invalid month range')
        start_year, start_month = map(int, row['start_month'].split('-'))
        end_year, end_month = map(int, row['end_month'].split('-'))
        first = start_year * 12 + start_month - 1
        last = end_year * 12 + end_month - 1
        if last - first >= 1200:
            raise ValueError('Month evidence spans more than Pace can summarize')
        cutoff = manifest.get('throughDate')
        for number in range(first, last + 1):
            month = f'{number // 12:04d}-{number % 12 + 1:02d}'
            if row['currency'] != target or cutoff and month > cutoff[:7]:
                continue
            scope = restore_text(row['source_dataset'])
            status = row['status']
            partial_cutoff = bool(cutoff and month == cutoff[:7] and date.fromisoformat(cutoff).day != calendar.monthrange(int(cutoff[:4]), int(cutoff[5:7]))[1])
            if (month in missing[scope] or partial_cutoff) and status in {'complete', 'confirmedZero'}:
                status = 'partial'
            month_scopes[month].append((scope, status))
    for month, scopes in month_scopes.items():
        observed = monthly_sources[month]
        relevant = [(scope, status) for scope, status in scopes if not observed or scope in observed]
        complete = {scope for scope, status in relevant if status in {'complete', 'confirmedZero'}}
        for scope, status in relevant:
            if status == 'confirmedZero' and source_sums[(month, scope)] != 0:
                raise ValueError('A declared zero month contains expenses')
        if relevant and observed.issubset(complete) and not any(status in {'partial', 'unknown'} for _, status in relevant):
            months.add(month)
    if months:
        first, last = min(months), max(months)
        if (int(last[:4]) - int(first[:4])) * 12 + int(last[5:]) - int(first[5:]) >= 1200:
            raise ValueError('These dates span more than Pace can summarize. Check the date format or choose a shorter history.')
    # Check aggregate Int64 range independently of per-record correctness.
    checked_integer(str(ready)); checked_integer(str(dated_total)); checked_integer(str(monthly_total))
    average = str((Decimal(ready) / len(months)).quantize(Decimal(1), rounding=ROUND_HALF_UP)) if months else None
    return {'recordCount': len(rows), 'readyCount': sum(decisions[k]['disposition'] == 'included' for k in keys) - len({k for k in held if decisions[k]['disposition'] == 'included'}),
            'toCheckCount': len(held), 'targetCurrency': target, 'totalMinorUnits': str(ready),
            'datedTotalMinorUnits': str(dated_total), 'monthlyTotalMinorUnits': str(monthly_total),
            'recordedMonths': len(months), 'averageMinorUnits': average,
            'referenceEstimatedCount': estimates, 'months': sorted(months), 'sha256': digest(Path(path).read_bytes())}
