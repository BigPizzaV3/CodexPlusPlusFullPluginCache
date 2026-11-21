---
name: local-seo
description: Use when the user asks about a brand's local SEO or Google Business Profile listing: views on Google Maps and Search, calls, direction requests, reviews or map rankings.
---

Analyze a brand's local presence on Google. Read-only flow. Reply in the user's language.

1. Call `list_brands` and confirm the brand.
2. Call `gbp_overview` with `days` (7–90, 30 by default): views on Search and Maps, website clicks, calls, direction requests, a review summary and the keywords people use to find the listing, with the change against the previous period.
3. Call `gbp_reviews` with `only_unanswered = true` for reviews awaiting a reply (or without the filter to see the latest ones).
4. Call `gbp_geogrid` for map rankings per keyword: average position, % of grid points in the top 3 and the trend. It is an estimate (requires the Growth or Pro plan).
5. Write the analysis:
   - Visibility and customer actions, with the change.
   - Reviews: average rating, volume, unanswered ones and recurring themes. If the user asks, draft replies for them to post.
   - Map rankings: where the brand is strong and where it is weak.
   - Prioritized actions (reply to reviews, complete the listing, post updates, work on weak keywords).

Rules:
- Make MCP calls one at a time.
- The connector does not reply to reviews or edit the listing: the user posts the draft replies.
- The data comes from the nightly sync; if a tool says a connection or plan is missing, explain it.
