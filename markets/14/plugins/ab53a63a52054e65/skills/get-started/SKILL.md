---
name: get-started
description: Set up and start using Trendhaus for TikTok research. Use when the user installs Trendhaus, asks what it can do, or asks how to analyse TikTok videos, trends, hooks, competitors, comments or sounds.
---

# Getting started with Trendhaus

Trendhaus gives ChatGPT live public TikTok data with analysis on top. It is read-only research: it never posts, follows or changes anything on TikTok.

## Connect

The user signs in to their Trendhaus account once when connecting. No TikTok login or API key is needed. If a call says the user is out of actions, tell them what it says; plans are managed in their Trendhaus dashboard.

## Which tool for which question

| The user wants… | Tool |
|---|---|
| A breakdown of one video they paste (hook, scenes, sound, comments, how it performed) | `trendhaus_post_analysis` (set `includeComments` for comment themes and purchase intent) |
| What is trending now, or trends a brand could use | `trendhaus_trend_radar` (discovery first; pass a `trend_name` from the results for one trend's full history) |
| Hooks that work in a niche | `trendhaus_hook_library` |
| What competitors are posting | `trendhaus_competitor_pulse` (uses the tracked competitors, or pass `handles`) |
| A creator's profile or recent posts | `tiktok_get_user_info`, `tiktok_get_user_feed` |
| Comments on a post | `tiktok_get_comments`, then `tiktok_get_replies_comment_of_post` for one thread |
| Who uses a sound | `tiktok_get_music_posts` |
| Videos for a keyword or hashtag | `tiktok_search_video`, `tiktok_get_challenge_posts` |
| Top-performing ads | `tiktok_get_top_ads`, then `tiktok_get_ads_detail` |
| Remaining actions | `trendhaus_check_usage` |

## Personalise once

When the user mentions their own handle, niche, region or competitors, save them with `trendhaus_update_my_context`. Other tools then use that profile, and `trendhaus_competitor_pulse` checks the saved competitors without asking again.

## Read results faithfully

- Analysis tools return a `gaps` list. A result with gaps is partial in exactly the way the gap describes (for example, not niche-filtered), so say so.
- Paid-promotion flags are best-effort; a post without a flag may still be promoted.
- `first_seen_at` on a trend is when Trendhaus first saw it, not a forecast.
- Hook Library and Post Analysis watch real videos and can take from a few seconds to about 3 minutes.

## First prompts to suggest

- "Break down this TikTok for me: [link]"
- "What's trending on TikTok right now that [my brand] could use?"
- "Show me TikTok hooks that are working for [niche] creators"
- "What are @competitor1 and @competitor2 posting, and what's working best for them?"
