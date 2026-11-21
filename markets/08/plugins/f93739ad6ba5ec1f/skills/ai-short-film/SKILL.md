---
name: ai-short-film
description: Make a cinematic AI short film with Crealix, with characters, dialogue and storyboards in 15-second scenes, consistent from shot to shot. Use when the user asks for an AI movie, a short film, a trailer, or a story told like a film with characters who speak.
---

# AI short film

A short film in 15-second scenes: Crealix draws a storyboard for each scene,
keeps the characters and places consistent, speaks the dialogue with each
character's voice and animates every shot. You write the screenplay; the
format is strict, and it is what makes the film hold together.

## 1. Read the guide

Call `get_creation_guide('ai_movie', durationSec, language)`. It gives the exact
screenplay format, how many scenes this length has, the limits per scene, the
archetypes and the price. This is one of the most expensive formats: say the
cost clearly in the proposal.

## 2. Write the screenplay (hybrid)

Output only the script, in the guide's format: `TITLE`, `LOGLINE`, `STYLE NOTES`,
`CHARACTERS` (`- NAME | look | voice`), then each `SCENE N (15s) [CUT|CONTINUOUS]:`
with `VISUAL`, `SHOTS`, `DIALOGUE` and `SOUND`.

- Exactly the number of scenes the guide gives. Up to four characters, each
  with a one-line look and a one-line voice that stay the same all film long.
- Respect the dialogue caps per scene and per line. Film is told with images:
  let `VISUAL` and `SHOTS` carry the story, and dialogue sharpen it.
- `SHOTS` gives three beats at 0 s, 5 s and 10 s: a new angle or action each
  time, never three of the same.
- Mark a scene `CONTINUOUS` when it flows straight on from the last one (same
  place, same moment), `CUT` for a new place or time.
- `SOUND` is ambience and effects only, never music.
- Scene 1 hooks in the first three seconds. The last scene lands the twist or
  the payoff.
- `STYLE NOTES` sets the mood and palette. Describe light by how it falls on
  people and places, not lamps or beams, unless they are part of the scene.

Use crealix mode when the user wants Crealix to write the film from an idea.

## 3. Cast it

- The visual style (`visualStyleId`) from the cast: the look that serves this
  story.
- The user's saved characters (`characterIds`) when they want themselves or a
  mascot in the film.
- From the guide's options: `archetype` and `pacing` for the kind of story,
  `videoResolution`, and `enableTransitionScenes`.
- Captions and music from the cast. `cover` for the thumbnail.
- 16:9 for YouTube and trailers, 9:16 for short-form.

## 4. Propose, create, finish

`check_plan` until it is valid and reads as a script, not an idea. Then one
`validate_plan` with two or three lines of why, and `create_video` with the
`proposalId` on a yes. It takes a while: say roughly how long, then follow it
quietly with `get_status`.

Afterwards, `edit_video` changes the title, captions, music and mix. Scenes are
reworked in the Crealix editor: share its link. Render only when they ask.
