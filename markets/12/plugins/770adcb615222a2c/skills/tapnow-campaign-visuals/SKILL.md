---
name: tapnow-campaign-visuals
description: Plan and produce campaign visuals with TapNow - a key visual first, then every placement it needs (poster, banner, social post, story, slide), or a matching series of visuals from a list of themes. Use when the user wants an ad, a poster, a key visual, social or banner creatives, a campaign set, or one visual in several sizes.
---

# Campaign visuals

Three kinds of request, three paths:

| The user wants | Path |
| --- | --- |
| One key visual, poster, cover or banner | Brief, then key visual (steps 1–2) |
| The same visual in several placements | Key visual first, then adapt it (steps 1–3) |
| A series that shares one look: product benefits, an event series, brochure pages | A matching series (steps 1 and 4) |

The tools list their models, formats and options in their descriptions. Read them there each time instead of assuming them.

## 1. Brief

Ask once, in one short message, for whatever the user has not said:

- The goal, and the single message the visual has to carry.
- Where it will run. The placements decide the shapes.
- Brand material to match: logo, product photo, a past campaign, brand colors.

Bring brand images in with `upload_image`, or find them in the user's library with `find_library_assets`. Each image parameter's description says which IDs it accepts; when one does not take a library `file/<file_id>`, bring that image in with `upload_image` first.

## 2. Key visual

- Start with the shape of the most important placement.
- Write one specific prompt: subject, setting, light, palette, mood, composition, and where empty space for the copy goes.
- Lock the brand look in words. Name the brand colors (by name or hex) and describe the style as two to four adjectives plus one comparison, for example "clean, warm, editorial, like a premium kitchenware catalog". Reuse the exact same wording for everything in the campaign.
- Pass the logo, product photo or past campaign to `create_image` as reference images so the visual stays on brand.
- Keep headlines, prices and buttons out of the image by default and leave room for them; the user adds the copy in their design tool. If they want text rendered in the image, choose a model that the tool description says handles text and layout well, and keep the text short.
- When the user wants options, ask for a few candidates in one call and let them pick. The chosen image is the key visual from then on.

## 3. Adapt it to each placement

| Need | Do this |
| --- | --- |
| Same picture, different frame | `resize_for_platform` with the key visual. It crops without generating anything new. Where a panel can be shown, the user picks formats and adjusts the framing there; otherwise confirm the list of formats in text. |
| A very different shape, or the crop would cut into the subject | `create_image` with the key visual as the reference. Prompt: recompose for the new shape, keep subject, palette, light and style. |
| A version with the real product in it | `create_image` with the key visual and the product photo as references. |

The original stays as it is; every adaptation is a new image. Start the adaptations that do not depend on each other one after another, then collect them with `get_production_result`.

## 4. A matching series

1. Agree on the list of themes first, one image per theme, and say how many images that is before you start.
2. Call `create_deck_visuals` with the themes, the style wording, the brand color, and the key visual or a past campaign image as the style reference. The reference gives the strongest consistency.
3. Images in a series contain no text; space is left for copy.
4. To fix one image, do not rerun the set. Call `create_image` for that theme with the same style wording and one finished image from the set as the reference.

## Deliver

List each image with its placement and format, give the TapNow project link, and offer `save_to_library` into a folder named after the campaign so the set is easy to find later.
