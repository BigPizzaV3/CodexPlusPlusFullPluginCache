---
name: grade-my-footage
description: Use this when someone wants the look of a clip they already have changed rather than new footage made, such as a color grade, a film look, a warmer or cooler feel, a day for night pass, or matching two clips to each other. Trigger on grade, color grade, LUT, film look, match the look, fix the color. Do not use it to generate a new scene.
---

# Grade my footage

Change how an existing clip looks without changing what happens in it.

## When to trigger

Trigger on "grade this", "give it a film look", "make it warmer", "these two clips do not match", "can you fix the color", "apply a LUT".

Do not trigger when the person wants a new shot, a different action or a different subject. That is a new render, so use make-a-video.

## Ask for this first

Ask once, bundled:

1. A link to the clip, or confirmation it is already in their NOLGIA library.
2. The look they are after, in their own words. A reference film, a season, a mood or a named look all work.
3. Whether anything must stay exactly as it is, such as skin tone, a brand color or a product finish.
4. Whether this has to match another clip, and where that one is.

## Steps

1. Call `nolgia_list_color_presets` to get the names of the built-in looks. Use those names as vocabulary when you talk to the person, so they can point at one instead of describing a feeling.
2. If the clip is already theirs, call `nolgia_list_assets` filtered to video and `nolgia_get_asset` for a fresh link.
3. Call `nolgia_list_presets` if it has not been called yet in this conversation, and read the color
   grade route, which is the guided version of this job.
4. Call `nolgia_list_models` and pick a video model whose `references` block accepts video references, then check how many it takes.
5. Call `nolgia_text_to_video` with the clip passed as a video reference, either `video_asset_ids` for something in their library or `video_urls` for a link. Write the grade in the prompt: the contrast, where the shadows sit, the color of the highlights, the saturation, and the grain if any. State plainly that the action, the framing and the cut must not change, only the look. Name anything that must be protected.
6. Poll `nolgia_list_jobs`, then `nolgia_get_asset`.
7. Compare the result against the original before delivering. If the action changed, the framing moved or a face changed, that is a failed grade. Say so and re-run with a tighter instruction.

## What to return

The graded clip alongside a plain description of the look you applied, so they can ask for more or less of it. If they are matching two clips, deliver both and say which one you matched to.

Tell them the exact built-in looks can also be dialled in by hand in the NOLGIA editor if they want frame level control. Never name a model and never discuss what anything cost.

## When to stop or decline

- No clip: stop and ask for one.
- The clip is long enough that a full re-render is the wrong tool: say so, and point them at the editor for a grade applied over the whole timeline.
- The request is to make real footage of a real person look like something that did not happen: decline.
