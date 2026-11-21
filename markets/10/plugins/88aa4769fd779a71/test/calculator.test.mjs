import test from 'node:test';
import assert from 'node:assert/strict';
import { calculate, convertUnit, summary, InputError } from '../src/calculator.mjs';

const args = (mass = '13.7', volume = '2.5') => ({ mass, massUnit: 'mg', volume, volumeUnit: 'mL' });

test('concentration and unit conversion match independent arithmetic', () => {
  const r = calculate(args());
  assert.equal(r.concentration.mgPerMl, '5.48');
  assert.equal(r.concentration.mcgPerMl, '5480');
  assert.equal(r.concentration.rounded, false);
});
test('decimal fractions do not inherit binary float errors', () => {
  assert.equal(calculate(args('0.1', '0.2')).concentration.mgPerMl, '0.5');
});
test('equivalent mass and volume units produce identical concentration', () => {
  const first = calculate(args()).concentration;
  const second = calculate({ mass: '13700', massUnit: 'mcg', volume: '2500', volumeUnit: 'uL' }).concentration;
  assert.deepEqual(first, second);
});
test('switching units preserves the physical quantity and is reversible', () => {
  assert.equal(convertUnit('13.7', 'mg', 'mcg', 'mass'), '13700');
  assert.equal(convertUnit('13700', 'mcg', 'mg', 'mass'), '13.7');
  assert.equal(convertUnit('2.5', 'mL', 'uL', 'volume'), '2500');
  assert.equal(convertUnit('2500', 'uL', 'mL', 'volume'), '2.5');
});
test('a repeating decimal is explicitly marked approximate', () => {
  const r = calculate(args('1', '3'));
  assert.equal(r.concentration.mgPerMl, '0.333333333333');
  assert.equal(r.concentration.mcgPerMl, '333.333333333');
  assert.equal(r.concentration.rounded, true);
  assert.match(summary(r), /Approximately/);
});
test('very small results never round to zero', () => {
  const r = calculate(args('0.000000001', '1000000000'));
  assert.equal(r.concentration.mgPerMl, '0.000000000000000001');
  assert.equal(r.concentration.mcgPerMl, '0.000000000000001');
});
test('large ratios retain exact plain decimal output', () => {
  const r = calculate(args('1000000000', '0.000000001'));
  assert.equal(r.concentration.mgPerMl, '1000000000000000000');
  assert.equal(r.concentration.mcgPerMl, '1000000000000000000000');
});
test('leading zeros, whitespace and leading decimal points are normalized', () => {
  const r = calculate(args(' 001.20 ', '.4'));
  assert.equal(r.input.mass, '1.2');
  assert.equal(r.concentration.mgPerMl, '3');
});
for (const invalid of ['', ' ', '0', '-1', 'NaN', 'Infinity', '1e3', '1,5', '1,000', '1 mg', '0x10', '1.2.3', '2/3', '<script>']) {
  test(`rejects invalid numeric input ${JSON.stringify(invalid)}`, () => {
    assert.throws(() => calculate(args(invalid)), InputError);
    assert.throws(() => calculate(args('1', invalid)), InputError);
  });
}
test('rejects numbers as implicit inputs, unsupported units, and extra fields', () => {
  assert.throws(() => calculate({ ...args(), mass: 2 }), InputError);
  assert.throws(() => calculate({ ...args(), massUnit: 'g' }), InputError);
  assert.throws(() => calculate({ ...args(), volumeUnit: 'units' }), InputError);
  assert.throws(() => calculate({ ...args(), dose: '1' }), InputError);
});
test('limits apply after unit normalization and are labeled software limits', () => {
  assert.throws(() => calculate(args('0.0000000001')), /software limit/);
  assert.throws(() => calculate(args('1000000001')), /software limit/);
  assert.equal(calculate({ ...args(), mass: '0.000001', massUnit: 'mcg' }).normalized.massMg, '0.000000001');
});
test('scaled inputs preserve concentration across 100 independent examples', () => {
  for (let i = 1; i <= 100; i++) {
    const r = calculate(args(String(i * 7), '7'));
    assert.equal(r.concentration.mgPerMl, String(i));
    assert.equal(r.concentration.mcgPerMl, String(i * 1000));
    const scaled = calculate(args(String(i * 49), '49'));
    assert.deepEqual(r.concentration, scaled.concentration);
  }
});
test('copied result includes both inputs, units, formula and assumptions', () => {
  const text = summary(calculate(args()));
  assert.match(text, /final solution volume 2.5 mL/);
  assert.match(text, /13.7 mg \/ 2.5 mL = 5.48 mg\/mL/);
  assert.match(text, /fully dissolved/);
  assert.match(text, /Not dosing or preparation advice/);
});
test('long precise decimals survive unit conversion without rejection or rounding', () => {
  const original = '1.12345678901234567890123456789012345678';
  const mg = convertUnit(original, 'mcg', 'mg', 'mass');
  assert.equal(convertUnit(mg, 'mg', 'mcg', 'mass'), original);
  const a = calculate({ ...args(), mass: original, massUnit: 'mcg' });
  const b = calculate({ ...args(), mass: mg, massUnit: 'mg' });
  assert.deepEqual(a.concentration, b.concentration);
});
test('conversion rejects out-of-range or excessive precision inputs without changing quantity', () => {
  assert.throws(() => convertUnit('0.0000000000001', 'mg', 'mcg', 'mass'), /software limit/);
  assert.throws(() => calculate(args('1.12345678901234567890123456789012345678901')), /40 significant digits/);
});
