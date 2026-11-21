"""Local financial scenarios only; standard library, no network or persistence.

Read a minimal JSON scenario from stdin. Percentages are explicit assumptions.
The full-relief model matches the Arclight website's exact rational equations.
"""
from fractions import Fraction
import json
import re
import sys


class InputError(ValueError):
    pass


RULES = {
    'principal': (1, 100000000, 2),
    'rate_percent': (0, 100, 4),
    'months': (0, 1200, 2),
    'fee': (0, 100000000, 2),
    'probability_percent': (0, 100, 4),
}


def number(value, field):
    if isinstance(value, bool) or not isinstance(value, (str, int, float)):
        raise InputError(f'{field}: use a finite plain decimal number')
    text = str(value).strip()
    if len(text) > 40 or not re.fullmatch(r'(?:\d+(?:\.\d*)?|\.\d+)', text):
        raise InputError(f'{field}: use a nonnegative plain decimal number')
    lo, hi, places = RULES[field]
    if '.' in text and len(text.split('.')[1]) > places:
        raise InputError(f'{field}: too many decimal places')
    result = Fraction(text)
    if not lo <= result <= hi:
        raise InputError(f'{field}: outside allowed range')
    return result


def fixed(value, places=2):
    value = Fraction(value)
    scaled = abs(value.numerator) * 10 ** places
    q, r = divmod(scaled, value.denominator)
    if r * 2 >= value.denominator:
        q += 1
    sign = '-' if value < 0 and q else ''
    if not places:
        return sign + str(q)
    digits = str(q).zfill(places + 1)
    return sign + digits[:-places] + '.' + digits[-places:]


def pct(value):
    return fixed(value * 100, 6).rstrip('0').rstrip('.')


def threshold(value):
    status = ('unreachable_above_100_percent' if value > 1 else
              'below_zero_percent' if value < 0 else 'within_0_to_100_percent')
    return {'percent': pct(value), 'status': status,
            'meaning': 'Equality at this assumed full-relief probability; higher gives lower expected cost.'}


def calculate(data):
    allowed = set(RULES) | {'alternative', 'sensitivity_percent'}
    if not isinstance(data, dict) or set(data) - allowed:
        raise InputError('Use only the documented financial scenario fields')
    if not {'principal', 'rate_percent', 'months', 'fee'} <= set(data):
        raise InputError('principal, rate_percent, months and fee are required')
    v = {key: number(data[key], key) for key in ('principal', 'rate_percent', 'months', 'fee')}
    p = None if data.get('probability_percent') is None else number(data['probability_percent'], 'probability_percent') / 100
    raw_sensitivity = data.get('sensitivity_percent', ['10', '25', '50', '80', '90'])
    if not isinstance(raw_sensitivity, list) or not 1 <= len(raw_sensitivity) <= 25:
        raise InputError('sensitivity_percent must contain 1 to 25 percentages')
    probabilities = [number(x, 'probability_percent') / 100 for x in raw_sensitivity]
    alt = data.get('alternative')
    if 'alternative' in data and (not isinstance(alt, dict) or set(alt) != {'fee', 'probability_percent'}):
        raise InputError('alternative requires only fee and probability_percent')
    a = None if alt is None else {'fee': number(alt['fee'], 'fee'),
                                  'probability': number(alt['probability_percent'], 'probability_percent') / 100}
    principal, fee = v['principal'], v['fee']
    interest = principal * v['rate_percent'] / 100 * v['months'] / 12
    balance = principal + interest
    alt_cost = None if a is None else a['fee'] + (1 - a['probability']) * balance

    def row(probability):
        cost = fee + (1 - probability) * balance
        ceiling = principal - (1 - probability) * balance
        result = {'assumed_full_relief_percent': pct(probability), 'expected_cost': fixed(cost),
                  'savings_vs_repay_now': fixed(principal - cost), 'fee_ceiling_vs_repay_now': fixed(ceiling)}
        if a is not None:
            other_ceiling = a['fee'] + (probability - a['probability']) * balance
            result.update(advantage_vs_alternative=fixed(alt_cost - cost),
                          fee_ceiling_vs_alternative=fixed(other_ceiling),
                          relevant_fee_ceiling=fixed(min(ceiling, other_ceiling)))
        else:
            result['relevant_fee_ceiling'] = fixed(ceiling)
        return result

    output = {
        'model': 'Simple interest; full relief or full loss; fixed fee paid in either outcome.',
        'probabilities': 'Explicit assumptions or hypothetical sensitivity; actual case odds are not estimated.',
        'inputs': {key: fixed(value, RULES[key][2]) for key, value in v.items()},
        'interest': fixed(interest), 'projected_balance': fixed(balance),
        'repay_now_cost': fixed(principal), 'full_win_cost': fixed(fee), 'full_loss_cost': fixed(fee + balance),
        'break_even_probability_vs_repay_now': threshold(1 - (principal - fee) / balance),
        'selected_scenario': None if p is None else row(p),
        'sensitivity': [row(x) for x in probabilities],
        'fee_ceiling_meaning': 'Mathematical equality under assumptions; not a recommended fee or market valuation.',
    }
    if a is not None:
        output['alternative'] = {'fee': fixed(a['fee']), 'assumed_full_relief_percent': pct(a['probability']),
                                 'expected_cost': fixed(alt_cost), 'full_win_cost': fixed(a['fee']),
                                 'full_loss_cost': fixed(a['fee'] + balance)}
        output['break_even_probability_vs_alternative'] = threshold(a['probability'] + (fee - a['fee']) / balance)
    return output


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError('Duplicate JSON fields are not allowed')
        result[key] = value
    return result


def main():
    if len(sys.argv) != 1:
        print('Usage: python appeal_calculator.py < scenario.json', file=sys.stderr)
        return 2
    try:
        raw = sys.stdin.read(8193)
        if len(raw) > 8192:
            raise InputError('Scenario input exceeds 8192 characters')
        data = json.loads(raw, parse_float=str, parse_int=str,
                          parse_constant=lambda _: (_ for _ in ()).throw(InputError('Nonfinite JSON number')),
                          object_pairs_hook=unique_object)
        print(json.dumps(calculate(data), indent=2))
        return 0
    except (InputError, json.JSONDecodeError, RecursionError):
        # Do not echo input values or unknown keys, which could contain identifiers.
        print('Invalid financial scenario. Use the documented schema and numeric limits.', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
