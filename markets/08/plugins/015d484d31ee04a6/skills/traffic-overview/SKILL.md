---
name: traffic-overview
description: Summarize OpenRevenue site traffic with headline stats and an optional timeseries. Use when the user asks how a site is doing, for traffic this week or month, or for a high-level analytics overview. Do not use for referrers, funnels, goals, visitors, or performance.
---

# Traffic overview

Use this skill to summarize traffic for a site the user can access in their linked OpenRevenue account.

1. If the domain is unclear, call `list_projects` and ask which site to use.
2. Call `get_project_stats` with `domain` and period (`7d` default, or the period the user names).
3. Optionally call `get_timeseries` for the same domain and period when they want a trend.
4. Answer only with numbers returned by the tools. Never invent metrics or project IDs.
5. Prefer the site domain (for example `example.com`).

If a tool errors or access is denied, say so and stop.
