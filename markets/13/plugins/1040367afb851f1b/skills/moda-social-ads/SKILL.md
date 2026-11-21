---
name: moda-social-ads
description: >-
  Static ads: platform-native single ads and multi-size display banner sets
  (IAB) — one message across sizes, exported together.
---

# moda-social-ads

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

## Sizes and defaults

The IAB core set (`category='web-ads'`), plus any size the user names:

| Size | Role | Notes |
|---|---|---|
| 300×250 | medium rectangle | the workhorse — design the MASTER here |
| 728×90 | leaderboard | hostile: one line, logo, CTA — nothing else |
| 160×600 | skyscraper | vertical stack, CTA at the bottom |
| 300×600 | half page | the roomy one; the master usually scales here first |
| 320×50 | mobile banner | hostile: type only, 4–6px off every edge |
| 970×250 | billboard | the only size with room for imagery |

Platform-native single ads (`category='web-ads'` or `'social'`): IG story ad
1080×1920 (bottom reserved from y 1400 for CTA chrome), Facebook feed ad
1200×628, IG feed ad 1080×1080 or 1080×1350.

Craft, in one pass: the Rule of One — one audience, one promise, one ask.
Hierarchy is hook → brand → CTA, with brand and CTA both visible; the CTA is
button-shaped and the highest-contrast element ("See the demo", never "Learn
more"). Keep type and CTA 8–10px off every edge — networks add a border at
serve time. Photography rarely survives these sizes: prefer solid colour,
gradients, shapes, type, and generated patterns.

## Recipe — the size set (master first)

1. `canvas_create(name='[Campaign] — ads', intent='[the one promise]', width=300, height=250, category='web-ads', brand_kit_id='[KIT]')` — send the link immediately.
2. Design and APPROVE the master on page 1: `canvas_apply_markup(canvas_ref, page, markup, screenshot=true)`, then at most one repair write. Do not adapt anything until the master is right.
3. Add one page per size in `canvas_edit` code (`create('page', { width: 728, height: 90 })`), repeated for each size in the set, then re-read for the fresh page ids.
4. Re-COMPOSE each size (never squash): one markup apply per page, serial on the
   one canvas — the same message, re-laid for the shape. Check the two hostile
   sizes (728×90, 320×50) first; they break layouts before the others do.
5. `canvas_screenshot(canvas_ref, pages=[IDS])` in ≤3-page batches; judge the set
   for one voice, one CTA, one brand presence. ONE repair round, then export.
6. `export(canvas_ref, format='png', pixel_ratio=2)` — a multi-page png export
   arrives as one zip: the set ships together, one download for the trafficker.

## Recipe — one platform-native ad

1. `canvas_create(name='[Campaign] — [placement]', intent='[the one promise]', width=[W], height=[H], category='web-ads', brand_kit_id='[KIT]')` — link immediately.
2. Write the idea in one sentence first: "For [audience], [brand] is the
   [category] that [single claim]." Kill every secondary message.
3. Author in ONE apply; keep the CTA inside the placement's chrome-free zone.
4. `canvas_screenshot(canvas_ref)` — squint test: blurred, does it still
   show what it is for and where the eye lands? Fix what fails in at most ONE repair write, captured the same way, then ship.
5. `export(canvas_ref, format='png', pixel_ratio=2)` — hand over the link.

## Examples

- "banner ads in the standard sizes" → size-set recipe, IAB core, one zip.
- "an Instagram ad for the spring sale" → platform-native recipe at 1080×1350.
- "just a 728×90 and a 300×250" → size-set recipe with those two pages only.
- "an animated banner ad" → not this skill: load moda-video (motion wins).

## Errors

Any typed error → load moda-core and read its recovery reference.
`canvas_busy` is likeliest here (many pages, many applies): applies to one
canvas stay SERIAL — they serialize on the server anyway, so fanning them out
buys nothing and can come back busy.

## Make it recurring

A campaign refresh on a cadence → moda-automate; the approved size-set skeleton
→ moda-templates, so the next campaign starts at step 4.

See also: moda-social — organic posts, carousels, one-off graphics ·
moda-core — the contract, recovery, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/ads.md | depth: IAB set, per-size composition patterns, CTA and stopping power |
| references/markup.md | before any markup apply |
| references/export.md | zip semantics, pixel ratio, warnings |
| references/no-brand-design.md | no kit is active — inventing the identity: palette law, type, imagery, layout system |
