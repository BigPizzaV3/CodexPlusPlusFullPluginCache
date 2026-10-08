---
name: drama-casting
description: Cast Namsiang Thai voices for drama by character gender, age, role, and personality; direct Gemini performances line by line; prepare auditions; and generate only confirmed clips through the Namsiang remote MCP.
---

# Namsiang drama casting and performance direction

Use this workflow whenever the user asks to cast Thai voices, audition characters, generate dialogue, or retrieve generated audio through Namsiang.

## Casting workflow

1. Read the supplied script by scene and dramatic beat. Extract one stable brief per character: role, stated gender and age, relationship to other characters, social position, personality, warmth, authority, energy, emotional range, and any hard exclusions. If the script does not establish a trait, label it as an assumption instead of presenting it as fact.
2. Call `get_voice_service_status`, then `list_thai_voices` with `ready_only: true`. Use only voices returned by the live catalog. Never invent a voice, provider voice ID, or capability.
3. Filter candidates by readiness, locale, usage rights, output needs, stated gender, and plausible age range. Then rank by role, personality, vocal weight, energy, warmth, authority, and dramatic range. Never infer gender or age from a voice name; use catalog metadata.
4. Recommend at most three contrasting logical voices per character. Explain the match and tradeoff from catalog metadata. Do not declare a winner when the evidence is weak; propose an audition.
5. Audition identity and acting separately. For each candidate, use short clips covering a neutral identity line, a restrained/subtext line, and an emotional peak when the role needs that range. Each clip must have one primary emotional objective.
6. Ask the user or studio to choose. Do not silently replace a selected actor, even when another engine is available.
7. Lock one logical `voice_id` to each `project_id` + `character_id` for the episode or project. Keep the same ID and model across lines and takes unless the user explicitly approves a recast.
8. Build the performance plan described below before synthesis. Do not generate until the user confirms the exact voice IDs, exact dialogue, per-line direction, formats, and expected number of paid generations.
9. After confirmation, call `create_thai_speech` once per clip. Use stable `content_id` and `idempotency_key` values so retries do not spend credits twice.
10. Use `get_speech_job` for status and `download_speech_audio` only when the job succeeds.

## Per-line performance plan

Create one director-sheet row per spoken clip before calling the write tool. Include:

- `scene`: immediate place, time, stakes, and who is present.
- `audio_profile`: the locked character identity plus current physical state; do not change age or persona between lines.
- `emotion`: one supported primary emotion. Treat it as a broad control, not the complete performance.
- `style`: speaking intention, relationship, subtext, restraint or intensity, emphasis, and how the line should land.
- `pace`: rhythm, hesitation, breath, acceleration, and meaningful pauses in natural language.
- `sample_context`: the preceding line or event and what the character is reacting to. Keep it concise and never place it in `text`.
- `performance_prompt`: any remaining Gemini direction, including a short emotional arc and explicit negative direction such as “กลั้นน้ำตา ไม่สะอื้น ไม่ตะโกน”.

The exact authored dialogue goes only in `text`. For Gemini use the structured `performance` fields plus `performance_prompt`, because a detailed acting objective is more useful than an emotion label alone. Keep `accent: "Neutral Thai"` unless the role explicitly requires another accent, and keep temperature at 0.7 for continuity unless the user requests exploratory alternate takes.

## Generation rules

- Treat `create_thai_speech` as a paid write action. Always obtain confirmation immediately before the first generation in a batch.
- Preserve authored Thai dialogue exactly. Put performance intent in `emotion`, the Gemini performance fields, pace, volume, pitch, and pause controls rather than rewriting words or inserting stage directions into speech.
- Use `⏸0.1` or `▮0.1` only for a deliberate authored pause. Ordinary spaces are not timing controls.
- Do not claim that every voice expresses every emotion equally well. Recommend an audition when performance range is uncertain.
- Never reveal or request Cartesia, MiniMax, or Gemini keys or provider-specific voice IDs. The MCP accepts logical voice IDs only.
- Prefer a ready Gemini logical voice when the scene needs nuanced acting and the audition supports the casting choice; do not choose it solely from the provider name.
- For Gemini drama, send both the applicable structured `performance` fields and a concise `performance_prompt`. Set `fallback_policy` to `forbid` so a character never changes engine silently.
- When the same line needs alternatives, change one acting variable at a time and label takes clearly. Do not use temperature as a substitute for direction.
- Never substitute a public or fallback voice without naming the change and receiving approval.

## Recommended user-facing result

Present two compact tables before generation:

1. Casting: character, gender/age/role brief, candidate logical voice IDs, reason/tradeoff, and lock status.
2. Director sheet: clip ID, exact dialogue, locked voice, primary emotion, subtext/intention, pace, and confirmation status.

State exactly which choices still require the studio's decision and the number of paid clips that confirmation will create. After generation, report each `job_id`, status, engine returned by the service, and whether the request was an idempotent replay.
