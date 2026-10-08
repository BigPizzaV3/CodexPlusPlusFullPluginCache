---
name: dashboard-comparator
description: >-
  Use this skill to build a live, MSCI-branded HTML dashboard aligning 2-5 MSCI indexes side by side on composition and/or performance/risk via the IndexAI Insights MCP, all on one shared currency, variant and as-of date. Trigger for "compare these indexes", "side by side", "which of these has more X", when 3 or more indexes are named, or when 2 indexes are named alongside an explicit request for an aligned comparison table rather than an index-vs-parent framing, even if the user never says MSCI. Produces a rendered, refreshable .html artifact via the bundled assemble.py — never a text-only answer. This dashboard owns no new metrics; it is an alignment contract over composition and performance/risk.
---

# Index Comparator Dashboard

Build a self-contained, MSCI-branded HTML dashboard comparing 2-5 indexes side by side. This is a **compare mode**, not a new metric set — it reuses the composition pulls (`dashboard-composition`) and the performance/risk pulls (`dashboard-performance-risk`), rendered as aligned columns rather than a single dashboard's own view. If the user's question is really about one index, or a single index vs its parent variant, route to the single-index dashboards instead of forcing a one/two-index "comparison." See `references/recipes.md` §6 and `references/metric-audit.md` §6.

## Output

Header strip confirming the shared currency/variant/as-of date across all indexes → composition comparison table (weights/sector/country side by side) → performance comparison table (multi-period returns side by side) → risk analytics panel (native IMX charts, one per index or one relative-to-baseline) → standard disclaimer footer. Present with `present_files`, listing every index name/code included.

## Workflow

1. Resolve all 2-5 index codes via `search_index_indexes` — never guess.
2. **Mandatory alignment contract** — confirm with the user if unspecified rather than guessing per index: one currency, one variant (STRD/GRTR/NETR), one as-of date (and, for performance, one range) across every selected index. A silent mismatch (one index in NETR, another in GRTR) produces a wrong comparison, not just an incomplete one.
3. For composition: reuse the constituents/sector/country pulls, once per index, at the shared date.
4. For performance/risk: reuse the in-shell returns/factor-tilt pulls per index; for risk analytics, call `calculate_metrics` per index (or with one index as `benchmark_portfolio` for an explicit active view against a chosen baseline).
5. Render side by side — columns per index, never a blended average — so a reader sees each index's own numbers next to the others'. A null value for one index/period is shown "n/a" in that index's column — never drop the index from the table because one field is missing.
6. Add one grounded interpretive callout per major section (standing rule 10).

## Interpretation

- This dashboard is a compare mode over the other analyst dashboards, not an independent data source — every number in it must trace back to the same fields those dashboards use.
- Never let one index's missing field cause the whole comparison row to be dropped; show "n/a" and keep every other index's data intact.

## Handoff

- A single index's own detail, in full → `dashboard-composition`.
- A single index's own performance/risk detail, in full → `dashboard-performance-risk`.
- Climate/ESG comparison specifically (index vs parent framing) → `dashboard-climate`.
- What changed at a review, for one index → `dashboard-changes`.
- Eligibility or methodology rules → `dashboard-methodology`.

## Guardrails

- Confirm the alignment contract (currency/variant/date) before pulling any data, not after rendering a mismatched table.
- Every dashboard must build through `assets/assemble.py`. This package bundles everything needed to do so: `assets/{dashboard-shell.html, assemble.py, disclaimer-footer.html, disclaimer-notice.txt, refresh-snippet.html, logos/}` and `references/{brand.md, recipes.md, metric-audit.md, mcp-queries.md}`. Full build mechanics, the shared shell/brand/disclaimer stack, and the as-of/range control are documented in `references/recipes.md`'s "Shared conventions" section (self-contained in this package) — apply them exactly as written; do not re-derive or simplify them.
