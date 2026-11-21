#!/usr/bin/env python3
"""Compute a planning budget. Read one JSON file, print JSON, no network/writes."""
import json
import re
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


def number(value, name, maximum=Decimal('1000000000000')):
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ValueError(name + ' must be a finite nonnegative number')
    try:
        result = Decimal(str(value))
    except InvalidOperation:
        raise ValueError(name + ' must be a finite nonnegative number') from None
    if not result.is_finite() or result < 0 or result > maximum:
        raise ValueError(name + ' must be finite and between 0 and ' + str(maximum))
    return result


def currency(value):
    if not isinstance(value, str) or not re.fullmatch('[A-Z]{3}', value):
        raise ValueError('currency must be a three-letter uppercase code')
    return value


def amount(value):
    return format(value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), '.2f')


def calculate(data):
    if not isinstance(data, dict):
        raise ValueError('input must be an object')
    allowed = {'nights', 'base_currency', 'rates', 'items', 'contingency_percent', 'reserve', 'target'}
    if set(data) - allowed:
        raise ValueError('unknown budget input fields: ' + ', '.join(sorted(set(data) - allowed)))
    nights = data.get('nights')
    if isinstance(nights, bool) or not isinstance(nights, int) or not 1 <= nights <= 3660:
        raise ValueError('nights must be an integer from 1 to 3660')
    base = currency(data.get('base_currency'))
    supplied = data.get('rates', {})
    if not isinstance(supplied, dict):
        raise ValueError('rates must be an object')
    rates = {base: Decimal(1)}
    for code, value in supplied.items():
        currency(code)
        rate = number(value, 'rate', Decimal('1000000'))
        if rate <= 0 or (code == base and rate != 1):
            raise ValueError('rates must be positive; base currency rate must equal 1')
        rates[code] = rate
    items = data.get('items')
    if not isinstance(items, list) or not 1 <= len(items) <= 200:
        raise ValueError('items must contain 1 to 200 entries')
    totals = {kind: Decimal(0) for kind in ('recurring', 'one_time', 'deposit')}
    lines = []
    monthly = False
    for item in items:
        if not isinstance(item, dict) or set(item) != {'label', 'amount', 'currency', 'basis', 'kind'}:
            raise ValueError('each item needs exactly label, amount, currency, basis, kind')
        label = item['label']
        if not isinstance(label, str) or not label.strip() or len(label) > 160:
            raise ValueError('item label must contain 1 to 160 characters')
        code = currency(item['currency'])
        if code not in rates:
            raise ValueError('missing explicit exchange rate for ' + code)
        basis, kind = item['basis'], item['kind']
        if not isinstance(basis, str) or not isinstance(kind, str) or basis not in ('night', 'month', 'stay') or kind not in totals:
            raise ValueError('invalid item basis or kind')
        if kind in ('deposit', 'one_time') and basis != 'stay':
            raise ValueError('deposit and one_time items must use stay basis')
        monthly = monthly or basis == 'month'
        multiplier = Decimal(nights) if basis == 'night' else Decimal(nights) / 30 if basis == 'month' else Decimal(1)
        converted = number(item['amount'], 'item amount') * rates[code] * multiplier
        totals[kind] += converted
        lines.append({'label': label, 'kind': kind, 'basis': basis, 'base_amount': amount(converted)})
    spending = totals['recurring'] + totals['one_time']
    percent = number(data.get('contingency_percent', 0), 'contingency_percent', Decimal(100))
    contingency = spending * percent / 100
    reserve = number(data.get('reserve', 0), 'reserve')
    cash = spending + contingency + totals['deposit'] + reserve
    result = {
        'base_currency': base, 'nights': nights, 'items': lines,
        'recurring_spending': amount(totals['recurring']), 'one_time_spending': amount(totals['one_time']),
        'trip_spending': amount(spending), 'spending_per_night': amount(spending / nights),
        'contingency_percent': str(percent), 'contingency': amount(contingency),
        'refundable_deposits': amount(totals['deposit']), 'emergency_reserve': amount(reserve),
        'total_cash_needed': amount(cash),
        'rates_base_units_per_foreign_unit': {key: str(value) for key, value in rates.items()},
        'notes': ['Totals use unrounded amounts; displayed lines use two decimal places.',
                  'Two decimals are a display convention, not currency settlement precision.',
                  'Missing costs are not included; estimated inputs produce estimated totals.']}
    if monthly:
        result['notes'].append('Monthly amounts use nights / 30 as an estimate; actual billing may differ.')
    if 'target' in data:
        result['target'] = amount(number(data['target'], 'target'))
        result['cash_headroom'] = amount(number(data['target'], 'target') - cash)
    return result


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError('usage: budget.py INPUT.json')
        path = Path(sys.argv[1])
        if path.stat().st_size > 1000000:
            raise ValueError('input exceeds 1 MB')
        result = calculate(json.loads(path.read_text(encoding='utf-8')))
        print(json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, OSError, InvalidOperation) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
