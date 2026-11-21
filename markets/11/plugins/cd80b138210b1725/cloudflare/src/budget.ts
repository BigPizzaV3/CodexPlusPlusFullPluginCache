import { z } from 'zod';

export const MAX_TOKENS = 1_000_000_000_000;
export const fields = ['reference_limit_tokens', 'used_tokens', 'planned_increase_tokens',
  'reserved_output_tokens', 'recent_turn_tokens'] as const;
export const bases = ['user_provided', 'assumed', 'supplied_measurement'] as const;
const count = (minimum = 0) => z.number().int().min(minimum).max(MAX_TOKENS).nullable().optional();
export const inputSchema = z.object({
  reference_limit_tokens: count(1).describe('Explicit reference budget; never inferred from a model/platform name.'),
  used_tokens: count().describe('Explicit current usage estimate; not a lifetime total.'),
  planned_increase_tokens: count().describe('Extra context for the next task, excluding the separate output reserve.'),
  reserved_output_tokens: count().describe('Additional output reserve; missing is unknown, not zero.'),
  recent_turn_tokens: z.array(z.number().int().min(0).max(MAX_TOKENS)).max(6).nullable().optional()
    .describe('Up to six chronological turn-end totals. Last must equal supplied used_tokens.'),
  sources: z.object(Object.fromEntries(fields.map(field => [field, z.enum(bases).optional()]))).strict().optional()
    .describe('Fixed provenance enums for supplied fields only; not proof of verified telemetry.'),
}).strict();

export type Input = z.infer<typeof inputSchema>;
type Field = typeof fields[number];
type Basis = typeof bases[number];
type Data = Record<Exclude<Field, 'recent_turn_tokens'>, number | null> & { recent_turn_tokens: number[] | null };
export class BudgetInputError extends Error {
  constructor() { super('Only documented bounded token counts and fixed source enums are accepted. Check numeric bounds and provenance.'); }
}

const nullNumber = z.number().finite().nullable();
const metricsSchema = z.object({ used_tokens: nullNumber, fraction: nullNumber,
  remaining_tokens: nullNumber, over_budget_tokens: nullNumber,
  weather: z.enum(['Unknown', 'Clear', 'Fair', 'Cloudy', 'Showers', 'Storm']) }).strict();
export const outputSchema = z.object({
  schema_version: z.literal(1), basis: z.literal('explicit_numeric_inputs'),
  reference_limit_tokens: z.number().int().nullable(),
  inputs: z.object({ reference_limit_tokens: z.number().int().nullable(), used_tokens: z.number().int().nullable(),
    planned_increase_tokens: z.number().int().nullable(), reserved_output_tokens: z.number().int().nullable(),
    recent_turn_tokens: z.array(z.number().int()).max(6).nullable() }).strict(),
  sources: z.object(Object.fromEntries(fields.map(field => [field, z.enum(bases).nullable()]))).strict(),
  current: metricsSchema,
  plan: z.object({ added_tokens: z.number().int().nullable(), after: metricsSchema, fits_reference: z.boolean().nullable() }).strict(),
  growth: z.object({ tokens_per_turn: nullNumber, intervals: z.number().int().min(0).max(5),
    turns_until_reference: z.number().int().nullable(), forecast: z.array(z.object({
      step: z.number().int().min(1).max(5), budget: metricsSchema }).strict()).max(5) }).strict(),
  unknowns: z.array(z.enum(['reference_limit_tokens', 'used_tokens', 'planned_increase_tokens',
    'reserved_output_tokens', 'growth_insufficient_turns', 'actual_platform_context',
    'actual_compaction_policy', 'account_quota', 'monetary_cost'])),
  notices: z.array(z.literal('recent_decrease_resets_growth')),
  limitations: z.array(z.string()),
}).strict();

export function validate(input: unknown) {
  const parsed = inputSchema.safeParse(input);
  if (!parsed.success) throw new BudgetInputError();
  const original = parsed.data;
  const data = Object.fromEntries(fields.map(field => [field, original[field] ?? null])) as Data;
  const sources: Record<Field, Basis | null> = {} as Record<Field, Basis | null>;
  for (const field of fields) {
    const supplied = original.sources?.[field];
    if (supplied !== undefined && data[field] === null) throw new BudgetInputError();
    sources[field] = data[field] === null ? null : supplied ?? 'user_provided';
  }
  if (data.recent_turn_tokens?.length && data.used_tokens !== null && data.recent_turn_tokens.at(-1) !== data.used_tokens) {
    throw new BudgetInputError();
  }
  return { data, sources };
}

// Integer rational arithmetic keeps forecast/band boundaries consistent with
// the existing Python Fraction calculator. JSON output alone uses numbers.
function metrics(numerator: bigint | null, denominator: bigint, limit: number | null) {
  const result = { used_tokens: numerator === null ? null : Number(numerator) / Number(denominator),
    fraction: null as number | null, remaining_tokens: null as number | null,
    over_budget_tokens: null as number | null, weather: 'Unknown' as z.infer<typeof metricsSchema>['weather'] };
  if (numerator !== null && limit !== null) {
    const bound = BigInt(limit) * denominator;
    result.fraction = Number(numerator) / Number(bound);
    result.remaining_tokens = Number(bound > numerator ? bound - numerator : 0n) / Number(denominator);
    result.over_budget_tokens = Number(numerator > bound ? numerator - bound : 0n) / Number(denominator);
    const rank = [35n, 55n, 70n, 85n].findIndex(cut => numerator * 100n < bound * cut);
    result.weather = (['Clear', 'Fair', 'Cloudy', 'Showers', 'Storm'] as const)[rank === -1 ? 4 : rank];
  }
  return result;
}

export function planContextBudget(input: unknown) {
  const { data, sources } = validate(input);
  const limit = data.reference_limit_tokens, used = data.used_tokens;
  const increase = data.planned_increase_tokens, reserve = data.reserved_output_tokens;
  const added = increase !== null && reserve !== null ? increase + reserve : null;
  const after = used !== null && added !== null ? used + added : null;
  let recent = [...(data.recent_turn_tokens ?? [])];
  let lastDecrease = -1;
  for (let index = 1; index < recent.length; index++) if (recent[index] < recent[index - 1]) lastDecrease = index;
  const notices: Array<'recent_decrease_resets_growth'> = [];
  if (lastDecrease !== -1) { recent = recent.slice(lastDecrease); notices.push('recent_decrease_resets_growth'); }
  const intervals = Math.max(0, recent.length - 1);
  const delta = intervals >= 2 ? BigInt(recent.at(-1)! - recent[0]) : null;
  const denominator = BigInt(intervals || 1);
  let until: number | null = null;
  const forecast: Array<{ step: number; budget: ReturnType<typeof metrics> }> = [];
  if (delta !== null && used !== null && limit !== null) {
    if (used >= limit) until = 0;
    else if (delta > 0n) {
      const distance = BigInt(limit - used) * denominator;
      until = Number((distance + delta - 1n) / delta);
    }
    for (let step = 1; step <= 5; step++) forecast.push({ step,
      budget: metrics(BigInt(used) * denominator + delta * BigInt(step), denominator, limit) });
  }
  const unknowns: string[] = fields.filter(field => field !== 'recent_turn_tokens' && data[field] === null);
  if (delta === null) unknowns.push('growth_insufficient_turns');
  unknowns.push('actual_platform_context', 'actual_compaction_policy', 'account_quota', 'monetary_cost');
  return {
    schema_version: 1, basis: 'explicit_numeric_inputs', reference_limit_tokens: limit,
    inputs: data, sources, current: metrics(used === null ? null : BigInt(used), 1n, limit),
    plan: { added_tokens: added, after: metrics(after === null ? null : BigInt(after), 1n, limit),
      fits_reference: after !== null && limit !== null ? after <= limit : null },
    growth: { tokens_per_turn: delta === null ? null : Number(delta) / Number(denominator), intervals,
      turns_until_reference: until, forecast }, unknowns, notices,
    limitations: [
      'Arithmetic from supplied numbers; no access to current ChatGPT or Codex telemetry.',
      'Weather uses reference-budget cuts at 35%, 55%, 70% and 85%; it is not a platform policy.',
      'Forecast extends the mean change across at least two consecutive intervals after the last decrease; includes zero-growth intervals.',
      'Forecast starts from current usage and excludes the one-off next-task plan. No guaranteed compaction timing.',
      'Missing estimates stay unknown. No account quota or currency pricing is inferred.',
    ],
  };
}
