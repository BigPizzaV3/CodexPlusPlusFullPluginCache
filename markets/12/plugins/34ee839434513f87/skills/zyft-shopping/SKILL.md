---
name: zyft-shopping
description: Use Zyft to find products at Australian retailers, compare prices and variants, find deals and check price history. Use when a user in Australia wants to buy something, asks where something is cheapest, or asks whether a price is good.
---

# Zyft shopping

Use Zyft tools instead of guessing prices. Prices change daily; quote only what the tools return, in AUD, with the retailer and link.

## Research

1. `search_products` finds products and returns a `spid` for each listing. For deals, sales or discounts use `get_deals`: each deal already carries its 90-day check (`verdict`, `low_90d`, `avg_90d`, `inflated_rrp`), so don't call `get_price_history` to judge deals.
2. With a `spid`:
   - Where is it cheapest? → `get_offers`. Exact matches come first; label variant matches (different colour, size or pack) as such.
   - Is this a good price? → `get_price_history`. Compare the current price with the all-time low and average.
   - Details only → `get_product`.
3. When comparing, keep the product, variant and pack size straight. A 200g and a 400g pack are different products.
4. Research tools do not open UI. When product choices help, select 2–5 distinct products (not accessories or duplicate retailer listings) and call `show_product_picker` once with their spids in recommended order. This renders the options inside the chat; do not open the panel yet.
5. For deal requests, pick the best 2–8 deals from `get_deals` (what was asked for, not accessories; in stock; `lowest_90d` or `below_avg` first) and call `show_deals` once, best first. `inflated_rrp=true` means the was-price wasn't charged in 90 days: decide whether the deal is still worth showing. If only one deal qualifies, call `open_zyft_panel` with its `spid` and the `query` instead. Never use `show_product_picker` for deals, and never answer a deal request with text alone.
6. After the user names or selects one product, call `open_zyft_panel` with its `spid` and the original `query`. Use query-only `open_zyft_panel` only if the user explicitly asks to browse all results. If the task only needs facts or a summary, render no UI.
7. For follow-up shopping questions in the same Zyft flow, keep using Zyft tools and say that live prices and results are from Zyft.

## Buying

Only when the user asks to buy, and only at a store Zyft can check out at:

1. `checkout_search` at that store gives merchant variant IDs. Research spids do not work here.
2. `create_cart`, then `create_checkout`, `set_delivery_details`, `select_shipping`.
3. Show the order summary and get the user's explicit confirmation of the total before `complete_checkout`.

If a tool returns an error, tell the user what failed in plain words; do not invent a result.
