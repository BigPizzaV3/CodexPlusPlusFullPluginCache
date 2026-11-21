---
name: google-short-video-research
description: Retrieve Google's short-video search results and their original source links with HasData. Use when Google is the requested discovery source; native YouTube or TikTok searches use their own skills.
---

# Find short videos in Google

Read `../hasdata-research/SKILL.md` and the Search sources section of `../hasdata-research/references/tool-catalog.md`.

Call `hasdata_google_serp_short_videos_getShortVideosSearchResults` with q and requested localization. Start with one page. Return actual titles, platform/source URLs and available dates, creators or counters from the payload.

Do not silently substitute a YouTube search, TikTok search or full organic SERP. Returned Google placement is not a universal native-platform ranking, and missing counters are unknown.

For the content of a selected YouTube video, use `../youtube-research/SKILL.md` with its actual returned URL/ID and a separately budgeted transcript call. A Google snippet is not a transcript or proof the video was watched.
