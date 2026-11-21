---
name: moda-social-linkedin
description: >-
  LinkedIn creative: posts, document carousels (exported as ONE multi-page
  PDF), banners, company-page art.
---

# moda-social-linkedin

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
| Link/landscape post image | 1200×627 | `social` | the feed default for a link-style post |
| Portrait post image | 1080×1350 | `social` | more feed height; use when the piece is type-led |
| Document-carousel page | 1080×1350 | `carousel` | 6–10 pages; ships as ONE PDF |
| Profile banner | 1584×396 | `social` | the profile photo covers the bottom-left |
| Company page cover | 1128×191 | `social` | very short — a lockup and one line, nothing else |

- Document carousels are read SMALL in the feed: headline-first pages, one idea
  per page, body type no smaller than ~34px at 1080 wide.
- Profile banner: keep the bottom-left quiet, place content center/right (the
  right two-thirds), copy limited to a name/role plus at most one short line.
- Carousel page bottom-center ~60px is overlapped by LinkedIn's own chrome.

## Recipe — document carousel (the signature move)

**A LinkedIn carousel is a document — ONE multi-page PDF, never a zip of
images.** The description promises it; the export step is where it is kept.

1. `canvas_create(name='[Topic] — LinkedIn doc', intent='[brief]', width=1080, height=1350, category='carousel', brand_kit_id='[KIT]')` — send the link immediately.
2. Lock the system first: 2–4 colors, exactly two fonts, one grid, one motif.
3. Author page 1 ALONE — the hook, 5–9 words, no logo: `canvas_apply_markup(canvas_ref, page, markup, screenshot=true)`; at most one repair write, then it is the look.
4. Create the remaining pages in `canvas_edit` code (`create('page', …)`, then re-read for the fresh page ids), then one markup apply per page — serial on one canvas. Last page carries the one ask and the brand.
5. `canvas_screenshot(canvas_ref, pages=[IDS])` in ≤3-page batches; judge as a set, fix in ONE repair round, then export.
6. `export(canvas_ref, format='pdf')` — one multi-page PDF. Read `warnings[]` and relay any caveat honestly; put the URL in the caption, since LinkedIn consumes the pages as images.

## Recipe — single post image, banner, or company art

1. `canvas_create(name='[Topic] — LinkedIn', intent='[brief]', width=[W], height=[H], category='social', brand_kit_id='[KIT]')` — link immediately.
2. Person-first when a name is given (the name is the hero lockup, the company
   supports); company-led only on request: logo + one value prop, no headshots.
3. Author in one apply: `canvas_apply_markup(canvas_ref, page, markup)`.
4. `canvas_screenshot(canvas_ref)` — check the bottom-left avatar zone on a
   banner, contrast and type floor everywhere (`screenshot=true` on the apply saves the separate call); at most ONE repair write, captured the same way, then ship.
5. `export(canvas_ref, format='png', pixel_ratio=2)` — hand over the link.

## Examples

- "a LinkedIn carousel about our launch" → document-carousel recipe → ONE PDF.
- "a post image for this announcement" → single recipe at 1200×627.
- "refresh my LinkedIn banner" → single recipe at 1584×396, content center/right.
- "company page cover for [Company]" → single recipe at 1128×191, lockup only.
- "a 10-page LinkedIn doc on [Topic]" → carousel recipe, 10 pages, one PDF.

## Errors

Any typed error → load moda-core and read its recovery reference.
The trap here is exporting a carousel as a zip: png/jpeg multi-page arrives as a
zip, so carousels export `format='pdf'`. `stale_revision` heals — retry once.

## Make it recurring

A weekly thought-leadership carousel → moda-automate runs the schedule (the
artifact still routes here); the winning page system → moda-templates.

See also: moda-social — other platforms, ad sets, carousel theory ·
moda-core — the contract, recovery, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/linkedin.md | depth: document-post conventions, banner lockups, feed legibility |
| references/markup.md | before any markup apply |
| references/export.md | PDF vs zip, warnings, pixel ratio |
| references/no-brand-design.md | no kit is active — inventing the identity: palette law, type, imagery, layout system |
