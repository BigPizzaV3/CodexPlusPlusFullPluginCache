---
name: pixverse-create-voice
description: "Voiceover: produce natural narration or explicitly timed takes, preserving pronunciation, voice continuity and measured timing for editing."
---

# Create Voice

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
In MCP mode, read `../../skills-shared/mcp-workflow.md` and follow the MCP scope below.
Do not execute the local setup, queue, filesystem, QA or finishing instructions below in MCP mode.
Script-only work needs no login or tools.

### MCP Scope

Generate standalone spoken narration or explicitly requested separate takes. Preserve exact text, language and pronunciation; discover actual voice/model IDs. Deliver returned timing metadata without inventing alignment. No dubbing, forced alignment, exact-window repair or automatic concatenation.

List accessible workspaces or inspect the current selection. Switch only to the user's explicitly requested workspace using the freshly verified expected_current_workspace_id. This does not authorize spending or team administration.

Preserve the spoken text, language and pronunciation requirements. Discover actual voice IDs and supported voice models. Ask only for material missing choices. Deliver the speech asset; measured timing, revoicing and timeline alignment require the production workflow.

For execution, read `../../skills-shared/execution-surface.md`. It selects the supported CLI or MCP branch, checks account and quality requirements, and preserves submission identity through delivery.

# Voiceover


## Make The Takes

- Preserve the accepted text and speaker language. Choose a voice using the current CLI voice catalog; use real returned IDs. A stored voice ID is not evidence of voice-cloning support.
- Split at natural thought or breath boundaries. Keep continuous passages together when tone matters; one subtitle per TTS request is only useful for a deliberately timed take list.
- Use the voice model's actual supported controls for speed, emotion or style. Send the spoken text separately from nonspoken direction; do not accidentally speak labels such as “pause” unless the engine supports an established markup syntax.
- Submit via the existing paid queue contract. Measure returned duration and listen for word errors, clipped ends and unnatural pauses.
- If a time window is strict, record its bounds and actual voiced interval. Use the
  selected mode's content/duration correction; never time-stretch or cut speech to fit.
  A separately requested speed effect is an explicit edit, not a narration repair.

## Cue Example

Spoken text: “Open the lid, then press the button on the side.”
Direction: reassuring instructional delivery; a natural breath after “lid”; pronounce every action clearly. Keep this direction outside the literal TTS text when the selected model has no markup/control for it.

## Use With Video

Actual audio determines caption and edit timing. Use `../pixverse-captions/SKILL.md` when burned captions are requested. New narration over an on-camera speaker requires verified sync capability or a new native speech shot; do not silently replace the audio beneath old lip motion.

## Deliver

Provide the audio, exact spoken text, measured timing and take identifiers. Only repair failed takes. Avoid introducing a separate narration task where an accepted native video soundtrack already meets the brief.

## Execution

Read `../../skills-shared/production-brief.md` for reference roles, prompt construction and revisions.
For media execution, follow `../../skills-shared/cli-workflow.md`; load the gateway before manual
CLI commands or queue specs. Resolve the plugin root from this skill's installed path:
set `PIXVERSE_RUNTIME="<absolute-plugin-root>/scripts/pixverse-runtime"` and invoke `"${PIXVERSE_RUNTIME}"` with the documented arguments.
Prompt-only work ends with the usable plan and prompts; it needs no account or generation calls.