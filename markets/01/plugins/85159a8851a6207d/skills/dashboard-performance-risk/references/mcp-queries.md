# MCP Queries & Refresh Contract

All index data comes from the MSCI MCP via two tools: **`fetch_index_data`** (point-in-time, one `date`) and **`fetch_index_timeseries`** (a date range). Index/name resolution uses **`search_index_indexes`**; datapoint discovery uses **`search_index_datapoints`**. There is no GraphQL tool — the older `executeIndexGQLSchema` / `getIndex*` interface has been retired. Resolve codes live; never hardcode. Every datapoint ID below was verified against the live catalog and, where noted, against a live fetch.

## Tool call shape (both tools)

`fetch_index_data`:
```
codes:        ["990100"]                 // MSCI index code(s), resolved via search_index_indexes
datapoints:   ["equity_index.performance.period_returns.period", ...]
date:         "YYYYMMDD"                  // one business date
currency:     "USD"                       // default USD
variant:      "GRTR"                       // STRD | GRTR (default) | NETR
order_by / order_direction                 // for list datapoints (e.g. closing_weight desc)
page / page_size                            // list pagination (default page_size 10)
rebalance_target                            // "previous" (default) | "upcoming" | "proforma_start_date"
info_points:  { ... }                       // datapoint-specific hints (e.g. latest_date)
```

`fetch_index_timeseries`: same `codes` / `datapoints` / `currency` / `variant`, plus `start_date`, `end_date`, `frequency` ("daily" default | "monthly"). Only pass datapoints whose `supports_range=true`.

**Response shape (important for parsing).**
- `fetch_index_data` returns `{ requested_date, fetched_date, scalars, list_tables[] }`. `scalars` = `{ "NAME (code)": { datapoint_id: value } }`. Each `list_tables[]` entry is one (entity × list datapoint): `{ index_code, index_label, datapoint_id, date, pagination:{page,page_size,total_rows,total_pages}, table:{ columns:["date","value"], rows:[["YYYYMMDD", value], ...] } }`.
- `fetch_index_timeseries` returns `{ errors, table, list_tables? }`. `table` (scalar datapoints) = `{ columns:["date","{name} ({code}) {datapoint_id}"], rows:[...] }`. List datapoints arrive in `list_tables[]` as above.
- Parse by matching `datapoint_id` (data) — do not rely on array position. When several list datapoints are requested together with the same `order_by`, rows align across tables by position (top weight ↔ its ISIN ↔ its name).

## 0. Resolve the index code (always first)
Call `search_index_indexes(indexName: "<name>")`. Each hit carries `msci_index_code`, `index_name`, `official_brand_name`, `default_variant`, `default_currency`. Confirm name + code with the user when several plausible matches return.

## 0b. Resolve the latest business date (always, before pulling data)

Never hardcode a date or use today's calendar date. Fetch a cheap point-in-time datapoint and read the echoed `fetched_date`:
```
fetch_index_data(codes:["<code>"], datapoints:["equity_index.performance.period_returns.period"], date:"<a recent weekday YYYYMMDD>")
-> response.fetched_date   // the actual business date the feed served; use it as the shared as-of date
```
`fetched_date` may differ from `requested_date` (weekend/holiday snap). Use the returned `fetched_date` for every dashboard's as-of/calc date. The resolved date is shared across all dashboards.

## §1 — Index Composition Analyst

One dashboard, two tabs. The Index tab and Security tab share the per-index constituents/returns pulls below.

### Index tab

**Returns (per index), point-in-time** — two aligned list datapoints:
```
fetch_index_data(
  codes: ["<code>"], date: "<asof>", variant: "GRTR",
  datapoints: [
    "equity_index.performance.period_returns.period",   // "1D","1W","1M","3M","6M","MTD","QTD","YTD","1Y","3Y","5Y","7Y","10Y","15Y","20Y"
    "equity_index.performance.period_returns.returns"    // decimal fraction; ×100 to display
  ], page_size: 20
)
```
Periods ≤ 1Y are cumulative; periods > 1Y (3Y, 5Y, 7Y, 10Y, 15Y, 20Y) are **annualized CAGR** — label them. total_rows is 15; page_size 20 gets them all in one page. Some periods are **null** (show "n/a"). VERIFIED LIVE (World, 20250630): returns come back as decimals (0.168 = 16.8%).

**Constituents + identifiers + effective universe size** — aligned list datapoints, `closing_weight` desc:
```
fetch_index_data(
  codes: ["<code>"], date: "<asof>",
  datapoints: [
    "equity_index.constituents.closing_weight",              // PERCENT — display as-is (World NVIDIA ≈ 5.12 = 5.12%)
    "equity_index.constituents.identifiers.security_name",
    "equity_index.constituents.identifiers.isin",
    "equity_index.constituents.identifiers.RIC",             // best-effort ticker; may be blank
    "equity_index.constituents.identifiers.ISO_country_symbol"
  ],
  order_by: "closing_weight", order_direction: "desc",
  page_size: 2000                                            // avoid truncation; pagination block reports total_rows
)
```
`nb_of_securities` (index size) is a separate scalar: `equity_index.description.nb_of_securities` (STRD-gated — fetch with `variant:"STRD"`).

**Sector weights** (aligned list pair):
```
datapoints: ["equity_index.sector_weight.sector_name", "equity_index.sector_weight.gics_closing_weight"]  // weight PERCENT, as-is; total_rows ≈ 11
```
**Country weights** (aligned list pair):
```
datapoints: ["equity_index.country_weight.country_name", "equity_index.country_weight.cty_closing_weight"]  // weight PERCENT, as-is
```
VERIFIED LIVE: sector weights (Info Tech ≈ 11.39) and country weights (Canada ≈ 3.20, Austria ≈ 0.05) are already percent — display as-is, never ×100.

**Historical index level (Performance tab, over the selected range):** `fetch_index_timeseries(codes:["<code>"], start_date:"<START>", end_date:"<END>", variant:"GRTR", currency, datapoints:["<index-level datapoint that supports range>"], frequency:"daily")`. `<START>`/`<END>` are filled by the as-of + range control. Only request datapoints whose `supports_range=true`.

**In-scope factsheet fields:** discover with `search_index_datapoints` at build time and pull only those that exist (valuation/fundamentals, factor, ESG/climate). Respect each datapoint's catalog unit. Omit anything not exposed — do not compute a proxy. No methodology-sensitive risk metrics.

### Security tab

A single security in depth, and its membership across a **user-selected** set of indexes. Facts only.

**1) Resolve the security (standard MSCI search).** Match name/RIC/ISIN with case-insensitive token/substring search (so "space" returns every match, not one). Read `equity_index.constituents.description.msci_security_code` for the resolved code and reuse it.

**2) Per selected index — detail + membership:**
```
fetch_index_data(
  codes: ["<index_code>"], date: "<asof>",
  datapoints: [
    "equity_index.constituents.closing_weight",              // PERCENT — this security's weight in the index
    "equity_index.constituents.identifiers.security_name",
    "equity_index.constituents.identifiers.isin",
    "equity_index.constituents.identifiers.RIC",
    "equity_index.constituents.identifiers.ISO_country_symbol",
    "equity_index.constituents.description.msci_security_code"
    // + current_fif / current_eod_nos where the constituents datapoint exposes them
  ],
  order_by: "closing_weight", order_direction: "desc", page_size: 2000
)
```
Match the resolved security code in the returned rows; if absent, mark "not a constituent" (do not drop the row). Join `equity_index.sector_weight.*` / `country_weight.*` for context if shown.

**3) Licensed / thematic fields (entitled only).** If the connector exposes proprietary datapoints (e.g. thematic scores) for this user, discover them via `search_index_datapoints`, pull, and show them in a clearly-labelled licensed section. If nothing is returned, hide the section — never fabricate.

**Deferred (not supported today):** "which of ALL standard + custom indexes is this security in, over a date range." IndexAI Insights has no security→index reverse mapping yet; document it as coming and do NOT brute-force scan indexes. The supported view is membership across the **user-selected** indexes above.


## §2 — Index Performance & Risk Analyst

**In-shell (MCP-direct — same tools as everywhere else).**

Returns (same call as §1's Index tab):
```
fetch_index_data(codes:["<code>"], date:"<asof>", variant:"GRTR",
  datapoints:["equity_index.performance.period_returns.period","equity_index.performance.period_returns.returns"],
  page_size:20)
```

Factor (FaCS) tilts — scalar, EOM-only, relative to MSCI ACWI IMI:
```
fetch_index_data(codes:["<code>"], date:"<asof (EOM)>",
  datapoints:["equity_index.facs_ratios.value","equity_index.facs_ratios.quality","equity_index.facs_ratios.momentum",
              "equity_index.facs_ratios.size","equity_index.facs_ratios.volatility","equity_index.facs_ratios.liquidity",
              "equity_index.facs_ratios.growth","equity_index.facs_ratios.divyield"])
```

Historical level (for the chart, over the selected range):
```
fetch_index_timeseries(codes:["<code>"], start_date:"<START>", end_date:"<END>", frequency:"daily",
  datapoints:["<index-level datapoint that supports range>"])
```

**Native IMX chart (a different tool — `calculate_metrics`, NOT `fetch_index_data`).** Discover the exact mnemonic set with `search_index_datapoints` at build time (the `imx` result block); the ones verified live are `key_metrics`, `key_risk_metrics`, `index_tracking_error`, `index_sharpe_ratio`, `index_information_ratio`, `active_risk_attribution_group_breakdown`, `risk_attribution_group_breakdown`, `active_risk_contributing_constituents`, `total_risk_contributing_constituents`. Call `calculate_metrics` with the resolved index code and, for any relative metric, a `benchmark_portfolio` — without one, relative metrics (tracking error, information ratio, active drawdown, active-risk attribution) return **null**, not zero. `calculate_metrics` renders its own interactive chart; do not parse its output and re-plot it in the dashboard's inline SVG. IMX is present only when index IMX tools are enabled on the connection, and covers **equity indexes only** — verify before use, and if unavailable, say risk analytics aren't available on this connection rather than approximating.

## §3 — Sustainability & Climate Index Analyst

WACI — index vs parent. **VERIFIED LIVE:** `equity.sustainability_factor.input.index.{waci_index,waci_parent}` is a **FIMD-scoped** pair (returns null for a non-FIMD index — confirmed against World Climate Paris Aligned PAB, 735619) and only applies to factor indexes in `data/fimd-indexes.txt`. For the normal "compare index X to index Y" ask, pull the WACI field for **each code separately** and compare — this is what actually populates for climate/PAB-style indexes:
```
fetch_index_data(codes:["<code>","<parent_or_comparison_code>"], date:"<asof (EOM)>",
  datapoints:["equity_index.esg_metrics_additional.wtd_avg_carbon_intensity_by_sales_scope_1_2_3",
              "equity_index.esg_metrics_additional.coverage_weighted_average_carbon_intensity_scope_1_2_3"])
```
VERIFIED LIVE (20260731, USD): MSCI World (990100) ≈ 875.3 tCO2e/$M sales (coverage 99.5%); MSCI World Climate Paris Aligned PAB (735619) ≈ 354.2 (coverage 99.5%). `equity_index.esg_metrics.index_wgt_avg_carbon_intensity` returns **null** for both — do not use it as the primary field; `index_wgt_avg_carbon_intensity_sc2` (Scope 1+2 only) does populate (World ≈ 94.5, PAB ≈ 33.4) and is fine as a secondary context figure. Only fetch the FIMD `waci_index`/`waci_parent` pair when the index is confirmed FIMD-eligible (§7).

Implied Temperature Rise (with its coverage field — always report together, standing rule 8):
```
fetch_index_data(codes:["<code>"], date:"<asof (EOM)>",
  datapoints:["equity_index.esg_metrics.implied_temperature_rise","equity_index.esg_metrics.cov_implied_temperature_rise"])
```

Climate VaR (aggregate + coverage):
```
fetch_index_data(codes:["<code>"], date:"<asof (EOM)>",
  datapoints:["equity_index.esg_metrics.total_var",
              "equity_index.esg_metrics_additional.coverage_climate_var_physical_risk",
              "equity_index.esg_metrics_additional.coverage_climate_var_policy_risk"])
```

EU BMR alignment fields:
```
fetch_index_data(codes:["<code>"], date:"<asof (EOM)>",
  datapoints:["equity_index.esg_metrics.climate_aligned","equity_index.esg_metrics.benchmark_investable_overlap",
              "equity_index.sfdr_metrics.eu_sust_invst_scrn_wt_sm"])
```
VERIFIED LIVE (20260731): MSCI World (990100) `climate_aligned:false`, `benchmark_investable_overlap:null` (not a regulated EU BMR disclosure index — null here is the correct answer, not a missing-data error); MSCI World Climate Paris Aligned PAB (735619) `climate_aligned:true`, `benchmark_investable_overlap:43.0%` (this IS the Art. 1(e) PAB investable-universe overlap figure). `eu_sust_invst_scrn_wt_sm` returned null for both at this date — treat a null there as "not disclosed for this index," not a fetch error.

All these are EOM-only (`availability: EndOfMonthBusinessDate`) — pass any date in the target month; it snaps to the 2nd business day, same convention as FIMD (§7). Do not intraday-refresh these fields; the as-of control still resolves to the latest published month.

## §4 — Index Changes Analyst

**1) Review effective dates (recursive).** Start at the latest business date; step back to get earlier reviews:
```
fetch_index_data(codes:["<code>"], variant:"STRD", date:"<cd>",
  datapoints:["equity_index.master_description.last_rebalancing_date",
              "equity_index.master_description.next_rebalancing_date",
              "equity_index.master_description.future_days"])
-> read scalars["NAME (code)"]["equity_index.master_description.last_rebalancing_date"] = T
   then set cd = (T − 1 business day) and repeat for the prior review.
```
(`last_rebalancing_date` / `next_rebalancing_date` / `future_days` are scalars, STRD-gated, standard_family.)

**2) Per review effective date T (T1 = T − 1 business day).** Three separate `fetch_index_data` calls (these are different date/target combinations, so they are separate calls, not one document):

PRE composition at T1:
```
fetch_index_data(codes:["<code>"], date:"<T1>",
  datapoints:["equity_index.constituents.closing_weight",             // PERCENT
              "equity_index.constituents.identifiers.security_name",
              "equity_index.constituents.description.msci_security_code"],
  order_by:"closing_weight", order_direction:"desc", page_size:2000)
// nb_of_securities (index size) at T1 via equity_index.description.nb_of_securities (variant STRD)
```

REVIEW changes at T (completed rebalance → rebalance_target "previous"):
```
fetch_index_data(codes:["<code>"], date:"<T>", rebalance_target:"previous",
  datapoints:["equity_index.review_change_counts.nb_of_additions",
              "equity_index.review_change_counts.nb_of_deletions",
              "equity_index.review_change_counts.nb_of_fif_changes",
              "equity_index.additions.msci_security_code",           // list of ADDED codes
              "equity_index.deletions.msci_security_code",           // list of DELETED codes
              "equity_index.proforma_constituents.initial_weight"])  // post-review target weight — DECIMAL → ×100
```
Set `date = last_rebalancing_date` (T). If the chosen date is outside MSCI's live review/disclosure window the review-change datapoints come back empty; relay `outsideRebalWindow.message` verbatim when present.

POST size at T: `equity_index.description.nb_of_securities` at T (variant STRD) = N(Post-review).

**Two-step name resolution (REQUIRED — changed from the old interface).** `additions`/`deletions` return bare `msci_security_code` values with NO names. To get names, make a SECOND `fetch_index_data` whose `codes[]` are those security codes (batched) and datapoints `security.description.security_name` (and optionally `security.description.ISO_country_symbol`), reusing the same `date`. Do NOT mix index and security codes in one call.

**3) Official index turnover — range-only now.** `total_index_turnover` no longer supports a single day:
```
fetch_index_timeseries(codes:["<code>"], start_date:"<T>", end_date:"<T>", currency:"USD", variant:"GRTR",
  datapoints:["equity_index.performance.total_index_turnover"])
```
VERIFIED LIVE: value is a **fraction** (0.000958 = 0.0958%) → ×100 to display. The catalog docstring's "already percent" claim is wrong; trust the ×100 rule (and `metric-audit.md`). `start=end=T` isolates the review-day turnover. The returned `date` cell may be blank on the aggregate — that is expected. (Whether MSCI reports this one-way vs two-way is a display convention documented in `metric-audit.md`/`recipes.md` §4; the value and ×100 unit are what is verified here.)

**4) Refresh (detect a newer review only):**
```
fetch_index_data(codes:["<code>"], variant:"STRD", date:"<latest business date>",
  datapoints:["equity_index.master_description.last_rebalancing_date"])
```

---

## §5 — Index Methodology Analyst

**1) Resolve the security.** `search_index_securities(query:"<name/ticker/ISIN>")` → `msci_security_code`.

**2) Eligibility screen** (against a reference index code, or an Inclusion Module entity name):
```
fetch_index_data(codes:["<msci_security_code>"], date:"<asof>",
  datapoints:["security.index_inclusion_monitor.index_eligible_fg",
              "security.index_inclusion_monitor.current_index_mcap_musd"])
```
For module-level / country-filtered lists instead of a single security, pass a module entity name and a country filter:
```
fetch_index_data(codes:["IIM GLOBAL"], date:"<asof>", info_points:{country_code:"US"},
  datapoints:["security.index_inclusion_monitor.index_eligible_fg"])
```
Numeric security codes ignore `info_points.country_code` and return a single-security row.

**3) Component flags (pull alongside the roll-up, always — needed to explain any failure):**
```
datapoints: ["security.index_inclusion_monitor.size_segment_fg",
             "security.index_inclusion_monitor.minimum_free_float_market_capitalization_fg",
             "security.index_inclusion_monitor.minimum_foreign_inclusion_factor_flag",
             "security.index_inclusion_monitor.foreign_room_flag",
             "security.index_inclusion_monitor.atvr_12m_fg", "security.index_inclusion_monitor.atvr_3m_fg",
             "security.index_inclusion_monitor.fot_12m_fg", "security.index_inclusion_monitor.fot_3m_fg",
             "security.index_inclusion_monitor.china_a_share_with_connect_line"]
```
(Discover exact sibling IDs with `search_index_datapoints` — the namespace above is the one verified live; confirm before relying on it for a new field.) Read every flag that is False/"Not Met" and attribute the failure to all of them, not just the first.

**Mandatory disclaimer (do not skip).** This datapoint's own `constraints.notes` carries a 9-point disclaimer block that `fetch_index_data` does NOT inject automatically. Copy it verbatim into `assemble()`'s `extra_disclaimers` whenever step 2/3 is shown.

**4) Methodology rules (capping/buffer/country classification):**
```
search_index_methodology_stack(indexCode:"<code>", query:"capping rules" | "buffer zone migration" | "country classification")
```
Cite the returned `methodology_name` + snippet. If `hits` is empty, prefix the answer with the tool's own mandated fallback note rather than answering from memory unlabeled.

## §6 — Index Comparator

No new tool calls — reuses §1 and §2 exactly, once per selected index (2-5), with the same `date`/`currency`/`variant` args on every call:
```
// per index i in the selected set, same asof/currency/variant for all:
fetch_index_data(codes:["<code_i>"], date:"<asof>", currency:"<shared>", variant:"<shared>",
  datapoints:[ /* §1 composition fields and/or §2 performance fields, per the requested dimension */ ])
```
For a risk comparison, call `calculate_metrics` once per index, optionally with one selected index passed as every other call's `benchmark_portfolio` for an explicit active view. If the user hasn't specified currency/variant/date, ask once before issuing any of the per-index calls — do not let each index resolve its own default and silently mismatch.

## §7 — Factor Index Methodology Data (FIMD)

FIMD uses the namespace `equity.sustainability_factor.input.security.*`. The table is the index's **holdings, descending by weight**, with the single composite **factor score joined beside each holding's weight**. Exactly four displayed columns: **Security · MSCI code · Weight % · Factor** — Weight from the constituents dataset, Factor from the FIMD dataset.

**Q0 — Eligibility (code list + live probe).** Require the code in `data/fimd-indexes.txt` (the vetted FIMD eligibility list, 289 codes), then:
```
fetch_index_data(codes:["<code>"], date:"<any date in the target month>",
  datapoints:["equity.sustainability_factor.input.security.msci_security_code"])
```
`list_tables[].pagination.total_rows > 0` → eligible (`total_rows` = parent-universe size). Empty / `error` → not available for that index/date.

**Q1 — Index holdings by weight (join target).**
```
fetch_index_data(codes:["<code>"], date:"<as-of>", order_by:"closing_weight", order_direction:"desc",
  page_size:2000, variant:"STRD",
  datapoints:["equity_index.constituents.closing_weight",
              "equity_index.constituents.identifiers.security_name",
              "equity_index.constituents.description.msci_security_code"])
```
The index's holdings with weight + name + code, largest first. (Constituents carry names, so no two-step needed here.) Factor-index parents are small (e.g. EAFE Quality ≈ 690 names), so all constituents join and render; for an unusually large parent, default the table to the top 100 by weight and page the rest.

**Q2 — FIMD factor map (join source).** Rebalance (T-9, default) uses `.rebalancing` ids after resolving the date; Month-end uses bare ids (2nd-business-day snap). Pull only the **single composite score** for the index's family plus the map's own `msci_security_code`.
```
# Rebalance: step 1 — resolve date (next_rebalancing_date if non-null else last_rebalancing_date)
fetch_index_data(codes:["<code>"], variant:"STRD", date:"<probe>",
  datapoints:["equity_index.master_description.last_rebalancing_date",
              "equity_index.master_description.next_rebalancing_date"])
# Rebalance: step 2 — server resolves T-9 (e.g. 20260701 -> calc 20260618)
fetch_index_data(codes:["<code>"], date:"<resolved rebalancing date>", variant:"STRD", page_size:800,
  datapoints:["equity.sustainability_factor.input.security.msci_security_code.rebalancing",
              "equity.sustainability_factor.input.security.<composite_score>.rebalancing"])
# Month-end (bare ids; date snaps to the 2nd business day, e.g. 20260401 -> 20260402):
fetch_index_data(codes:["<code>"], date:"20260401", variant:"STRD", page_size:800,
  datapoints:["equity.sustainability_factor.input.security.msci_security_code",
              "equity.sustainability_factor.input.security.<composite_score>"])
```
The input is **index-scoped — it CANNOT be fetched per security code** (passing security codes returns `"No Data available for the given input index <code>"`, verified). So pull the map for the index and **join client-side by `msci_security_code`** to the holdings from Q1. The map is a single call at load.

**Q3 — Render.** Join Q1 × Q2 on the security code; render the holdings **descending by weight** — `Security · MSCI code · Weight % · Factor`, the **Factor column highlighted** as the key metric. A blank Factor cell (unrated / not-mapped) shows "n/a", never zero. Do NOT add descriptor columns.

**FIMD composite-score field** (choose by family; confirm via `search_index_methodology_stack`): Quality → `quality_score`; Momentum → `momentum_score` / `composite_momentum_score`; High Dividend Yield → `composite_dividend_score`. Label the Factor column for the family (e.g. "Quality Score"). The descriptor fields (`return_on_equity`, `debt_to_equity`, `earnings_variability`, momentum z-scores) feed the score but are **not pulled as displayed columns** — cite them only in the "rules that matter" panel.

**Notes.**
- Discover the exact composite-score id with `search_index_datapoints`; confirm the index's factor via `search_index_methodology_stack`.
- `order_by` `closing_weight` on Q1 sorts the holdings; the composite score is dense for factor indexes, so the join is clean.
- Match forms: `.rebalancing` value id ⇢ `.rebalancing` `msci_security_code`; bare ⇢ bare.
- Two datasets, one join key: the constituents `...description.msci_security_code` (Q1) and the FIMD-input `...security.msci_security_code` (Q2) are the SAME MSCI security codes — join on the code VALUE. Inside the FIMD-input fetch, co-request its OWN `...msci_security_code` (not the constituents one).

## Refresh contract — as-of / control, self-sufficient on claude.ai

The control is an **as-of date picker + range selector** (with a "Latest" toggle), not a bare one-click refresh. "Latest" resolves the latest served business date live (§0b); unticking it uses the picked date. The selected range sets `<START>`; the as-of date fills `<DATE>` and `<END>`. It uses the claude.ai/Desktop artifact runtime's built-in Claude bridge to reach the MSCI MCP. The artifact `fetch`es the Anthropic Messages API with the MSCI MCP attached as `mcp_servers`, and the response carries `mcp_tool_use` + `mcp_tool_result` blocks from the live MCP. It needs **no API key, no external server, and no separate service**; the platform injects auth. In testing the connector that serves these tools is **MSCI MCP** (`https://mcp.msci.com/mcp/v1.0/mcp`); attach whichever connected MCP exposes `fetch_index_data` / `search_index_indexes` (the snippet tries known URLs in order). Full code in `assets/refresh-snippet.html`. Contract:

1. Hold the dashboard's call set (array of `{ key, tool, args }`, where `tool` is `fetch_index_data` or `fetch_index_timeseries` and `args` is that tool's input object) in the artifact. On update, resolve the as-of date (the picked date, or — with "Latest" ticked — the served `fetched_date` per §0b), compute the range start from that date and the selected range, then fill each call's args: `<DATE>` and `<END>` = as-of date, `<START>` = range start. Run the calls at those dates.
2. On click, for each entry, call the platform bridge (artifact `fetch` to the Messages endpoint with the MSCI MCP attached as `mcp_servers`), instructing it to run that tool with those args and return JSON only.
3. Parse the response by block **type**: collect `mcp_tool_result` blocks, `JSON.parse` their text; ignore `text`/`mcp_tool_use` blocks for data. Then read `scalars` / `list_tables` (or `table`) as above, matching by `datapoint_id`.
4. Re-render from the parsed data, recompute only the approved simple transformations, update the "as-of" stamp, clear old warnings. On failure keep the last-loaded snapshot and show a visible note. Show a spinner (the round-trip can take 60–120s).

Build the dashboard **data-driven** (a JS data object + a `render()` function) so the handler can swap in the refreshed data and re-render every view in place. A copy opened as a bare file outside the Claude runtime cannot reach the MCP; the dashboard states this so the fallback is expected, not a bug.

---
