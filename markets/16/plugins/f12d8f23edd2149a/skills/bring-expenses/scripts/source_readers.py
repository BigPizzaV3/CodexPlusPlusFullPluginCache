"""Bounded, read-only discovery. Source contents never become executable code."""
from __future__ import annotations

import csv
import io
import json
import re
import sqlite3
import stat
import zipfile
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path, PurePosixPath

from converter import MAX_FILE, MAX_INPUT_ROWS, bounded_rows, clean, digest, validate_workbook

MAX_MEMBERS = 10_000
MAX_EXPANDED = 200 * 1024 * 1024
SUPPORTED = {'.csv', '.tsv', '.txt', '.xlsx', '.json', '.jsonl', '.ndjson',
             '.sqlite', '.sqlite3', '.db', '.ofx', '.qfx', '.qif', '.realm', '.pdf'}
HEADER_WORDS = {'date', 'amount', 'cost', 'category', 'description', 'transaction',
                'transaction date', 'note', 'currency', 'debit', 'credit', 'id'}


class SourceError(ValueError):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def json_default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    raise TypeError('Unsupported source value')


def checked_path(path):
    path = Path(path)
    if not path.is_file() or path.is_symlink():
        raise SourceError('missing_file', 'Choose the source file again.')
    if path.stat().st_size > MAX_FILE:
        raise SourceError('source_too_large', 'This file is too large. Export a shorter date range.')
    return path


def read_text(path, encoding=None):
    data = checked_path(path).read_bytes()
    if encoding:
        try:
            return data.decode(encoding), encoding
        except (UnicodeError, LookupError):
            raise SourceError('encoding', 'This file cannot be read with that text encoding.') from None
    for codec in ('utf-8-sig', 'utf-16' if data.startswith((b'\xff\xfe', b'\xfe\xff')) else 'utf-8'):
        try:
            return data.decode(codec), codec
        except UnicodeError:
            pass
    raise SourceError('encoding', 'Choose this file\'s text encoding, or export it as UTF-8 CSV.')


def header_index(rows, selected=None):
    if selected is not None:
        if not isinstance(selected, int) or isinstance(selected, bool) or not 1 <= selected <= 100:
            raise SourceError('header', 'Choose the row containing the column names.')
        return selected - 1
    for index, values in enumerate(rows[:30]):
        words = {clean(v).casefold() for v in values if v is not None}
        if len(words & HEADER_WORDS) >= 2:
            return index
    return next((i for i, row in enumerate(rows[:30]) if any(clean(v) for v in row)), 0)


def rows_to_table(rows, selected_header=None):
    if not rows:
        return [], [], 1
    index = header_index(rows, selected_header)
    if index >= len(rows):
        raise SourceError('header', 'The selected header row is outside this table.')
    headers = [clean(v) for v in rows[index]]
    # Allow unused trailing columns, but never silently rename competing fields.
    while headers and not headers[-1]:
        headers.pop()
    if not headers or any(not h for h in headers) or len(set(headers)) != len(headers):
        raise SourceError('header', 'Some column names are missing or repeated. Choose the correct header row.')
    output = []
    for row_number, values in enumerate(rows[index + 1:], index + 2):
        if not any(v is not None and str(v).strip() for v in values):
            continue
        if len(values) > len(headers) and any(v is not None and str(v).strip() for v in values[len(headers):]):
            raise SourceError('columns', f'Row {row_number} has more values than column names. Check the separator or header.')
        row = dict(zip(headers, values))
        row['__pace_location'] = f'row {row_number}'
        output.append(row)
        if len(output) > MAX_INPUT_ROWS:
            raise SourceError('row_limit', 'This table has too many rows. Export a shorter date range.')
    return headers, output, index + 1


def flatten(value, prefix=''):
    output = {}
    for key, item in value.items():
        name = f'{prefix}.{key}' if prefix else str(key)
        if isinstance(item, dict):
            output.update(flatten(item, name))
        elif isinstance(item, list):
            output[name] = json.dumps(item, default=json_default, ensure_ascii=False)
        else:
            output[name] = item
    return output


def sqlite_tables(path, selected=None):
    # immutable+read-only prevents writes/journals; select-only SQL is authored here.
    connection = sqlite3.connect(path.resolve().as_uri() + '?mode=ro&immutable=1', uri=True)
    connection.set_progress_handler(lambda: 1 if budget[0] > 5_000_000 else count(), 1000)
    budget = [0]

    def count():
        budget[0] += 1000
        return 0

    def quoted(value):
        return '"' + value.replace('"', '""') + '"'

    try:
        names = [r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
        if len(names) > 100:
            raise SourceError('table_limit', 'This database has too many tables. Use its app\'s transaction export.')
        if selected is not None:
            if selected not in names:
                raise SourceError('table', 'That table was not found in the database.')
            names = [selected]
        output = []
        for name in names:
            cursor = connection.execute('SELECT * FROM ' + quoted(name) + f' LIMIT {MAX_INPUT_ROWS + 1}')
            headers = [column[0] for column in cursor.description]
            rows = []
            for index, values in enumerate(cursor, 1):
                if index > MAX_INPUT_ROWS:
                    raise SourceError('row_limit', 'This table has too many rows. Export a shorter date range.')
                if any(isinstance(v, bytes) for v in values):
                    raise SourceError('binary_table', 'This table contains binary data. Choose a transaction table or export CSV.')
                rows.append({**dict(zip(headers, values)), '__pace_location': f'{name} / row {index}'})
            output.append((name, headers, rows, {}))
        return output
    except sqlite3.DatabaseError:
        raise SourceError('database', 'This database cannot be read safely. Use its app\'s transaction export.') from None
    finally:
        connection.close()


def ofx_rows(text):
    """Read common OFX XML/SGML statements; credits need explicit classification."""
    rows = []
    for index, block in enumerate(re.findall(r'<STMTTRN\b[^>]*>(.*?)</STMTTRN>', text, re.I | re.S), 1):
        def tag(name):
            match = re.search(r'<' + name + r'\b[^>]*>\s*([^<\r\n]+)', block, re.I)
            return match.group(1).strip() if match else ''
        raw_date = tag('DTPOSTED')
        # OFX dates can carry local offsets. Preserve the raw value for review;
        # calendar-day adapters do not invent an instant from missing offsets.
        when = f'{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:8]}' if re.match(r'^\d{8}', raw_date) else raw_date
        rows.append({'id': tag('FITID'), 'date': when, 'raw_date': raw_date,
                     'amount': tag('TRNAMT'), 'type': tag('TRNTYPE'),
                     'note': ' '.join(v for v in (tag('NAME'), tag('MEMO')) if v),
                     '__pace_location': f'transaction {index}'})
        if len(rows) > MAX_INPUT_ROWS:
            raise SourceError('row_limit', 'This statement has too many records.')
    if not rows:
        raise SourceError('ofx', 'No transaction table was found in this statement.')
    currency = re.search(r'<CURDEF>\s*([A-Z]{3})', text, re.I)
    # Multiple account sections must be inspected explicitly, not blended.
    if len(re.findall(r'<(?:BANKTRANLIST|INVTRANLIST|CCSTMTRS)\b', text, re.I)) > 1:
        raise SourceError('multiple_accounts', 'Export each account separately so expenses keep the right identity.')
    return [('transactions', list(rows[0])[:-1], rows, {'currency': currency.group(1).upper() if currency else None,
                                                    'signedOutflows': True, 'creditsNeedChoice': True})]


def qif_rows(text):
    rows, row, account = [], {}, 'transactions'
    for line in text.splitlines():
        if line.startswith('!Type:'):
            if rows:
                raise SourceError('multiple_accounts', 'Export each QIF account separately.')
            account = line[6:]
        elif line == '^':
            if row:
                row['__pace_location'] = f'transaction {len(rows) + 1}'
                rows.append(row)
            row = {}
        elif line:
            field = {'D': 'date', 'T': 'amount', 'P': 'payee', 'M': 'note', 'L': 'category', 'N': 'number'}.get(line[0])
            if field:
                row[field] = line[1:]
            if line[0] in {'S', '$', 'E'}:
                row['has_splits'] = 'yes'
        if len(rows) > MAX_INPUT_ROWS:
            raise SourceError('row_limit', 'This statement has too many records.')
    if row or not rows:
        raise SourceError('qif', 'The QIF transactions are incomplete or unreadable.')
    headers = sorted(set().union(*(r.keys() for r in rows)) - {'__pace_location'})
    return [(account, headers, rows, {'signedOutflows': True, 'creditsNeedChoice': True, 'splitRowsNeedChoice': True})]


def read_tables(path, profile=None):
    profile = profile or {}
    path = checked_path(path)
    extension = path.suffix.casefold()
    if path.read_bytes()[:16] == b'SQLite format 3\x00':
        return sqlite_tables(path, profile.get('table'))
    if extension in {'.csv', '.tsv', '.txt'}:
        text, encoding = read_text(path, profile.get('encoding'))
        delimiter = profile.get('delimiter')
        if delimiter is None:
            try:
                delimiter = csv.Sniffer().sniff(text[:65536], delimiters=',;\t|').delimiter
            except csv.Error:
                # Export titles/preambles often defeat Sniffer. Recognized
                # header fields establish a separator without guessing amounts.
                candidates = []
                for separator in (',', ';', '\t', '|'):
                    preview = list(csv.reader(io.StringIO(text[:65536]), delimiter=separator))[:30]
                    score = max((len({clean(v).casefold() for v in row} & HEADER_WORDS) for row in preview), default=0)
                    candidates.append((score, separator))
                best = max(score for score, _ in candidates)
                winners = [separator for score, separator in candidates if score == best]
                delimiter = winners[0] if best >= 2 and len(winners) == 1 else '\t' if extension == '.tsv' else ','
        if delimiter not in {',', ';', '\t', '|'}:
            raise SourceError('separator', 'Choose a supported column separator.')
        try:
            values = bounded_rows(csv.reader(io.StringIO(text), delimiter=delimiter, strict=True))
        except csv.Error:
            raise SourceError('csv', 'The CSV quoting is broken. Export a fresh copy.') from None
        headers, rows, header = rows_to_table(values, profile.get('headerRow'))
        return [('table', headers, rows, {'encoding': encoding, 'delimiter': delimiter, 'headerRow': header})]
    if extension in {'.json', '.jsonl', '.ndjson'}:
        text, _ = read_text(path)
        try:
            if extension in {'.jsonl', '.ndjson'}:
                value = bounded_rows(json.loads(line, parse_float=Decimal) for line in text.splitlines() if line.strip())
            else:
                value = json.loads(text, parse_float=Decimal)
        except (ValueError, RecursionError):
            raise SourceError('json', 'This JSON file is broken or too deeply nested.') from None
        tables = {'records': value} if isinstance(value, list) else {k: v for k, v in value.items() if isinstance(v, list)} if isinstance(value, dict) else {}
        if profile.get('table'):
            tables = {k: v for k, v in tables.items() if k == profile['table']}
        output = []
        for name, values in tables.items():
            if len(values) > MAX_INPUT_ROWS:
                raise SourceError('row_limit', 'This JSON table has too many records.')
            if not all(isinstance(v, dict) for v in values):
                continue
            rows = [{**flatten(v), '__pace_location': f'{name} / row {i}'} for i, v in enumerate(values, 1)]
            headers = sorted(set().union(*(r.keys() for r in rows)) - {'__pace_location'}) if rows else []
            output.append((name, headers, rows, {}))
        if not output:
            raise SourceError('json_table', 'No record table was found. Choose the transaction array or export CSV.')
        return output
    if extension == '.xlsx':
        validate_workbook(path)
        try:
            from openpyxl import load_workbook
        except ImportError:
            raise SourceError('xlsx_runtime', 'Spreadsheet reading is unavailable here. Export the sheet as CSV.') from None
        workbook = load_workbook(path, read_only=True, data_only=True)
        output = []
        try:
            names = [profile['sheet']] if profile.get('sheet') else workbook.sheetnames
            if len(names) > 100:
                raise SourceError('sheet_limit', 'This workbook has too many sheets. Export the expense sheet separately.')
            for name in names:
                if name not in workbook.sheetnames:
                    raise SourceError('sheet', 'That sheet was not found in this workbook.')
                values = bounded_rows(list(row) for row in workbook[name].iter_rows(values_only=True))
                try:
                    headers, rows, header = rows_to_table(values, profile.get('headerRow'))
                    output.append((name, headers, rows, {'headerRow': header}))
                except SourceError as error:
                    # Keep matrices visible with source cells, not guessed headers.
                    output.append((name, [], [], {'layoutQuestion': str(error), 'cellRows': len(values),
                                                 'sampleCells': values[:15]}))
            return output
        finally:
            workbook.close()
    if extension in {'.ofx', '.qfx'}:
        return ofx_rows(read_text(path, profile.get('encoding'))[0])
    if extension == '.qif':
        return qif_rows(read_text(path, profile.get('encoding'))[0])
    if extension == '.realm':
        raise SourceError('realm_runtime', 'Use the tested Realm reader if its compatibility runtime is available; otherwise export transactions from the old app.')
    if extension == '.pdf':
        raise SourceError('document_recovery', 'Read each page in the file workspace and prepare source-linked expense rows for review. A PDF is not yet a transaction table.')
    raise SourceError('unsupported_file', 'This format is not readable yet. Export transactions as CSV or XLSX from the original app.')


def stage_inputs(paths, workdir):
    """Expand selected folder ZIPs safely, preserving locations. Never extractall."""
    workdir = Path(workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    total_input = sum(checked_path(p).stat().st_size for p in paths)
    if len(paths) > 100 or total_input > MAX_FILE:
        raise SourceError('intake_limit', 'Choose fewer files or a shorter date range (100 MiB maximum).')
    files, ignored, expanded = [], [], 0
    for path in map(Path, paths):
        if path.suffix.casefold() != '.zip':
            files.append({'path': str(path.resolve()), 'name': path.name})
            continue
        with zipfile.ZipFile(path) as archive:
            members = archive.infolist()
            if len(members) > MAX_MEMBERS:
                raise SourceError('zip_limit', 'This ZIP contains too many files.')
            for member in members:
                name = member.filename.replace('\\', '/')
                parts = PurePosixPath(name).parts
                if name.startswith('/') or '..' in parts or re.match(r'^[A-Za-z]:', name):
                    raise SourceError('zip_path', 'This ZIP contains unsafe file paths. Export a fresh copy.')
                if member.flag_bits & 1 or stat.S_ISLNK(member.external_attr >> 16):
                    raise SourceError('zip_encrypted', 'Choose an unlocked ZIP containing ordinary files.')
                expanded += member.file_size
                if expanded > MAX_EXPANDED or member.file_size > MAX_FILE:
                    raise SourceError('zip_limit', 'This ZIP expands to too much data. Export a smaller date range.')
            # Recognized Pace ZIPs should go to Pace unchanged, not be treated
            # as raw tables and lose their source identity or backup semantics.
            manifests = [m for m in members if PurePosixPath(m.filename).name == 'manifest.json' and '__MACOSX' not in PurePosixPath(m.filename).parts]
            if len(manifests) == 1 and manifests[0].file_size <= 200_000:
                try:
                    manifest = json.loads(archive.read(manifests[0]))
                    if manifest.get('schema') in {'PaceCSVArchive', 'PaceExpenseTransfer'}:
                        files.append({'path': str(path.resolve()), 'name': path.name, 'paceArchive': manifest.get('contents', 'backup' if manifest['schema'] == 'PaceCSVArchive' else 'expenses')})
                        continue
                except (ValueError, AttributeError):
                    pass
            folder = workdir / digest(path.read_bytes())[:24]
            folder.mkdir(exist_ok=True)
            seen = set()
            for member in members:
                name = member.filename.replace('\\', '/')
                parts = PurePosixPath(name).parts
                if member.is_dir() or any(p.startswith('.') or p == '__MACOSX' for p in parts) or PurePosixPath(name).name in {'Thumbs.db', 'desktop.ini'}:
                    ignored.append({'file': f'{path.name}/{name}', 'reason': 'Folder or system metadata'})
                    continue
                if name.casefold() in seen:
                    raise SourceError('zip_duplicate', 'This ZIP contains competing copies with the same name.')
                seen.add(name.casefold())
                target = folder.joinpath(*parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.is_symlink():
                    raise SourceError('zip_path', 'The extraction folder contains a symbolic link.')
                target.write_bytes(archive.read(member))
                files.append({'path': str(target.resolve()), 'name': f'{path.name}/{name}'})
    return files, ignored


def inspect_files(paths, workdir):
    files, ignored = stage_inputs(paths, workdir)
    findings = []
    for source in files:
        item = {**source, 'sha256': digest(Path(source['path']).read_bytes())}
        if source.get('paceArchive'):
            item['nextStep'] = 'Import this Pace file directly in Pace. Conversion is not needed.'
            findings.append(item)
            continue
        try:
            item['tables'] = []
            for name, headers, rows, facts in read_tables(source['path']):
                category_fields = [h for h in headers if clean(h).casefold() in {'category', 'type', 'kind', 'currency'}]
                counts = {field: {} for field in category_fields}
                for row in rows:
                    for field in category_fields:
                        value = clean(row.get(field))
                        counts[field][value] = counts[field].get(value, 0) + 1
                item['tables'].append({'name': name, 'columns': headers, 'rowCount': len(rows),
                                       'sample': rows[:8], 'groups': counts, **facts})
        except SourceError as error:
            item['issue'] = {'code': error.code, 'message': str(error)}
        except (ValueError, OSError, zipfile.BadZipFile):
            item['issue'] = {'code': 'unreadable_file', 'message': 'This file could not be read. Export a fresh transaction copy.'}
        findings.append(item)
    return {'files': findings, 'ignoredFiles': ignored, 'fileCount': len(files)}
