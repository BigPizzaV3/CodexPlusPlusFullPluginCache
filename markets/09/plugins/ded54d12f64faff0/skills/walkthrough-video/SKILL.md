---
name: walkthrough-video
description: Turn a room render or photo into a short cinematic walkthrough video with MeltFlex. Use when the user wants a video, reel, animation or a moving camera through the room.
---

# Walkthrough video

## Steps

1. Use the most recent render, or a photo the user shares.
2. Confirm length if the user did not say: 4 seconds (100 credits) or 8 seconds (150 credits).
3. Call `create_walkthrough` with `image`, optional `prompt` for camera direction, `duration_seconds` and `aspect_ratio` (`16:9` for listings and YouTube, `9:16` for Reels and TikTok).
4. The card updates by itself while the clip renders (about 1 to 4 minutes). If the host cannot refresh it, call `check_job` with the `jobId` every 10 to 15 seconds until it succeeds.

## Camera directions that work

- "Slow dolly forward at eye level toward the window."
- "Gentle pan from left to right across the kitchen island."
- "Slow push in on the bed, soft morning light."
