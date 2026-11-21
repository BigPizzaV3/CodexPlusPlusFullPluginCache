---
name: site-performance
description: Report Core Web Vitals and page speed for an OpenRevenue site from real-visitor data. Use when the user asks whether their site is fast, about Core Web Vitals, LCP, INP, CLS, FCP or TTFB, or whether speed changed after a release. Do not use for traffic totals, referrers, funnels, goals, or visitors.
---

# Site performance

Use this skill for Core Web Vitals measured from real visitors on a site the user can access.

1. Resolve `domain` (ask, or call `list_projects` if needed).
2. Call `get_performance` with `domain` and period (`7d` default, or the period the user names). To judge a release, call it for the period before and the period after.
3. The tool returns `avg_lcp`, `avg_inp`, `avg_fcp` and `avg_ttfb` in milliseconds, `avg_cls` as a unitless score, and `sample_count`.
4. Rate each metric against Google's thresholds (good / poor): LCP 2.5 s / 4 s, INP 200 ms / 500 ms, CLS 0.1 / 0.25, FCP 1.8 s / 3 s, TTFB 0.8 s / 1.8 s. Between the two values is "needs improvement".
5. Say that these are averages (Google assesses the 75th percentile), and mention `sample_count` when it is small.
6. Report only metrics the tool returned. Never invent values.

If a tool errors or access is denied, say so and stop.
