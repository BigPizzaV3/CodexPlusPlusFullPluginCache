---
name: dashboard-composition
description: >-
  Use this skill to build a live, MSCI-branded HTML dashboard showing what sits inside one or more MSCI indexes via the IndexAI Insights MCP: constituents and top holdings, constituent weights, country/region/sector breakdowns, concentration, and — on a second tab — a single security's identifiers, weight, FIF/NOS and whether it's a member of each selected index. Trigger for "top 10 holdings", "sector breakdown", "country weights", "how many stocks are in it", "which index holds this stock", "compare index composition", even if the user never says MSCI. Produces a rendered, refreshable .html artifact via the bundled assemble.py — never a text-only answer.
---

# Index Composition Dashboard

Build a self-contained, MSCI-branded HTML dashboard describing one or more indexes' internal structure at a stated date, plus (on a second tab) one security's cross-index membership. This is a dashboard-building skill: every response ends in a rendered `.html` artifact assembled through `assets/assemble.py`, never hand-authored HTML, and never a prose-only answer. Composition is a point-in-time snapshot — it answers what is in the index and at what weight, not how it performed (→ `dashboard-performance-risk`) and not why a rule exists (→ `dashboard-methodology`).

## Output

One dashboard, two top-level tabs — an **Index** tab and a **Security** tab — sharing one resolved as-of date and the same selected set of indexes. Identify each index as `<name> (<msci_index_code>)` and state the fetched date in the header. Present the file with `present_files`; state the dashboard type, index name(s)/code(s), currency, variant, as-of date/range, and that the control re-pulls live in claude.ai. Full field list and exact units: `references/metric-audit.md` §1. Full layout/build detail: `references/recipes.md` §1.

## Workflow

1. Resolve every index with `search_index_indexes` — never guess an MSCI index code; confirm name + code (and variant/currency) when more than one plausible match returns. For the Security tab, resolve the security with standard MSCI search (case-insensitive token/substring — "space" must return every match, not one row; no hard cap).
2. Resolve the as-of business date from the echoed `fetched_date` of a cheap probe call — never today's calendar date (`references/mcp-queries.md` §0b).
3. Pull, once per index: multi-period returns (`equity_index.performance.period_returns.{period,returns}`); constituents + identifiers + sector + country weights (`equity_index.constituents.closing_weight`, `.identifiers.{security_name,isin,RIC,ISO_country_symbol}`, `equity_index.sector_weight.{sector_name,gics_closing_weight}`, `equity_index.country_weight.{country_name,cty_closing_weight}`, large `page_size` — a small page truncates the breakdown too); `equity_index.description.nb_of_securities`. This one constituents pull feeds both tabs.
4. Add the in-scope factsheet extension (valuation/fundamentals, factor, ESG/climate) **only where `search_index_datapoints` confirms the catalog exposes it** for this index — omit anything not exposed, never compute a proxy. Methodology-sensitive risk metrics stay out of this tab (→ `dashboard-performance-risk`).
5. Build the artifact via `assets/assemble.py` (see this package's README section below) — never hand-author the header, footer, brand CSS or disclaimers; that chrome is shared and inherited automatically.
6. Validate before rendering (`references/metric-audit.md` § Validation): weight in [0,100]; top weight flagged if >~40%; sector Σ≈100 (±1); country Σ≈100 (±1.5); null return periods show "n/a", never zero.
7. Add one grounded interpretive callout per major section (standing rule 10) — every claim must trace to a value shown elsewhere on the same dashboard.

## Index tab

Performance (KPI cards YTD/1Y/3Y CAGR/5Y CAGR + full multi-period table + historical level chart) → Rankings (YTD/1Y, indexes null for a period omitted, not ranked zero) → Weights & concentration (top-10 constituents, sector weights, the **full** country breakdown sorted desc and scrollable — never a hard top-12 cap — cumulative top-10 weight, and a one-line concentration read; never compute effective-number-of-stocks, it isn't an MCP field) → in-scope factsheet metrics, each labelled with its `datapoint_id`.

## Security tab

Security header (name, ISIN, RIC, country, sector, MSCI security code) → detail KPIs (weight, FIF to 3dp, NOS where present, each labelled with source + as-of date) → cross-index membership table: Index · In index? · Weight (%) · Sector · Country, right-aligned numeric columns, tabular numerals, **"not a constituent" shown, never a dropped row** → licensed/thematic fields only when the connector actually returns them for this user, hidden entirely otherwise.

## Interpretation

- Never assume composition from an index's name — "World" or "Asia" in the name doesn't imply a specific country list; resolve and show the real breakdown.
- Weights are point-in-time and move with prices, corporate events, and reviews.
- A flat "not a constituent" result is a completely correct answer when the two selected indexes have disjoint country universes (e.g. World vs EM never overlap) — but it's the least informative pairing for demonstrating the Security tab's value, since no security could ever show a meaningful two-sided weight comparison there. When the goal is to show *how much a position's weight shifts* between two benchmarks (not just whether it's included), pick indexes that genuinely overlap (e.g. a global index and a regional/country subset of it).
- "Search which of ALL standard + custom indexes a security is in, over a date range" is a **deferred capability**, not supported by current IndexAI Insights (needs security↔index mapping) — say it's planned, never brute-force it by scanning indexes. The supported view is membership across the selected indexes only.

## Handoff

- Returns, factor tilts, or risk analytics for an index → `dashboard-performance-risk`.
- Carbon intensity, temperature alignment, or climate/ESG index-vs-parent → `dashboard-climate`.
- What changed at the last N reviews (additions/deletions/turnover) → `dashboard-changes`.
- Why a security is/isn't eligible, or the rule behind a weight cap → `dashboard-methodology`.
- Comparing composition across more than 2 indexes at once, all aligned → `dashboard-comparator`.
- A factor index's methodology input (Quality/Momentum/Dividend score beside weight) → `dashboard-fimd`.

## Guardrails

- Facts only — MCP-direct fields + simple arithmetic (sum, count, sort, min/max, average, %, % change, top-minus-bottom spread). Nothing else, no forward estimates, no dollar exposure unless AUM is supplied.
- When required inputs (which indexes, which security) are missing, ask the user to clarify before building rather than guessing.
- Render the full scope every time — a table the recipe says shows everything must actually show everything (page/scroll, don't silently sample).
- Every dashboard must build through `assets/assemble.py`. This package bundles everything needed to do so: `assets/{dashboard-shell.html, assemble.py, disclaimer-footer.html, disclaimer-notice.txt, refresh-snippet.html, logos/}` and `references/{brand.md, recipes.md, metric-audit.md, mcp-queries.md}`. Full build mechanics, the shared shell/brand/disclaimer stack, and the as-of/range control are documented in `references/recipes.md`'s "Shared conventions" section (self-contained in this package) — apply them exactly as written; do not re-derive or simplify them.
