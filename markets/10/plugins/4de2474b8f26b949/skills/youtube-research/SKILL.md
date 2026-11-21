---
name: youtube-research
description: Search native YouTube videos or Shorts, read video/channel data, or retrieve a supplied video's transcript with HasData. Use for YouTube research and transcript-based summaries, not Google's video carousel.
---

# Research YouTube videos and channels

Read `../hasdata-research/SKILL.md` and the Social and video section of `../hasdata-research/references/tool-catalog.md`.

Choose only the operation needed:
- Video discovery: `hasdata_youtube_search_getYoutubeSearchResults` with q.
- One video's metadata: `hasdata_youtube_video_getYoutubeVideo` with v.
- A transcript or content summary: `hasdata_youtube_transcript_getYoutubeTranscript` with v.
- A channel or its requested tab: `hasdata_youtube_channel_getYoutubeChannel` with channelId and the supported tab.

Extract the 11-character video ID directly from an unambiguous watch, youtu.be or shorts URL; no discovery request is needed for a valid supplied URL. channelId accepts supported UC IDs and public @handles. Preserve @ for a YouTube channel handle; do not apply Instagram's normalization. Resolve a display name only when the identity is unclear.

For a content summary, retrieve the transcript rather than automatically fetching metadata, search and transcript together. Preserve segment times and link the original video with timestamps when available. State transcript language and auto-generated status when returned. Do not claim to have watched the video or invent a transcript after failure.

For searches and channels, keep returned views, publication dates and source links. Use only returned paginationToken values when further pages are requested. Google short-video discovery belongs to `../google-short-video-research/SKILL.md`.

A request for YouTube Shorts is a native YouTube task, not permission to switch to Google. Apply only supported returned filters; do not invent a Shorts filter token or label ordinary videos as Shorts without source evidence. If the result does not establish the requested format, state that limitation.

Honor a requested transcript/file output instead of automatically replacing it with a summary. Provide full transcript text only when reproduction is permitted, such as user-owned or authorized content; otherwise offer a summary and timestamped links rather than exporting an unrestricted third-party transcript.
