---
name: videogen-marketing-video
description: >-
  Make a narrated marketing or communications video for professional services,
  B2B software, real estate, local businesses, travel, events, or nonprofits.
  Prefer script_to_video. Do not use for product UGC ads, training, education
  lessons, news recaps, or social-creator shorts.
---

# Marketing and communications video

Narrated campaign and services marketing (not a 3-shot product UGC ad).

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

Agencies, legal, finance, healthcare practices, recruiting, SaaS, real estate listings, local services, travel and hospitality, events, or nonprofit campaigns.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. Draft or use their script. `script` is spoken verbatim, so write for the ear (about 20–30 seconds per ~50 words). Prefer about one minute unless they asked otherwise.
3. Default to `script_to_video` with optional `style`, `aspectRatio` (default `{ width: 16, height: 9 }`), `language`, and `voiceId` from `list_tts_voices` when they care about the voice.
4. Use `storyboard_to_video` only if they want a short shot list (property hero shots, event teaser). Cap at 3 scenes unless they explicitly ask for more.
5. For a talking-head presenter, create or reuse an `ACTOR` entity and pass `actorEntityId` (optional `avatarQuality`).
6. For a PDF one-pager or slide deck, `open_uploader` then `slideshow_to_video`.
7. Poll until `succeeded`, `remix_project` with `CAPTIONS` plus `ANIMATE_IMAGES` or `TRANSITIONS`, `export_project`, share `downloadUrl`.

## Output

A narrated marketing MP4 and `projectId`. Do not invent ids.

## Do not

- Treat a long services explainer as a many-scene storyboard.
- Use this skill for CPG/app UGC (use videogen-product-ad) or employee training (use videogen-training-video).
