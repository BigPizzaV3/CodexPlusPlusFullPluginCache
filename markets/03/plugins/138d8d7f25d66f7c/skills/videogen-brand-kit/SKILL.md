---
name: videogen-brand-kit
description: >-
  Create or reuse VideoGen actors, products, and visual styles from reference
  images. Use when the user wants a consistent character, product, or look.
  Do not start a full video until they ask.
---

# Brand kit (actors, products, styles)

Reusable team entities. Stop after the entity exists unless they asked to generate a video next.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

They want a consistent spokesperson, product, visual look, or slideshow theme, or they brought reference images to reuse later.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. `list_entities` (filter `entityType` when you know the kind) before creating a duplicate. Built-in catalog rows have `isBuiltIn: true` and cannot be updated or archived.
3. `open_uploader` so they attach a reference still (or PDF/PPT for a slideshow theme).
4. `create_entity` with `entityType` `ACTOR`, `PRODUCT`, `VISUAL_STYLE`, or `SLIDESHOW_THEME`, plus a `name`.
5. `add_entity_reference` with the uploaded `fileId` and usually `isDefault: true`.
6. Return the `vg_enti_...` id and say how to use it: `actorEntityId` on `script_to_video` / `generate_avatar` / `slideshow_to_video`; product or style on later storyboard work; `slideshowThemeEntityId` on `slideshow_to_video`.
7. Do not start a workflow unless they asked for a video in the same turn.

## Output

A real entity id and what it is for. Do not invent ids.

## Do not

- Send them to manage entities in the VideoGen UI unless they asked (`get_app_deep_link` with `NAVIGATE` → `ENTITIES`).
- Archive or update a built-in catalog entity.
