---
name: make-an-ad
description: Create an image or video ad for the user's brand with Hermoso. Use when the user asks to make, design or render an ad, a social post visual, a video ad, cut-ins of their own screens over a video, a longer version of a clip, or variations of an ad they already have. A UGC video with a person on camera, a product photoshoot, and a remake of an ad they like each have their own skill.
---

# Make an ad

Use this skill to turn a request like "make an Instagram ad for our summer sale" into a finished file in the
user's Hermoso Library. Explicit instructions from the user always take priority over this skill: their format,
size, length, wording, product and style choices win over any default below.

## Before you start
- Hermoso reads the saved brand profile (products, logo, colours, voice) by itself. Call `get_brand` only if you
  do not yet know whether a brand is saved. If none is saved, use the get-started skill first.
- You need to know: image or video, and where it will run (for example an Instagram feed post is square, a Reel
  or TikTok is vertical 9:16). If the user did not say and it matters, ask one short question. If they say "you
  choose", pick and say what you picked.

## Choose the route
- **An image ad** (a feed post, a banner, a product visual): call `generate_image` with a clear prompt that names
  the product, the scene, the offer and the text to show, plus `aspectRatio` (1:1 square, 4:5 portrait, 9:16
  vertical, 16:9 landscape).
- **A video ad**: call `plan_ad` with the product, format and, if the user named one, the length in seconds. Show
  the user the concept and script in a few lines. When they are happy (or asked you not to check), call
  `render_ad` with the plan's full output as `creative`. Pass the length the user asked for; never shorten it.
- **A quick short video from a description** (no script needed): `generate_video` with a prompt, `aspectRatio` and
  `durationSeconds`.
- **A simple native format** (for example a photo slideshow or a text-led post): `make_template_ad`.
- **Copy the structure of an ad they like, for their brand**: for a video link (TikTok, Reel, Facebook, X, YouTube)
  call `plan_video_remake`, then `render_ad` with the creative it returns. For a static image ad call `clone_static` with
  the image URL. The result keeps the structure and pacing and uses the user's own product and words, never the
  original brand's.
- **Cut-ins of the user's own screens** (an app, a web page, a dashboard, a review or a chart shown for a beat as a
  card while the footage keeps playing): pass the pictures as `inserts` to `plan_ad` and `render_ad`. Keep them few
  and short, on the line that talks about them. A photo is not laid over the video.
- **A longer version of a clip**: `generate_video` with `extend` set to true, the clip as `refVideo`, and a prompt for
  what happens next. By default it cuts to a new shot of the same scene rather than stretching the old one.
- **Variations of an ad they already have**: different headlines on a static ad with `headline_variants`, new
  opening hooks on a video with `hook_variants`, or more versions of a winning ad with `multiply_ad`. For a small
  change to an image (swap the background, fix a word) use `edit_image`.

For the opening of a video, the hook mechanics in `references/hooks.md` help you pick one that fits the product.
Read it when you are writing or choosing a hook.

## Long renders
Video renders usually take a few minutes. When a tool returns a job id instead of a file, call `get_job` with that
id until it reports done or error. Several checks are normal; do not start the render again, because that would
charge twice. If the user asks later where a render went, `list_jobs` and `list_library` show recent jobs and
finished files.

## Files from the user
If the user wants to use their own photo or video, and gives you a public link, `upload_file` turns it into a URL
the other tools accept.

## Saving the file
Finished files are in the user's Hermoso Library already. If they want a copy in Google Drive, `save_to_drive` saves
it (with `folder` when they name one). It needs Google Drive connected in the Hermoso workspace.

## Output
Show the finished image or video (the Hermoso card displays it) with one line on what it is, and offer one useful
next step: a variation, a different size, or scheduling it (the schedule-posts skill).

## Do not
- Do not add prices, discounts, ratings, awards or claims the user or the saved brand did not state.
- Do not write health, medical, financial or other claims the product cannot back up (for example "cures" a
  disease). Offer an honest alternative instead.
- Do not add an end card, captions or music unless the user asks for them.
- Do not use another company's logo, trademark or a real person's likeness without the user confirming they have
  the rights.
- Creating ads uses credits from the user's Hermoso account, and each paid reply says what it charged: pass that on
  in one line rather than estimating it. Make what the user asked for; do not render extra versions they did not
  ask for.
