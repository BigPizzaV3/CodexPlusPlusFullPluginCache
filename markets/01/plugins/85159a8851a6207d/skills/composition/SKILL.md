---
name: composition
description: >-
  Use this skill for what sits inside an MSCI index: constituents and holdings, constituent weights, top-N holdings, country/region/sector/industry breakdowns, constituent counts, index concentration, and whether a given security is a member of a named index. Trigger for "top 10 holdings", "sector breakdown", "country weights", "how many stocks are in it", "how much of X is Y", "which index holds this stock", even if the user never says MSCI.
---

# Index composition and constituents

Use the MSCI Index app to describe an index's internal structure at a stated date. Composition is a point-in-time snapshot: it answers what is in the index and at what weight, not how the index performed and not why the rule exists.

## Output

Lead with the requested rows or figure. Identify the index as `<name> (<msci_index_code>)` and state the fetched date. When a list is paginated, state how many rows are shown versus available. Never present a partial page as the full index.

## Workflow

1. Resolve the index with `search_index_indexes`. Never guess an MSCI index code. Resolve several independent indexes in parallel.
2. Discover the exact datapoints with `search_index_datapoints`. Do not compose ids from naming patterns. Typical search concepts:
   - constituents and constituent weights
   - constituent identifiers (ISIN, ticker, security code)
   - country, region, sector, and industry-group weights
   - number of securities / constituent count
   - adjusted and unadjusted market capitalisation
3. Prefer a **native breakdown datapoint** when discovery returns one. Sector, country, and industry-group weights are published, not derived — expect families such as `equity_index.sector_weight.*` (sector name, GICS closing weight, number of securities), `equity_index.country_weight.*`, and `equity_index.industry_group_weight.*`. Confirm the exact ids through discovery. Only aggregate constituent rows client-side when the catalog has no published breakdown, and say the figure was derived by aggregation.
4. These breakdowns are **list-cardinality but range-capable**. They paginate under `fetch_index_data`, and `fetch_index_timeseries` does serve them, returning `list_tables`. Respect the returned `range_window`: daily frequency is capped at roughly 30 days, so use `frequency=monthly` for longer histories rather than looping point-in-time calls.
5. Route on the returned flags: `supports_single_day=true` → `fetch_index_data`; `supports_range=true` with a date range → `fetch_index_timeseries`.
6. For top/bottom holdings, pass `order_by` (typically `closing_weight`) with `order_direction`, plus `page` and `page_size`. Do not sort a single page client-side and call it the top N of the index.
7. When requesting parallel list datapoints from the same dataset, keep rows aligned by the shared `msci_security_code` so weights stay paired with their own identifiers.
8. Read `strict_gate`, `range_window`, and `constraints.notes` before fetching.

## Membership questions

For "which index holds this security" or "is this stock in the index":

1. Resolve the security with `search_index_securities`. Do not infer a country filter from suffixes such as `(US)`, `ADR`, `CDI`, or `ADS`.
2. For a **named** index, confirm membership from that index's constituent list or from the documented membership/eligibility flag, and state which basis was used.
3. For an **open-ended** "which indexes hold this", there is no exhaustive reverse lookup across every MSCI index. There is a **bounded** one: the `security.index_inclusion_monitor.weight_in_*` family covers the major standard families (World, ACWI, ACWI IMI, EM, EM IMI, World IMI, EM Small Cap and siblings) and returns a per-family weight for a resolved security code. Use it for the major families, then say plainly that the answer covers those families and the indexes checked, not every MSCI index.
4. Inclusion-monitor data is published only for the latest applicable monitor (T+6). A requested date is pinned to that monitor date and the response says so — report the pinned date, not the date you asked for. Any value from this family carries a mandatory disclaimer in `constraints.notes`; reproduce it verbatim.

## Concentration

- Derive top-N concentration from returned weights, state N, and state the date.
- Say whether the weights are closing weights or another documented basis.
- Do not describe concentration as a risk measure. It is a weight statistic.

## Interpretation

- Never assume composition from an index name. An index containing "World" or "Asia" does not imply a country list.
- Index-level aggregates are not constituent medians.
- Weights are point-in-time and move with prices, corporate events, and reviews.
- Preserve units exactly as returned; if market cap arrives in USD millions, label it or convert with an explicit label.

## Handoff

- Performance, returns, valuation multiples, and factor scores → `benchmark`.
- Why a constituent qualifies, or the rule behind a weight cap → `methodology`.
- What changed at a review, or a proforma constituent list → `index-changes`.
- Comparing composition across several indexes → `compare`.

## Guardrails

- Never double-convert a weight. Check the datapoint description for the decimal-versus-percentage statement before formatting, and align with `benchmark`: weights format as percentages unless the description states the value is already a decimal fraction.
- Never guess an index code, a datapoint id, or a constituent list.
- Do not claim a complete constituent list when only one page was fetched, or when entitlements may have filtered the result.
- If a requested date snaps, report both the requested and fetched date.
- Absence of a security from a returned page is not proof it is not in the index.
