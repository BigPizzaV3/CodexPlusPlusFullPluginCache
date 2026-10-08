---
name: peer-analysis
description: >
  Produce a Peer Analysis HTML report for a target company and its credit peers using Moody's
  GenAI MCP tools. Use this skill whenever the user asks to compare a company against its peers,
  run a peer analysis, do a credit peer comparison, generate a peer group report, or analyze
  relative credit positioning. Trigger even if they just name a company and mention "peers",
  "peer comparison", "credit comparison", "peer group", or "relative value".
---

# Peer Analysis Skill

Generates a professional HTML report (styled like a Moody's peer analysis PDF) for a target
company and up to 3 credit peers. Data is pulled from multiple `Moodys MCP server` MCP tools and
consolidated into a single HTML artifact covering peers comparison, ratings chart, and ESG.

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

## Required MCP server

`Moodys MCP server` — tools used: `findEntity`, `getEntityPeers`, `getEntityRatings`,
`getCreditOpinion`, `getEntityFinancials_v2` (sections: Profile, Summary, RatingOutlook, FactorsLeadingToUpgrade,
FactorsLeadingToDowngrade, CreditStrengths, CreditChallenges, ESGConsiderations,
KeyIndicatorsTable, ScorecardTable, ESGConsiderations), `getEntitySectorOutlook`

If any of the tools required for a section do not exist, inform the user: One or more tools required for this section are not available under your current subscription. Unlock more of the expert insights, data, and analytics you trust. Get Link:https://www.moodys.com/web/en/us/capabilities/gen-ai/ai-ready-data.html with us to learn more. 

## Bundled files

- `assets/template.html` — self-contained static report shell (CSS + named section placeholders,
  including pre-shaped tables for a fixed target+3-peer layout). No embedded data, no inline
  script. Treat this file as the **read-only structural reference**: read it, fill it in
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

This skill uses the **`cover-multi`** variant. Skill-specific override retained above the
marker region: `**.page { max-width: 1050px }**` (PA reports are wider than the 900px canonical
default to fit the multi-column scorecard / key-indicators tables). Skill-specific CSS that
stays local: `.sub-heading`, all PA-specific table classes (`.pa-table`, `.credit-drivers-table`,
`.ki-table`, `.sc-table`), and the chart helpers (`.chart-container`, `.chart-title`,
`.chart-legend`, `.chart-legend-item`, `.chart-legend-swatch`). All outlook-badge usage in this
skill must use the canonical pastel variants (`stable` / `positive` / `negative` / `review` /
`na`) defined by the shared skill — no solid-fill or inline-color overrides. PA flags the target
entity on the cover with `class="company-chip target"`; the chip wrappers themselves come from
the shared cover-multi snippet.

The prefix used for the end-of-document container in this skill is `pa`, so the container id
is `#pa-sources`. Optional per-section recap blocks live in `#pa-cite-peers`,
`#pa-cite-ratings`, and `#pa-cite-esg`. Internal MCP tool names (e.g. `getCreditOpinion`)
are NEVER rendered inside `.source-meta`.

---

## Step 1 — Resolve the target company

Call `findEntity` with the company name provided by the user. Store the canonical entity name
and entity ID.

If the user provides only one company name, that is the **target company**. The peers will be
discovered automatically in Step 2.

---

## Step 2 — Discover and resolve peers

Call `getEntityPeers` for the target company. Select the top 3 peers returned.

You now have a set of up to **4 companies** (1 target + up to 3 peers). For each peer, call
`findEntity` to resolve its canonical entity name and ID.

---

## Step 3 — Read the template

Read `assets/template.html` (relative to this skill directory) once. Keep its exact structure —
CSS, `<head>`, section order, table skeletons (including all pre-shaped 4-company columns/rows),
row labels, and element IDs — as the scaffold for the final artifact. Do **not** copy it to the
workspace and do **not** open it.

---

## Step 4 — Gather all data in parallel

For every company in the set (target + up to 3 peers), fire **all of the following in a single
parallel batch** (one message, many tool calls):

### Credit Opinion data (per company)

Call `getCreditOpinion`,`getEntityFinancials_v2` requesting these sections, about the key Indicators table this should be populated with most recent fiscal year available (e.g. 2025 FY) on `getEntityFinancials_v2`. Not LTM allowed:

| Section parameter | Purpose |
|---|---|
| `Profile` | Company description for the Peers Table |
| `FactorsLeadingToUpgrade` | Upgrade factors for Credit Drivers |
| `FactorsLeadingToDowngrade` | Downgrade factors for Credit Drivers |
| `CreditStrengths` | Credit strengths for Credit Drivers |
| `CreditChallenges` | Credit challenges for Credit Drivers |
| `KeyIndicatorsTable` | Financial metrics for Key Indicators table |
| `ScorecardTable` | Scorecard data |
| `ESGConsiderations` | ESG narrative containing the CIS classification and E/S/G scores for the ESG Table & Heatmap |

### Ratings (per company)

Call `getEntityRatings` — retrieve the current long-term rating, rating class, rating date,
outlook, and historical ratings (need at least the last 5 rating actions for the Ratings Chart).

### ESG (per company)

Source ESG from the `ESGConsiderations` section of `getCreditOpinion` (requested in the Credit
Opinion call above). This section is narrative text, but Moody's states the overall CIS
classification and the E, S, and G issuer-profile scores within it (e.g. "CIS-3", "E-4", "S-3",
"G-2"). Extract those codes verbatim for the ESG Table & Heatmap. If a given score is not stated
in the narrative, follow the `na` / `--` conventions in the report spec rather than inventing one.

### Sector outlook (once per sector)

Call `getEntitySectorOutlook` for the target company's sector. Reuse for peers in the same
sector.

Hold all results in context for Step 5 synthesis.

---

## Step 5 — Synthesize + emit the complete artifact

After data is gathered, write the **entire filled `template.html` document** — with every
element from the streaming protocol populated in place — to a single `.html` file in
`/mnt/user-data/outputs/`, then render it. The full required delivery sequence (`create_file`
→ `present_files` → `visualize:show_widget` → one short sentence) is specified in the
**Step 6 — Output and presentation** section below; follow it exactly.

The HTML file **must**:

- Be written in a single `create_file` call (no progressive `StrReplace` edits, no multi-file
  split).
- Contain a complete, standalone HTML document (doctype → `</html>`) that renders without
  external dependencies.
- Preserve the template's `<head>` (CSS, fonts), section order, table skeletons, row labels, and
  element IDs exactly. Only the empty targets defined below are populated.

Write in professional financial/credit analysis language. Always reference specific companies by
name. The target company is **always the first column / first row** in every table. Render order
of content inside the file follows the page top-to-bottom so the artifact is human-readable
as well as browser-renderable: cover/header fields first, then Peers Comparison sub-sections
(1–6), Ratings Chart, ESG, and citations/sources last.

Attribute substantive claims with numbered citation references. The exact inline markup, the
URL-less fallback, and the rule that `n` matches the row position of the source inside
`#pa-sources` are defined in [references/shared-citations.md](references/shared-citations.md).

### Cover / header fields (write first)

- `#pa-report-date` — e.g. `April 20, 2026` (plain text)
- `#pa-footer-date` — same value (plain text)
- `#pa-target-company` — canonical name of the target (plain text)
- `#pa-peer-count` — integer count of peers resolved in Step 2 (plain text)
- `#pa-company-chips` — `<span class="company-chip target">Target</span>` followed by one
  `<span class="company-chip">Peer</span>` per peer (space-separated; target first)
- `#pa-cover-img-right`, `#pa-cover-img-bottom` — optional. If you have image URLs or data URIs
  to use, set the `src` attributes **and** add the `has-cover-image` class to the corresponding
  container (`<div class="cover-top has-cover-image">` and/or `<div class="cover-bottom has-cover-image">`).
  If you do not have images, leave the template as-is — the empty image strips will collapse
  automatically and the cover will render as a clean navy block with the accent bar.

### Report body — sections, streaming protocol & charts

Before emitting, read [`references/report-spec.md`](references/report-spec.md) for the
authoritative body-authoring spec: the Section 1 sub-sections (Peers Table, Peers Rating,
Credit Drivers, Key Indicators, Scorecards, Conclusion), Section 2 (Ratings Chart + analysis),
Section 3 (ESG Table + analysis), where the optional `#pa-cite-*` recaps and the
`#pa-sources` rows go, the **streaming protocol** (element → content mapping), the reference
HTML snippets, the Ratings-Chart SVG template (constants, rating→value map, coordinate
formulae), and the class-selection rules and conventions. **The spec also carries three
Amendments that override this base layout — apply them.** Populate every `#pa-*` target
exactly as specified there.

---

## Step 6 — Output and presentation (required final steps)

> ## ⚠️ CRITICAL — THE SKILL IS NOT COMPLETE UNTIL THE REPORT IS VISIBLY RENDERED
>
> Writing the file is **not** delivery. After you write the HTML you **must** actively render
> it with every display tool available, in order, before you say anything else. Do not end
> your turn until the rendered report is on screen.

Follow this exact sequence. Do not skip a step, reorder, or substitute alternatives:

1. **Write the HTML file in a single call.** Call `create_file` to write the entire standalone
   HTML document (`<!doctype html>` → `</html>`) to
   `/mnt/user-data/outputs/{target_company_slug}_peer_analysis.html` in **one** call.
   `{target_company_slug}` is the target's canonical name lowercased with spaces and special
   characters replaced by underscores (e.g. `apple_inc_peer_analysis.html`). No progressive
   edits, no multi-file split.
2. **Present the file.** Immediately call `present_files` on that exact path to surface the
   artifact to the user.
3. **Show the widget.** Immediately call `visualize:show_widget` on the same file to render the
   report visually. Call this even if `present_files` already succeeded — firing both renderers
   is what guarantees the report always appears.
4. **Confirm in one short sentence.** Only after the renderers return, add a single brief
   sentence in chat (e.g. `Peer Analysis for {Target Company} — the report is available above as
   a self-contained HTML artifact.`). Nothing more.

If a display tool call fails or is unavailable, immediately try the other one rather than
stopping. Never end your turn at step 1, and never paste the HTML into chat or suggest shell
commands.

---

## Tips

- Run ALL data-gathering tool calls in a single parallel batch (one message, many tool calls).
- Deliver the report as **one** `.html` file in `/mnt/user-data/outputs/`, then render it with
  **both** `present_files` and `visualize:show_widget` (see Step 6). Never paste it as a fenced
  ` ```html ` code block, never split across files or messages, and never stop at file creation.
- The target company always appears as the first column / first row in every table and
  comparison.
- The conclusion must orient around the target company — how it differentiates from its peers.
- If fewer than 3 peers are returned, leave the unused column/row IDs empty. The pre-shaped
  tables keep those cells blank — do not attempt to collapse or restructure the table.
- If `getCreditOpinion` does not return a particular section, write `Not available` in the
  corresponding cell rather than leaving it blank.
- `getEntitySectorOutlook` typically applies to all companies in the same sector — call once
  and reuse.
- Emit the ratings-chart SVG directly into `#pa-ratings-chart` — the template no longer builds
  the chart at render time. Pick the `.outlook-badge` class yourself using the rules above.
- For companies with fewer than 5 historical ratings, either repeat the oldest available rating
  value to fill the trailing points, or reduce `maxPts` in the chart formula to the largest
  available count (and drop the corresponding `Rating k` x-axis labels).
- Inline citations follow the shared citations skill — read
  [references/shared-citations.md](references/shared-citations.md) before authoring any `[n]`
  reference or the Citations block.

---

## Amendments (in `references/report-spec.md`)

Three amendments in [`references/report-spec.md`](references/report-spec.md) override the base
report layout and **must be applied**:

1. **Most recent fiscal year** — always populate Key Indicators and Scorecards from each
   entity's most recent FY-end `getEntityFinancials_v2` data (with the distorted-EBITDA `†`
   handling), not whatever year the credit opinion cites.
2. **Visual Enhancements** — rating summary cards (`#pa-rating-cards`), financial comparison
   bar charts (`#pa-fi-charts`), and the ESG score heatmap (`#pa-esg-heatmap`).
3. **Section layout / ratings-chart / ESG overrides** — emit rating cards instead of the
   `<tbody id="pa-peers-rating">` table, the enhanced ratings chart, and the ESG heatmap
   instead of the `<tbody id="pa-esg-table">` table.

See the spec for the full rules, reference snippets, the updated element-ID mapping, and the
exact list of base elements to omit.
