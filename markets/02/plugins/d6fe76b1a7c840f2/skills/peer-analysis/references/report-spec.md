# Peer Analysis — Report Authoring Spec

Detailed body-authoring rules for the Peer Analysis report. Read this before emitting the
HTML artifact. It is authoritative for the Section 1–3 element specs, the streaming protocol
(element → content mapping), the reference HTML snippets, the Ratings-Chart SVG template, the
class-selection rules and conventions, **and the three Amendments that override the base
layout** (kept in their original order at the end). The output contract, MCP tool list,
cover/header fields, and the delivery steps remain in `SKILL.md`.

The target company is always the first column / first row in every table. Inline citations
follow [`references/shared-citations.md`](shared-citations.md); MCP tool names are never
rendered inside `.source-meta`.

---

## Section-by-section authoring

### Section 1 — Peers Comparison Table & Analysis

**1) Peers Table** → `<tbody id="pa-peers-table">`

Write one `<tr>` per company. Two columns: company name + a substantive description paragraph
sourced from the Credit Opinion `Profile` section (headquarters, business overview, key
brands/segments, approximate TTM revenue). Description paragraphs may carry inline citations.

**2) Peers Rating** → `<tbody id="pa-peers-rating">`

Write one `<tr>` per company. Three columns: company name, rating (formatted as
`{rating} ({rating class} / {date})`), and `<span class="outlook-badge …">Outlook</span>`.
Use class rules below.

**3) Credit Drivers** — 5 rows × 4 company columns, pre-shaped `<table>` with per-cell IDs

Write the 4 company header cells first:
- `#pa-cd-col-1` — target name (plain text)
- `#pa-cd-col-2`, `#pa-cd-col-3`, `#pa-cd-col-4` — peer names in order (leave empty if fewer
  than 3 peers were resolved)

Then write the 20 body cells (`#pa-cd-r{1..5}-c{1..4}`). Each cell is a substantive paragraph
with specific quantitative thresholds where available. Cells may carry inline citations:

- Row 1 (`Upgrade factors`) — from `FactorsLeadingToUpgrade`
- Row 2 (`Downgrade factors`) — from `FactorsLeadingToDowngrade`
- Row 3 (`Credit strengths (qualitative)`) — from `CreditStrengths`
- Row 4 (`Credit challenges (qualitative)`) — from `CreditChallenges`
- Row 5 (`Quantitative support (most recent financials in context)`) — from
  `KeyIndicatorsTable`; cite the most recent period's key metrics (debt/EBITDA, EBITA margin,
  EBITA/interest, RCF/net debt, revenue)

If a Credit Opinion section is missing for a company, write `Not available` in the corresponding
cell rather than leaving it blank.

**4) Key Indicators** — 4 rows × 11 columns, pre-shaped `<table>`

For each company row `r ∈ {1..4}` (target = row 1), write the 11 cells:
- `#pa-ki-r{r}-company` — company name
- `#pa-ki-r{r}-v1` — Period (e.g. `2025 FY`)
- `#pa-ki-r{r}-v2` — Revenue (USD)
- `#pa-ki-r{r}-v3` — Total Debt (USD)
- `#pa-ki-r{r}-v4` — EBITA (USD)
- `#pa-ki-r{r}-v5` — EBITA Margin
- `#pa-ki-r{r}-v6` — EBITDA (USD)
- `#pa-ki-r{r}-v7` — Debt/EBITDA
- `#pa-ki-r{r}-v8` — EBITA/Interest
- `#pa-ki-r{r}-v9` — Net LT Debt (USD)
- `#pa-ki-r{r}-v10` — RCF/Net Debt

Source all values from `getEntityFinancials_v2`. If fewer than 3 peers are
resolved, leave the unused row's cells empty.

**5) Scorecards** — 7 rows × 8 sub-columns (4 companies × Current/Forward), pre-shaped `<table>`

Write the 4 top-level company headers first:
- `#pa-sc-col-1` — target name
- `#pa-sc-col-2`, `#pa-sc-col-3`, `#pa-sc-col-4` — peer names

Write the 8 sub-header labels:
- `#pa-sc-col-{1..4}-curr` — current-period label (e.g. `Current 2025 FY`)
- `#pa-sc-col-{1..4}-fwd` — forward-period label (e.g. `Forward`)

Then write the 56 body cells (`#pa-sc-r{1..7}-c{1..4}-curr` and `-fwd`) for the 7 rows:
- Row 1 — Scale: Revenue/Sales (USD bn)
- Row 2 — Profitability: EBIT(A) margin
- Row 3 — Leverage: Debt/EBITDA
- Row 4 — Cash flow: RCF/Net debt
- Row 5 — Coverage: EBIT(A)/Interest
- Row 6 — Scorecard-indicated outcome
- Row 7 — Actual rating

Source from `ScorecardTable` in the Credit Opinion and `getEntityFinancials_v2`

**6) Conclusion** → `#pa-conclusion`

Three `<p>` paragraphs focused on **differentiation** of the target among its peers. Paragraphs
may carry inline citations:

- Paragraph 1: How the target differentiates positively vs. weaker peers on quantitative metrics
  (leverage, coverage, cash flow). Cite specific ratios.
- Paragraph 2: Business risk profile comparison — where the target is more concentrated or less
  diversified vs. stable peers. Reference upgrade/downgrade triggers.
- Paragraph 3: Practical positioning — frame the target's "path to stand out" by linking back
  to the upgrade/downgrade framework and key risk factors.

### Section 2 — Ratings Chart

**Chart** → `#pa-ratings-chart`

Emit a single inline `<svg>` block authored by the agent (see SVG template below). The chart
plots the last 5 rating actions for each company as a line chart. X-axis uses sequential labels
(`Rating 1` … `Rating 5`, most recent first); Y-axis maps Moody's rating symbols to a numeric
scale.

**Analysis** → `#pa-ratings-analysis`

One `<p>` paragraph on rating trajectories — which companies show improvement, deterioration,
or stability, and what that implies for relative credit positioning. May carry inline citations.

### Section 3 — ESG Table & Analysis

**ESG Table** → `<tbody id="pa-esg-table">`

Write one `<tr>` per company. Five columns: company name, Overall (CIS-*), Environmental (E-*),
Social (S-*), Governance (G-*).

**Analysis** → `#pa-esg-analysis`

Two `<p>` paragraphs. Paragraphs may carry inline citations:

- Paragraph 1: Compare ESG profiles across the peer set. Identify which companies share similar
  profiles and what drives the overall classification.
- Paragraph 2: Highlight the key differentiator (typically Governance) and explain which company
  stands out as weaker/stronger and why.

### Citations & sources (write last)

- `#pa-cite-peers` — optional `<div class="section-citations">…</div>` recap for the
  peers-comparison section. Use the markup defined in
  [references/shared-citations.md](references/shared-citations.md). Omit if empty.
- `#pa-cite-ratings` — optional recap for the ratings-chart section. Same markup.
- `#pa-cite-esg` — optional recap for the ESG section. Same markup.
- `#pa-sources` — end-of-document Citations rows. One `<div class="source-item">` per source,
  in `[1], [2], …` order, using the canonical row markup from the shared citations skill.
  Internal MCP tool names are NEVER rendered in `.source-meta`.

---

## Streaming protocol (element → content mapping)

| Element ID                                           | Content type                                                           |
|------------------------------------------------------|------------------------------------------------------------------------|
| `#pa-report-date`                                    | Plain text date                                                        |
| `#pa-footer-date`                                    | Plain text date (same value)                                           |
| `#pa-target-company`                                 | Plain text (canonical target name)                                     |
| `#pa-peer-count`                                     | Plain text integer                                                     |
| `#pa-company-chips`                                  | `<span class="company-chip target">` + `<span class="company-chip">`s  |
| `#pa-cover-img-right`, `#pa-cover-img-bottom`        | `<img>` element — set `src` attribute                                  |
| `<tbody id="pa-peers-table">`                        | `<tr>` rows (company name + description) with inline citations         |
| `<tbody id="pa-peers-rating">`                       | `<tr>` rows with `<span class="outlook-badge …">`                      |
| `#pa-cd-col-1` … `#pa-cd-col-4`                      | Plain text (company names)                                             |
| `#pa-cd-r{1..5}-c{1..4}`                             | Prose cell content (short `<p>` or plain text) with inline citations   |
| `#pa-ki-r{1..4}-company`                             | Plain text (company name)                                              |
| `#pa-ki-r{1..4}-v{1..10}`                            | Plain text (period / metric value)                                     |
| `#pa-sc-col-1` … `#pa-sc-col-4`                      | Plain text (company names, span 2 sub-columns)                         |
| `#pa-sc-col-{1..4}-curr`, `#pa-sc-col-{1..4}-fwd`    | Plain text sub-header labels (Current / Forward period)                |
| `#pa-sc-r{1..7}-c{1..4}-curr`, `…-fwd`               | Plain text scorecard cell values                                       |
| `#pa-conclusion`                                     | Three `<p>` paragraphs with inline citations                           |
| `#pa-ratings-chart`                                  | Single `<div class="chart-container">…<svg>…</svg>…</div>` block       |
| `#pa-ratings-analysis`                               | One `<p>` paragraph with inline citations                              |
| `<tbody id="pa-esg-table">`                          | `<tr>` rows (company + overall + E + S + G)                            |
| `#pa-esg-analysis`                                   | Two `<p>` paragraphs with inline citations                             |
| `#pa-cite-peers`, `#pa-cite-ratings`, `#pa-cite-esg` | `<div class="section-citations">…</div>` (optional, see shared citations skill) |
| `#pa-sources`                                        | `<div class="source-item">` rows (see shared citations skill)          |

If fewer than 3 peers are returned, leave unused column/row IDs empty. Do not collapse or remove
cells — the pre-shaped table simply keeps those cells blank.

### Reference HTML snippets

**Peers table row** (`<tbody id="pa-peers-table">`):

```html
<tr>
  <td class="company-name">Target Co</td>
  <td>Headquartered in Dearborn, Michigan, Target Co is a global automaker with TTM revenue of approximately $180B <a href="https://example.com/credit-opinion-target" target="_blank" class="cite-ref">[1]</a>, anchored by its F-Series, SUV, and Pro commercial businesses <a href="https://example.com/profile-target" target="_blank" class="cite-ref">[2]</a>.</td>
</tr>
```

**Peers rating row** (`<tbody id="pa-peers-rating">`):

```html
<tr>
  <td class="company-name">Target Co</td>
  <td>Baa3 (Senior Unsecured - Dom Curr / 2024-05-09)</td>
  <td><span class="outlook-badge stable">Stable</span></td>
</tr>
```

**Company chips** (`#pa-company-chips`):

```html
<span class="company-chip target">Target Co</span>
<span class="company-chip">Peer One</span>
<span class="company-chip">Peer Two</span>
<span class="company-chip">Peer Three</span>
```

**ESG table row** (`<tbody id="pa-esg-table">`):

```html
<tr>
  <td class="company-name">Target Co</td>
  <td>CIS-3</td>
  <td>E-4</td>
  <td>S-3</td>
  <td>G-2</td>
</tr>
```

**Credit Drivers — per-cell write** (repeat for each of the 20 body cells):

```html
Leverage sustained below 2.5x Debt/EBITDA, EBITA margin above 7%, and sustained positive free cash flow after dividends <a href="https://example.com/credit-opinion-target" target="_blank" class="cite-ref">[1]</a>.
```

**Conclusion paragraph** (inside `#pa-conclusion`, same inline-citation pattern applies to
`#pa-ratings-analysis` and `#pa-esg-analysis`):

```html
<p>On pure quantitative credit metrics, Target Co stands out decisively: Debt/EBITDA of 0.7x and EBITA/Interest of 27x are in line with the strongest-scoring peers, while its scale advantage (LTM revenue of $294B vs. $61B and $23B for the peer set) and FCF/Debt of 41% add a differentiation layer the others cannot match <a href="https://example.com/credit-opinion-target" target="_blank" class="cite-ref">[1]</a><a href="https://example.com/peer-ratings" target="_blank" class="cite-ref">[2]</a>.</p>
```

**Key Indicators — single row** (emit the full `<tr>` for each company inside the
`#pa-key-indicators` table, keeping the per-cell `id` attributes intact):

```html
<tr>
  <td id="pa-ki-r1-company">Target Co</td>
  <td id="pa-ki-r1-v1">LTM (30 Sep 2025)</td>
  <td id="pa-ki-r1-v2">180.2B</td>
  <td id="pa-ki-r1-v3">155.6B</td>
  <td id="pa-ki-r1-v4">7.8B</td>
  <td id="pa-ki-r1-v5">4.33%</td>
  <td id="pa-ki-r1-v6">13.1B</td>
  <td id="pa-ki-r1-v7">11.88x</td>
  <td id="pa-ki-r1-v8">3.62x</td>
  <td id="pa-ki-r1-v9">136.0B</td>
  <td id="pa-ki-r1-v10">18.5%</td>
</tr>
```

**Scorecard — per-cell write** (Current or Forward):

```html
2.7x
```

**Section citations recap** (`#pa-cite-peers`, `#pa-cite-ratings`, `#pa-cite-esg`) and
**sources rows** (`#pa-sources`): see
[references/shared-citations.md](references/shared-citations.md) for the canonical markup.
Reuse the same `[n]` numbering across inline references, optional recap blocks, and the
end-of-document Citations block. Never include MCP tool names in `.source-meta`.

---

## Ratings Chart SVG template

Emit the entire chart as a single HTML string into `#pa-ratings-chart`. The agent authors the
SVG directly — there is no runtime script.

### Hardcoded constants

- Dimensions: `W = 700`, `H = 350`
- Padding: `PAD_L = 70`, `PAD_R = 30`, `PAD_T = 30`, `PAD_B = 50`
- Plot area: width `= W - PAD_L - PAD_R = 600`, height `= H - PAD_T - PAD_B = 270`
- Number of x-axis points: `maxPts` = the largest number of ratings any company has, capped at 5
- Palette (first = target): `#0066cc`, `#e6550d`, `#1a7a4a`, `#8b5cf6`, `#d63384`

### Moody's rating → numeric value map

| Rating | Value | Rating | Value |
|--------|-------|--------|-------|
| Aaa | 21 | Ba1 | 11 |
| Aa1 | 20 | Ba2 | 10 |
| Aa2 | 19 | Ba3 | 9 |
| Aa3 | 18 | B1 | 8 |
| A1 | 17 | B2 | 7 |
| A2 | 16 | B3 | 6 |
| A3 | 15 | Caa1 | 5 |
| Baa1 | 14 | Caa2 | 4 |
| Baa2 | 13 | Caa3 | 3 |
| Baa3 | 12 | Ca | 2 |
|     |    | C | 1 |

`RATING_LABELS` (index 0..20 → symbol): `["C", "Ca", "Caa3", "Caa2", "Caa1", "B3", "B2", "B1", "Ba3", "Ba2", "Ba1", "Baa3", "Baa2", "Baa1", "A3", "A2", "A1", "Aa3", "Aa2", "Aa1", "Aaa"]`.

### Coordinate formulae

Compute once per chart:

- Collect every rating value across all companies' last-5 series → `values[]`.
- `minV = clamp(min(values) - 1, 1, 21)`
- `maxV = clamp(max(values) + 1, 1, 21)` (ensure `maxV > minV`; if equal, set `maxV = minV + 1`)

Per point `(i, v)` where `i` is the x-index (0-based) and `v` is the rating value:

- `xPos(i) = PAD_L + (i / (maxPts - 1)) * 600` = `70 + (i / (maxPts - 1)) * 600`
- `yPos(v) = PAD_T + 270 - ((v - minV) / (maxV - minV)) * 270` = `30 + 270 - ((v - minV) / (maxV - minV)) * 270`

### Reference SVG block

```html
<div class="chart-container">
  <div class="chart-title">Last 5 Ratings for Target and Peers</div>
  <svg viewBox="0 0 700 350" width="100%" preserveAspectRatio="xMidYMid meet">
    <!-- Horizontal gridlines + y-axis rating labels (one line + label per rating tick from minV to maxV) -->
    <line x1="70" y1="30"  x2="670" y2="30"  stroke="#e5e7eb" stroke-width="1"/>
    <text x="64" y="34" text-anchor="end" font-size="10" fill="#475569">Baa1</text>
    <line x1="70" y1="84"  x2="670" y2="84"  stroke="#e5e7eb" stroke-width="1"/>
    <text x="64" y="88" text-anchor="end" font-size="10" fill="#475569">Baa2</text>
    <line x1="70" y1="138" x2="670" y2="138" stroke="#e5e7eb" stroke-width="1"/>
    <text x="64" y="142" text-anchor="end" font-size="10" fill="#475569">Baa3</text>
    <line x1="70" y1="192" x2="670" y2="192" stroke="#e5e7eb" stroke-width="1"/>
    <text x="64" y="196" text-anchor="end" font-size="10" fill="#475569">Ba1</text>
    <line x1="70" y1="246" x2="670" y2="246" stroke="#e5e7eb" stroke-width="1"/>
    <text x="64" y="250" text-anchor="end" font-size="10" fill="#475569">Ba2</text>
    <line x1="70" y1="300" x2="670" y2="300" stroke="#e5e7eb" stroke-width="1"/>
    <text x="64" y="304" text-anchor="end" font-size="10" fill="#475569">Ba3</text>

    <!-- X-axis baseline + tick labels -->
    <line x1="70" y1="300" x2="670" y2="300" stroke="#334155" stroke-width="1.5"/>
    <text x="70"  y="320" text-anchor="middle" font-size="10" fill="#475569">Rating 1</text>
    <text x="220" y="320" text-anchor="middle" font-size="10" fill="#475569">Rating 2</text>
    <text x="370" y="320" text-anchor="middle" font-size="10" fill="#475569">Rating 3</text>
    <text x="520" y="320" text-anchor="middle" font-size="10" fill="#475569">Rating 4</text>
    <text x="670" y="320" text-anchor="middle" font-size="10" fill="#475569">Rating 5</text>

    <!-- Target company line (palette[0] = #0066cc) -->
    <path d="M70,138 L220,138 L370,192 L520,192 L670,192"
          fill="none" stroke="#0066cc" stroke-width="2.5"/>
    <circle cx="70"  cy="138" r="4" fill="#0066cc"/>
    <circle cx="220" cy="138" r="4" fill="#0066cc"/>
    <circle cx="370" cy="192" r="4" fill="#0066cc"/>
    <circle cx="520" cy="192" r="4" fill="#0066cc"/>
    <circle cx="670" cy="192" r="4" fill="#0066cc"/>

    <!-- Repeat <path>+<circle>s for peers 2, 3, 4 using palette[1..3] -->
  </svg>
  <div class="chart-legend">
    <div class="chart-legend-item"><span class="chart-legend-swatch" style="background:#0066cc"></span>Target Co</div>
    <div class="chart-legend-item"><span class="chart-legend-swatch" style="background:#e6550d"></span>Peer One</div>
    <div class="chart-legend-item"><span class="chart-legend-swatch" style="background:#1a7a4a"></span>Peer Two</div>
    <div class="chart-legend-item"><span class="chart-legend-swatch" style="background:#8b5cf6"></span>Peer Three</div>
  </div>
</div>
```

### Class-selection rules

**`.outlook-badge`** modifier (inside peers-rating rows):

- `stable` — outlook is "Stable"
- `positive` — outlook is "Positive"
- `negative` — outlook is "Negative"
- `review` — outlook contains "Review" (e.g., "Rating Under Review")
- `na` — outlook is missing or unknown

**`.company-chip.target`** applies only to the target (first) chip. Remaining chips use plain
`.company-chip`.

### Conventions

- Use `<p>` for paragraphs, `<ul><li>` for bullets, `<strong class="subsection-title">…</strong>`
  for bold subheaders inside prose containers.
- Emit inline citations per [references/shared-citations.md](references/shared-citations.md).
  Inline citations are the primary attribution mechanism — the optional per-section blocks
  (`#pa-cite-peers`, `#pa-cite-ratings`, `#pa-cite-esg`) remain available as supplementary
  summary boxes.
- Do NOT include overall section titles — the template already has those.
- `rating` values: use Moody's rating symbol (e.g. `Aaa`, `Aa1`, `Baa2`, `Ba1`). If not found,
  use `N/A`.
- `outlook` values: `Stable`, `Positive`, `Negative`, `Rating Under Review`, or `N/A`.

---

---

## Amendments (apply these — they override the base layout above)

## Amendment: Always use the most recent fiscal year for Key Indicators and Scorecards

When populating the Key Indicators table (`#pa-ki-r{1..4}-*`) and the Scorecard table
(`#pa-sc-r{1..7}-c{1..4}-curr`), always use the **most recent fiscal year-end (FY) data
available** from `getEntityFinancials_v2` — never default to an earlier year simply because
the credit opinion's Key Indicators table cites it, or because one peer's most recent year
differs from another's.

### Procedure

1. After calling `getEntityFinancials_v2` with `excludeInterimData: true`, inspect the
   returned columns for each entity and identify the **latest year with a non-null Revenue
   value** — that is the most recent fiscal year end for that entity.
2. Use that year's figures for the Key Indicators table and the "Current" column of the
   Scorecard, regardless of what year the credit opinion's exhibit uses.
3. If different entities have different most-recent years (e.g. one entity has 2025 data
   while another only has 2024), use each entity's own most recent year independently and
   label the `#pa-ki-r{n}-v1` cell accordingly (e.g. `2025 FY` vs `2024 FY`).

### Handling distorted EBITDA years

If the most recent fiscal year contains a non-cash charge (e.g. goodwill impairment) that
makes reported EBITDA or Debt/EBITDA not meaningful on a reported basis:
- Still use that year as the period reference.
- Populate EBITDA and ratio cells with the reported figure plus a `†` marker (e.g.
  `-$1.6B†`, `N/M†`).
- Add a footnote below the Key Indicators table explaining the distortion and citing the
  Moody's-adjusted figure where available from the credit opinion.
- Use the Moody's-adjusted ratio (from the credit opinion's Key Indicators table) for the
  Scorecard leverage cell rather than the distorted reported figure.

---

## Amendment: Visual Enhancements

Three additional visual components are added to the report. Emit them inline as part of the
single HTML artifact (same non-negotiable output contract applies). All new elements use only
the CSS classes already defined in `assets/template.html` — no external scripts or libraries.

---

### Visual 1 — Rating Summary Cards (`#pa-rating-cards`)

Placed **immediately after** the Peers Rating table (sub-heading 2), before sub-heading 3
(Credit Drivers). Emit one `.rating-card` per company (target first, then peers in order).
The target card carries the extra class `target-card`.

**What to populate:**
- `.rc-company` — abbreviated company name (≤ 25 chars; truncate with "…" if longer)
- `.rc-rating` — Moody's rating symbol (e.g. `Baa2`)
- `.rc-class` — rating class + date (e.g. `Senior Unsecured / 2024-05-09`)
- `.outlook-badge` — outlook badge using the canonical pastel classes (`stable`, `positive`,
  `negative`, `review`, `na`)

**Reference snippet** (emit one block like this per company inside `#pa-rating-cards`):

```html
<div class="rating-card target-card">
  <div class="rc-company">Target Co</div>
  <div class="rc-rating">Baa2</div>
  <div class="rc-class">Senior Unsecured / 2024-05-09</div>
  <span class="outlook-badge stable">Stable</span>
</div>
```

---

### Visual 2 — Financial Comparison Bar Charts (`#pa-fi-charts`)

Placed **immediately after** the Key Indicators table (sub-heading 4), before sub-heading 5
(Scorecards). Emit a two-column grid (`div.fi-chart-grid`) containing exactly **two**
`div.fi-chart-box` blocks:

1. **Revenue** — horizontal bar chart comparing Revenue (USD) for all companies
2. **Debt/EBITDA** — horizontal bar chart comparing Debt/EBITDA ratio for all companies

For each chart, the widths are proportional: the company with the largest value gets a
`fi-bar-fill` width of `100%`; all others are scaled relative to that maximum.

**Colour palette** (same as the ratings chart): target = `#0066cc`, peer 1 = `#e6550d`,
peer 2 = `#1a7a4a`, peer 3 = `#8b5cf6`. Assign colours in the same company order as all
other tables (target first).

**Values:** source from `getEntityFinancials_v2` (same figures used in Key Indicators).
Format Revenue as `$XB` or `$XM`; Debt/EBITDA as `X.Xx`.

If a value is missing or `N/A`, set `fi-bar-fill` width to `0%` and display `N/A` in
`.fi-bar-value`.

**Reference snippet** for one chart box (repeat once for Revenue, once for Debt/EBITDA):

```html
<div class="fi-chart-box">
  <div class="fi-chart-title">Revenue (USD)</div>
  <div class="fi-bar-row">
    <span class="fi-bar-label">Target Co</span>
    <div class="fi-bar-track"><div class="fi-bar-fill" style="width:100%;background:#0066cc;"></div></div>
    <span class="fi-bar-value">$180B</span>
  </div>
  <div class="fi-bar-row">
    <span class="fi-bar-label">Peer One</span>
    <div class="fi-bar-track"><div class="fi-bar-fill" style="width:34%;background:#e6550d;"></div></div>
    <span class="fi-bar-value">$61B</span>
  </div>
  <div class="fi-bar-row">
    <span class="fi-bar-label">Peer Two</span>
    <div class="fi-bar-track"><div class="fi-bar-fill" style="width:13%;background:#1a7a4a;"></div></div>
    <span class="fi-bar-value">$23B</span>
  </div>
  <div class="fi-bar-row">
    <span class="fi-bar-label">Peer Three</span>
    <div class="fi-bar-track"><div class="fi-bar-fill" style="width:20%;background:#8b5cf6;"></div></div>
    <span class="fi-bar-value">$36B</span>
  </div>
</div>
```

Omit bar rows for companies that were not resolved (fewer than 3 peers).

---

### Visual 3 — ESG Score Heatmap (`#pa-esg-heatmap`)

Placed **immediately after** the ESG table, before `#pa-esg-analysis`. Emit a colour-coded
HTML table (inside `div.esg-heatmap`) that makes the CIS and sub-scores scannable at a glance.

**Colour mapping** — apply a CSS class to each score `<td>` based on numeric severity
(lower CIS/sub-score = better):

| Score | Class | Meaning |
|-------|-------|---------|
| 1 | `esg-s1` | Green — minimal risk |
| 2 | `esg-s2` | Light green — limited risk |
| 3 | `esg-s3` | Amber — moderate risk |
| 4 | `esg-s4` | Orange — high risk |
| 5 | `esg-s5` | Red — very high risk |

Parse the numeric suffix from the Moody's score string (e.g. `CIS-3` → 3, `E-4` → 4).
If the score is `N/A` or missing, omit the colour class (plain white cell).

**Reference snippet:**

```html
<table>
  <thead>
    <tr>
      <th>Company</th>
      <th>CIS (Overall)</th>
      <th>E Score</th>
      <th>S Score</th>
      <th>G Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Target Co</td>
      <td class="esg-s3">CIS-3</td>
      <td class="esg-s4">E-4</td>
      <td class="esg-s3">S-3</td>
      <td class="esg-s2">G-2</td>
    </tr>
    <!-- one <tr> per company, same order as all other tables -->
  </tbody>
</table>
```

---

### Updated element ID mapping (addendum)

| Element ID / selector          | Content                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| `#pa-rating-cards`            | `.rating-card` divs — one per company (target first)                   |
| `#pa-fi-charts`               | Two `.fi-chart-box` divs inside `.fi-chart-grid` (Revenue, Debt/EBITDA)|
| `#pa-esg-heatmap`             | `.esg-heatmap` table with colour-coded CIS / E / S / G scores          |

---

## Amendment: Section Layout, Ratings Chart, and ESG Display Overrides

### Section 1 — Revised sub-section order

Emit sub-sections in this exact order:

1. **Peers Table** (`<tbody id="pa-peers-table">`) — unchanged, as defined above.
2. **Rating Cards only** (`#pa-rating-cards`) — emit the `.rating-card` blocks as defined in
   Visual 1. **Do NOT emit the `<tbody id="pa-peers-rating">` table at all.** The cards are the
   sole representation of peer ratings in Section 1.
3. **Credit Drivers table** — unchanged, as defined above.
4. **Key Indicators table** + **Financial Comparison Bar Charts** (`#pa-fi-charts`) — unchanged,
   both emitted as defined above (table first, then the two bar-chart boxes).
5. **Scorecard table** — unchanged, as defined above.
6. **Conclusion** (`#pa-conclusion`) — unchanged.

The `<table>` element whose `<tbody>` carries `id="pa-peers-rating"` must be **omitted entirely**
from the emitted HTML. Do not render it, do not hide it with CSS, do not leave an empty wrapper.

---

### Section 2 — Enhanced Ratings Chart

Replace the plain SVG line chart described earlier with the enhanced version below. The output
must still be emitted inline inside `#pa-ratings-chart`.

**Design goals:** visually polished, readable at a glance, clearly differentiates companies with
colour and shape, highlights the most-recent rating prominently.

**Layout — SVG viewBox `"0 0 780 400"`:**

- Left padding (y-axis labels): 80 px
- Right padding: 30 px
- Top padding: 40 px
- Bottom padding (x-axis labels + legend): 60 px
- Plot area: 670 × 300 px (x: 80→750, y: 40→340)

**Y-axis:** draw one horizontal gridline + label per rating tier present in the data set (use the
`minV`→`maxV` range from the coordinate formulae above, but now label with the Moody's symbol,
not a number). Gridlines are `stroke="#e5e7eb"`. Labels are `font-size="11"`, `fill="#64748b"`,
`text-anchor="end"` at `x="74"`.

**X-axis:** draw the baseline (`stroke="#334155"`, `stroke-width="1.5"`). Label each point with
the **actual rating date** (formatted `MMM YYYY`, e.g. `Jan 2023`) instead of `Rating N`.
Labels `font-size="10"`, `fill="#64748b"`, `text-anchor="middle"`, `y="358"`.

**Lines:** `stroke-width="2.5"`, rounded joins (`stroke-linejoin="round"`, `stroke-linecap="round"`).

**Data points:** each rating action is a `<circle r="5">` filled with the company colour. The
**most-recent point** (rightmost) for each company is instead a `<circle r="7">` with a white
inner ring — achieved by stacking a white `<circle r="4" fill="white"/>` on top of the coloured
outer circle. Add a `<title>` element inside each point group for tooltip text:
`{company} · {rating symbol} · {date}`.

**Value labels:** above each data point, emit a `<text>` showing the Moody's rating symbol
(`font-size="9"`, `fill` = company colour, `text-anchor="middle"`, `dy="-10"`). Suppress the
label if it would overlap a neighbour (points within 40 px horizontally from the same series can
share a label only at the leftmost occurrence; skip the rest in that cluster).

**Colour palette:** same as all other charts — target `#0066cc`, peer 1 `#e6550d`,
peer 2 `#1a7a4a`, peer 3 `#8b5cf6`.

**Legend:** emit below the SVG as a `<div class="chart-legend">` row (same pattern as before),
but add the actual current rating symbol in parentheses after each company name, e.g.
`Target Co (Baa2)`.

**Reference snippet** (abbreviated — fill in real coordinates from the formulae):

```html
<div class="chart-container">
  <div class="chart-title">Rating History — Last 5 Actions</div>
  <svg viewBox="0 0 780 400" width="100%" preserveAspectRatio="xMidYMid meet">

    <!-- Gridlines + Y-axis labels -->
    <line x1="80" y1="40"  x2="750" y2="40"  stroke="#e5e7eb" stroke-width="1"/>
    <text x="74" y="44"  text-anchor="end" font-size="11" fill="#64748b">Baa1</text>
    <!-- … one per tier … -->

    <!-- X-axis baseline -->
    <line x1="80" y1="340" x2="750" y2="340" stroke="#334155" stroke-width="1.5"/>
    <!-- X-axis date labels -->
    <text x="80"  y="358" text-anchor="middle" font-size="10" fill="#64748b">Jan 2021</text>
    <!-- … -->

    <!-- Target company — line -->
    <path d="M80,192 L247,192 L415,138 L582,138 L750,138"
          fill="none" stroke="#0066cc" stroke-width="2.5"
          stroke-linejoin="round" stroke-linecap="round"/>
    <!-- Rating labels above points -->
    <text x="80"  y="182" text-anchor="middle" font-size="9" fill="#0066cc">Baa2</text>
    <!-- Regular points -->
    <circle cx="80"  cy="192" r="5" fill="#0066cc"/>
    <circle cx="247" cy="192" r="5" fill="#0066cc"/>
    <circle cx="415" cy="138" r="5" fill="#0066cc"/>
    <circle cx="582" cy="138" r="5" fill="#0066cc"/>
    <!-- Most-recent point (highlighted) -->
    <circle cx="750" cy="138" r="7" fill="#0066cc"/>
    <circle cx="750" cy="138" r="4" fill="white"/>
    <title>Target Co · Baa1 · Mar 2025</title>

    <!-- Repeat for each peer with palette[1..3] -->
  </svg>
  <div class="chart-legend">
    <div class="chart-legend-item">
      <span class="chart-legend-swatch" style="background:#0066cc"></span>Target Co (Baa1)
    </div>
    <div class="chart-legend-item">
      <span class="chart-legend-swatch" style="background:#e6550d"></span>Peer One (Ba1)
    </div>
    <!-- … -->
  </div>
</div>
```

---

### Section 3 — ESG: Heatmap Only

**Do NOT emit the plain `<table>` whose `<tbody>` carries `id="pa-esg-table"`**. Remove it
entirely from the output HTML — do not render it, do not hide it.

Instead, emit **only** the colour-coded heatmap table (`#pa-esg-heatmap`, as defined in
Visual 3 above) as the sole ESG data table. Follow it immediately with `#pa-esg-analysis`.

The heatmap already contains all the same data (company, CIS, E, S, G scores) in a more
readable, colour-coded format; the plain table is redundant and must be omitted.

**Revised Section 3 emit order:**

1. `#pa-esg-heatmap` (colour-coded heatmap table — the only ESG table)
2. `#pa-esg-analysis` (two analysis paragraphs, unchanged)
3. Optional `#pa-cite-esg` recap block (if citations are present)

---

### Summary of omissions (do NOT emit these elements)

| Element | Reason |
|---|---|
| `<table>` wrapping `<tbody id="pa-peers-rating">` | Replaced by rating cards |
| `<table>` wrapping `<tbody id="pa-esg-table">` | Replaced by ESG heatmap |
