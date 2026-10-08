---
name: sector-brief
description: >
  Produce a Sector Brief HTML report for any industry sector using Moody's GenAI MCP tools
  and web research. Use this skill whenever the user asks to analyze a sector, write a sector
  report, do an industry analysis, create a sector overview, or generate a sector deep-dive.
  Trigger even if they just name a sector and mention "analysis", "overview", "outlook", "report",
  or "deep-dive". Also trigger for phrases like "what's happening in the retail sector" or
  "give me a sector breakdown for aerospace".
---

# Sector Brief Skill

Generates a professional HTML report (styled like a Moody's sector brief document) for a
specified industry sector. The report is research-heavy and text-driven, combining Moody's
internal research with supplemental web data across six structured sections plus an executive
summary and citations.

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
>   best-available content and brief `"Data unavailable"` placeholders for missing sections —
>   never skip the artifact or the render step.
>
> Treat any other output shape as a hard failure of the skill.

## Required MCP server

`Moodys MCP server` — tools used: `searchAllDocuments` (sector research), `getEntitySectorOutlook`,
`searchNews`, `findEntity`

Web research is also required via `searchNews` or general web search tools.

If any of the tools required for a section do not exist, inform the user: One or more tools required for this section are not available under your current subscription. Unlock more of the expert insights, data, and analytics you trust. Get Link:https://www.moodys.com/web/en/us/capabilities/gen-ai/ai-ready-data.html with us to learn more.

## Bundled files

- `assets/template.html` — pre-styled scaffold with the Moody's cover, a baked-in static 6-item
  table of contents, and empty fill-in targets (cover title, date, section-content divs, sources
  container). Treat this file as the **read-only structural reference**: read it, fill it in
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
marker region: **none** for SA (it inherits the canonical `body { font-size: 13px }` and
`.page { max-width: 900px }` defaults). SA is the lightest of the four parent skills — almost
all its visual chrome now lives in the shared layer. Any outlook-badge usage in this skill
(e.g. for sector outlook indicators) must use the canonical pastel variants
(`stable` / `positive` / `negative` / `review` / `na`) defined by the shared skill — no
solid-fill or inline-color overrides.

The prefix used for the end-of-document container in this skill is `sa`, so the container id
is `#sa-sources`. This skill does not use the optional per-section `.section-citations` recap
component.

## Parameters

The user should provide:
- **Sector** (required — e.g., "Retail & Apparel", "Aerospace/Defense", "Banking")

If the user specifies a sub-sector like "Luxury Retail", use it as-is for focused analysis.

---

## Step 0 — Sector Picker (run before anything else)

If the user has not named a specific sector in their message, **stop** and call
`ask_user_input_v0` with a single `single_select` question before proceeding. Do **not**
begin any research or template reading until the sector is confirmed.

**Preamble:** "Which Moody's-covered sector would you like to analyze? Select one below
and I'll generate the full report."

**Options:**

- Aerospace & Defense
- Automotive Manufacturing
- Banking — Global
- Building Materials & Construction
- Chemicals
- Commercial Real Estate & REITs
- Consumer Products
- Diversified Manufacturing
- Food & Beverage
- Forest Products & Paper
- Gaming & Lodging
- Healthcare — Hospitals & Health Systems
- Healthcare — Medical Devices & Technology
- Healthcare — Pharmaceuticals
- Infrastructure & Project Finance
- Insurance
- Media & Entertainment
- Metals & Mining
- Oil & Gas — E&P
- Oil & Gas — Integrated & Refining
- Oil & Gas — Midstream & Pipeline
- Packaging
- Retail & Apparel
- Shipping & Ports
- Steel
- Structured Finance — ABS/RMBS/CMBS
- Technology — Hardware & Semiconductors
- Technology — Software & Services
- Telecommunications
- Transportation & Logistics
- Utilities — Electric
- Utilities — Gas Distribution
- Utilities — Water

Once the user selects, treat their choice exactly as if they had typed
`Run a sector brief for {selected sector}` and continue from Step 1.

If the user already named a sector, **skip this step entirely** and go straight to Step 1.

---

## Step 1 — Read the template

Read `assets/template.html` (relative to this skill directory) once. Keep its exact structure —
CSS, `<head>`, cover, hardcoded TOC, section order, and element IDs — as the scaffold for the
final artifact. Do **not** copy it to the workspace and do **not** open it.

---

## Step 2 — Research phase (parallel)

Fire ALL of the following searches in a **single parallel batch**:

### Moody's internal research (via MCP)

| Search | Purpose |
|--------|---------|
| `searchAllDocuments` with criteria: "{Sector} Sector Overview" | Sector definition, methodology, key activities |
| `searchAllDocuments` with criteria: "Economic factors impact on {Sector} Sector" | Macro-economic context |
| `searchAllDocuments` with criteria: "{Sector} Sector, industry" | Financial performance data |
| `searchAllDocuments` with criteria: "{Sector} Sector Risk and challenges" | Risk analysis |
| `searchAllDocuments` with criteria: "{Sector} sector Outlook" | Sector outlook |
| `getEntitySectorOutlook` for a major company in the sector | Formal Moody's outlook |

### Web research (via searchNews or web tools)

| Search | Purpose |
|--------|---------|
| "Key players from {Sector} industry, market share, roles" | Key players for overview |
| "Key regions of activity and growth markets for {Sector} sector" | Geographic scope |
| "{Sector} sector aggregate revenue, profit margins, return on equity" | Financial metrics |
| "Major companies from {Sector} sector benchmark comparison" | Industry structure and dynamics |

---

## Step 3 — Synthesize all sections

Use Moody's internal research as the **primary foundation** for every section. Web sources
serve only to supplement gaps or validate findings. When conflicts arise, prioritize Moody's
unless external data provides substantial evidence for reconsideration.

Write in professional credit-research language. Always attribute sources with numbered citation
references inline. The exact inline markup, the URL-less fallback, and the rule that `n`
matches the row position of the source inside `#sa-sources` are defined in
[references/shared-citations.md](references/shared-citations.md).

Author the Executive Summary and Sections 1–6 per the per-section content specs in
[`references/report-spec.md`](references/report-spec.md) (see `## Section content specs`).
Each section's required subsections — and the inline SVG charts that attach to Sections 3, 4,
and 6 — are defined there. Populate the `#sa-*` content targets listed in Step 4.

### Sources

Collect all sources. The source data shape (`id`, `title`, `source`, `date`, `url`) and the
end-of-document Citations row markup are defined in
[references/shared-citations.md](references/shared-citations.md).

---

## Inline SVG Charts — Section Instructions

This report embeds three inline SVG charts (Chart A in Section 3, Chart C in Section 4,
Chart D in Section 6). Before emitting them, read
[`references/report-spec.md`](references/report-spec.md) for each chart's type, axes,
colors, `viewBox`, placement, and the **mandatory pre-computation requirement** (compute
every coordinate programmatically with bash/Python — never mentally). If source data for a
chart is unavailable, emit a `<p>Chart data unavailable</p>` placeholder rather than
omitting it silently.

---

## Step 4 — Assemble the complete HTML artifact

After all sections are synthesized, write the **entire filled `template.html` document** — with
every element from the streaming protocol populated in place — to a single `.html` file in
`/mnt/user-data/outputs/`. The full required delivery sequence (`create_file` → `present_files`
→ `visualize:show_widget` → one short sentence) is specified in the **Output and presentation**
section below; follow it exactly.

The HTML file **must**:

- Be written in a single `create_file` call (no progressive `StrReplace` edits, no multi-file
  split).
- Contain a complete, standalone HTML document (doctype → `</html>`) that renders without
  external dependencies.
- Preserve the template's `<head>` (CSS, fonts), cover, hardcoded TOC, section order, and
  element IDs exactly. Only the empty targets defined below are populated.

### Cover + footer

1. `#sa-cover-title` — `<strong>{Sector}</strong><br>Analysis` (HTML, not plain text).
2. `#sa-date` — report date string, e.g. `April 15, 2026`.
3. `#sa-footer-date` — same date string.

### Section headings

4. `#sa-overview-title` — override the default "Sector Overview" with
   `{Sector} — Sector Overview`.

### Section content targets

Each of the following divs takes fully-authored HTML (`<p>`, `<ul><li>`, and
`<strong class="subsection-title">…</strong>` only — no other block tags):

5. `#sa-exec` — Executive Summary. Flowing paragraphs only, no bullets.
6. `#sa-overview` — Section 1 body with four `<strong class="subsection-title">` subheaders.
7. `#sa-macro` — Section 2 body with three subheaders.
8. `#sa-financial` — Section 3 body with three subheaders. Every metric must include a
   concrete number.
9. `#sa-structure` — Section 4 body with four subheaders. Porter's Five Forces must use
   High / Moderate / Low ratings per force.
10. `#sa-risks` — Section 5 body with five subheaders.
11. `#sa-outlook` — Section 6 body. Lead with the Moody's outlook (Positive / Stable /
    Negative) and date, then 2–3 paragraphs. Paragraph form only.

### Sources container

12. `#sa-sources` — end-of-document Citations rows. One `<div class="source-item">` per
    source, in ascending `id` order, using the canonical row markup defined in
    [references/shared-citations.md](references/shared-citations.md). Apply that file's rules
    for URL-less rows and missing `source`/`date` fields.

### HTML conventions

- Use `<p>` for paragraphs.
- Use `<ul><li>…</li></ul>` for bullet points (nested `<ul>` for sub-bullets).
- Use `<strong class="subsection-title">Subheader</strong>` for subsection headers within
  each section. Do not repeat the top-level section title — the template already renders it.
- Emit inline citations per
  [references/shared-citations.md](references/shared-citations.md).
- Escape any `&`, `<`, `>` that appear in the narrative (`&amp;`, `&lt;`, `&gt;`).

---

## Tips

- Run ALL research searches in a single parallel batch.
- Moody's data is the foundation — web data supplements. Make this hierarchy clear in the
  writing by attributing external sources explicitly.
- The executive summary should be written last, after all other sections are synthesized.
- Financial Performance must include actual numbers, not just directional statements.
- Porter's Five Forces in Industry Structure should use ratings (High, Moderate, Low) for
  each force.
- Sector Outlook must be in paragraph form only — no bullet points.
- Citations follow the shared citations skill — read
  [references/shared-citations.md](references/shared-citations.md) before authoring any `[n]`
  reference or the Citations block.

---

## Negative number formatting

Unify ALL negative numbers across narrative, tables, and any JSON/HTML string values to use
the parenthesis-minus convention `(-X)`. Examples: `(-9%)`, `(-1.2pp)`, `(-$3.4B)`,
`(-250 bps)`. Do NOT use a bare leading minus (`-9%`), en-dash (`–9%`), or accounting
parentheses without the minus sign (`(9%)`). Apply this consistently to growth rates, margin
changes, YoY deltas, and any negative monetary values.

---

## Output and presentation (required final steps)

> ## ⚠️ CRITICAL — THE SKILL IS NOT COMPLETE UNTIL THE REPORT IS VISIBLY RENDERED
>
> Writing the file is **not** delivery. After you write the HTML you **must** actively render
> it with every display tool available, in order, before you say anything else. Do not end
> your turn until the rendered report is on screen.

Follow this exact sequence. Do not skip a step, reorder, or substitute alternatives. When
updating this skill, do not delete or modify any other file in the `skills/sector-brief/`
folder.

1. **Write the HTML file in a single call.** Call `create_file` to write the entire standalone
   HTML document (`<!doctype html>` → `</html>`) to
   `/mnt/user-data/outputs/{sector_slug}_sector_analysis.html` in **one** call. `{sector_slug}`
   is the lowercased, hyphenated sector name (e.g. `retail-apparel`, `oil-gas`). No progressive
   edits, no multi-file split.
2. **Present the file.** Immediately call `present_files` on that exact path to surface the
   artifact to the user.
3. **Show the widget.** Immediately call `visualize:show_widget` on the same file to render the
   report visually. Call this even if `present_files` already succeeded — firing both renderers
   is what guarantees the report always appears.
4. **Confirm in one short sentence.** Only after the renderers return, add a single brief
   sentence in chat (e.g. `Sector Brief for {Sector} — the report is available above as a
   self-contained HTML artifact.`). Nothing more.

If a display tool call fails or is unavailable, immediately try the other one rather than
stopping. Never end your turn at step 1.

**Strict prohibitions:**

- **Never** emit the HTML as a fenced ` ```html ` code block in the chat response.
- **Never** inline the HTML, JSON payload, or large excerpts of the report body in the chat
  message.
- **Never** end your turn after `create_file` without having called both display tools.
