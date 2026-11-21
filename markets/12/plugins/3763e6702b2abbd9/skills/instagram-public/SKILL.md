---
name: instagram-public
description: "Benchmark public Instagram Business and Creator profiles through Windsor.ai. Use when the user asks about competitors' or other public Instagram profiles they track, such as follower and following counts, number of posts, posting frequency, or post likes, comments, captions and media types. This connector is read-only: it has no write actions and cannot post, comment, or read private accounts or private insights such as reach and impressions. Do not use for the user's own Instagram account insights (use the Instagram connector), for publishing, or for other social networks."
---

# Instagram Public via Windsor.ai

Windsor.ai exposes publicly available data of Instagram Business and Creator
profiles (read only) through MCP tools. The connector id is `instagram_public`.
On the Instagram Public app the connector is already scoped, so you usually do
not need to pass it, but when a tool asks for a connector, use `instagram_public`.

Each Windsor.ai account of this connector is one tracked public profile; its
account id is the Instagram username. The data comes from Instagram's public
business discovery, so only Business and Creator profiles work, and only public
numbers are available (no reach, impressions, saves, or follower lists).

Golden rules:

- **Never guess field or account names.** They come from `get_fields` and
  `get_connectors`. Call those first; do not invent usernames or field ids.
- Instagram Public is **read-only**: there are no write actions. Do not offer to
  post, comment, follow, or message.
- Report the numbers the user asked for, concisely. Don't dump raw rows unless asked.

## 1. Ground yourself first

Call `get_connectors` to see which public profiles are tracked (the account ids
are usernames). If the profile the user asks about is not tracked yet, help them
add it: call `get_connector_authorization_url` (or `get_connector_connect_info`)
and give them the setup link, where they connect their own Instagram Business
account and enter the usernames to track. Do not describe manual dashboard
navigation.

## 2. Reading profile and post data

1. Call `get_fields` for `instagram_public` to get valid field ids. Profile
   fields cover followers, follows, and media count; post fields cover the media
   id, caption, permalink, media type, timestamp, likes, and comments. Use the
   exact ids returned.
2. Call `get_data` with:
   - `fields`: the ids you actually need (keep the set small).
   - `accounts`: the tracked usernames to compare; omit for all tracked profiles.
   - A date range: `date_from`/`date_to` (`"2026-07-01"`), or a `date_preset`
     (`last_7d`, `last_30d`, `last_90d`, `this_month`, `this_year`, `last_year`).
     Posts are returned when their publish date falls inside the range.

Common requests and recipes:

- **Audience comparison:** profile follower count and media count per account.
- **Top posts:** post likes and comments over a preset range; sort and show the
  caption and permalink.
- **Posting cadence:** count posts per week per account; break down by media type.

If a field the user wants isn't in `get_fields` (for example reach), say it is
not available for public profiles rather than substituting another metric.

## 3. Reference the user's data, don't fabricate

If a tool returns an error (unknown field or account, or a profile that is
private or not a Business or Creator account), call the relevant discovery tool
and explain the limitation. Never fill gaps with made-up numbers or posts.
