---
name: retouch
description: Change an image that already exists — edit, enhance, upscale, cut out the background, or apply film grain and colour grading. Use when there is already an image and the user wants it altered. Not for adding motion (use Effects) and not for generating from scratch (use Studio).
---

# Retoucher

The signal: **there is already an image**, and the user wants it changed.

## Tokens

| Token | Tool |
|---|---|
| `/cutout` `/remove-bg` | `remove_background` |
| `/enhance` `/upscale` | `enhance_image` |
| `/retouch` `/edit` | `edit_photo` |
| `/grain` `/grade` | `list_image_effects` → `apply_image_effect` |

`request_image_upload` for attachments — it renders the widget and places URLs into
context. Never call `user_upload` directly.

## Image effects are a finishing pass

`list_image_effects` returns **grain / film-stock and colour-grade presets**. They
re-render the image while preserving subject, wardrobe, pose, framing and background —
they do not add motion and do not change content.

Narrow the catalogue with `kind`: `grain` or `colorGrade`. Omit for both.

`apply_image_effect` takes `effect_id` and `asset_id` and runs a two-step workflow —
analyse the source with the preset, then image-to-image re-render. **It requires a paid
organization.** It also recovers the source's framing, resolution and (for fashion assets)
project and composition, and preserves them.

## The rule that matters

**Do only what was asked.** If the user says "remove the background", don't also brighten,
sharpen and recompose. Unrequested changes read as the tool malfunctioning, not as extra
value. When you think something else would help, say so in a line and offer — don't do it.

## Finishing a generation

Where a widget renders, it polls itself — don't call `fetch_status`. On a text-only host,
poll `fetch_status` with `id=<uuid>` and `sync: true` until `complete` or `error`.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## Inspect before generating

A request to change something that already exists is an **edit**, not a build. Find the
existing asset and modify it. Generate only what the requested change actually requires.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
