---
name: amazon-pnl-review
description: Review an Amazon seller's profit and loss in Sotrics and explain what changed, which products made or lost money, and why.
---

Use this when the user asks how their Amazon business is doing, about profit, margin, fees or a P&L.

1. If the user has not said which seller account, call `list_accounts` and use the default account; mention its name.
2. Call `get_sales_overview` for the period the user asked about (default: last 30 days) to get the headline numbers and the previous period.
3. Call `get_profit_and_loss` for the same range with a fitting grain (day for up to 14 days, week up to 90 days, otherwise month).
4. Explain in plain language:
   - sales, net profit and margin, and how they moved versus the previous period;
   - the two or three biggest drivers (fees, refunds, cost of goods, advertising);
   - the products that made the most profit and the products that lost money.
5. If a response says `demo` or sample data, say so. If it says advertising data is not connected, say that advertising costs are not included yet.
6. Never invent numbers that are not in the tool results. Sotrics is read only, so offer analysis, not changes.
