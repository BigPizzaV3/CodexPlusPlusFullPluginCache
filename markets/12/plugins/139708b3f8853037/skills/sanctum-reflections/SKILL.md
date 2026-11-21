---
name: sanctum-reflections
description: Use Sanctum Reflections for original contemplative dialogue, daily reflections, or requested voice playback in English or Spanish.
---

# Sanctum Reflections

Use the connected Sanctum Reflections tools for explicit requests for guided reflection or voice playback:

- `open_sanctum`: open the studio, optionally with a topic up to 1200 characters.
- `create_reflection`: reflect on a supplied topic of 2–1200 characters; length is brief, standard, or extended.
- `daily_reflection`: create a daily reflection, optionally with a theme up to 160 characters. This does not schedule recurring delivery.
- `create_reflection_audio`: only when the user requests audio of an existing reflection; text must be 2–1800 characters.
- `get_reflection_audio`: check a previously requested voice job by its returned UUID.

Set language to `english` or `spanish` according to the request. Discover live schemas before invoking tools; do not invent tools or silently truncate input beyond their limits.

Preserve the service disclosure: responses are original AI-generated reflections for personal contemplation, not professional advice, religious authority, secret doctrine, or an impersonation of a real person or organization.

If the service reports unavailable, relay that accurately. Do not claim that audio was generated without a successful result. Present returned audio through supported media playback when possible. Widget rendering depends on the host; do not promise an interactive widget without observing it.
