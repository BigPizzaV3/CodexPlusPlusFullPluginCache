---
name: youtube-watch-hours-planner
description: Use when the user wants to reach YouTube Partner Program watch hours with their streams, or asks why live stream watch time is not counting.
---

# YouTube Watch Hours Planner

1. channel_list to find the YouTube channel, then channel_list_videos. Count the uploads flagged qualifyingLongForm (public and not short): these are what the watch-hour rules count.
2. For each stream with a YouTube destination, playout_get_state: is archive rotation on? Then broadcast_get_details on its broadcast: is it public?
3. Explain from the help center (docs_search "watch hours archive rotation", then docs_get): only saved, public archives keep counting; YouTube may not save a broadcast longer than about 12 hours; the 11-hour rotation keeps every part saved.
4. insights_get_overview shows viewer hours over a period.
5. Give the user a checklist of what is in place and what is missing.

Never promise approval: YouTube reviews channels and decides. Do not suggest presenting recorded videos as live events.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
