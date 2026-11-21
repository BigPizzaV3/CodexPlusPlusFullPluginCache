---
name: split-receipt-by-category
description: >
  Use when the user shares a receipt (a photo, or a typed/pasted list of
  items and prices) from a single purchase and wants it logged to Kilter
  Money. Covers deciding whether the purchase needs to be split across
  categories at all, how to allocate tax/tip/discounts across split lines,
  and what to do when an item has no matching category yet.
---

# Splitting a receipt by category

A receipt is always **one purchase, one `add_expense` call** — never one
call per item or per category. The only question this skill answers is
whether that one call uses a single `categoryId`/`categoryName` or
`splits`.

## 1. Decide if it needs splitting at all

Most receipts do **not** need splitting. Only split when the items on the
receipt genuinely belong to two or more categories the user already keeps
separate.

- **Single-purpose merchant → never split**, regardless of how many food
  items are on the check. A restaurant, cafe, bar, coffee shop, or
  fast-food order is one `Dining`/`Restaurants`-type category even though
  it lists an appetizer, an entree, and a drink as separate line items —
  those aren't different categories to this user, they're one meal.
  Likewise a gas station fill-up, a single-item purchase, or a pharmacy
  errand for one thing: one category.
- **Multi-purpose merchant → split only if it actually crosses
  categories.** A grocery-store, big-box (Target/Walmart/Costco), or
  pharmacy receipt often mixes groceries, household supplies, pet
  supplies, electronics, or personal care on one ticket. Group the line
  items into however many of the user's *existing* categories they
  actually span (usually 2-3, rarely more) — don't create a split line
  per item, and don't split two items into different categories just
  because they're technically different products (all food/snack/drink
  items on a grocery run are still one `Groceries` line, even if some
  would arguably be "dining").

When in doubt, prefer the simpler read: a single category is always a
valid answer, and splitting when it isn't warranted just adds noise the
user has to review.

## 2. Always call `list_categories` first

Do this before reasoning about category names, whether splitting is
needed, or whether something is "missing" a category — skip archived
categories. Match items to the user's actual category names; don't invent
new category labels in the split without going through step 4.

## 3. Building the split lines

- One split line per category the receipt spans, not per item.
- **Tax and tip/discounts are not their own line.** Fold tax
  proportionally into each category's line based on that line's share of
  the pre-tax subtotal (round each line, then put any rounding remainder
  — usually a cent or two — on the largest line so the lines sum exactly
  to `amountCents`; `add_expense` rejects splits that don't reconcile
  exactly). Net a storewide discount into the affected line(s) the same
  way before allocating tax. A tip (restaurant) doesn't apply here since
  restaurant receipts aren't split in the first place.
- Double check the split lines sum to the receipt total before calling
  `add_expense`. If they don't reconcile, re-check the item grouping
  rather than fudging one line to make the math work.

## 4. An item doesn't fit any existing category

Don't silently force it into the closest existing category, and don't
silently invent a new category. Ask the user, once, naming the specific
item(s): e.g. "This receipt has a pet-supplies item but you don't have a
Pet Supplies category yet — want me to create one for it?"

- **If yes:** call `list_budgets` first.
  - If it returns one or more budgets (budgeting is enabled for this
    account), pick the budget that best matches the new category's theme
    and tell the user which one you'd assign it to before creating it
    (e.g. "I'll put it under your Household budget") so they can redirect
    or say "leave it unassigned" instead. Only ask them to choose outright
    if no budget is a reasonable fit.
  - If `list_budgets` returns empty, budgeting isn't set up on this
    account — create the category with no `budgetId` and don't bring up
    budgets.
  - Then `create_category` with the resolved `budgetId`/`budgetName` (or
    neither), and use the new category in the split.
- **If no:** ask which existing category to fold the item into instead
  (don't guess), or drop that item's amount from the logged expense if the
  user says so.

## 5. Confirm back to the user

After the single `add_expense` call, summarize what was logged in one
short line per split: category and amount (plus merchant/date/total if not
already obvious from context). If the user disagrees with how something
was split, that's a normal category edit in the app, not a reason to
re-log the expense.
