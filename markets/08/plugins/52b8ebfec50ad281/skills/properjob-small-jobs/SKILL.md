---
name: properjob-small-jobs
description: Budget an individual building trade, small job or repair, check local price support, or reconcile a supplied quantity and rate. Use for trade/repair cost questions such as plastering, decorating, flooring or fencing. Scope-only work lists and builder schedules use properjob-drawings-to-scope.
---

# Small jobs and repairs

## Country and language

Reply in the requested or conversation language. Keep the actual project country,
currency, units and tax basis independent of language; do not infer them from a
translation or a shared currency symbol. Use local terminology and the actual task/rate unit. A supplied foreign trade quote can be reconciled even when the country has no engine price for that trade; retain the distinction.

For international documents, number formats or jurisdiction questions, read the
[country and language rules](../properjob-building-work/references/international-workflows.md),
also available at `skill://proper-job/properjob-building-work/references/international-workflows.md`.

## Choose by the requested output

Use this skill when the main request is a trade/repair cost, price, rate or
quantity × supplied rate. An unsupported price can still lead to a useful
scope/measurement fallback below.

For a scope of works, work description, tender brief or builder pricing schedule
without a requested price, use `properjob-drawings-to-scope`, even for a small
repair and even without plans. Do not choose this skill merely because the work
is small or no drawing is attached.

## Workflow

Identify the requested intervention rather than pricing the entire building.
Distinguish repair from replacement, supply only from installed work, and a
single task from a room refurbishment. Use the user's units; room floor area is
not wall area, roof area or a count of fittings.

Read `properjob-building-work`, the actual `calculate_building_work` schema and
`properjob://building-work/market-coverage`. Check support for the precise local
task. GB detailed drawing roles are not universal standalone trade tariffs;
foreign room guides do not establish prices for every component or repair.

- If a supported standalone work type or typed refurbishment package represents
  the job, pass the known task, affected quantities and scope. Give the returned
  range with its minimum-budget, tax, assumption and inclusion basis, then ask
  the returned useful question. Never invent a call-out or minimum-job rate.
- If a drawing-based task is supported, follow the core skill's source-cited
  quantity workflow. Do not fabricate drawing observations from a verbal brief
  to force detailed pricing.
- If the task is unsupported, provide a useful scope/measurement schedule and
  mark the price unavailable. Ask for a supplied quote or rate if the user wants
  quantity × rate arithmetic. Preserve that rate's source, date, tax and
  supply/install basis; label it user-supplied, not a Proper Job benchmark.

For relevant tasks establish the material/specification, measured surface or
length/count, existing condition, preparation, removal/disposal, access and
making good. Ask only the most consequential unknown; do not demand a full form
before giving a supported rough price. Do not infer defects from age or photos
or provide safety-critical diagnosis.

Never use a whole-home price per square metre, a budget allocation, a currency
conversion or another country's labour rates to manufacture a small-job price.
General roofing, fencing, patios and service repairs remain unpriced wherever
the current policy does not support them. The skill can scope them without
claiming those additional rates have been implemented.
