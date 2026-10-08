---
name: videogen-hobby-video
description: >-
  Make a personal or hobby video (gifts, family, crafts, DIY, fan projects).
  Keep it short and ask which workflow. Do not use for business ads, training,
  news, or professional creator posts.
---

# Hobby and personal video

Personal projects, not a brand campaign.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

Gifts, family recaps, crafts, DIY, sports hobbies, fan edits, or other personal videos.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. If they have not named a workflow, ask briefly: script from text (`script_to_video`), photos/story (`storyboard_to_video`, at most 3 scenes), their audio (`voiceover_to_video`), or a deck (`slideshow_to_video`). Recommend `script_to_video` when they have a spoken idea and no shot list.
3. Keep it short. Do not add a brand CTA unless they asked for one.
4. Poll until `succeeded`. Optional `remix_project` with `CAPTIONS` and `ANIMATE_IMAGES`. `export_project` and share `downloadUrl`.

## Output

A personal MP4 and `projectId`. Do not invent ids.

## Do not

- Treat this as ecommerce UGC or influencer content unless they clearly asked for that.
- Start a long expensive storyboard for a simple personal message.
