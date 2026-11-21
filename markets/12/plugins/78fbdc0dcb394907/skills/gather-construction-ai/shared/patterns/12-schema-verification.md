# Pattern 12: Schema Verification and Graceful Degradation

Dashboard report field availability varies by workspace configuration. Before computing any metric that depends on a specific field (per-person daily granularity, days-on-site vs days-used, planned dates, possession timestamps, attendee lists, record IDs in report rows):

1. Call `getReportSchemas` (or inspect the first data response) to verify the field exists.
2. If it exists → proceed.
3. If it does not → **degrade explicitly**: compute the stated fallback (or omit the metric), and say in the output which metric was downgraded and why. Never fill a placeholder with an invented value.

**Divide-by-zero convention:** any ratio whose denominator is zero (planned = 0, output = 0, baseline rate = 0, delivered = 0) renders as "n/a" with a data-quality flag — never as a number, never as an error.

**Estimate discipline:** never present a numeric estimate without a stated derivation. Where a template asks for a quantity the data cannot support, write "not quantifiable from available records" instead.
