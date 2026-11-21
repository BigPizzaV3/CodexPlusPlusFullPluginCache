---
name: social-performance-summary
description: Use when the user asks for a summary of social media performance (reach, engagement, best posts) for one or more brands over a period.
---

Summarize social performance in a way that is useful for agency reporting. Read-only flow. Reply in the user's language.

1. Call `list_brands`. If the user does not name a brand, ask whether they want a specific one or all brands in the organization.
2. For each brand, call `social_metrics_summary` with `brand_id` and `days` (30 by default). It returns the period's KPIs with the change against the previous period, a breakdown by network and content type, and precomputed insights.
3. Call `social_post_metrics` with `order_by = "engagement"` for the best performing posts (and with `order_by = "reach"` if reach matters).
4. Write the summary:
   - Headline with the key figures (reach, engagement, video views) and their change.
   - Breakdown by network: Instagram, Facebook, LinkedIn, TikTok and YouTube, as connected.
   - Top 3 posts, with links, and why they worked (format, topic, timing).
   - 2–3 actionable recommendations for the next period, backed by the tool's insights.

Rules:
- Make MCP calls one at a time (for several brands, one after another).
- The data comes from daily snapshots, not real time; if a network has no data, say so instead of guessing.
