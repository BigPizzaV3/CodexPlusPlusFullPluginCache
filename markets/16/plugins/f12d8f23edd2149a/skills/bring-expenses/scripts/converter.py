"""Offline expense converter. Source text is data; never executed or sent away.
Money/date decisions are explicit. Harmless text cleanup is automatic.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, uuid, zipfile
from collections import Counter, defaultdict
from datetime import datetime, date, timezone
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from pathlib import Path
from zoneinfo import ZoneInfo

SCALES = {**dict.fromkeys('INR AED USD GBP EUR CAD AUD CHF SGD NZD CNY HKD'.split(), 2),
          **dict.fromkeys('JPY KRW VND'.split(), 0), **dict.fromkeys('KWD BHD OMR JOD TND'.split(), 3)}
PURPOSES = {'maintain', 'enjoy', 'build'}
MAX_FILE = 100 * 1024 * 1024
MAX_EXPANDED_WORKBOOK = 200 * 1024 * 1024
MAX_INPUT_ROWS = 100_000

def validate_workbook(path):
    if path.stat().st_size > MAX_FILE: raise ValueError("Source file exceeds limit")
    with zipfile.ZipFile(path) as archive:
        if len(archive.infolist()) > 10_000 or sum(x.file_size for x in archive.infolist()) > MAX_EXPANDED_WORKBOOK:
            raise ValueError("Expanded workbook exceeds limit")

def bounded_rows(iterator):
    result=[]
    for index,row in enumerate(iterator):
        if index >= MAX_INPUT_ROWS: raise ValueError("Source table exceeds row limit")
        result.append(row)
    return result

def clean(value):
    return re.sub(r'\s+', ' ', str(value or '').strip())

def json_bytes(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False) + '\n').encode()

def digest(value): return hashlib.sha256(value).hexdigest()

def amount_minor(value, currency, decimal_separator='.'):
    if currency not in SCALES: raise ValueError('Unsupported source currency')
    if isinstance(value, bool) or value is None: raise ValueError('Missing or invalid amount')
    text = str(value).strip().replace('\u00a0', '').replace(' ', '')
    if decimal_separator not in {'.', ','}: raise ValueError('Choose decimal separator')
    grouping = ',' if decimal_separator == '.' else '.'
    if grouping in text:
        if not re.fullmatch(r'-?\d{1,3}(?:' + re.escape(grouping) + r'\d{3})+(?:' + re.escape(decimal_separator) + r'\d+)?', text):
            raise ValueError('Ambiguous number separators')
        text = text.replace(grouping, '')
    if decimal_separator == ',': text = text.replace(',', '.')
    if not re.fullmatch(r'-?\d+(?:\.\d+)?', text): raise ValueError('Invalid amount')
    number = Decimal(text)
    rounded = (number * 10 ** SCALES[currency]).quantize(Decimal(1), rounding=ROUND_HALF_UP)
    if abs(number - rounded / 10 ** SCALES[currency]) > Decimal('0.000000001'):
        raise ValueError('Amount has more precision than source currency; review rounding')
    result = int(rounded)
    if not -(2**63) <= result < 2**63: raise ValueError('Amount exceeds supported range')
    return result

def date_evidence(value, precision, fmt=None):
    if precision == 'instant':
        text = value.isoformat() if isinstance(value, datetime) else str(value).strip()
        instant = datetime.fromisoformat(text.replace('Z', '+00:00'))
        if instant.tzinfo is None: raise ValueError('Instant needs an explicit timezone offset')
        return {'precision': 'instant', 'value': text}
    if isinstance(value, (date, datetime)):
        parsed = value
    elif fmt:
        parsed = datetime.strptime(str(value).strip(), fmt)
    else:
        text = str(value).strip()
        if precision == 'month': text += '-01'
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', text): raise ValueError('Choose date format for ambiguous dates')
        parsed = date.fromisoformat(text)
    return {'precision': precision, 'value': parsed.strftime('%Y-%m' if precision == 'month' else '%Y-%m-%d')}

def month_of(evidence, zone):
    if evidence['precision'] != 'instant': return evidence['value'][:7]
    return datetime.fromisoformat(evidence['value'].replace('Z', '+00:00')).astimezone(ZoneInfo(zone)).strftime('%Y-%m')

def through(evidence, cutoff, zone):
    if not cutoff: return True
    day = date.fromisoformat(cutoff)
    if evidence['precision'] == 'month':
        first = date.fromisoformat(evidence['value'] + '-01')
        next_month = date(first.year + first.month // 12, first.month % 12 + 1, 1)
        return next_month.toordinal() <= day.toordinal() + 1
    if evidence['precision'] == 'civilDate': return date.fromisoformat(evidence['value']) <= day
    return datetime.fromisoformat(evidence['value'].replace('Z', '+00:00')).astimezone(ZoneInfo(zone)).date() <= day

def load_rules(path=None):
    rules = json.loads(Path(path or Path(__file__).with_name('rules.json')).read_text())
    if any(v not in PURPOSES for v in rules['categoryDefaults'].values()): raise ValueError('Invalid purpose rule')
    for rule in rules.get('noteOverrides', []):
        if rule['purpose'] not in PURPOSES or len(rule['pattern']) > 1024: raise ValueError('Invalid note override')
        re.compile(rule['pattern'])
    return rules

def map_purpose(category, note, rules, specific=None):
    if specific:
        if specific.get('purpose') and specific['purpose'] not in PURPOSES: raise ValueError('Invalid transaction override')
        return specific.get('purpose'), specific.get('disposition', 'included'), specific.get('id', 'transaction-override'), specific.get('reason', 'Explicit transaction override')
    if clean(category).casefold() in {clean(k).casefold() for k in rules.get('categoryExclusions', [])}:
        return None, 'excluded', 'non-expense-category', 'Financial asset or transfer category'
    for rule in rules.get('excludePatterns', []):
        if re.search(rule['pattern'], note or '', re.I): return None, 'excluded', rule['id'], rule['reason']
    defaults = {clean(k).casefold(): v for k, v in rules['categoryDefaults'].items()}
    purpose = defaults.get(clean(category).casefold())
    matches = [rule for rule in rules.get('noteOverrides', []) if re.search(rule['pattern'], note or '', re.I)]
    if len(set(r['purpose'] for r in matches)) > 1:
        return purpose, 'held', 'conflicting-note-overrides', 'Multiple note rules disagree; review this transaction'
    if matches: return matches[0]['purpose'], 'included', matches[0]['id'], 'Transaction note overrides category default'
    if purpose: return purpose, 'included', 'category-default', 'Source category default'
    return None, 'held', 'missing-purpose', 'Choose a default for this source category'

MIXED_CATEGORIES={'subscriptions','gadgets','travel','travel (debt)','health & fitness','miscellaneous','others','business','education','education (debt)','apparels & accessories'}

def mapping_confidence(decision,category):
    if decision['disposition']=='held':return 'unresolved'
    if decision['ruleID']=='category-default':return 'low: mixed-category fallback' if clean(category).casefold() in MIXED_CATEGORIES else 'category default'
    return 'explicit rule or override; review source intent'

def record(source_key, dataset, value, currency, evidence, category, note, locator, rules, specific=None, normalization=None):
    minor = amount_minor(value, currency)
    if minor == 0: return None, {'sourceKey': source_key, 'disposition': 'excluded', 'ruleID': 'zero-cell', 'reason': 'Zero source cell; not a transaction or proof of a complete zero month'}
    purpose, disposition, rule, reason = map_purpose(category, note, rules, specific)
    row = {'sourceKey': source_key, 'sourceDataset': dataset, 'kind': 'refund' if minor < 0 else 'expense',
           'original': {'minorUnits': str(minor), 'currency': currency, 'scale': SCALES[currency]}, 'date': evidence}
    if purpose: row['purpose'] = purpose
    if len(source_key.encode()) > 512 or len(dataset.encode()) > 512: raise ValueError('Source identity exceeds limit')
    if note and len(str(note).encode()) > 16384: raise ValueError('Note exceeds limit; shorten explicitly before conversion')
    if note: row['note'] = str(note)
    if category: row['originalCategory'] = clean(category)
    if locator: row['sourceLocator'] = locator
    if normalization: row['normalization'] = normalization
    return row, {'sourceKey': source_key, 'disposition': disposition, 'ruleID': rule, 'reason': reason}

def master_rows(path, rules, controls):
    validate_workbook(path)
    from openpyxl import load_workbook
    workbook = load_workbook(path, read_only=True, data_only=True)
    sheet = workbook['Master Expenses']; iterator = iter(sheet.values); headers = next(iterator)
    records, decisions, audit = [], [], []
    for index, values in enumerate(iterator, 2):
        if index - 2 >= MAX_INPUT_ROWS: raise ValueError('Master exceeds row limit')
        item = dict(zip(headers, values)); granularity = item['Granularity']
        dataset = 'legacy-realm' if granularity == 'Dated app transaction' else 'legacy-monthly-actuals' if granularity == 'Monthly category total' else 'legacy-dated-sheet'
        # Curated master IDs are stable in this frozen master; Realm IDs are native.
        identity = str(item['Source transaction ID'] or item['Record ID'])
        key = dataset + '/' + identity
        precision = 'instant' if granularity == 'Dated app transaction' else 'month' if granularity == 'Monthly category total' else 'civilDate'
        evidence = date_evidence(item['Source UTC timestamp'] if precision == 'instant' else item['Period start'], precision)
        if not through(evidence, controls.get('throughDate'), controls['timeZone']):
            audit.append({'sourceKey': key, 'masterRecordID': item['Record ID'], 'disposition': 'excluded', 'ruleID': 'cutoff', 'reason': 'After historical cutoff', 'datePrecision': precision, 'date': evidence['value'], 'category': item['Category'], 'note': item['Comment'] or '', 'currency': item['Currency'], 'originalMinorUnits': str(amount_minor(item['Amount Original'], item['Currency'])), 'sourceLocator': f"{item['Source workbook']} / {item['Source sheet']} / {item['Source rows or cell']}"})
            continue
        row, decision = record(key, dataset, item['Amount Original'], item['Currency'], evidence, item['Category'], item['Comment'],
            f"{item['Source workbook']} / {item['Source sheet']} / {item['Source rows or cell']}", rules, controls.get('transactionOverrides', {}).get(str(item['Record ID'])))
        decisions.append(decision)
        if row: records.append(row)
        audit.append({**decision, 'masterRecordID': item['Record ID'], 'datePrecision': precision, 'date': evidence['value'],
            'mappingConfidence':mapping_confidence(decision,item['Category']),'category': item['Category'], 'note': item['Comment'] or '', 'purpose': (row or {}).get('purpose', ''), 'currency': item['Currency'],
            'originalMinorUnits': str(amount_minor(item['Amount Original'], item['Currency'])), 'sourceLocator': (row or {}).get('sourceLocator', '')})
    workbook.close()
    return records, decisions, audit

def canonical_rows(items, config, rules):
    """Long tables: explicit column map and expense/refund semantics."""
    records, decisions, audit = [], [], []
    occurrence = Counter(); columns = config['columns']; dataset = config['datasetID']
    for index, item in enumerate(items, 2):
        locator = f"{config.get('sheet', 'table')} / row {index}"
        kind = clean(item.get(columns.get('kind', ''), 'expense')).casefold()
        if kind not in {'expense', 'refund'}:
            audit.append({'sourceLocator': locator, 'disposition': 'excluded', 'reason': 'Non-expense source row', 'kind': kind}); continue
        currency = clean(item.get(columns.get('currency', ''), config.get('currency'))).upper()
        minor = amount_minor(item.get(columns['amount']), currency, config.get('decimalSeparator', '.'))
        if kind == 'refund' and minor > 0: minor = -minor
        if kind == 'expense' and minor < 0: raise ValueError('Negative expense needs explicit refund classification')
        evidence = date_evidence(item.get(columns['date']), config['datePrecision'], config.get('dateFormat'))
        category = clean(item.get(columns.get('category', ''))); note = str(item.get(columns.get('note', ''), '') or '')
        native_id = clean(item.get(columns.get('id', '')))
        if native_id: key = dataset + '/' + native_id
        else:
            fingerprint = digest(json_bytes([minor, currency, evidence, category, clean(note)]))
            occurrence[fingerprint] += 1; key = f'{dataset}/fingerprint/{fingerprint}/{occurrence[fingerprint]}'
        if not through(evidence, config.get('throughDate'), config['timeZone']):
            audit.append({'sourceKey': key, 'sourceLocator': locator, 'disposition': 'excluded', 'reason': 'After cutoff', 'date': evidence['value'], 'datePrecision':evidence['precision'], 'category':category, 'note':note,'currency':currency,'originalMinorUnits':str(minor)}); continue
        value = Decimal(minor) / 10 ** SCALES[currency]
        row, decision = record(key, dataset, value, currency, evidence, category, note, locator, rules, config.get('transactionOverrides', {}).get(key))
        decisions.append(decision)
        if row: records.append(row)
        audit.append({**decision, 'sourceLocator': locator, 'mappingConfidence':mapping_confidence(decision,category),'category': category, 'purpose': (row or {}).get('purpose', ''), 'currency': currency, 'originalMinorUnits': str(minor)})
    if not columns.get('id') and not config.get('keepUnidentifiedRepeats', False):
        repeats = {fingerprint for fingerprint, count in occurrence.items() if count > 1}
        held = {row['sourceKey'] for row in records if '/fingerprint/' in row['sourceKey'] and row['sourceKey'].split('/fingerprint/')[1].rsplit('/',1)[0] in repeats}
        for decision in decisions:
            if decision['sourceKey'] in held and decision['disposition'] == 'included':
                decision.update(disposition='held', ruleID='unidentified-repeat', reason='Matching rows without native IDs may be duplicates or genuine repeated spending; choose explicitly')
        by_key = {d['sourceKey']: d for d in decisions}
        for row in audit:
            if row.get('sourceKey') in held: row.update(by_key[row['sourceKey']])
    return records, decisions, audit

def table_rows(path, config):
    if path.stat().st_size > MAX_FILE: raise ValueError('Source file exceeds limit')
    if path.suffix.casefold() in {'.csv', '.tsv'}:
        with path.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream, delimiter=config.get('delimiter', '\t' if path.suffix.casefold() == '.tsv' else ','))
            if len(set(reader.fieldnames or [])) != len(reader.fieldnames or []): raise ValueError('Duplicate source headers')
            return bounded_rows(reader)
    if path.suffix.casefold() == '.xlsx':
        from openpyxl import load_workbook
        validate_workbook(path)
        workbook = load_workbook(path, read_only=True, data_only=True)
        sheet = workbook[config['sheet']]
        headers = [clean(v) for v in next(sheet.iter_rows(min_row=config.get('headerRow', 1), max_row=config.get('headerRow', 1), values_only=True))]
        rows = sheet.iter_rows(min_row=config.get('firstDataRow', config.get('headerRow', 1) + 1), max_row=config.get('lastDataRow'), values_only=True)
        if len(set(headers)) != len(headers): raise ValueError('Duplicate/blank headers; choose a clean table range')
        result = [dict(zip(headers, row)) for row in bounded_rows(rows) if any(v is not None for v in row)]
        workbook.close(); return result
    raise ValueError('Use CSV, TSV, XLSX or the supported Realm adapter')

def matrix_rows(path, config, rules):
    """Wide Actual matrices. Month header and selected expense rows are explicit."""
    validate_workbook(path)
    from openpyxl import load_workbook
    workbook = load_workbook(path, read_only=False, data_only=True)
    formulas = load_workbook(path, read_only=False, data_only=False)
    sheet = workbook[config['sheet']]; original = formulas[config['sheet']]
    columns = config.get('monthColumns')
    if columns is None:
        columns = []; current_month = None
        for col in range(1, sheet.max_column + 1):
            header = sheet.cell(config['monthHeaderRow'], col).value
            if isinstance(header, (date, datetime)): current_month = header.strftime('%Y-%m')
            if clean(sheet.cell(config['actualLabelRow'], col).value).casefold() == 'actual':
                if not current_month: raise ValueError('Actual column has no month')
                columns.append({'column': col, 'month': current_month})
    if len(columns)*len(config['expenseRows']) > MAX_INPUT_ROWS: raise ValueError('Matrix exceeds selected-cell limit')
    records, decisions, audit = [], [], []
    for column in columns:
        for row_index in config['expenseRows']:
            cell = sheet.cell(row_index, column['column']); value = cell.value
            source_key = config['datasetID'] + '/' + column['month'] + '/' + digest(clean(sheet.cell(row_index, config['categoryColumn']).value).casefold().encode())[:24]
            if value is None:
                if isinstance(original[cell.coordinate].value, str) and original[cell.coordinate].value.startswith('='):
                    raise ValueError('Missing cached formula value; recalculate in the source app')
                audit.append({'sourceKey': source_key, 'sourceLocator': cell.coordinate, 'disposition': 'excluded', 'reason': 'Blank Actual cell is unknown'})
                continue
            category = clean(sheet.cell(row_index, config['categoryColumn']).value)
            category = config.get('categoryAliases', {}).get(category, category)
            evidence = date_evidence(column['month'], 'month')
            if not through(evidence, config.get('throughDate'), config['timeZone']):
                audit.append({'sourceKey': source_key, 'sourceLocator': cell.coordinate, 'category': category,
                              'currency': config['currency'], 'originalMinorUnits': str(amount_minor(value, config['currency'])),
                              'disposition': 'excluded', 'reason': 'After historical cutoff'})
                continue
            comment = original[cell.coordinate].comment
            note = comment.text if comment else None
            if isinstance(original[cell.coordinate].value, str) and original[cell.coordinate].value.startswith('=') and value is None:
                raise ValueError('Missing cached formula value; recalculate in the source app')
            item, decision = record(source_key, config['datasetID'], value, config['currency'], evidence, category, note,
                config['sheet'] + ' / ' + cell.coordinate, rules, config.get('transactionOverrides', {}).get(source_key))
            if item: records.append(item)
            decisions.append(decision)
            audit.append({**decision, 'sourceLocator': cell.coordinate, 'category': category, 'originalMinorUnits':str(amount_minor(value, config['currency']))})
    workbook.close(); formulas.close()
    return records, decisions, audit

def realm_rows(path, config, rules):
    import subprocess, tempfile, os
    with tempfile.TemporaryDirectory(prefix='PaceRealmRows-') as directory:
        output = Path(directory) / 'rows.json'
        environment = dict(os.environ)
        if config.get('realmNodeModules'): environment['NODE_PATH'] = str(Path(config['realmNodeModules']).resolve())
        result = subprocess.run([config.get('nodeExecutable', 'node'), str(Path(__file__).with_name('realm_reader.cjs')), str(path.resolve()), str(output)],
                                env=environment, capture_output=True, timeout=120)
        if result.returncode != 0: raise ValueError('Realm could not be read. Use an unencrypted supported backup or export CSV from the original app.')
        items = json.loads(output.read_text())
        # Native ID without owner is permitted only when the logical source scope
        # explicitly chooses it and the selected rows are unique.
        return canonical_rows(items, config, rules)

def package(records, decisions, coverage, options, sources, rules):
    if len(records) > 50_000 or len(sources) > 100: raise ValueError('Transfer exceeds limits')
    if len(set(x['sourceKey'] for x in records)) != len(records): raise ValueError('Duplicate source identities; review exports instead of concatenating')
    if len(set(x['sourceKey'] for x in decisions)) != len(decisions): raise ValueError('Duplicate decision identities')
    totals = defaultdict(int)
    for row in records:
        money = row['original']; totals[(money['currency'], money['scale'])] += int(money['minorUnits'])
    for value in totals.values():
        if not -(2**63) <= value < 2**63: raise ValueError('Original total overflow')
    files = {'expenses.jsonl': b''.join(json_bytes(r) for r in sorted(records, key=lambda r: r['sourceKey'])),
        'decisions.json': json_bytes(sorted(decisions, key=lambda r: r['sourceKey'])), 'coverage.json': json_bytes(coverage),
        'reconciliation.json': json_bytes({'recordCount': len(records), 'originalTotals': [{'currency': c, 'scale': s, 'minorUnits': str(v)} for (c, s), v in sorted(totals.items())]})}
    manifest = {'schema': 'PaceExpenseTransfer', 'version': 1, 'converterVersion': 'pace-offline-1', 'ruleVersion': rules['version'],
        'timeZone': options['timeZone'], 'calendar': 'gregorian', 'targetCurrency': options['targetCurrency'],
        'sources': sources, 'recordCount': len(records), 'files': [{'name': n, 'bytes': len(d), 'sha256': digest(d)} for n, d in sorted(files.items())]}
    if options.get('throughDate'): manifest['throughDate'] = options['throughDate']
    # Logical content identity is deterministic; no user values in random logs.
    manifest['packageID'] = str(uuid.uuid5(uuid.NAMESPACE_URL, digest(json_bytes(manifest))))
    files['manifest.json'] = json_bytes(manifest)
    if any(len(d) > 25*1024*1024 for d in files.values()) or sum(map(len, files.values())) > MAX_FILE: raise ValueError('Package exceeds limits')
    return files

def csv_archive(files):
    """One portable CSV ZIP family for native backups and converted expenses."""
    manifest=json.loads(files['manifest.json'])
    if manifest.get('schema')!='PaceExpenseTransfer' or manifest.get('version')!=1:
        raise ValueError('Expected validated expense evidence')
    records=[json.loads(line) for line in files['expenses.jsonl'].splitlines() if line.strip()]
    def table(columns, rows, text_columns=()):
        stream=io.StringIO(newline=''); writer=csv.writer(stream,quoting=csv.QUOTE_ALL,lineterminator='\r\n');writer.writerow(columns)
        for row in rows:
            values=[]
            for column in columns:
                raw=row.get(column,''); value='' if raw is None else str(raw)
                if column in text_columns and (value.startswith("'") or value.lstrip().startswith(('=','+','-','@'))): value="'"+value
                values.append(value)
            writer.writerow(values)
        return stream.getvalue().encode('utf-8')
    columns=['source_key','source_dataset','kind','original_minor','original_currency','original_scale','date_precision','date','purpose','note','original_category','source_location','home_minor','home_currency','rate','rate_date','rate_source','rate_policy']
    rows=[]
    for record in records:
        original=record['original'];when=record['date'];rate=record.get('normalization',{})
        rows.append(dict(zip(columns,[record['sourceKey'],record['sourceDataset'],record['kind'],original['minorUnits'],original['currency'],original['scale'],when['precision'],when['value'],record.get('purpose',''),record.get('note',''),record.get('originalCategory',''),record.get('sourceLocator',''),rate.get('minorUnits',''),rate.get('currency',''),rate.get('rate',''),rate.get('rateDate',''),rate.get('provider',''),rate.get('policy','')])))
    output={'expenses.csv':table(columns,rows,{'source_key','source_dataset','note','original_category','source_location','rate_source'}),
        'coverage.csv':table(['source_dataset','start_month','end_month','currency','status'],[dict(zip(['source_dataset','start_month','end_month','currency','status'],[r['sourceDataset'],r['startMonth'],r['endMonth'],r['currency'],r['status']])) for r in json.loads(files['coverage.json'])],{'source_dataset'}),
        'decisions.csv':table(['source_key','disposition','rule','reason'],[dict(zip(['source_key','disposition','rule','reason'],[r['sourceKey'],r['disposition'],r['ruleID'],r['reason']])) for r in json.loads(files['decisions.json'])],{'source_key','rule','reason'}),
        'totals.csv':table(['currency','scale','minor_units'],[{'currency':r['currency'],'scale':r['scale'],'minor_units':r['minorUnits']} for r in json.loads(files['reconciliation.json'])['originalTotals']])}
    manifest={k:v for k,v in manifest.items() if k not in {'schema','version','files'}}
    manifest.update(schema='PaceCSVArchive',version=8,contents='expenses',files=sorted(output),checksums={name:digest(data) for name,data in sorted(output.items())})
    output['manifest.json']=json_bytes(manifest)
    return output

def write_archive(files, destination, *, legacy=False):
    files=files if legacy else csv_archive(files)
    if sum(len(v) for v in files.values()) >= 100 * 1024 * 1024 or any(len(v) > 25 * 1024 * 1024 for v in files.values()):
        raise ValueError('Archive exceeds limits')
    compression = zipfile.ZIP_STORED if legacy else zipfile.ZIP_DEFLATED
    with zipfile.ZipFile(destination, 'w', compression=compression, allowZip64=False) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0)); info.compress_type = compression
            archive.writestr(info, data)

def write_audit(rows, destination):
    keys = sorted(set().union(*(r.keys() for r in rows))) if rows else ['sourceKey']
    with destination.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, keys); writer.writeheader()
        for row in rows:
            # CSV opened in spreadsheets must not execute legacy notes as formulas.
            writer.writerow({k: "'"+str(v) if str(v).lstrip().startswith(('=', '+', '-', '@')) else v for k,v in row.items()})

def main():
    parser = argparse.ArgumentParser(description='Convert historical expenses offline. No Pace ledger access.')
    parser.add_argument('input', type=Path); parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--rules', type=Path); parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--master', action='store_true')
    args = parser.parse_args(); options = json.loads(args.config.read_text()); rules = load_rules(args.rules)
    ZoneInfo(options['timeZone'])
    if SCALES.get(options['targetCurrency']) != 2: raise ValueError('Pace home currency must use two decimal places')
    if args.master: records, decisions, audit = master_rows(args.input, rules, options)
    elif args.input.suffix.casefold() == '.realm': records, decisions, audit = realm_rows(args.input, options, rules)
    elif options.get('layout') == 'actualMatrix': records, decisions, audit = matrix_rows(args.input, options, rules)
    else: records, decisions, audit = canonical_rows(table_rows(args.input, options), options, rules)
    sources = options.get('sources') or [{'id': options['datasetID'], 'name': args.input.name, 'format': args.input.suffix.lstrip('.')}]
    if options.get('fxPolicy')=='userApprovedECBReference':
        from reference_rates import apply_reference_estimates
        rate_audit=apply_reference_estimates(records, options['referenceRatesPath'], options)
        write_audit(rate_audit,args.output.with_suffix('.rates.csv'))
        rules={**rules,'version':rules['version']+'+ecb-reference-1'}
    files = package(records, decisions, options.get('coverage', []), options, sources, rules)
    write_archive(files, args.output)
    write_audit(audit, args.output.with_suffix('.audit.csv'))
    args.output.with_suffix('.reconciliation.json').write_bytes(files['reconciliation.json'])
    print(json.dumps({'records':len(records), 'decisions':dict(Counter(d['disposition'] for d in decisions)), 'archiveSHA256':digest(args.output.read_bytes())}))

if __name__ == '__main__': main()
