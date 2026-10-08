---
name: dashboard-climate
description: >-
  Use this skill to build a live, MSCI-branded HTML dashboard of an MSCI index's sustainability and climate metrics via the IndexAI Insights MCP: WACI (weighted average carbon intensity), Implied Temperature Rise, Climate VaR, Low Carbon Transition score, and EU BMR alignment (climate-aligned flag, investable-universe overlap, sustainable-investment screening weight) — framed as index vs parent wherever a parent variant is resolved. Trigger for "carbon intensity", "WACI", "implied temperature rise", "climate VaR", "EU BMR", "Paris aligned", "how does this ESG index differ from its parent", even if the user never says MSCI. Produces a rendered, refreshable .html artifact via the bundled assemble.py — never a text-only answer.
---

# Sustainability & Climate Index Dashboard

Build a self-contained, MSCI-branded HTML dashboard showing how climate/ESG index construction reshapes an index relative to its parent. See `references/recipes.md` §3 and `references/metric-audit.md` §3 for the exact field list; these are EOM-published values (2nd business day snap) — never intraday-refreshed.

## Output

KPI row (WACI, ITR, aggregate Climate VaR) → index-vs-parent comparison table (when a parent is resolved) → EU BMR alignment panel → Low Carbon Transition score (native IMX chart callout, not a plain scalar) → coverage footnotes under every metric with a paired `cov_*` field → standard disclaimer footer. Present with `present_files`, stating index(es), as-of month, and that this is an EOM snapshot.

## Workflow

1. Resolve the index code, and its parent/standard-index variant if the user wants an explicit vs-parent view, via `search_index_indexes` — confirm with the user if ambiguous.
2. **In-shell (MCP-direct), pulled for each index code separately** — this pairing matters: pull `equity_index.esg_metrics_additional.wtd_avg_carbon_intensity_by_sales_scope_1_2_3` + its coverage field for both the index and the comparison index individually. The FIMD-namespace `waci_index`/`waci_parent` pair only applies to factor indexes in a vetted FIMD list and returns null for a standard index-vs-parent ask — do not use it for that. Also pull `equity_index.esg_metrics.implied_temperature_rise` + `cov_implied_temperature_rise`, `equity_index.esg_metrics.total_var` + its physical/policy coverage fields, and the EU BMR fields (`climate_aligned`, `benchmark_investable_overlap`, `eu_sust_invst_scrn_wt_sm`).
3. **Native IMX chart:** the index-level Low Carbon Transition score (`index_esg_low_carbon_transition_score_last`) has no plain catalog scalar — call `calculate_metrics` and present it as a native interactive chart, the same handling as risk analytics in `dashboard-performance-risk`, never re-plotted numbers.
4. Render every in-shell metric **paired with its coverage field** where one exists (standing rule 8) — a headline climate number with low coverage is misleading shown alone.
5. Validate (`references/metric-audit.md` § Validation): WACI/ITR/Climate VaR non-negative where the field's definition requires it; every `cov_*`-paired value shows its coverage; ITR is never converted to/from a carbon-intensity number.
6. Add one grounded interpretive callout per major section (standing rule 10) — e.g. quantify how much a Paris-aligned screen cuts carbon intensity or brings modelled temperature alignment under the Paris ceiling, citing the exact numbers shown.

## Interpretation

- ITR is a forward-looking modelled alignment estimate in °C — never state or imply it converts to/from a carbon-intensity figure.
- If the connector doesn't return a parent-index field for a given index, drop the vs-parent framing rather than fabricating a comparison — show the single-index view only.
- A null EU BMR overlap for an index means it isn't a regulated EU BMR disclosure benchmark — that's the correct answer, not missing data; say so rather than leaving a blank cell unexplained.

## Handoff

- Composition, holdings, or sector/country weights → `dashboard-composition`.
- Returns, factor tilts, or risk analytics → `dashboard-performance-risk`.
- What changed at the last N reviews → `dashboard-changes`.
- Eligibility or the rule behind a construction choice → `dashboard-methodology`.
- Comparing climate metrics across more than 2 indexes at once → `dashboard-comparator`.

## Guardrails

- Do not compute WACI, ITR, or Climate VaR yourself from underlying company data — these are MCP-direct/EOM-published values only.
- Every dashboard must build through `assets/assemble.py`. This package bundles everything needed to do so: `assets/{dashboard-shell.html, assemble.py, disclaimer-footer.html, disclaimer-notice.txt, refresh-snippet.html, logos/}` and `references/{brand.md, recipes.md, metric-audit.md, mcp-queries.md}`. Full build mechanics, the shared shell/brand/disclaimer stack, and the as-of/range control are documented in `references/recipes.md`'s "Shared conventions" section (self-contained in this package) — apply them exactly as written; do not re-derive or simplify them.
