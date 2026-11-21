---
name: voyager-cloud-video
description: "Cloud: generate short AI video clips with Voyager from a prompt, a start image or references, including saved Cast characters."
---

# Short videos

Follow `voyager-cloud` (read it with `load_skill` if it isn't loaded) for account,
models, costs and jobs. This plugin
makes short clips one at a time. Editing, cutting several clips together, titles and
timelines are not available here; if the local Voyager plugin is installed, use it
for that.

## Real product UI is never generated

Never generate a real app's screens, a website or a real product's interface:
models invent text and controls. Ask for a real screen recording or screenshot
and use it as a reference, or show the product in an abstract way.

## Generate a clip

1. Choose the video model as `voyager-cloud` describes: exactly the model the
   user named, otherwise the default (omit `model`). For a clip from a still the
   recommended image-to-video model takes the start image. Use only durations,
   aspect ratios, references and audio options the model supports, and pass a
   start image or other references as asset IDs in `reference_ids` or in the
   reference fields the model lists.
2. For a clip from a still, make or import the still first and show it; animate
   the still the user approved, and spend the video prompt on action and camera.
3. Pass Cast IDs for every recurring character on every clip and retake.
4. Call `generate_video` and poll
   `get_job`. Video takes minutes: tell the user it is running and poll the same
   job; never submit it again because it is slow.

## Inspect and deliver

Look at the result before presenting it: check the subject, motion, the
character's likeness and any requested words. A clip that drifted from the
approved still or Cast look is a failed take; say what failed and offer one
retake with a corrected prompt. Deliver with the download from `get_asset`.

## Track an object (SAM)

To track an object through an imported clip, run `generate_segmentation`
with `video` (the image rules are in `voyager-cloud-image`, "Select objects").

- `sam-3-1` for tracking: stable object ids across the clip and many objects
  at once. `sam-3` for a text prompt on a simple clip; `sam-2` for clicks or
  boxes only.
- Points and boxes are in the frame's own pixels and carry the `frame_index`
  they were placed on (also settable once as `frame_index`); pick a frame where
  the object is clearly visible.
- `mode` `segment-video-data` (the default for a video) returns one
  black-and-white mask video per object (white = object, same size, fps and
  frame count as the clip) and the JSON data; `segment-video` returns the
  clip with the tracked objects rendered.
- A mask video is a video editor's matte or an inpainting model's mask video
  (white = regenerate); download it from `get_asset`.
- Cost: about 0.5 credits per 16 frames with SAM 3 or SAM 2 (a 10 s clip at
  24 fps is 240 frames, about 7.5 credits), twice that with SAM 3.1. Estimate a
  long clip first.

## Exclusions

Every generated clip risks the same defects. Exclude this base set unless the
brief wants one of them: on-screen text and signage, logos, watermarks, morphing
(objects or bodies changing shape), extra limbs or objects, glow, particles and
lens flares, and palette drift. Use a negative-prompt field only when the model's `list_models` settings
  include one, passing it in `parameters` with the base set and any scene
  exclusion as nouns. Otherwise describe the
  wanted state ("an empty, dry street", "plain unmarked storefronts", "colours
  steady from start to end"); a brief closing line of exclusions ("No umbrellas,
  no shop signs.") is fine. Never describe the unwanted thing positively to limit
  it ("only two or three umbrellas", "one woman with a red umbrella", drizzle),
  and keep it out of the keyframe stills: what the prompt or a still shows, the
  model renders.

## The style key wins over photo references

Image models follow a photo more readily than words: given a photo of a person
and "line art", they tend to return a photo of the person. Once a style is set
(a requested look such as line art or a storyboard sketch, or a style key image),
hold it:

- For a recurring character, pass Cast IDs on every
  image/video estimate and run. The adapter adds its fixed description, refs
  and model token mapping. Write shot action, composition, camera, look and
  sound around the character's name; do not invent numbered Cast-ref tokens.
  With Elements (`cast` packages, see `voyager-cloud`), write `@as` where the
  Element appears instead of its name, and relay `cast_usage` warnings.
- Pass a photo only for identity: the face, hair, wardrobe, a product's shape and
  markings, a prop. Say which image does what, and that the photo does not set
  the look: "Use image 2 only for the woman's face, hair and coat. Draw the whole
  frame as loose black line art on white, like image 1, not as a photograph."
- Pass the style key image, when there is one, with every frame, and repeat its
  words in every prompt. A shot under a film's scoped look (a photoreal
  flashback) takes that look's image and words instead.
- Before accepting a frame, compare it with the look that applies to it: the
  same medium, line, fill, texture and palette. A frame that matches its scoped
  look is not a failed take. A frame that drifted toward the photo is a
  failed take, not a variant. Keep the same `cast` IDs and strengthen the style
  direction on a correction. Do not drop identity refs or substitute text-only
  identity. Report
  likeness results separately from style inspection: a face match can still be
  off-look, and an unavailable check is not a match.
