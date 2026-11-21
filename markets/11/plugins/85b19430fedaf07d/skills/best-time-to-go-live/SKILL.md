---
name: best-time-to-go-live
description: Use when the user asks when their viewers watch, which day or hour is best to go live, or when to schedule a show or premiere.
---

# Best Time to Go Live

1. Ask for the user's time zone if you do not know it.
2. insights_get_heatmap (default window 28 days, narrow with playoutId or channelId). Cells are day of week (0 = Sunday) and hour in UTC: convert to the user's zone before answering.
3. Mention the sample count: hours with few samples are a weak signal. Missing data means there is not enough streaming to measure yet, not that nobody watches.
4. insights_list_sessions adds context (peak viewers per session).
5. Answer with the two or three best windows in the user's time zone. Offer to schedule a show there (the weekly-show-schedule skill).

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
