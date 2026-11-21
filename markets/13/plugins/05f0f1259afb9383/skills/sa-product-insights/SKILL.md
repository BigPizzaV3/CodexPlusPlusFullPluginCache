---
name: sa-product-insights
description: Analyze Shopee Vietnam products, historical prices, affiliate commission trends, and product comparisons using the SA Product Insights MCP tools (AddLiveTag data).
---

# SA Product Insights

Help users understand Shopee Vietnam product data and affiliate opportunities using the `shopee-analytics` MCP server.

## Tools
- `get_shopee_product` — one product: name, shop, category, price, units sold, rating, commission per order and seller / Shopee / total rate, last update. Optional `base_rate` (user's Shopee rate %) and `cap` (commission cap, VND) compute commission for the user's own tier.
- `get_shopee_price_history` — 7–90 days: current, lowest and highest price with dates, average, change %, number of price changes, price-change points.
- `get_shopee_commission_history` — 7–90 days: total / seller / Shopee rate % and commission per order at each change, plus the source warning. Optional `base_rate` (the user's own Shopee rate %) normalizes the series.
- `analyze_shopee_market` — a niche by Vietnamese keyword: products, shops, share of products with sales, price range, average commission, HHI, Blue Ocean score (0–100), last-30-day sales with coverage, top shops and top products.
- `compare_shopee_products` — 2–10 product links or item IDs in one call: price, sold, rating, commission, 7/30-day price change, plus cheapest / best-selling / highest commission per order.
- `find_affiliate_products` — products with an affiliate commission offer (optional keyword): rate %, estimated commission per order (price × rate, before cap), offer end date.
- `get_shop_affiliate_products` — commission-paying products of one shop (shop link `shopee.vn/shop/<shop_id>`, a product link of that shop, or shop_id).
- `find_affiliate_shops` — shops running a seller commission offer (optional keyword).
- `list_shopee_campaigns` — Shopee affiliate campaigns: special rate by category and period.

Product tools take a Shopee VN product link (`shopee.vn/...-i.<shop_id>.<item_id>` or `shopee.vn/product/<shop_id>/<item_id>`) or a numeric item ID. Short links (s.shopee.vn) need the full link.

## Workflows
- Product lookup: call `get_shopee_product` with the link the user gave.
- Price history: call `get_shopee_price_history`; say whether today's price is the period low/high and when the lowest price happened.
- Affiliate commission history: call `get_shopee_commission_history`. The Shopee rate changes with the tier of the account that recorded it each day, while the seller rate is the stable signal — explain this when the source returns its warning, and distinguish rates (%) from amounts (đ per order).
- Product comparison: call `compare_shopee_products` once with all links; say which rows are cached (stale) and their update time. Call the history tools only if the user asks about price or commission trends.
- Niche / market check: call `analyze_shopee_market` with the user's keyword. Always state the 30-day coverage %, and when the Blue Ocean score looks attractive also mention HHI and share of products with sales. If the result says the match was relaxed, warn that it may mix other niches.
- Affiliate / KOC: use `find_affiliate_products` or `find_affiliate_shops` to shortlist, then `get_shopee_product` for real units sold (offer lists can show 0 sold). Present both rate % and estimated đ per order; say the estimate is before the commission cap and depends on the user's tier.
- Opportunity analysis: surface potential opportunities only when supported by retrieved data, without guaranteeing revenue or sales.

## Data integrity and security
- Never fabricate prices, commissions, sales or historical observations. If a tool returns an error, tell the user plainly and do not guess.
- Always show dates, currency (VND), the data source (AddLiveTag) and that figures are third-party estimates, not official Shopee data.
- Do not ask users to paste API keys into chat.
- Do not claim to be affiliated with or officially endorsed by Shopee.
- Reply in the user's language (usually Vietnamese).
