---
name: animate-a-logo
description: Use this when someone wants their logo or wordmark turned into a short animated ident, sting, bumper, reveal or end card. Trigger on logo animation, animate my logo, logo reveal, brand sting, ident, intro. Do not use it to design a new logo from nothing, and do not use it for a full advertisement.
---

# Animate a logo

Take a still mark and hand back a short ident the person can put on the front or the back of anything.

## When to trigger

Trigger on "animate my logo", "logo reveal", "I need an intro sting", "make an end card", "a bumper for my videos".

Do not trigger when there is no mark yet and the person actually wants one designed. In that case offer the logo route in run-a-preset first, then come back here.

## Ask for this first

Ask once, bundled:

1. A link to the mark, or confirmation it is already in their NOLGIA library. A version on a plain background works best.
2. How long, usually three to six seconds.
3. The feeling: clean and corporate, fast and sharp, warm and handmade, heavy and cinematic.
4. The shape: wide, square or vertical.
5. Whether a tagline appears under it, and the exact wording if so.

## Steps

1. If the mark is already theirs, call `nolgia_list_assets` and `nolgia_get_asset` to get a fresh link. If they only have it on a busy background, offer to clean it first with `nolgia_image_to_image`.
2. Call `nolgia_list_presets` if it has not been called yet in this conversation, and check the logo
   reveal routes. If one matches the feeling they described, follow its description.
3. Call `nolgia_list_models` and pick a video model that accepts a starting frame at the length and shape you need.
4. Call `nolgia_image_to_video` with `image_url` set to the mark. Write the movement yourself: how the mark arrives, what the light does, how it settles, and how long it holds at the end. Say in the prompt that the mark must match the reference exactly, with no redesign and no added or altered lettering. Set `aspect_ratio` and `duration_seconds`.
5. Poll `nolgia_list_jobs` until the job finishes, then call `nolgia_get_asset`.
6. Check the result frame by frame before delivering. Reject anything where the mark warps, the lettering changes, or extra text appears. Re-run it.

## What to return

The ident, its length and shape, and a note on where it sits best, front or back. Offer a second version at a different length, since most people want both a long and a short one.

Never name a model and never discuss what anything cost.

## When to stop or decline

- No mark and no willingness to make one: stop.
- The mark belongs to a company the person does not represent: decline.
- The lettering comes back wrong twice in a row: say so, and suggest holding the mark still and animating the background instead.
