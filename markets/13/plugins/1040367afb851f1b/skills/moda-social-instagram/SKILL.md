---
name: moda-social-instagram
description: >-
  Instagram creative: feed posts, stories, reel covers, carousels — IG sizes
  and safe areas built in. Stills only; animated → moda-video.
---

# moda-social-instagram

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
| Feed portrait / carousel slide | 1080×1350 | `carousel` | 4:5 — the IG default; use unless the user says square |
| Feed square | 1080×1080 | `social` | grid-safe; quote cards default here |
| Story / Reel cover | 1080×1920 | `social` | 9:16 vertical |

Safe areas — design full-bleed; only text, logos, CTAs, and focal points must
stay inside:

- Feed/carousel (1080×1350): platform chrome overlays ~60px top, ~50px bottom,
  ~50px top-right — keep essentials in a centered ~960×1200.
- Story/Reel (1080×1920): essentials inside y 250–1670 (username chrome above,
  reply bar below).
- Grid crop: the profile grid shows the center 1:1 — keep the subject of a 4:5
  post inside the middle square.
- Type: body ≈ 45px at 1080w, floor 28px — feed type is read at arm's length;
  cut copy before shrinking below the floor.

## Recipe — single post, story, or quote card

1. `canvas_create(name='[Topic] — IG', intent='[one-line brief]', width=1080, height=1350, category='social', brand_kit_id='[KIT]')` — send the link immediately.
2. Image-led concept? after laying out the canvas and its hero shape, use `canvas_edit_image` targeting that shape, with `operation.kind="generate"` and a full subject/style/brand-color prompt in `operation.prompt` for the hero. Type-led is equally strong — state the choice either way.
3. Author the page in ONE apply: `canvas_apply_markup(canvas_ref, page, markup)` (grammar: references/markup.md). Essentials inside the safe area above.
4. Look ONCE — `screenshot=true` on that apply returns the capture (or `canvas_screenshot(canvas_ref)`): check safe area, type floor, contrast, grid crop. Fix what fails in at most ONE repair write, captured the same way, then ship.
5. Deliver: live link + `export(canvas_ref, format='png', pixel_ratio=2)` — hand over the download link it returns.

## Recipe — carousel (5–8 slides)

1. `canvas_create(name='[Topic] carousel', intent='[brief]', width=1080, height=1350, category='carousel', brand_kit_id='[KIT]')` — link immediately.
2. Lock the system before slide 1: 2–4 colors, exactly two fonts, one grid, one
   repeating motif.
3. Author slide 1 ALONE — the hook: 5–9 words, no logo (branding on slide 1
   reads as an ad). Look once (`screenshot=true` on the apply); at most one repair write, then it is the system.
4. Create the remaining slides in `canvas_edit` code (`create('page', …)`, then
   re-read for the fresh page ids), then one markup apply per slide — vary
   composition (full-bleed type, number-hero, split, quiet slide, pull-quote,
   photo-led) so adjacent slides never repeat a layout; applies to ONE canvas
   stay serial. The last slide carries the one ask and the brand.
5. Screenshot all pages and judge as a set: brightness spread, motif continuity,
   one stat per slide (oversized numeral, small source footer). ONE repair round for what fails, then export.
6. `export(canvas_ref, format='png', pixel_ratio=2)` — a multi-page png export
   arrives as one zip, and that zip IS the IG carousel deliverable.

## Examples

- "an IG post announcing [Feature]" → single-post recipe, 1080×1350.
- "a quote card from [Person] for Instagram" → single-post recipe, 1080×1080.
- "a 6-slide carousel of [Topic] tips" → carousel recipe.
- "a story for [Event] tomorrow" → single-post recipe at 1080×1920.
- "a poster for Instagram" → this skill at 1080×1350 (platform wins over print
  words; a poster to print is moda-document-print).

## Errors

Any typed error → load moda-core and read its recovery reference.
`invalid_markup`: one page per apply, then re-run; `stale_revision` heals —
re-read and retry once.

## Make it recurring

A series ("every Monday", "tips series") → moda-automate schedules the run;
a winning layout → moda-templates saves it as the team template.

See also: moda-social — formats beyond IG, ad sets, carousel theory ·
moda-core — the contract, recovery, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/instagram.md | more depth: Reels covers, grid strategy, caption handoff |
| references/markup.md | before any markup apply |
| references/design-quality.md | type ladder detail, imagery, shaders, AI-slop list |
| references/no-brand-design.md | no kit is active — inventing the identity: palette law, type, imagery, layout system |
