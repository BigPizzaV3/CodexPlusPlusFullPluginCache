---
name: idea-ai-audio-production
description: "Create coordinated narration, music, and sound effects with idea.ai from a creative brief, with deliberate voice, timing, and cost choices."
---

# Audio production pack

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_audio` for each narration, music, effects, or cleanup asset. For uploaded sources, use measured upload metadata in `quote_cost` before approving a media-to-audio operation.

## Turn the brief into an audio plan

Identify the requested assets: narration, a music bed, sound effects, or a subset. Establish language, duration, mood, pace, instrumentation, loop requirements, and intended use. Keep an explicit asset list with one purpose and duration target per item.

## Inspect the relevant audio models

Discovery examples are ElevenLabs v3 (`eleven_v3`), ElevenLabs Music (`eleven_music_v1`), and ElevenLabs Sound Effects (`eleven_sound_effects_v1`). Inspect actual models before choosing options. Music exposes `duration_seconds` and `force_instrumental`; sound effects exposes `duration_seconds` and `loop`.

For speech, obtain the model's voice catalogue and real voice IDs through `list_voices`. Use facets to resolve missing preferences and offer a small selection instead of silently picking from hundreds of voices. Keep script wording distinct from voice direction.

Quote each asset using its actual prompt or structured `inputs` text/voice list and complete options. For structured dialogue, retain `inputs` when merging resolvedOptions; a separate prompt is optional. For prompt-priced speech, include the actual script rather than letting an omitted prompt select a maximum-length quote. Explain any reservation and settlement conditions. A revised script can change the price.

## Review and deliver the assets

Check spoken wording, pronunciation, pacing, requested duration, clipping, noise, musical direction, and loop seams where playback is available. For existing noisy media, VEED Clean Audio (`fal_veed_clean_audio_v1`) exposes normalization, strength, and loudness controls; treat cleanup as an additional scoped action.

Deliver separate, clearly named audio files with their purpose and timing notes. A general multitrack mixer is not exposed by the inspected tools. Do not claim that independently generated music, narration, and effects have been mixed or synchronized into a finished soundtrack unless an available additional tool actually performs and verifies that work.
