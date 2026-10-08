---
name: brainerce-store-health
description: "Sweep a Brainerce store for the things that quietly go wrong and hand the merchant a short list of what to fix. Use when the merchant says check my store, is everything ok, spring clean, audit the shop, what am I missing, anything broken, or I have not looked at this in a while. Finds products left as drafts, items out of stock, promotions that expired or were never switched off, and orders stuck waiting on someone. For store owners, not developers. Do not choose this for the routine morning check-in on yesterday's numbers, use brainerce-daily-summary. Do not choose this for a specific metric or trend, use brainerce-analytics. Do not choose this to act on one known order, use brainerce-order-handling. Do not choose this to audit how the catalog is structured rather than its state, use brainerce-store-architecture. Keywords: store health, audit, check my store, spring clean, tidy up, what is broken, drafts, out of stock, expired discount, stuck orders, housekeeping, review my shop."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Find the quiet problems a busy merchant stops seeing, and give them an ordered list of what to do about it.

## Core principle

The output is a to-do list, not a report. Every line should name a real thing, say why it costs the merchant something, and be actionable. A finding with no consequence attached gets ignored, and rightly so.

Read only. This skill diagnoses. Fixing happens after the merchant picks something.

## When to use this skill first

- "Check my store", "is everything ok", "anything broken".
- "Spring clean", "tidy up the shop", "audit this".
- "I have not looked at this in months".
- "What am I missing".

## When NOT to use this skill first

- The routine "how did yesterday go": use `brainerce-daily-summary`.
- One number or a trend: use `brainerce-analytics`.
- One known order: use `brainerce-order-handling`.
- How the catalog is STRUCTURED rather than what state it is in, so variant explosion, a flat category tree, tags doing a category's job: use `brainerce-store-architecture`. This sweep is about state; that one is about shape.

---

## The four sweeps

Run all four. A sweep that finds nothing is still worth one line, because "no drafts left hanging" is information.

### 1. Products that are not really for sale

- `list_products` filtered to draft status: products the merchant created and forgot to publish. These are invisible to customers and the merchant usually believes they are live.
- `list_products` plus `get_product_inventory` on what comes back: items at zero stock. Cross-check against `get_top_selling_products`, because a best seller at zero is urgent and a slow mover at zero is housekeeping.
- Products with no category. Uncategorised items are hard for customers to reach even when published.

### 2. Promotions nobody is watching

- `list_discount_rules` and `list_coupons`. Look for two different problems, and do not merge them:
  - **Expired**: past its end date and cluttering the list. Low priority.
  - **Still running and probably should not be**: no end date, or an end date that already passed while the rule stayed enabled, or a promotion the merchant set up for an event that is over. This one costs money every day, so it goes at the top.

### 3. Orders waiting on somebody

- `get_orders_by_status` for unfulfilled and pending. Rank by age. An unfulfilled order from three weeks ago is a customer who has probably given up.
- `get_recent_orders` to see whether the backlog is growing or is a one-off.

### 4. Signals from customers

- `list_product_reviews` filtered to low ratings, and `get_product_review_stats` on the products that sell most. A best seller whose rating has slipped is worth knowing about before it shows up in the revenue.

## Shape the answer

Order by cost to the merchant, not by category. Put money-losing first, customer-facing second, housekeeping last. Cap the list; five real problems beat thirty observations.

**Use this shape:**

> ✓ I went through your store. Four things worth your time, most costly first:
>
> 1. **A 30% sale is still running on Summer Dresses.** It has no end date and it started in June. Every order since then has been discounted. Want me to switch it off?
> 2. **Six orders are unfulfilled**, the oldest from 4 November. That customer has been waiting eleven days.
> 3. **Ceramic Mug is out of stock** and it was your best seller last week. Every day it stays at zero is lost sales.
> 4. **Three products are still drafts**: Linen Scarf, Wool Hat, Gift Box. Customers cannot see them.
>
> Also fine: no expired coupons cluttering things up, and your review ratings are all above 4.
>
> Which of these do you want to start with?

**Clean store, use this shape:**

> ✓ Your store looks in good shape. No drafts left hanging, nothing out of stock, no promotions running past their date, and no orders sitting unfulfilled for more than a day.
>
> The one thing I would keep an eye on: Ceramic Mug is down to 4 in stock and it sells about 3 a day.

## Rules

- Read only. Do not fix anything during the sweep, even something obviously wrong. Report, then let the merchant choose.
- Every finding needs a consequence. "Three drafts" is a fact; "three drafts customers cannot see" is a reason to care.
- Rank by cost. An overrunning discount outranks an untidy tag list, always.
- Name real items and real dates. Vague findings get ignored.
- Say what came back clean. Otherwise the merchant cannot tell whether you checked.
- Cap the list at around five items and offer to go deeper. A thirty-item audit gets closed.
- Do not report the same thing twice under two headings.
- This connector cannot delete anything, so never offer to clear out old items. Switching a promotion off is possible with `toggle_discount_rule`; removing it is a dashboard task.

## Cross-skill connections

- The merchant picks a promotion to switch off or change: `brainerce-launch-a-sale`.
- They pick an order out of the list: `brainerce-order-handling`.
- They want to restock or publish a draft: `brainerce-product-onboarding`.
- They want to understand a trend the sweep hinted at: `brainerce-analytics`.
- The sweep keeps hitting the same structural problem, such as one product with hundreds of variants: `brainerce-store-architecture`.

Route once, and do not bounce back and forth.
