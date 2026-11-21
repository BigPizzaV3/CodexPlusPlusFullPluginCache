---
name: change-history-review
description: Review a Google Ads change history export to find the changes that explain a performance shift and the risky ones, such as target changes inside the calibration window, large budget swings, bid strategy changes, auto-applied recommendations and edits to conversion goals, networks or locations. Use when the user shares change history or asks what changed, who changed it, or whether a change caused a drop.
---

# Change history review

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

Change history export (Tools, Change history, Download) for the period around the performance change, ideally 4 weeks before it to 2 weeks after.

## Steps

1. Run `python scripts/ppc.py inspect --data <file>` to confirm the date range, then `python scripts/ppc.py changes --data <file> [--big-change 0.2] [--learning-days 14] --out changes`.
2. If the user has not shared performance data, ask for the campaign report by Day for the same period (see `performance-triage`). Without it, report the risky changes but do not name a cause.
3. Read `net_changes` (where a setting ended after several steps), then `flags` from high to medium:
   - Targets changed again before the bidder calibrated: results in between cannot be read.
   - Steps above 20% in targets or budgets.
   - Bid strategy changes.
   - Auto-applied recommendations.
   - Conversion goal, network and location changes.
4. Put the flagged changes on the performance timeline. A change is a candidate cause only if it precedes the shift and fits its direction (a lower tCPA cuts volume, a broader match type lowers conversion rate).
5. Look for typos in values: a target or budget off by a factor of 10 or 100 for a short time is common and costly.

## Output

- The timeline of material changes (targets, budgets, strategy, status), one line each.
- Flags with severity and why they matter.
- Which change most likely explains the performance shift, with the evidence, or "none of these" if nothing lines up.
- Process advice when the pattern is frequent edits: batch changes, wait 1 to 2 conversion cycles, keep a change log.

## Rules

- Change history can miss some changes (some shared library edits). Absence is not proof.
- Do not blame a person. Describe the change and its effect.

## Scripts and references

- `scripts/ppc.py changes`; `references/principles.md`, `references/bidding-budgets.md`.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
