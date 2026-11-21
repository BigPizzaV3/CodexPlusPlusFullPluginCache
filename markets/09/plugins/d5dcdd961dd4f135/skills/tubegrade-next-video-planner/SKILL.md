---
name: tubegrade-next-video-planner
description: Decide the single best next video for a creator's own channel, weighing what already works for them, what is breaking out with similar channels, and which title formats are rising. Use for "what should my next video be", "plan my next upload", "which of these ideas should I make first".
---

# Next video planner

Read `references/tubegrade-tools.md` first.

Goal: ONE recommended next video (plus two runners-up), justified by the
user's own channel and by what is working for channels like theirs.

## 1. Scope
You need the user's channel (handle or URL). If they gave candidate ideas,
evaluate those instead of generating new ones.

## 2. Evidence lanes — budget ≈ 50–80 credits (say so before starting)
1. **Their baseline**: `tubegrade_get_channel` (size, average views, growth)
   and `tubegrade_get_channel_outliers` (what already over-performs for them).
2. **Their peers**: `tubegrade_my_competitors` if they track any; otherwise
   `tubegrade_similar_channels` and pick 2–3. Run
   `tubegrade_get_channel_outliers` on at most 2 peers.
3. **The market**: one `tubegrade_find_outliers` on their core topic
   (`days` 180, `min_ratio` 2).
4. **Packaging climate**: one `tubegrade_viral_formats` (`kind` title, no
   filters); note which formats are emerging or rising.

Skip any lane the user's question doesn't need. If the channel is brand new
(few videos), lean on lanes 2–4 and say so.

## 3. Decide
Score each candidate topic on:
- **Proven for them** — similar topics already beat their own average
- **Proven nearby** — peers or the market show breakouts on it
- **Fresh** — recent breakouts (last 6 months), not a played-out topic
- **Feasible** — they can make it with what their channel shows
- **Packaging fit** — a strong (ideally rising) format suits it

Prefer topics with evidence in two or more lanes.

## 4. Deliver
**Make next: <working title>**
- Why: 2–3 sentences tying the lanes together
- Evidence: the specific videos (link, views, outlier ratio) from their
  channel and from peers/market
- Suggested angle and format; the proven title format it can use
- Risk: what could make it underperform

**Runners-up**: two more, one line each with their best evidence.

**What to check after publishing**: compare its first-week views with their
channel average (from `tubegrade_get_channel`).

## Hand-offs
Titles and thumbnails → **tubegrade-packaging-studio**; script →
**tubegrade-script-writer**.

## Don't
- Don't recommend a topic with evidence from a single video only, unless you
  label it low confidence.
- Don't exceed the stated budget without asking.
