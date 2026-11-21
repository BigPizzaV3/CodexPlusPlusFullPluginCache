---
name: log-expense
description: Record an expense in FamilyWell Spending, or summarize what the family spent.
---

To record spending, call `spending_add_expense` with the amount, currency if the user gave one, the date (today if not said) and the shop. Leave the category out unless the user named one: FamilyWell guesses it. Without a list, the expense goes to the family's default list.

To answer "how much did we spend", call `spending_get_summary` for the period, or `spending_list_expenses` for the individual expenses.

FamilyWell only records expenses. It never pays, transfers or charges money, so never suggest it can.
