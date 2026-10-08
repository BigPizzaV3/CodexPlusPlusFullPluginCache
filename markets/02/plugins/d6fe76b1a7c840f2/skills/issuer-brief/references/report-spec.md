# Issuer Brief — Report Authoring Spec

Detailed body-authoring rules for the Issuer Brief report. Read this before emitting the
HTML artifact. It is authoritative for the per-section element specs (Sections 1–11), the
streaming protocol (element → content mapping), the reference markup snippets, the SVG chart
templates, the class-selection rules, and the per-section citation-recap letter mapping. The
output contract, the **no estimated/approximated numbers** contract, the MCP tool list, and
cover/footer fields remain in `SKILL.md`.

Every numeric value must come directly from a Moody's MCP tool response or a
`searchCompanyFilings` filing — never estimated. Inline citations follow
[`references/shared-citations.md`](shared-citations.md); never place citation markup inside
data cells.

---

## Section-by-section authoring

### Section 1 — Company Overview

5. `#pib-overview-kpi` — KPI scorecard strip: a row of exactly 4 metric cards rendered as an
   inline SVG (`width="780" height="90"`). Each card shows a metric name (top, small caps) and
   value (bottom, bold). Source the four metrics from `getEntityFinancials_v2` and `getEntityRatings`:
   (1) Revenue (LTM, in billions, e.g. `$412.3B`), (2) EBITDA Margin (LTM, e.g. `31.2%`),
   (3) Net Debt / EBITDA (LTM, e.g. `1.8×`), (4) Moody's Rating (current long-term rating,
   e.g. `Aa1`). Cards are evenly spaced; use a light `#f4f6f9` fill with a `#0066cc` left-border
   accent (4 px). Render inside `<div class="chart-container">…</div>`.

   SVG layout constants: `W=780`, `H=90`, 4 cards each `cardW=170`, `gap=16`,
   total cards span = `4×170 + 3×16 = 728`, left offset `ox = (780−728)/2 = 26`.
   Card `x` for card `i` (0-indexed) = `ox + i×(170+16)`.
   Per card: background `<rect>` at card x, y=10, w=170, h=70, fill `#f4f6f9`, rx=4;
   accent `<rect>` at card x, y=10, w=4, h=70, fill `#0066cc`, rx=2;
   label `<text>` at card x+14, y=32, font-size=10, fill=`#6b7280`, font-weight=600 (metric name);
   value `<text>` at card x+14, y=58, font-size=20, fill=`#00205b`, font-weight=700 (metric value).

6. `#pib-overview-rating-timeline` — Rating upgrade timeline showing Moody's rating history as a
   horizontal step-line SVG. Source rating history from `getEntityRatings`. Constants:
   `W=780`, `H=160`; padding `{top:30, right:30, bottom:50, left:70}`; plot area `cW=680`, `cH=80`.
   X-axis = dates of rating changes (oldest left, most recent right). Y-axis = ordinal rating scale
   (map ratings to numeric rank: Aaa=1, Aa1=2, Aa2=3, Aa3=4, A1=5, A2=6, A3=7, Baa1=8, Baa2=9,
   Baa3=10, Ba1=11, Ba2=12, Ba3=13, B1=14, B2=15, B3=16, Caa1=17 … show only ratings present
   in history on the y-axis). Draw as a step-line: horizontal segment at rating level, then
   vertical drop/rise at the change date. Stroke `#0066cc`, stroke-width=2, fill=none.
   Place a filled circle (`r=4`, fill=`#0066cc`) at each rating-change point and a label above
   (font-size=10, fill=`#00205b`, font-weight=600) showing the rating symbol.
   X-axis labels: year of each change, rotated `-30°`. Y-axis labels: rating symbols at each
   tick. Title: `<text x="390" y="16" text-anchor="middle" font-size="11" fill="#00205b"
   font-weight="700">Moody's Rating History</text>`. Render inside `<div class="chart-container">`.

7. `#pib-overview` — **2–3 paragraphs** in `<p>…</p>` covering: (1) opening statement of
   significance, founding info, headquarters, and core business; (2) industry position, key
   products/services, and target markets; (3) financial overview snapshot (revenue, margins, key
   metrics) and strategic priorities. No bullet points, no bold text in the body. Use hyperlinked
   inline citations per the shared citations skill.

### Section 2 — Business Segments and Operations

Revenue per segment **must be sourced exclusively from `searchCompanyFilings`** (annual or
quarterly company filings) to ensure consistency with reported company data. Do **not** use
earnings call data or Moody's estimates for segment revenue figures.

8. `#pib-segments-intro` — one introductory paragraph in `<p>…</p>`.
9. `#pib-segments-pie` — revenue-by-segment **bar chart** rendered as an inline SVG. Constants:
   `W=600`, `H=320`; padding `{top:40, right:20, bottom:80, left:80}`; plot area `cW=500`, `cH=200`.
   Let `N` = number of segments. `bw = min(cW / N × 0.6, 60)`; `gap = (cW − bw × N) / (N + 1)`.
   `mx = max(revenue values)`; `yPos(v) = 40 + 200 − (v / mx) × 200`.
   Bar `x` for segment `i` (0-indexed) = `80 + gap × (i + 1) + bw × i`.
   **If you do not have a calculator tool, use bash or Python to compute all of the above values before emitting any SVG — do not attempt to calculate them mentally.**
   Fill each bar with the palette in index order: `#0066cc, #e74c3c, #27ae60, #f39c12, #8e44ad, #16a085`.
   Emit the revenue value (in the same unit as the pie, e.g. `$12.3B` or `XX%`) above each bar,
   centred on the bar (`text-anchor="middle"`, font-size=10, fill=`#444c58`).
   Emit the segment name below the x-axis baseline, centred on the bar, rotated `-30°`
   (font-size=10, fill=`#444c58`).
   Draw the x-axis baseline: `<line x1="80" y1="240" x2="580" y2="240" stroke="#9aa0ab"/>`.
   Title: `<text x="300" y="24" text-anchor="middle" font-size="12" fill="#00205b"
   font-weight="700">Revenue by Segment</text>`.
   Render inside `<div class="chart-container">`.
11. `#pib-segments-list` — one `<li>` per segment. Each `<li>` must contain a
    `<strong>Segment Name</strong>` header followed by **one paragraph** of prose describing the
    segment's business activities, key products/services, end markets, and revenue contribution.
    Revenue figures cited must match those sourced from company filings used in the pie chart.
    Structure: `<li><strong>Segment Name</strong><p>Description paragraph with revenue
    context…</p></li>`.
12. `#pib-segments-outro` — one closing paragraph in `<p>…</p>`.

### Section 3 — Historical Financials

**ALL numeric values in the financial table MUST be populated exclusively from data returned by
the `getEntityFinancials_v2` MCP tool.** Do not supplement or override table cells with figures
from earnings calls, credit opinions, news, or any other source. If a value is not available in
`getEntityFinancials_v2`, write `"--"` in that cell. This ensures every number is factual and
verifiable from Moody's MCP data. Annual columns are limited to exactly 3 full fiscal years (oldest → most recent). Include a single YoY% column calculated **only between the last two fully completed years** (FY−1 vs FY), and an LTM column. **Remove all quarterly columns.** The table layout runs left to right as: line items | FY−2 | FY−1 | FY | YoY% (FY vs FY−1) | LTM.

9. `#pib-fin-col-1` … `#pib-fin-col-5` — period labels. Canonical order: FY−2, FY−1, FY, YoY% (FY vs FY−1), LTM (adapt labels to actual fiscal years, e.g. `2022`, `2023`, `2024`, `YoY%`, `LTM`). Do **not** populate `#pib-fin-col-6`, `#pib-fin-col-7`, or `#pib-fin-col-8` — leave them empty.
10. `#pib-fin-r{1..19}-c{1..5}` — per-cell numeric values in millions for columns 1–5. The YoY% column (c4) is computed as `(FY value − FY−1 value) / |FY−1 value| × 100`, formatted as e.g. `+4.2%` or `−3.1%`. Write `"--"` when the value is zero or unavailable. Never touch the row-label `<td>` cells. Leave `c6`, `c7`, and `c8` cells empty.

    The financial table **must** include the following line items in this exact order (map to row IDs r1–r14; leave r15–r19 empty if not applicable):
    r1 = Revenue, r2 = Gross Profit, r3 = Operating Profit (EBIT), r4 = Interest Expense,
    r5 = Net Income, r6 = Cash & Cash Equivalents, r7 = Total Assets, r8 = Total Liabilities,
    r9 = Total Equity, r10 = Cash Flow from Operations, r11 = Capital Expenditures,
    r12 = Depreciation & Amortization, r13 = Net Cash from Investing, r14 = Net Cash from Financing.
    Leave rows r15–r19 (including the EPS row at r19) empty — do **not** populate them.
11. `#pib-fin-summary` — one dense 6–8 sentence paragraph in `<p>…</p>` integrating revenue,
    EBITDA margin, leverage, cash flow, and key operational metrics.
12. `#pib-fin-highlights` — `<ul><li>…</li></ul>` bullet points covering headline results vs
    guidance, performance drivers, updated guidance, and strategic commentary.
13. `#pib-fin-analysis` — HTML with subsection headers and dense analytical bullets organised by
    Revenue & End-Market Performance, Profitability & Margins, Leverage & Liquidity. Use
    `<strong class="subsection-title">…</strong>` for each sub-heading, followed by
    `<ul><li>…</li></ul>`.

### Section 4 — Company Metrics

> **Note:** This section was formerly "Share Price Performance and Valuation." The Monthly Share
> Price chart and its analysis, the Peer Share Price chart and its analysis, and the first
> valuation table (Market & Price Data) and its analysis have been **removed**. Do not emit
> `#pib-shareprice-monthly-chart`, `#pib-shareprice-monthly-analysis`, `#pib-shareprice-peer-chart`,
> `#pib-shareprice-peer-analysis`, or `#pib-val-1-*` elements. Leave those IDs empty.

14. `#pib-val-col-1` … `#pib-val-col-4` — shared company headers starting from valuation
    table 2 (the first remaining table). Target company in column 1. Leave unused columns empty
    if fewer than 3 peers.
19. `#pib-val-2-col-*`, `#pib-val-3-col-*`, `#pib-val-4-col-*`, `#pib-val-5-col-*` — repeat the
    same company names across all five valuation tables.
20. `#pib-val-{1..5}-r{i}-c{1..4}` — per-cell values for the five valuation tables (row labels
    are pre-filled). Source valuation data from `getEntityFinancials_v2` for both the target company
    and peer companies to ensure data availability. Use `"--"` for missing values.
21. `#pib-val-{1..5}-analysis` — one paragraph each in `<p>…</p>` comparing target vs peers for
    that table. No citation numbers inside the table cells.

### Section 5 — Peer Comparison and Competitive Landscape

22. `#pib-peers-intro` — one short intro paragraph in `<p>…</p>`.
23. `#pib-peers-table` — one `<tr>` per company (target first):
    `<tr><td>Target Co</td><td>Description from Credit Opinion Profile…</td></tr>`.
24. `#pib-peers-rating` — one `<tr>` per company:
    `<tr><td>Target Co</td><td>Aaa</td><td><span class="outlook-badge stable">Stable</span></td></tr>`.
25. `#pib-ki-col-1` … `#pib-ki-col-4` — reuse the valuation-table company labels.
26. `#pib-ki-r{1..8}-c{1..4}` — per-cell values (8 metrics × up to 4 companies).
    Row labels pre-filled.
27. `#pib-peers-conclusion` — **1–2 paragraphs** in `<p>…</p>` summarising the target company's quantitative and business-risk differentiation relative to peers and its relative competitive positioning.

### Section 6 — Industry Overview and Trends

28. `#pib-industry` — **exactly 3 paragraphs** in `<p>…</p>`, one per subsection, with the subsection title rendered as `<strong class="subsection-title">…</strong>` before the paragraph text. Cover only these three subsections in order:
    (1) **Macroeconomic Context** — macro conditions affecting the sector;
    (2) **Industry Size and Growth** — market size, growth rates, and key demand drivers;
    (3) **Industry Outlook and Trends** — forward-looking view, emerging trends, and regulatory considerations.
    Do **not** include Sub-Sector and Regional Performance or a standalone Competitive Landscape prose subsection; those are replaced by the Porter's diagram below.

29. `#pib-industry-porters` — **Porter's Five Forces diagram** rendered as an inline SVG. Layout: hub-and-spoke with a central box connected by horizontal/vertical lines to four surrounding boxes. Positions:
    - Centre: `cx=370, cy=200` — **Competitive Rivalry** (assessed intensity)
    - Top: `cx=370, cy=40` — **New Entrants**
    - Bottom: `cx=370, cy=360` — **Substitutes**
    - Left: `cx=100, cy=200` — **Supplier Power**
    - Right: `cx=640, cy=200` — **Buyer Power**

    Each box is `w=180, h=60`, centred on its `cx/cy`. Draw connector lines from the edge of the centre box to the nearest edge of each surrounding box (straight horizontal or vertical lines, stroke=`#9aa0ab`, stroke-width=1.5).

    Colour-code each box by assessed intensity based on gathered data:
    - **High** → fill=`#ffe4e6`, stroke=`#e74c3c`, title-color=`#b91c1c`
    - **Medium** → fill=`#fef9c3`, stroke=`#f39c12`, title-color=`#92400e`
    - **Low** → fill=`#dcfce7`, stroke=`#27ae60`, title-color=`#166534`

    Each box contains two `<text>` lines: (1) force name, font-size=11, font-weight=700, fill=title-color; (2) intensity label (e.g. "High", "Medium", "Low"), font-size=10, fill=`#444c58`.

    SVG constants: `W=740`, `H=420`. Title: `<text x="370" y="410" text-anchor="middle" font-size="11" fill="#00205b" font-weight="700">Porter's Five Forces</text>`.
    Render inside `<div class="chart-container">`.

### Section 7 — Strategic Developments

28b. `#pib-strategy-timeline` — **horizontal timeline SVG** rendered inline, listing all strategic events from the past 12 months in chronological order (oldest left → most recent right). Constants: `W=740`, `H=120`. Draw a horizontal baseline at `y=60` from `x=40` to `x=700` (stroke=`#9aa0ab`, stroke-width=1.5). For each event place a filled circle (`r=5`, fill=`#0066cc`) on the baseline at its proportional date position; a short vertical stem (`stroke=#0066cc`, stroke-width=1) rising to `y=36`; and a `<text>` label above the stem (`text-anchor="middle"`, font-size=9, fill=`#00205b`, font-weight=600) showing a 2–3 word title on one line and the date (`YYYY-MM-DD`) on the next line (dy=+11). Below the baseline add a `<text>` at `y=80` per event showing the year tick mark if space permits. Title: `<text x="370" y="14" text-anchor="middle" font-size="11" fill="#00205b" font-weight="700">Strategic Developments Timeline</text>`. Render inside `<div class="chart-container">`.

29. `#pib-strategy-list` — one `<li>` per development from the past 12 months (same events as the timeline):
    `<li><strong>Title</strong>: 2026-01-15 — description with citation <a href="…" target="_blank" class="cite-ref">[3]</a>.</li>`.
    Cover M&A, partnerships, strategic shifts, capital allocation.

### Section 8 — Management and Governance

30. `#pib-mgmt-cards` — a row of name cards rendered as an inline SVG showing key executives and directors from `getEntityManagersDirectors`. Each card is `w=160, h=70`, spaced 12px apart, with fill=`#f4f6f9`, stroke=`#d1d5db`, rx=4. Each card shows: (1) person's name (font-size=11, font-weight=700, fill=`#00205b`); (2) their position/title (font-size=9, fill=`#6b7280`). Lay out cards in rows of up to 4; compute SVG height dynamically (`rows × 82 + 20`). SVG width=`700`. Render inside `<div class="chart-container">`.

31. `#pib-mgmt` — **1–2 paragraphs** in `<p>…</p>` summarising the leadership team's experience and strategic focus, board governance structure, and any notable recent governance changes or leadership transitions. Normal text only; no subsection headers.

### Section 9 — Credit Profile

32. `#pib-credit-analysis` — **1–2 paragraphs** in `<p>…</p>` covering the key aspects of the debt profile, leverage trends, maturity schedule, liquidity position, and credit ratings.
33. `#pib-credit-chart` — one inline `<svg>` (see **Debt Maturity** template). Data for this
    chart **must** come from `searchCompanyFilings`; use the actual future calendar-year debt
    obligation periods as reported in the filing's maturity schedule.
34. `#pib-rating-table` — one `<tr>` per rating class:
    `<tr><td>Senior Unsecured - Fgn Curr</td><td>Aaa</td><td><span class="outlook-badge stable">Stable</span></td><td>2024-11-20</td></tr>`.

### Section 10 — Risks and Challenges

35. `#pib-risks-narrative` — **1–2 paragraphs** in `<p>…</p>` summarising the current key risks and challenges facing the company, spanning market/competitive, operational, regulatory, and technology dimensions.
36. `#pib-risk-table` — 5–7 `<tr>`s:
    `<tr><td>Market &amp; Competitive</td><td>Description…</td><td>Impact…</td><td>Mitigation…</td></tr>`.
    No citation numbers inside cells.

### Section 11 — ESG Profile

37. `#pib-esg-kpi` — a row of exactly **4 metric cards** rendered as an **inline SVG** (`width="780" height="90"`). The four cards are: (1) **Overall CIS Score**, (2) **Environmental (E) Score**, (3) **Social (S) Score**, (4) **Governance (G) Score**. Source all four scores from `getCreditOpinion` (`ESGConsiderations` section). Use the same card layout as the KPI scorecard strip in Section 1 (same SVG layout constants: `cardW=170`, `gap=16`, `ox=26`; `#f4f6f9` fill, `#0066cc` left-border accent). Render inside `<div class="chart-container">`.

38. `#pib-esg-narrative` — **three short paragraphs** in `<p>…</p>`, one per ESG dimension:
    (1) **Environmental** — key environmental initiatives, risks, and performance;
    (2) **Social** — social policies, workforce practices, and community impact;
    (3) **Governance** — governance structure, board practices, and oversight quality.
    Use `<strong class="subsection-title">…</strong>` before each paragraph.

39. `#pib-esg-r{1..3}-focus` / `#pib-esg-r{1..3}-score` — category-row cells (Environmental,
    Social, Governance rows are pre-labelled). Focus is a short text; score is the Moody's
    ESG score (e.g. `E-3`). No citations inside cells.

### Citations

38. `#pib-sources` — end-of-document Citations rows. One `<div class="source-item">` per
    source, in `[1], [2], …` order. Use the canonical row markup defined in
    [references/shared-citations.md](references/shared-citations.md). Numbering must match
    inline `[n]` references.

---

---

## Streaming protocol (element → content)

| Element ID | Content type |
|---|---|
| `#pib-cover-company`, `#pib-company`, `#pib-date`, `#pib-footer-date` | Plain text |
| `#pib-overview-kpi` | One inline `<svg>` — KPI scorecard strip (4 metric cards) |
| `#pib-overview-rating-timeline` | One inline `<svg>` — Moody's rating history step-line |
| `#pib-overview`, `#pib-mgmt` | `<p>…</p>` paragraphs (with subsection titles where noted) |
| `#pib-segments-intro`, `#pib-segments-outro`, `#pib-peers-intro`, `#pib-peers-conclusion`, `#pib-fin-summary`, `#pib-fin-analysis`, `#pib-val-{2..5}-analysis`, `#pib-credit-analysis`, `#pib-risks-narrative`, `#pib-esg-narrative`, `#pib-industry` | `<p>…</p>` paragraphs |
| `#pib-fin-highlights` | `<ul><li>…</li></ul>` |
| `#pib-segments-list` | One `<li>` per segment (with `<strong>` header + prose paragraph) |
| `#pib-strategy-list` | One `<li>` per development |
| `#pib-strategy-timeline` | One inline `<svg>` — horizontal event timeline |
| `#pib-mgmt-cards` | One inline `<svg>` — name cards grid |
| `#pib-esg-kpi` | One inline `<svg>` — 4 ESG metric cards |
| `#pib-industry-porters` | One inline `<svg>` — Porter's Five Forces hub-and-spoke diagram |
| `#pib-fin-col-{1..5}` | Plain text period label (FY−2, FY−1, FY, YoY%, LTM) |
| `#pib-fin-r{1..19}-c{1..5}` | Plain text number (millions) or YoY% (c4 only) or `"--"` |
| `#pib-val-col-{1..4}`, `#pib-val-{2..5}-col-{1..4}`, `#pib-ki-col-{1..4}` | Plain text company label |
| `#pib-val-{2..5}-r{i}-c{1..4}`, `#pib-ki-r{1..8}-c{1..4}` | Plain text number / ratio / `"--"` |
| `#pib-peers-table`, `#pib-peers-rating`, `#pib-rating-table`, `#pib-risk-table` | One `<tr>…</tr>` per row |
| `#pib-esg-r{1..3}-focus`, `#pib-esg-r{1..3}-score` | Plain text |
| `#pib-segments-pie`, `#pib-credit-chart` | One inline `<svg>` (see templates below) |
| `#pib-cite-{a..k}` | Optional per-section recap as one `<div class="section-citations">…</div>` (markup defined in [references/shared-citations.md](references/shared-citations.md)). Empty when the corresponding section carries no inline `[n]` references. |
| `#pib-sources` | One `<div class="source-item">…</div>` per source |

**Fixed 4-company layout**: valuation tables and the key-indicators table assume target + up to
3 peers (4 columns). If fewer than 3 peers are available, leave unused column header / cell IDs
empty — do not collapse or restructure the tables.

## Reference markup snippets

Pre-filled `row-label` cells are never changed from the template. Only the empty data cells are
populated:

```html
<!-- Already in the template (do not touch) -->
<tr><td class="row-label">Total debt</td><td id="pib-fin-r14-c1"></td>…</tr>

<!-- Peers table row (into #pib-peers-table) -->
<tr><td>Target Co</td><td>Description from Credit Opinion Profile…</td></tr>

<!-- Peers rating row (into #pib-peers-rating) -->
<tr><td>Target Co</td><td>Aaa</td><td><span class="outlook-badge stable">Stable</span></td></tr>

<!-- Rating table row (into #pib-rating-table) -->
<tr><td>Senior Unsecured - Fgn Curr</td><td>Aaa</td><td><span class="outlook-badge stable">Stable</span></td><td>2024-11-20</td></tr>

<!-- Risk table row (into #pib-risk-table) -->
<tr><td>Market &amp; Competitive</td><td>Description…</td><td>Impact…</td><td>Mitigation…</td></tr>

<!-- Segment bullet (into #pib-segments-list) -->
<li><strong>iPhone</strong><p>The iPhone segment encompasses Apple's line of smartphones running iOS. It is the company's largest revenue contributor, generating $209,586.0m (50.4% of total revenue) in FY2024 as reported in the annual filing. The segment benefits from strong brand loyalty, a growing services attach rate, and continued premium pricing power across global markets.</p></li>

<!-- Strategy bullet (into #pib-strategy-list) -->
<li><strong>Title</strong>: 2026-01-15 — description of the development with citation <a href="https://www.moodys.com/research/doc--PBC_…" target="_blank" class="cite-ref">[3]</a>.</li>
```

For `#pib-sources` source-item rows, use the canonical row markup defined in
[references/shared-citations.md](references/shared-citations.md).

## SVG chart templates

Palette (indexed, target = first): `#0066cc, #e74c3c, #27ae60, #f39c12, #8e44ad, #16a085`.

Every chart is wrapped in `<div class="chart-container">…</div>` so the existing CSS applies.

### KPI Scorecard Strip (`#pib-overview-kpi`)

See layout constants defined in Section 1, item 5 above. Four metric cards rendered inline.

### Rating History Step-line (`#pib-overview-rating-timeline`)

See layout constants defined in Section 1, item 6 above. Horizontal step-line chart sourced
from `getEntityRatings`.

### Revenue by Segment Bar Chart (`#pib-segments-pie`)

See layout constants defined in Section 2, item 9 above. Data sourced exclusively from
`searchCompanyFilings`.

### Debt Maturity (`#pib-credit-chart`)

> **⚠️ MANDATORY DATA REQUIREMENT — NO ESTIMATION PERMITTED**
>
> `searchCompanyFilings` **MUST** be called with a query targeting the debt maturity schedule
> (e.g. `"long-term debt maturities schedule obligations"`) before this chart can be emitted.
> This is a required tool call — it cannot be skipped, inferred from total debt figures, or
> substituted with data from any other source.
>
> - **NEVER** estimate, split, distribute, or approximate maturity amounts from aggregate debt.
> - **NEVER** construct buckets from total debt divided by assumed years.
> - If `searchCompanyFilings` does not return an explicit per-year maturity schedule, leave
>   `#pib-credit-chart` **empty** and omit the chart entirely. Do not render a chart with
>   fabricated values.

**Source data exclusively from `searchCompanyFilings`** (annual reports, 10-K, or debt/liquidity
footnotes) — do **not** use Moody's estimates or earnings call figures for maturity amounts.
Build the chart using **future debt obligation periods** as reported in the filing's debt
maturity schedule. Use the actual future years (e.g. 2025, 2026, 2027, 2028, 2029, Thereafter)
rather than generic buckets; drop any year with zero obligations before computing layout.

Bar chart. Constants:

- `W=700`, `H=250`; padding `{top:20, right:20, bottom:60, left:70}`; plot area `cW=610`, `cH=170`.
- Buckets: use the actual future calendar years from the filing's debt maturity schedule (e.g.
  `2025, 2026, 2027, 2028, 2029, Thereafter`). **Drop any year whose value is 0** before
  computing layout. Let `N` = remaining bucket count.
- `bw = min(cW / N × 0.6, 50)`; `gap = (cW − bw × N) / (N + 1)`.
- `mx = max(values)`; `yPos(v) = 20 + 170 − (v / mx) × 170`.
- Bar `x` for bucket `i` = `70 + gap × (i + 1) + bw × i`.
- Fill bars with `#0066cc`. Emit the value above each bar as `{v}B` (right-aligned to the bar
  centre) and the label below rotated `-25°`.
- Title `<text x="350" y="14" text-anchor="middle" font-size="12" fill="#00205b" font-weight="700">Debt Maturity Profile (USD-Billion)</text>`.

```html
<div class="chart-container">
  <svg width="700" height="250" viewBox="0 0 700 250" xmlns="http://www.w3.org/2000/svg">
    <text x="350" y="14" text-anchor="middle" font-size="12" fill="#00205b" font-weight="700">Debt Maturity Profile (USD-Billion)</text>
    <!-- baseline -->
    <line x1="70" y1="190" x2="680" y2="190" stroke="#9aa0ab"/>
    <!-- per bucket: <rect> + value label + rotated x-label -->
    <rect x="{bx}" y="{yPos(v)}" width="{bw}" height="{190 − yPos(v)}" fill="#0066cc"/>
    <text x="{bx + bw/2}" y="{yPos(v) − 4}" text-anchor="middle" font-size="10" fill="#444c58">{v}B</text>
    <text x="{bx + bw/2}" y="210" text-anchor="middle" font-size="10" fill="#444c58" transform="rotate(-25 {bx + bw/2} 210)">{label}</text>
  </svg>
</div>
```

## Class-selection rules

- `outlook-badge` variants: `stable` / `positive` / `negative` / `review` / `na` (canonical
  pastel set defined by the shared template skill). Map by outlook text:
  `Stable → stable`, `Positive → positive`, `Negative → negative`,
  `Review for Upgrade` / `Review for Downgrade` / `RUR` → `review`. If the outlook is missing
  or unknown, use `na` (renders as muted gray) — do not default to `stable`.
- `subsection-title` on a `<strong>` is the canonical way to render a sub-heading inside a
  `section-content` block.

---

## Per-section citation recap mapping (`#pib-cite-a` … `#pib-cite-k`)

Per-section recap blocks live in `#pib-cite-a` … `#pib-cite-k`, mapped one-to-one to the
eleven report sections in document order:

| Letter | Section                                          |
|--------|--------------------------------------------------|
| `a`    | 1. Company Overview                              |
| `b`    | 2. Business Segments and Operations              |
| `c`    | 3. Historical Financials                         |
| `d`    | 4. Company Metrics                               |
| `e`    | 5. Peer Comparison and Competitive Landscape     |
| `f`    | 6. Industry Overview and Trends                  |
| `g`    | 7. Strategic Developments                        |
| `h`    | 8. Management and Governance                     |
| `i`    | 9. Credit Profile                                |
| `j`    | 10. Risks and Challenges                         |
| `k`    | 11. ESG Profile                                  |

Each `#pib-cite-{x}` should be filled with a single `<div class="section-citations">…</div>`
recap as defined in the shared skill (`.cite-label` "Citations" pill plus one `.cite-item` per
source referenced in that section). The recap re-uses the same global `[n]` numbering as the
inline references and `#pib-sources` — it never starts a new sequence. If a section has no
inline citations, leave the corresponding `#pib-cite-{x}` empty.
