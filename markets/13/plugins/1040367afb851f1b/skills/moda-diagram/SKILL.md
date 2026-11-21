---
name: moda-diagram
description: >-
  Boxes-and-arrows diagrams on Moda with anchored connectors: flowchart, org
  chart, architecture, decision tree, swimlane, journey map, 2x2, quadrant,
  market map. Use for: "diagram this". NOT: data charts → moda-chart; UI
  screens/wireframes → moda-mockup; a decorative shape graphic (a circle with
  a caption) → moda-social; a diagram for a deck/document being built stays
  with that skill.
---

# moda-diagram

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

## Name the intent first

Two shapes live here, and they are built differently:

- **Structure with links** — flowchart, process, org chart, architecture,
  decision tree, swimlane, journey map: shapes plus `<connector>`.
- **A positioned field** — 2×2 matrix, quadrant chart, market map: axes,
  pole labels, and plotted marks built from shapes and text, **never
  `<chart>`** (it has no format for this).

Three asks that look like diagrams and are not: a bar/line/pie of real data →
load moda-chart; an app screen, wireframe, or dashboard layout → load
moda-mockup; a graphic that merely uses shapes (a quote card, a circle with a
caption) → load moda-social. A diagram destined for a deck or document
already being built stays with that skill — do not hand the build off.

Distill the content before designing: nodes and edges for a diagram, axes and
players for a matrix. Fewer primitives, shorter labels.

## Workflow

1. **Create + link**: `canvas_create(name='…', intent='an auth flow diagram',
   width=1600, height=1000, category='diagram')` — 1600×1000 suits most
   diagrams; matrices ride 960×540. `intent` explains the blank page to
   whoever opens the link first. Send it at once: "follow along live here."
2. **Read references/diagram.md** for the mode's recipe and
   references/markup.md for the connector grammar; compute the type ladder
   per references/design-quality.md. Brand kit in play → `brand_show`
   and use its palette for the accent semantics only.
3. **Author in small batches**, one section or lane per apply
   (`canvas_apply_markup(canvas_ref, page, markup)`). Connector targets
   resolve by
   same-call name, node id, or a unique existing name (ids from
   `canvas_read`), so later applies anchor to earlier nodes. Both
   endpoints must sit on the SAME page, and within one apply a node is
   defined BEFORE the connector that references it. Read every result;
   repair before adding more.
4. **Verify**: `canvas_screenshot` and LOOK — no connector crossing a
   node, no label collisions, even spacing, and the flow readable at a
   glance.
5. **Deliver**: the live link IS the handoff — diagrams get revised more than
   any other format. No format words in the ask? Offer once in the final
   reply and do NOT run it. Export:
   `export(canvas_ref, format='png', pixel_ratio=2)` (pdf when it is headed
   into a document).

## The bar

- **Links are `<connector>`, never hand-placed lines.** Connectors stay
  anchored when a node moves, including through later incremental edits;
  `from`/`to` take `@Target:top|bottom|left|right`. A connector may sit inside
  a `<group>`/`<row>`/`<column>`: it is out-of-flow there (takes no layout
  slot) and travels with the container.
- **Clarity beats exhaustiveness.** Flow top-to-bottom or left-to-right
  unless asked otherwise; detail that will not fit a box belongs in a caption
  outside the flow.
- **Color carries meaning**: neutral for ordinary steps, green for success,
  red for failure, the accent for emphasis only — never on every node.
- **Node text is the type anchor**; connector labels and captions step down.
- Swimlanes and multi-section architecture: build real lanes with containers
  and alignment (`group="true"` when a container must be a connector target),
  and keep routing simple enough to avoid crossings.



## Errors

Small applies plus a screenshot are the guard — `invalid_markup` names the
element it skipped (a connector pointing at a name that resolves to nothing
is the common one); `stale_revision` heals on one re-read and retry.
Anything else, or the same typed code twice: stop and run
`ask_expert("<what failed>", context="<the error>")` (free). Deeper recipes per
typed error live in moda-core's recovery reference.

## References

| Doc | Load when |
|---|---|
| references/diagram.md | always — the diagram and 2×2 recipes |
| references/markup.md | before writing any markup (connector grammar) |
| references/design-quality.md | type ladder, palette discipline |
| references/brand.md | a brand kit exists |
| references/edit-code.md, references/reading-and-verifying.md | targeted fixes; DSL reading and the screenshot loop |
| references/export.md, references/omni-and-media.md, references/gotchas.md | delivering png/pdf; media; anything surprising |
