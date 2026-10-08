---
name: brainerce-analytics
description: "Answer how much, how many, what is best and what is the trend for a Brainerce store, using the right reporting tool instead of counting rows by hand. Use when the merchant asks about revenue, sales, total orders, average order value, best sellers, worst sellers, how this month compares to last, whether a sale worked, how many customers, or what people think of a product. Turns a plain question into the correct statistics call and answers with a number plus what it means. For store owners, not developers. Do not choose this for the general morning check-in, use brainerce-daily-summary. Do not choose this to act on a specific order, use brainerce-order-handling. Do not choose this for a health sweep of drafts and stuck orders, use brainerce-store-health. Keywords: revenue, sales, how much, how many, total, average order value, AOV, best sellers, top products, trend, compare, month over month, growth, conversion, ratings, reviews, report, statistics, analytics."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Turn a merchant's question into the right reporting call, and give back a number that means something.

## Core principle

A number without a comparison is not an answer. "You made 12,400 this month" leaves the merchant no wiser than before they asked. "12,400 this month, up from 9,800 last month" is the answer they were actually looking for. Always fetch the comparison period.

And never count by hand. Paging `list_orders` to sum revenue is slow, is capped, and quietly gives a wrong total when the results run past the first page. The statistics tools exist because that failure is easy to miss.

## When to use this skill first

- Money: revenue, sales, totals, average order value.
- Counts: how many orders, how many customers, how many of a product sold.
- Rankings: best sellers, worst sellers, top customers.
- Trends and comparisons: this month against last, is it growing, did the sale work.
- Product sentiment: ratings and what reviewers said.

## When NOT to use this skill first

- General "how is it going" first thing in the morning: use `brainerce-daily-summary`.
- One order, one customer, one action: use `brainerce-order-handling`.
- Finding problems rather than measuring: use `brainerce-store-health`.
- Setting up a promotion, as opposed to measuring one: use `brainerce-launch-a-sale`.

---

## Question to tool

| The merchant asks | Call |
|---|---|
| "How much did I make", "revenue this month", "how are sales" | `get_store_analytics_summary` |
| "How many orders", "how many are still unpaid", "breakdown by status" | `get_orders_stats` |
| "What is my average order", "are people spending more" | `get_average_order_value` |
| "What sells best", "top products", "what should I restock" | `get_top_selling_products` |
| "How many orders are unfulfilled right now" | `get_orders_by_status` |
| "What came in today", "the last few orders" | `get_recent_orders` |
| "How many products do I have" | `count_products` |
| "Who are my best customers", "how many customers" | `list_customers` |
| "What has this customer spent" | `get_customer`, then `get_customer_orders` |
| "How is this product rated", "what do people say" | `get_product_review_stats`, then `list_product_reviews` |
| "Did the sale work" | `get_store_analytics_summary` for the sale window and the window before it, plus `list_discount_rules` to confirm the dates |

⛔ Do not answer a totals question by listing orders and adding them up. `list_orders` is a search tool. Its results are paged, so a hand count silently under-reports as soon as the period is busy, and the merchant has no way to tell.

## Getting the period right

- Read the store's timezone-sensitive settings and currency from `get_store` before quoting any figure. Never assume dollars.
- Turn "this month" and "last week" into explicit dates and state them in the answer, so the merchant can tell you if they meant something else.
- Fetch the comparison period in the same breath as the main one. It is one more call and it is what makes the answer useful.

## Answer shape

Lead with the number. Then the comparison. Then one observation, if there is a real one.

**Use this shape:**

> ✓ 12,430 ILS across 58 orders in November so far.
>
> That is up from 9,810 across 47 orders in the same stretch of October, so about 27% more revenue and a slightly higher average order.
>
> Most of the growth is Ceramic Mug, which went from 12 units to 31.

**Ranking, use this shape:**

> ✓ Your top sellers over the last 30 days, by units:
>
> 1. Ceramic Mug, 31 sold, 2,015 ILS
> 2. Linen Scarf, 18 sold, 2,340 ILS
> 3. Wool Hat, 14 sold, 1,120 ILS
>
> Worth noting: Linen Scarf brings in more money than Ceramic Mug despite selling fewer, so if you are deciding what to promote, it is not the same answer as "what sells most".

**Not enough data, use this shape:**

> There were only 3 orders in that window, so a percentage change would be misleading. Here are the raw numbers instead: 3 orders, 210 ILS, against 2 orders and 145 ILS the week before.

## Rules

- Always fetch a comparison period. A bare number is not an answer.
- Use the store's currency from `get_store`.
- State the exact dates you used.
- Say when the sample is too small for a percentage rather than reporting a 200% rise off two orders.
- Never sum a paged list by hand.
- Do not invent a cause for a change. "Revenue is up 27%" is a fact; "because of your Instagram post" is a guess, and this connector has no marketing data.
- Read only. If the merchant reacts to a number by wanting to act, hand off rather than acting here.
- If a tool returns nothing for the period, say the period was empty. Do not silently widen the window to find something.

## Cross-skill connections

- The general morning briefing rather than a specific question: `brainerce-daily-summary`.
- The merchant wants to act on a slow seller by discounting it: `brainerce-launch-a-sale`.
- They want to restock a best seller: `brainerce-product-onboarding`.
- The numbers point at a problem rather than a trend: `brainerce-store-health`.

Route once, and do not bounce back and forth.
