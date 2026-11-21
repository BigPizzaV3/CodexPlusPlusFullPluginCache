---
name: faceless-video
description: Make a narrated faceless video with Crealix, illustrated scene by scene with AI images, from a topic, an idea or the user's script. Use for explainers, facts, history, true or scary stories, motivation and top lists, on TikTok, Reels, Shorts or YouTube (up to 20 min), including a scene-by-scene storyboard.
---

# Faceless video

A narrator tells the story while every sentence becomes an AI image in one visual
style, with captions and music. The user never appears on camera. You write the
words and cast it; Crealix plans the scenes and makes the images, voice and
captions.

## 1. Pick how to plan it

Call `get_creation_guide('faceless', durationSec, language)` first. It returns the
narration budget for this length and voice, the three modes, prices and the cast.

- **hybrid** (default): you write the narration; Crealix splits it into scenes and
  writes each image prompt for the chosen style.
- **agent**: you write every scene yourself (the line and what the frame shows).
  Use it when the user wants to control or approve each scene, or brings a
  storyboard. Follow [references/storyboard.md](references/storyboard.md).
- **crealix**: Crealix writes it from an idea or a catalog topic. Only when the
  user asks for a surprise or for Crealix to write it.

If the user already wrote a script, use it as written in hybrid mode. Tell them
if it is far over the budget for the length they want, and offer a longer
video or a trimmed version you write.

## 2. Write the narration

Stay within the guide's `maxChars` for the length. The script's length sets the
video's length.

- The first sentence is the hook, spoken in the first two seconds: a claim, a
  question or stakes. No greetings, no "in this video", no title card.
- One idea per sentence. Each sentence becomes a picture, so make it concrete
  and visible: who, what, where. Avoid runs of abstract sentences.
- Keep lines short and punchy. Keep a question open and escalate. Every few
  sentences, pay something off.
- End on a twist, a punchline or a line that loops back to the hook. Add a call
  to action only if it fits the voice of the video.
- Plain text only: no scene markers, headings, stage directions, emojis or
  hashtags. Write numbers and names the way the narrator should say them.
- Facts about real people, events or numbers: only what you know is true. When
  unsure, say less.

## 3. Cast it

Read the whole cast and choose what suits this video: its topic, tone, audience,
pacing and platform. There is no default answer for a kind of video.

- Voice: tone and gender that fit the narrator of this story. Adapt
  `voiceSettings` from `voiceDelivery` to the pacing you wrote.
- Visual style: each style says how it looks and which topics it does not suit.
  Never pick one marked as unsuitable for this topic.
- Captions: readable on a phone with the sound off. Music: the mood of the story,
  under the voice.
- `imageTier`: BASIC unless the user wants sharper images; say what PRO costs.
- A recurring mascot or person the user saved (`browse_catalog('characters')`):
  pass `characterIds`. To make a new one, use `create_character` first.
- `cover`: a 3–6 word headline in a cover style. `voiceEffect` only when the
  story needs it.
- Aspect ratio: 9:16 for TikTok, Reels and Shorts; 16:9 for YouTube.

## 4. Propose and create

Use `check_plan` until the plan is valid, fits the length and nothing important is
left to generic defaults. Then show it once with `validate_plan` and recommend it in
two or three lines: what you chose and why it suits this video. On a yes in the
chat, call `create_video` with the same fields and the `proposalId`. If they pressed
Create on the card, it is already being made.

## 5. After it is made

- Follow it quietly with `get_status`. When it is ready, say so in one line; the
  card plays the draft.
- Changes: follow the edit-video skill. New images with `generate_scene_media`;
  clips with `animate_scenes` (the price comes first and the user approves it).
- The final MP4 only when they ask: the card's Render button, or `render_project`.
