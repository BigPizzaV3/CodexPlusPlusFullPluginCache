# Product video prompt skeletons

Fill the parts in square brackets. Give one camera move and one subject action per clip.

## Product as reference, new scene

Use this when the image has role reference and the product only needs to look right.

```
The [product] from reference 1 [one action], [one camera move: slow push-in, orbit, pull back or rack focus], [setting and light].
[Pace: slow and steady or lively]. [Look: editorial, warm neutral grade, soft grain].
Sound: [room tone and one named sound, no music] or none.
Keep the [label, logo, colours, shape] exactly as in reference 1. No on-screen text.
[Brand line from the brand kit, if there is one.]
```

Example: "The matte black candle from reference 1 on an oak table, flame flickering gently, slow push-in from medium to close-up, warm window light from the right, dust motes in the beam. Slow pace, warm neutral grade, soft grain. Sound: quiet room tone and a faint wick crackle, no music. Keep the label and jar shape exactly as in reference 1. No on-screen text."

## Start frame, motion only

Use this when the image has role start_frame and the clip must open on the exact still. Say only what changes. Do not describe the scene again: the model already has it, and a new description causes drift.

```
Animate the image. [What moves]: [subject motion in one clause]. Camera: [one move, speed].
Everything else stays as in the frame: [label, layout, colours]. [For a loop: end close to the opening pose.]
No on-screen text. Sound: [none or room tone].
```

Example: "Animate the image. The steam above the cup rises and curls slowly; the cup, table and logo do not move. Camera: very slow push-in. Everything else stays as in the frame. End close to the opening pose for a loop. No on-screen text. Sound: none."

## Craft rules

- Give one camera move and one subject action per clip. Do not stack adjectives.
- If the user says only "animate it", propose a move: a slow orbit or push-in for a packshot, ambient motion or a slow handheld drift for a lifestyle photo.
- For a loop, ask the clip to end close to the opening pose.
- For a 9:16 story or reel placement, keep the product out of the top 14%, the bottom 35% and 6% at each side of the frame.

## Fixes

- If text appears on screen, put "No on-screen text, no captions" first in the prompt.
- If the product changes shape, use fewer scene words and more exact words, or switch to a start frame.
- If the clip drifts away from the still, ask for "camera only, subject static" and a slower move.
