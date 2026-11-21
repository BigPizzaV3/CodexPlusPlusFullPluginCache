---
name: make-a-video
description: Use this when someone wants a finished video made from a written brief, such as a social ad, a brand spot, a product film, a scene, an explainer or a trailer, and also when they hand over a still image and want it to move. Do not use it to change the look of footage that already exists, and do not use it for narration or music on its own.
---

# Make a video

Turn a spoken brief into a finished clip the person can download and post.

## When to trigger

Trigger when someone describes a video they want and expects a file back. Typical openings: "make me a 15 second ad for", "I need a spot for my brand", "turn this photo into a clip", "can you film this scene".

Do not trigger when the person only wants an existing clip regraded (use grade-my-footage), when they only want narration or music (use voiceover-for-a-script), or when they are asking what NOLGIA can make (use run-a-preset).

## Ask for this first

Ask once, in a single friendly message, and accept one word answers:

1. What it is for, and the brand, product or subject.
2. Where it runs, so the shape is right: vertical for phones, wide for a site or a screen, square for a feed.
3. How long, in seconds.
4. The feeling, in three words.
5. Anything of theirs it must include: a link to a photo, a product shot, a logo, or an asset already in their NOLGIA library.

If they say they do not know, offer two or three concrete directions and take it from there. Never make them write the prompt. You write the prompt from their answers.

If they give a complete brief up front, follow it to the letter and only fill the gaps.

## Steps

1. Call `nolgia_list_presets` ONCE, and only if you have not already called it in this conversation: a
   repeat returns the same catalog and draws a duplicate gallery. If one of the guided routes clearly
   matches what they asked for, say so and hand over to the run-a-preset skill instead of improvising.
2. Call `nolgia_list_models` and pick a video model whose durations and aspect ratios cover the brief, and whose reference inputs cover whatever material they supplied. Check the model's `references` block before you pass any reference field, because the server rejects fields the model does not accept.
3. If they gave a starting image, call `nolgia_image_to_video` with `image_url` set to that image. Otherwise call `nolgia_text_to_video`. Write a full prompt yourself: the setting, the action, the camera, the light and the mood. Set `aspect_ratio` and `duration_seconds` from their answers. For anything longer than one continuous take, pass `shots`, each with its own `prompt` and `duration_seconds`.
4. Video runs as a background job. Poll `nolgia_list_jobs` until the job is finished or failed. Tell the person it is rendering and roughly how long it takes. Do not poll in a tight loop.
5. When it finishes, call `nolgia_get_asset` for the link.
6. If this is part of a campaign with more pieces coming, call `nolgia_create_project` once and then `nolgia_add_project_assets` so everything stays together.

## What to return

The finished clip, a one line description of what you made, and the shape and length. Offer one next step: a cutdown, a different aspect ratio, or a voiceover over the top.

Never name a model, never quote a preset's internal guidance text back to the person, and never discuss what anything cost.

## When to stop or decline

- No brief and no answers: ask, do not guess.
- They want a real, named person depicted: decline and offer a character of their own instead.
- The job comes back failed: say so plainly, say what you will change, and offer to re-run once. Do not re-run silently more than once.
