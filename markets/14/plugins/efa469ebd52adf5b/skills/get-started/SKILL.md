---
name: get-started
description: First-run guide for the OrderInChat Shopping plugin. Use when the shopper has just connected OrderInChat Shopping, asks what this plugin can do, or asks how to shop at an OrderInChat store from chat.
---

# Get started with OrderInChat Shopping

## Priority (instruction following)

1. Explicit user instructions override this skill when they conflict.
2. Never invent stores, products, prices or policies — only report MCP tool results.
3. Keep the welcome short; do not create a cart during onboarding.

## When to use

- The shopper just connected OrderInChat Shopping or says "get started", "what can you do", "how does this work".
- A tool call fails because the account is not connected.

## Steps

1. Explain in 4–5 short bullets what they can do:
   - Find a participating store by its name or link (`find_stores`). Stores are not listed; the shopper needs the store's name or link.
   - Search the store's catalog and see prices, stock, variants, options and add-ons (`search_products`, `get_product`).
   - See the store's bookable services and their free time slots (`list_booking_services`, `get_booking_availability`); a chosen slot goes into a cart, and the booking is confirmed and paid on the store's website.
   - Ask about shipping, returns, payment methods, coupons and the store FAQ.
   - Build a cart and get a link to review and pay on the store's own website (`create_cart`). ChatGPT never pays or places an order.
   - Browsing, carts and booking links work without an account. Only the shopper's own orders and their status (`list_my_orders`, `get_order_status`) need sign-in with OrderInChat.
2. Ask which store they want to shop at, unless they already named one; then call `find_stores` with it.
3. If a tool asks for sign-in or fails with an authentication error, tell the shopper to sign in to (or reconnect) OrderInChat Shopping (Sign in with OrderInChat).
4. Offer starter prompts, for example "Show me the bestsellers", "What's the return policy?", "How much is shipping to my country?".

## Do not

- Promote plans, upgrades or other stores.
- Ask for card numbers, passwords or codes in chat; sign-in happens through OAuth and payment on the store website.

## Output

The capability bullets and one question asking for the store name (or the store's details when already known).
