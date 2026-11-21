---
name: reporting-best-practices
description: Build a marketing performance report with Toffu: KPI hierarchy, cadence and an executive summary. Use when the user asks for a weekly, monthly or client report, or how to structure one.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

Give the report in the chat, with tables. There is no dashboard or file output here.

# Marketing Reporting & Dashboard Design

## KPI Hierarchy
Structure metrics in three tiers:
- **North Star Metric**: the single metric most correlated with business success (e.g., MRR, revenue, activated users).
- **Primary KPIs** (3-5): directly influence the north star. Examples: CAC, ROAS, conversion rate, LTV.
- **Secondary KPIs** (5-10): operational metrics that influence primaries. Examples: CTR, CPC, email open rate, bounce rate.

Report top-down: north star first, then drill into primaries and secondaries only to explain changes.

## Reporting Cadence
- **Daily**: automated alerts on anomalies (spend spikes, conversion drops, site errors). No manual reports.
- **Weekly**: channel performance summary. Focus on trends vs prior week and targets.
- **Monthly**: full performance review. Include MoM and YoY comparisons, campaign-level analysis, budget reconciliation.
- **Quarterly**: strategic review. Attribution analysis, incrementality results, budget reallocation recommendations, competitive landscape shifts.

## Dashboard Layout Principles
- **Top row**: north star metric + primary KPIs with trend indicators (up/down arrows, % change).
- **Middle section**: channel breakdown table or chart. Sortable by key metrics.
- **Bottom section**: detailed views — campaign performance, audience segments, content performance.
- Use consistent date ranges. Default to last 30 days with comparison to prior period.
- Limit to 1 page (or 1 scroll) for executive dashboards. Detail dashboards can go deeper.

## Data Storytelling
- Don't just present numbers. Answer: **what happened, why, and what we're doing about it**.
- Lead with the insight, not the data. "Conversion rate dropped 15% because landing page load time doubled after the deploy on March 3rd" — not "here's a chart of conversion rate."
- Use annotations on charts to mark events (launches, outages, seasonal peaks).

## Anomaly Detection
- Set thresholds for automated alerts: any metric moving > 20% from trailing 7-day average.
- Investigate anomalies within 24 hours. Most are data issues or external factors — catch real problems fast.
- Track false positive rate. Tune thresholds to minimize alert fatigue.

## Benchmark Setting
- Set benchmarks from: historical performance (trailing 90-day average), industry data, or competitor analysis.
- Update benchmarks quarterly. Stale benchmarks lose relevance.
- Report performance vs benchmark, not just raw numbers. Context makes data actionable.

## Executive Summary Format
Every report starts with a 3-5 sentence executive summary:
1. Overall performance vs target (on track / ahead / behind).
2. Biggest win this period.
3. Biggest risk or underperformance.
4. Key action items for next period.
