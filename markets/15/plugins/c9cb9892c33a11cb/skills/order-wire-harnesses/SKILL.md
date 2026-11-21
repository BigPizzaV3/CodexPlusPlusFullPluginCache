---
name: order-wire-harnesses
description: Design, price and order custom XT30, XT30(2+2) or XT30 + JST GH wire harnesses (power, CAN and pigtail cables for robots, batteries and actuators) from Acorn Harness. Use when the user wants a custom XT30-family cable, a quote for one, a checkout link, or the status of an Acorn order.
---

# Order wire harnesses from Acorn Harness

Acorn Harness builds custom XT30, XT30(2+2) and XT30 + JST GH wire harnesses to order: jumpers (a plug on both ends) and pigtails (a plug on end A, tinned leads on end B). They are Assembled in the USA, 100% continuity tested, and ship within 5 business days to US addresses.

Use the `acorn` MCP server's tools:

1. `list_options` when you need the allowed values or the rules for combining them.
2. Before quoting, get all six choices for each design from the user: connector, length, power gauge, end A, end B and quantity. Ask about end A and end B as separate questions and never assume either one; "right angle on one end" still leaves which way, and what the other end is. Ask for everything that's missing in one message, with the options listed. If the user tells you to choose, choose and say what you chose. A configurator link or design code from the user can go in `design` instead.
3. `quote_harness` with the complete design(s). Show the preview picture it returns for each design (if the picture doesn't appear, give the item's `preview_url`), the price per wire harness, the subtotal, and each item's `configurator_url` so the user can check the design on acornharness.com. Tell the user which defaults were used: each item's `defaults_applied` lists them, and the user can change any of them.
4. Before ordering, confirm the design, quantity and price with the user. Then call `create_order` and give the user the `checkout_url`. They pay and enter the shipping address on acornharness.com; nothing is charged or built until they do. The link expires after 24 hours.
5. `get_order_status` with the order id to check payment.

## Translating a request into a design

- Match the connector to what the cable plugs into: `xt30` for 2-pin power (batteries, ESCs, power boards); `xt30-22` for power plus a CAN pair, as on Damiao and MyActuator actuators; `xt30-gh` for power on an XT30 with the signal pair on a JST GH 1.25 mm plug. For an XT30(2+2) on one end and JST GH on the other, use `xt30-22` with `end_b_gh: true`.
- `length_mm` is the wire only, between the rear faces of the plugs (to the wire tips on a pigtail). Convert inches to mm (1 in = 25.4 mm).
- `power_gauge`: 14 AWG for long runs or over about 20 A, 16 AWG for most robot joints, 18 AWG for the tightest bends.
- `end_a` and `end_b`: `straight`, `ra-up` or `ra-down` (power wires bent 90° up or down as seen from the wire side). Only `end_b` can be `unterminated` (a pigtail).
- `swap_signals: true` crosses the signal pair (swaps CAN H/L between the ends).
- Only the optional fields (`colors`, `twisted`, `swap_signals`, `end_b_gh`) have defaults. Set them when the user asks for something other than the default.

## Rules

- Never ask for, accept or repeat card numbers or other payment details. Payment only happens on the checkout page.
- Quote prices exactly as the tools return them. They exclude shipping (chosen at checkout) and sales tax.
- Made to order, so there are no returns. If a wire harness arrives damaged or defective, the buyer emails support@almond.bot with photos within 14 days of delivery and it is repaired or replaced.
- For anything the tools can't do (net terms, special parts, non-US shipping), point the user to support@almond.bot.
