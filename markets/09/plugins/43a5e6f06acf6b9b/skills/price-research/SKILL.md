---
name: price-research
description: Retrieve and compose CostInflation price evidence, calculate quantity-defined comparisons, and present dated findings with charts, tables and citations.
---

Use CostInflation as evidence and calculation tools. Choose the calls that supply
the information needed for the user's question; the host agent owns interpretation
and recommendations. All calls are read-only and need no sign-in.

Resolve category IDs with `search` or `get_catalog`. The catalog accepts an optional
`query`, `index_kind`, `cursor` and `page_size` (1–50); follow `next_cursor` with
the same filters to continue. Use `fetch` for a category's measured quantity,
supported area IDs, canonical units, dated evidence and citation. Do not guess
category IDs, area IDs or unit codes. Preparation calls do not open a widget.
Location inputs are supported public `area_ids`, not street addresses. If a
requested place is outside the returned panel, explain that coverage and offer a
supported-area comparison; do not ask for a precise address that these tools
cannot resolve. These tools return category evidence and estimates, not checkout
prices, purchases or payment-card operations.

Choose operations by the evidence needed:

| Tool | Inputs and purpose |
| --- | --- |
| `get_coverage` | `series_ids`, optional `area_ids`, `start_date`, `end_date`: inspect available dates, missing calendar days, gaps and freshness. |
| `get_price_history` | One `series_id`, optional areas and dates: read actual observations and boundary changes; provides the existing interactive history view. |
| `get_price_matrix` | `series_ids`, `area_ids`, optional `at_date`: compare measured category quantities across areas with per-cell actual dates, age and status. |
| `get_price_changes` | `series_ids`, `area_ids`, `start_date`, `end_date`, optional `order_by`: obtain exact changes between distinct actual boundaries; order by `absolute_change`, `percent_change` or `end_value`. |
| `compare_basket` | Explicit `items`, `area_ids`, optional `at_date`: calculate category estimates, line costs, completeness and complete-area rankings; provides the existing editable basket view. |
| `get_basket_history` | Explicit `items`, `area_ids`, start/end dates, optional `observation_policy`: calculate a fixed-quantity basket on calendar dates, retaining missing lines and null incomplete totals. |
| `decompose_basket_change` | The same fixed items, areas, dates and policy: obtain item contributions that reconcile to the complete basket change. |
| `compare_price_quotes` | `quotes` with `quote_id`, USD `price`, `quantity`, `unit`; `common_unit`, optional `common_quantity` and `benchmark`: normalize supplied quotes and optionally compare with a dated category/area observation. |
| `get_history_statistics` | Categories, areas, start/end dates, optional `statistics`: request `min`, `max`, `median` and `current_rank` over equally weighted daily category observations, with sample counts, gaps and tie definitions. |
| `get_price_distribution` | One leaf `series_id`, areas, optional `at_date` and `quantiles` (`p05`, `p25`, `p75`, `p95`): read published category bands, counts and weighting method. |
| `get_package_size_changes` | One leaf category, areas and start/end dates: retrieve anonymous consecutive-day matched package/price changes, match coverage and excluded/ambiguous cohorts. |
| `render_price_view` | `view_kind` and the originating result's `view_data` as `data`: present prepared evidence as `line`, `bars`, `contribution`, `matrix` or `table`. |

Dates are canonical `YYYY-MM-DD`. Multi-category reads accept up to 12 distinct
categories and 12 areas. Basket operations accept up to 30 distinct leaf items;
every item requires `series_id`, an exact decimal `quantity` and explicit `unit`.
`display_units` means multiples of the entire displayed quantity. Five pounds is
`quantity: "5", unit: "pounds"`, not five bags. Quote comparisons likewise use
compatible canonical physical/count units and exact decimal strings.

Basket history and decomposition use `{"kind":"same_day"}` by default. Use
`{"kind":"bounded_as_of","max_age_days":N}` (1–30) only when the user's
comparison permits earlier observations. Preserve the applied policy and actual
dates. For follow-ups, retain the categories, quantities, areas and period unless
the user changes them. Shorten an oversized selection rather than silently dropping
rows; query windows and prepared views have explicit server limits.

Read complete `structuredContent`; `response_summary` is a factual preview rather
than a prescribed answer. Use returned exact arithmetic, ordering and coverage
statuses. Incomplete basket totals are null; partial subtotals do not enter
`complete_area_ids_by_total`. Earlier boundaries, same observations, missing dates
and zero-baseline percentages have explicit meanings. Statistical ranks describe
daily category history; distribution bands describe a different population.
`current_rank.min_rank` through `max_rank` is the ascending rank interval, with
1 representing the lowest price. `percentile_at_or_below` is the percentage of
observed days priced at or below the latest value: six of seven such days means
85.7%. Preserve `below_count`, `equal_count` and `above_count` when explaining ties.
Preserve the returned pooled/panel weighting method. Summed marginal bands are
scenarios, not measured basket percentiles. Matched package changes alone do not
establish shrinkflation, causality or the entire category's change. Supplied quotes
remain distinct from CostInflation observations.

After assembling useful evidence, call `render_price_view` with returned `view_data`
unchanged: for example `{"view_kind":"table","data":result.view_data}`.
Choose a line view for dated series, bars for comparisons, contribution bars for
item deltas, and a matrix/table for exact multi-category inspection. The component
offers numeric-column selection, filters, sorting and accessible evidence tables;
there is no need to manufacture chart coordinates or recompute money. If a result
has no `view_data` because its complete evidence exceeds view limits, request a
smaller selection or use a compact native table. Non-UI clients still receive the
complete evidence. Do not narrate every lookup, dump JSON, or repeat the view's
full tables in the answer.

Ground claims in the returned category, measured quantity, area scope and actual
dates. Cite returned canonical URLs near supported findings; use the returned
methodology link rather than inventing website paths. Attribute analysis to
CostInflation and responsibility to CostInflation Team. Keep public explanations
source-neutral; do not reveal underlying proprietary rows, internal identifiers,
data destinations or collection mechanics. Scheduling, notifications and durable
user memory belong to the host, not these stateless tools.
