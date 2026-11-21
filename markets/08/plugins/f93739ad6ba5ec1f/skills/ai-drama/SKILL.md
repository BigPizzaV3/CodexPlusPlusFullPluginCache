---
name: ai-drama
description: Make an AI drama with Crealix, a viral micro soap opera starring bright 3D cartoon characters with fruit or object heads on human bodies, with dialogue and twists. Use when the user asks for an AI drama, a fruit drama or love island, a mini telenovela, or a short dramatic story with talking characters.
---

# AI drama

A micro soap opera in one-minute bites: two or three characters, each a glossy
3D cartoon humanoid with a fruit, food or object for a head, act out a story
full of betrayal, love and twists. You write the scenes and the dialogue;
Crealix casts the characters with locked voices and makes each clip.

## 1. Read the guide

Call `get_creation_guide('ai_drama', durationSec, language)`: the exact script
format with the number of scenes for this length, the allowed lengths and
languages, the niches and worlds catalogs, and the price. Characters speak with
their own voices, so there is no narrator to choose.

## 2. Write it (hybrid)

Follow the format: at least three scenes, each headed `SCENE N:` on its own line,
then one line of what we see, then the dialogue as `NAME: "line"`.

- The characters are humanoid: a full cartoon body that walks, gestures and
  dresses like a person, with the object as the head ("a pineapple bride in a
  white gown"). Never a bare object with a face.
- Scene 1 opens on the line or the action, in the first second. No slow build.
- Every scene has real action: someone walks in, turns away, slams a door,
  storms off, laughs. Never two heads talking still.
- Each scene's dialogue is a real turn: a threat, a confession, a condition.
  One or two lines, fast, and a reaction to land it.
- Build to a twist near the end and close on a punchy line.
- Name each character once and keep the names consistent.

Use crealix mode when the user wants Crealix to write it, or only picks a niche.

## 3. Choose the options

From the guide's catalogs, choose what suits this story:
- `options.nicheId` (the kind of drama) and `options.domainId` (its world), or
  `options.customNicheText` for a niche of the user's own.
- `options.useViralHook` for a stronger cold open.
- Captions and music from the cast. `cover` for short-form.
- `options.qualityTier`: NORMAL unless the user wants more; say what it costs.

## 4. Propose, create, finish

`check_plan` until it is valid, one `validate_plan` with two or three lines of why,
and `create_video` with the `proposalId` on a yes in the chat. Follow it quietly
with `get_status`.

Afterwards, `edit_video` changes the title, captions, music and mix. Scenes are
reworked in the Crealix editor: share its link. Render only when they ask.
