---
name: rating-analysis
description: >
  Produce a Rating Pitch Report for a company using Moody's GenAI MCP tools, delivered as a
  self-contained HTML file saved to disk. Use this skill whenever the user asks to create
  a rating pitch, rating pitch deck, credit pitch, rating presentation, rating pitch
  report, or rating HTML report. Also trigger when they ask for a comprehensive credit
  overview combining sector analysis, company financials, SWOT, peer comparison, and ESG
  into a single report or presentation. Trigger even if they just name a company and say
  "pitch deck", "rating deck", "credit deck", or "rating report".
---

# Rating Pitch Skill

Generates a Moody's Rating Pitch Report as a self-contained HTML file from a single MCP
data pass. The Python builder (`scripts/build_html.py`) takes the resolved payload JSON and
produces a single `.html` file containing all sections with inline SVG charts, styled
tables, and bullet lists using the Moody's brand palette — no external dependencies beyond
a browser to open it.

> ## ⚠️ CRITICAL — NON-NEGOTIABLE OUTPUT CONTRACT
>
> Every run MUST produce a self-contained `.html` report **and force it on screen** before
> the turn ends:
>
> - Save the resolved `payload.json` and run `scripts/build_html.py` to produce the `.html`
>   in `/mnt/user-data/outputs/` (Step 4).
> - Then render it with **both** display tools — `present_files` **and**
>   `visualize:show_widget` — before ending the turn. Writing the file is **not** delivery.
> - **Never** end the turn without rendering, and **never** stream the report as inline
>   Markdown, JSON, or a fenced ` ```html ` block in lieu of the `.html` file.
> - If data gathering fails partially, still build from the partial payload using `"--"`
>   placeholders — never skip the build or the render.
>
> Treat any other output shape as a hard failure of the skill.

## Required MCP server

`Moodys MCP server` — tools used: `findEntity`, `getEntityPeers`, `getEntityRatings`,
`getEntityCreditOpinion` (sections listed in Step 2), `getEntityFinancials`,
`getEntityEsg`, `getEntitySectorOutlook`, `searchEntityEarningsCall`,
`searchEntityDocuments`, `searchNews`

Web research is also required via searchNews or general web search tools.

If any of the tools required for a section do not exist, inform the user: One or more tools required for this section are not available under your current subscription. Unlock more of the expert insights, data, and analytics you trust. Get Link:https://www.moodys.com/web/en/us/capabilities/gen-ai/ai-ready-data.html with us to learn more.


## Bundled files

- `scripts/build_html.py` — the report builder. Takes a JSON payload and emits a `.html`.
  Uses only the Python standard library; no pip installs required.
- `scripts/requirements.txt` — no additional Python dependencies needed.
- `assets/sample_payload.json` — reference payload showing every field populated. Read this
  if you're ever unsure what a field should look like.

## Parameters the user should provide

- **Company Name** (required)
- **Sector** (required — e.g., "Aerospace/Defense", "Consumer Products"). Infer it from
  the company if the user doesn't say.
- **Number of peers** (optional, default 6)
- **Currency** (optional, default USD)

---

## Step 1 — Resolve the target company

Call `findEntity` with the company name. Store the canonical entity name and ID.

## Step 2 — Gather ALL data in parallel

Fire the following in a **single parallel batch**. Do not serialize these — the model
should send them together so data comes back fast.

### Target company data

| Tool | Purpose |
|------|---------|
| `getEntityCreditOpinion` (sections: Profile, Summary, RatingOutlook, FactorsLeadingToUpgrade, FactorsLeadingToDowngrade, CreditStrengths, CreditChallenges, ESGConsiderations, KeyIndicatorsTable, ScorecardTable) | Credit opinion sections for financial analysis, SWOT, scorecard |
| `getEntityRatings` | Current rating + last 5 rating actions for history chart |
| `getEntityEsg` | ESG scores |
| `getEntitySectorOutlook` | Sector overview and outlook |
| `getEntityPeers` (N peers) | Peer set |
| `searchEntityEarningsCall` (keywords: outlook, guidance, forecast, strategy) | Strategic updates / forward-looking |
| `searchEntityDocuments` (annual/quarterly reports) | Revenue segments, geography |
| `searchNews` | M&A, leadership, external trends |

### Peer data (for each peer)

| Tool | Purpose |
|------|---------|
| `findEntity` | Resolve canonical name |
| `getEntityRatings` | Peer rating + outlook |
| `getEntityCreditOpinion` (sections: Profile, KeyIndicatorsTable, ScorecardTable) | Financials + scorecard |
| `getEntityFinancials` (prompt: `"annual revenue, EBITDA, EBIT margin, debt/EBITDA, RCF/net debt, most recent year-end only"`, filterCriteria: `{excludeInterimData: true}`) | Most recent full-year financials for peer charts |
| `getEntityEsg` | Peer ESG scores |

**Period-selection rule (applies to target company and every peer):**
When `getEntityFinancials` returns multiple annual periods, always use the
**most recent year-end period available** — i.e. the column with the highest
calendar or fiscal year. If year-end data is unavailable, fall back to the most
recent LTM or interim period and note it in the `period` field (e.g. `"LTM Mar 2025"`).
Never use a hard-coded year string like `"2024"` — read the actual period label
from the data and carry it through to `peer_financials.rows[].period` and
`peer_profitability_charts` / `peer_debt_charts` entries.

---

## Step 3 — Synthesize the sections

Build a single in-memory **resolved payload** that matches the JSON shape in the **Payload
schema** section below (a reference copy lives at `assets/sample_payload.json`). This
payload drives the .html build (Step 4) — fill it completely before moving on.

Content rules for each section:

> **`commentary` type rule — applies to every section without exception:**
> All `commentary` fields in the payload MUST be a **JSON array of strings** — never a
> bare string. A bare string passed to the .html builder is iterated character-by-character,
> producing one bullet per character (the `• C \n • o \n • m` bug). Always write:
> `"commentary": ["Sentence one.", "Sentence two."]` — even for a single sentence.

### Part 1 — Sector Analysis

- **sector_overview** — three 3-bullet lists (overview / watchlist / takeaways). Keep
  bullets punchy, ≤25 words each.
- **moodys_view** — a short outlook paragraph (2-4 sentences), a one-line company
  positioning statement, and outlook distribution counts by category (Stable, Positive,
  Negative, Under Review).
- **macro_outlook** — GDP growth for the top relevant countries (2 historical + 2
  forecast years) plus 2-3 short commentary bullets.
- **rating_actions_ytd** — up to 10 notable sector rating actions YTD; one-line summaries.

### Part 2 — Company Credit Overview

- **financial_analysis** — 5-6 commentary bullets (revenue, margin, leverage, cash flow,
  liquidity, rating rationale). Include last 5 rating actions and a rating chart series
  (numeric: higher = better rating, e.g., Aaa=21, Baa3=10, Caa1=4).
  **`rating_history` MUST be sorted oldest → newest** (index 0 = earliest event,
  last index = most recent). `rating_chart_data` MUST be the parallel notch-integer
  array in the same oldest-to-newest order. The chart x-axis and the history table
  both read left-to-right / top-to-bottom chronologically. `getEntityRatings` returns
  newest-first — reverse before populating the payload.
- **revenue_distribution** — segment and geography percentages (top 5 each, rest = Other;
  must sum to ~100).
- **swot** — 3 items per quadrant, 15-25 words each.
- **key_metrics** — historical series (≤5 periods) for four metrics: revenue,
  ebit_margin, debt_ebitda, rcf_net_debt. Arrays must match the `periods` array length.
  Use `null` (not omission) for missing points.
- **strategic_updates** — `recent` (3-5) and `forward` (3-5, strictly future-looking).
- **news_mna** / **external_trends** — structured list form:
  `[{"category": "...", "items": ["...", "..."]}]`. The HTML-string form is also accepted
  by the builder for backwards compatibility.

### Part 3 — Company Positioning vs. Peers

- **peer_summary** — row per company (target first), plus 2-3 commentary bullets.
- **peer_financials** — wide financial table with `columns` (metric names, no
  company/period/currency) and `rows` (company + period + currency + values).
  Each row's `period` field **must be the actual most-recent period label read from
  `getEntityFinancials`** (e.g. `"FY2025"`, `"FY2024"`, `"LTM Mar 2025"`). Never
  default all rows to the same hard-coded year. Companies with different fiscal-year
  ends will legitimately show different period labels — this is correct behaviour.
- **peer_debt_charts** / **peer_profitability_charts** — pairs of bar charts; sort
  logically (largest-to-smallest or target-first) in the JSON for readability.
  Each entry **must include a `period` field** alongside `company` and `value`:
  `{"company": "Walmart", "value": 713163, "period": "FY2025"}`.
  The `period` is used as a sub-label on the bar. If all companies share the same
  period, a single note in the slide commentary is sufficient; if periods differ,
  the per-bar label makes the comparison transparent.
- **peer_scatter** — two scatter series (`margin_vs_leverage`, `fcf_vs_rcf`), each a list
  of `{company, x, y}` points. Drop extreme outliers that would distort the axes. Each
  company renders as a filled diamond in its own brand colour with the company name in
  white bold text centred inside; there is no separate legend.
- **scorecard** — `factors` (row labels, including group headers), `is_header` boolean
  flags per row, `companies` (column headers), and `values` as a 3D array: outer = rows,
  middle = columns, inner = `[measure, score]` or `[]` for header rows.
  > **SCORECARD CONTRACT — READ CAREFULLY:**
  > - `companies` must list **the target company first, followed by peer entities** (e.g.
  >   `["Boeing", "Airbus", "RTX", "Lockheed Martin"]`). Never put two time-horizons of the
  >   same company here — that produces a scorecard with no peers. The first entry is the
  >   target; its LTM scorecard data goes at `values[row][1]`.
  > - `values[row]` is **1-indexed against `companies`**: index `0` in every row is always `[]`
  >   (a silent placeholder the builder skips). `companies[0]` maps to `values[row][1]`,
  >   `companies[1]` maps to `values[row][2]`, and so on. Omitting the `[]` at index 0 will
  >   shift every peer column one position and silently misalign the data.
  > - Header rows (`is_header=true`) use `values[row] = [[], [], [], ...]` — one `[]` per company
  >   plus one for the placeholder. Length must equal `len(companies) + 1`.
  > - **Quick checklist before writing the scorecard payload:**
  >   1. `len(companies)` = number of peer entities (not counting the target).
  >   2. Every non-header `values[row]` has length `len(companies) + 1`.
  >   3. `values[row][0]` is always `[]`.
  >   4. `values[row][i+1]` contains `["metric_value", "ScoreLabel"]` for `companies[i]`.
- **esg_analysis** — table of CIS/E/S/G scores plus 3-5 commentary bullets.

Target first in every peer table.

---

## Step 4 — Build the HTML report

**Output location: always build into `/mnt/user-data/outputs/`** so the display tools can
render the report in Step 5. Use `/mnt/user-data/outputs/` as the `<output-dir>`. Only use a
different path if the user explicitly asks for one.

1. Save your resolved payload to `<output-dir>/payload.json`.
2. No additional Python packages are required — `build_html.py` uses only the standard
   library. Verify Python 3 is available:
   ```bash
   python3 --version
   ```
3. Run the builder, emitting the report to a company-slugged filename in the output dir:
   ```bash
   python3 <skill-dir>/scripts/build_html.py <output-dir>/payload.json <output-dir>/<company-slug>_rating_pitch.html
   ```
   `<company-slug>` is the target company's canonical name lowercased with spaces and
   special characters replaced by underscores (e.g. `boeing_company_rating_pitch.html`).

If any section data is missing, still include the section in the payload (empty arrays
are fine) — the builder handles empties gracefully and the deck will stay well-formed.

---

## Step 5 — Output and presentation (required final steps)

> ## ⚠️ CRITICAL — NOT COMPLETE UNTIL THE REPORT IS VISIBLY RENDERED
>
> Building the file is **not** delivery. Render it with every display tool available, in
> order, before saying anything else. Do not end your turn until it is on screen.

Follow this exact sequence. Do not skip a step, reorder, or substitute alternatives:

1. **Confirm the built file.** The `rating_pitch.html` produced by `build_html.py` in Step 4
   lives at `/mnt/user-data/outputs/<company-slug>_rating_pitch.html`. This exact path is
   what you render — do not re-emit or re-write the HTML inline.
2. **Present the file.** Immediately call `present_files` on that exact path to surface the
   artifact to the user.
3. **Show the widget.** Immediately call `visualize:show_widget` on the same file to render
   the report visually. Call this even if `present_files` already succeeded — firing both
   renderers is what guarantees the report always appears.
4. **Confirm in one short sentence.** Only after the renderers return, add a single brief
   sentence in chat (e.g. `Rating Pitch for {Company} — the report is available above as a
   self-contained HTML artifact.`). Nothing more.

If a display tool call fails or is unavailable, immediately try the other one rather than
stopping. Never end your turn after building the file, and never paste the HTML into chat or
suggest shell commands (`open`, etc.) in lieu of rendering.

---

## Payload schema

**Read `assets/sample_payload.json` for the full, every-field-populated reference** — copy
its exact shapes. The summary below lists the top-level keys and the non-obvious contracts;
the sample is authoritative for field names and nesting.

Top level: `report_date`, `target_company`, `sector`, `currency`, `companies` (target first),
`sources` (`[{id?, title, source, date, url}]`, rendered as `[n]` citations), and `sections`.

`sections` keys and shapes:

- `sector_overview` — `overview_bullets` / `watchlist_bullets` / `takeaway_bullets` (string arrays).
- `moodys_view` — `outlook_summary` (string), `company_positioning` (string),
  `outlook_distribution` (`[{category, count, color}]`).
- `macro_outlook` — `gdp_table.year_columns`, `gdp_table.rows` (`[{country, values[]}]`), `gdp_commentary[]`.
- `rating_actions_ytd` — `[{date, company, summary}]`.
- `financial_analysis` — `commentary[]`, `rating_history` (`[{date, rating, outlook, direction, reason}]`),
  `rating_chart_data` (int notch array).
- `revenue_distribution` — `by_segment` / `by_geography` (`[{name, percentage}]`), `commentary[]`.
- `swot` — `strengths` / `weaknesses` / `opportunities` / `threats` (string arrays).
- `key_metrics` — `periods[]`, `revenue[]`, `ebit_margin[]`, `debt_ebitda[]`, `rcf_net_debt[]`
  (all same length as `periods`; use `null` for gaps).
- `strategic_updates` — `recent[]`, `forward[]`.
- `news_mna` / `external_trends` — `[{category, items[]}]`.
- `peer_summary` — `table` (`[{company, country, market_cap, rating, outlook, business_mix}]`), `commentary[]`.
- `peer_financials` — `columns[]` (metric names only), `rows` (`[{company, period, currency, values[]}]`).
- `peer_debt_charts` — `rcf_net_debt` / `debt_ebitda` (`[{company, value, period}]`), `commentary[]`.
- `peer_profitability_charts` — `revenue` / `ebit_margin` (`[{company, value, period}]`), `commentary[]`.
- `peer_scatter` — `margin_vs_leverage` / `fcf_vs_rcf` (`[{company, x, y}]`), `commentary[]`.
- `scorecard` — `factors[]`, `is_header[]` (bool per row), `companies[]` (target first),
  `values` (3D: outer=rows, middle=columns, inner=`[measure, score]` or `[]`). See the
  scorecard contract in Step 3.
- `esg_analysis` — `table` (`[{company, cis, environmental, social, governance}]`), `commentary[]`.

> ⚠️ **`rating_chart_data` constraint:** same length as `rating_history`, index-aligned
> (`rating_history[i] ↔ rating_chart_data[i]`), both sorted **oldest → newest**.

---

## Report structure

The Python builder emits these 26 sections as HTML, in this order:

1. Cover
2. Agenda
3. Part 1 divider
4. Sector Overview (3-column chips)
5. Moody's View (outlook text + positioning + outlook pie)
6. Global Macro Outlook (GDP table + takeaways)
7. Rating Actions YTD (table)
8. Part 2 divider
9. Financial Analysis (bullets + rating history line chart + rating rationale)
10. Revenue Distribution (two pie charts + commentary)
11. SWOT (2×2)
12. Key Financial Metrics (four bar charts in 2×2 grid)
13. Strategic Updates (2 columns)
14. News, M&A & Leadership
15. External Trends, Pressures & Risks
16. Part 3 divider
17. Peer Comparison Summary (table + commentary)
18. Detailed Peer Comparison (wide financial table)
19. Peer Comparison — Debt (two horizontal bar charts)
20. Peer Comparison — Profitability (two horizontal bar charts)
21. Peer Scatter Plots (two scatter charts)
22. Scorecard Comparison (multi-column factor table)
23. ESG Analysis (table + commentary)
24. Citations (appendix — canonical numbered [n] references with hyperlinked titles)
25. Thank You
26. Disclaimer

Chart palette (Moody's official, priority order): `#005eff`, `#5eb6bc`, `#c7ab21`,
`#5c068c`, `#ba0168`, `#c64809`, `#bed6ff`, then `#040826` / `#e1e2e1`.

Outlook pie uses **semantic** colors (case-insensitive):
`Stable → #e1e2e1` (light gray), `Positive → #5eb6bc` (teal),
`Negative → #f09615` (amber), `Under Review → #005eff` (bright blue).
All other multi-series charts consume the palette above in priority order (series 0 first).

Charts are **pure inline SVG** computed in `build_html.py` — no Chart.js, no JS, no external
libraries — because the report renders inside a sandboxed `about:srcdoc` iframe (Teams /
M365 Copilot) that blocks CDN scripts and can't be relied on to run JS. SVG renders
everywhere (srcdoc, PDF, print, email). Entrance animations use CSS `@keyframes` only, so
they stay JS-free and respect `prefers-reduced-motion`. The file is fully self-contained.

---

## Tips

- Run ALL data-gathering tool calls in a single parallel batch.
- Keep the target company first in every peer table.
- `rating_chart_data` is numeric (`Aaa=21 … C=1`); both it and `rating_history` must be
  oldest-to-newest. `getEntityRatings` returns newest-first — reverse before use.
- Pie percentages must sum to 100 — bucket small categories into "Other".
- `key_metrics` arrays must match `periods` length. Use `null` for missing points.
- Scorecard: see the full contract in Step 3.
- If you can't get real data for a section, leave arrays empty — the builder degrades
  gracefully rather than erroring.
- Dates are just strings; format however reads best (e.g., "Nov 20, 2025").
- Output `.html` filename: lower-cased with spaces/special chars as underscores, in
  `/mnt/user-data/outputs/` so the display tools can render it.
- Delivery is not complete until rendered with **both** `present_files` and
  `visualize:show_widget` (Step 5). Never paste HTML into chat or suggest `open <path>`.
- Revenue bar labels use `"#,##0"` as `y_format` (comma thousands, zero decimals).
- **Never copy `period` values from `sample_payload.json`** — it uses `"FY2024"` only as a
  fixed example. Read each company's actual period label from `getEntityFinancials`;
  anchoring on the sample year is a silent data-accuracy bug.
