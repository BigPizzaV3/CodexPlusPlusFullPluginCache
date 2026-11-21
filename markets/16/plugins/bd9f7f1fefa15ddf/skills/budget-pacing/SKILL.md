---
name: budget-pacing
description: Check Google Ads monthly budget pacing from a daily cost export. Shows month-to-date spend, run rate, end-of-month forecast and the daily spend needed to land on budget, including regulatory surcharges. Use when the user asks if they will over or underspend, how much to spend per day, or how to adjust budgets for the rest of the month.
---

# Budget pacing

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

- Report by Day with Cost (and Campaign, to pace one campaign or group) for the current month.
- Monthly budget, and whether it includes the regulatory surcharge Google adds in some countries (`references/platform-facts.md`, section on surcharges).

## Steps

1. Run `python scripts/ppc.py pacing --data <file> --budget B [--surcharge S] [--today YYYY-MM-DD] [--campaign name] --out pacing`.
2. Report spend to date, forecast at the last-7-day rate, and daily spend needed.
3. Decide the lever:
   - Underspending and losing impression share to budget: raise daily budgets.
   - Underspending with little lost to budget: budget is not the limit; the target or the reach is. Raising budget will not spend it.
   - Overspending: lower daily budgets by the gap, and remember Google can spend up to twice the daily budget on a single day.

## Rules

- Today's spend is partial and is excluded.
- Change budgets in steps of about 20% or less on Smart Bidding campaigns.
- A forecast from the first days of the month is noisy. Say so before day 7.

## Scripts and references

- `scripts/ppc.py pacing`; `references/bidding-budgets.md`.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
