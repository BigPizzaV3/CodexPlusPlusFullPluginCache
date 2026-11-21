---
name: tubegrade-competitor-breakdown
description: Break down a rival YouTube channel — size and growth, which videos over-perform for it and why, its packaging style, how its best videos open — and turn it into opportunities for the user. Also finds who a channel's real competitors are. Use for "analyze @channel", "how is my competitor growing", "who are my competitors", "track this channel".
---

# Competitor breakdown

Read `references/tubegrade-tools.md` first.

Goal: what is working for a competitor, backed by numbers, and what the user
should do about it.

## 1. Scope
- **Breakdown of one channel**: you need its handle or URL. Knowing the user's
  own channel makes the "what it means for you" part sharper — ask once.
- **"Who are my competitors?"**: run `tubegrade_similar_channels` (5) on the
  user's channel, and `tubegrade_my_competitors` (2) if they track any. Present
  the list with sizes and links; offer to break one down or track them.
- **"Track this channel"**: `tubegrade_track_competitor` (free) — only on request.

## 2. Evidence — budget ≈ 30–45 credits (+ optional transcripts)
1. `tubegrade_get_channel` — size, average views, upload frequency, and the
   `growth` block when present.
2. `tubegrade_get_channel_outliers` — its breakout videos vs its own baseline.
3. `tubegrade_channel_videos` (`popular`) — what built the channel, versus its
   recent outliers (what works now).
4. `tubegrade_channel_thumbnails` (`recent`, `limit` 10–12) — look at the style.
5. Optional, ask first: `tubegrade_get_transcript` on its top 1–2 recent
   outliers (10 each) to study the hooks.

## 3. Analyse
- **Trajectory**: growing, flat or declining (from `growth`; say if there is no
  history yet). Multiply per-period averages by the gap for totals.
- **What over-performs**: cluster the outliers by topic, format and title
  pattern. Which clusters repeat? What has stopped working (popular-but-old vs
  recent)?
- **Packaging style**: what their thumbnails consistently do.
- **Hooks** (if transcripts): how the openings earn attention.
- **Gaps**: topics their audience clearly wants (outliers, or demand in
  comments if checked) that they cover rarely or poorly.

## 4. Deliver
1. **Snapshot** — subscribers, average views, upload cadence, trajectory.
2. **What works for them** — 3–5 patterns, each with linked example videos and
   their outlier ratios.
3. **Packaging style** — 3–4 observations from the thumbnails.
4. **Opportunities for the user** — 3–5 concrete moves (topics, formats,
   angles), each tied to the evidence and adapted to the user's channel.
5. Offer: track this channel (free, if their account includes tracking), or
   hand-offs → **tubegrade-video-ideas**, **tubegrade-packaging-studio**.

## Don't
- Don't speculate about a competitor's revenue, private analytics, or contact
  details.
- Don't recommend copying their videos; recommend the mechanism.
