---
name: yield-clarity
description: Answer questions about the person's Yield Clarity financial plan (net worth, holdings, spending, forecast, financial independence date, what-ifs, Monte Carlo odds, portfolio history) using the Yield Clarity tools.
---

Use the Yield Clarity tools when the person asks about their own finances as recorded in Yield Clarity.

Choosing a tool:

- Start with `get_plan_overview` for general questions. If the person has several plans or names one, call `list_plans` first and pass its `planId`.
- `get_holdings` for individual investments, accounts, pensions and property; `get_expenses` for planned spending; `get_portfolio_history` for how things have changed.
- `get_forecast` for the projected financial independence (FI) date and the year-by-year path.
- `what_if` for hypothetical changes (saving more or less, a different retirement date, return or inflation, extra one-off or recurring costs or income, or switching saved decisions on or off). It compares with the current plan and saves nothing.
- `run_monte_carlo` for probabilities. It takes up to about 20 seconds.
- `list_decisions` for the what-if decisions the person has saved in the app.

Presenting results:

- Quote amounts in the plan's currency, as returned. Say "projected" or "estimated" for forecasts: they depend on the person's own assumptions.
- Forecasts cover the portfolio counted towards FI; net worth also includes property and other assets. Don't mix the two.
- If a tool says the account or plan lacks access to a feature, pass that on plainly.
- These tools can't change the person's plan. If they want to make a change, tell them to do it in the Yield Clarity app.
