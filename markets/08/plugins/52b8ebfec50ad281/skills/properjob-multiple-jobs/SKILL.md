---
name: properjob-multiple-jobs
description: Organise several building or renovation jobs into one budget with explicit coverage and overlap checks. Use for mixed lists of rooms, repairs, extensions and external works rather than a single isolated job.
---

# Budget several jobs together

## Country and language

Reply in the requested or conversation language. Keep the actual project country,
currency, units and tax basis independent of language; do not infer them from a
translation or a shared currency symbol. Keep every package attached to its actual country, currency, tax and unit basis. A change of language does not make foreign packages additive or allow UK rates to fill unpriced work.

For international documents, number formats or jurisdiction questions, read the
[country and language rules](../properjob-building-work/references/international-workflows.md),
also available at `skill://proper-job/properjob-building-work/references/international-workflows.md`.

## Workflow


Turn the user's actual work list into a scope register. Give each physical area
or item a stable neutral ID, location/entity, work extent, quantity/unit if known,
and inclusion relationship. Distinguish new, retained, repair and replacement
work. Preserve unknowns and do not silently choose specifications.

Read `properjob-building-work` and current
`properjob://building-work/market-coverage` before pricing. Check the current tool
schema for the actual country and work type; a recognised country is not support
for every trade.

- Prefer one supported composite refurbishment/project calculation when its
  scope can represent the jobs faithfully. Pass room counts and explicit
  containment facts rather than adding rooms to floor area that includes them.
- Use separate calculations for genuinely independent supported packages only
  when their physical scope and inclusions do not overlap. Reuse unchanged
  results. Never rename an unsupported repair or patio as a whole-home remodel
  simply to obtain a price.
- Mark each package as calculator-priced, supplied quote/amount, included within
  another package, unpriced or unresolved overlap. An overall guide breakdown
  allocates its total; those lines are not independent trade estimates.
- Check kitchen/bathroom fitout, decoration, service alterations, demolition,
  access/setup, disposal, margin, contingency and tax before combining anything.
  If bundled prices cannot separate shared costs, do not subtract an invented
  overlap credit or claim a combined project total.

Use host arithmetic for a separately labelled budget summary only after checking
that amounts have the same currency, tax basis and non-overlapping scope. Show
source, basis and inclusion for every amount. A sum of independent low/high
endpoints is a planning envelope, not a calibrated probability interval or a
single-engine quote. Do not add point totals and ranges without explaining the
basis. Never combine alternative options as if all will be built.

Return the priced subtotal, included sub-items and a visible list of unpriced or
overlapping work. Call it a partial budget if any requested work is unresolved;
do not label it a complete price. Ask the next question that resolves the largest
gap. This skill adds coordination, not new trade rates or worldwide coverage.
