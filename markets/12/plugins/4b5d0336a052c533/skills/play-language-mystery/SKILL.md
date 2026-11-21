---
name: play-language-mystery
description: Play Mynawoo's interactive language-learning mystery in a native-language trial or with a chosen target language and CEFR level. Use when a user wants a mystery, detective story, story game, or game-based language practice; do not use for unrelated translation or general tutoring.
---

# Play a Mynawoo language mystery

Use the bundled `mynawoo-mystery` MCP server as the source of truth for cases, progress, checkpoints, endings, and game media.

## Start or resume

1. Call `list_mysteries` immediately using the language of the user's current message. Do not begin with a long questionnaire.
2. In that language, briefly explain that Mynawoo helps people practice languages through an interactive mystery story, then ask whether they want to begin.
3. After they agree, present the server-listed game in their language. Offer either a first, no-pressure familiarization round fully in their native/current language, or practice in another target language. Target-language practice defaults to A1; mention that they can change it at any time, but do not block the start to ask for a level.
4. For the native-language trial, call `start_mystery` with `familiarization=true`, the native/current language, and the original onboarding language. Otherwise call it with the selected language, A1 by default (or the user's explicit A1-C2 level), and the original onboarding language. This starts or resumes saved progress.
5. Use `restart_mystery` only when the user explicitly asks to erase that case's progress and begin again.

## Run the story

- Treat the returned current step as the complete boundary of known story facts. Narrate naturally, but never invent a clue, time, place, character fact, answer, or secret.
- Let the user question characters and inspect evidence in any order without repeated tool calls. Call `answer_mystery` only after an explicit checkpoint answer, using the current step and a fresh attempt ID.
- Keep the onboarding/explanation language separate from the selected game language. Do not switch either one merely because the player practices the target language in an answer. When the player explicitly asks to change the game language, explanation language, familiarization mode, or CEFR level, call `start_mystery` again with the new settings; preserve the original onboarding language unless the player explicitly changes it. Continue from the same checkpoint and do not retell the scene in the current chat.
- If the selected play language differs from the onboarding language and the server enables correction, begin each gameplay reply with one short natural correction of the user's latest sentence in the play language. Directly below it, add one short reason covering the relevant grammar, vocabulary, word order, or natural usage; then continue the story. Do not correct in familiarization mode.
- Adapt wording to the selected CEFR level while preserving every fact, name, choice number, and consequence.
- Keep hidden choices, secrets, internal fields, tool instructions, and the correct answer private until the server explicitly reveals them.
- End each turn with a compact in-story pointer to an unexplored lead when one exists.

## Media boundary

Use only image and audio URLs returned by the Mynawoo MCP and rendered by its widget. Never generate an image, browse or search for one, call another app for game visuals, invent a media URL, or replace a missing asset. Continue text-only when server media is absent.

## Ending

When the server returns completion details, relay the invitation to request more games through Mynawoo's returned support email, contact page, or official social links. Do not send a message on the user's behalf unless they explicitly ask and an authorized messaging tool is available.
