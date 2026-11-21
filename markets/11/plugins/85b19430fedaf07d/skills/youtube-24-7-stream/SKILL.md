---
name: youtube-24-7-stream
description: Use when the user wants a live stream that runs around the clock on YouTube from their own videos, or asks how to keep a looping YouTube stream going with every part of it saved.
---

# 24/7 YouTube Stream Setup

Input: a stream (or videos to build one) and a connected YouTube channel.

1. Find the stream with playout_list, or build one as in the get-started skill (media_import, playlist_create, playout_create).
2. Call channel_list. If no YouTube channel is connected, call channel_connect_link with platform YOUTUBE and give the user the link. They sign in to YouTube in their own browser. When they say they are done, check channel_list again, then continue.
3. Add the YouTube destination with destination_create. Without a broadcast id it creates a new public broadcast.
4. Explain what the plan allows, from org_get_capabilities:
   - Free: each session stops after 2 hours and its broadcast ends, so YouTube saves every session as its own video.
   - Paid plans: the stream can run continuously. YouTube may not save a broadcast longer than about 12 hours, so offer destination_set_archive_rotation, which starts a new broadcast every 11 hours. Each part gets its own watch link and live chat starts fresh.
5. If the user wants watch hours to count, check the broadcast is public with broadcast_get_details.
6. Only if the user says the videos show realistic AI-generated or altered people, voices or scenes, turn on destination_set_altered_content.
7. Confirm, then playout_start. Check with playout_get_state that the YouTube destination's liveState is running.

Do not promise monetization or Partner Program approval; YouTube decides. Do not add "LIVE" wording to titles for recorded content unless the user asks for it.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
