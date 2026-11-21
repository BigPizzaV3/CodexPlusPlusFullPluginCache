---
name: cap-table
description: Model startup dilution with a cap table calculator and SAFE calculator. Use calculate_cap_table for a pro-forma cap table before and after SAFEs, convertible notes and a priced round with an option pool top-up, with Excel and PDF files; use calculate_safe_ownership for a quick investment / post-money cap check.
---

# Zovo Cap Table Calculator

Use `calculate_cap_table` when the user describes current holders and a next event: SAFEs, convertible notes, and/or a priced round. Use `calculate_safe_ownership` for "how much does a $X SAFE at a $Y cap buy".

1. Pass every current holder in `holders` with shares, fully diluted: founders, granted options, the unallocated option pool (name it "Option pool" or set `kind: "pool"`) and prior preferred rounds. Text like "Alice 4.5M; Bob 4.5M; Option pool 1M" also works.
2. SAFEs: `amount`, `valuation_cap`, `discount` (percent), `type` (`post` is the YC default, `pre` for a pre-money SAFE), `mfn`. List SAFEs in the order they were issued so MFN terms come from later SAFEs.
3. Notes: `principal`, `interest_rate` (simple, percent), `issue_date`, `valuation_cap`, `discount`. The conversion date defaults to `round.date`, else today.
4. Priced round: `round.pre_money_valuation` (or `post_money_valuation`), `round.new_money`, optional `round.target_pool_percent` (unallocated pool after the round as a % of post-money fully diluted shares; the top-up goes in the pre-money), optional `round.investors`.
5. If the user gives the data, call right away. Ask one short question only when the share counts are missing; percentages alone can be modeled with 10,000,000 total shares if the user agrees.
6. After the result, give the price per share, each instrument's conversion price and which price applied (cap or discount), founders' ownership before and after, the Excel and PDF links, and the note that this is an illustrative model, not legal or tax advice; the real documents govern.

Do not use it for valuation advice, legal drafting, 409A valuations, tax questions or lab dilution (mg/mL) math.
