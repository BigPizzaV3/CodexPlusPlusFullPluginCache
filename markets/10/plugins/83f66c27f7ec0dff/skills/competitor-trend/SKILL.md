---
name: competitor-trend
description: Show how a brand's AI visibility has developed over time and how it ranks against the competitors it tracks in 3RD. Use when the user asks about trends, development, momentum, or who is ahead of them.
---

Use this skill for questions about change over time and position against competitors.

1. Call `list_brands` and take the `brandId`. Ask which brand if there are several and the user named none.
2. Call `get_visibility_trend` with `days` set to the period the user asked for (default 30). It returns one visibility score per day.
3. Call `get_competitor_ranking` with the `brandId`. Pass `fromDate` and `toDate` (YYYY-MM-DD) for the same period as the trend; without them it covers the last 30 days.
4. Answer with:
   - how the series moved: the first and last value, the highest and lowest day, and any sharp change;
   - the brand's rank and score, and the competitors ranked above and just below it;
   - the period each part covers.

Report scores exactly as returned. Only compare against competitors that `get_competitor_ranking` returns; to see or change the tracked list, the user can call `list_competitors` or use the 3RD app. Do not explain a movement unless a tool result supports the explanation.
