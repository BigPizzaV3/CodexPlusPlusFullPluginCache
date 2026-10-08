---
name: videogen-creator-video
description: >-
  Make social and creator content (TikTok, Reels, YouTube Shorts, influencer
  posts). Prefer short vertical video with captions. Do not use for corporate
  training, news recaps, long explainers, or cinematic film scenes.
---

# Creator and influencer video

Short-form social content for an audience, not a corporate training tape.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

TikTok, Reels, Shorts, YouTube intros, or influencer posts. The user is making content for followers, not a company L&D library.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. Default `{ width: 9, height: 16 }`. Ask only if they want landscape.
3. If they want a 2–3 beat hook (face, demo, CTA), call `storyboard_to_video` with **at most 3 scenes**, each with `prompt` and optional `voiceoverScript`.
4. If they want a spoken talking-track over b-roll, call `script_to_video` and keep it short.
5. If they have a recorded voiceover, `open_uploader` then `voiceover_to_video`.
6. Poll until `succeeded`. `remix_project` with `CAPTIONS` and `ANIMATE_IMAGES`. `export_project` and share `downloadUrl`.

## Output

A social-ready MP4 and `projectId`. Do not invent ids.

## Do not

- Build a long landscape explainer (use videogen-marketing-video or videogen-education-video).
- Skip captions on vertical social unless they asked to leave them off.
