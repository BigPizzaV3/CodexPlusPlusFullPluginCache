---
name: group-expenses
description: Publish a shared expense page for a trip, a shared house or a group event with create_expense_ledger, then read balances and the settle-up list with show_expense_ledger_results, add expenses with add_ledger_expenses, and delete, add members or close with update_expense_ledger.
---

# Zovo Group Expenses

Use this when a group wants one shared page where everyone adds what they paid and sees who owes whom.

1. `create_expense_ledger`: pass `currency` (ISO code such as EUR, USD, JPY, KWD) and `members` (2 to 30 first names). Add any expenses the user already mentioned in `expenses` (and repayments in `payments`). If the currency or the names are missing, ask one short question.
2. Splits: `split: "equal"` with `split_between` (default: everyone), `split: "exact"` with `parts` as name -> amount, or `split: "shares"` with `parts` as name -> whole-number shares. Amounts are text in the ledger currency, for example "86.50" or "10,000".
3. Reply with both links from the result. Say plainly: share the public link with the group; keep the organizer link private. Then give the balances and the settle-up payments.
4. Later questions ("who owes whom", "what's the total") need the organizer link: call `show_expense_ledger_results` with it. New expenses from the chat go to `add_ledger_expenses`. Deleting an expense (by its number, such as #3), adding a member, renaming, or closing the page go to `update_expense_ledger`.

Do not use this for a one-off bill split that nobody else needs to open, for sending money, or for currency conversion. Names only: do not ask for emails, phone numbers or bank details.
