"""Pace for ChatGPT file-workspace entry point. No app access or network calls."""
from __future__ import annotations

import argparse
import csv
import json
import re
import tempfile
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import date
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

from converter import (PURPOSES, SCALES, amount_minor, clean, date_evidence, digest, json_bytes,
                       load_rules, master_rows, matrix_rows, package, realm_rows, record,
                       through, write_archive, write_audit)
from package_validation import INSTANT_PATTERN, validate_archive
from source_readers import SourceError, inspect_files, json_default, read_tables

NONEXPENSES = {'income', 'transfer', 'investment', 'principal', 'budget', 'pending', 'balance', 'excluded'}


def purpose_rules(config):
    rules = load_rules(Path(__file__).with_name('general-rules.json'))
    for category, purpose in config.get('categoryDefaults', {}).items():
        if purpose not in PURPOSES:
            raise ValueError('Choose Maintain, Enjoy or Build for each category.')
        rules['categoryDefaults'][category] = purpose
    for override in config.get('noteKeywordOverrides', []):
        keywords = override['keywords']
        if override['purpose'] not in PURPOSES or not keywords or len(keywords) > 30:
            raise ValueError('Invalid note rule.')
        if any(not isinstance(k, str) or not k.strip() or len(k) > 200 for k in keywords):
            raise ValueError('Invalid note keyword.')
        # Literal phrases only. Uploaded content can never supply regex/code.
        rules['noteOverrides'].append({'id': override['id'], 'purpose': override['purpose'],
                                       'pattern': '|'.join(re.escape(k) for k in keywords)})
    return rules


def field(item, columns, key, default=''):
    return item.get(columns.get(key, ''), default)


def convert_table(items, profile, rules, options, occurrence=None):
    columns = profile['columns']
    if not {'amount', 'date'}.issubset(columns):
        raise ValueError('Choose the expense amount and date columns.')
    if not columns.get('kind') and not profile.get('expenseOnly') and not profile.get('signedOutflows'):
        raise ValueError('Confirm this is an expense-only table, or identify the transaction types first.')
    dataset = profile['datasetID']
    records, decisions, audit, issues = [], [], [], []
    occurrence = occurrence if occurrence is not None else Counter()
    for index, item in enumerate(items, 1):
        locator = clean(item.get('__pace_location') or f'row {index}')
        if profile.get('sheet'):
            locator = f"{profile['sheet']} / {locator}"
        locator = f"{profile.get('sourceName', dataset)} / {locator}"
        raw_amount, raw_date = field(item, columns, 'amount', None), field(item, columns, 'date', None)
        category, note = clean(field(item, columns, 'category')), str(field(item, columns, 'note') or '')
        native_id = clean(field(item, columns, 'id'))
        entry = {'sourceDataset': dataset, 'sourceLocator': locator, 'category': category,
                 'sourceAmount': raw_amount, 'sourceDate': raw_date}
        try:
            # Exact exclusions based on understood source flags occur before
            # money parsing. Income is accounted for, never coerced into an expense.
            filters = profile.get('excludeWhere', {})
            rejected = next((key for key, values in filters.items() if clean(item.get(key)).casefold() in {str(v).casefold() for v in values}), None)
            raw_kind = clean(field(item, columns, 'kind')).casefold()
            kind_map = {str(k).casefold(): v for k, v in profile.get('kindMap', {}).items()}
            kind = kind_map.get(raw_kind, raw_kind) if raw_kind else 'expense' if profile.get('expenseOnly') else ''
            if rejected or kind in NONEXPENSES or (profile.get('signedOutflows') and category.startswith('[') and category.endswith(']')):
                entry.update(disposition='excluded', reason='Source flag excludes this record' if rejected else f'Not an expense: {kind or "account transfer"}')
                audit.append(entry)
                continue
            if item.get('has_splits') and not profile.get('splitsReviewed'):
                raise SourceError('split_transaction', 'This payment contains several parts. Check its expense and transfer portions.')
            currency = clean(field(item, columns, 'currency', profile.get('currency'))).upper()
            minor = amount_minor(raw_amount, currency, profile.get('decimalSeparator', '.'))
            if profile.get('signedOutflows') and not raw_kind:
                if minor < 0:
                    kind, minor = 'expense', -minor
                else:
                    raise SourceError('incoming_payment', 'Is this a refund or money coming in?')
            elif kind == 'expense' and minor < 0:
                if profile.get('signedOutflows'):
                    minor = -minor
                else:
                    raise SourceError('negative_expense', 'Is this negative amount a refund?')
            elif kind == 'refund' and minor > 0:
                minor = -minor
            if kind not in {'expense', 'refund'}:
                raise SourceError('transaction_type', 'Is this an expense, a refund or a transfer?')
            precision = profile.get('datePrecision')
            if precision not in {'instant', 'civilDate', 'month'}:
                raise SourceError('date_format', 'Choose whether these records contain a time, a date or a monthly total.')
            when = date_evidence(raw_date, precision, profile.get('dateFormat'))
            if precision == 'instant' and not re.fullmatch(INSTANT_PATTERN, when['value']):
                raise SourceError('date_format', 'This timestamp needs a complete original time and timezone offset.')
            entry.update(currency=currency, originalMinorUnits=str(minor), date=when['value'], datePrecision=precision)
            if not through(when, options.get('throughDate'), options['timeZone']):
                entry.update(disposition='excluded', reason='After the chosen last date')
                audit.append(entry)
                continue
            if native_id:
                key = dataset + '/' + native_id
            else:
                signature = digest(json_bytes([minor, currency, when, category, clean(note)]))
                scoped_signature = (dataset, signature)
                occurrence[scoped_signature] += 1
                key = f'{dataset}/fingerprint/{signature}/{occurrence[scoped_signature]}'
            specific = profile.get('transactionOverrides', {}).get(key)
            value, decision = record(key, dataset, Decimal(minor) / 10 ** SCALES[currency], currency,
                                     when, category, note, locator, rules, specific)
            if profile.get('extractionNeedsReview') and not specific and decision['disposition'] == 'included':
                decision.update(disposition='held', ruleID='document-extraction', reason='Check this amount and date against the original page before adding it.')
            decisions.append(decision)
            if value:
                records.append(value)
            entry.update(decision)
            entry['purpose'] = (value or {}).get('purpose', '')
            audit.append(entry)
        except (ValueError, TypeError, KeyError, ArithmeticError) as error:
            issue = {**entry, 'code': getattr(error, 'code', 'unreadable_value'),
                     'message': str(error) if isinstance(error, (ValueError, SourceError)) else 'This amount or date could not be read.',
                     'disposition': 'needs_source_fix'}
            issues.append(issue)
            audit.append(issue)
    repeats = {signature for (scope, signature), count in occurrence.items() if scope == dataset and count > 1}
    if not profile.get('keepUnidentifiedRepeats'):
        held = {r['sourceKey'] for r in records if '/fingerprint/' in r['sourceKey'] and r['sourceKey'].rsplit('/', 1)[0].split('/fingerprint/')[-1] in repeats}
        for decision in decisions:
            if decision['sourceKey'] in held and decision['disposition'] == 'included':
                decision.update(disposition='held', ruleID='unidentified-repeat', reason='These matching purchases may be separate expenses or copies. Choose before adding them.')
    return records, decisions, audit, issues


def reconcile_copies(records, decisions, audit):
    """Same proven source identity and fact: one record; conflicts stay held."""
    by_key, decision_by_key = {}, {}
    for decision in decisions:
        decision_by_key.setdefault(decision['sourceKey'], decision)
    conflicts = []
    for row in records:
        key = row['sourceKey']
        if key not in by_key:
            by_key[key] = row
            continue
        prior = by_key[key]
        # Location is presentation evidence, not transaction identity.
        left, right = [{k: v for k, v in r.items() if k != 'sourceLocator'} for r in (prior, row)]
        if left != right:
            decision_by_key[key].update(disposition='held', ruleID='source-conflict', reason='Two copies give different details for this expense. Choose the correct copy.')
            conflicts.append({'code': 'source_conflict', 'sourceKey': key, 'savedSource': prior,
                              'otherSource': row, 'message': 'These copies disagree. Choose one.'})
        else:
            entry = next((e for e in reversed(audit) if e.get('sourceKey') == key and e.get('sourceLocator') == row.get('sourceLocator')), None)
            if entry:
                entry.update(disposition='overlapping_copy', reason='Same original source identity and details already included in this file')
    return list(by_key.values()), list(decision_by_key.values()), conflicts


def flag_overlaps(records, decisions, profiles):
    """Only accounts explicitly placed in one overlap group are comparable."""
    groups = {p['datasetID']: p.get('overlapGroup', p['datasetID']) for p in profiles}
    values = defaultdict(list)
    from converter import month_of
    for row in records:
        money = row['original']
        group = groups[row['sourceDataset']]
        values[(group, money['currency'], row.get('purpose'), month_of(row['date'], profiles[0]['timeZone']))].append(row)
    by_key = {d['sourceKey']: d for d in decisions}
    for rows in values.values():
        if any(r['date']['precision'] == 'month' for r in rows) and any(r['date']['precision'] != 'month' for r in rows):
            for row in rows:
                decision = by_key[row['sourceKey']]
                if decision['disposition'] == 'included':
                    decision.update(disposition='held', ruleID='monthly-detail-overlap', reason='A monthly total and individual purchases cover the same spending. Choose what to keep.')


def convert(config, output_directory):
    options = config['options']
    target = options['targetCurrency']
    if SCALES.get(target) != 2:
        raise ValueError('Pace does not currently support that home currency for this import.')
    ZoneInfo(options['timeZone'])
    if options.get('throughDate'):
        date.fromisoformat(options['throughDate'])
    if options.get('fxPolicy', 'pending') not in {'pending', 'userApprovedECBReference'}:
        raise ValueError('Choose a supported currency conversion policy.')
    if not 1 <= len(config['sources']) <= 100:
        raise ValueError('Choose between one and 100 source tables.')
    rules = purpose_rules(config)
    records, decisions, audit, issues, sources, coverage, profiles = [], [], [], [], [], [], []
    total_bytes = 0
    seen_paths = set()
    occurrences = Counter()
    for source in config['sources']:
        path = Path(source['path'])
        if path.resolve() not in seen_paths:
            total_bytes += path.stat().st_size
            seen_paths.add(path.resolve())
        if total_bytes > 100 * 1024 * 1024:
            raise ValueError('The selected sources exceed 100 MiB.')
        before = digest(path.read_bytes())
        if source.get('sha256') and source['sha256'] != before:
            raise ValueError('A file changed after it was inspected. Read it again before converting.')
        profile = {**source['profile'], **options, 'sourceName': source.get('name', path.name)}
        profiles.append(profile)
        if not profile.get('datasetID') or len(profile['datasetID'].encode()) > 512:
            raise ValueError('Give this source a stable app/account identity.')
        if profile.get('adapter') == 'master':
            r, d, a = master_rows(path, rules, profile)
            problem = []
            source_defs = [{'id': identity, 'name': source.get('name', path.name), 'format': 'curated master'} for identity in sorted({v['sourceDataset'] for v in r})]
        elif profile.get('layout') == 'actualMatrix':
            r, d, a = matrix_rows(path, profile, rules)
            problem = []
            source_defs = [{'id': profile['datasetID'], 'name': source.get('name', path.name), 'format': 'monthly actuals'}]
        elif path.suffix.casefold() == '.realm':
            r, d, a = realm_rows(path, profile, rules)
            problem = []
            source_defs = [{'id': profile['datasetID'], 'name': source.get('name', path.name), 'format': 'realm'}]
        else:
            tables = read_tables(path, profile)
            selected = [t for t in tables if t[0] == profile.get('sheet', profile.get('table', t[0]))]
            if len(selected) != 1 or selected[0][3].get('layoutQuestion'):
                raise ValueError('Choose one expense table and its layout before converting.')
            r, d, a, problem = convert_table(selected[0][2], profile, rules, options, occurrences)
            source_defs = [{'id': profile['datasetID'], 'name': source.get('name', path.name), 'format': path.suffix.lstrip('.')}]
        if digest(path.read_bytes()) != before:
            raise ValueError('The source changed during reading. Start again with a saved copy.')
        for entry in a:
            entry['sourceName'] = profile['sourceName']
        records.extend(r); decisions.extend(d); audit.extend(a); issues.extend(problem)
        sources.extend(source_defs); coverage.extend(profile.get('coverage', []))
    if issues and not config.get('allowPartial'):
        return {'status': 'needs_choices', 'sourceIssueCount': len(issues), 'issues': issues,
                'message': 'Some rows could not be read. Fix them or explicitly continue with the other expenses. No import file was created.'}
    records, decisions, conflicts = reconcile_copies(records, decisions, audit)
    issues.extend(conflicts)
    # Matching ID-less rows across files remain separate evidence until chosen.
    counts = Counter(r['sourceKey'].rsplit('/', 1)[0] for r in records if '/fingerprint/' in r['sourceKey'])
    keep_repeats = {p['datasetID']: bool(p.get('keepUnidentifiedRepeats')) for p in profiles}
    by_key = {d['sourceKey']: d for d in decisions}
    for row in records:
        if '/fingerprint/' in row['sourceKey'] and counts[row['sourceKey'].rsplit('/', 1)[0]] > 1 and not keep_repeats.get(row['sourceDataset']):
            decision = by_key[row['sourceKey']]
            if decision['disposition'] == 'included':
                decision.update(disposition='held', ruleID='unidentified-repeat', reason='These matching purchases may be separate expenses or copies. Choose before adding them.')
    # Master adapter has frozen internal scopes rather than the profile scope.
    scoped_profiles = [{**profiles[0], 'datasetID': identity} for identity in {r['sourceDataset'] for r in records}]
    scoped_profiles.extend(profiles)
    flag_overlaps(records, decisions, scoped_profiles)
    source_ids = {}
    for source in sources:
        source_ids.setdefault(source['id'], source)
    rate_audit = []
    if options.get('fxPolicy') == 'userApprovedECBReference':
        from reference_rates import apply_reference_estimates
        rate_audit = apply_reference_estimates(records, config['referenceRatesPath'], options)
        rules['version'] += '+ecb-reference-1'
    files = package(records, decisions, coverage, options, list(source_ids.values()), rules)
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='pace-delivery-', dir=output) as temp:
        staging = Path(temp)
        archive = staging / 'Pace Expenses.zip'
        write_archive(files, archive)
        summary = validate_archive(archive)
        # Decision changes (repeats/overlap) must appear in the downloadable audit.
        by_key = {d['sourceKey']: d for d in decisions}
        for entry in audit:
            if entry.get('sourceKey') in by_key and entry.get('disposition') != 'overlapping_copy':
                entry.update(by_key[entry['sourceKey']])
        write_audit(audit, staging / 'Mapping audit.csv')
        if rate_audit:
            write_audit(rate_audit, staging / 'Currency estimates.csv')
        reconciliation = {**json.loads(files['reconciliation.json']), 'summary': summary,
                          'sourceRows': len(audit),
                          'outcomes': dict(Counter(e['disposition'] for e in audit)), 'sourceIssues': issues,
                          'sourceFiles': [{'name': s.get('name', Path(s['path']).name), 'sha256': digest(Path(s['path']).read_bytes())} for s in config['sources']]}
        (staging / 'Reconciliation.json').write_text(json.dumps(reconciliation, default=json_default, ensure_ascii=False, indent=2))
        # A portable mapping/crosswalk permits reuse without permanent service storage.
        crosswalk = {'version': 1, 'sources': [{'name': s.get('name'), 'profile': s['profile']} for s in config['sources']],
                     'identities': [{'sourceKey': r['sourceKey'], 'sourceDataset': r['sourceDataset'], 'date': r['date'], 'original': r['original']} for r in records]}
        (staging / 'Source identities.json').write_text(json.dumps(crosswalk, ensure_ascii=False, indent=2))
        entries = [{**r, 'decision': by_key[r['sourceKey']], 'needsChoice': by_key[r['sourceKey']]['disposition'] == 'held' or (by_key[r['sourceKey']]['disposition'] == 'included' and (not r.get('purpose') or r['original']['currency'] != target and 'normalization' not in r))} for r in records]
        result = {'status': 'ready', 'summary': summary, 'sourceIssueCount': sum(i.get('disposition') == 'needs_source_fix' for i in issues),
                  'issues': issues, 'expenses': entries, 'downloads': ['Pace Expenses.zip', 'Mapping audit.csv', 'Reconciliation.json', 'Source identities.json'] + (['Currency estimates.csv'] if rate_audit else [])}
        (staging / 'Review.json').write_text(json.dumps(result, default=json_default, ensure_ascii=False))
        for artifact in staging.iterdir():
            if (output / artifact.name).exists():
                raise ValueError('Choose a new output folder so the previous download stays intact.')
        for artifact in staging.iterdir():
            artifact.replace(output / artifact.name)
    return {k: v for k, v in result.items() if k not in {'expenses', 'issues'}}


def review(path, query='', offset=0, limit=50, only_choices=False):
    result = json.loads(Path(path).read_text())
    values = result.get('expenses', [])
    term = query.strip().casefold()
    matches = [row for row in values if (not only_choices or row['needsChoice']) and
               (not term or term in ' '.join(str(row.get(k, '')) for k in ['note', 'purpose', 'originalCategory', 'sourceLocator', 'date', 'original']).casefold())]
    return {'summary': result.get('summary'), 'matchedCount': len(matches), 'offset': offset,
            'items': matches[offset:offset + limit], 'sourceIssues': result.get('issues', [])[:limit]}


def main():
    parser = argparse.ArgumentParser(description='Prepare old expenses for Pace; never access or change the app.')
    commands = parser.add_subparsers(dest='command', required=True)
    inspect = commands.add_parser('inspect'); inspect.add_argument('files', nargs='+'); inspect.add_argument('--workdir', required=True)
    generate = commands.add_parser('convert'); generate.add_argument('--config', required=True); generate.add_argument('--output', required=True)
    validate = commands.add_parser('validate'); validate.add_argument('archive')
    browse = commands.add_parser('review'); browse.add_argument('result'); browse.add_argument('--query', default=''); browse.add_argument('--offset', type=int, default=0); browse.add_argument('--limit', type=int, default=50); browse.add_argument('--only-choices', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'inspect':
            value = inspect_files(args.files, args.workdir)
        elif args.command == 'convert':
            value = convert(json.loads(Path(args.config).read_text()), args.output)
        elif args.command == 'validate':
            value = validate_archive(args.archive)
        else:
            if args.offset < 0 or not 1 <= args.limit <= 100:
                raise ValueError('Choose a page of 1–100 expenses.')
            value = review(args.result, args.query, args.offset, args.limit, args.only_choices)
        print(json.dumps(value, default=json_default, ensure_ascii=False, allow_nan=False))
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'status': 'needs_choices', 'code': getattr(error, 'code', 'conversion'),
                          'message': str(error) if isinstance(error, ValueError) else 'The selected file or conversion settings could not be read. No Pace records changed.'}))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
