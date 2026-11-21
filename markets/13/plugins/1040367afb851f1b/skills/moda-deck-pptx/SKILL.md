---
name: moda-deck-pptx
description: >-
  Import a .pptx into Moda as an editable canvas, then fix it. For "clean up
  this PowerPoint" or any .pptx in hand. Import runs in the Moda app; this
  skill routes you there.
---

# moda-deck-pptx

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

## Sizes and defaults

| Thing | Value | Notes |
|---|---|---|
| Import | in the Moda app: Import → PowerPoint | FREE, un-billed — there is no import tool on this surface |
| Result | one canvas, one page per slide | slide size is preserved from the file |
| Round trip | `export(canvas_ref, format='pptx')` | native shapes and text layers, not screenshots |
| Data law | every source string and number survives verbatim | a cleanup that loses data is a failure |

Import is app-only here and costs nothing. Ask the user to import the deck in
the Moda app and paste the canvas link back; everything after that is yours.
Never claim you imported a file you could not.

## Recipe — import, then fix

1. Ask the user to import the deck in the Moda app and paste the canvas link back — free, and the only import route on this surface. Everything below runs on that canvas.
2. `canvas_read(canvas_ref, summary=true)` — the page index and what landed on each slide.
3. `canvas_screenshot(canvas_ref, pages=[IDS])` in ≤3-page batches, worst slides first. Judge with your own eyes; list the fixes before making any.
4. Fix smallest-change-first, one slide at a time: `canvas_edit(canvas_ref, code)` for targeted property changes (references/edit-code.md); `canvas_apply_markup(canvas_ref, page, markup, mode='replace_page_nodes', expected_revision=[REV])` to rebuild a slide outright (grammar: references/markup.md); `canvas_delete(canvas_ref, ids=[…])` for cruft. Data preservation is non-negotiable — restate every source string and number verbatim.
5. Re-theming to the team's kit? `canvas_update(canvas_ref, brand_kit_id='[KIT]')` records the kit; the tokens still have to be authored into the slides (kit creation itself is moda-brand's job).
6. `canvas_screenshot(canvas_ref)` again and compare against your fix list.
7. Deliver the live link; export back only on a format word or an accepted offer: `export(canvas_ref, format='pptx')`.
8. **Read the export warnings** — `pptx_shape_rasterized` (an image baked in rather than editable) and `pptx_content_dropped` (an element missing entirely) name exactly what did not survive. Repair or disclose; never hand over a silently degraded deck.

## Examples

- "clean up this PowerPoint" → import, screenshot the worst slides, fix, export.
- "put our brand on this deck" → import, bind the kit, re-author the tokens.
- "what's actually in this deck?" → import + `canvas_read(summary=true)`; no edits unasked.
- "fix slide 7's chart" → import, then the targeted-edit step on that page only.
- "build a NEW deck from this content" → moda-deck owns authoring from scratch.

## Errors

Any typed error → load moda-core and read its recovery reference.
An import that fails or returns an empty canvas is a file problem, not a retry
problem: say what happened, then `ask_expert("<question>")` with what the app
reported.

## Make it recurring

The cleaned deck is the team's canonical starting point — flag it with
`canvas_update(canvas_ref, template_type='template')` via moda-templates, so the
next deck starts there instead of from another crufty .pptx.

See also: moda-deck — authoring a deck from a brief, doc, or notes ·
moda-core — the contract, recovery, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/deck-design.md | judging and rebuilding an imported slide |
| references/edit-code.md | before any targeted fix program |
| references/export.md | the pptx round trip and its warnings |
