---
name: moda-social-youtube
description: >-
  YouTube art: thumbnails (readable at 320px) and channel banners.
---

# moda-social-youtube

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

## Sizes and defaults

| Format | Size | `category` | Notes |
|---|---|---|---|
| Thumbnail | 1280×720 | `social` | judged at ~320px wide — that is the real brief |
| Channel banner | 2560×1440 | `social` | only 1546×423 centred is visible on every device |

- **Thumbnail rules, not preferences**: ≤4 words of on-image text; the subject
  or face fills a third of the frame; one high-contrast focal point; type ≥120px
  at 1280 wide so it survives the shrink. No thin weights, no full sentences.
- **Banner safe core**: everything that must be seen — name, tagline, upload
  cadence, logo — lives inside the centred 1546×423. Decoration extends outward
  into the 2560×1440 field, which desktop shows and phones crop away.

## Recipe — thumbnail

1. `canvas_create(name='[Episode] — thumb', intent='[one-line brief]', width=1280, height=720, category='social', brand_kit_id='[KIT]')` — send the link immediately.
2. Subject first: a photo the user gave you (the `upload` tool) or after laying out the canvas and its hero shape, use `canvas_edit_image` targeting that shape, with `operation.kind="generate"` and a full subject/style/brand-color prompt in `operation.prompt`.
3. Author in ONE apply: `canvas_apply_markup(canvas_ref, page, markup)` — ≤4 words, type ≥120px, one focal point (references/markup.md).
4. **The 320px check** (this recipe's verify twist): `screenshot=true` on that apply (or `canvas_screenshot(canvas_ref)`), then judge it at thumbnail scale — a thumbnail that only reads full-size is a failed thumbnail. Fix what fails in at most ONE repair write, captured the same way, then ship.
5. `export(canvas_ref, format='png', pixel_ratio=2)` — hand over the link.

## Recipe — channel banner

1. `canvas_create(name='[Channel] — banner', intent='[brief]', width=2560, height=1440, category='social', brand_kit_id='[KIT]')` — link immediately.
2. Author the safe core FIRST — the centred 1546×423 — then extend background,
   texture, and colour outward to the full frame in the same apply.
3. `canvas_screenshot(canvas_ref)`; check that cropping to the core loses
   nothing that carries meaning; at most ONE repair write, captured the same way, then ship.
4. `export(canvas_ref, format='png', pixel_ratio=2)` — hand over the link.

## Examples

- "a thumbnail for this episode" → thumbnail recipe, judged at 320px.
- "thumbnails for these 3 videos" → run the thumbnail recipe per video, one
  canvas each; the winning layout goes to moda-templates.
- "refresh our channel art" → banner recipe, everything meaningful in the core.
- "a YouTube banner AD" → not channel art: moda-social-ads owns paid formats.

## Errors

Any typed error → load moda-core and read its recovery reference.
Most likely here: type that passes full-size and dies at 320px — shrink the
screenshot before delivering. `stale_revision` heals — retry once.

## Make it recurring

Template-ize the winning thumbnail via moda-templates, then moda-automate the
per-video instance — a thumbnail system beats a thumbnail.

See also: moda-social — other platforms, ad sets, one-off graphics ·
moda-core — the contract, recovery, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/youtube.md | depth: thumbnail composition patterns, banner device crops |
| references/markup.md | before any markup apply |
| references/no-brand-design.md | no kit is active — inventing the identity: palette law, type, imagery, layout system |
