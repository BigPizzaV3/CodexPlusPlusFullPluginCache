---
name: compare-websites
description: Compare two public websites using completed Perseo Insights analyses and explain their factual differences.
---

Use this skill when the user asks to compare two websites.

1. Start an analysis for each URL with `analyze_site`.
2. Check both jobs with `get_analysis_status`.
3. After both are complete, call `compare_sites` with the two task IDs.
4. Explain the returned metric deltas and finding differences.
5. Do not invent measurements or infer findings not present in the tool output.
6. Preserve uncertainty when a metric is unavailable.
7. Include each report URL when available. 

8. Performance metric deltas relate to the scanner's load-time heuristic;
   do not present them as PageSpeed/Lighthouse differences without distinct
   PageSpeed data for both URLs.

