---
name: ai-skeleton
description: Make an AI skeleton video with Crealix, where a glass skeleton lives through a "what if" or survival scenario, shot by shot, with narration. Use when the user asks for a skeleton video, a what-if or "how long could you survive" scenario, or "what happens to your body if…".
---

# AI skeleton

A photoreal glass skeleton goes through an escalating scenario (fall into the
sun, go a week without sleep, live on Mars) while a narrator speaks to the viewer
in the second person. Every sentence becomes one short animated shot of the
skeleton.

## 1. Read the guide

Call `get_creation_guide('ai_skeleton', durationSec, language)`. It gives the exact
script format with its word budget for this length and language, the allowed
lengths, the format templates, the skeleton variants and the price.

## 2. Write the script (hybrid)

Follow the guide's format exactly:
- A one-sentence curiosity hook: "What if you fell into the sun?"
- Four to six escalating periods. Each starts with a short header line on its
  own ("Minute 1", "Day 30", "Level 3"). Headers show on screen and are never
  spoken.
- Under each header, two to four short sentences, one per line. Each sentence is
  something that happens TO the skeleton with a visible result ("Your bones
  glow orange through your chest"), never a pose or a feeling.
- Escalate: every period is worse, stranger or bigger than the one before.
- Close with one punchline sentence.

Keep the science plausible and the tone vivid. Nothing gory beyond what the
scenario needs.

Use crealix mode only when the user wants Crealix to write it, or picks a format
template (`formatTemplateSlug`) and wants its take on it.

## 3. Cast it

- `options.formatTemplateSlug`: the template that matches the scenario, if one
  does.
- `options.characterVariantSlug` or `characterCustomization`: the skeleton's look,
  when the scenario calls for it (a suit on Mars, armour in a battle).
- Narrator voice and delivery from the cast, suited to this script's energy.
- Captions and music from the cast. `cover` for short-form.
- `options.qualityTier`: NORMAL unless the user wants higher quality; say what it
  costs.
- A saved character (`characterIds`) only when the user wants their own
  character in it.

## 4. Propose, create, finish

`check_plan` until it is valid (the guide snaps the length to the ones this
format makes), then one `validate_plan` with two or three lines of why. On a yes,
`create_video` with the `proposalId`. Follow it with `get_status` and say in one line
when the draft is ready.

After that, follow the edit-video skill. `edit_video` changes the title,
captions, music and mix, and what a scene shows (an image or clip in Crealix).
The narrator stays the one chosen at creation, so choose it well. Render only
when they ask.
