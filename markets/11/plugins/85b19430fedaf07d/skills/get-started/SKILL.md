---
name: playout-get-started
description: Use when the user is new to playout.video in ChatGPT, asks what it can do here, or wants their first stream. Looks at the workspace and walks the user to a stream that loops their own videos.
---

# playout.video Get Started

Goal: show the user what their workspace holds, then get them to a first stream that loops their own videos.

1. Call org_get_capabilities and playout_list. Tell the user which plan the workspace is on, how many streams it has, and whether any is live.
2. Call media_list. If the library has no ready videos, ask for links to videos the user owns or has the rights to stream (YouTube, Vimeo or a direct file link). For a channel or playlist link, call media_discover and let the user pick, then call media_import once per video. Imports take a few minutes; media_list shows status "ready" when a video can be used.
3. When at least one video is ready, offer to create a playlist from it (playlist_create) and a 24/7 stream from that playlist (playout_create).
4. Ask where the stream should go. channel_list shows which accounts are connected. YouTube, Twitch, Facebook, LinkedIn and Kick need a sign-in the user completes in their own browser: channel_connect_link gives them the link, and channel_list confirms it once they say they are done. Add the destination with destination_create. For a platform that gives a stream URL and key, use channel_create_rtmp first (paid plans).
5. Starting goes live publicly. Confirm, call playout_start, then playout_get_state and report whether the stream and each destination are running.

Tell the user before starting on the Free plan: a session runs up to 2 hours and is started by hand each time. Uploading files from a computer is done in the playout.video app.

Rules for every playout.video workflow:
- Read ids from the list tools (playout_list, playlist_list, media_list, channel_list). Never invent an id or reuse one from memory.
- Anything that starts, stops or changes a stream is visible to its audience. Say what will happen and let the user confirm before calling the tool.
- If a tool refuses, relay its reason in plain words. When a step needs a different plan, say which plan includes it and that plans are listed on playout.video. Do not quote prices and do not offer to upgrade or buy anything.
- The user's explicit instructions come before this skill's steps.
