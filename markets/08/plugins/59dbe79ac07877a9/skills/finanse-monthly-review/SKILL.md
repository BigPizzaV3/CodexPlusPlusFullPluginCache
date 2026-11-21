---
name: finanse-monthly-review
description: Use when the user wants a review, recap or check-up of their Finanse budget — "how did this month go", "monthly summary", "compare with last month", "where can I cut", "am I on track" (PL: "jak minął miesiąc", "podsumowanie miesiąca", "gdzie mogę oszczędzić"). One summary card plus a short review with concrete next steps.
---

# Finanse monthly review

Follow the `finanse` skill rules. Default period: the current month; "last month" or a named month replaces it.

## Steps

1. `get_monthly_stats` (silent) with `periods` = the reviewed month **and** the month before, in one call — totals, category split and budget use for both.
2. `show_monthly_summary` with `periods` = the reviewed month — the **only** card of the review.
3. Write the review under the card, never repeating its numbers:

| Section | Content |
|---|---|
| Result | Net and its change vs the previous month in % |
| Watch | Categories over or above 80% of their budget, and the biggest jump vs the previous month |
| Next steps | 1–3 concrete actions, e.g. lower one budget, a category to watch, a repeating cost to automate (offer `show_recurring_suggestions`) |

Keep it under 80 words. Safe-to-spend and upcoming payments only if the user asks (`show_safe_to_spend`, `show_upcoming_transactions` — one card per reply). Never propose moving money or investing — Finanse only records transactions.
