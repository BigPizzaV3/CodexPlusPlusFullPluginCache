---
name: videogen-product-ad
description: >-
  Make a short UGC or product-marketing video for a physical or digital product
  (CPG, ecommerce, apps, gadgets). Use storyboard_to_video with at most 3
  scenes. Do not use for long explainers, training, news, film scenes, or
  service-business marketing.
---

# Product ad (physical and digital products)

VideoGen's focus cohort: first-world ecommerce and product marketing. Default to a short, visual-first spot.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

Ads, UGC, product launches, unboxings, app demos, or shoppable clips for consumer physical or digital products.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. If they have a product photo or spokesperson still, `open_uploader`, then `create_entity` (`PRODUCT` or `ACTOR`) and `add_entity_reference` with `isDefault: true`.
3. Ask only if missing: product name, one benefit, and aspect (default `{ width: 9, height: 16 }` for social; `{ width: 16, height: 9 }` if they asked for landscape).
4. Call `storyboard_to_video` with **at most 3 scenes** unless they explicitly ask for more. Each scene needs a visual `prompt`; add `voiceoverScript` for spoken lines. Typical beat: hook, product in use, call to action. Optional `style` in plain language; omit it for cinematic photo-real. Optional `quality`: `HIGH`.
5. Warn that credit use scales with scene count if they insist on more than 3 scenes, then confirm before starting.
6. Poll `get_workflow_run` until `succeeded`. Keep `projectId`.
7. `remix_project` with `CAPTIONS` and `ANIMATE_IMAGES` (add `TRANSITIONS` when it helps). Then `export_project` and share `downloadUrl`.

## Output

A short product video MP4 plus the `projectId`. Do not invent ids.

## Do not

- Expand a product brief into a 5–10 scene storyboard.
- Use `script_to_video` for a 3-shot UGC ad unless they asked for a longer narrated piece.
- Start `generate_motion_graphic` as the first example of what VideoGen can do.
