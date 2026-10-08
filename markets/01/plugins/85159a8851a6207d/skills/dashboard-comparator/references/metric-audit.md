# Approved Metric Specification

Authoritative, closed list of what each dashboard may show, the exact IndexAI Insights MCP field that supplies it, and the unit/interpretation rule. A value not specified here is not shown unless the user explicitly insists, in which case the approximation disclaimer mechanism applies (see end).

Active dashboards: **§1 Index Composition Analyst** (Index tab + Security tab), **§2 Index Performance & Risk Analyst**, **§3 Sustainability & Climate Index Analyst**, **§4 Index Changes Analyst**, **§5 Index Methodology Analyst**, **§6 Index Comparator**, and **§7 Factor Index Methodology Data (FIMD)**.

## Standing rules

1. **MCP-only, or simple arithmetic on MCP fields.** Allowed transformations: sum, count, sort/rank, min/max, arithmetic average, percentage, percentage change, top-minus-bottom spread. Nothing else.
2. **No ad hoc methodology-sensitive analytics.** Tracking error, Sharpe, Sortino, Jensen's alpha, beta, information ratio, correlation, realized/rolling volatility, standard-deviation dispersion, max drawdown each have multiple defensible calculation conventions — this skill never derives them with its own arithmetic. They are NOT wholesale unavailable, though: MSCI computes them itself as **IMX analytics** (`calculate_metrics`, equity indexes only) and §2 surfaces them there, rendered as MSCI's own interactive chart rather than recreated inside the dashboard shell (the tool's own description says not to rebuild its output as a table or ASCII chart). Relative IMX metrics (tracking error, information ratio, active drawdown, active-risk attribution) return **null without a `benchmark_portfolio`** — never read a blank as zero active risk.
3. **No forward estimates.** No estimated post-event weights, prices, or index impacts.
4. **No external data** unless the user supplies it as an explicit custom-extension input.
5. **Flag abnormal values; never silently suppress or "fix" them.**
6. **Licensed/proprietary fields** (e.g. thematic scores) may be shown ONLY when the connector returns them for an entitled user — never fabricated.
7. **Datapoint-mandated disclaimers are separate from the standard footer and must be carried verbatim.** Some datapoints (e.g. `security.index_inclusion_monitor.*`, used by §5) specify their own mandatory disclaimer block in `constraints.notes` that `fetch_index_data` does NOT inject automatically. When such a datapoint is used, pass its exact text through `assemble()`'s `extra_disclaimers` parameter — never paraphrase or omit it, and never conflate it with the approximation disclaimer (rule 2's exemption does not exempt this).
8. **Coverage fields travel with the metric they describe.** Sustainability/climate metrics that carry a paired `cov_*` (coverage) field — e.g. `esg_metrics.implied_temperature_rise` alongside `esg_metrics.cov_implied_temperature_rise` — must show that coverage percentage next to the metric, not as an afterthought; a headline climate number without its coverage is misleading when coverage is low.
9. **Render the full scope each recipe specifies — never silently sample or truncate.** When a recipe states a count or scope ("last N=5 reviews," "all listed IMX risk categories," "render all constituents for a small parent"), that is a floor, not a suggestion, regardless of how many MCP calls or how much build time it takes. The only acceptable truncation is one a recipe itself states as an explicit fallback (§7 FIMD's top-100-by-weight fallback for an unusually large parent universe; §4's 1pp weight-change cutoff, which is itself user-adjustable and expandable to "show all"). A field the connector genuinely doesn't expose is omitted **visibly** — say so on the dashboard face — never dropped silently to save build time. Truncating a section the recipe describes as complete (e.g. showing 12 of a ~690-name FIMD universe, or 1 of the last 5 reviews) is a spec violation, not a reasonable shortcut.
10. **Every dashboard carries grounded commentary, not just raw numbers.** Each major section gets a short interpretive callout — the difference between a data dump and an analyst briefing (e.g. "PAB's Climate VaR of −2.6% vs World's −15.1% implies materially lower modelled downside"). Every claim in it must trace to a specific value shown elsewhere on the *same* dashboard; never introduce an external fact, forecast, or opinion that isn't derivable from the pulled data. This is interpretation of real numbers, not a new derived metric, so it does not trigger the approximation disclaimer (rule 2) — but a fabricated or unsourced claim is never acceptable regardless of that exemption.

## Units — verified against the live endpoint (do not trust docstrings)

| Field | Source | Actual unit | Rule |
|---|---|---|---|
| `equity_index.constituents.closing_weight` | constituents | **percent** | display as-is (World NVIDIA ≈ 5.12 = 5.12%) — VERIFIED LIVE |
| `equity_index.sector_weight.gics_closing_weight` | sector | **percent** | display as-is; Σ ≈ 100 — VERIFIED LIVE |
| `equity_index.country_weight.cty_closing_weight` | country | **percent** | display as-is; Σ ≈ 100 — VERIFIED LIVE (small values are genuinely small) |
| `new_fif`, `current_fif` | constituents | **decimal 0–1** | show to 3 dp |
| index returns (`equity_index.performance.period_returns.returns`) | performance | **decimal fraction** | ×100 for display; 3Y+ annualized (CAGR) — VERIFIED LIVE |
| `equity_index.performance.total_index_turnover` | performance (range-only) | **fraction** | ×100 for display (docstring's "already percent" is WRONG) — VERIFIED LIVE 0.000958 = 0.0958% |

Weight robustness guard: read the largest weight; if > 1 the array is percent (display as-is), if ≤ 1 it is decimal (×100 for display). Sanity-check Σ ≈ 100 (percent) or ≈ 1 (decimal); flag impossible sums rather than rescaling twice.

Security `RETURNS` de-duplication: the array repeats periods across `LOC`/`USD`. Keep one value per (`CALC_DATE`, `period`, `ISO_currency_symbol`); prefer the requested currency.

Date-boundary guard: use valid MCP calc dates, not raw calendar month-ends; if a requested date is a weekend/holiday use the nearest prior date the query actually returns.

---

## §1 — Index Composition Analyst

One dashboard, two tabs. Both tabs draw on the same per-index constituents/returns pulls.

### Index tab (verified fields)

| Metric | MCP source | Notes |
|---|---|---|
| Multi-period returns (1D…20Y, YTD, MTD, QTD) | `fetch_index_data` → `equity_index.performance.period_returns.period` + `.returns` (aligned lists) | decimal; 3Y+ annualized (CAGR), label it; a period may be **null** — show "n/a" |
| YTD / 1Y rankings | sort the direct return fields across selected indexes | indexes null for the period are omitted, not ranked 0 |
| Top-N constituents + weight | `fetch_index_data` → `equity_index.constituents.closing_weight`, `order_by:closing_weight desc` | percent, as-is |
| Identifiers (name, RIC, ISIN, country) | `equity_index.constituents.identifiers.{security_name,RIC,isin,ISO_country_symbol}` | RIC best-effort, may be blank |
| Cumulative top-N weight | running sum of displayed weights | after the scale guard |
| Sector weights | `equity_index.sector_weight.sector_name` + `.gics_closing_weight` | percent; **large `page_size`** |
| Country weights (FULL breakdown) | `equity_index.country_weight.country_name` + `.cty_closing_weight` | percent; large `page_size`. **Show the full list (sorted desc, scrollable) — the old hard top-12 cap is removed**; you may still highlight the top N |
| Index size | `equity_index.description.nb_of_securities` (scalar, `variant:STRD`) | universe count |
| Historical time series (index level) | `fetch_index_timeseries` → index level over the selected `<START>`–`<END>` range | for the Performance section chart, where the datapoint supports range |
| Dollar exposure | — | DROP unless the user supplies AUM |
| Buy/sell signal, recommendation | — | DROP, not an MCP field |

**In-scope factsheet extension (discover — do NOT assume field IDs).** To align with the factsheet, additionally show the *in-scope* factsheet metrics — valuation & fundamentals, factor exposures, ESG & climate — **only where the catalog actually exposes them**. Discover the exact datapoints with `search_index_datapoints` at build time, apply the standing rules (MCP-direct or simple arithmetic; correct units from the catalog), label each metric with its `datapoint_id`, and **omit anything not exposed** rather than computing a proxy. Do not include methodology-sensitive risk metrics here — those stay deferred (Standing rule 2). This is deliberately "in-scope factsheet metrics", not "every factsheet metric".

### Security tab

Security-level detail plus cross-index membership over the **selected** set of indexes. Facts only.

| Metric | MCP source | Notes |
|---|---|---|
| Resolved security identifiers | standard MSCI search → `equity_index.constituents.identifiers.{security_name,isin,RIC,ISO_country_symbol}`, `equity_index.constituents.description.msci_security_code` | resolve once (case-insensitive token/substring; no 80-row cap); reuse the code |
| Weight in an index | `equity_index.constituents.closing_weight` (matched to the security) per selected index | percent, as-is |
| FIF | `current_fif` (constituents where exposed) | decimal 0–1, 3 dp |
| NOS | `current_eod_nos` where exposed | integer; show only if present |
| Sector / country context | `equity_index.sector_weight.*` / `country_weight.*` joined for context | percent |
| Cross-index membership (selected indexes) | for each selected index, is the security a constituent + its weight | table; "not a constituent" when absent — do not drop the row |
| Licensed / thematic fields | proprietary datapoints (e.g. thematic scores) **only when the connector returns them for an entitled user** | hide the section entirely if not returned; never fabricate |
| Membership across ALL standard+custom indexes + date range | — | **DEFERRED — not supported by current IndexAI Insights** (needs security↔index mapping). Document as coming; do NOT brute-force it |
| Estimated post-event weight / any forward value | — | DROP — forward estimate, not an MCP value |

## §2 — Index Performance & Risk Analyst

Two distinct sources feed this dashboard — keep them visually and mechanically separate (standing rule 2).

### In-shell (MCP-direct, `fetch_index_data`/`fetch_index_timeseries`)

| Metric | MCP source | Notes |
|---|---|---|
| Multi-period returns (1D…20Y, YTD, MTD, QTD) | `equity_index.performance.period_returns.period` + `.returns` | decimal; 3Y+ annualized (CAGR); null periods show "n/a" |
| Factor (FaCS) tilts | `equity_index.facs_ratios.{value,quality,momentum,size,volatility,liquidity,growth,divyield}` | dimensionless exposure relative to MSCI ACWI IMI; EOM only |
| Dividend yield | `equity_index.performance.yield` (STRD+USD only; else `equity_index.ratios.monthly_yield`) | percent; respect the `strict_gate` |
| Historical index level | `fetch_index_timeseries` over the selected range | for the performance chart, where `supports_range=true` |

### Native IMX chart (called out, not recreated)

| Metric | `imx` mnemonic | Notes |
|---|---|---|
| Key risk metrics (total risk, downside risk, Sortino, VaR/CVaR 95/99, max drawdown, skewness, kurtosis) | `key_risk_metrics` | absolute risk; monthly returns, 36+ months recommended |
| Tracking error | `index_tracking_error` | **requires `benchmark_portfolio`** — null without one |
| Sharpe ratio | `index_sharpe_ratio` | no benchmark required |
| Information ratio | `index_information_ratio` | **requires benchmark** |
| Key metrics (return, risk, Sharpe, information ratio, active return, tracking error, beta, turnover, valuation) | `key_metrics` | composite summary table |
| Active-risk attribution (Market/Industries/Countries/Styles/Currencies/Specific) | `active_risk_attribution_group_breakdown`, `risk_attribution_group_breakdown` | **requires benchmark** for the active variant |
| Active/total risk contributors (constituents) | `active_risk_contributing_constituents`, `total_risk_contributing_constituents` | top/bottom contributors |

Call `calculate_metrics` with the mnemonics above; render its output as its own interactive chart alongside the dashboard body — never parse its numbers back into the shell's inline-SVG renderer. Equity indexes only; do not use for fixed income or hedged indexes. When a relative metric is requested without a benchmark, state that a benchmark is required rather than showing a blank as zero.

**Completeness (standing rule 9 applies here specifically).** The Risk Analytics panel must attempt *every* category listed in the table above — absolute risk (`key_risk_metrics`), tracking error, Sharpe, information ratio, the composite `key_metrics` table, both risk-attribution breakdowns, and both risk-contributor grids — not an arbitrary subset of one or two. A category that genuinely needs a benchmark the user didn't supply is labeled "requires a benchmark" rather than omitted from the panel; a category that errors is labeled with the error, not silently dropped. Showing only tracking error and Sharpe while leaving out VaR/CVaR, drawdown, and attribution is exactly the kind of silent scope-cut standing rule 9 forbids.

## §3 — Sustainability & Climate Index Analyst

Framed around **index vs parent** wherever the connector exposes a parent-index variant, per the standing "index vs parent" ask.

| Metric | MCP source | Notes |
|---|---|---|
| WACI (weighted avg carbon intensity by sales, Scope 1+2+3) | `equity_index.esg_metrics_additional.wtd_avg_carbon_intensity_by_sales_scope_1_2_3` (+ its `coverage_weighted_average_carbon_intensity_scope_1_2_3` coverage) | tCO2e/USD million sales; EOM (2nd business day) — **VERIFIED LIVE** (MSCI World 990100 ≈ 875.3, coverage ≈ 99.5%); `equity_index.esg_metrics.index_wgt_avg_carbon_intensity` returns **null** for standard indexes — do not rely on it |
| WACI — Scope 1+2 only (context) | `equity_index.esg_metrics.index_wgt_avg_carbon_intensity_sc2` | scalar — VERIFIED LIVE (World ≈ 94.5) |
| WACI — index vs parent (**FIMD-scoped only**) | `equity.sustainability_factor.input.index.{waci_index,waci_parent}` | **VERIFIED LIVE returns null for a non-FIMD index** (e.g. World Climate Paris Aligned PAB, 735619) — this pair is SIMD/FIMD methodology-input transparency for factor indexes (`data/fimd-indexes.txt`), NOT a general index-vs-parent mechanism. For the standard "how does index X compare to index Y" ask, pull the WACI field above for **both index codes separately** and compare — that is what actually populates for climate/PAB-style indexes |
| WACI (SFDR PAI 3, EUR) | `equity_index.sfdr_metrics.waci_eur` | scalar, EOM |
| Implied Temperature Rise | `equity_index.esg_metrics.implied_temperature_rise` (+ `equity_index.esg_metrics.cov_implied_temperature_rise` coverage) | °C; a modelled forward alignment estimate — never converts to/from a carbon-intensity number; always show its coverage field alongside it (standing rule 8) |
| Climate VaR (aggregate) | `equity_index.esg_metrics.total_var` | 1.5°C-scenario aggregate of policy/physical/tech-opportunity risk |
| Climate VaR coverage (physical/policy) | `equity_index.esg_metrics_additional.coverage_climate_var_physical_risk`, `coverage_climate_var_policy_risk` | percent index weight covered |
| Low Carbon Transition score (index-level aggregate) | **IMX only** — `index_esg_low_carbon_transition_score_last` via `calculate_metrics`; the catalog only exposes this at security level (`equity.sustainability_factor.input.security.cbn_lct_score`, SIMD/FIMD transparency), there is no plain index-level scalar. Render as a native IMX chart callout, same handling as §2's risk analytics | 0-10; higher = more aligned |
| EU BMR — climate alignment | `equity_index.esg_metrics.climate_aligned` | scalar flag |
| EU BMR — investable-universe overlap | `equity_index.esg_metrics.benchmark_investable_overlap` | Art. 1(e) EU BMR 2020/1818 overlap test — this is the PAB/CTB investable-universe metric |
| EU sustainable-investment screening weight | `equity_index.sfdr_metrics.eu_sust_invst_scrn_wt_sm` | percent |

Every carbon/climate figure that has a paired `cov_*` field must show it (standing rule 8). Do not compute WACI, ITR, or Climate VaR yourself from underlying company data — these are MCP-direct/EOM-published values only.

## §4 — Index Changes Analyst

Per review effective date T (T₋₁ = business day before T). All values are MCP-direct fields or simple arithmetic on them.

| Metric | MCP source | Unit / rule |
|---|---|---|
| Review effective dates | `equity_index.master_description.last_rebalancing_date` (recursed to date−1 business day; `variant:STRD`) | YYYYMMDD |
| N(Pre-review) | `equity_index.description.nb_of_securities` at T₋₁ (`variant:STRD`) | count |
| N(Post-review) | `equity_index.description.nb_of_securities` at T (`variant:STRD`) | count; MUST equal N(Pre-review) − Deletions + Additions |
| Additions / Deletions / FIF changes | `equity_index.review_change_counts.{nb_of_additions,nb_of_deletions,nb_of_fif_changes}` (`rebalance_target:previous`, `date=T`) | counts. FIF-changes count kept but usefulness under review |
| Added / deleted security codes | `equity_index.additions.msci_security_code` / `equity_index.deletions.msci_security_code` | bare codes — resolve names via a SECOND fetch on `security.description.security_name` (two-step) |
| Pre-review weights | `equity_index.constituents.closing_weight` at T₋₁ | **percent**, as-is |
| Post-review (target) weights | `equity_index.proforma_constituents.initial_weight` | **decimal** → ×100 |
| Index turnover (%) | `fetch_index_timeseries(equity_index.performance.total_index_turnover)` at T (start=end=T) | **fraction → ×100** (VERIFIED LIVE); **one-way** (= ½ `Σ|Δw|`); printed report shows **two-way** = ×2 |
| Addition TO (%) | Σ post weight over `ADDITIONS` codes | simple sum; one-way added weight |
| Deletion TO (%) | Σ pre weight over `DELETIONS` codes | simple sum; one-way removed weight |
| Significant weight changes | `Δw = w_post − w_pre` over the union of pre/post securities, **filtered to \|Δw\| ≥ cutoff (default 1pp)**, sorted by `\|Δw\|` desc | percentage points; added rows pre=0, deleted rows post=0, else reweighted. **Cutoff is user-adjustable and expandable to the full list on request** (was a fixed top-5) |
| Reason for deletion (security level) | IRCR content | **DEFERRED — not captured by IndexAI today; integrate on IRCR dataset upload.** Show the column marked "coming"; do not fabricate |
| Estimated post-event weights / trade or order list | — | DROP — forward estimate / index-implementation workflow; out of scope |

**Disclaimer.** Turnover (direct MCP field × ×100) and the TO sums (simple sums) are exempt from the approximation disclaimer. The `Σ|Δw|/2` proxy is a cross-check only.

**Validation (run every build).** Assert `rebalanceDate == T` on each review-change call; assert N(Post-review) = N(Pre-review) − Deletions + Additions per review; pre/post weights each sum to ≈100 (±1) after normalization; one-way turnover ≥ Addition TO — flag any violation on the dashboard face, do not hide it.

---

## §5 — Index Methodology Analyst

Two sources, stitched together — a live quantitative screen plus cited rule text. Never blend the two: the screen answers "does it pass today's checks," the methodology text answers "why does the rule exist and where do capping/buffer bands kick in."

| Metric | MCP source | Notes |
|---|---|---|
| Composite eligibility flag | `security.index_inclusion_monitor.index_eligible_fg` | TRUE only if every component flag passes; FALSE takes precedence over any blank input; BLANK only when no requirement fails and a required input is missing. **This is a reference indicator, not a final index decision** — see caveats below |
| Component flags (read every one on a failure, not just the first) | `size_segment_fg`, `minimum_free_float_market_capitalization_fg`, `minimum_foreign_inclusion_factor_flag`, `foreign_room_flag`, `atvr_12m_fg`, `atvr_3m_fg`, `fot_12m_fg`, `fot_3m_fg`, `china_a_share_with_connect_line` | each is itself a datapoint under the same namespace; attribute a failure to ALL failing flags, not the first found |
| Current index market cap (context) | `security.index_inclusion_monitor.current_index_mcap_musd` | USD millions; blank when not a current constituent — that blank is the correct answer, do not recompute |
| Capping / buffer / country-classification rules (cited text) | `search_index_methodology_stack(indexCode, query)` | semantic search over the actual methodology documents; cite the methodology name + snippet, never paraphrase from training data. If the tool returns no hits, prefix the answer with "⚠️ Note: The following information is from general knowledge, not the official MSCI methodology document." per the tool's own fallback rule |

**Caveats to always state alongside the eligibility flag** (from the datapoint's own documentation — do not omit):
- Size-segment cutoffs shown are the interim daily-maintenance cutoffs, not the final Index Review cutoffs.
- Free float, foreign room, and liquidity reflect the latest available data as of the prior month-end, not the actual review price-cutoff date.
- **Buffer/migration rules (size-migration 2/3 and 1.5x, Small Cap entry) are NOT reflected in this snapshot** — those live only in the cited methodology text, never in `index_eligible_fg`.
- AUM figures elsewhere in the Inclusion Module are indicative only, not actual fund flows.

**Mandatory disclaimer (standing rule 7).** Whenever `index_eligible_fg` or any Index Inclusion Module datapoint is shown, append its full disclaimer block verbatim via `assemble()`'s `extra_disclaimers` — the 9-point block starting "This report provides a high-level assessment..." and ending with the MSCI legal notice link. This is carried in the datapoint's own `constraints.notes`, not injected automatically by the fetch tool.

## §6 — Index Comparator

Not a new metric set. A **compare mode** over §1 (composition) and §2 (performance/risk) for 2-5 indexes at once.

**Alignment contract (mandatory, confirm with the user if unspecified):**
- One **currency** across all selected indexes.
- One **variant** (STRD/GRTR/NETR) across all selected indexes.
- One **as-of date** (and, for performance, one **range**) across all selected indexes.

**Pulls.** Reuse §1's constituents/sector/country/returns pulls and §2's factor-tilt pulls, once per selected index, with the same date/currency/variant. For risk analytics, call `calculate_metrics` once per index (or pass the comparison index as `benchmark_portfolio` where the user wants an active/relative view) — same native-chart handling as §2.

**Rendering.** Side-by-side columns/rows per index, not a single blended average. Do not silently drop an index whose data is null for a period — show "n/a" for that index/period cell, same rule as §1/§2.

## §7 — Factor Index Methodology Data (FIMD)

The **factor** methodology input from the `equity.sustainability_factor.input.security.*` namespace, shown for the index's holdings with the **composite factor score beside each holding's index weight** (`equity_index.constituents.closing_weight`, joined by `msci_security_code`). Every input has a **bare id** (month-end; date auto-snaps to the 2nd business day) and a **`.rebalancing` sibling** (server resolves the review's T-9 date; two-step last/next-rebalancing lookup). `entity_type=equity_index`, `cardinality=list`. The input is index-scoped — it **cannot** be fetched by security code (verified: returns "No Data available for the given input index …"), so join via the index map. **Licensed.**

The table is deliberately minimal — exactly four displayed columns: **Security · MSCI code · Weight % · Factor**. Weight comes from the index constituents dataset; the Factor is the single composite score from the FIMD dataset. The descriptor inputs (ROE, Debt/Equity, Earnings Variability, momentum z-scores) drive the score inside the methodology but are **not shown as columns** — they belong in the "rules that matter" panel, not the holdings table.

| Metric (displayed column) | MCP source (`equity.sustainability_factor.input.security.` + …) | Unit / rule |
|---|---|---|
| Security (name) | `equity_index.constituents.identifiers.security_name` | join via `msci_security_code` |
| MSCI code | `equity_index.constituents.description.msci_security_code` (join key) | MSCI security code; matches the FIMD map's `msci_security_code` (`.rebalancing` when value ids are `.rebalancing`) |
| Index weight (from constituents dataset) | `equity_index.constituents.closing_weight` | % of index; the table's sort key (desc) |
| **Factor score (composite) — key column, from FIMD dataset** | Quality → `quality_score`; Momentum → `momentum_score` / `composite_momentum_score`; High Dividend Yield → `composite_dividend_score` | dimensionless (~−3…+3 for a z-composite; some transformed). One column, labelled for the family (e.g. "Quality Score") |

Descriptors (`return_on_equity`, `debt_to_equity`, `earnings_variability`, `earnings_variability_z_score`, `quality_z_score`, `6m_momemtum_zscore`, `12m_momemtum_zscore`) are **not displayed** — they feed the composite and are described in the rules panel only.

**Discovery, not assumption.** Discover the exact composite-score id with `search_index_datapoints` and confirm the index uses it via `search_index_methodology_stack`, then pull `msci_security_code` + that single score. A blank Factor cell for a holding means unrated / not-mapped — show "n/a", never zero-fill.

**Validation.** Availability probe (`msci_security_code`) returns rows before rendering; `pagination.total_rows` reads as the parent-universe size. The constituent pull returns weights summing to a plausible total (≤100). The composite factor score is within a plausible range (z-composite roughly [−5,5] — flag outside). Rebalance view: resolved calc date equals the server T-9 for the chosen review (else surface "No Data", offer Month-end). Month-end `note` confirms the 2nd-business-day snap. Assert the Factor column renders beside weight for the joined holdings.

**Disclaimer.** Direct MCP datapoints + simple arithmetic → no approximation disclaimer. It applies only if the user forces a methodology-sensitive derived metric out of these inputs.

---

## Validation (run on every build)

**§1 Index tab** — constituent weight in [0,100]; top weight ≤ ~40% for a broad index (else flag); Σ sector ≈ 100 (±1); Σ country ≈ 100 (±1.5); annualized (3Y+) returns within ~[−50%, +75%], shorter periods ~[−60%, +100%] (flag outside); null periods shown "n/a"; any in-scope factsheet field respects its catalog unit.

**§1 Security tab** — resolved security code stable across index calls; FIF ∈ [0,1] when present; NOS > 0 when present; weight in [0,100]; "not a constituent" shown, not dropped; licensed section hidden when not returned.

**§2 Performance & Risk** — in-shell returns/factor fields follow §1's return/unit checks; relative IMX metrics (tracking error, information ratio, active drawdown, active-risk attribution) are never rendered as 0 or blank when `benchmark_portfolio` is absent — surface the "benchmark required" state instead; equity-only — refuse (don't silently proxy) for fixed income/hedged indexes.

**§3 Sustainability & Climate** — WACI/ITR/Climate VaR values are non-negative where the field's own definition requires it; every value with a paired `cov_*` field shows that coverage percentage; ITR is never converted to/from a carbon-intensity number; the index-vs-parent comparison is built by fetching `wtd_avg_carbon_intensity_by_sales_scope_1_2_3` (and the other §3 fields) for **each index code separately**, never via `waci_index`/`waci_parent` unless the index is FIMD-eligible (`data/fimd-indexes.txt`).

**§4 Changes** — assert each review's `rebalanceDate == T`; N(Post-review) = N(Pre-review) − Deletions + Additions per review; pre/post weights each sum to ≈100 (±1); one-way turnover ≥ Addition TO — flag violations on the dashboard face.

**§5 Methodology** — `index_eligible_fg` component flags are read directly, never recomputed from the roll-up logic; every failing flag is attributed, not just the first; the buffer/migration caveat and the full IIM disclaimer (via `extra_disclaimers`) are present whenever this datapoint renders; cited methodology text carries its methodology name, never a from-memory paraphrase (or the mandatory "⚠️ Note" prefix when no hits returned).

**§6 Comparator** — all selected indexes share one currency/variant/as-of date (assert before rendering, not after); a null cell for one index/period is shown "n/a", never silently dropping that index from the comparison.

**§7 Factor Methodology Data (FIMD)** — index is in `data/fimd-indexes.txt` AND the live `msci_security_code` probe returns rows before rendering; the constituent pull joins to the factor map by `msci_security_code`; the composite factor score populates (z-composite roughly [−5,5], flag outside); Rebalance-view calc date matches the server T-9 (else "No Data" → offer Month-end); Month-end `note` confirms the 2nd-business-day snap. Table shows the holdings descending by weight with exactly four columns (Security · MSCI code · Weight % · Factor), the Factor beside the weight; the per-security input is index-scoped (join via the index map, never per-security fetch).

Hard impossibilities (negative level, weight > 100, FIF outside [0,1]) stop the build. Merely abnormal values render with a visible flag.

---

## Disclaimers (every dashboard)

**1. Persistent sample disclaimer — always.** Footer, verbatim:

> Sample / provided as-is. This dashboard is a sample recipe showing what is possible with the IndexAI Insights MCP. It is not an MSCI product and is not maintained as a deliverable.

**1b. MSCI Notice and Disclaimer — always.** Below the sample disclaimer, a compact compliance line and a "Notice and Disclaimer" expander holding the FULL MSCI notice, embedded **verbatim** from `assets/disclaimer-notice.txt` via the build helper in `assets/disclaimer-footer.html`; never retype, paraphrase, summarize, reformat, or regenerate it. Compact line:

> For informational purposes only. The Information is the proprietary property of MSCI and must not be relied upon as investment advice or a recommendation. It is not a prediction or guarantee of future performance; past performance is not indicative of future results. It is not possible to invest in an index, and index returns do not represent the results of actual trading. GICS is the exclusive property of MSCI and S&P Dow Jones Indices.

**2. Datapoint-mandated disclaimer — whenever a datapoint's own `constraints.notes` requires one.** Currently applies to §5's Index Inclusion Module fields (`security.index_inclusion_monitor.*`). Pass the exact block through `assemble()`'s `extra_disclaimers` so it renders verbatim, separate from and in addition to blocks 1/1b — `fetch_index_data` does NOT inject it automatically. Never trim, summarize, or merge it with the sample/compliance text above.

**3. Approximation disclaimer — only if the user insists on a genuinely ad hoc metric outside MSCI's own computed analytics.** Render it with all three: an inline "⚠ Approximation — not MSCI-endorsed" marker, an on-hover tooltip carrying the text below verbatim, and a persistent bottom-of-dashboard disclaimer carrying it verbatim, placed **last**:

> Note: This calculation is an approximation generated outside of MSCI's official index methodology framework. MSCI-methodology-aligned risk and performance analytics will be available through the MSCI connector in a future release. This output should not be interpreted as an MSCI-endorsed metric

Simple arithmetic is exempt. Note this disclaimer is now narrower than before: MSCI-computed IMX risk analytics (§2) are no longer "future release" — this block is only for a metric the user forces outside of both the MCP catalog and IMX.
