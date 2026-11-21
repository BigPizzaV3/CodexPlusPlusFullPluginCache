---
name: analyze-website
description: Analyze a public website with Perseo Insights and explain its SEO, performance, security, accessibility and technical findings.
---

Use this skill when the user asks to audit, inspect, diagnose or analyze a public website.

1. Call `analyze_site` with the requested URL.
2. Use `get_analysis_status` until the scan is complete.
3. Call `get_analysis_result` for the structured result.
4. Base every factual finding on data returned by Perseo Insights.
5. Prioritize errors before warnings and explain practical impact.
6. Keep security, SEO, performance, accessibility and technical findings distinct.
7. Link to `report_url` when the result provides one.
8. State that Perseo Insights performs a passive website analysis.

9. If metrics.performance_score differs from performance.pagespeed_score,
   explain that metrics.performance_score is a load-time-only scanner heuristic,
   while performance.pagespeed_score comes from Google PageSpeed/Lighthouse for
   the stated strategy (usually mobile). Never describe the difference as an
   inconsistency or use the scanner heuristic as a replacement for Lighthouse.
10. Treat PageSpeed timings and scanner load_time as different measurements.
11. A word frequent in the body is not automatically a target SEO keyword.
    Recommend keyword-placement changes only for a specifically identified
    search query or an explicitly declared target keyword.
12. Missing FAQ Schema, Speakable markup and question-form headings are
    optional content/AI-readiness suggestions, not universal SEO errors.
13. DKIM lookup probes only common selectors. A negative result is inconclusive;
    if outbound_mail_disallowed_by_spf is true, do not recommend enabling DKIM
    solely because the common selector probe did not find a record.
