---
name: remake-a-clip
description: Use this when someone has a video clip and wants it remade rather than a new one made from scratch. Three ways are covered. Keep the clip's movement and have their own photos, characters or product perform it, swap or remove one person, animal, product, prop or outfit and keep the rest of the shot exactly as filmed, or keep the subject and its movement and move the whole scene to a new place with new light. Trigger on remake, redo this clip, swap, replace the person, remove the boom mic, take the crew member out, get rid of the cup, put my product in this, same moves, new setting, new world. Do not use it to change only the colors of a clip.
---

# Remake a clip

Miroge remakes a clip the person already has. It keeps what they want from the original and changes the rest.

## When to trigger

Trigger on "remake this with my product", "same dance, but it's me", "swap the mug for our bottle", "remove the boom mic from this take", "take the guy in the vest out of the shot", "put this scene on a beach at sunset", "keep the rider, change the city".

Do not trigger when the person only wants the colors or the grade changed (use grade-my-footage), wants other camera angles of the same take (use every-angle-from-one-take), or has no clip at all (use make-a-video).

## The three ways

- **Motion transfer**: the clip's moves, timing and camera, performed by the person's own photos, saved characters or product.
- **Swap**: replace one person, animal, product or outfit and keep everything else as filmed. Swap can also **remove** one thing (a boom mic, a crew member, a stray cup): Miroge finds it in the clip, redraws only that spot, and gives back every other frame exactly as filmed, faces and sound included.
- **New world**: keep the subject and its moves, and redraw the place and the light around it.

## Ask for this first

Ask once, bundled:

1. Which clip: one already in their NOLGIA library.
2. Which of the three ways, in their words if they are not sure. You can map it.
3. For motion transfer or a swap, who or what goes in: a photo in their library, a saved character or a saved product. A swap can also be described in words. For a removal, only what should go, in a few plain words, the way it looks in the shot.
4. For a new world, the new place, its material, color and light, and anything that must stay exactly as it is.

## Steps

1. Find the clip with `nolgia_list_assets` filtered to video, and any photos they name the same way. Where the host shows this server's cards, let the person point at them.
2. If they want to compare prices or models first, call `nolgia_miroge_options` with the clip, the mode and the same photos, characters or product. It is free.
3. Call `nolgia_miroge` with the clip as `source_asset_id`, the `mode` (motion, swap or world), the cast in `element_asset_ids`, `character_ids` or `product_id`, and the person's own words in `prompt`. Miroge writes the rest of the instruction itself, so do not pad the prompt. For a new world, put what must not change in `keep`. To take something out, send `mode` swap with `remove` naming it in a few plain words ("the boom mic", "the man in the yellow vest") and no cast: that is what the site's Remove sends, and everything else comes back exactly as filmed. Leave length and shape alone unless the person asks, so the remake matches the clip.
4. The render runs in the background. Check it with `nolgia_get_miroge`, passing the same clip and mode so the card shows the original beside the remake. Do not poll in a tight loop.
5. Only if the person asks for another version of the identical remake, send it again with `another_take` set. Otherwise a repeat within five minutes returns the render already running.
6. If they ask to stop it, call `nolgia_cancel_job` after confirming, and tell them what the result says about credits.

## What to return

The remake beside the original, the way it was remade in one line, and what was kept. For a removal, say what was taken out and that the rest of the shot, faces and sound are the original's. Offer one next step: the same clip in one of the other two ways, or a different place for the new world.

Never name a model, and never promise a refund or a price the tool result does not show.

## When to stop or decline

- No clip: stop and ask for one.
- A new world with no description of the place: ask for it before anything is spent.
- The swap or the cast would put a real, named person the user has no rights to into the clip: decline and offer a saved character of their own instead.
- The render fails: say so plainly with the reason the result gives, and offer one re-run. A removal that could not find the thing says what it looked for and refunds the credits: ask the person to name it more plainly (its color and what it is) before running it again.
