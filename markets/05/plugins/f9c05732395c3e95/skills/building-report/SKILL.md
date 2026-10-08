---
name: building-report
description: Produce a complete, sourced research note on one Dubai apartment building — prices, rents, gross yields, growth and evidence for every unit size — using the Dubai Wealth Index tools. Use when the user asks to "tell me about", assess, research, write up or do due diligence on a named Dubai building or tower, or wants a report, spreadsheet or chart about one.
---

# Report on one Dubai building

Explicit user instructions take priority over this workflow.

## 1. Confirm the building

1. Call `search` with the name the user gave.
2. If the top hit carries a `matchedName`, the user's name is another name for
   that building (a project or marketing name). Say so in the answer:
   "Vera Residences is registered as Vera Tower, Business Bay."
3. If two hits are close, or `get_building` returns `resolved.building.confidence`
   of `fuzzy`, ask the user which building they mean before going further.

## 2. Read the whole building once

Call `get_building` with `detail: "report"`. Do not call it again per bedroom
type — the report already covers every publishable one. It returns:

- `identity` — registered name, area, DLD project. Quote the registered name.
- `bedrooms[]` — for each publishable unit size: sale and rent medians, gross
  yield and its price basis, short-term and off-plan figures where published,
  `growth` with both comparison windows, the area benchmark and a 6-year trend.
- `growthWindows` — the dates and bases every growth figure compares.
- `suppressed[]` — each figure that did not clear its evidence gate, and why.
- `limitations[]` — the caveats that travel with the figures.

## 3. Check the evidence when it matters

If a headline rests on few sales (a count under about 10), or the user asks
how solid a figure is, call `get_building_transactions` for the same building
and say whether the median rests on many comparable deals or a few scattered
ones. Check `factsEdition` against `metricsEdition` before reconciling counts.

## 4. Write it up

- Lead with the registered name, area and data date (`dataAsOf`).
- For each unit size: price, rent, gross yield, and the sample behind each.
- Growth: give the percentage with both windows, e.g. "+8.2% (median AED 2,040
  /sqft on 46 sales vs AED 1,885 on 51 in the prior 12 months)".
- List the suppressed figures as "not published: <reason>", never as zero.
- Close with the limitations that apply, and link `attribution` / the
  `canonicalUrl`.
- For a chart or spreadsheet, use the report's `trend` rows and per-bedroom
  figures as the data; do not interpolate missing years.

Never add a figure the tools did not return, and never describe a gross yield
as a net return.
