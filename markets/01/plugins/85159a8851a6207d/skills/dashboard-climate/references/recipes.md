# Dashboard Recipes

One section per dashboard: what it pulls (approved set only — see `metric-audit.md`), the layout, and notes. Brand, control and refresh conventions are shared below. Exact tool calls and datapoint IDs are in `mcp-queries.md`. All styling comes from `references/brand.md` (this skill brands its own output; do not reach for another skill).

The active set is **six analyst dashboards + FIMD + licensed-index support**: §1 Index Composition Analyst (one dashboard, two tabs), §2 Index Performance & Risk Analyst, §3 Sustainability & Climate Index Analyst, §4 Index Changes Analyst, §5 Index Methodology Analyst, §6 Index Comparator, and §7 Factor Index Methodology Data (FIMD).

---

## Shared conventions

**Build via the shared shell.** Every dashboard is assembled from `assets/dashboard-shell.html` through `assets/assemble.py`; the header/logo, the as-of date + range control (with live date resolution), disclaimers, brand, and responsive base are inherited, not hand-written. The per-dashboard notes below describe only the body (`body_html`), the `queries`, and the `render(payload)` re-render.

**Brand.** Apply `references/brand.md` in full: the `:root` variable block, Inter, the dark `daintree→smokey-blue` header gradient with the inlined white MSCI logo (`assets/logos/msci-logo-white.svg`), MSCI card/KPI/table/button patterns, the 30-colour data-viz palette applied in hierarchical order for categorical series, and Values colours (teal/red) only for financial up/down. Follow its Chart rules section in full — Inter Regular and Semi bold, semi-bold axis labels 1pt larger, 0.5pt Silver axis lines with a solid #707070 zero line, 2pt data lines with no per-point markers, units in the chart title rather than a Y-axis label, and a centred legend using circles. Rounded corners, generous white space.

**Layout & alignment.** Header (logo + title + sub-title + "Data via IndexAI Insights MCP · <variant> · <ccy> · as-of <date> · <range>" + the as-of/range control top-right). Tabs for multi-view dashboards. KPI cards row, then tables/charts. **Metrics must line up** — use the shell KPI grid (do not hand-set card widths), tabular numerals on figures, and the `num` helper on numeric table cells so columns right-align. A ragged, misaligned metric row was flagged in testing; keep KPI values on a consistent grid and rendering aligned with the panels. Footer: the standard disclaimer footer from `assets/disclaimer-footer.html` — (1) sample disclaimer verbatim, (2) compact compliance line + "Notice and Disclaimer" expander holding the FULL MSCI notice injected **verbatim** from `assets/disclaimer-notice.txt`, (3) approximation disclaimer only if an off-spec metric is shown, placed last. Insert the footer INSIDE the centered page container, and keep it the ONLY sample-disclaimer line.

**Responsive.** No horizontal overflow on a narrow window — `auto-fit` KPI rows, `min-width:0`, clamped KPI fonts, `overflow-x:auto` on wide tables, `body{overflow-x:hidden}`. Check at ~380–700px.

**Charts.** Prefer lightweight inline SVG (no external chart lib / CDN) so the artifact is fully self-contained. Follow `brand.md` chart rules.

**As-of date + range (replaces the old one-click refresh).** The header control is a **"Latest" toggle + an as-of date picker + a range selector**. "Latest" (default) resolves the latest served business date live; unticking it uses the picked date. The selected range (1M/3M/6M/YTD/1Y/3Y/5Y/Max) sets the lookback. The control fills `<DATE>`/`<END>` (as-of date) and `<START>` (range start) in each query's args, re-pulls, and calls `render()`. Latency can be high — re-pull only what the view needs and show a spinner.

**First render.** Embed the real snapshot pulled during the build; the control replaces it. Never ship placeholder numbers as real.

**`render()` must actually update the DOM (mandatory, not optional).** A `render_body` that parses `payload` but never writes it back to the page is a shipped bug, not a stub to fill in later — the Update button will silently do nothing, which is worse than no button at all. Tag every value that can change on refresh with an `id`, and have `render(payload)` set `textContent`/`innerHTML` on each by id. Look up each index's scalars by **matching the code inside parentheses** in the response's `"{name} (code)"` keys (`for (var k in scalars) if (k.indexOf("("+code+")") !== -1) ...`) rather than hardcoding the exact `"{name} (code)"` string — the index name text is not guaranteed stable. Before treating a dashboard as done, mentally (or actually) trace `render()` against a realistic mock payload shaped like a real MCP response and confirm every id it targets exists in `body_html` and every value it computes matches the units/rule in `metric-audit.md`.

**Don't give an unrendered metric its own empty-looking panel.** If a metric is deliberately not shown in-shell (e.g. an IMX-only analytic with no plain catalog field, see §2/§3), explain that in one line of the small print at the bottom — not as a full card with its own header, which reads to a client as a broken or missing widget sitting at the same visual weight as real data.

**Labelling.** 3Y+ returns annualized (CAGR). State currency + variant + range. "n/a" for null values. Weights are percent — display as-is.

**Commentary (standing rule 10, mandatory on every dashboard).** Each major section (KPI row, each table/panel) gets one short interpretive callout — a sentence or two, placed as a `<p class="mut">` note directly under that section, not blended into the raw numbers — that says what the data *means*, not just what it is (e.g. "EM's top holding is more concentrated than World's despite EM being more country-diversified"). Every figure the callout cites must already be visible elsewhere on the same dashboard; never cite an external fact, a forecast, or an opinion the pulled data doesn't support. Skip a section's commentary rather than force a weak or padded observation, but don't skip all of them — a dashboard with zero interpretive callouts fails standing rule 10 outright.

**Validation.** Run `metric-audit.md` § Validation before rendering; surface flags on the dashboard face, not just in logs.

**Metric rule.** MCP-direct values and simple arithmetic only (see `metric-audit.md`). If the user insists on a methodology-sensitive/non-MCP metric, attach the approximation marker + tooltip + bottom disclaimer with the exact text. Simple arithmetic is exempt.

**Licensed-index support (cross-cutting).** For entitled/licensed content, the analyzer may add proprietary fields (e.g. thematic scores) next to the standard MCP fields — but only when the connector actually returns them for this user. Never fabricate licensed data; keep disclaimers, metric rule and branding identical.

---

## §1 — Index Composition Analyst

**One dashboard, two top-level tabs: an *Index* tab and a *Security* tab.** Keep the two-tab structure — do not split this into separate dashboards. Both tabs share one resolved as-of date and the same selected set of indexes.

**Inputs:** one or more indexes (resolved via `search_index_indexes`; confirm name+code). For the Security tab, a security (resolved via standard MSCI search) whose membership is checked across those same indexes. Optional: licensed/thematic fields (entitled only).

**Common pulls:** `search_index_indexes` per index; `fetch_index_data` for returns (`equity_index.performance.period_returns.period` + `.returns`); `fetch_index_data` for constituents+identifiers+sector+country (`equity_index.constituents.closing_weight`, `.identifiers.{security_name,isin,RIC,ISO_country_symbol}`, `equity_index.sector_weight.{sector_name,gics_closing_weight}`, `equity_index.country_weight.{country_name,cty_closing_weight}`, large `page_size`); `equity_index.description.nb_of_securities` for index size. The constituents pull feeds BOTH tabs (index composition and the security's per-index weight), so pull it once per index. Add the other **in-scope factsheet fields only where the MCP exposes them** (valuation/fundamentals, factor, ESG/climate, historical time series) — see `metric-audit.md` §1; anything not exposed is simply omitted (do not compute a proxy).

### Index tab
Index/benchmark level. Sections (stacked; the tab itself is one of the two top-level tabs):
1. *Performance* — KPI cards per index (YTD, 1Y, 3Y CAGR, 5Y CAGR; "n/a" where null); full multi-period table; historical index-level time series (`fetch_index_timeseries` over the selected range) where the datapoint supports range.
2. *Rankings* — sortable YTD and 1Y rankings (omit indexes null for that period).
3. *Weights & concentration* — top-10 constituents, sector weights, and the **full country breakdown** (default-sorted desc, scrollable — not a hard top-12; the old top-12 cap was removed per testing), cumulative top-10 weight + a one-line concentration read (top-weight and top-10 share; do NOT compute effective number of stocks — not an MCP field).
4. *Factsheet metrics* — the in-scope factsheet set actually returned (valuation & fundamentals, factors, ESG & climate) — each labelled with its MCP source; methodology-sensitive risk is intentionally absent (deferred).

### Security tab
Single-security focus, across the selected indexes. Resolve the security with **standard MSCI search** (case-insensitive token/substring — so "space" returns AST SPACEMOBILE, EXTRA SPACE STORAGE, GE AEROSPACE, HOWMET AEROSPACE, SPACE EXPL TECH CORP, not one row; **no hard 80-row cap** — page through and show all matches). Sections:
1. *Security header* — resolved name, ISIN, RIC, country, sector, MSCI security code.
2. *Detail KPIs* — for a chosen index, current weight, FIF (3 dp), NOS where present; each labelled with its MCP source and as-of date.
3. *Cross-index membership* — a table over the selected indexes: Index · In index? · Weight (%) · Sector · Country. Right-aligned numeric columns (`num`), tabular numerals; "not a constituent" where absent — do not drop the row.
4. *Licensed / thematic (entitled only)* — proprietary fields when the connector returns them; hidden entirely otherwise.

**Notes / guardrails.**
- One shared as-of date; pull sector/country weights with large `page_size` (a small page truncates them too). No dollar exposure unless AUM supplied; no recommendations.
- **Facts only** — MCP-direct fields + simple arithmetic. No forward estimates, no methodology-sensitive analytics.
- **Deferred capability (not active):** "search which of ALL standard + custom indexes a security is in, over a date range." Not supported by current IndexAI Insights — it needs security↔index mapping. Say it is a planned capability; do NOT approximate it by brute-force scanning indexes. The supported view is membership across the **selected** indexes above.
- When required inputs are missing, ask the user to clarify before building — this was praised as a good client experience.

## §2 — Index Performance & Risk Analyst

**Purpose.** Returns, factor tilts, and performance drivers as a refreshable MSCI-branded dashboard, plus MSCI's own IMX risk analytics (tracking error, Sharpe/information ratio, VaR/CVaR, drawdown, active-risk attribution) surfaced as a native interactive chart alongside it. See `metric-audit.md` §2 for the exact field/mnemonic list and the in-shell-vs-native-chart split.

**Inputs:** the index (required); an optional benchmark index for relative/active metrics; currency/variant (default USD, GRTR); as-of date + range.

**Build — in two parts:**

1. **In-shell part (goes through `assemble.py` like every other dashboard).** `fetch_index_data` for `equity_index.performance.period_returns.{period,returns}` and `equity_index.facs_ratios.*`; `fetch_index_timeseries` for the historical level chart and (where `supports_range=true`) factor-tilt history. Render KPI cards (YTD/1Y/3Y CAGR/5Y CAGR), a multi-period returns table, and a factor-tilt bar/radar panel using `brand.md` chart rules — all MCP-direct, all inline SVG, no external chart lib.
2. **Native IMX part (NOT built through the shell's own chart renderer).** Call `calculate_metrics` with the mnemonics in `metric-audit.md` §2 (`key_metrics`, `key_risk_metrics`, `index_tracking_error`, `index_sharpe_ratio`, `index_information_ratio`, risk-attribution breakdowns), passing the benchmark index as `benchmark_portfolio` when the user wants a relative view. Present the result as its own interactive chart in the conversation, with a clearly labeled "Risk analytics (live IMX chart)" panel in the dashboard body that **links to / describes** this rather than re-plotting the numbers — the tool's own instructions say not to recreate its output as a table or ASCII chart. If a relative metric comes back null because no benchmark was passed, say so; never render it as zero.

**Layout.** KPI row (YTD, 1Y, 3Y CAGR, latest tracking error if a benchmark is set) → multi-period returns table → historical level chart → factor-tilt panel → "Risk analytics" panel (native IMX chart callout) → standard disclaimer footer. Equity indexes only — for fixed income/hedged indexes, state that IMX risk analytics are not available and show only the in-shell returns/factor fields.

**Notes / guardrails.**
- Do not attempt to recompute Sharpe/tracking error/etc. from the in-shell returns yourself even as a fallback — that is exactly the ad hoc-methodology violation standing rule 2 exists to prevent. If IMX is unavailable on the connection, say risk analytics aren't available rather than approximating them.
- Label the FaCS tilts as relative to MSCI ACWI IMI (per their own field description), not as absolute levels.

## §3 — Sustainability & Climate Index Analyst

**Purpose.** How climate/ESG index construction reshapes an index relative to its parent — WACI, Implied Temperature Rise, Climate VaR, Low Carbon Transition score, and EU BMR alignment fields (climate alignment, investable-universe overlap, sustainable-investment screening weight). See `metric-audit.md` §3 for the exact field list.

**Inputs:** the index (required); its parent/standard-index variant when the user wants an explicit vs-parent view (resolve via `search_index_indexes`, confirm with the user if ambiguous); as-of date (EOM-published fields — no intraday).

**Build.**
1. Resolve the index code (and parent code, if requested) via `search_index_indexes`.
2. **In-shell (MCP-direct):** pull `equity_index.esg_metrics_additional.wtd_avg_carbon_intensity_by_sales_scope_1_2_3` + its coverage field for **each index code separately** (index and parent/comparison) — VERIFIED LIVE as the field that actually populates; the FIMD-namespace `waci_index`/`waci_parent` pair only applies to factor indexes in `data/fimd-indexes.txt` and returns null otherwise (do not use it for a general index-vs-parent ask). Also pull `equity_index.esg_metrics.implied_temperature_rise` + its `cov_implied_temperature_rise` coverage, `equity_index.esg_metrics.total_var` + the physical/policy coverage fields, and the `eu_bmr_metrics` fields (`climate_aligned`, `benchmark_investable_overlap`, `eu_sust_invst_scrn_wt_sm`).
3. **Native IMX chart:** the index-level Low Carbon Transition score (`index_esg_low_carbon_transition_score_last`) has no plain catalog scalar — call `calculate_metrics` and present it the same way §2 presents risk analytics: a native interactive chart, not re-plotted numbers.
4. Render every in-shell metric **paired with its coverage field** where one exists (standing rule 8) — a headline number with low coverage is misleading on its own.

**Layout.** KPI row (WACI, ITR, aggregate Climate VaR) → index-vs-parent comparison table (when a parent is resolved) → EU BMR alignment panel → Low Carbon Transition score (native IMX chart callout) → coverage footnotes under each metric that has a `cov_*` field → standard disclaimer footer.

**Notes / guardrails.**
- ITR is a forward-looking modelled alignment estimate in °C — never state or imply it converts to/from a carbon-intensity figure.
- These are EOM-published values (2nd business day snap, same as FIMD) — do not intraday-refresh them; the as-of control still resolves the latest published month.
- If the connector does not return a parent-index field for a given index, drop the vs-parent framing rather than fabricating a parent comparison — show the single-index view only.

## §4 — Index Changes Analyst

**Purpose.** A refreshable, MSCI-branded summary of an index's last *N* index reviews (rebalances): per review, the index constituent counts before/after, additions, deletions, FIF changes, official index turnover, one-way addition/deletion turnover, and the significant constituent weight changes. This is a *review-summary* dashboard (read-only facts + simple arithmetic) — NOT a proforma trade/order list.

**Inputs:** the index (required); number of reviews *N* (default 5); currency/variant for turnover (default USD, GRTR). A China A breakout is optional and OFF by default.

**Deterministic build — do exactly this, in order. Exact tool calls and datapoint IDs are in `mcp-queries.md` §4.**

- **Step 0 — Resolve the index code.** `search_index_indexes`; confirm name+code with the user. Never hardcode codes.
- **Step 1 — Find the *N* review effective dates (recursive).**
  1. Resolve the latest business date (`mcp-queries.md` §0b — never today's calendar date). `fetch_index_data(index, variant:STRD, date=latest, datapoints:["equity_index.master_description.last_rebalancing_date"])` → R1.
  2. Call again at `date = R1 − 1 business day` → its `last_rebalancing_date` is R2.
  3. Repeat until *N* dates (R1…R_N) are collected.
- **Step 2 — Per effective date T (T₋₁ = the business day before T), make these `fetch_index_data` calls (separate calls — different dates/targets):**
  - *PRE composition* — constituents at T₋₁ (`closing_weight` PERCENT, `identifiers.security_name`, `description.msci_security_code`, `order_by:closing_weight desc`, `page_size:2000`) + `equity_index.description.nb_of_securities` at T₋₁ (STRD) = **N(Pre-review)**.
  - *REVIEW changes* — at T, `rebalance_target:"previous"`: `review_change_counts.{nb_of_additions,nb_of_deletions,nb_of_fif_changes}`, `additions.msci_security_code`, `deletions.msci_security_code`, `proforma_constituents.initial_weight` (DECIMAL). If outside the live review window, relay `outsideRebalWindow.message`.
  - *POST count* — `nb_of_securities` at T (STRD) = **N(Post-review)**.
  - *Names for ADDED/DELETED codes (two-step, REQUIRED)* — a SECOND `fetch_index_data` with those codes in `codes[]` and `security.description.security_name`. Do NOT mix index and security codes in one call.
  - *Official turnover* (range-only) — `fetch_index_timeseries(index, start_date=T, end_date=T, currency, variant, datapoints:["equity_index.performance.total_index_turnover"])`.
- **Step 3 — Compute (simple arithmetic on MCP fields only):**
  - Normalize weights (max>1 → percent as-is; max≤1 → ×100). PRE `closing_weight` is percent; PROFORMA `initial_weight` is decimal → ×100.
  - **Assert N(Post-review) = N(Pre-review) − Deletions + Additions** (flag if not).
  - Weight-change table over the **union** of PRE and POST securities: `Δw = w_post − w_pre` (missing side = 0); name from the two-step resolution, else PRE.
  - **Addition TO(%)** = Σ `w_post` over ADDITIONS codes. **Deletion TO(%)** = Σ `w_pre` over DELETIONS codes.
  - **Significant weight changes** = union rows with **|Δw| ≥ the cutoff (default 1pp)**, sorted by `|Δw|` desc, each tagged *added* / *deleted* / *reweighted*. (Change from the old fixed top-5; see below.)
  - **Index turnover(%)** = official `total_index_turnover` × 100 — do NOT recompute; the `Σ|Δw|/2` proxy is only a cross-check.

**Layout (single page; tables, no chart needed).**
1. KPI row — Index, reviews analyzed, last review effective date, latest turnover.
2. **Review summary** table — one row per review: Effective date · N(Pre-review) · N(Deletions) · N(Additions) · N(Post-review) · Index turnover (%) · Addition TO (%) · Deletion TO (%) · FIF changes. (Numeric columns right-aligned, tabular numerals.)
3. **Significant constituent weight changes by review** — a per-review tab selector with a small KPI strip (turnover, add/del TO, counts) and a table of **all changes with |Δw| ≥ cutoff** (Security · Status · Pre-review weight · Post-review weight · Change pp · [Reason for deletion — deferred]). A **cutoff control** (default 1pp) lets the user tighten/loosen it, and a **"Show all constituent changes"** toggle expands to the full union list on request — showing every constituent by default would clutter the view, so 1pp is the default cutoff.
4. **Index information** table — index name+code, last review effective date, snapshot business date.

**State on the dashboard face how each table is computed (mandatory comments):**
- *Summary table* — N(Pre/Post) = `nb_of_securities` at T₋₁ and T; counts from `REVIEW_CHANGE_COUNTS`; Index turnover = official one-way `TOTAL_INDEX_TURNOVER`×100 at T; Addition/Deletion TO = one-way summed weights; identity N(Post)=N(Pre)−Del+Add.
- *Weight-change table* — `Δw = post − pre` (pp); ADDED rows pre=0, DELETED rows post=0, REWEIGHTED are continuing names; only rows with |Δw| ≥ the cutoff are shown unless expanded.
- *Index info* — dates are YYYYMMDD business dates.

**Labels (reviewed — use consistently).** Use **"Effective date"** for the review effective date and **"Last review effective date"** for the most recent one (do not mix "last rebalance effective date" / "last effective date"). Use **Pre-review / Post-review** for the index the business day before, and on, the effective date (MSCI's printed review report calls these "Current"/"Proforma" because it is produced at announcement; for a historical view those are misleading — relabel and note the mapping).

**Reason for deletion (IRCR) — DEFERRED.** A security-level "reason for deletion" (from IRCR content) is **not captured by IndexAI Insights today**. Leave the column present but marked "coming with the IRCR dataset"; wire it in once the IRCR dataset is uploaded. Do not fabricate reasons.

**FIF change (under review).** Keep the FIF-changes count in the summary; its usefulness is an open question — surface it, and be ready to drop it if the reviewers decide it adds little.

**Scope (open question).** Extending this to non-derived indexes (e.g. GIMI) as the sole rebalance experience is under consideration; today the dashboard works for indexes where the review datapoints resolve. Do not assume GIMI coverage until confirmed.

**Turnover convention (important).** The dashboard shows MSCI's official **one-way** daily turnover (`TOTAL_INDEX_TURNOVER` at T). MSCI's printed review report shows **two-way** turnover (= 2 × one-way = gross `Σ|Δw|`). State which is shown; if the user wants the report's figure, double it (or show both). Turnover is a direct MCP field (× a simple ×100), so it does **not** trigger the approximation disclaimer; Addition/Deletion TO are simple sums — also exempt.

**Refresh / as-of.** Historical reviews are immutable; what changes is whether a NEWER review has occurred. On re-pull, run `fetch_index_data(index, variant:STRD, date=<resolved as-of>, datapoints:["equity_index.master_description.last_rebalancing_date"])`; if later than the snapshot's last review, show a banner ("a newer review effective <date> exists — regenerate"); else confirm unchanged. Do NOT re-pull all per-review data on refresh (too slow/fragile); the embedded snapshot is authoritative for the historical rows. The as-of picker lets the user anchor "latest review as of <date>".

**Notes / guardrails.**
- Review-change datapoints are fetched with `rebalance_target:"previous"` at `date=T`, in their own call. Allow >60s. Added/deleted names need the separate two-step resolution.
- Pull PRE and PROFORMA with `page_size:2000`.
- If a review-change call returns `outsideRebalWindow.message`, relay it verbatim.
- This is a review SUMMARY — NOT a proforma trade/order list. Estimated post-event weights and trade lists remain out of scope.

## §5 — Index Methodology Analyst

**Purpose.** Two things a PM/product-team question actually needs together: (1) a live eligibility screen for a named security against a reference index/module, and (2) 2-3 cited rules — capping, buffer zones, country classification — pulled from the actual methodology document, not from memory. See `metric-audit.md` §5 for the exact fields and the mandatory disclaimer.

**Inputs:** the security (required, resolved via standard MSCI search); the reference index or Inclusion Module entity (e.g. `IIM GLOBAL`, `IIM AMERICAS`, `IIM EMEA`, `IIM APAC`) with an optional country filter; the methodology question (eligibility check, capping rule, buffer rule, country classification, review-period question).

**Build.**
1. Resolve the security's MSCI code via `search_index_securities`.
2. Pull `security.index_inclusion_monitor.index_eligible_fg` and every component flag (`size_segment_fg`, `minimum_free_float_market_capitalization_fg`, `minimum_foreign_inclusion_factor_flag`, `foreign_room_flag`, `atvr_12m_fg`, `atvr_3m_fg`, `fot_12m_fg`, `fot_3m_fg`, `china_a_share_with_connect_line`) for the security against the chosen module/index.
3. If `index_eligible_fg` is FALSE or blank, read every component flag and attribute the result to **all** that fail or are "Not Met" — not just the first found.
4. For a rules question (capping/buffer/country classification/review period), call `search_index_methodology_stack(indexCode, query)` and cite the methodology name + the returned snippet; if nothing returns, prefix the answer with the tool's own mandated "⚠️ Note: ... not the official MSCI methodology document" fallback rather than answering from training data unlabeled.
5. Attach the mandatory Index Inclusion Module disclaimer verbatim via `assemble()`'s `extra_disclaimers` whenever step 2/3 data is shown.

**Layout.** Eligibility strip (pass/fail + every component flag, colour-coded) → "why" panel narrating each failing flag with its own input values and cutoff dates → "rules that matter" panel (2-3 cited capping/buffer/country-classification rules, methodology name shown) → the buffer/migration caveat stated plainly (size-migration 2/3 and 1.5x, Small Cap entry are NOT reflected in the eligibility snapshot) → standard disclaimer footer **plus** the IIM disclaimer block.

**Notes / guardrails.**
- Never recompute the `index_eligible_fg` roll-up yourself from the component flags — read the field directly; the roll-up logic has precedence rules (FALSE beats blank) that are easy to get subtly wrong.
- The eligibility snapshot's size-segment cutoffs are interim daily-maintenance cutoffs, not the final Index Review cutoffs — say so.
- If the user asks a pure eligibility question with no methodology-rules component, still show the eligibility screen but you may omit the "rules that matter" panel; if they ask a pure rules question with no security, omit the eligibility strip.

## §6 — Index Comparator

**Purpose.** Compare 2-5 indexes side by side on composition and/or performance/risk, all aligned to the same currency, variant, and as-of date. See `metric-audit.md` §6 — this dashboard owns no new metrics; it is an alignment contract over §1 and §2.

**Inputs:** 2-5 indexes (resolved via `search_index_indexes`); which dimension(s) to compare (composition, performance, risk, or all); one currency; one variant; one as-of date + range.

**Build.**
1. Resolve all index codes; if the user hasn't specified currency/variant/date, ask once rather than guessing per index — a silent mismatch (one index in NETR, another in GRTR) produces a wrong comparison, not just an incomplete one.
2. For composition: reuse §1's constituents/sector/country pulls, once per index, at the shared date.
3. For performance/risk: reuse §2's in-shell returns/factor-tilt pulls per index; for risk analytics, call `calculate_metrics` per index (or with one index as `benchmark_portfolio` for an explicit active view against a chosen baseline).
4. Render side by side — columns per index, not a blended average — so a reader can see each index's own numbers next to the others'.

**Layout.** Header strip confirming the shared currency/variant/as-of date across all indexes → composition comparison table (weights/sector/country side by side) → performance comparison table (multi-period returns side by side) → risk analytics panel (native IMX charts, one per index or one relative-to-baseline) → standard disclaimer footer.

**Notes / guardrails.**
- A null value for one index/period is shown as "n/a" in that index's column — never drop the index from the table because one field is missing.
- This dashboard is a compare **mode**: if the user's question is really just about one index, route to §1/§2/§3/§5 directly rather than building a one-index "comparison."

## §7 — Factor Index Methodology Data (FIMD) — mechanics

FIMD is built on the namespace `equity.sustainability_factor.input.security.*` (per-security methodology inputs). It shows, for the index's holdings, the **factor score** that the methodology uses to select and weight names, **beside each holding's index weight** — so a reader sees *why the weight is what it is*. The table is deliberately minimal.

**Self-explanatory title (required).** FIMD is an acronym — title the dashboard in plain words with the acronym in parentheses, e.g. *"Factor Index Methodology Data — the factor score behind index selection & weighting (FIMD)."*

**Licensed view.** FIMD is separately licensed. Render only when the connector actually returns data (the live probe). Never fabricate values. Keep the standard disclaimers + a "licensed data — shown when entitled" note.

**Eligibility — code list + live probe.** (1) The index must be in `data/fimd-indexes.txt` (the vetted FIMD eligibility list, 289 codes); if not, route to §1/§4. (2) Live-probe `fetch_index_data(codes:["<code>"], datapoints:["equity.sustainability_factor.input.security.msci_security_code"], date:"<as-of>")` — rows in `list_tables` (`pagination.total_rows`>0) → eligible; empty/error → tell the user it isn't available for that index/date (and, in Rebalance view, that Month-end may have data).

**Two views (default = Rebalance).** Control = a **Month-end / Rebalance (T-9)** toggle + a **month** picker (no range selector) + a **Refresh** button that re-runs the MCP.
- **Rebalance (T-9) — default:** `.rebalancing` sibling ids. Resolve the date first (`equity_index.master_description.next_rebalancing_date` if non-null else `last_rebalancing_date`), pass it as `date`; the server resolves the **T-9 pro-forma** calc date (e.g. 1 Jul 2026 → 2026-06-18). If the probe returns "No Data" (upcoming review not published), say so and offer Month-end.
- **Month-end:** bare ids; pass any date in the month — it **auto-snaps to the 2nd business day** (2026-04 → 2026-04-02; `note`/`fetched_date` confirm).

**Index-holdings join (this is the table).** The dashboard's table is the index's **holdings, descending by weight**, with the factor score **beside that holding's index weight**. Exactly **four columns: Security · MSCI code · Weight % · Factor** (plus a rank number) — do NOT add the fundamental descriptor columns. **Weight comes from the index constituents dataset; the Factor comes from the FIMD dataset.** Build it by:
1. Pull the index's **constituents by weight**: `fetch_index_data(codes:["<code>"], datapoints:["equity_index.constituents.closing_weight","equity_index.constituents.identifiers.security_name","equity_index.constituents.description.msci_security_code"], order_by:"closing_weight", order_direction:"desc", page_size:2000)`.
2. Pull the **FIMD factor map** for the parent universe (`msci_security_code` + the single composite score id, in the matching bare / `.rebalancing` form).
3. **Join by `msci_security_code`** client-side; render the holdings descending by weight — `Security · MSCI code · Weight % · Factor` — where Factor is the composite score highlighted as the key column. Table is scrollable ("Index holdings" like the mockup). Factor-index parents are small (e.g. EAFE Quality ≈ 690 names), so the whole set joins fast and **all constituents render — not a top-N sample** (standing rule 9: a table that claims to show holdings in full must actually contain all of them; page/scroll within the same table is fine, silently dropping rows is not). For an unusually large parent only, default to the top 100 by weight and page the rest, and say so on the dashboard face.

The methodology input is **index-scoped** — it CANNOT be fetched per security code (passing security codes returns "No Data available for the given input index <code>" — verified). So the join must read the index map; the map is a single call at load.

**Which factor to show (methodology-driven).** Read the methodology stack (`search_index_methodology_stack`) to confirm the composite factor the index uses, pull `msci_security_code` + that single composite score, and confirm it populates. Infer the family from the index name: **Quality → `quality_score`**, **Momentum → `momentum_score` / `composite_momentum_score`**, **High Dividend Yield → `composite_dividend_score`**. Label the Factor column for the family (e.g. "Quality Score"). Discover exact ids with `search_index_datapoints` at build time. Do NOT surface the descriptor inputs (ROE, Debt/Equity, Earnings Variability, momentum z-scores) as columns — the single composite factor score is what sits beside weight.

**Rules that matter (required panel).** Show 2-3 short **rules pulled from the methodology book** (via the methodology stack) that explain why the factor score matters, cited to the methodology document — matching the mockup's "Rules that matter" panel above the holdings table. Example (Quality): (1) Quality Score = the average of the z-scores of Return on Equity, Debt/Equity and Earnings Variability (winsorized 5th/95th pct). (2) Debt/Equity and Earnings Variability enter with a **negative** z-score (higher leverage / more volatile earnings → lower score). (3) Selection ranks the parent by Quality Score and keeps a fixed number of the highest positive scores; weighting is market-cap-based among those names; a security missing ROE or Debt/Equity is excluded. Pull the equivalents for Momentum / Dividend indexes from the methodology stack.

**Layout (single page, matching the mockup).** (1) availability strip; (2) "rules that matter" panel; (3) KPI row (parent-universe size, constituent count, the factor-score headline, largest-holding weight — simple arithmetic only); (4) "methodology inputs shown" chips (Weight flagged as the constituents-dataset input, Factor flagged as the key metric); (5) the **"Index holdings — weight vs the factor that selects them" table** (Security · MSCI code · Weight % · Factor, factor column highlighted); (6) **a grounded commentary callout (standing rule 10 — this numbered list is not exhaustive of the shared conventions; commentary is still mandatory here)** — e.g. does the highest-weighted holding also carry a high factor score, or does weight and score diverge; (7) index info (name+code, view, resolved calc date, rebalance effective date). State on the face: how the calc date was derived; that Weight comes from the constituents dataset and Factor from the FIMD dataset, joined by MSCI security code; that a blank Factor cell means unrated / not-mapped, not zero; that weight is market-cap-based among the factor-selected names.

**Metric rule.** Every value is a **direct MCP datapoint**; summaries limited to simple arithmetic (count, mean, min/max, %). These published inputs are NOT the excluded methodology-sensitive analytics — no approximation disclaimer unless the user forces a bespoke risk metric out of them.

**Refresh.** The control re-pulls (Month-end) or re-resolves the rebalance date (Rebalance), re-does the holdings×factor join, and re-renders (data-driven). Allow long round-trips.

**Units.** Factor scores/z-scores are dimensionless (~−3…+3 for z; some transformed). No ×100. Weight is a percentage. See `metric-audit.md`.

**Worked pull (EAFE Quality, 145826, Rebalance view).** Constituents by weight (join target); factor map `["...msci_security_code.rebalancing","...quality_score.rebalancing"]`; join by code; render the holdings by weight with **Security | MSCI code | Weight % | Quality Score (key)**. Weight is market-cap-based among the quality-selected names (note this, so weight vs score is read correctly). Exact calls in `mcp-queries.md` §7.
