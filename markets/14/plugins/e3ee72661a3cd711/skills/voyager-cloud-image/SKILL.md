---
name: voyager-cloud-image
description: "Cloud: generate or edit still images with Voyager, including branded images and images of saved Cast characters."
---

# Images

Follow `voyager-cloud` (read it with `load_skill` if it isn't loaded) for account,
models, costs and jobs.
Choose the image model as `voyager-cloud` describes. Honor an explicit size,
aspect ratio, count and quality; otherwise make one square image.

## Source real subjects

For a real subject, use the first usable source: the user's asset (brief,
attachments in this conversation or a brand kit), then the
subject's official source or open libraries/stock, then generation when exact
structure or labels are not required, then a hand-built depiction labeled
schematic. The user's explicitly requested version wins; a guessed asset type
is not such a request. Abstract or invented subjects are made freely. Follow the
runtime's likeness, licensing and factual-claim boundaries.

## Recurring characters

For a character across several images, use a Cast card as `voyager-cloud`
describes and pass its ID with `generate_image` on every image, edits included.
Additional style, composition or edit references stay explicit asset IDs.
Visually compare results with their references; never invent a likeness verdict.

## Exact words, logos and layouts

Image models misspell and redraw. When the brief needs exact words, a real logo
or several sizes, generate the picture without lettering and say that exact text
and layout are finished in a design tool; pass a real logo only as an imported or
brand-kit asset ID, never redrawn from memory. A thumbnail may heighten the real
story; it should not imply events the video never contains.

## Generate or edit

Write the prompt as subject, action, setting, composition, light and look. For an
edit, import the image with `import_reference`, pass its asset ID and describe
only the change and what must stay the same. Say which reference does what when
there are several ("image 1 sets the look; image 2 is the product"). Show every
output; offer one targeted retake rather than a batch of guesses.

## Select objects (SAM)

To select an object, cut it out, erase or replace it, or turn it into 3D, run
`generate_segmentation` (Meta's SAM) on an imported image. It returns one mask
per object (white object on black, the source's size), a transparent cut-out
per object, a preview and a JSON data file; show the preview.

- Model: `sam-3` by default, with a text `prompt` ("the red car", "every
  person"). `sam-2` takes clicks and boxes only, and `mode`
  `segment-everything` (every object, no selection). `sam-3-1` for video
  tracking (see `voyager-cloud-video`).
- Select by `prompt`, `points` (`{x, y, label: "positive"|"negative"}`; a
  negative point excludes that spot) or `boxes` (`{x_min, y_min, x_max,
  y_max}`), in the image's own pixels with the origin top-left, never display
  or thumbnail coordinates. `max_objects` caps the count.
- `mode`: `segment-image` (default), `segment-image-data` (masks from raw
  data), `segment-everything`, `image-embedding` (a JSON file for other tools).
- Erase or replace: pass the mask's `file_` id as `mask` in `parameters` of an
  edit model that lists a mask (GPT Image 2.6 Flare, Ideogram 4.5; read
  `list_models(model=...)` for its mask convention) with the image, and
  describe the area's new content. A cut-out is already the object on a
  transparent background.
- Object to 3D: `generate_3d(model="sam-3", mode="image-to-3d")` with the image
  and the masks in `parameters` (`image`, `masks`); `image-to-3d-body` for one
  person (`image`, `mask`).
- Cost: about 0.5 credits per image with SAM 3 or SAM 2, twice that with SAM
  3.1, 2 credits per 3D result. A wrong selection is a cheap retake: adjust the
  points or prompt, not the model.

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

## Brand and type

- [Typography](references/typography.md) for any lettered image.
- [Color and brand](references/color-and-brand.md) for named brands, brand kits and contrast.

When these files aren't available, read them with `load_skill` for this skill and
`file` set to the path.

## GPT Image 2.6 Flare and Sunburst

Use the model ID `gpt-image-2.6-flare` or `gpt-image-2.6-sunburst`; reference images make it an edit.
- **Flare:** Clean text, transparency, careful edits and quick GIFs.
- **Sunburst:** Intricate hero art, showcase GIFs and demanding revisions, slower.
Read `list_models` for that exact operation's schema before building settings.

- `quality` (default high) and `reasoning_effort` (default high) are separate settings;
  take their values from `list_models`. Extra reasoning adds latency and tokens.
- Keep both models' defaults unless requested: `image_size: "landscape_4_3"` for generation
  (`auto` for edits), `background: "auto"`, and `output_format: "png"`.
- Text-to-image supports PNG/JPEG/WebP, GIF animation and SVG. Edit supports
  PNG/JPEG/WebP and GIF. SVG requires `count: 1`.
- For GIFs, animated stickers, looping reactions, or animated logos, choose **Sunburst** with
  `output_format: "gif"` by default: it is the showcase-quality choice. Use Flare for GIFs only for
  quick drafts, many variations, or when the user wants faster output.
  When "animated" or "moving" means a short simple loop, make a GIF; use a video model for real
  motion or longer clips.
  Keep the defaults (9 frames, 200 ms per frame) unless the user asks: `num_frames: 9`, `frame_duration_ms: 200`.
  These defaults are fine; change frames or speed only when the user asks for a longer, smoother,
  or faster loop, within the frame and per-frame limits `list_models` reports. Cost scales with frame count.
  Choose between Flare and Sunburst by speed and detail, not by cost.
  `image_size` is per frame and all frames share the pixel budget; check `list_models` for size limits.
  Keep the downloaded `.gif` as an animated image asset; do not flatten it to a PNG.
- Edit accepts up to 16 `images`, plus either `mask` (white edits, black
  preserves) or `markup_image` (a transparent annotation PNG matching the first
  image's dimensions), never both. Put these fields in the operation's settings.
- Transparent backgrounds use `background: "transparent"`. Cost depends on tokens;
  the initial hold may be below the final charge, which uses the actual generation cost.
