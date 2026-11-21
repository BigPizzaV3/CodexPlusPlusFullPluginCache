---
name: stock-footage-video
description: Make a narrated video with Crealix over real stock footage, a clip for every sentence, from a topic or the user's script. Use when the user wants real footage instead of AI images, for travel, finance, business, health, news-style explainers or motivation. Also swaps clips afterwards.
---

# Stock footage video

A narrator reads the script while real stock clips play under it, each one
matched to its sentence, with captions and music. Every sentence becomes a
footage search, so the writing decides what the viewer sees.

## 1. Read the guide

Call `get_creation_guide('stock', durationSec, language)`: the words budget for
this length, the cast (voices, captions, music) and the price. Stock footage is
included; the user pays for the narration and, later, the render.

## 2. Write for footage

- About 2.5 words per second (the guide gives the figure). Use hybrid mode and
  write it yourself. Use crealix mode only when the user asks Crealix to write it.
- Hook in the first sentence. No greetings.
- One idea per sentence, and each sentence describes something a camera could
  film: people doing things, places, objects, weather, cities, nature.
  "A trader stares at red numbers on six screens" finds footage; "the market
  is uncertain" does not.
- Keep abstract lines rare and next to concrete ones, so the footage still makes
  sense.
- Plain text, no headings or stage directions. The words are read as written.
- Facts, figures and claims: only what you know is true.

## 3. Cast it

Choose from the cast what suits this video: its topic, tone, audience and
platform.
- Voice and delivery (`voiceSettings` adapted from `voiceDelivery`).
- Captions and music under the voice.
- `cover` for short-form, and `voiceEffect` only when it serves the story.
- 9:16 for TikTok, Reels and Shorts; 16:9 for YouTube; 1:1 when asked.

## 4. Propose and create

`check_plan` until it is valid and fits the length, then one `validate_plan`, with
two or three lines on why your choices suit this video. On a yes in the chat,
`create_video` with the `proposalId`. A press on the card's Create button has
already created it.

## 5. Improve the footage

When it is ready (`get_status`), the card plays the draft. If a scene shows the
wrong thing:
1. `search_stock_media` with a concrete query for that line, at the video's shape.
2. `import_media_from_url` with the chosen clip's `videoUrl`.
3. `edit_video({ scenes })` to put the imported clip on that scene number.

`edit_video` also changes the title, captions, music and mix. The narrator stays
the one chosen at creation. Edits are free and `undo_last_change` reverses them.
Render only when they ask: the card's Render button, or `render_project`.
