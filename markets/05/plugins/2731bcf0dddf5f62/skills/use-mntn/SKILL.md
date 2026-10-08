---
name: use-mntn
description: Use MNTN Performance TV tools for advertiser discovery, campaign reporting, audience planning, campaign management, and carefully confirmed budget or delivery changes.
---

# Use MNTN

Work only within the connected user's MNTN permissions. Start by resolving the advertiser when the request does not identify one, and never guess an advertiser ID.

## Read and analyze

- Read the relevant advertiser, campaign, audience, flight, or creative before proposing a change.
- For reporting, call `get_reporting_metadata` before `run_report` so the requested tables, metrics, and dimensions are valid.
- Treat segment rows as overlapping audience observations, not additive account totals. Use Graph metrics for account totals.
- Explain material filters, date ranges, and attribution choices in the result. Use last-touch metrics only when the user asks for last-touch reporting.

## Change MNTN state

- Make changes only when the user's request clearly authorizes them. A request to inspect, analyze, recommend, or draft does not authorize a write.
- Before launching, pausing, replacing or boosting a budget, or changing an active flight budget, show the exact campaign, schedule, amount, and likely effect. Obtain explicit confirmation before the committing call.
- Treat preview or dry-run output as a proposal. If a commit requires a preview token or acknowledgement value, preserve the reviewed inputs exactly; preview again if they change.
- Creating or cloning a campaign does not make it deliver: it still needs an explicit budget and launch. Do not imply otherwise.
- Do not claim that MNTN can upload creative through this plugin. It can inspect existing creatives and attach supported existing creative records.

## Feedback

Before calling `submit_feedback`, show the exact report that will be sent to MNTN and obtain explicit confirmation. Do not add identity fields; attribution comes from the authenticated connection.

When a tool refuses access, lacks a scope, or requires reauthorization, explain the returned requirement and let the user decide whether to continue. Never work around authorization controls.
