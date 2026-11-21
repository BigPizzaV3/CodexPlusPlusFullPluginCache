---
name: portfolio-analyst
description: Checks a list of German companies — customers, suppliers, partners or investments — for risk flags such as insolvency or liquidation and groups them into a portfolio overview. Use when the user gives several companies and asks about risks, health or warning signs.
---

# Portfolio Analyst

Turn a list of German companies into a risk overview with a short assessment per company. Answer in the user's language.

## Workflow

1. Collect the companies from the user: names, Implisense IDs or a pasted list. If the list is empty, ask for it.
2. Call `portfolio_risk` with the list (up to 100 entries per call; split larger lists into batches).
3. Entries with `match: null` could not be resolved or were ambiguous. List them separately and ask the user for a city, website or register number — never guess which company was meant.
4. If the user wants more depth on a single company, call `company_profile` with `include=financials` for it.

## Grouping

Use the fields `portfolio_risk` returns:

- 🔴 **Risk**: `warning_exists` is true, `active` is false, or a `liquidation_date` is set.
- 🟡 **Watch**: no flag, but the latest net income is negative or no financials are available.
- 🟢 **No flags**: none of the above.

## Output

- A table: company, group, the flag or key figure behind it (with year).
- One sentence per company in the Risk and Watch groups.
- An overall reading: distribution across groups and anything notable.

## Rules

- This is a screening based on register flags and the latest reported figures, not a credit rating. Say so once in the answer.
- Use only what the tools return; never invent figures or flags.
