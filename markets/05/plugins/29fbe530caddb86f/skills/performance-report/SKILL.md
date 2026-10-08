---
name: performance-report
description: |
  Analyze posting performance through the doublespeed MCP and turn it into decisions: exact aggregates, per-account and per-format breakdowns, winner/loser calls, and a written report. Use when the user asks what's working, for analytics, a performance report, account health, or what to post more of.
---

# Performance Report via doublespeed

## Setup

1. `whoami` to confirm the active product; `list_products` + `set_product` if wrong or missing. Never switch products on your own initiative afterward.

## Gather

1. **Aggregates first.** `get_post_metrics` returns exact totals, averages, medians, maximums, engagement, and per-account performance across the full filtered post set in one call - use it for every numeric claim instead of paginating and summing yourself. Filter by date range to compare periods.
2. **Ranked posts.** `list_posts` sorted by `viewsCount` (or date) for the top and bottom performers; pull `include_scene_data` only for the handful you'll dissect.
3. **Per-account drilldown.** `list_account_posts` for one account's history; `get_account` / `list_accounts` for status (good, warming, burned) and profile setup.

## Analyze

- Judge on **engagement rate** (likes/saves/comments relative to views), not raw views: distribution is noisy and one lucky post is not a format.
- Cut by format (slideshow vs video), hook style, account, and posting time. A format needs several reps before the algorithm catches - do not kill it on one flop.
- Dissect the top 3-5 winners' actual structure (hook wording, slide order, audio) - that nuance is the actionable part, not the numbers.
- Note account health: burned or inactive accounts drag averages; flag them rather than blending them in.

## Report

1. Write a short report: what won and why (with post links), what lost, per-account calls (double down / fix profile / rest), and 3-5 concrete next posts.
2. Persist findings into the strategy and feedback files described in `doublespeed://skills/content-creator` so the next session builds on them.
3. Turn "more of what works" into action with `doublespeed://skills/content-remixer`.

## Notes

- Repeat post and review links in your reply as short descriptive markdown links.
- Numbers come from `get_post_metrics`; never estimate from a sampled page of posts.
