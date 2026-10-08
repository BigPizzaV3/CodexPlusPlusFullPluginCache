---
name: halan-portfolio-review
description: Review the signed-in user's Halan Borsa holdings, costs, custodians, and settlement availability, optionally with current EGX prices. Use for portfolio or holding questions; do not use for another person's account or unrelated budgeting advice.
---

# Halan Portfolio Review

1. If the user names particular companies rather than supplying ISINs, resolve them with `search_symbols` first.
2. Call `get_portfolio_details` with the requested ISINs, or with an empty list for the full portfolio.
3. Present each holding's ISIN, total units, average cost, last-updated time, and per-custodian total and settled units. Include settlement-cycle availability only when it helps the user's question.
4. For current valuation or unrealized gain/loss, call `get_stock_quote` for each relevant holding. Label the quote time and currency, show the calculation basis, and do not substitute a missing quote.
5. Explain concentration or diversification using the returned holdings and clearly identified calculations. Keep observations descriptive rather than prescriptive.

Never expose one user's portfolio to another user, guess a custodian or settlement cycle, or imply that holdings changed. This workflow is read-only and does not create an order.
