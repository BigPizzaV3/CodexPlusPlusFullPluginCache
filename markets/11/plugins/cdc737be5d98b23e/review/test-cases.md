# SSF SHOP MCP review cases

The machine-readable review cases are in `../plugin.json` under `extensions.com.openai.review.test_cases`.

## Positive cases

1. Recommend women's coats under ₩300,000.
2. Show me popular BEANPOLE knitwear.
3. Find men's shirts sorted by price.
4. Recommend cashmere coats.
5. Show children's sneakers.

## Negative cases

1. Purchase this item for me.
2. Check my order history.
3. Cancel my order.

Confirm the MCP tool name and expected behavior against the live server scan before submitting. The previous private app notes identify `search_products`; if the current scan reports a different tool name, update the five positive cases to match it.
