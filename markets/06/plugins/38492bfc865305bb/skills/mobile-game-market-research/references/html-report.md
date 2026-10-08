# Complete HTML Research Report

Use for authorized research deliverables and report revisions. The primary output
is one HTML file that a teammate can download and open in a browser without the
author's tools, project files, or chat. Follow the user's language and existing
visual conventions. An explicitly requested format takes precedence.

## Content and reading flow

Use the schemas in [templates.md](templates.md) and, when applicable,
[concept-development.md](concept-development.md) as content models, not a demand
for separate Markdown deliverables. Scale depth with [framework.md](framework.md).

Lead with the recommendation, confidence, strongest supporting and opposing
evidence, commitment being considered, and next action. Show report title, stable
report ID, version, updated date, evidence cutoff, research scope and level,
author/owner when known, and recommendation versus owner-approval status.

Provide an anchored table of contents; keep navigation available on long reports
without covering content on small screens. A useful reading order is:

1. Decision memo and brief: objective, scope, constraints, method and limitations.
2. Market and competitors: comparable performance snapshots and deconstructions.
3. Player and creative findings: observations, interpretation and counter-evidence.
4. Opportunities and concepts: separate market attractiveness and execution fit,
   selected and held/rejected options, concrete sessions and loops where relevant.
5. Validation and commitment: assumptions, bounded tests, thresholds and risks;
   financial scenarios and stop criteria only when the research level calls for them.
6. Evidence and data appendix: source register, underlying values, calculations,
   uncertainty, missing inputs and the current handoff.

Combine short sections and omit inapplicable ones. State material gaps instead of
filling them with invented figures. A Scan needs only its bounded findings and
decision; the format does not increase its research depth or evidence quota.

Keep all substantive findings, context, counter-evidence and recommendation-driving
data in the report. Details and appendices may collapse but must remain accessible
within the same document. External source links and optional raw exports support
further investigation; they must not be the only place to read the analysis or
values behind a chart. Large source datasets may stay in their canonical store:
embed the relevant slice or sufficient aggregates with selection rules, row counts,
exclusions, calculations and limitations to assess each claim. Mark abridgments.

## Evidence, diagrams and numbers

Give findings, concepts, sources and datasets stable IDs and internal anchors.
Link a material claim to its in-report evidence entry; include source identity,
original URL or supplied-file locator, snapshot date, platform, geography, time
window, filters and metric definitions where material. Include the relevant
observation or bounded excerpt so the reader can understand the evidence offline.
Distinguish observations, third-party estimates, calculations, hypotheses and
decisions. Preserve access limitations and source provenance when raw evidence
cannot be redistributed; include a permitted summary and flag the verification gap.

Place charts beside their interpretation. Include units, currencies, periods,
IAP/IAA and gross/net coverage where relevant, sample size, missing-value handling,
source IDs and estimate labels. Supply an in-report HTML table of plotted values
and the formulas or aggregation method. Do not plot unknowns as zero or compare
incompatible metrics as a single ranking. Show market attractiveness and execution
feasibility separately. Label financial sensitivity controls as scenarios, retain
the baseline assumptions and disclose formulas; slider outputs are not forecasts.

Use inline SVG or embedded raster images for diagrams and static charts. Render
Mermaid or other diagram syntax before delivery rather than requiring the reader
to install a renderer or load one online. Provide text descriptions of diagrams.
Add sorting, search, filters or tooltips only when they help with the actual data;
essential explanations and values must not exist only in hover interactions.

## Portable implementation and print

- Embed required CSS, JavaScript, chart data, icons and images. Use available local
  fonts or embed appropriately licensed fonts. No CDN, remote font, iframe, API,
  neighboring file or local server may be required for reading the report.
- Keep the complete content and data tables in semantic HTML. JavaScript may
  enhance navigation and comparisons; disabling it must leave the findings,
  evidence and values readable. Avoid fetching local JSON from a file URL.
- Use accessible headings, labeled controls, keyboard navigation and sufficient
  contrast. Make tables horizontally scrollable on narrow screens without causing
  the whole page to overflow. Reflow charts or use a labeled, keyboard-scrollable
  region on narrow screens; do not shrink chart labels into unreadable text.
  Do not rely only on color to express confidence.
- Treat imported reviews, source titles and dataset strings as text: escape them
  before embedding in HTML or scripts; do not execute source-supplied markup.
- Include print styles that expose all substantive sections, evidence, details
  and table rows, including those hidden by active filters or tabs. Hide controls,
  avoid clipped charts/tables and preserve readable source references. Print/PDF
  must retain the baseline values and narrative even without interactive behavior.

Prefer the simplest implementation that meets the study's needs; a framework,
server, build system or specific visualization plugin is not required. If a
required capability is unavailable, report the exact gap and deliver the best
readable artifact possible without claiming offline or print verification passed.

## Revision and sharing

Follow the receiving project's approved output location and canonical ownership.
Keep one authoritative set of findings and values. Canonical Markdown/KB/data
sources may remain internal authoring inputs; generate narrative, tables and
charts from the same versioned snapshot. If HTML itself is the authoring source,
do not create a competing Markdown copy. Increment the report version when
findings or data change; identify the superseded revision and summarize material
changes. Preserve stable anchors where possible.

Hand off the HTML as the primary artifact, with a short decision-oriented reply.
The file can be forwarded and downloaded for browser viewing; mail/chat/Drive
previews may not render HTML or run its interactions. A hosted link is an optional
way to open the same report directly when publishing is authorized. Honor the
intended audience and available access controls; a static file has no inherent
authentication. Do not claim that hosting, team access, delivery or live comments
exist unless actually configured and verified. PDF is an optional static export,
not required companion reading. External original sources may still require
network access or their own account.

## Verify the deliverable

Use available browser capabilities to open a copy of the HTML alone in a separate
folder with network disabled. Check desktop and narrow layouts, internal evidence
links, representative data against the supplied/canonical snapshot, and any
filter/sort controls. Verify JavaScript-disabled reading and print preview after
collapsing details or filtering a table: all substantive content and data must
remain available. If exporting PDF, inspect the resulting pages as well.

Record actual checks and limitations in the handoff. Structural inspection alone
does not prove browser, offline, mobile or print behavior. Validate each generated
report; the existence of this specification is not evidence that a report passed.
