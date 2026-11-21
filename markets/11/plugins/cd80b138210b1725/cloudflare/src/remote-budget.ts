import { z } from 'zod';
import { BudgetInputError, bases, MAX_TOKENS, planContextBudget } from './budget';

export function cachedMcpSchema<S extends z.ZodType>(schema: S) {
  const input = schema['~standard'].jsonSchema.input({ target: 'draft-2020-12' });
  const output = schema['~standard'].jsonSchema.output({ target: 'draft-2020-12' });
  return { '~standard': { ...schema['~standard'], jsonSchema: {
    input: () => input, output: () => output,
  } } };
}

export const remoteFields = ['reference_limit_tokens','used_tokens','planned_increase_tokens',
  'reserved_output_tokens','growth_per_turn_tokens'] as const;
const count = (minimum = 0) => z.number().int().min(minimum).max(MAX_TOKENS).nullable().optional();
export const remoteInputSchema = z.object({
  reference_limit_tokens: count(1).describe('Explicit reference budget; not a model/platform lookup.'),
  used_tokens: count().describe('Explicit current token estimate, not a lifetime total.'),
  planned_increase_tokens: count().describe('Extra next-task context excluding the separate output reserve.'),
  reserved_output_tokens: count().describe('Additional output reserve; explicit zero only when intended.'),
  growth_per_turn_tokens: count().describe('Explicit estimate of future token growth per turn. No past-turn or conversation records are accepted.'),
  sources: z.object(Object.fromEntries(remoteFields.map(field=>[field,z.enum(bases).optional()]))).strict().optional(),
}).strict();
const nullableNumber=z.number().finite().nullable();
const metrics=z.object({used_tokens:nullableNumber,fraction:nullableNumber,remaining_tokens:nullableNumber,
  over_budget_tokens:nullableNumber,weather:z.enum(['Unknown','Clear','Fair','Cloudy','Showers','Storm'])}).strict();
export const remoteOutputSchema=z.object({
  schema_version:z.literal(1),basis:z.literal('explicit_numeric_inputs'),reference_limit_tokens:z.number().int().nullable(),
  inputs:z.object(Object.fromEntries(remoteFields.map(field=>[field,z.number().int().nullable()]))).strict(),
  sources:z.object(Object.fromEntries(remoteFields.map(field=>[field,z.enum(bases).nullable()]))).strict(),
  current:metrics,plan:z.object({added_tokens:z.number().int().nullable(),after:metrics,fits_reference:z.boolean().nullable()}).strict(),
  growth:z.object({basis:z.literal('supplied_rate'),tokens_per_turn:nullableNumber,turns_until_reference:z.number().int().nullable(),
    forecast:z.array(z.object({step:z.number().int().min(1).max(5),budget:metrics}).strict()).max(5)}).strict(),
  unknowns:z.array(z.enum([...remoteFields,'actual_platform_context','actual_compaction_policy','account_quota','monetary_cost'])),
  limitations:z.array(z.string()),
}).strict();

export function validateRemote(input:unknown) {
  const parsed=remoteInputSchema.safeParse(input);
  if(!parsed.success)throw new BudgetInputError();
  const args=parsed.data;
  for(const field of remoteFields)if(args.sources?.[field]!==undefined && args[field]==null)throw new BudgetInputError();
  return args;
}

export function planRemoteBudget(input:unknown) {
  const args=validateRemote(input);
  const numeric=Object.fromEntries(remoteFields.map(field=>[field,args[field]??null]));
  const sources=Object.fromEntries(remoteFields.map(field=>[field,args[field]==null?null:args.sources?.[field]??'user_provided']));
  const original=planContextBudget(Object.fromEntries(remoteFields.filter(field=>field!=='growth_per_turn_tokens').map(field=>[field,numeric[field]])));
  const limit=args.reference_limit_tokens??null,used=args.used_tokens??null,rate=args.growth_per_turn_tokens??null;
  let until:number|null=null;
  const forecast=[];
  if(limit!==null&&used!==null&&rate!==null) {
    if(used>=limit)until=0;
    else if(rate>0)until=Math.ceil((limit-used)/rate);
    for(let step=1;step<=5;step++) {
      const future=used+rate*step;
      // Original per-input cap applies to user inputs, not generated forecast totals.
      const fraction=future/limit;
      const rank=[35n,55n,70n,85n].findIndex(cut=>BigInt(future)*100n<BigInt(limit)*cut);
      forecast.push({step,budget:{used_tokens:future,fraction,remaining_tokens:Math.max(0,limit-future),
        over_budget_tokens:Math.max(0,future-limit),weather:['Clear','Fair','Cloudy','Showers','Storm'][rank===-1?4:rank]}});
    }
  }
  return {schema_version:1,basis:'explicit_numeric_inputs',reference_limit_tokens:limit,inputs:numeric,sources,
    current:original.current,plan:original.plan,growth:{basis:'supplied_rate',tokens_per_turn:rate,turns_until_reference:until,forecast},
    unknowns:[...remoteFields.filter(field=>numeric[field]===null),'actual_platform_context','actual_compaction_policy','account_quota','monetary_cost'],
    limitations:[
      'Arithmetic from explicitly supplied numbers; no current chat, account, local file or model API access.',
      'The growth rate is a supplied estimate, not a fitted observation or verified telemetry; no prior-turn arrays are accepted.',
      'Forecast starts from current usage, excludes the one-off task plan and assumes the supplied rate continues.',
      'Weather uses reference cuts at 35%, 55%, 70% and 85%; reference crossing does not predict actual platform compaction.',
      'Missing inputs stay unknown. No account quota or currency pricing is inferred.',
    ]};
}
