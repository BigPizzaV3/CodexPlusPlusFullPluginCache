---
name: multistream-to-more-platforms
description: Use when the user wants the same stream on more platforms at once: YouTube, Twitch, Facebook, LinkedIn, Kick, Instagram, TikTok, X or another RTMP server.
---

# Multistream to More Platforms

1. channel_list shows the connected accounts.
2. YouTube, Twitch, Facebook, LinkedIn and Kick need a sign-in. If one is missing, channel_connect_link gives the user a link to connect it in their own browser. When they say they are done, check channel_list again.
3. For a Facebook Page or LinkedIn page rather than a personal profile, channel_list_targets gives the ids destination_create needs.
4. Platforms that give a stream URL and key (Instagram, TikTok, X, any RTMP server): when the user provides both, channel_create_rtmp (Creator plan and up).
5. destination_create for each platform. The plan sets how many destinations one stream can have; a refusal says so.
6. If the stream is already live, each new destination goes live with destination_start (confirm first). If it is stopped, playout_start takes every destination live.
7. playout_get_state confirms each destination's liveState.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
