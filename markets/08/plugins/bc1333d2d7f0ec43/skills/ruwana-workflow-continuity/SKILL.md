---
name: ruwana-workflow-continuity
description: Continue an active Ruwana Studio workflow across follow-up intent changes, especially when the user refers to an existing Ruwana result and asks to display, inspect, edit, animate, make video, transfer motion, create an avatar, use LAB or use PRO. Preserve the canonical Ruwana result and use the appropriate Ruwana MCP tool instead of treating a currently unloaded tool schema as an unavailable Ruwana capability.
---

# Ruwana workflow continuity

Use this skill when the user explicitly starts work with Ruwana/Ruwana Studio, requests a Ruwana module, or continues work on an established Ruwana result, job, displayed card or inspected image. A follow-up such as “this”, “that”, “this result”, “the one above”, “animate it”, “make a video from it”, or “edit it” continues the Ruwana workflow unless the user clearly asks to switch to another system.

## Continuity rule

1. Preserve the exact canonical Ruwana `result_id`, production job identity and media references already established by prior Ruwana tool output.
2. When the user's intent changes, reconsider the Ruwana MCP dependency and select the Ruwana tool that matches the new intent. Do not assume that only tools used in previous turns exist.
3. Never interpret “the schema/tool is not currently present in the locally loaded subset” as “Ruwana does not provide this capability.” Before stating that a Ruwana capability is unavailable, resolve the request against the tools exposed by the Ruwana MCP dependency.
4. Do not replace an active Ruwana production workflow with a ChatGPT-native image/video/edit route merely because the follow-up uses generic wording such as “animate this”. Native or other-app execution is appropriate only when the user clearly switches away from Ruwana or the request is not part of an active Ruwana workflow.
5. If a genuinely required Ruwana input is missing, recover it from prior Ruwana output or Ruwana read tools when possible. Ask only for an input that cannot actually be resolved. Do not invent identifiers or capability state.

## Intent handoff

Use the tool descriptions as the source of truth for each module's full execution contract. For continuity routing:

- Existing READY Ruwana image + simple no-prompt “animate this/it” -> `ruwana_quick_animate` with the exact canonical `result_id`.
- Full directed video production from a Ruwana image -> `ruwana_video_generate`; preserve the canonical source with `start_result_id` when available.
- Actual pixel judgment/description/diagnosis needed -> `ruwana_inspect_result_image`; simple replay/display alone does not require inspection.
- Show an already-resolved result -> `ruwana_display_result` after the relevant Ruwana data/production result supplies its exact media.
- Creative image edit/transformation or LAB workflow -> `ruwana_lab_generate` according to its mode contract.
- Ruwana model-based photographic production -> `ruwana_pro_generate` according to its structured PRO contract.
- Motion transfer from a source video to a character image -> `ruwana_motion_generate`; do not confuse this with Quick Animate or general Video.
- Talking-avatar production -> `ruwana_avatar_generate` according to its exclusive script/TTS or uploaded-audio path.
- Pending/generating production -> `ruwana_job_status` until the requested workflow can continue from canonical server truth.

## Success condition

The conversation may move between read, display, inspect and production intents without losing Ruwana context. A successful follow-up uses the correct currently exposed Ruwana tool, keeps canonical identity across turns, and never falsely reports a Ruwana capability as absent merely because that tool was not used or loaded in the immediately preceding turn.
