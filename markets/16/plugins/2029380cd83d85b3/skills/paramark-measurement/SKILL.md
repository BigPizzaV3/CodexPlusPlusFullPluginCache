---
name: paramark-measurement
description: Answer questions about a customer's marketing measurement in Paramark, using the Paramark MCP tools. Use when the user asks what their marketing drove, how channels compare on incremental contribution, cost per incremental outcome or ROAS, what their Marketing Mix Modeling (MMM) or Live MMM results show, which reports they have, what an experiment was designed to detect or measured, or what they spent and measured. Do not use for general marketing questions that need no account data.
---

Use this skill when the user wants numbers from their own Paramark account.

## Steps

1. Call `whoami` once per conversation to learn which customer the connection is scoped to. Every other tool reads that customer's data.
2. For the full history of a model, call `list_mmms`, then `get_mmm_report` for the MMM the user means; it returns the newest published report unless you pass a `refresh_month` and `refresh_year` from `list_mmm_reports`. `summary_data` is the per-channel view of the summary window and answers most "which channel" questions without re-aggregating; `channels_data` is the same per period.
3. For what has happened since the published report, call `get_live_mmm_output_since_refresh`. It returns only the periods after `source_data_end`. Rows with `is_partial` true are incomplete periods; say so when quoting them.
4. For the inputs behind a model, call `get_media_data` (spend and impressions per channel) or `get_target_metrics_data` (the target metric over time). State the window you asked for.
5. For "what reports do I have", call `list_mmms` then `list_mmm_reports` for each MMM, and give the `report_url` links it returns.
6. For experiments, call `list_experiment_designs` then `get_experiment_design` for the power curve (the probability of detecting a causal effect at each lift), or `list_experiment_results` then `get_experiment_results` for the measured lift. `measured_impact.runs` holds the absolute lift on the target per published run; pass `include_time_series` only when the user asks for the daily series.

## Vocabulary

- `incremental` is a channel's contribution to the target metric, in the target's units. `metadata.target_metric` names the target. Call it incremental contribution, not a prediction or a forecast of anything.
- `channel` is a series. The `baseline` row is what the target would have been without marketing; leave it out when ranking channels.
- `cpa` is cost per incremental outcome and `roas` is incremental return on ad spend. Either is null when the channel's contribution is too small to divide by, so report that rather than a number.
- `total_data` sums baseline and all channels per period and carries `actual`, the measured target, beside `incremental`.
- Write in sentence case and say "forecast", never "predict". Spell out Marketing Mix Modeling (MMM) on first use.

## Rules

- Quote only values the tools returned. Never estimate a channel's contribution, spend or efficiency from memory or from another channel's numbers.
- When a tool reports that something was not found or the window is out of range, say so and offer the nearest thing it can do. Do not retry with guessed ids.
- Round to what a marketer reads: whole currency amounts, one decimal for ratios, and the period labels the data uses.
- The tools are read-only. If the user asks to change a model, a report or a plan, say that this plugin cannot and point them to the Paramark dashboard.
