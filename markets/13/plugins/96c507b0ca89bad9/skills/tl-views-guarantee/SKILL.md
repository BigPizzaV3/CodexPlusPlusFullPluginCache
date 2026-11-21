---
name: tl-views-guarantee
description: Assess historical YouTube view performance when discussing a creator sponsorship views guarantee. Use for VG, minimum views, bundle size, likelihood to hit, or guarantee negotiation questions.
---

# Views-guarantee data review (MCP)

The CLI skill uses a local script to retrieve historical snapshots and run a reproducible 10,000-draw bootstrap. The MCP has no computation tool for that simulation. Never present a hand-calculated value as the CLI's statistical recommendation.

## Workflow

1. Call tl_whoami, then tl_skill_track with skill="tl-views-guarantee" and stage="started"; retain its run_id. Resolve the channel with tl_channels_find and inspect tl_schema_es, tl_schema_fb, and tl_describe for available view and snapshot fields.
2. Check balance and estimate cost before retrieving historical data. Query only the channel and needed date window; prefer aggregates where supported.
3. If tools expose enough history, summarize sample count, date window, and observed 30-day views. Report spread or percentiles only when they can be computed from returned data. Label the result descriptive, not a bootstrap likelihood or official VG recommendation.
4. If the user needs the CLI-equivalent bundle-size, guarantee, and hit-probability result, explain that this connector cannot compute it yet. Do not invent a probability or guarantee.

Before the final response, call tl_skill_track with skill="tl-views-guarantee", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.


