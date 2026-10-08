---
name: dashboard-performance-risk
description: >-
  Use this skill to build a live, MSCI-branded HTML dashboard of an MSCI index's returns, factor (FaCS) tilts, and dividend yield via the IndexAI Insights MCP, plus MSCI's own computed IMX risk analytics (tracking error, Sharpe/information ratio, VaR/CVaR, drawdown, active-risk attribution) called out as a native interactive chart. Trigger for "how has X performed", "tracking error vs Y", "Sharpe ratio", "factor tilts", "VaR", "drawdown", "risk attribution" for an index, even if the user never says MSCI. Produces a rendered, refreshable .html artifact via the bundled assemble.py — never a text-only answer, and never a hand-derived risk number.
---

# Index Performance & Risk Dashboard

Build a self-contained, MSCI-branded HTML dashboard of an index's returns and factor drivers, with MSCI's own IMX risk analytics surfaced as a native interactive chart. Two distinct sources feed this dashboard and must stay visually and mechanically separate: MCP-direct catalog fields render **inside** the shell; IMX-computed risk analytics render as their **own interactive chart**, never re-plotted into the shell's SVG renderer. See `references/recipes.md` §2 and `references/metric-audit.md` §2 for the exact field/mnemonic list.

## Output

One dashboard: KPI row (YTD, 1Y, 3Y CAGR, latest tracking error if a benchmark is set) → multi-period returns table → historical level chart → factor-tilt panel → "Risk analytics" panel (native IMX chart callout) → standard disclaimer footer. Equity indexes only — for fixed income/hedged indexes, state plainly that IMX risk analytics aren't available and show only the in-shell returns/factor fields. Present the file with `present_files`, stating index/benchmark, currency, variant, as-of date/range.

## Workflow

1. Resolve the index (required) and, if the user wants relative metrics, a benchmark index — both via `search_index_indexes`, never guessed. Resolve the as-of business date from a probe call's `fetched_date`, never today's calendar date.
2. **In-shell part** (through `assets/assemble.py` like every dashboard): `fetch_index_data` for `equity_index.performance.period_returns.{period,returns}` and `equity_index.facs_ratios.*`; `fetch_index_timeseries` for the historical level chart and, where `supports_range=true`, factor-tilt history. Render KPI cards, the multi-period table, and a factor-tilt panel — all MCP-direct, inline SVG, no external chart lib.
3. **Native IMX part** (NOT built through the shell's chart renderer): call `calculate_metrics` with the mnemonics in `references/metric-audit.md` §2 — `key_metrics`, `key_risk_metrics`, `index_tracking_error`, `index_sharpe_ratio`, `index_information_ratio`, both risk-attribution breakdowns, both risk-contributor grids — passing the benchmark as `benchmark_portfolio` when a relative view is wanted. Present the result as its own interactive chart in the conversation; the dashboard body only labels and describes this panel, it does not re-render the numbers.
4. Attempt **every** category in that mnemonic list, not an arbitrary subset (standing rule 9) — a category genuinely needing a benchmark the user didn't supply is labelled "requires a benchmark", never omitted from the panel or shown as zero; a category that errors is labelled with the error, never silently dropped.
5. Validate: in-shell returns/factor fields follow the same return/unit checks as the Composition dashboard; relative IMX metrics are never rendered as 0 or blank when `benchmark_portfolio` is absent.
6. Add one grounded interpretive callout per major section (standing rule 10).

## Interpretation

- Never recompute Sharpe/tracking error/etc. yourself from the in-shell returns, even as a fallback — that's exactly the ad hoc-methodology shortcut the metric rule exists to prevent. MSCI computes these itself as IMX analytics; if IMX is genuinely unavailable on the connection, say so rather than approximating.
- Label FaCS tilts as relative to MSCI ACWI IMI (per their own field description), never as absolute levels.
- Momentum-style factor strategies can reverse sharply when leadership rotates — a strong multi-year tilt number doesn't guarantee a positive short-horizon return; state both where relevant.

## Handoff

- What's inside the index (holdings, sector/country weights, cross-index membership) → `dashboard-composition`.
- Carbon intensity, temperature alignment, climate VaR, or a Low Carbon Transition score → `dashboard-climate`.
- What changed at the last N reviews → `dashboard-changes`.
- Eligibility or the rule behind a factor/weight → `dashboard-methodology`.
- Comparing performance/risk across more than 2 indexes at once → `dashboard-comparator`.
- The factor methodology input behind selection/weighting (Quality/Momentum/Dividend score) → `dashboard-fimd`.

## Guardrails

- MCP-direct fields + simple arithmetic only for the in-shell part; methodology-sensitive analytics (tracking error, Sharpe, Sortino, alpha, beta, information ratio, correlation, rolling volatility, max drawdown) are never derived by this skill's own arithmetic — only ever shown via the native IMX chart.
- A relative metric requested without a benchmark is stated as requiring one, never shown blank or as zero.
- Every dashboard must build through `assets/assemble.py`. This package bundles everything needed to do so: `assets/{dashboard-shell.html, assemble.py, disclaimer-footer.html, disclaimer-notice.txt, refresh-snippet.html, logos/}` and `references/{brand.md, recipes.md, metric-audit.md, mcp-queries.md}`. Full build mechanics, the shared shell/brand/disclaimer stack, and the as-of/range control are documented in `references/recipes.md`'s "Shared conventions" section (self-contained in this package) — apply them exactly as written; do not re-derive or simplify them.
