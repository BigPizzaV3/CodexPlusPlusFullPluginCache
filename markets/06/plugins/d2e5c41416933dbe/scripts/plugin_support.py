"""Copied into each standalone plugin; no repository runtime dependency."""
import argparse
from decimal import Decimal, InvalidOperation
import json
import os
from pathlib import Path
import tempfile


def obj(value, field='input'):
    if not isinstance(value, dict):
        raise ValueError(f'{field} must be an object')
    return value


def text(value, field='value'):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{field} must be a nonempty string')
    return value


def records(value, field, id_key='id', limit=10000):
    if not isinstance(value, list) or len(value) > limit:
        raise ValueError(f'{field} must be a list of at most {limit} objects')
    found = set()
    for row in value:
        obj(row, field)
        if id_key is not None:
            key = text(row.get(id_key), f'{field}.{id_key}')
            if key in found:
                raise ValueError(f'Duplicate {field}.{id_key}: {key}')
            found.add(key)
    return value


def amount(value, field='amount', nonnegative=True):
    if type(value) not in (str, int):
        raise ValueError(f'{field} must be a decimal string or integer')
    try:
        result = Decimal(value)
    except InvalidOperation:
        raise ValueError(f'Invalid {field}') from None
    if not result.is_finite() or (nonnegative and result < 0):
        raise ValueError(f'{field} must be finite' + (' and nonnegative' if nonnegative else ''))
    if len(result.as_tuple().digits) > 24 or abs(result.as_tuple().exponent) > 12 or result.adjusted() > 18:
        raise ValueError(f'{field} exceeds supported precision (24 digits, scale/exponent 12, 19 integer digits)')
    return result


def validate_json(value):
    try:
        json.dumps(value, allow_nan=False)
    except (TypeError, ValueError, RecursionError) as exc:
        raise ValueError('Input must contain finite JSON values') from exc


def main(run):
    parser = argparse.ArgumentParser(description='Aivana GmbH local plugin | https://www.aivana-gmbh.ai')
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.input.resolve() == args.output.resolve() or (args.output.exists() and args.input.samefile(args.output)):
            raise ValueError('Input and output must be different files')
        with args.input.open('rb') as handle:
            raw = handle.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            raise ValueError('Input exceeds 8 MiB')
        data = json.loads(raw.decode('utf-8-sig'))
        obj(data)
        validate_json(data)
        result = run(data)
        payload = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
        args.output.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=args.output.parent, delete=False) as handle:
                temporary = Path(handle.name)
                handle.write(payload)
            os.replace(temporary, args.output)
        finally:
            if temporary and temporary.exists():
                temporary.unlink()
        return 0
    except (ValueError, TypeError, KeyError, OSError, RecursionError) as exc:
        parser.exit(2, f'Error: {exc}\n')
