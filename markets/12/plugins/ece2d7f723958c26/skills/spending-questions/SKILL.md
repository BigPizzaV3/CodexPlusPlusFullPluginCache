---
name: spending-questions
description: Answers questions about the person's spending and receipts in Receiptix — how much went where, in a month, on a trip or in a shared project, at a shop or on a category, compared with before — and finds a receipt by what was bought, where, or when. Use when they ask about money they spent, a purchase, a receipt, a bill, a trip's cost, or who paid what.
---

# Spending questions in Receiptix

Receiptix holds the person's receipts: photos, PDFs, forwarded emails and typed or spoken entries,
each read into a merchant, a date, line items with categories, and a total in the receipt's own
currency. Receipts live in their personal space or in projects — trips, households, shared budgets
— some of them shared with other people.

## Figures come from get_spending

- Any total, split or comparison — "how much on groceries in September", "by month this year",
  "did we eat out more than last month" — is one `get_spending` call. It converts every receipt at
  the app's rates and counts each line under its own category, exactly as the app's reports do.
- Never add up receipts from a listing yourself: amounts sit in different currencies, and a receipt
  can mix categories.
- A question about a trip, a household or "we" is about a project: find it with `list_projects`
  first, then pass its id.
- Say which space or project a figure is for, and in which currency. When some receipts could not
  be converted, or are still being read, say so.

## Finding receipts

- By what was bought, where, or what it was for — "the headphones", "that dinner in Lisbon" —
  use `search_receipts`; it matches meaning as well as exact words.
- By date, merchant, category, tag, who paid or amount — use `list_receipts` with a filter.
- For the lines, tax, the text read from the receipt or its original file, use `get_receipts`.
- When nothing matches, say so plainly, and suggest a different word, a wider period or another
  project. Never invent a receipt, a price or a date.

## When the view is on screen

The person sees Receiptix's view with the figures or receipts. Answer the question in a sentence or
two — the number they asked for, or what stands out — rather than repeating the view.

This connection only reads. Receipts are added and changed in the Receiptix app.
