---
name: tl-channel-authenticity
description: Review available YouTube channel and video performance evidence for unusual patterns before or after a sponsorship. Use to vet a channel or investigate suspicious views, engagement, or delivery.
---

# Channel evidence review (MCP)

This connector supports a bounded data review, not the full CLI authenticity audit. It lacks the local comment scraper, anomaly-scoring scripts, and some peer-cohort checks. Never label a creator fraudulent or claim bot activity from one metric.

## Workflow

1. Call tl_whoami, then tl_skill_track with skill="tl-channel-authenticity" and stage="started"; retain its run_id. Resolve the channel with tl_channels_find. Confirm the record if multiple candidates appear.
2. Inspect tl_schema_es, tl_schema_fb, and tl_describe to learn which fields are exposed. Check tl_balance and use query dry-run pricing before broad searches.
3. Use narrowly scoped tl_db_es and, where schema supports it, tl_db_fb queries to review upload cadence, views over time, and available metrics. Compare like with like by format, age, and period; report sample size and date window.
4. Separate observed anomalies from benign explanations. If comments, demographics, or a valid peer cohort are unavailable, state that those checks were not performed.
5. Give a calibrated result: no clear anomaly in checked data, needs further review, or notable anomaly. Do not give a definitive authenticity verdict.

Do not run unbounded transcript searches. Do not claim comment analysis, screenshot-demographics review, the CLI scoring rubric, or a complete integrity audit unless the relevant data was actually available and checked.

Before the final response, call tl_skill_track with skill="tl-channel-authenticity", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.

