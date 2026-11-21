---
name: print-and-frame
description: Order a previewed Routeframe finisher poster printed at 30 x 40 cm or 50 x 70 cm, unframed or in a black, white or oak wood frame, through checkout on Routeframe's site, and track the order until it arrives. Use when a user in the United States asks about poster sizes, frames, delivery times or shipping, wants to order the poster they previewed for themselves or framed as a gift shipped straight to the runner, or asks where their Routeframe order is. Printing ships only within the United States; elsewhere the poster in the card is the whole product.
---

Use this skill when a finisher poster is ready to print. The user's explicit instructions always come first.

## Flow

1. `get_print_options` lists every size and frame, where Routeframe ships and the delivery estimate. Share what the user asks about; for a gift, a framed size suits it and the estimate lets the user time it for the occasion.
2. `start_order` takes the same race, year, runner name, finish time, note, style and units as the preview, plus the size, frame and quantity the user chose. It returns a link to Routeframe's own checkout page, where the user enters the delivery address (for a gift it can be the runner's) and pays. Addresses and card details stay on that page and out of the chat. Nothing is charged in ChatGPT and nothing prints until payment.
3. `get_order_status` shows this user's orders, newest first, or one order by its number (RF- and six characters), with status and tracking.

## Scope

- Physical prints only, shipped only within the United States. Elsewhere get_print_options, start_order and get_order_status say printed posters aren't available in the user's country.
- If there is no preview yet, make one first with the finisher-poster skill.
