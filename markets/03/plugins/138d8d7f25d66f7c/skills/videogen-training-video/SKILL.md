---
name: videogen-training-video
description: >-
  Make employee, customer, partner, or HR training and enablement videos, often
  with an on-screen avatar. Use for onboarding, how-tos, compliance, or
  enablement. Do not use for ads, news recaps, school courses, or film scenes.
---

# Training and enablement video

Corporate and customer training. Avatars are the usual presenter.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

Employee onboarding, policies, process training, sales enablement, customer how-tos, technical implementation, partner enablement, or HR/benefits training.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. If they have a slide deck, `open_uploader` then `slideshow_to_video` (optional `slideScripts`, `actorEntityId`, `slideshowThemeEntityId`).
3. Otherwise write a clear spoken script and call `script_to_video`. Use `aspectRatio` `{ width: 16, height: 9 }` unless they asked for another frame.
4. For an on-screen trainer: `open_uploader` a headshot if they have one, `create_entity` with `entityType: ACTOR`, `add_entity_reference` (`isDefault: true`), pass `actorEntityId` (optional `avatarQuality`). Or `list_entities` with `entityType: ACTOR` and reuse a built-in or team actor. Built-in rows have `isBuiltIn: true` and cannot be updated.
5. Poll until `succeeded`. `remix_project` with `CAPTIONS` and `TRANSITIONS`. `export_project` and share `downloadUrl`.

## Output

A training MP4 the learner can follow, plus `projectId`. Do not invent ids.

## Do not

- Make a product ad or news recap.
- Skip captions on training content unless the user asked to leave them off.
