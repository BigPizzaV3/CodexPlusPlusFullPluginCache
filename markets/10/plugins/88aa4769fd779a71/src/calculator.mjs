import Decimal from 'decimal.js';

const D = Decimal.clone({ precision: 60, rounding: Decimal.ROUND_HALF_UP });
export const NOTICE = 'Educational concentration arithmetic only. Not dosing or preparation advice.';
export const ASSUMPTION = 'Uses the final total solution volume and assumes the entered mass is fully dissolved. This does not verify purity, stability, solubility, or suitability for use.';
export const SIGNIFICANT_DIGITS = 12;
export const INPUT_MAX_LENGTH = 96;
const units = { mass: { mg: '1', mcg: '0.001' }, volume: { mL: '1', uL: '0.001' } };
const labels = { mass: 'Peptide mass', volume: 'Final solution volume' };

export class InputError extends Error {
  constructor(field, message) { super(message); this.name = 'InputError'; this.field = field; }
}

function parse(value, field) {
  if (typeof value !== 'string' || value.length > INPUT_MAX_LENGTH || !/^(?:\d+(?:\.\d+)?|\.\d+)$/.test(value.trim())) {
    throw new InputError(field, `${labels[field]} must be a number using a decimal point, without commas, units, or scientific notation.`);
  }
  const number = new D(value.trim());
  if (number.sd() > 40) throw new InputError(field, `${labels[field]} supports up to 40 significant digits.`);
  if (!number.isPositive() || number.isZero()) throw new InputError(field, `${labels[field]} must be greater than zero.`);
  return number;
}

function normalize(value, unit, kind) {
  if (!Object.hasOwn(units[kind], unit)) throw new InputError(kind, `Choose a supported ${kind} unit.`);
  const number = parse(value, kind).times(units[kind][unit]);
  if (number.lt('0.000000001') || number.gt('1000000000')) {
    throw new InputError(kind, `${labels[kind]} is outside this calculator's numeric range (0.000000001 to 1000000000 ${kind === 'mass' ? 'mg' : 'mL'}). This is a software limit, not a recommended range.`);
  }
  return number;
}

export function convertUnit(value, from, to, kind) {
  if (!Object.hasOwn(units, kind) || !Object.hasOwn(units[kind], from) || !Object.hasOwn(units[kind], to)) {
    throw new InputError(kind, 'Choose supported units.');
  }
  return normalize(value, from, kind).div(units[kind][to]).toFixed();
}

export function calculate(input) {
  if (!input || typeof input !== 'object' || Array.isArray(input)) throw new InputError('mass', 'Enter a mass and final solution volume.');
  const allowed = new Set(['mass', 'massUnit', 'volume', 'volumeUnit']);
  if (Object.keys(input).some(key => !allowed.has(key))) throw new InputError('mass', 'This calculator accepts only mass, final solution volume, and their units.');
  const massMg = normalize(input.mass, input.massUnit, 'mass');
  const volumeMl = normalize(input.volume, input.volumeUnit, 'volume');
  const mg = massMg.div(volumeMl).toSignificantDigits(SIGNIFICANT_DIGITS);
  const mcg = massMg.times(1000).div(volumeMl).toSignificantDigits(SIGNIFICANT_DIGITS);
  const rounded = !mg.times(volumeMl).eq(massMg) || !mcg.times(volumeMl).eq(massMg.times(1000));
  return {
    input: { mass: new D(input.mass.trim()).toFixed(), massUnit: input.massUnit, volume: new D(input.volume.trim()).toFixed(), volumeUnit: input.volumeUnit },
    normalized: { massMg: massMg.toFixed(), volumeMl: volumeMl.toFixed() },
    concentration: { mgPerMl: mg.toFixed(), mcgPerMl: mcg.toFixed(), rounded, significantDigits: SIGNIFICANT_DIGITS },
    formula: `${massMg.toFixed()} mg / ${volumeMl.toFixed()} mL ${rounded ? 'approximately equals' : '='} ${mg.toFixed()} mg/mL`,
    assumption: ASSUMPTION,
    notice: NOTICE
  };
}

export function summary(result) {
  return [
    'Peptide Reconstitution Calculator by Peptara Labs',
    `Input: ${result.input.mass} ${result.input.massUnit}; final solution volume ${result.input.volume} ${result.input.volumeUnit}.`,
    `${result.concentration.rounded ? 'Approximately ' : ''}${result.concentration.mgPerMl} mg/mL (${result.concentration.mcgPerMl} mcg/mL).`,
    `Formula: ${result.formula}.`,
    result.concentration.rounded ? `Rounded to ${SIGNIFICANT_DIGITS} significant digits.` : 'No display rounding was needed.',
    ASSUMPTION,
    NOTICE
  ].join('\n');
}
