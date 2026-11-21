---
name: stream-health-check
description: Use when the user asks whether their stream is working, why it went offline, why a platform shows an error, or whether anything went down overnight.
---

# Stream Health Check

1. playout_list, then playout_get_state for each stream the user cares about (all of them if they did not say).
2. For each stream report: is it on air (isRunning and running.status), what is playing (running, not the saved items), and for each destination its liveState with any error text.
3. For "did it go down?", call insights_list_sessions. An "error" end followed by a new session of the same destination minutes later is the push reconnecting by itself, not downtime. Say so.
4. For YouTube destinations, destination_list_archive_parts shows the current part and when the last 11-hour rotation happened.
5. For an error message you cannot explain, docs_search with its key words, then docs_get.

Output: one short block per stream: on air or not, each platform's state, the last error if any, and the next step.
Only fix things the user asks you to fix, after confirming. A destination that stopped while its stream keeps running is restarted with destination_start; a stopped stream is started with playout_start.
Do not guess causes the data does not show.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
