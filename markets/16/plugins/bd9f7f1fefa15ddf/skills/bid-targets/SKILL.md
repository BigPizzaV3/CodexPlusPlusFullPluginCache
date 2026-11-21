---
name: bid-targets
description: Set Google Ads target CPA or target ROAS from unit economics instead of past results. Calculates break-even and target CPA or ROAS for e-commerce (order value, margin, lifetime value) and lead generation (deal value, funnel rates), adjusted for incrementality. Use when the user asks what tCPA or tROAS to set, whether a target is too high or low, or how much they can pay per lead or sale.
---

# Bid targets from unit economics

Turns business numbers into a target CPA or ROAS the bidder can use, and explains the gap with the current target.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

E-commerce: average order value, gross margin, repeat purchase (lifetime value as a multiple of the first order), profit to keep.

Lead generation: deal or customer value, margin, lead-to-opportunity rate, opportunity-to-win rate, lifetime multiple, profit to keep.

Optional: share of reported conversions that are incremental (from a lift test; default 100%). Current target and current CPA or ROAS.

Ask for what is missing in one message. If the user does not know a rate, use their best estimate and say the result moves with it.

## Steps

1. Run `python scripts/ppc.py targets --order-value V --margin M [--ltv-multiple L] [--profit-share P] [--incrementality I]`, or `--deal-value D --lead-to-opp R1 --opp-to-win R2 --margin M ...` for leads.
2. Show the calculation steps from `steps`, one per line.
3. Compare with the current target and the current results:
   - Target far below break-even: room to scale; raise it in steps of 10% to 20%.
   - Target above break-even: the account buys conversions at a loss at the margin.
4. Remind that the target governs the marginal conversion. Average CPA is below the marginal one.

## Rules

- Never set a target by copying last period's ROAS or CPA. Start from the economics, then watch volume.
- Do not apply margin or LTV twice if conversion values already include them.
- Check whether the campaign uses a portfolio before suggesting a change (`references/bidding-budgets.md`).
- Changes in steps, then wait 1 to 2 conversion cycles (`references/platform-facts.md`).

## Scripts and references

- `scripts/ppc.py targets`; `references/bidding-budgets.md`.
- If code execution is not available, show the arithmetic by hand.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
