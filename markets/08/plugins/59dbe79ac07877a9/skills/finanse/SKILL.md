---
name: finanse
description: Use for ANY question or task about the user's Finanse budget — spending, income, categories, category budgets, balance, safe-to-spend, recurring payments, savings goals, searching transactions, or recording, editing and deleting expenses, incomes and shop receipts (PL: wydatki, przychody, budżet, saldo, paragon, płatność cykliczna, cel oszczędnościowy). Picks the right Finanse tool, batches calls and keeps every write behind the user's approval.
---

# Finanse

Finanse records money the user **already** spent or received. It never sends, pays, transfers or invests money, never connects to a bank and never asks for card details. Say "record", never "pay".

## Cards vs. silent lookups

`show_*` tools and every write render a card in the chat. Every other tool is a **silent lookup** — the user sees nothing.

- **One card per reply.** Call a `show_*` tool only when the user asks to see that thing. Never call one to look something up.
- **The card is the answer.** After a card, write at most one short sentence. Never re-list its rows, amounts, category, account or date, and never draw your own summary card, table or bullet list of it.
- **No card before a write.** Adding one expense renders exactly one card: the saved transaction.

## Pick the tool

| User asks | Tool | Card |
|---|---|---|
| Which budgets/projects do I have, switch project | `list_projects` | — |
| Account ids, the default account, today's date | `list_accounts` | — |
| Category ids (before any write) | `list_categories` | — |
| Rows as data — recategorise, ids to edit/delete, duplicates, counts, merchant totals | `find_transactions` | — |
| Numbers to reason with — totals, category split, budget use, month vs month | `get_monthly_stats` | — |
| Show my accounts / balances | `show_project_overview` | ✅ |
| Show where the money went in a month | `show_monthly_summary` | ✅ |
| Show every transaction in a month | `show_transactions` | ✅ |
| Show transactions matching a note ("paliwo", "Netflix") | `show_search_results` | ✅ |
| Show how my balance moved | `show_balance_history` | ✅ |
| Show my budgets | `show_budget_status` | ✅ |
| How much can I still spend | `show_safe_to_spend` | ✅ |
| What payments are coming | `show_upcoming_transactions` | ✅ |
| What repeats / what could be automated | `show_recurring_suggestions` | ✅ |
| Record one expense or income | `list_categories` (+ `list_accounts` if an account is named) → `create_transaction` | ✅ saved |
| Record several | `list_categories` → `create_transactions` | ✅ saved |
| A shop receipt / paragon / photo of a bill | `list_categories` → `create_receipt_expenses` (never `create_transaction(s)`) | ✅ review |
| Set up a recurring payment | `list_categories` → `create_recurring_transaction` | — |
| Change one / many transactions | `find_transactions` → `update_transaction` / `bulk_update_transactions` | ✅ preview |
| Delete transactions | `find_transactions` → `delete_transaction` | ✅ preview |
| Savings goals, contributions, "when will I reach X" | `get_savings_goals`, `allocate_funds`, `simulate_savings_timeline` | — |

## Rules

1. **Project** — omit `projectId` unless the user names another budget; then resolve it with `list_projects`.
2. **Categories before writes** — call `list_categories` first and use a real category. Expense vs income follows the category, never the sign of the amount. No fitting category → ask which one; never invent it.
3. **One call per batch** — tools taking `periods`, `queries`, `transactionIds`, `updates` or `items` get the whole batch in one call. Never loop month by month or item by item.
4. **Two-step writes** — `update_transaction`, `bulk_update_transactions`, `delete_transaction` and `create_receipt_expenses` first return a preview card with buttons. Ask for approval in one sentence; if the user approves in chat, repeat the call with the returned `confirmationToken`. Never confirm on the user's behalf.
5. **Notes in the user's style** — `list_categories` returns the user's recent notes; every note you write (`notes`) matches their length and detail. A receipt's `categoryNotes` are the exception: `Merchant: kinds of items` — 1–3 generic item types per category (`Action: lampy robocze`), never the merchant alone and never one entry per line.
6. **Dates are wall clock** — `2026-09-17T17:20` as the user reads it, never a `Z` instant. Resolve "yesterday" against `today` from `list_categories` or `list_accounts`. A receipt's `purchasedAt` needs the time printed on it.
7. **Many rows never go to a card** — "move every Netflix from the last 6 months to Subscriptions" is `find_transactions` → `bulk_update_transactions`; the only card is the preview. `show_transactions` hands you counts, not rows.
8. **Refusals are final** — no project, no subscription or a `restricted` role: relay the tool's message plainly. Never link to checkout or mention prices.
