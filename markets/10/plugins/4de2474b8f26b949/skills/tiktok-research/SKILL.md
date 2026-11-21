---
name: tiktok-research
description: Search TikTok or retrieve public profile, posts and sampled video comments with HasData. Use for native TikTok data, not Google's short-video placements, private access or posting.
---

# Research public TikTok data

Read `../hasdata-research/SKILL.md` and the Social and video section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_tiktok_search_getTikTokSearch` with keyword and actual type enum video or user for discovery. Profile and account-post tools are `hasdata_tiktok_profile_getTikTokProfile` and `hasdata_tiktok_posts_getTikTokPosts`, using handle without @.

For comments, call `hasdata_tiktok_comments_getTikTokComments` with an actual videoId. Extract it from an unambiguous supplied /video/ URL or reuse a returned ID. commentId selects replies to a real returned comment; do not invent either identifier.

Use only the operation needed and one initial page. Preserve returned URLs, dates, counters and sample size. Profile stats are not content transcripts; comments are not proof of the creator's intent. Missing data stays unavailable and no single snapshot proves growth.

Use returned nextPageToken only for requested continuation. For clips appearing in Google, use `../google-short-video-research/SKILL.md`. Do not log in, bypass a private account, post, follow or message.
