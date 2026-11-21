---
name: properjob-budget-options
description: Compare supported scope and specification changes against a user's building budget. Use for affordability questions, renovation cost savings and choosing what to keep, simplify or defer.
---

# Fit a project to a budget

## Country and language

Reply in the requested or conversation language. Keep the actual project country,
currency, units and tax basis independent of language; do not infer them from a
translation or a shared currency symbol. Keep the same local pricing and tax basis across alternatives. Reuse an unchanged result when only the explanation language changes; do not invent a new price or claim the card supports an unavailable translation.

For international documents, number formats or jurisdiction questions, read the
[country and language rules](../properjob-building-work/references/international-workflows.md),
also available at `skill://proper-job/properjob-building-work/references/international-workflows.md`.

## Workflow


Keep the user's target amount, currency, tax basis and whether it covers building
work or the whole project distinct. Start with the existing baseline and known
priorities. If the budget basis is unknown, state that and still identify useful
options; do not replace the user's design or silently remove requested work.

Read `properjob-building-work` before calculating. Reuse the existing baseline
unless its facts changed. Propose a few concrete, separately labelled options
such as smaller area, retained layout/fittings, a different specification or
clearly defined deferred work. Keep essential requirements stated by the user.
Do not suggest omitting necessary safety work or assume it is unnecessary.

Calculate only supported options the user requested or agreed to explore. For
GB/US legacy Guide Price comparisons use `compare_guide_scenarios` only within
its existing contract; otherwise use `calculate_building_work` for each changed
scenario. Keep country, units, scope and the same pricing-policy basis aligned.
Tool defaults are still assumptions, not confirmed user choices.

Show the changed scope, returned price, tradeoff and what remains outside each
option. Use server-returned deltas when available. Otherwise use explicit host
arithmetic on comparable returned amounts, labelled as a comparison. For ranges,
endpoint changes describe movements in the guide bands, not guaranteed savings;
if reporting a possible difference interval use baseline.low - option.high to
baseline.high - option.low. Negative differences and overlapping bands matter.
Do not compare a draft central amount with a guide band as if identical evidence.

Compare the target with the same tax and cost scope. A low endpoint below the
target does not prove affordability. Say when the upper estimate exceeds it or
fees/unpriced work prevent an overall conclusion. Do not adjust the engine price
or invent supplier discounts to make the target appear achievable.

If supported options still exceed the budget, say so and describe the choices
that remain. Deferring work can repeat setup costs; do not invent a phasing saving
or promise that inflation, finance, grants or resale gains will cover the gap.
