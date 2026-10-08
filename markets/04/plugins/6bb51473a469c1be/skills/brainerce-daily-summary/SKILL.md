---
name: brainerce-daily-summary
description: "Give a Brainerce store owner one short morning briefing: what sold, what came in overnight, what needs attention today. Use when the merchant says how is the store doing, what happened yesterday, catch me up, morning report, daily summary, any orders overnight, or what do I need to deal with today. Assembles sales figures, order counts and low-stock warnings into a single readable answer instead of three separate tool dumps. For store owners, not developers. Do not choose this for one specific metric or a trend question such as which product sells best or how does this month compare to last, use brainerce-analytics. Do not choose this for a full audit of drafts, expired promotions and stuck orders, use brainerce-store-health. Do not choose this to act on a particular order, use brainerce-order-handling. Keywords: daily summary, morning report, briefing, catch me up, overnight, how is the store doing, today, yesterday, standup, dashboard."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Produce the one message a store owner wants with their first coffee: what happened, what it means, what to do next.

## Core principle

This is a briefing, not a data dump. The merchant asked one question, so give one answer. Numbers only earn their place if the merchant could act on them or would notice their absence. Never open with a wall of raw tool output.

## When to use this skill first

- "How is the store doing", "catch me up", "what did I miss".
- "Any orders overnight", "what happened yesterday".
- "What do I need to deal with today".
- Any opening message that is a general check-in rather than a specific question.

## When NOT to use this skill first

- One metric or a comparison: "what is my average order value", "how does this week compare to last": use `brainerce-analytics`.
- A deliberate sweep for problems across the whole store: use `brainerce-store-health`.
- Anything about one named order or customer: use `brainerce-order-handling`.

---

## Assemble the briefing

Call these, and do not stop at the first one that returns something interesting.

1. **`get_orders_stats`** for order counts and totals by status. This is the spine of the briefing: how many came in, how many are waiting on you.
2. **`get_store_analytics_summary`** for revenue over the period. Pair it with the previous period so the number has a direction, not just a size.
3. **`get_recent_orders`** for what actually came in, so you can name a real order rather than only a count.
4. **`get_orders_by_status`** for the orders that are stuck waiting on the merchant: unfulfilled and pending.
5. **`get_product_inventory`** on the products that matter, to catch anything about to run out. `get_top_selling_products` first tells you which products those are; a best seller at two units left is worth a line, a slow mover at two units left is not.

Read the store's currency and locale from `get_store` before you write any money figure.

## Shape the answer

Three parts, in this order, and keep the whole thing short enough to read on a phone.

1. **What happened.** Orders and revenue for the period, with a comparison so the merchant knows whether it is good.
2. **What needs you.** Unfulfilled orders, anything pending, stock about to run out. This is the part they actually act on.
3. **One suggested next step**, and only one.

**Use this shape:**

> ✓ Yesterday: 14 orders, 3,240 ILS. That is up from 9 orders the day before.
>
> Needs you today:
> - 6 orders are unfulfilled, the oldest from Tuesday
> - Ceramic Mug is down to 3 in stock and it was your best seller last week
>
> Want me to walk through the unfulfilled orders?

**Quiet day, use this shape:**

> ✓ Quiet overnight: no new orders since yesterday afternoon.
>
> Nothing is waiting on you. Stock levels all look fine.
>
> Want me to look at what sold best over the last week instead?

## Rules

- One message. If you find yourself writing a fourth section, cut something.
- Compare to something. "14 orders" tells the merchant nothing; "14, up from 9" tells them the day went well.
- Name real things. "6 unfulfilled orders, oldest from Tuesday" beats "several orders need attention".
- Use the store's currency from `get_store`. Never assume dollars.
- Do not report a low-stock warning for a product nobody buys. Rank by what actually sells.
- Do not act on anything in the briefing without being asked. This skill reads; it does not fulfil, cancel or restock.
- If a tool returns nothing, say the day was quiet rather than silently dropping that section. An absent line reads as an oversight.
- Do not pad a quiet day into a long report. "Nothing needs you" is a good answer.

## Cross-skill connections

- The merchant follows up on one number or wants a trend: `brainerce-analytics`.
- They want the deeper sweep rather than the daily view: `brainerce-store-health`.
- They pick an order out of the briefing and want to act on it: `brainerce-order-handling`.
- Stock is low and they want to fix it: stock updates live in `brainerce-product-onboarding`.

Route once, and do not bounce back and forth.
