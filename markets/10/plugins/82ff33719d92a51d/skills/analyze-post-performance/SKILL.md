---
name: analyze-post-performance
description: >
  Pull social media analytics for a post, content group, or time range and
  summarize performance. Use when the user says "how did my posts do",
  "analytics", "which post performed best", "engagement rate", or asks about
  specific metrics such as views, likes, comments, or shares.
---

# Analyze Post Performance

## Goal
Give the user a clear, accurate summary of their social performance.

## Workflow

### For a specific post

1. Reuse a known post ID, or call `listPosts` to locate the post without guessing.
2. Call `getPostAnalytics` for that post ID.
3. Return the available totals and per-platform metrics. Include trends or engagement rates only when the tool returns them.

### For posts in a time range

1. Reuse the known content group. If the brand is missing or ambiguous, call `listContentGroups` and ask the user to choose.
2. Call `listPosts` and filter the results to the requested period, such as this week or the last 30 days.
3. Call `getPostAnalytics` for each qualifying published post.
4. Summarize available totals, top posts, platform differences, content types, and daily changes. State when a platform provides no metrics.
5. Finish with one or two observations grounded in the returned data.

### For content-group totals

Call `getGroupAnalytics` when the user specifically asks for aggregate content-group analytics. Use the closest supported period and state the period used.

### Across brands

Use `getAnalyticsOverview` for an account-wide comparison. State its returned period and filters. Do not present a limited overview as a complete history.

## Data freshness

Use freshness information returned by the tools. When the user requests new metrics, call `refreshAnalytics`; honor its cooldown and report errors or skipped items. A refresh does not guarantee every platform supplied current metrics. If analytics are stale, say so; never state a fixed refresh interval unless the tool reports one.

## Never do

- Never invent missing numbers.
- Never compute a rate differently from the API's returned definition.
- Never treat unavailable metrics as zero.
- Never answer from memory when current analytics can be fetched.
