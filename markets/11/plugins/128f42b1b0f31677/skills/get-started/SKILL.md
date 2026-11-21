---
name: get-started
description: Use Spliteo to check shared balances, record group expenses with the right split, plan settle-ups, and review personal spending, budgets and savings goals.
---

# Using Spliteo

Spliteo tracks expenses people share in groups (roommates, trips, couples) and the user's own spending, budgets and savings goals. It records money; it never sends or receives payments.

## Look things up before writing

- Resolve a group the user names with `list_groups`, then get its members' `userId`s with `get_group`. Never guess ids.
- When the user names a category, find its id with `list_categories`.
- Use the group's currency unless the user says otherwise.

## Recording a shared expense

`create_group_transaction` describes who paid and who owes as cash flows:

- Each payer has a positive `cashFlow` equal to what they paid.
- Each person sharing the cost has a negative `cashFlow` equal to their share.
- Positive entries add up to the amount, negative entries to minus the amount.
- A payer who also shares the cost appears twice.

Example: the user (A) paid 60 for dinner, split evenly with B and C. Participants are `[A +60, A -20, B -20, C -20]`. `splitConfig` uses `"evenly"` for both sides and lists A as payer, and A, B and C as recipients.

A repayment between members is a transaction with `type: "transfer"`.

## Balances and settling up

- One group: `get_group_balances`.
- Per person across all groups: `get_consolidated_balances`. Overall totals: `get_user_balance_summary`.
- Fewest payments to settle a group: `get_settlement_suggestions`. It only suggests. People pay each other outside Spliteo, and the user can then record each payment as a transfer.

## Personal finance

- A month at a glance: `get_monthly_summary`.
- Budgets: `list_budgets`. Savings goals: `list_goals`, and `contribute_to_goal` to add to one.
- Spending by category over a date range: `get_category_analytics`.

## Changing or deleting

- Before calling an `update_*` or `delete_*` tool, confirm with the user exactly what will change. Deleting a group transaction changes every member's balance and can't be undone.
- After any write, tell the user what was recorded: description, amount, currency, who paid and how it was split.
