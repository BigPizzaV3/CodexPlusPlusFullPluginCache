---
name: post-scheduling
description: Plan, write and schedule social media posts with the SocialAPI app. Turn a brief or a week of themes into posts adapted to each platform, check them against each platform's rules, save drafts, and schedule or publish only after approval. Use when the user says "schedule a post", "plan my posts for the week", "content calendar", "cross-post this", "post to Instagram and LinkedIn", "draft a post", "publish now", or shares an announcement to put on social media.
---

# Post scheduling

Requires the SocialAPI app in ChatGPT. Every tool name starts with `social_api_`. The `socialapi` skill holds the full `create_post` fields, media rules, platform support and error codes: follow it for every call.

## 1. Brief

Get the message, the platforms, the dates and times with a timezone, and the media as public links. Ask only for what is missing. Without a timezone, ask before scheduling anything.

## 2. Accounts and per-platform ids

- `list_accounts` and map each platform the user named to its account `id`.
- Facebook Page or LinkedIn Page: `list_account_pages` for the `page_id`.
- Pinterest: `list_pinterest_boards` for the `board_id`, required on every Pinterest target.
- TikTok: `get_creator_info` before every post, and use one of the privacy levels it lists in `platform_data.tiktok.privacy_level`.

## 3. Write one variant per platform

Put the shared text in `text` and each platform's version in its target's own `text`. Adapt length, tone and hashtags to each network:

- Instagram: caption with hashtags. Every post needs an image or video and `platform_data.instagram.content_type` (`feed`, `carousel`, `reel` or `stories`).
- X: short. A longer message becomes a thread with `segments`.
- LinkedIn: longer and professional. A link preview goes in `platform_data.linkedin.article_url`.
- YouTube and Pinterest: set `title`.
- Google Business Profile: a short local update.

For exact limits, call `get_constraints` rather than guessing.

## 4. Check

`validate_post` with `account_ids`, the text, the media and the same `platform_data`. Fix every `errors` entry, report `warnings`. `validate_post` does not catch a missing Instagram image or video, so check that yourself.

## 5. Show the calendar

One table: date and time (user's timezone and UTC), platform, final text, media, check result. Wait for approval.

## 6. Save, schedule or publish

- By default, save drafts: `create_post` with neither `publish_now` nor `scheduled_at`. Drafts are free.
- After an explicit yes: `scheduled_at` (RFC3339) to schedule, or `publish_now: true`. Publishing or scheduling costs a post credit, so check `get_usage` first when there are many. One `create_post` per time slot; a target may carry its own `scheduled_at`.
- The same content posted again within 24 hours is refused unless `skip_duplicate_check: true`. Ask before setting it.
- After publishing, poll `get_post` until it reads `published`, `partial` or `failed` before saying it worked. Offer `retry_post` for failed targets.
