---
name: promote-a-youtube-video
description: Use when someone wants more views, subscribers, listeners or fans for a YouTube video, Short, music video or channel, or asks how to promote a video, what promotion costs, or whether promoted views are real.
---

# Promote a YouTube video with Sprizzy

1. **Get the video.** If the user shared a video link, call `plan_youtube_video_promotion` with it and their goal
   (views, subscribers, music_fans or website_traffic). If they shared a channel instead, call
   `list_youtube_channel_videos_to_promote` and let them pick a video. If they shared nothing, answer their question
   briefly (use `get_youtube_video_promotion_playbook` for cost, safety or how-it-works questions) and ask for the link.
2. **Walk through the card.** The user can see the Promotion Readiness card, so do not read every check back. Lead
   with the score and verdict, explain the one or two fixes that matter most for their goal, and expand the targeting
   starting points into concrete audiences (similar channels or artists, topics, places).
3. **Offer the launch.** When the video is ready, point to the "Promote this video on Sprizzy" button. The user picks
   the audience and budget on Sprizzy before anything runs.

Be accurate: never promise views, subscribers or virality. Costs are estimates. Sprizzy uses real ads on Google
Ads, never bots; decline requests for fake views or fake subscribers.
