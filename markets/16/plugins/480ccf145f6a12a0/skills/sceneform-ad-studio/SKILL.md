---
name: sceneform-ad-studio
description: Create static ads, UGC and creator-style video ads with hooks, carousels, and new headlines, sizes, languages, or Reshoots of finished ads in Sceneform. Use when the user asks for an ad, ad creative, UGC or creator video for a brand or product, product promotion, campaign, A/B variants, or a swipeable post. NOT for a plain image or clip without an ad brief (sceneform-generate) or animated text and graphics (sceneform-motion).
license: MIT
metadata:
  author: sceneform
  version: "0.11.0"
---

# Ads and carousels

The ad tools write the detailed visual direction themselves. Your job is the
strategy they cannot invent: the brand facts, the angle, the audience, the
offer, and a concept sharp enough that the ad says one thing well. Read a
reference file by calling `load_skill` with this skill's name and the file's
`path`, or open it when this skill is installed locally.

## Steps

### 1. Ground the brand

Call `list_brand_kits`. Use a `ready` kit and its `product_ref` when the ad
sells one product; a product already carries its brand.

- No kit for the brand or product yet: load sceneform-brand and follow its
  build steps, then come back here.
- A kit still `building` is not ready, and the ad is still owed: wait for it
  with `get_brand_kit` and `timeout_seconds: 40`, up to three calls in a row
  while it is `building`. Once it is `ready`, go on to step 2 in the same
  turn. If it is still `building` after the third call, say it is on its
  way and stop.
- A ready kit whose products are still `importing` can make the ad now:
  pass its `brand_kit_ref` without a `product_ref`. Only an ad about one
  named product waits for that product. With a card, say the product is on
  its way and stop; otherwise check `get_brand_kit` on a later turn. A
  `failed` product can be imported again with `add_product`. An ad made from
  an unread brand or product comes out generic.
- No kit and no link: the concept carries every fact, and you offer to build
  a kit for the next ads.

Done when the ad has a ready kit or product, or the user chose to go without
one.

### 2. Choose format, count, and sizes

- Static image ad: `generate_static_ad`. A UGC or creator video, or any
  video ad: `generate_video_ad`, which picks the model and writes the
  script and shots itself. Swipeable post with a caption:
  `generate_carousel`.
- One ad unless the user asks for more. "A few", "some options", or "to
  test" means three to five concepts, each on a different angle.
- Static ad sizes: 4:5 for Instagram and Facebook feeds (the default), 9:16
  for Stories and Reels, 1:1 for LinkedIn and square placements, 16:9 for
  YouTube and the web. New sizes of a finished ad are variants, not new ads.
- Video ads run 4 to 30 seconds; 15 is the default and suits most feeds.
  They are 9:16 at 720p unless the user asks for another `aspect_ratio` or
  `resolution`. `ad_type` picks the style (UGC by default; unboxing, ASMR,
  TV spot, product showcase, tutorial, Japanese TV ad); only UGC, unboxing,
  ASMR, and tutorial take a hook or setting.
- Static ads and their variants render at 1K unless the user asks for 2K
  or 4K in `resolution`.

Done when you know each ad's tool, angle, and size.

### 3. Write the concept

Read [references/concepts.md](references/concepts.md) and write each
`concept` from its template: one angle, the audience, the message, the
proof, the offer, and the call to action, at most 1,200 characters. For a
video ad add a `setting_brief`: one line naming the place or situation.

Done when each concept passes the checklist in that file.

### 4. Pick the template, hook, or recipe

Read the matching catalog: `list_ad_templates` for static layouts,
`list_ad_hooks` for video openings, `list_carousel_recipes` for carousel
styles. Pick the one whose description fits the angle, and pass its id as
`template_id`, `hook_id`, or `recipe_id`. Leave it out to let the tool pick.

- A person in the ad: a ready `persona_ref` from `list_personas` in
  `reference_refs` (up to 3 images for static, 10 for video), chosen by the
  casting rules in the concepts file. The product stays in `product_ref`.
- An `element_ref` from `list_elements` or an image `asset_ref` also goes in
  `reference_refs`. A carousel takes a `persona_ref` as a recurring
  character. For a new reusable AI influencer, use sceneform-brand first.

### 5. Generate

`generate_static_ad` and `generate_video_ad` take `requests`, a list with one
request per concept: one ad is one request, several ads are one call with
several. Static and video ads are separate calls. Pass `project_ref` or
`folder_ref` in each request to file them.

### 6. Follow and check

An ad returns an `operation_ref`. With `card_offered: true` the host was
given a card that tracks it: say it is on its way and stop. Otherwise, or
when the user asks for it or cannot see the card, call `wait_operations`. A
carousel returns a `carousel_ref` and `maximum_credits`, the cap (unused
credits are refunded); the card follows it, or `get_carousel` reports its
status, caption, and slides.

When a later step needs the result (a finished ad as the source for
variants), wait for it and carry on. Before calling an ad good, run
`analyze_media` on it: is the headline legible and spelled right, does the
product match, does the first second of a video hook? Report what you
checked.

### 7. Change a finished ad

New headlines, sizes, or languages, and Reshoots of video ads: read
[references/changes.md](references/changes.md).

## Spending

Ads start at once and charge the credits they return. Pass
`quote_only: true` when the user asks what something costs, and on every
spend call for the rest of the conversation once they ask you to check
first. Give a quote's summary and credits in one sentence and call
`confirm_actions` with its `action_ref` only after the user says yes; with
`card_offered: true` the host was also given a card with Generate (or
Approve) and Skip, so say they can approve there. A quote with `shortfall` cannot start yet: relay why and stop. In a
batch, retry only the ad that failed with `retryable: true`, with its own
tool; resubmitting the batch charges every ad again. A call that timed out
may have started: find it with `list_operations` before anything else.

From the CLI, read [references/cli.md](references/cli.md).
