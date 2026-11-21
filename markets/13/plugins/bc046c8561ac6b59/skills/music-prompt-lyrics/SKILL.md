---
name: music-prompt-lyrics
description: Create complete music-generation prompts and original lyrics for a user's song idea, with optional save to the WizPrompt library when tools are available.
---

Use this skill when the user wants a song prompt, Suno-ready style direction, original lyrics, or a complete song draft.

Before writing, infer a strong musical direction from the user's idea unless a missing fact would change ownership, safety, or storage. Do not ask for tempo, key, mood, or vocal style just because the user omitted them.

Follow the shared template in `../../references/output-templates.md`.

Workflow:

1. Call `begin_song` with the idea, known project, optional model and user-confirmed available controls. Use the returned guidance and editorial rubric. If this tool is unavailable, fall back to `get_studio_guidance` with `workflow: "song"` and disclose unavailable saved context.
2. Apply current explicit instructions and approved project direction before confirmed personal defaults. `begin_song` loads owned project context; use `get_creative_context` separately only when more context is needed. Never infer permanent preferences from feedback.
3. Draft the song in chat first. Include `Title`, `Style`, `Lyrics` or clear instrumental direction, `Exclusions`, `Settings`, and optional `Studio Notes`.
4. Keep the style prompt separate from lyrics. The style prompt should describe genre, mood, tempo, key, vocal character or instrumental focus, instrumentation, production texture, and mix feel.
5. Do not put real artist names, song titles, copyrighted lyrics, or conversational instructions inside the final style prompt.
6. Use bracketed section tags inside the lyrics where they help generation, such as `[Intro]`, `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Outro]`, and `[End]`.
7. Review hook strength, natural phrasing, breath room, section progression, cliche control, musical coherence and genre fit. Fix weak areas, then call `prepare_song` with the song and structured `editorial_review`, using all seven distinct assessments for status `completed` and `audio_evaluated: false`. Present separate copy fields and unresolved findings. Preliminary text checks and completed host review do not prove audio quality.
8. If the user asks to save the result, or the active workflow clearly includes saving, use `save_prompt` only after `prepare_song` succeeds or returns only non-blocking warnings. Include `studio_metadata` with model, exclusions, settings, instrumental state, guidance version, and studio notes when those fields exist. Include an `idempotency_key` for create/save retries. If project selection is needed, use library/project tools to identify the target first.
9. Confirm saved only after the save tool returns success. If save tools are unavailable or fail, use the save failure template and preserve the draft in the chat.

Quality checks:

- The title is original and specific.
- The style prompt starts with the strongest genre and mood signals.
- The lyrics use one central metaphor or clear narrative frame.
- Instrumental packages use arrangement cues instead of full vocal lyrics.
- Exclusions resolve unwanted bleed without contradicting the style prompt.
- The output avoids unsupported promises about commercial performance.
- Any save confirmation includes the stable ID returned by the tool.

For result complaints, call `plan_song_revision` with the user-reported issue and explicit preserved elements. Confirm which Suno operations are available before suggesting a paid or model-specific editor. Draft only the targeted changes, rerun editorial review and prepare_song, then save a linked revision only when asked. Do not generate audio or spend Suno credits.
