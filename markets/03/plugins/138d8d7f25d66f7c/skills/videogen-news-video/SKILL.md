---
name: videogen-news-video
description: >-
  Make a news recap, briefing, or launch-summary video from text. Prefer
  script_to_video around one minute, landscape. Do not use for ads, training,
  education lessons, or cinematic film scenes.
---

# News and briefing video

Short recap or briefing from a script, not an ad.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

News recaps, daily briefings, launch summaries, or "what happened" videos from text the user provides or that is already in the chat.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. Write a tight spoken script from the source they gave. Do not invent quotes, numbers, or outcomes. If a fact is missing, ask or skip it.
3. Call `script_to_video` with `{ width: 16, height: 9 }` unless they asked for another frame. Optional `style` for a news-desk or clean editorial look.
4. Poll until `succeeded`. `remix_project` with `CAPTIONS` and `ANIMATE_IMAGES`. `export_project` and share `downloadUrl`.

## Output

A briefing MP4 and `projectId`. Do not invent ids.

## Do not

- Use `storyboard_to_video` for a one-minute recap.
- Turn a news brief into a product ad or opinion piece the user did not ask for.
