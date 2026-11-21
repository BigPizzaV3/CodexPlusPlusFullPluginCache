---
name: talking-objects
description: Make a talking objects video with Crealix, where everyday objects with faces talk in a short comic scene, lip-synced. Use when the user asks for talking objects, food or products that talk, or a funny dialogue between things.
---

# Talking objects

Everyday objects come alive and talk to each other in a short comic scene. You
write who speaks and what they say; Crealix designs each object with a face,
gives it a voice and animates it lip-synced, one line per scene.

## 1. Read the guide

Call `get_creation_guide('talking_objects', durationSec, language)`: the exact
format and word budget per line, the allowed lengths, the moods and presets, and
the price. The objects speak with their own voices, so there is no narrator to
choose.

## 2. Write the dialogue (hybrid)

- One line per scene, written `OBJECT: "line"`. The object's name is what gets
  drawn, so name it plainly (TOASTER, COFFEE MUG, OLD SNEAKER).
- Each line stays under the guide's word cap, about 20 words. One joke per line.
- Two or three objects, each with a clear personality that shows in how it
  talks: the smug one, the anxious one, the one who has seen too much.
- Open with the funniest or most surprising line. End on a payoff or a
  comeback.
- The objects should belong together (a kitchen, a desk, a gym bag), so the
  scene reads at a glance.

Use crealix mode when the user wants Crealix to write it from an idea.

## 3. Choose the options

From the guide's catalogs, choose what suits this dialogue:
- `options.moodId`: the tone of the scene.
- `options.presetSlug` or `categoryAngle`: a ready-made angle when the idea
  matches one.
- `options.enableSfxLayer` for sound effects under the dialogue.
- Captions and music from the cast, `cover` for short-form.
- `options.qualityTier`: NORMAL unless the user wants more; say what it costs.

## 4. Propose, create, finish

`check_plan` until it is valid, one `validate_plan` with two or three lines of why,
then `create_video` with the `proposalId` on a yes in the chat. Follow it with
`get_status`.

Afterwards, `edit_video` changes the title, captions, music and mix. The scenes
themselves are reworked in the Crealix editor: share the editor link, never
open it for the user. Render only when they ask.
