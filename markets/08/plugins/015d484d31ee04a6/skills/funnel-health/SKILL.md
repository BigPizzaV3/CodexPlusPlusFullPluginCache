---
name: funnel-health
description: Report OpenRevenue funnel conversion and drop-off. Use when the user asks about funnels, conversion rates, or where visitors leave a funnel. Do not use for creating or deleting funnels, goals, headline traffic, referrers, or visitors.
---

# Funnel health

Use this skill for read-only funnel conversion and step drop-off on a site the user can access.

1. Resolve `domain` (ask, or call `list_projects` if needed).
2. Call `list_funnels` for that domain.
3. Match the user's funnel name to a `funnelId`, or ask which funnel if ambiguous.
4. Call `get_funnel_report` with `domain`, `funnelId`, and period (`7d` default).
5. Summarize conversion and the weakest step from the report only.
6. Do not create, update, or delete funnels with this skill.

If a tool errors or access is denied, say so and stop.
