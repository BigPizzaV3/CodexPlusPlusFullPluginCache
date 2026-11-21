---
name: moda-social-tiktok
description: >-
  TikTok stills: video covers and photo-mode posts — 9:16 sizing and safe
  areas.
---

# moda-social-tiktok

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
| Cover frame / photo-mode page | 1080×1920 | `social` | 9:16 — everything on TikTok is this size |
| Photo-mode set | 1080×1920 × N | `carousel` | one page per photo; ships as a zip of pngs |

Safe areas — design full-bleed; only text, logos, CTAs, and focal points stay
inside:

- **Post**: UI covers top y 0–190, the right icon rail x 900–1080 (y 190–1780),
  and the caption band y 1780–1920. Safe zone **x 120–840, y 252–1742**.
- **Ad**: extra CTA chrome — bottom reserved from y 1400. Safe zone **x 120–840,
  y 252–1280**. Assume a normal post unless the user says ad.
- Cover frames are also shown as a small grid tile on the profile: the subject
  and any title must survive at ~1/6 scale.
- Type: body ≈ 48px at 1080 wide, floor 32px — vertical video is read in motion.

This skill owns the STILL: the cover frame and photo-mode pages. An actual
TikTok video is moda-video (render format wins over platform).

## Recipe — cover frame or single photo-mode page

1. `canvas_create(name='[Topic] — TikTok', intent='[one-line brief]', width=1080, height=1920, category='social', brand_kit_id='[KIT]')` — send the link immediately.
2. Image-led? after laying out the canvas and its hero shape, use `canvas_edit_image` targeting that shape, with `operation.kind="generate"` and a full subject/style/brand-color prompt in `operation.prompt` for the backdrop; type-led is equally strong.
3. Author in ONE apply: `canvas_apply_markup(canvas_ref, page, markup)` — title inside x 120–840, y 252–1742 (references/markup.md).
4. Look ONCE — `screenshot=true` on that apply returns the capture (or `canvas_screenshot(canvas_ref)`): check the right rail and caption band are clear, then judge the title at tile scale; at most ONE repair write, captured the same way, then ship.
5. `export(canvas_ref, format='png', pixel_ratio=2)` — hand over the link.

## Recipe — photo-mode set

1. `canvas_create(name='[Topic] — photo set', width=1080, height=1920, category='carousel', brand_kit_id='[KIT]')` — link immediately.
2. Prove page 1 alone (author → look → at most one fix) before adding pages: it sets
   the system every later page repeats — 2–4 colors, two fonts, one motif.
3. Create the rest in `canvas_edit` code (`create('page', …)`, then re-read for
   the fresh page ids), then one markup apply per page, serial on the one
   canvas; vary composition so neighbours differ.
4. `canvas_screenshot(canvas_ref, pages=[IDS])` in ≤3-page batches; judge as a set, fix in ONE repair round, then export.
5. `export(canvas_ref, format='png', pixel_ratio=2)` — a multi-page png export
   arrives as one zip, and that zip IS the photo-mode deliverable.

## Examples

- "a cover for our new TikTok" → cover recipe at 1080×1920.
- "a 5-photo TikTok post about [Topic]" → photo-mode set, 5 pages, zip.
- "a TikTok ad still" → cover recipe with the ad safe zone (bottom clear from y 1400).
- "make the TikTok video itself" → not this skill: load moda-video.

## Errors

Any typed error → load moda-core and read its recovery reference.
Most likely here: text drifting under the right rail — capture the fixing write
(`screenshot=true`); still one repair round, not a loop. `stale_revision` heals — re-read and retry once.

## Make it recurring

A cover-frame series on a posting cadence → moda-automate; the proven cover
layout → moda-templates, so every upload starts from the winner.

See also: moda-social — other platforms, carousel theory, one-off graphics ·
moda-core — the contract, recovery, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/tiktok.md | depth: safe-area map, cover-vs-photo craft, tile-scale legibility |
| references/markup.md | before any markup apply |
| references/no-brand-design.md | no kit is active — inventing the identity: palette law, type, imagery, layout system |
