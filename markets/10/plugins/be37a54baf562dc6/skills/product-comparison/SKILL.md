---
name: product-comparison
description: Compare two or three named products with Sovrnti on innovation, control and scale, for one country, region or the world view. Use it when the user has finalists or specific products in mind. Examples are "Microsoft 365 or Nextcloud Hub for a French hospital?" and "how do Google Workspace and Proton compare on control?". For a whole market, use market-benchmark instead.
---

# Compare named products

Explicit user instructions take priority over this workflow.

## Inputs

- **Products.** Two or three, named as the user wrote them. Aliases such as "M365" work. If the user names more than three, ask which three matter most.
- **Place.** A country name, an ISO code, a region or "world". If the user names no place and the answer could depend on location, ask once which country matters. Do not guess a country.
- **Priority.** If the user states what matters most (for example control of data, or features), use it to order the answer. If not, do not invent one.

## Steps

1. Call `sovrnti_product_compare` with the products and the place. The market is optional: the tool finds the market the products share.
2. If the tool rejects the request because the products are in different markets, pass on its message. Suggest comparing products within one market.
3. If sovereignty is the user's concern, call `sovrnti_market_get_delta` for that market and place. Read only the rows for the compared products.

Use the same place in every call.

## Output

1. **Answer first.** One sentence on how the products differ for the user's stated priority. If the user stated no priority, say where each product leads instead of naming a winner.
2. **Table.** Capability area by product, as the tool returns it, then the Innovation, Control and Scale scores.
3. **Where each product leads and where it trails.** Two lines per product.
4. **What to verify.** Two or three questions for each vendor, taken from the areas where the product scores lowest or where the result depends on configuration. Present them as points to check, not as findings.
5. **Source line.** "Source: Sovrnti, <today's date>, <place>."

If the host shows Sovrnti's interactive comparison, summarise it. Do not repeat every number.

## Rules

- Use only the scores and capability areas the tools return. Never invent a score or a capability.
- If a product is not found, say that Sovrnti does not score it, and offer the closest products the tools return.
- If a tool returns an error, say so in plain words and offer the next best step.
- If a tool says the user has no credits left, pass its message on as it is. Do not suggest a workaround.
