---
name: compare
description: >-
  Use this skill to compare two to five MSCI indexes side by side on performance, risk, composition, valuation, or sustainability metrics. Trigger for "compare A and B", "A vs B", "what is the difference between these indexes", "how does A differ from B", "which of these is more concentrated", even if the user never says MSCI. The comparison must be aligned on one currency, one return variant, and one as-of date.
---

# Aligned index comparison

A comparison is only meaningful when every index is measured the same way. This skill exists to enforce that alignment; the underlying figures come from the same workflows used for a single index.

## Output

One row per index, one column per requested metric. Identify each index as `<name> (<msci_index_code>)`. State the alignment basis **once, above the table**: currency, return variant, and as-of date. Then give the differences that answer the question.

## Alignment contract

Before fetching, fix and then state:

1. **Currency** — one currency for all indexes.
2. **Variant** — one of `STRD` (price), `GRTR` (gross total return), `NETR` (net total return) for all indexes. These are materially different answers and are never interchangeable.
3. **As-of date** — one date, or one period with one anchor, for all indexes.

If the user specifies none of these, choose a defensible default, state it explicitly, and apply it uniformly.

## Workflow

1. Resolve every index with `search_index_indexes`, in parallel. Never guess a code.
   Pass all resolved codes in a **single** `fetch_index_data` call where the datapoints allow it. Verified live: multiple codes in one request return keyed per entity as `<name> (<code>)`, which keeps the comparison on one request, one date, and one basis by construction.
2. If any requested benchmark is not an MSCI index, say so and exclude it. Do not silently substitute a similar MSCI index.
3. Discover each requested metric once with `search_index_datapoints`, then apply the same id across all indexes so the columns are genuinely comparable.
4. Route by dimension, keeping the alignment contract intact:
   - performance, risk, valuation, factor scores → the `benchmark` workflow
   - constituents, weights, country/sector splits, concentration → the `composition` workflow
   - construction and review rules → the `methodology` workflow
   - climate and sustainability metrics with coverage → the `climate` workflow
5. Read `strict_gate` before fetching. If one index cannot be served in the chosen variant or currency, either move every index to the documented fallback id, or report that index as unalignable and exclude it from the compared columns. Never mix gates within one table.
6. Remember that end-of-month snapping applies to the whole request. If any datapoint snaps, every index in that request snaps with it. Report the requested and fetched dates.
7. For history, use `fetch_index_timeseries` over one shared date range at one frequency.

## Interpretation

- If one index is the parent of another, or one is a screened or capped version of the other, say so. That relationship usually explains most of the difference.
- IMI, Standard, Small Cap, and All Cap are different universes, not variants of one index.
- Differences in constituent count or country coverage often explain a return gap better than any single metric.
- Comparing an aggregate index-level ratio across indexes is valid only if the same definition was returned for each.

## Guardrails

- Never compare gross against net, or one currency against another, within a table.
- Never compare figures from different as-of dates without labelling every date in the row.
- Do not exceed five indexes without confirming scope; beyond that, ask which metrics matter.
- If a metric is unavailable for one index, leave the cell explicitly unavailable rather than substituting a near-equivalent id.
- A difference in a returned metric is not an explanation. If the user asks why, hand off to `benchmark` for drivers or `methodology` for the governing rule.
