---
name: capital-gains-tax
description: Work out the capital gains tax on a person's sales of shares, funds, crypto, property or other assets for one tax year in one country, from their dates and amounts to the tax owed, and hand them the full calculator with the sales filled in.
---

# Capital gains tax for a tax year

Use this workflow when someone wants to know what they owe on assets they sold, or what they would owe on a sale they are planning.

## 1. Pin down the country and the tax year

- The country is where the seller is taxed on the gain, usually their country of tax residence. A property is also taxed where it stands; if the seller lives elsewhere, work out each country separately.
- Call `get_capital_gains_tax_rules` for the country unless its rules are already in this conversation. Read the calculator's `taxYears` to map what the user said ("this tax year", "2024/25", "last year") to the start year the tools use, and check `assetTypes`, `saleOptions` and `profileOptions`.
- If the country has no calculator (`calculator` is null), answer from its rules tables and questions and link its `pageUrl`.

## 2. Collect each sale

For every sale, get:

- What was sold, mapped to one of the country's `assetTypes` keys.
- The purchase date and the total paid, plus buying costs (commission, stamp duty, legal fees).
- The sale date and the total received, plus selling costs.
- For property, capital improvements.
- Any `saleOptions` the country's rules turn on for that sale (a main home, a qualifying holding size, a business relief). Ask only about the options that could apply to what was sold.

When the user uploads an exchange or broker export (Coinbase, Binance, Koinly, DEGIRO, Trade Republic and similar CSVs), pass the file's full text as `exports`; for any other list of buys and sells, pass each trade as `transactions`. Either way, include every buy back to the first one, since the country's matching rules (the UK's 30-day rule and pool, Canada's average cost) depend on them. Use the amounts in the country's own currency. When the user gives quantities and unit prices, multiply them out. When a sale was split across several purchases, enter one sale per purchase lot.

## 3. Collect the year's context

- When `incomeAffectsTax` is true and the user has said their income for the year, pass it as `annual_income`. When they haven't, calculate without it: the result uses the country's median income, and the card has an income field they can change.
- Pass unused losses from earlier years as `prior_year_losses` when the country carries losses forward.
- Set `profileOptions` that differ from their defaults (residency, filing status, state).

## 4. Calculate

Call `calculate_capital_gains_tax` with every sale of the tax year in one call. Sales in other tax years belong in separate calls, one per year.

If the result's `income.assumed` is true, tell the user the tax is worked out on the country's median income and ask for theirs: they can type it into the card, or give it to you and you call again with `annual_income`. If the result has `incomeNeeded`, ask for the income and call again. If it returns an error naming a field, fix that field and call again.

## 5. Answer

- Lead with the tax owed for the year, then walk through the `steps` in order, naming each allowance, exemption and loss used.
- Mention any sale marked exempt and why (its `note`).
- Pass on the `checks`: they tell the user what to report and when.
- Give the `calculatorUrl`. It opens the full calculator on capitalgainstax.net with these sales filled in, where the user can adjust them, import broker files and download the summary for their return.
