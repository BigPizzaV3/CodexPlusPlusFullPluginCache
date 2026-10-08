---
name: earnings-brief
description: >
  Produce an Earnings Call Summary HTML report for 2–5 companies using Moody's GenAI MCP tools.
  Use this skill whenever the user asks to summarize earnings calls, generate an earnings call
  summary, analyze earnings transcripts across peers, or create an earnings call report. Trigger
  even if they just name companies and mention "earnings" or "transcript".
---
 
# Earnings Brief Skill
 
Generates a professional HTML report (styled like a Moody's earnings call summary PDF) for 2–5
companies by pulling data from multiple `Moodys MCP server` MCP tools and consolidating 13
structured sections plus a hardcoded table of contents into a single HTML artifact.
 
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
>   best-available content. When the earnings call transcript for a company cannot be
>   located, **note that fact in the Executive Summary and omit the company from every other
>   section of the report** (no rows, no subtitles, no `"--"` placeholders for that company).
>   When a transcript exists but does not contain information for a specific section, **omit
>   that company from that section only** (no subtitle, no bullets, no placeholder). Never
>   skip the artifact itself.
>
> Treat any other output shape as a hard failure of the skill.
 
## Allowed data sources
 
This skill may **only** extract information from the following two sources:
 
1. `Moodys MCP server` — tools used: `findEntity` and `searchEntityEarningsCall`. These are the
   only MCP tools that may be called. Do **not** call `getCreditOpinion`,
   `getEntitySectorOutlook`, `getEntityPeers`, `searchAllDocuments`,
   `searchNews`, or any other MCP tool, regardless of section.
2. `web_search` — used **only as a fallback** when `searchEntityEarningsCall` returns no usable
   earnings call transcript for a given company, and used **only** to locate and extract the
   text of that company's earnings call transcript on the web. Do not use `web_search` for
   credit opinions, sector outlooks, news, peers, ESG, or any other purpose.
   **Recency requirement (web_search fallback):** if the transcript located via `web_search`
   is older than **100 days** from today, discard it and treat the transcript as unavailable
   for that company. Do not fall back to any other source — handle the company per the
   missing-transcript policy (note in the Executive Summary, omit from every other section).
These rules apply to **every** section of the report. No section may be enriched with credit,
sector, ESG, peer, filings, or news data.
 
## Bundled files
- `assets/template.html` — self-contained static report shell (CSS + named section placeholders).
  No embedded data, no inline script. Treat this file as the **read-only structural reference**:
  read it, fill it in, and write the complete filled document to a new `.html` file in
  `/mnt/user-data/outputs/`.
## Shared chrome & citations

Before emitting, read [`references/shared-template.md`](references/shared-template.md) (page
chrome: cover, TOC, section block, sources-section wrapper, footer, outlook-badge, design
tokens) and [`references/shared-citations.md`](references/shared-citations.md) (citation
numbering, hyperlinking, source data shape, markup snippets). Both are **authoritative** — do
not invent, duplicate, or restyle anything they already define. The canonical CSS is already
inlined in `assets/template.html` between the `/* BEGIN/END shared-template-css */` and
`/* BEGIN/END shared-citations-css */` markers; never re-copy it at emit time.

The rest of this section is the skill-specific binding.
 
This skill uses the **`cover-multi`** variant. Skill-specific overrides retained above the
marker region: **none** for ECS (it inherits the canonical `body { font-size: 13px }` and
`.page { max-width: 900px }` defaults). Skill-specific CSS that stays local: the ECS
`.credit-badge`, the `.yoy-table` / `.ratings-table` rules, and `.ratings-factors`. All
outlook-badge usage in this skill must use the canonical pastel variants
(`stable` / `positive` / `negative` / `review` / `na`) defined by the shared skill — no
solid-fill or inline-color overrides.
 
Skill-specific carve-outs that override or extend the shared rules are listed in the section
synthesis rules below — most importantly: **the numeric `.yoy-change` cell stays
citation-free** (no `<a class="cite-ref">` or `<span class="cite-ref">` inside it). The
prefix used for the end-of-document container in this skill is `ecs`, so the container id is
`#ecs-sources`. Optional per-section recap blocks live in `#ecs-cite-a` … `#ecs-cite-l`.
 
---
 
## Step 1 — Resolve companies
 
For each company name provided by the user, call `findEntity` to get the canonical entity name
and entity ID (use the canonical name throughout the report).
 
Collect 2–5 companies. If the user gives fewer than 2, ask for more.
 
---
 
## Step 2 — Read the template
 
Read `assets/template.html` (relative to this skill directory) once. Keep its exact structure —
CSS, `<head>`, hardcoded TOC, section order, table skeletons, row labels, and element IDs — as
the scaffold for the final artifact. Do **not** copy it to the workspace and do **not** open it.
 
---
 
## Step 3 — Gather earnings call transcripts
 
For each company, fire the following calls in a single parallel batch (one message, many tool calls):
 
### Earnings call transcript (×4 per company) — primary source
| Category label        | Keywords                                                                                            |
|-----------------------|-----------------------------------------------------------------------------------------------------|
| Revenue & Price       | `Revenue, Net Sales, Sales, Volumes, Units sold, Price, Pricing`                                    |
| Sector & Market       | `Industry, Sector Performance, Demand, Market Condition`                                            |
| Supply Chain & Region | `Supply Chain, Materials, Tariffs, Input, Logistics, Regional Performance, Geographic Condition, Geography` |
| Guidance & Events     | `Business Outlook, Guidance, Revision, Corporate Events, Transaction`                               |
 
### Web search fallback (only if `searchEntityEarningsCall` returns nothing usable)
 
If — and only if — `searchEntityEarningsCall` returns no usable transcript content for a given
company, run `web_search` to locate that company's most recent earnings call transcript on the
web, and extract the transcript text from the result. The web search must be scoped solely to
finding the earnings call transcript for that entity — not to news, analyst commentary, credit
opinions, or any other content.
 
**Apply the 100-day recency rule:** check the date of the transcript located via `web_search`.
If the transcript is older than 100 days from today, discard it and treat the transcript as
unavailable for that company. Do not substitute any other source.
 
All synthesis in Step 4 must be derived exclusively from the transcript content gathered in
this step (either via `searchEntityEarningsCall` or, where applicable, the web_search
fallback). No other tools may be called.
 
### Missing-tool handling
 
If any of the tools required for a section do not exist, inform the user: One or more tools required for this section are not available under your current subscription. Unlock more of the expert insights, data, and analytics you trust. Get [in touch] with us to learn more. The [in touch] should be the link Link:https://www.moodys.com/web/en/us/capabilities/gen-ai/ai-ready-data.html
 
---
 
## Step 4 — Synthesize + emit the complete artifact
 
After data is gathered, write the **entire filled `template.html` document** — with every
element from the streaming protocol populated in place — to a single `.html` file in
`/mnt/user-data/outputs/`, then render it. The full required delivery sequence (`create_file`
→ `present_files` → `visualize:show_widget` → one short sentence) is specified in the
**Output and presentation** section below; follow it exactly. The file is the deliverable; do
not paste the HTML into the chat as a fenced code block.
 
The HTML file **must**:
 
- Be a complete, standalone HTML document (doctype → `</html>`) that renders without external
  dependencies.
- Preserve the template's `<head>` (CSS, fonts), hardcoded TOC, section order, table skeletons,
  row labels, and element IDs exactly. Only the empty targets defined below are populated.
- Be written in a single `create_file` call (no progressive `str_replace` edits, no
  multi-file split).
Render order of content inside the file follows the page top-to-bottom so the artifact is
human-readable as well as browser-renderable: cover/TOC fields first, then sections 1 → 13, then
sources.
 
Use earnings call transcript content as the **sole** source for every section. Do not enrich
with credit, sector outlook, ESG, peer, or news data — those tools are not permitted in this
skill. Write in professional financial language. Name specific companies in bullets rather
than speaking abstractly.
 
Attribute substantive claims with numbered citation references. The exact inline markup, the
URL-less fallback, and the rule that `n` matches the row position of the source inside
`#ecs-sources` are defined in [references/shared-citations.md](references/shared-citations.md).
 
### Cover / header fields (write first)
- `#ecs-report-date` — e.g. `April 4, 2026` (plain text)
- `#ecs-footer-date` — same value (plain text)
- `#ecs-company-count` — number of companies (plain text)
- `#ecs-company-chips` — one `<span class="company-chip">Company Name</span>` per company (space-separated)
- `#ecs-cover-img-right`, `#ecs-cover-img-bottom` — optional. If you have image URLs or data URIs
  to use, set the `src` attributes **and** add the `has-cover-image` class to the corresponding
  container (`<div class="cover-top has-cover-image">` and/or `<div class="cover-bottom has-cover-image">`).
  If you do not have images, leave the template as-is — the empty image strips will collapse
  automatically and the cover will render as a clean navy block with the accent bar.

### Section synthesis, streaming protocol & markup

Before emitting, read [`references/report-spec.md`](references/report-spec.md) for the
authoritative body-authoring spec: the per-section synthesis rules (sections **a–l**,
including the per-section omit rule), where the optional Citations recap blocks
(`#ecs-cite-a` … `#ecs-cite-l`) and the end-of-document `#ecs-sources` rows go, the
**streaming protocol** (element → content mapping), the reference HTML snippets (YOY table
row, company chip, credit badge, subsection subheader), the `.yoy-change` / `.credit-badge`
class-selection rules, and the HTML conventions. Populate every `#ecs-*` target exactly as
specified there. Remember: the numeric `.yoy-change` cell stays citation-free.

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
   `/mnt/user-data/outputs/{companies_slug}_earnings_call_summary.html` in **one** call. No
   progressive edits, no multi-file split.
2. **Present the file.** Immediately call `present_files` on that exact path to surface the
   artifact to the user.
3. **Show the widget.** Immediately call `visualize:show_widget` on the same file to render the
   report visually. Call this even if `present_files` already succeeded — firing both renderers
   is what guarantees the report always appears.
4. **Confirm in one short sentence.** Only after the renderers return, add a single brief
   sentence in chat (e.g. `Earnings Call Summary for {Company A}, {Company B}, … — the report
   is available above as a self-contained HTML artifact.`). Nothing more.

If a display tool call fails or is unavailable, immediately try the other one rather than
stopping. Never end your turn at step 1, and never paste the HTML into chat or suggest shell
commands.
 
---
 
## Tips
 
- Run ALL data-gathering tool calls in a single parallel batch (one message, many tool calls).
- Emit the final HTML as a single `.html` file written to `/mnt/user-data/outputs/`, then
  render it with **both** `present_files` and `visualize:show_widget` (see the Output and
  presentation section) — do not paste it inline as a fenced code block, do not stream partial
  sections, do not split across multiple files or messages, and never stop at file creation.
- If `searchEntityEarningsCall` returns no usable transcript for a company, fall back to
  `web_search` **only** to retrieve that company's earnings call transcript from the web, and
  apply the 100-day recency rule. If no transcript can be located within that window, note
  the omission in the Executive Summary and exclude that company from every other section
  (no rows, no subtitles, no placeholders).
- Do not call any other MCP tool (no credit opinion, no sector outlook, no news, no peers, no
  ESG, no document search) — those sources are out of scope for this skill.
- Pick the correct `.yoy-change` / `.credit-badge` modifier class yourself using the rules above — the template no longer does this at render time.
- Emit `<tr>` rows directly inside each `<tbody id="ecs-tbody-…">` placeholder; do not re-create the `<table>` or `<thead>`.
- Inline citations follow the shared citations skill — read [references/shared-citations.md](references/shared-citations.md) before authoring any `[n]` reference or the Citations block.
