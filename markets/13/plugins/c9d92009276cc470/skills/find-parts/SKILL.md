---
name: find-parts
description: Find industrial automation parts in 4D Controls' current stock by part number or by specification, compare candidates, and share each part's product page link.
---

Use the 4D Controls tools to answer questions about parts 4D Controls has in stock.

1. If the customer gives a part number, search for it with search_products first.
2. If there is no exact match, or the customer describes what they need, search by a short product type plus one key rating (for example "power supply 24VDC"), then open the likely candidates with get_product and compare their specifications.
3. For each part you mention, give its condition, price and stock, and show its buy_url as a link. Prices exclude GST, VAT, sales tax and import duties.
4. For warranty, returns, shipping or payment questions, call get_store_policies.
5. If nothing suitable is in stock, say so and suggest emailing sales@4dcontrols.com.au.
