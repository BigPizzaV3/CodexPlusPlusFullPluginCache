---
name: videogen-film-scene
description: >-
  Make cinematic or narrative film and entertainment scenes with shot-by-shot
  visual control. Use storyboard_to_video. Do not use for ads, news, training,
  or social-creator shorts.
---

# Film and entertainment scene

Cinematic narrative shots, not a marketing spot.

Also follow `references/always.md`.

If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry.

## When to use

Film, TV, narrative shorts, mood pieces, or entertainment scenes where the user cares about what each shot looks like.

## Steps

1. Call `get_me` if this chat has not already confirmed a linked account.
2. Collect the beat: setting, characters, action, camera. Do not invent plot the user did not ask for.
3. Call `storyboard_to_video` with **at most 3 scenes** unless they explicitly ask for more. Each scene needs a visual `prompt` (lighting, lens, blocking). Optional `voiceoverScript`, `title`, `durationSeconds` (1–15). Optional `style` for a named look; omit for cinematic photo-real.
4. Confirm before going past 3 scenes. Credit use scales with scene count.
5. Poll until `succeeded`. Optional `remix_project` with `ANIMATE_IMAGES` and `TRANSITIONS`. `export_project` and share `downloadUrl`.

## Output

A cinematic scene MP4 and `projectId`. Do not invent ids.

## Do not

- Turn a film brief into a product ad or news recap.
- Pad a single shot request into a long storyboard.
