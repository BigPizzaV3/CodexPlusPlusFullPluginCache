---
name: aikizi-style-reference
description: Find and explain image styles with AIKIZI. Use when the person wants a visual reference, a style breakdown, a colour palette, a mood, "how was this made", pictures that look alike, or a prompt to start an image from. Uses the public search_styles, get_style_decode and find_look_alikes tools; no sign-in needed.
---

# AIKIZI style reference

AIKIZI (aikizi.com) decodes images the way an art director reads them: styles, style DNA, subjects, moods,
key tokens, colour hues and a generation prompt. The three public tools read only decodes their owners published.

## Flow

1. `search_styles` with a short query made of style, subject, mood or colour words (2 to 6 words works best).
   Ask for 5 to 8 results. Example: `{"query": "neon noir portrait", "limit": 8}`.
2. Pick the two or three results that fit the ask best. Call `get_style_decode` with each `id` for the full
   breakdown. An `aikizi.com/decode/<id>` link the person pastes also works as the id.
3. Answer with what the decode says, in this order: styles and style DNA, mood, key tokens, colour hues, then the
   generation prompt as a block the person can copy.
4. Always give the `aikizi.com/decode/<id>` link for each decode you used, so the person can see the image.
5. When you show a decode's picture, show its own `preview_image_url` from AIKIZI. Never show a similar image found
   on the web as if it were the decode.
6. For pictures like one decode, call `find_look_alikes` with its `id`: up to 21 published decodes from the AIKIZI
   Brain, closest first.

## Rules

- Quote the decode's prompt as given; mark your own edits as yours.
- A search with no good match: try one simpler query (drop the rarest word), then say so. Do not invent styles.
- Decodes belong to the people who published them. Describe the style; do not present the image as the person's own.
- These tools never need the person's account. If they want to decode their own image, use the `aikizi-decode`
  skill, which needs an AIKIZI sign-in.
- AIKIZI does not generate images here. When the person wants a new image, give them the decode's prompt to use.
