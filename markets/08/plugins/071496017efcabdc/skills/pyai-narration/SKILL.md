---
name: pyai-narration
description: "Create expressive, directed or multi-line narration from a script using PyAI Cast, including supported voices, pauses and emotions."
---

# Narration

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `get_cast_capabilities`, `direct_cast_script`, `preview_cast_line`, `render_cast`, `get_cast_render`, `get_cast_audio`

Read `get_cast_capabilities` for available voices and supported directions. Use `direct_cast_script` to structure the supplied script when needed, retaining the user's intended wording and speaker assignments.

Use `preview_cast_line` for a requested sample, or `render_cast` for the requested full narration. Both media generation and previews may consume usage; do not generate extra variants just to demonstrate the integration.

For asynchronous renders, preserve the original job ID and poll `get_cast_render`; do not resubmit pending work. Retrieve completed media through `get_cast_audio` and return the actual audio/link. Report an incomplete render's ID and status when the task's waiting limit is reached. Do not invent unsupported emotions, voices or rendering options.
