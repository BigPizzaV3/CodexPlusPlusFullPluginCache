---
name: daily-digest
description: >
  Report everything posted today across all platforms with key engagement
  metrics. Use when the user says "what posted today", "daily recap",
  "today's performance", or similar.
---

# Daily Digest

## Goal
Give a short summary of today's publishing activity and early engagement.

## Workflow

1. **Determine today.** Use the user's known timezone; otherwise ask. Use UTC only when the user accepts it.

2. **Fetch today's posts.** Call `listPosts` and filter returned published posts to today's window. Call `listVideos` and apply the same date and status filter for videos.

3. **Fetch analytics.** Call `getPostAnalytics` for each qualifying post. If metrics are missing or stale, say so rather than guessing.

4. **Check video state.** Call `getVideoStatus` when a video's current publishing state is unclear.

5. **Summarize.** Return:
   - Total items published today and platforms used.
   - Per-platform counts and available views, likes, comments, and shares.
   - The top-performing item, with a short content preview and its raw metrics.
   - Any failures and the error details returned by PostQuickAI.

6. **Offer safe follow-up.**
   - For a confirmed failed video platform, offer `retryVideoPublish` and get approval before calling it.
   - For a failed post, explain that this connector has no post retry tool and direct the user to the dashboard.
   - If nothing was published, offer to prepare tomorrow's drafts; do not schedule without confirmation.

## Never do

- Never extrapolate a trend from one day.
- Never include items outside the selected day.
- Never show percentages without the underlying counts.
- Never invent missing analytics or claim a retry succeeded before checking its result.
