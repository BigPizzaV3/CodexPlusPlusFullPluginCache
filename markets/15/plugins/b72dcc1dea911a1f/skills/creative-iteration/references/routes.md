# Iteration routes and prompt skeletons

Choose one route for each round. Pick the smallest change that can fix the problem. Every route gets a quote and an approval before it runs.

## Route table

| Feedback | Route | What to send | Typical size |
|---|---|---|---|
| One thing is wrong: a label, a hand, a colour or an object | Edit | The result as a reference. The edit skeleton below. | 1 image |
| Mostly right, but the feel is off: warmer, moodier or cleaner | Edit | The result as a reference. One change line and the keep line. | 1 image |
| More options near a good result | Re-roll with an anchor | The good result as a reference. The same prompt with one phrase changed. A generation count of 2 to 4. Keep the seed if the model has a seed control. | 2 to 4 images |
| "Like option 2, but with the light of option 1" | Blend | Both results as references. Name what to take from each. | 1 to 2 images |
| Wrong direction | Back a step | Correct the brief and make it again with the image or video skill. Do not patch. | A full first round |
| A clip needs a slower move, another camera move or more length | Video edit or extend | The clip as the one source video, with mode video_edit or video_extend. Change only the motion. | 1 clip |
| The product drifted in a clip | Make the clip again | The best still as the start frame. A prompt that names only the motion. | 1 clip |
| The same defect comes back after a round | Change the route | Another model from the list, or a Space built for that defect. | Depends on the route |
| Many directions from one good image | Space | A published Space that makes a grid of variations, if one fits. | Set by the Space |

## Model choice

Pick the model from the `list_models` result for the route's mode. Pick a model that takes reference images and the aspect ratio.

- For an edit, prefer a model whose description says it edits from a reference and keeps the rest.
- For a text fix, prefer a model that renders text well.
- For a re-roll, prefer a model with a seed control. Ask for 2 to 4 images. If you know the original seed, keep it and change one phrase.
- For a re-roll, explore at a lower resolution. Use the full resolution only for the direction the user picks.
- To try another model, pick it from the same list. Keep the prompt.

## Edit skeleton

```
Change only [the one thing, for example: the label text to read "NORTH FERN SERUM" exactly].
Keep everything else identical: composition, lighting, background, product shape, colours and shadows.
Do not add or remove objects. Add no other text.
```

Put any text that must appear in quotes. Spell it out letter by letter in your check.

Take the exact text from the user, the brand kit or the original product photo. Do not guess a spelling. Do not add claims.

## Re-roll with an anchor skeleton

```
Same scene as reference 1: [the scene in one line].
Keep [what worked, for example: the slate surface, the window light from the left and the tight framing].
Change: [one change, for example: warmer light and longer shadows].
Product exactly as reference 2.
```

Pass the good result as reference 1. Pass the original product photo as reference 2 when the product must stay exact.

## Blend skeleton

```
Use the composition and product placement of reference 1.
Use the light and colour of reference 2.
Keep the product exactly as it appears in reference 1.
```

## Video motion skeleton

```
Keep the scene, the product and the framing exactly as in the source.
Change only the motion: [for example: make the push-in slower and end on the label].
```

## Checks after each round

- Compare the new result with the earlier one on the thing that changed.
- Compare it on everything that must stay: product shape, label, colours, framing and background.
- If an edit changed more than asked, shorten the prompt to the change line and the keep line.
- If the seed did not hold, use the result as the anchor instead.
- If a fix still misses, change the prompt or the model. Quote again, ask for a new approval and use a new key, such as `iterate-serum-hero-1x1-v3`. This is a new round, not a retry.
- After 3 rounds that do not pass, stop and offer another route.
