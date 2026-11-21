---
name: check-price
description: Look up what the company's own suppliers charge for a product in its Exayard catalog, lowest first. Use when the customer asks what their suppliers charge, for the best price on a product, or to check a price on a quote.
---

# Check a price

## Steps

1. **Find the product.** If the customer says "this" or "the selected", call `get_selection` first. Otherwise
   call `search_products` with the product in the customer's words (size, material and grade if they gave them).
   If several products match, show the closest few and ask which one.
2. **Get the price.** Call `get_best_price_for_product` for the chosen product, with the quantity if the customer
   gave one.
3. **Report.** Give the best price, the unit and the supplier, then the other suppliers' prices on file. If no
   supplier has a price, say so and give the catalog cost when there is one. If the customer compared it with a
   price they were quoted, say how far apart the two are.

## Rules

- Prices come only from tool results, in the currency and units in the customer's settings. These are the
  prices the company has on file from its own suppliers, not market prices; never call them that. If nothing is
  found, say so; never guess a price.
- Plain words to the customer: no record ids and no tool names.
