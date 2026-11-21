---
name: performance-report
description: Build social media performance reports with the SocialAPI app. Account, brand and post analytics over a period, follower growth and reach, top posts by engagement and comments, what commenters talk about, and next steps backed by the numbers. Use when the user asks "how did my account perform", "monthly report", "social analytics", "which posts did best", "follower growth", "engagement rate", "compare my platforms", or needs a report for a client.
---

# Performance report

Requires the SocialAPI app in ChatGPT. Every tool name starts with `social_api_`. The `socialapi` skill holds the analytics parameters, series format and error codes: follow it for every call.

## 1. Period and scope

- Dates are `YYYY-MM-DD`, at most 400 days. With no period given, use the last 30 days and state the dates. For a comparison, run the same call on the previous period of equal length.
- One account: `get_account_analytics` (with `page_id` for one Facebook or LinkedIn Page). A client or business with several accounts: `get_brand_analytics` with `brand_id`.

## 2. Read the numbers correctly

- A `gauge` (such as followers) is a level: growth is last value minus first value.
- A `flow` (such as reach) is a per-day count: sum it over the period.
- On a brand, a day with a lower `subjects_counted` had fewer accounts reporting. Call it a gap in the data, not a drop.
- No history yet: say so. Never fill in numbers.

## 3. Posts

- Posts published through SocialAPI: `list_posts` with `from`, `to` and `status: published`, then `get_post_metrics` for each post's current numbers and `get_post_analytics` for its history.
- Posts by comment count, including ones published elsewhere: `list_inbox_posts` with `sort_by: comments`.
- For the top 3 posts, read the comments with `list_post_comments` and sum up the main themes, quoting a few.

## 4. Report

1. Headline numbers with the change against the previous period, in percent.
2. A table per platform or account.
3. Top and bottom posts with their `permalink` and the metric they are ranked on.
4. What the audience talks about.
5. Three next steps, each tied to a number in the report (format, day, topic). Describe correlations, never claim one caused the other.

## 5. Spreadsheet

When the user wants a file, `create_export` for the account, then poll `get_export`. Its download link lasts 15 minutes, so share it as soon as it is ready. The free plan allows 2 exports a month.
