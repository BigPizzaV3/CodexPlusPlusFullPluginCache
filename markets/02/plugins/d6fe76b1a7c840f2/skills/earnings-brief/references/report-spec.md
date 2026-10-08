# Earnings Brief — Report Authoring Spec

Detailed body-authoring rules for the Earnings Call Summary report. Read this before
emitting the HTML artifact. It is authoritative for the per-section synthesis rules
(sections **a–l**), the placement of citation recap blocks and `#ecs-sources`, the
streaming protocol (element → content mapping), the reference HTML snippets, the
class-selection rules, and the HTML conventions. Cover/header fields, allowed data
sources, and the output contract remain in `SKILL.md`.

All synthesis must derive exclusively from the earnings call transcript content gathered
in Step 3. Inline citations follow
[`references/shared-citations.md`](shared-citations.md).

---

### Section synthesis rules
 
> **Per-section omit rule (applies to every section a–l).** If a company's earnings call
> transcript exists but does not contain information relevant to a given section, **omit
> that company from that section entirely** — do not emit a row, subtitle, bullet, or any
> "Not disclosed" placeholder for it. The section may legitimately cover fewer companies
> than the full set. (Companies whose transcript could not be located at all are handled
> per rule **a** and are excluded from every section.)
 
**a. Executive Summary** → `#ecs-executive-summary`
**Exactly one combined `<p>` paragraph of 100 words or less** that summarises the entire contents of the newsletter across all covered companies. **Do NOT write one paragraph per company** and do NOT structure it as a per-company recap — it must be a single, general, combined summary of the whole report based solely on the earnings call transcript content. May carry inline `<a class="cite-ref">[n]</a>` hyperlink citations.
If the earnings call transcript for any requested company could not be located (neither via `searchEntityEarningsCall` nor a web_search result within the 100-day window), **explicitly note that fact in the Executive Summary** (e.g., "An earnings call transcript for {Company X} could not be located and it is therefore not covered in this report."). That company must then be **omitted from every other section** — no row in the YOY tables, no subtitle, no bullets, no placeholder.
 
**b. Overall Credit Consideration** → `#ecs-credit-badge` + `#ecs-overall-credit`
Answer the question: **Are conditions in the industry and macro-environment credit positive, negative, or neutral?** Determine the answer **solely from the earnings call transcript content**, by looking across all covered companies for industry-wide trends and patterns.
Write the sentiment badge into `#ecs-credit-badge` (see snippet below).
Write one intro `<p>` (≤250 chars) that gives an overview with a **clearly formed opinion** on whether industry/macro conditions are credit positive, negative, or neutral, followed by a `<ul>` of **exactly 5 `<li>` bullets** (≤150 chars each) into `#ecs-overall-credit` that **list the five considerations supporting that view**. The intro paragraph and each bullet may carry inline citations.
**The view and every supporting consideration must be derived from trends or patterns observed across the covered companies — i.e., the industry as a whole.** Do **not** extrapolate isolated events that apply to just one company into an industry-level claim. Group companies that share a dynamic into a single bullet (e.g., "Company A and Company B both cite easing input cost pressure …"). Do **not** write one bullet per company.
Draw exclusively on the earnings call transcript. Do not consult credit opinions, sector outlooks, or any other tool.
 
**c. Revenue YOY Trend** → `#ecs-tbody-revenue`
One `<tr>` per company: company-wide YOY revenue change (`+X.XX%` / `-X.XX%` / `Up` / `Down` / `Flat` / `Not specified`) and a 70–90 char commentary. Not segment-specific. The commentary cell may carry inline citations; the numeric `.yoy-change` cell stays citation-free.
 
**d. Volumes YOY Trend** → `#ecs-tbody-volumes`
Same row format as (d) but for sales volumes. The commentary cell may carry inline citations; the numeric `.yoy-change` cell stays citation-free.
 
**e. Selling Price Trend** → `#ecs-tbody-prices`
Same row format as (d) but for selling prices. The commentary cell may carry inline citations; the numeric `.yoy-change` cell stays citation-free.
 
**f. Qualitative / Broad Industry Commentary on Revenue, Volumes & Pricing** → `#ecs-qualitative`
Exactly three paragraphs in this fixed order: **a. Revenue, b. Volumes, c. Pricing**. Each paragraph **must give a general view of the industry** in which the covered companies operate — i.e., synthesise the cross-company patterns observed in the earnings call transcripts into an industry-level commentary, not a per-company recap. **Each paragraph must be between 200 and 300 characters.**
Prefix each paragraph with a `<strong class="subsection-title">Revenue</strong>` (etc.) subheader. Derive macro framing exclusively from cross-company observations in the earnings call transcripts. Each paragraph may carry inline citations.
 
**g. End Market Conditions** → `#ecs-end-markets`
Exactly four thematic commentaries describing the market conditions in which the covered companies operate. Each commentary has a `<strong class="subsection-title">…</strong>` subheader (≤70 chars summarising the bullets) + a `<ul>` with **at least 2 `<li>` bullets**. **Combined bullet length per commentary: 250–300 characters.** Derive narratives exclusively from the earnings call transcripts. Each bullet may carry inline citations.
**Provide your view on the trends or patterns observed across all covered companies** — these commentaries must reflect cross-company industry dynamics, not isolated single-company facts repackaged.
**Each bullet (and every comment) must explicitly name the company or companies it applies to** by stating the company name directly within the sentence. If two or more companies share the dynamic, name all of them in the same bullet. Do not write company-agnostic bullets.
 
**h. Supply Chain Conditions** → `#ecs-supply-chain`
**Emit exactly three important thematic commentaries**, each covering one of the following topic areas: **(1) Raw Materials / Input Costs, (2) Trade Relations / Tariffs, or (3) Impact on Business Operations**. Pick the three most relevant topics surfaced in the transcripts (the three may be the three distinct topics above, or any combination drawn from them where the same topic recurs across companies in materially different ways). Each commentary has a `<strong class="subsection-title">…</strong>` subheader (≤70 chars summarising the bullets) + a `<ul>` with **at least 2 `<li>` bullets**. **Combined bullet length per commentary: 200–250 characters.** Each bullet may carry inline citations.
**Provide your view on the trends or patterns observed across all covered companies** — these commentaries must reflect cross-company industry dynamics, not isolated single-company facts repackaged.
**Each bullet (and every comment) must explicitly name the company or companies it applies to** by stating the company name(s) directly within the sentence. **Mention the name of the specific companies that are facing the event being described in each point.** If two or more companies share the dynamic, name all of them in the same bullet — e.g., `Company A and Company B are both investing in AI and digital transformation to streamline operations and lower delivery costs.` Do not write company-agnostic bullets.
 
**i. Business Conditions by Geography** → `#ecs-geography`
Summarise the general conditions of the market by geography. Emit exactly four regional blocks, in this order: **North America**, **Latin America**, **Europe, Middle East and Africa**, **Asia Pacific**. No other regions may be added; do not split or rename these four. Each block has a `<strong class="subsection-title">…</strong>` subheader of **no more than 70 characters that summarises the bullets below** (single line, no trailing period). Then a `<ul>` with **at least 2 `<li>` bullets**, **200–250 characters combined per region**, opens directly after the `</strong>`. Each bullet may carry inline citations.
**Provide your view on the trends or patterns observed across all covered companies** — each regional block must reflect cross-company observations of conditions in that geography, not a single-company anecdote.
**Each bullet (and every comment) must explicitly name the company or companies it applies to** by stating the company name(s) directly within the sentence. **Mention the name of the specific companies that are facing the event being described in each point.** If two or more companies share the dynamic in that region, name all of them in the same bullet. Do not write company-agnostic bullets.
If none of the covered companies discussed a given region on their earnings call, **omit that region's block entirely** rather than emitting an empty subheader.
 
**j. Next Quarter & Full Year Business Outlook / Guidance** → `#ecs-outlook`
One commentary per company (≥2 bullets, 200–250 chars combined). Include next-quarter AND full-year guidance as stated on the earnings call. Include quantitative data where available in the transcript. Each bullet may carry inline citations.
The `<strong class="subsection-title">…</strong>` subtitle **must be a single line in the form `Company Name: Short General Summary`**, where the summary is a brief, general descriptor (≤80 chars, no trailing period) of what the bullets below cover. The summary lives **inside** the `<strong>` tag, joined to the company name by a colon — it is part of the subtitle itself, not a separate sentence underneath. Example: `<strong class="subsection-title">Company Name: Focused on AI-Driven Turnaround and Pipeline Conversion</strong>`. The `<ul>` of bullets opens directly after the `</strong>`.
 
**k. Earnings Revisions for Applicable Companies** → `#ecs-revisions`
One commentary per company that revised earnings (≥2 bullets, 200–250 chars combined). Each bullet may carry inline citations.
The `<strong class="subsection-title">…</strong>` subtitle **must be a single line in the form `Company Name: Short Summary`**, where the summary is a brief descriptor (≤80 chars, no trailing period) of the revisions covered in the bullets below. The summary lives **inside** the `<strong>` tag, joined to the company name by a colon — it is part of the subtitle itself, not a separate sentence underneath. Example: `<strong class="subsection-title">Company Name: Narrowed Revenue Decline, Raised Free Cash Flow Guidance</strong>`. The `<ul>` of bullets opens directly after the `</strong>`.
Whenever a bullet states that management **raised or lowered a specific financial metric** (revenue, EPS, margin, FCF, capex, etc.), it **must support the claim with the quantitative data point from the transcript when available** — include the new figure, the prior figure, and/or the magnitude of change (e.g., `raised FY revenue guidance to $12.4B from $12.1B (+2.5%)`). Only omit the figure if the transcript itself does not provide it.
If a company did not make or did not mention any revision in its earnings call transcript, **omit that company entirely from this section** — do not emit a subtitle, summary sentence, bullets, or any "No revisions disclosed" placeholder for it.
 
**l. Corporate Events** → `#ecs-events`
One commentary per company with relevant events (≥2 bullets, 300–350 chars combined).
Cover M&A, restructurings, plant closures, force majeures **as discussed on the earnings call**. Each bullet may carry inline citations.
The `<strong class="subsection-title">…</strong>` subtitle **must be a single line in the form `Company Name: Short Summary`**, where the summary is a brief descriptor (≤80 chars, no trailing period) of the events covered in the bullets below. The summary lives **inside** the `<strong>` tag, joined to the company name by a colon — it is part of the subtitle itself, not a separate sentence underneath. Example: `<strong class="subsection-title">Company Name: Closed Target Co. Acquisition and Restructured EMEA Operations</strong>`. The `<ul>` of bullets opens directly after the `</strong>`.
 
### Citations & sources (write last)
 
- `#ecs-cite-a` … `#ecs-cite-l` — optional per-section recap blocks. Use the
  `<div class="section-citations">…</div>` markup defined in
  [references/shared-citations.md](references/shared-citations.md). Omit any section's block
  if empty.
- `#ecs-sources` — end-of-document Citations rows. One `<div class="source-item">` per
  source, in `[1], [2], …` order, using the canonical row markup from the shared citations
  skill.
---
 
## Streaming protocol (element → content mapping)
 
| Element ID                       | Content type                                                       |
|----------------------------------|--------------------------------------------------------------------|
| `#ecs-report-date`               | Plain text date                                                    |
| `#ecs-footer-date`               | Plain text date (same value)                                       |
| `#ecs-company-count`             | Plain text integer                                                 |
| `#ecs-company-chips`             | Sequence of `<span class="company-chip">…</span>`                  |
| `#ecs-cover-img-right`           | `<img>` element — set `src` attribute                              |
| `#ecs-cover-img-bottom`          | `<img>` element — set `src` attribute                              |
| `#ecs-executive-summary`         | One or more `<p>`; prose may carry inline citations |
| `#ecs-credit-badge`              | Single `<div class="credit-badge …">` element                      |
| `#ecs-overall-credit`            | `<p>` intro + `<ul><li>` bullets; prose may carry inline citations |
| `#ecs-tbody-revenue`             | `<tr>` rows with `.yoy-change` class; commentary cell may carry inline citations |
| `#ecs-tbody-volumes`             | `<tr>` rows with `.yoy-change` class; commentary cell may carry inline citations |
| `#ecs-tbody-prices`              | `<tr>` rows with `.yoy-change` class; commentary cell may carry inline citations |
| `#ecs-qualitative`               | `<strong class="subsection-title">` + `<p>` (×3); prose may carry inline citations |
| `#ecs-end-markets`               | `<strong class="subsection-title">` + `<ul><li>` (×4); bullets may carry inline citations |
| `#ecs-supply-chain`              | `<strong class="subsection-title">` + `<ul><li>` (×3); bullets may carry inline citations |
| `#ecs-geography`                 | `<strong class="subsection-title">Region: Summary</strong>` + `<ul><li>` (×4 fixed regions); bullets may carry inline citations |
| `#ecs-outlook`                   | `<strong class="subsection-title">` + `<ul><li>` per company; bullets may carry inline citations |
| `#ecs-revisions`                 | `<strong class="subsection-title">` + `<ul><li>` per company; bullets may carry inline citations |
| `#ecs-events`                    | `<strong class="subsection-title">` + `<ul><li>` per company; bullets may carry inline citations |
| `#ecs-cite-a` … `#ecs-cite-l`    | `<div class="section-citations">…</div>` (optional, see shared citations skill) |
| `#ecs-sources`                   | `<div class="source-item">` rows (see shared citations skill)      |
 
### Reference HTML snippets
 
**YOY table row** (`#ecs-tbody-revenue`, `#ecs-tbody-volumes`, `#ecs-tbody-prices`):
 
```html
<tr>
  <td class="company-name">Company A</td>
  <td class="yoy-change up">+5.20%</td>
  <td>Revenue growth driven by pricing gains in North America <a href="https://example.com/transcript-q1-2026" target="_blank" class="cite-ref">[1]</a>, partially offset by volume declines in EMEA <a href="https://example.com/credit-opinion-a" target="_blank" class="cite-ref">[2]</a>.</td>
</tr>
```
 
**Company chip** (`#ecs-company-chips`):
 
```html
<span class="company-chip">Company A</span>
```
 
**Credit sentiment badge** (`#ecs-credit-badge`):
 
```html
<div class="credit-badge positive">Positive</div>
```
 
**Subsection subheader inside prose containers**:
 
```html
<strong class="subsection-title">North America</strong>
<ul>
  <li>Retail demand held up against tariff pass-through <a href="https://example.com/transcript-q1-2026" target="_blank" class="cite-ref">[1]</a>.</li>
  <li>Pricing remained disciplined across grocery and consumables <a href="https://example.com/sector-outlook" target="_blank" class="cite-ref">[3]</a>.</li>
</ul>
```
 
**Section citations recap** (`#ecs-cite-a` … `#ecs-cite-l`) and **sources rows**
(`#ecs-sources`): see [references/shared-citations.md](references/shared-citations.md) for the
canonical markup. Reuse the same `[n]` numbering across inline references, optional recap
blocks, and the end-of-document Citations block.
 
### Class-selection rules
 
**`.yoy-change`** modifier (on the second `<td>` of YOY rows):
- `up` — value starts with `+`, equals `Up`, or parses to a positive number
- `down` — value starts with `-`, equals `Down`, or parses to a negative number
- `flat` — value equals `Flat` or `0`
- `na` — value is `Not specified`, `N/A`, empty, or `—`
**`.credit-badge`** modifier (for `#ecs-credit-badge`):
- `positive`, `negative`, or `neutral`. Label text is the capitalized sentiment.
### Conventions
 
- Use `<p>` for paragraphs, `<ul><li>` for bullets, `<strong class="subsection-title">…</strong>` for bold subheaders inside prose containers.
- Emit inline citations per [references/shared-citations.md](references/shared-citations.md). Inline citations are the primary attribution mechanism — the optional per-section blocks (`#ecs-cite-a` … `#ecs-cite-l`) remain available as supplementary summary boxes. Numeric `.yoy-change` cells stay citation-free.
- Do NOT include overall section titles — the template already has those.
- `yoy_change` values: `+X.XX%` or `-X.XX%` if numeric, else `Up` / `Down` / `Flat` / `Not specified`.
---
