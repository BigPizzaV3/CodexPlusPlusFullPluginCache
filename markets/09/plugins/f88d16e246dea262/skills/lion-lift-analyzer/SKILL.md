---
name: lion-lift-analyzer
description: Review progress and training trends over a given period (days, weeks, or months) across any combination of swim, bike, run, and lift. Use when the user asks for an analysis, review, or summary of their training over a time range, for one sport or all of them.
---

# Analyze training over a period

Analyze completed training across the sports and time range the user asks about, and explain what the data actually shows — trends, balance, consistency, standout sessions — not just a restated list of numbers.

## Scope the analysis

- Resolve the exact date range and which sports to include (swim, bike, run, lift, or any combination — default to all four if the user doesn't say). Confirm an ambiguous range ("last month," "this training block") against today's date rather than guessing a boundary.
- Use `list_collections` / `list_fields` to confirm the current schema if anything is uncertain. Use `fetch_records` with `start_date`/`end_date` and `status` `completed` for each relevant sport's own collection (`lifts`, `run`, `bike`, `swim`); widen the range slightly around local-day boundaries since dates are stored in UTC.
- If a `goals` collection exists, pull relevant weekly targets as context for whether training volume matched intent — don't treat a goal as a requirement the user is being graded against.

## Check for the context that actually changes the conclusion

- If a `dailyLog` collection exists, check relevant sleep and work entries for the same period. If short sleep or a heavy work stretch overlaps a dip in training volume or performance, describe it as a possible contributing factor, not a proven cause.
- Use only available Lion Lift read tools for athlete context. If age, height, weight, sex, or training experience would materially change an interpretation, ask the user directly; never guess or imply these details were retrieved from a profile tool.
- Note any other real gap in the data (missing heart rate, a sport with too few sessions to say anything meaningful) rather than filling it in.

## Draw real conclusions

- Look for actual patterns: volume trend up or down, consistency (sessions per week, gaps), whether hard efforts cluster or spread out, balance across the requested sports, and any standout session (a clear best/worst effort, a notable jump or drop).
- Distinguish a real trend (several sessions moving the same direction) from a single outlier session — don't call one unusually good or bad session a trend.
- Tie conclusions to specific sessions and dates as evidence, not just an aggregate average.

## Present the analysis

- Lead with the clearest two or three takeaways, then the supporting detail per sport. State the exact date range and which sports were included.
- Call out explicitly, near the top, any contributing factor found in the sleep/work logs or any missing context (age/height/weight, or missing performance data) that limits how confidently a conclusion can be drawn.
- This skill only reads and analyzes. Never call a scheduling tool from here.
