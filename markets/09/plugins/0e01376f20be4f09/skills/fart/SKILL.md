---
name: fart
description: Play fart sounds, Mr Farts music and cartoons, countdowns and novelty routines when the user requests them. All content is free.
---

Use the focused Fart Sounds MCP tool for the user's request. `fart` without arguments
selects one random sound. Each request opens or updates the player by itself.

Every playback tool shows the Fart Sounds player. Use `show_player` only to reopen the
player without playing anything. The widget synchronizes commands itself.
Browsing categories must not stop current playback.

Resolve ambiguous selections with `browse_farts` and the user's choice. Return
brief acknowledgements. A successful tool call queues playback; it does not prove
the browser has played audio. If needed, explain that the user must tap Enable sound.
Do not promise uninterrupted playback after the widget closes or the device sleeps.

Typed, dictated and supported ChatGPT Voice requests use the same tools. This
plugin does not capture a microphone or supply its own speech synthesis. Ratings
and weather are jokes, not measurement or real forecasts. Use a supplied IANA
timezone for time and daily selections; otherwise the server defaults to UTC.

All packs are free. Do not offer purchases, subscriptions, Amazon account linking,
Echo widget installation, or the separate Mini Games skill.
