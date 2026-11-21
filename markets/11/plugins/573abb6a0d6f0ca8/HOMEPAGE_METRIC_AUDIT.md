# Homepage median-Yield source audit — 2026-10-02

The owner-supplied v0.1.14 ChatGPT comparison read the [SignalAF homepage](https://signalaf.com/) and noticed that its headline median Yield was 34.45 while the four-degree chart showed Operator Center of Mass Yield 1.90. These are not two estimates of one statistic.

`sigrank-app/app/page.tsx` renders `homeStats.median_yield` in the headline. `getHomepageStats()` in `lib/board/queries.ts` selects `signa_rate` from all-time `metric_snapshots` and stores the median of positive values in `median_yield`. SIGNA-RATE is a retired, distinct metric; labeling this value Yield is an upstream mapping bug. Separately, `FourDegreesChart.tsx` calls `getAverageUsersColumn()`, which takes real all-time board rows and computes the median of their canonical cascade `yield_` values. Its population filters, cache/fallback behavior and update date may also differ from the headline path and the plugin's 22-person claimed-only Active board.

The headline `top_yield` has a separate window difference: `refresh_system_stats()` in migration `20260901200000_0048_refresh_system_stats_yield.sql` selects the latest **30-day** snapshot per operator, then its top canonical Yield. The four-degree top-evaluation column reads the **all-time** board. Do not treat their top values as interchangeable either.

Plugin behavior: use the dedicated MCP's `get_field_stats(window="all", view="total")` for direct Active comparison. The homepage ladder can explain modeled baseline → operator median → top-100 median → top eval as separately sourced context. Do not quote the headline 34.45 as canonical Yield, invent a formula reconciling it with 1.90, or present either as the Active 22-person median.

Remediation identified before PR #177: compute the homepage headline median from canonical per-operator Yield on an explicitly defined cohort/window, or label/remove the legacy statistic. Add a source/cohort/as-of note beside both homepage figures and test that the headline query never reads `signa_rate` for a Yield label. This paragraph records the pre-fix audit; production remediation is documented below.

## Remediation prepared in app PR #177

The homepage headline now reuses the Four Degrees all-time real-operator Yield median. `getHomepageStats()` and `/api/v1/stats` compute Yield from I/O/W/R instead of `signa_rate`, while `llms.txt` labels its separate yieldable-snapshot cohort. The homepage `top_yield` remains a 30-day system-stat value and is labeled accordingly. The live page was verified after deployment with headline and chart median both 1.90; the original 34.45 versus 1.90 observation remains historical evidence, not a current expected result.
