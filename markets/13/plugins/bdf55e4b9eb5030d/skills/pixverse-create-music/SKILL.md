---
name: pixverse-create-music
description: "Generate music, songs and soundtracks. Route spoken narration to pixverse-create-voice and existing-media mixing to video editing; music generation does not imply dedicated SFX support."
---

# Create Music

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
In MCP mode, read `../../skills-shared/mcp-workflow.md` and follow the MCP scope below.
Do not execute the local setup, queue, filesystem, QA or finishing instructions below in MCP mode.
Script-only work needs no login or tools.

### MCP Scope

Generate standalone music using live music models and supported lyrics or instrumental controls. Spoken narration belongs to pixverse-create-voice. Do not promise dedicated SFX generation, mixing, trimming, fades or exact-duration soundtracks through music generation.

List accessible workspaces or inspect the current selection. Switch only to the user's explicitly requested workspace using the freshly verified expected_current_workspace_id. This does not authorize spending or team administration.

Discover supported music models and input fields from the current catalog. Describe mood, instrumentation, energy, desired duration and any supplied lyrics. Do not invent voices, exact timing guarantees or unsupported sound-generation modes.

For execution, read `../../skills-shared/execution-surface.md`. It selects the supported CLI or MCP branch, checks account and quality requirements, and preserves submission identity through delivery.

# Music Production



## CLI Execution

Apply `../../skills-shared/quality-policy.md` to all generated images/videos: Sunburst 2K/high,
Seedance 2.5 1080p with automatic prompt enhancement, and an explicit upgrade/fallback
choice for Free/Basic or model-entitlement rejection.

For an explicitly selected Canvas project or node, read
`../../skills-internal/pixverse-agent-canvas/SKILL.md` first and follow its Canvas
preflight and delivery contract; the ordinary queue/local route below does not replace it.

For ordinary creation or editing, read `../../skills-shared/cli-workflow.md` before
executing this workflow. It contains the existing account-aware routing, paid-work
confirmation, progress, preview and project-handoff rules. Studio and Production are
not prerequisites. The shared account, confirmation and direct-medium rules govern the
examples and defaults below. Read the gateway only when writing manual CLI commands or queue specs.
Creation command examples below are queue-task fragments, not permission to submit paid
`pixverse create` commands directly.

Read `../../skills-shared/audio-craft.md`.

For standalone SFX/reference-audio capabilities, read
`../../skills-shared/extended-capabilities.md`. Native UGC voices follow their
specialized workflow; do not simplify its audio map into a sparse generic prompt.

## Related Audio Work

For spoken narration, separate takes or timed voice work, use
`../pixverse-create-voice/SKILL.md`; do not submit voice through this music Skill.
For subtitles, use `../pixverse-captions/SKILL.md`. Standalone SFX and video sound
follow their actual capabilities and the related guidance above; never present them as music modes.

## Music

Use standalone music when BGM/soundtrack is requested:

```bash
pixverse music models --json
pixverse create music --model music-2.6 --prompt "..." --instrumental --json
```

Use lyrics only when vocals are part of the concept. `music-3.0` (MiniMax Music 3.0)
and `music-v2` (ElevenLabs Music V2) support lyrics, auto lyrics and instrumental
generation; the default remains `music-2.6`. Read
`../../skills-shared/pixverse-cli-models.md` for the reviewed alternatives.

Music is generated at auto-duration and edited to the picture; `--duration-seconds` and
`--no-duration-auto` are refused by the queue because the service rejects fixed targets.
Treat a requested length as an edit requirement: measure the returned audio and trim/fade
locally. See the shared audio craft reference.

## Video Audio

Use in-video generated sound when the brief wants the model to synchronize ambience and sound effects to the generated motion. Do not describe this as "music none" shorthand; write the no-music requirement in plain natural language.

Before using `--audio`, decide and record one of these modes:

These switches apply only when the selected model exposes them. Seedance 2.5 omits both
`--audio` and `--no-audio`; keep sound intent in the prompt, inspect returned sound, and mute
locally for a silent deliverable. Missing toggle support does not establish missing audio.

MiniMax H3/H3 Max is a different contract: generated audio is unsupported. Its
`--audios` accepts reference inputs; it does not enable output sound. Plan separate
voice/music or local sound assets when sound is required, preserving paid approval.

| Mode | Use when | Command stance |
|---|---|---|
| synced SFX/ambience | model should create sound tied to visible motion, with no music | `--audio`; use natural-language no-music instruction |
| clean picture | sound will be rebuilt from separate stems or user asked for silent picture | `--no-audio` |
| fused native audio | casual social/UGC clip where baked audio including music may be acceptable | `--audio` where supported; preserve the workflow’s complete sound/voice plan |

For in-video generated sound, use a plain-language audio paragraph and avoid musical cue words:

```text
This video should not generate any music, background music, score, melody, rhythmic bed, or trailer-style musical hit.
Only generate synchronized sound effects and environmental ambience for what is visible in the shot.
The sound should be natural and quiet: physical Foley from the characters and objects, room tone, air, footsteps, fabric, breath, water, and other diegetic sounds.
Do not add orchestral emotion, musical chimes, melodic pads, percussion, or any soundtrack-like layer.
```

If the result contains unwanted music or unpleasant SFX/ambience, mark that audio rejected and strip/replace it. Do not mix BGM over a bad generated track.

If `quote queue` adds an audio note, treat it as an advisory reminder. If the prompt already says "no music" or the user's intent is clear, proceed to confirmation without changing the route. Only rewrite the sound paragraph when it is quick and obviously improves the prompt; do not switch to `--no-audio` or delay the run just to silence the note.

For post overlay, use `../pixverse-video-editing/SKILL.md` and keep audio assets separate.