---
name: performance-report
description: Build a social media performance report from Postproxy data - what was published, how posts performed, and how followers and engagement changed over a period. Use when the user asks how their social accounts or posts are doing, wants a weekly or monthly report, or wants to compare networks or posts.
---

# Performance report

Produce a short, accurate report from Postproxy data. Read-only: this skill never changes anything.

## Data to gather

1. `summary_get` for the period (`window`, or `from`/`to` for an explicit range, and `profile_group_id` to report on one brand). It returns posts published and failed, engagement totals, comments, reviews, and DM volume per network, with comparison counts for the previous period.
2. `history_list` for the posts behind those numbers (raise `limit` for longer periods).
3. `post_stats` with up to 50 post IDs to rank posts. Each post has several snapshots over time, so use the latest one per post and network.
4. `profiles_stats` for follower and audience trends per profile. Facebook, LinkedIn, Telegram, and Google Business need a `placement_id` from `profiles_placements`.

## How to read the numbers

- Engagement in `summary_get` is lifetime-to-date for posts published in the window, not engagement earned during the window. Say this when comparing periods.
- In `summary_get`, a post sent to three networks counts once in post totals and three times in `by_platform`.
- Stats fields are each network's own metrics and aren't normalized. Compare like with like (for example, Instagram likes against Instagram likes) and don't add up different metrics across networks.
- `engagement` is null when insights are turned off for the account. Say that instead of reporting zero.
- Google Business stats are impressions, website clicks, calls, direction requests, and conversations. There is no follower count.

## Report shape

1. A headline line: posts published, the overall engagement trend, and the most important change.
2. A per-network table with posts, key engagement metrics, and follower change.
3. The top three posts with links and why they likely did well (format, topic, timing), and any failed posts with the error.
4. Two or three concrete suggestions based on the data, such as what to post more of or when to schedule. Label them as suggestions.

Only report numbers returned by the tools. If data is missing for a network, say so rather than estimating.
