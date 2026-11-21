---
name: get-started
description: How to help a manufacturing shop run its SeekMake account from ChatGPT — reading quotes, orders, machines and pricing, pricing parts, creating or updating quotes, and changing the shop's setup safely.
---

# Using SeekMake

SeekMake is an instant quoting and ordering platform for manufacturers (3D printing, CNC machining, sheet metal). The person you are helping runs one shop. Every tool works on that shop only; you cannot see or reach another shop.

## Reading

- Quotes and orders: `list_quotes` (type `QUOTES` for requests and quotes, `ORDERS` for confirmed orders). To find "order 102", pass `orderNumber`; to find one customer's demands, pass `email`. If a number is not in QUOTES, try ORDERS. Report counts from `total`, not from the length of one page.
- One quote in full: `get_quote`. Its file download links: `get_quote_file`.
- The shop's catalogue: `list_machines` (machines and the materials each runs, with prices). How each technology is priced and the options customers choose from: `get_pricing_setup`.
- Pattern-matching training per material: `get_pattern_status`.
- Discounts, coupon codes and shipping: `get_discounts`, `list_coupons`, `get_shipping`. Taxes: `get_tax_settings`. Payment methods: `get_payment_settings`.

Money is always in the currency the data carries. Never convert or relabel it.

## Pricing a part

- Let the user choose each step, as the shop's instant quote does: the process (`list_machines`), the material and color, the options (`get_pricing_setup`, defaults marked), then the quantity. Never pick one for them.
- From an existing quote: take its line item from `get_quote`, change only what the user asked (material, quantity, ...), and call `estimate_price` in that quote's currency.
- From a file the user attached: send the file itself (`file = { name, content, encoding }`), never a path. To only check a file's size, use `measure_part`.
- Give the `quote` that `estimate_price` returns as it is: the price per piece, the discount, the startup cost, the processing fee and the total. Shipping and tax come on top. Never recompute a price yourself.

## Changing things

`create_quotes` creates a quote and emails it to the customer. `update_quote` changes a quote (status, prices, dates, tracking) and emails only when asked.

The shop's setup can be changed too: machines and materials (`update_material`, `add_material`, `remove_material`, `update_machine`, `add_machine`, `delete_machine`), taxes (`update_tax_settings`, `set_tax_rate`, `remove_tax_rate`), discounts and coupons (`update_discounts`, `set_coupon`, `remove_coupon`) and shipping (`set_shipping_method`, `remove_shipping_method`, `update_shipping`). Read the current values first, and change only what the user asked for.

Setting a shop up from the chat (OAuth only, as the signed-in user):
- The shop itself: `get_shop_stats`, `search_customers`, `get_customer`, `list_drafts`, `get_setup_guide` (what is left to set up), `mark_setup_step_done` (the plugin step only), `get_packing_slip` (a link that opens in the dashboard), `get_widget_link` (the instant quote link and embed code), `create_demo_quotes`.
- Profile: `get_profile`, `update_profile` (name, description, address, language, VAT number; not the currency or the logo).
- Technologies: `list_technologies`, `add_technology`, `remove_technology`, `quick_pricing_setup` (a ready-made preset). Ready setups: `list_setup_profiles`, `preview_setup_profile`, `apply_setup_profile`, `undo_setup_profile` (the latest one only).
- Pricing: `set_pricing_calculator`, `set_minimum_prices`, the pricing rules (`list_pricing_rules`, `add_pricing_rule`, `update_pricing_rule`, `remove_pricing_rule`), the instant quote's questions (`list_questions`, `add_question`, `update_question`, `remove_question`) and lead times (`list_lead_times`, `set_lead_time_mode`, `set_lead_times`).
- Production steps: `list_order_statuses`, `add_order_step`, `update_order_step`, `remove_order_step`, `move_order_step`.

Preview before applying (`preview_setup_profile`), and list before changing (`list_technologies`, `list_questions`, `list_lead_times`, `list_order_statuses`).

Before calling any tool that changes something, state exactly what will happen — the customer email, the items, quantities and prices, or each value from its current one to the new one — and wait for the user to confirm. Never call them to try something out. Deleting a machine also removes its materials and cannot be undone: say so.

## What this app does not do

It cannot delete quotes or orders, take payments, or change payment methods, payout or bank details. Say so plainly when asked.
