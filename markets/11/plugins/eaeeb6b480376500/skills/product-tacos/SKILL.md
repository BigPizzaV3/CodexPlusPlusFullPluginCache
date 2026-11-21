---
name: product-tacos
description: Use when the user asks for TACoS (total advertising cost of sales), ad spend as a share of sales, or advertising efficiency for a specific product or product family. Produces a product-level TACoS with the window and data coverage it is based on.
---

# Product-level TACoS

1. Call `list_accounts` and pick the account and marketplace the product belongs to.
2. Identify the product. Pass the user's wording as `product_query` to `seller_analytics` with `dataset=realtime_sales` (`group_by=sku` or `parent` as appropriate). If the response asks for confirmation between several products, show the choices and let the user pick; reuse the returned `product_set_ref` for follow-up calls.
3. Make two matched calls for the same account, marketplace, confirmed product and date window (default: last 30 days):
   - `seller_analytics` with `dataset=realtime_sales` for total product sales;
   - `advertising_analytics` with `dataset=spend_by_asin` for the directly attributable Sponsored Products and Sponsored Display spend.
4. Compute TACoS = advertising spend ÷ total sales × 100. Use the returned `requested_window`, `coverage_window`, `data_status` and `data_through`: if advertising data lags behind sales, compute over the dates both cover and label the result provisional.
5. Never use account-wide advertising totals or advertising-attributed sales as the denominator. Show sales, spend, TACoS and the exact dates used.
