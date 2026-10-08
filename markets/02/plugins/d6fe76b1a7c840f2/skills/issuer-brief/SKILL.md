---
name: issuer-brief
description: >
  Produce a comprehensive Issuer Brief HTML report for a company using Moody's
  GenAI MCP tools. Use this skill whenever the user asks to create an Issuer Brief,
  company profile report, credit memo, investment book, or comprehensive company analysis. Also
  trigger when they ask for a report combining company overview, financials, peer comparison,
  industry overview, strategic developments, management, credit profile, risks, and ESG into a
  single document. Trigger even if they just name a company and say "Issuer Brief", "info book", "company
  book", "credit book", or "full company report".
---

# Issuer Brief Skill

Generates a professional HTML report (styled like a Moody's Issuer Brief) for a
target company. The report consolidates data from multiple Moody's MCP tools, annual/quarterly
reports, earnings calls, and news into 11 structured sections plus a pre-rendered table of
contents. Section 4 is titled "Company Metrics" (formerly "Share Price Performance and Valuation").

The workflow is **single-artifact delivery**: gather all data, then write the entire filled
HTML document to a single `.html` file in `/mnt/user-data/outputs/` and actively render it to
the user with **both** `present_files` and `visualize:show_widget`. The rendered HTML artifact
is the deliverable — writing the file without rendering it is a failed run.

> ## ⚠️ CRITICAL — NON-NEGOTIABLE OUTPUT CONTRACT
>
> **The LLM MUST deliver the final report as a single standalone HTML artifact file that it
> then actively renders on screen.** Creating the file is only half the job — a file that is
> written but never surfaced is a failed run, and is the single most common failure mode for
> this skill. Specifically:
>
> - The LLM **MUST** write the **complete, standalone HTML document** (`<!doctype html>` →
>   `</html>`), with every section from the streaming protocol populated inline, to a single
>   `.html` file in `/mnt/user-data/outputs/` using the `create_file` tool.
> - The LLM **MUST** then render that file with **both** display tools — `present_files`
>   **and** `visualize:show_widget` — before ending its turn. Firing both renderers is what
>   guarantees the report always appears even if one tool is unavailable.
> - The LLM **MUST NOT** end its turn after `create_file` without having called the display tools.
> - The LLM **MUST NOT** emit the report inline as a fenced ` ```html ` code block, as prose,
>   Markdown, JSON, attachments, or links. The rendered HTML artifact itself is the answer.
> - The LLM **MUST NOT** split the report across multiple files, multiple messages, partial
>   snippets, or summaries.
> - If data gathering fails partially, still produce the single HTML artifact file with the
>   best-available content and `"--"` placeholders for missing cells — never skip the artifact
>   or the render step.
>
> Treat any other output shape as a hard failure of the skill.

> ## ⚠️ CRITICAL — NO ESTIMATED OR APPROXIMATED NUMBERS ALLOWED
>
> **Every numeric value in the report — in tables, charts, KPI cards, prose, and SVGs — MUST
> come directly from a Moody's MCP tool response or a company filing retrieved via
> `searchCompanyFilings`.** Estimation, approximation, interpolation, and inference from
> indirect sources are strictly forbidden. Specifically:
>
> - **NEVER** write `~`, `approx.`, `estimated`, or any similar qualifier next to a number.
>   If the exact figure is unavailable from the data gathered, use `"--"` instead.
> - **NEVER** derive a number by splitting, distributing, or back-calculating from an aggregate
>   (e.g. do not allocate total debt across maturity buckets by assumption).
> - **NEVER** invent segment revenue, EPS, FCF, ROE, debt maturity amounts, or any other
>   metric that was not explicitly returned by a tool call.
> - **Charts are not exempt**: every bar height, data point, and label in every SVG chart
>   (KPI scorecard, rating timeline, segment revenue bar, debt maturity bar) must map 1-to-1
>   to a value returned by a tool. If tool data is insufficient to build a chart accurately,
>   omit the chart and leave the container empty rather than render fabricated values.
> - **Peer data is not exempt**: only populate peer columns with values explicitly returned
>   by `getCreditOpinion`, `getEntityFinancials_v2`, or `getEntityRatings` for that peer.
>
> Treat any estimated or approximated number in the emitted report as a hard failure of the skill.

## Required MCP server

`Moodys MCP server` — tools used: `findEntity`, `getEntityPeers`, `getEntityRatings`,
`getCreditOpinion`, `getEntitySectorOutlook`, `searchAllDocuments`,
`searchEntityEarningsCall`, `searchNews`, `getEntityFinancials_v2`, `getEntityManagersDirectors`,
`searchCompanyFilings`.

If any of the tools required for a section do not exist, inform the user: One or more tools required for this section are not available under your current subscription. Unlock more of the expert insights, data, and analytics you trust. Get Link:https://www.moodys.com/web/en/us/capabilities/gen-ai/ai-ready-data.html with us to learn more. 

> ESG data (CIS, E, S, G) comes from `getCreditOpinion` via the `ESGConsiderations` section.

## Bundled files

- `assets/template.html` — self-contained static report shell: CSS, layout, a hardcoded 11-entry
  table of contents, pre-shaped tables (financial / 5 valuation / key-indicators / ESG-score)
  with cell-level IDs, and empty targets (containers, `<tbody>`, `<ul>`, `<div>`) for variable
  content. Treat this file as the **read-only structural reference**: read it, fill it in
  mentally, and emit the complete filled document in the final response.

## Shared chrome & citations

Before emitting, read [`references/shared-template.md`](references/shared-template.md) (page
chrome: cover, TOC, section block, sources-section wrapper, footer, outlook-badge, design
tokens) and [`references/shared-citations.md`](references/shared-citations.md) (citation
numbering, hyperlinking, source data shape, markup snippets). Both are **authoritative** — do
not invent, duplicate, or restyle anything they already define. The canonical CSS is already
inlined in `assets/template.html` between the `/* BEGIN/END shared-template-css */` and
`/* BEGIN/END shared-citations-css */` markers; never re-copy it at emit time.

The rest of this section is the skill-specific binding.

This skill uses the **`cover-simple`** variant. Skill-specific overrides retained above the
marker region: `**body { font-size: 12.5px }**` (PIB renders denser financial tables than the
13px canonical default) and `**.page { max-width: 920px }**` (slightly wider than the 900px
canonical default). Skill-specific CSS that stays local: `table.data-table`, `table.fin-table`,
and the PIB chart helper (`.chart-container` PIB variant — centered, no background).

**Chart spacing rule:** Every `.chart-container` must have `margin-top: 28px` (increased from the
template default of 16px) so that visualization titles do not visually merge with the preceding
section or subsection headings. When emitting the final HTML, ensure the `.chart-container` CSS
rule reads `.chart-container { margin: 28px 0 20px; text-align: center; }` — update the value
in the `<style>` block if it differs from the template default.

**Outlook-badge migration.** PIB previously shipped a solid-fill `.outlook-badge` styling
(white text on solid `--green` / `--red` / `--amber` / `--accent` backgrounds) inside its own
template. That carve-out has been **removed**. PIB now inherits the canonical pastel variant
from the shared skill — pastel background + colored text, with the same five class variants
(`stable` / `positive` / `negative` / `review` / `na`) used everywhere else. Do not re-define
`.outlook-badge` rules locally and do not emit inline `style="..."` overrides on outlook
badges. The `--green`, `--red`, `--amber` custom properties are no longer present and must not
be referenced anywhere in the emitted HTML.

Skill-specific carve-out: **never put citation markup inside data cells** (financial,
valuation, key-indicators, rating, risk, or ESG tables). The prefix used for the
end-of-document container in this skill is `pib`, so the container id is `#pib-sources`.
Per-section recap blocks live in `#pib-cite-a` … `#pib-cite-k`, mapped one-to-one to the
eleven report sections in document order; the full letter→section mapping and recap rules
are in [`references/report-spec.md`](references/report-spec.md). Each recap reuses the global
`[n]` numbering and is left empty when its section carries no inline citations.

## Parameters

The user should provide:
- **Company Name** (required)
- **Currency** (optional, defaults to USD)

---

## Step 1 — Resolve the target company and peers

Call `findEntity` with the company name. Store the canonical entity name and ID.
Then call `getEntityPeers` for the target to get up to 3 peers. Call `findEntity`
for each peer to resolve their entity IDs.

---

## Step 2 — Read the template

Read `assets/template.html` (relative to this skill directory) once. Keep its exact structure —
CSS, `<head>`, hardcoded TOC, section order, table skeletons, row labels, and element IDs — as
the scaffold for the final artifact. Do **not** copy it to the workspace and do **not** open it.

---

## Step 3 — Gather all data in parallel

Fire ALL of the following in a **single parallel batch**. This is the heaviest step — launch
everything at once.

### For the target company

| Tool Call | Purpose |
|-----------|---------|
| `getCreditOpinion` (sections: Profile, Summary, CreditStrengths, CreditChallenges, FactorsLeadingToUpgrade, FactorsLeadingToDowngrade, KeyIndicatorsTable, ScorecardTable, ESGConsiderations) | Credit profile, strengths/challenges, financials, ESG |
| `getEntityFinancials_v2` | Primary source for historical financials (3 full fiscal years + LTM) and valuation table data |
| `getEntityRatings` | Current rating, outlook, historical ratings |
| `getEntitySectorOutlook` | Sector outlook |
| `searchAllDocuments` with "Credit Opinion" | Credit opinion documents |
| `searchAllDocuments` with "Business units, Segment Revenue, Profile, Segments, Revenue Drivers" | Business segment data |
| `searchCompanyFilings` with "segment revenue, business segments, revenue by segment" | Per-segment revenue from annual/quarterly filings to populate Business Segments and Operations section |
| `searchAllDocuments` with "Risk factors, competitive pressures, market volatility, regulatory compliance, litigation" | Risk analysis |
| `searchAllDocuments` with "Leverage, Debt, Liquidity, Credit Facilities, Coverage, Ratings, Outlook" | Credit profile data |
| `searchEntityEarningsCall` with "Target Market, Services, Products, Mission, Vision, Markets, Geographies, Revenue" | Company overview from earnings call |
| `searchEntityEarningsCall` with "Business units, Segment Revenue, Drivers, Revenue Drivers, Earnings" | Business segments from earnings call |
| `searchEntityEarningsCall` with "Market Size, Growth Rate, Demand, Competition, Market Share, Regulation, Trends" | Industry analysis |
| `searchEntityEarningsCall` with "Share, Stock, Price, Market capitalization, Earnings per share, Dividend, Valuation" | Share price data |
| `searchEntityEarningsCall` with "Risk factors, competitive pressures, market volatility, economic uncertainty" | Risks from earnings call |
| `searchEntityEarningsCall` with "merger, acquisitions, strategic developments, alliances, partnerships" | Strategic developments |
| `searchNews` with "{Company} Market, Industry Overview and Trends" | Industry news |
| `searchNews` with "{Company} merger, acquisitions, strategic developments" | M&A news |
| `searchNews` with "{Company} Share, Stock, Price, Valuation" | Share price news |
| `searchNews` with "{Company} Management, governance, leadership" | Management news |
| `getEntityManagersDirectors` | Names and roles of current managers and directors for Management & Governance section |

### For each peer (up to 3 peers)

| Tool Call | Purpose |
|-----------|---------|
| `getCreditOpinion` (Profile, KeyIndicatorsTable, CreditStrengths, CreditChallenges, FactorsLeadingToUpgrade, FactorsLeadingToDowngrade, ScorecardTable, ESGConsiderations) | Peer comparison data + ESG |
| `getEntityFinancials_v2` | Peer valuation and financial data for Share Price Performance and Valuation section |
| `getEntityRatings` | Peer ratings |

---

## Step 4 — Synthesize + emit the complete artifact

Use Moody's internal research as the **primary foundation**. Earnings call data and news
supplement. Write in professional credit-research language with numbered citation references
inline in narrative text. The exact inline markup, the URL-less fallback, and the rule that
`n` matches the row position of the source inside `#pib-sources` are defined in
[references/shared-citations.md](references/shared-citations.md) — read it before authoring
any `[n]` reference.

After data is gathered, write the **entire filled `template.html` document** — with every
element from the streaming protocol populated in place — to a single `.html` file in
`/mnt/user-data/outputs/`, then render it. The full required delivery sequence (`create_file`
→ `present_files` → `visualize:show_widget` → one short sentence) is specified in the
**Step 5 — Output and presentation** section below; follow it exactly.

The HTML file **must**:

- Be written in a single `create_file` call (no progressive `StrReplace` edits, no multi-file
  split).
- Contain a complete, standalone HTML document (doctype → `</html>`) that renders without
  external dependencies.
- Preserve the template's `<head>` (CSS, fonts), hardcoded TOC, section order, table
  skeletons, row labels, and element IDs exactly. Only the empty targets defined below are
  populated.

Render order of content inside the file follows the page top-to-bottom so the artifact is
human-readable as well as browser-renderable.

### Cover + footer

1. `#pib-cover-company` — plain text, canonical target name.
2. `#pib-company` — plain text target name.
3. `#pib-date` — report date, e.g. `April 15, 2026`.
4. `#pib-footer-date` — same date string.

### Section-by-section authoring (Sections 1–11)

Before emitting, read [`references/report-spec.md`](references/report-spec.md) for the full
per-section element specs — every `#pib-*` target for Sections 1 through 11 (Company
Overview, Business Segments and Operations, Historical Financials, Company Metrics, Peer
Comparison and Competitive Landscape, Industry Overview and Trends, Strategic Developments,
Management and Governance, Credit Profile, Risks and Challenges, ESG Profile), the exact SVG
layout constants for each chart, the financial-table row/column mapping, and the
`#pib-sources` Citations rows. Populate every target exactly as specified there, honoring the
no-estimation contract above.

---

## Step 5 — Output and presentation (required final steps)

> ## ⚠️ CRITICAL — THE SKILL IS NOT COMPLETE UNTIL THE REPORT IS VISIBLY RENDERED
>
> Writing the file is **not** delivery. After you write the HTML you **must** actively render
> it with every display tool available, in order, before you say anything else. Do not end
> your turn until the rendered report is on screen.

Follow this exact sequence. Do not skip a step, reorder, or substitute alternatives:

1. **Write the HTML file in a single call.** Call `create_file` to write the entire standalone
   HTML document (`<!doctype html>` → `</html>`) to
   `/mnt/user-data/outputs/{company_slug}_issuer_brief.html` in **one** call. No progressive
   edits, no multi-file split.
2. **Present the file.** Immediately call `present_files` on that exact path to surface the
   artifact to the user.
3. **Show the widget.** Immediately call `visualize:show_widget` on the same file to render the
   report visually. Call this even if `present_files` already succeeded — firing both renderers
   is what guarantees the report always appears.
4. **Confirm in one short sentence.** Only after the renderers return, add a single brief
   sentence in chat (e.g. `Issuer Brief for {Target Company} — the report is available above as
   a self-contained HTML artifact.`). Nothing more.

If a display tool call fails or is unavailable, immediately try the other one rather than
stopping. Never end your turn at step 1, and never paste the HTML into chat or suggest shell
commands.

---

## Streaming protocol, markup snippets & chart templates

The element → content mapping table, the reference markup snippets (financial row, peers
table / rating rows, rating-table row, risk-table row, segment bullet, strategy bullet), the
SVG chart templates (KPI scorecard, rating step-line, segment revenue bar, debt-maturity bar,
Porter's Five Forces diagram, management cards) with their layout constants and palette, and
the class-selection rules all live in
[`references/report-spec.md`](references/report-spec.md). Read it before emitting any `#pib-*`
content or chart. The debt-maturity and segment charts require `searchCompanyFilings` data —
leave the container empty rather than fabricate values.

## Tips

- Run ALL research searches in a single parallel batch to minimize latency.
- **No estimated or approximated numbers anywhere in the report.** Every figure in tables,
  charts, KPI cards, and prose must come directly from a tool response; use `"--"` when a
  value is unavailable. See the CRITICAL no-estimation block above.
- **`searchCompanyFilings` is a required call** for the debt-maturity and segment-revenue
  charts. If it does not return the per-year schedule or segment breakdown, leave the chart
  container empty rather than fabricate values.
- Target company appears first in every table and comparison; reuse the same column labels
  across the valuation / key-indicators tables. Financial values are in millions; never hide
  a row. If fewer than 3 peers are returned, leave unused columns/cells blank — do not
  collapse the tables.
- Emit each chart SVG directly into its container — the template does not render charts at
  load time. Exact placement, layout constants, and the Section 4 / `#pib-val-1-*` omissions
  are in [`references/report-spec.md`](references/report-spec.md).
- Citation references `[n]` go inline in narrative text per
  [references/shared-citations.md](references/shared-citations.md); never inside table cells.
  Each section's optional `#pib-cite-{a..k}` recap reuses the global numbering.
- Deliver the report as **one** `.html` file in `/mnt/user-data/outputs/`, then render it with
  **both** `present_files` and `visualize:show_widget` (see Step 5). Never paste it as a fenced
  ` ```html ` code block, never split across files or messages, and never stop at file creation.
