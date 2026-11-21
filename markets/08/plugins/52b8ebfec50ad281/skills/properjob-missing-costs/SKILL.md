---
name: properjob-missing-costs
description: Check a building brief, budget or quote for missing work and overlooked project costs. Use when someone asks what they have forgotten, what is excluded or what could increase their renovation budget.
---

# Check missing building costs

## Country and language

Reply in the requested or conversation language. Keep the actual project country,
currency, units and tax basis independent of language; do not infer them from a
translation or a shared currency symbol. Use the project jurisdiction for possible permits, fees and site requirements. Do not turn a UK omission checklist into confirmed requirements abroad; keep local unknowns as questions.

For international documents, number formats or jurisdiction questions, read the
[country and language rules](../properjob-building-work/references/international-workflows.md),
also available at `skill://proper-job/properjob-building-work/references/international-workflows.md`.

## Workflow


Start from the supplied brief, quote, drawing review or existing calculator
result. Reuse known facts and the existing price; do not recalculate just to
explain exclusions. If the user has no documents, review the known project now
and ask at most one material question after the useful findings.

For relevant items record one of: included with a source, explicitly excluded,
allowance with a source, unknown, or not applicable with a reason. Quote silence
is unknown. An allowance is not a confirmed final cost. Do not present a generic
checklist as confirmed additional work.

Check the project interfaces that could leave a gap:

- Strip-out, temporary protection/support, access, scaffolding, waste and site
  setup; shared setup should be counted once.
- Ground conditions, drainage, existing structure, weatherproofing and connecting
  old and new work; specialist requirements remain questions unless established.
- Plumbing, electrical and heating changes, fittings, client-supplied items,
  finishing adjacent surfaces and reinstating outside areas.
- Separately budgeted design/survey costs, permissions/inspections, tax, temporary
  accommodation and contingency where relevant. Do not assert a local legal
  requirement or tax entitlement without an applicable current source.

Return the important gaps with why they matter, the evidence and the next fact
needed. Prioritise consequences qualitatively when amounts are unknown. Never
attach invented percentages or prices to a possible omission. Preserve a usable
existing estimate, explicitly stating whether unresolved work is outside it.

Read `properjob-building-work` before a requested price update. Send only newly
established, supported scope to `calculate_building_work`; reuse unchanged
results. For supplied extra amounts, ordinary host arithmetic may reconcile a
separately labelled budget ledger. That is not a new Proper Job rate. Use
`properjob-project-budget` when the user wants that overall budget.

This is a scope review, not an inspection, structural diagnosis or certification.
Never mark unseen drawings or unanswered checks as completed.
