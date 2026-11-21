---
name: performance-triage
description: Explain why Google Ads performance changed between two periods from a report export. Splits the change in CPA, ROAS or conversions into demand, impression share, CTR, CPC and conversion rate, by segment (brand, non-brand, PMax, app, upper funnel), and separates mix shift from real change. Use when the user asks why CPA went up, why conversions dropped, or what happened to their account, and can share a campaign report with a Day or Week column.
---

# Performance triage

Turns a "why did it change" question into arithmetic, then into a short diagnosis with the next check.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

A campaign report exported from Google Ads with a time segment. Ask for exactly this if it is missing:

- Segment: Day (or Week), covering both periods.
- Columns: Campaign, Campaign type, Impr., Clicks, Cost, Conversions, Conv. value (if value matters), Search impr. share, Search lost IS (rank), Search lost IS (budget).
- In the interface: Campaigns view, set the date range to cover both periods, add the columns, segment by Day, download as CSV or Excel.

Also ask for the two periods to compare. Default: the last 28 complete days against the 28 before.

## Steps

1. Run `python scripts/ppc.py inspect --data <file>`. Check the date range and the segments. If brand campaigns are not detected, ask how they are named and pass `--brand-regex`.
2. Run `python scripts/ppc.py triage --data <file> --a <start:end> --b <start:end> --out triage`.
3. Read `references/diagnostics.md`, then the output:
   - `mix`: how much of the account CPA change is mix shift between segments.
   - Per segment: `change`, `cpa_explained_by`, `conversions_explained_by`, `verdict`.
   - `warnings`.
4. Ask for the change history of the period if the cause points at the account (targets, budgets, pauses, new campaigns), and match dates.
5. If conversions lag (leads to sales, trials to paid), say whether the latest days are mature before reading conversion metrics.

## Output

- First line: what moved, by how much, and the main cause, for the segment that matters most (usually non-brand).
- The values table (before and after, per segment) and the changes table from `triage.md`, including the day the shift starts when one is found.
- The diagnosis per segment that moved, in one or two lines each.
- The next check, and the action if the cause is already clear.

## Rules

- Never report an account-level CPA change without the mix split and the segment view.
- Few conversions (under about 30 in a period) means ratio changes are noise. Say so.
- Do not name a cause the numbers do not show. "Demand fell" needs eligible impressions; "auction got expensive" needs CPC with CVR flat.
- Platform facts only from `references/platform-facts.md`.

## Scripts and references

- `scripts/ppc.py` (pandas, numpy). Handles Google Ads exports in English and Spanish with preamble and totals rows; other languages via `--map '{"Kosten": "cost"}'`.
- If code execution is not available, give the user the command to run locally.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
