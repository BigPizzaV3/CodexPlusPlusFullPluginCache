---
name: store-daily-briefing
description: Give a Capi merchant a short daily briefing on their store — sales against the previous period, what needs attention, stock at risk and customer service — when they ask how the store is doing, for a summary, a morning briefing, or "what should I do today".
---

Use this skill when a merchant asks for an overview of their store: "how is my store doing", "give me a summary", "morning briefing", "what should I focus on today", or the same in Arabic ("شلون المتجر", "ملخص اليوم", "شو لازم أعمل اليوم").

1. Call `sales_report` with `period: "today"`. If the merchant names a period ("this week", "last month"), use the closest of `yesterday`, `last_7_days`, `last_30_days` or `last_90_days` instead.
2. Call `store_problems` once.
3. Call `service_report` with the same period as step 1.
4. Only if `sales_report` or `store_problems` mentions low or zero stock, call `find_my_products` with `filter: "out_of_stock"`.

Then answer in the merchant's language, in this order and briefly:

- **Sales** — revenue, orders and average order value against the previous period, with the change. Say plainly when a figure went down.
- **Needs attention** — at most five items from `store_problems`, most urgent first, each with its dashboard link.
- **Stock** — out-of-stock best sellers by name, if any.
- **Customer service** — the rating and the one main reason behind low ratings, if the report gives one.
- **Next step** — one concrete action the merchant can take today.

Rules:

- Use only figures the tools returned. If a tool returns an error or no data, say so for that section; never estimate or fill a gap.
- Do not call any tool that changes settings (knowledge base, rules, working hours, agent behaviour, versions) during a briefing. Offer the change and wait for the merchant to ask for it.
- Never ask for, or try to reveal, customer names, phone numbers, emails or addresses. The tools do not return them.
