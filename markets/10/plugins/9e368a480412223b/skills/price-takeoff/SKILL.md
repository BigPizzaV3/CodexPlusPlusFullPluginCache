---
name: price-takeoff
description: Price the quantities of an Exayard takeoff with supplier prices, cost books and the company's own price lists. Use when the customer asks to price a takeoff, cost out quantities, or build a priced bill of quantities.
---

# Price a takeoff

## Steps

1. **Find the takeoff.** If the customer says "this" or "the selected", call `get_selection` first. Otherwise
   use `list_projects` and `get_project`, then `get_takeoff_summary` to confirm there are measured quantities. If
   there are none, offer to take off the plans first.
2. **Price it.** Call `build_priced_boq`. A small set comes back priced in the turn. A larger one shows a card
   with **Approve**: stop there and let the customer press it. You never start a large pricing run yourself.
3. **Report.** Give the total and the biggest lines. Every price shows where it came from (a supplier, a cost
   book, or the company's own price list); keep that with the number.
4. **Gaps.** If a line has no price, say so and leave it blank. Never invent a price.
5. **Changes.** Lines, quantities, prices and markups are changed in the line items table: the customer presses
   **Open** on the card, or you call `home`.

## Rules

- Prices and totals come only from tool results, in the currency and units in the customer's settings.
- If a step is refused because of the account's plan or its AI usage, pass on the message and its link as given,
  and say nothing more about plans or prices.
- Plain words to the customer: no record ids and no tool names.
