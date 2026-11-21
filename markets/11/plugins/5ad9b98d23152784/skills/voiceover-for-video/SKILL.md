---
name: voiceover-for-video
description: "For generating narration from agreed words, use the exact spoken text and current model voice controls to separate speech content from delivery settings. Not needed for writing or editing the script itself."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Voiceover for video

Follow the confirmed contract of the chosen model. Keep the creative task separate from the
exact text to be spoken, and use only the declared delivery parameters.

## Text to be spoken

Put the exact approved spoken words into `input.prompt`. Preserve wording, numbers,
abbreviations, names and pauses. Use inline audio tags only when the model's current prompting
guidance supports them and the user included or requested that delivery.

## Delivery

Read `givon_get_model_schema` for the chosen voiceover model. List voices through
`givon_list_voices` (CLI: `givon voice list`) and pass the chosen id as `input.voice`.
Use only delivery controls exposed as flat properties in that schema, with their declared
values and defaults. Do not assume a project-default voice or copy fields from an internal
chat contract. Keep delivery instructions separate from words that should actually be spoken.
Quote this exact input and continue through `givon-ai-create` after approval.
