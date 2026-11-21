---
name: get-started
description: How to work with Tensai Plan, the money planner, through its connector. Use when the person asks to record income or expenses, check balances, budgets or spending, or manage their Tensai Plan projects.
---

# Working with Tensai Plan

Tensai Plan keeps a person's income and expenses in **projects** (personal, household, business). Each project has one or more **currencies**, and every currency is its own ledger with its own balance.

1. Start with `list_projects`: it gives the connected projects, their currencies, today's date and what the person may do in each. When several projects are connected and the person has not said which one, ask.
2. Before recording a movement, look at `list_categories` and pick the category that fits; if none clearly fits, ask.
3. Amounts are major units (12.5 is twelve and a half) and dates are `YYYY-MM-DD`. Never invent an amount or a date the person did not give; ask.
4. Never convert between currencies or add amounts of different currencies together. An exchange (`create_exchange`) always uses the two amounts the person gives.
5. For several movements at once use `create_transactions`.
6. Confirm with the person before deleting anything.

Useful reads: `list_balances` (balance per currency), `spending_summary` (spending per category over a period), `list_budgets` (budgets of a month and how much is used), `list_transactions` (search by date, category, currency or text).
