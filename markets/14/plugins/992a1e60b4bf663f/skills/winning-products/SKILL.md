---
name: winning-products
description: Find products that are selling now in a niche, and the Shopify stores behind them. Use when the user asks for winning products, product ideas, what to sell, trending or best-selling products, or the fastest-growing stores in a niche or country.
---

# Find winning products

Use the tools of the SellWinners connector. Tool calls use the user's SellWinners credits (`usage_get` shows what is left), so answer with as few calls as the question needs.

These steps and answer formats are defaults. When the user explicitly asks for a different format, order, number of results or SellWinners tool, follow the user. The rules on confirmations, public links, the plan and the monthly quota always apply.

## Steps

1. Settle the niche (a word such as `coffee` or `pet supplies`, or a category), one to five product keywords, and the market as a two-letter country code if the user named one. Ask only when the niche is missing.
2. Call `find_winning_products` with `niche`, `keywords`, `country` and `max_results` (how many shops, 1 to 30; start with 10). It returns the best sellers whose title matches a keyword, taken from the fastest-growing shops of the niche, up to three per shop. When the answer says no category matched the niche, tell the user the products were found by keyword alone.
3. To widen the list of stores, call `search_shops` with the niche words as `query`, and `sort_by` set to `growth30d`, `estMonthlySales` or `unitsSold`. Its `country` is the country a shop was created in, not its market. For an exact category, first call `lookup_filter_ids` with `type` `categories`, then pass the ids as `filters` `{"categoryIds": [...]}`.
4. For a store the user wants to go deeper on, `find_similar_shops` with its domain lists its competitors, and the competitor-research skill covers a full brief.

Other ways in:

- **Products across every store:** `search_products` with the product words as `query` and `sort_by` set to `estSales`, `activeAds`, `bestSelling` or `newest`.
- **A picture of a product:** `search_products_by_image` with `image_url`, a direct link to a PNG, JPG or WEBP image, lists the products that look like it, closest first, with their shops.

Search tools answer with `data` and `pagination`. Ask for the next `page` only when the user wants more results.

## Answer

- Start with a table: product, store domain, price when present, the signal that makes it a winner (growth, estimated sales, units sold) and a link.
- Follow with two or three sentences on the pattern across the list: shared angles, price bands, markets.
- When an answer carries `restrictions`, the user's plan shortened it. Say what was left out.
- Keep product and image URLs as links. Don't paste raw JSON.

When a tool says a request is outside the user's plan (`plan_not_eligible`), don't try to get the same data another way, with other brands or other SellWinners tools. Tell the user in one sentence what the message says, with the link it gives, and answer the rest of the question with what the plan covers.

A tool named here can be missing from the connector when the user's plan doesn't include it. Then say so in one sentence and answer with the tools that are there.

When a tool answers that the plan's credits are used up, or that the plan doesn't include MCP access, stop calling SellWinners tools for this request. Tell the user in one sentence, with the renew date, the wait or the link the message gives.
