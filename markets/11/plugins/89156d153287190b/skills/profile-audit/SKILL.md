---
name: profile-audit
description: Audit how one social media profile performed over a period using Socialinsider data — followers and engagement trend, aggregate post metrics, post-type mix, and the posts that actually worked. Use when the user asks how a profile, account, brand or channel is doing, wants a performance review, monthly report, engagement-rate check, or asks why reach or engagement moved.
---

# Profile audit

Produce a performance audit for one tracked profile from Socialinsider data.

## Rules

1. **Call `socialinsider_get_date_context` first, always.** Your training data may be from an
   earlier year. Never guess or hardcode a year. Use the returned `date_ranges` values verbatim
   as the `date` argument (`{start, end, timezone}`, millisecond timestamps).
2. **Never invent ids.** `id` and `profile_type` must come from `socialinsider_list_profiles`.
   `projectname` is the project the profile lives in.
3. **Aggregate, don't paginate.** Use `socialinsider_get_posts_summary` for totals and averages
   and `socialinsider_get_top_posts` for rankings. Only fall back to `socialinsider_get_posts`
   when the user needs individual post records.
4. **Read-only.** This skill never calls a write tool (`create_*`, `add_*`, `remove_*`).

## Steps

1. `socialinsider_get_date_context` — get today's date and ready-made ranges.
2. `socialinsider_list_profiles` — resolve the profile the user named to its `id`, `profile_type`
   and `projectname`. If several profiles match, ask which one before continuing.
3. Pick the window. Default to `last_30_days` when the user didn't say. If the user asks about a
   trend or change, also fetch the immediately preceding window of equal length so you can compare.
4. Gather, in parallel:
   - `socialinsider_get_profile_data` — daily followers, engagement rate, reach, impressions.
   - `socialinsider_get_posts_summary` — true post count, totals, averages, breakdown by post type.
   - `socialinsider_get_top_posts` — `metric: "engagement"`, `limit: 5`.
5. If the profile is `instagram_profile_own`, add `socialinsider_get_instagram_stories` for the
   same window. Skip it silently for any other profile type — it is unavailable there.

## Output

A short written audit, in this order:

- **Headline** — one sentence: direction and size of the move ("engagement rate down 18% MoM on
  flat follower growth").
- **Numbers** — a compact table: followers (start, end, delta), posts published, total engagement,
  average engagement per post, engagement rate. Add the prior-period column when you fetched one.
- **What worked** — the top posts, with the metric that made them top and what they have in common
  (format, topic, length, posting time). Name the pattern, not just the posts.
- **Post-type mix** — which formats the profile leans on versus which formats earn engagement.
  Call out a mismatch when it exists.
- **Recommendations** — at most three, each tied to a number you just showed.

State the date range and timezone you used. Flag any metric the API returned as empty rather than
reporting it as zero — for non-owned profiles, reach and impressions are often simply unavailable.
