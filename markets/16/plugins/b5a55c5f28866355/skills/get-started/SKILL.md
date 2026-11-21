---
name: get-started
description: "Start here with Deal.ai: what it can do in ChatGPT and which tool fits which question. Use when the user first connects Deal.ai, asks what it can do, or asks a shopping question and no other Deal.ai skill fits."
---

# Get started with Deal.ai

Deal.ai compares prices for the same product across US stores (Best Buy, Walmart, Target, Amazon, brand stores and more), tracks each product's price over time, checks whether a deal is real, and has a shopping agent that researches what to buy. The user's own Deal.ai account holds their wish list, which e-mails them when a watched product's price drops.

When the user asks what Deal.ai can do, answer in a few lines from the list above and suggest one or two things to try. Don't call a tool just to describe Deal.ai.

## Which tool for which question

- "What should I buy?", "best X under $Y": the find-what-to-buy skill (`ask_deal_ai`).
- "How much is X?", "where is X cheapest?": the compare-prices skill (`search_products`, `get_product_prices`).
- "Is this a good deal?", a store link with a price: the check-a-deal skill (`check_deal`).
- "Any deals on X?", "today's Best Buy deals": the deals skill (`get_deals`).
- "Tell me when it drops", "what am I watching?": the watch-prices skill.
- Details or specs of one product: `get_product_details`. Two to four products side by side: `compare_products`.

## Rules for every answer

- Prices are the stores' listed prices at the time shown, before tax. Say when a price was seen; prices change.
- Link the Deal.ai page each answer gives, and use a price's `buy_url` when the user wants to buy. Nothing is bought in ChatGPT: the user buys on the store's site.
- A price marked as a marketplace seller's (eBay, a third-party seller) is labelled as such and is never "the best price".
- When an answer ends with store-link notes (commission, Klarna, Amazon), keep them in your reply.
- Never state a price, store or verdict that a Deal.ai tool didn't return.

## When not to use Deal.ai

Questions with no shopping in them, arithmetic, and general product knowledge you can answer yourself. Deal.ai never buys anything, pays, or changes an order.
