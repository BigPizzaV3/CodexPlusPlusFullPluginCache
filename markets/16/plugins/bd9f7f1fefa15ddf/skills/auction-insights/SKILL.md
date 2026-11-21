---
name: auction-insights
description: Read a Google Ads auction insights export to see which competitors gained or lost share, who is new, and who ranks above you, and connect it to CPC and impression share changes. Use when the user shares an auction insights report or asks who they compete with, why CPCs rose, or whether a competitor is bidding on their brand.
---

# Auction insights

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

Auction insights export from the Campaigns or Keywords view, segmented by Week (or Month) for at least 8 periods: Display URL domain, Campaign, Week, Search Impr. share (Auction Insights), Search overlap rate, Search position above rate, Top of page rate, Abs. Top of page rate, Search outranking share.

## Steps

1. Run `python scripts/ppc.py auction --data <file> [--campaign name] [--window 4] --out auction`.
2. Report, in this order:
   - Your own impression share now and its change.
   - Competitors whose share rose most, and new entrants above 10%.
   - Competitors with high overlap and rising position above rate: they are bidding harder on your queries.
3. Connect to the account: if CPC rose in the same weeks (see `performance-triage`), name the competitor movement as the likely cause, and check lost IS (rank).
4. For brand campaigns: any competitor with meaningful share is bidding on the brand. That is the case for keeping brand ads, and a reason to check trademark policy options.

## Rules

- Values shown as "< 10%" are bounds; the script keeps them out of averages.
- Several campaigns in one export are averaged without impression weights. Filter one campaign, or export at account level, before quoting exact shares.
- Auction insights show who appears, not their spend or results. Do not infer competitor budgets.

## Scripts and references

- `scripts/ppc.py auction`; `references/diagnostics.md`.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
