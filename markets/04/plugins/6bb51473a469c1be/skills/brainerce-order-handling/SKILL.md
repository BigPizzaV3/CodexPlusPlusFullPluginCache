---
name: brainerce-order-handling
description: "Work a single Brainerce order from question to action: look it up, understand its state, then fulfil, move its status or cancel it. Use when the merchant says where is order 1042, this customer is asking about their order, mark this as shipped, add tracking, cancel this one, the customer changed their mind, or what has this person bought before. Includes the rules for when NOT to touch an order. For store owners, not developers. Do not choose this for counts and totals across many orders such as how many orders today or revenue this week, use brainerce-analytics or brainerce-daily-summary. Do not choose this to sweep for stuck orders across the whole store, use brainerce-store-health. This connector cannot issue refunds or record payments. Keywords: order, fulfil, fulfill, ship, shipped, tracking number, cancel order, order status, customer asking, where is my order, refund, order history, delivery."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Handle one order well: read it fully, act only where acting is right, and tell the merchant exactly what the customer will now see.

## Core principle

Order actions are visible to a real customer within seconds. Fulfilling sends an email. Cancelling cannot be undone from here. So the order gets read in full before anything changes, and the merchant is told what the customer will receive before you send it, not after.

## When to use this skill first

- A named or numbered order: "where is 1042", "this one has not shipped".
- A customer question routed through the merchant: "she is asking where her parcel is".
- An action on one order: mark shipped, add tracking, move status, cancel.
- "What has this customer bought before".

## When NOT to use this skill first

- Counts, totals or trends across many orders: use `brainerce-analytics`, or `brainerce-daily-summary` for the morning view.
- Sweeping the store for orders stuck in one state: use `brainerce-store-health`.
- The order should have had a discount and did not: check the promotion in `brainerce-launch-a-sale`.

---

## Step 1: find and read the order

- Order number or id: `get_order`.
- Vaguer than that: `list_orders` filtered by status, date or customer, or `get_recent_orders` for "the one that came in this morning".
- A customer's history: `get_customer` to identify them, then `get_customer_orders`.

Read the whole order before proposing anything. Its current status determines which actions are even sensible, and the line items determine what you are about to tell a customer.

If more than one order matches what the merchant said, list the candidates and ask. Do not pick.

## Step 2: choose the action from the state, not from the phrasing

| Merchant says | State | Do |
|---|---|---|
| "mark it shipped", "it went out today" | Paid, unfulfilled | `fulfill_order` with tracking if they have it |
| "move it to processing", "put it back to pending" | Any | `update_order_status` |
| "cancel it", "she changed her mind" | Not yet fulfilled | `cancel_order` |
| "cancel it" | Already fulfilled and shipped | Stop. See below. |
| "refund her" | Any | Not possible here. See below. |
| "mark it paid", "the cash arrived" | Any | Not possible here. See below. |

## When NOT to touch an order

These are the cases where doing what was asked is the wrong move.

- **Already fulfilled and shipped, and the merchant says cancel.** Cancelling does not recall a parcel. Say what cancelling would and would not do, and ask what they actually want: a return, a refund, or a note to the courier. Do not cancel and let them discover the parcel is still in transit.
- **The merchant asks for a refund.** This connector cannot issue one. Say so plainly and point at the Brainerce dashboard. Do not cancel the order as a substitute; a cancellation is not a refund and the customer's money does not move.
- **The merchant asks to mark an order as paid.** Also not available here, also a dashboard task. Do not move the status to something adjacent and imply the payment is recorded.
- **The order is already in the state being asked for.** Say it is already there rather than calling the tool again and reporting success.
- **The merchant is guessing which order they mean.** Confirm first. There is no undo on a cancellation.
- **Anything involving the customer's address.** This connector cannot edit addresses. Dashboard task.

## Step 3: act, then say what the customer sees

Fulfilment and status changes send customer-facing email. That is the part the merchant most needs to know about, and the part they are most often surprised by.

**Fulfilled, use this shape:**

> ✓ Order 1042 is marked fulfilled with tracking number RR123456789IL.
>
> Ronit has been emailed the tracking link automatically.
>
> Anything else on this order?

**Cancelled, use this shape:**

> ✓ Order 1042 is cancelled and the two Ceramic Mugs are back in stock.
>
> Ronit has been emailed the cancellation. Her payment is not refunded by this, so if money needs to go back you will need to do that from the Brainerce dashboard.

**Declining, use this shape:**

> Order 1042 already shipped on Tuesday, so cancelling it here would not stop the parcel. It would only mark the order cancelled and put the stock back, while the box is still on its way to Ronit.
>
> Do you want me to leave it as is while you arrange a return, or is there something else going on with it?

**Cannot do it, use this shape:**

> I cannot issue refunds from here. That one is done in the Brainerce dashboard, under the order.
>
> I can cancel the order if that is useful, but that is a separate thing: it stops the order and restocks the items, and it does not move any money.

## Rules

- Read the order with `get_order` before you change it. Always.
- Confirm which order before any destructive action. Cancellation has no undo.
- Say out loud when an action emails the customer, before you take it if there is any doubt.
- Never substitute an adjacent action for one that is unavailable. A cancel is not a refund; a status change is not a payment record.
- One order at a time. There is no bulk action here, and there should not be one.
- Use the store's currency from `get_store` when quoting totals.
- If a fulfilment appears to have partly succeeded, read the order again rather than fulfilling twice. A second fulfilment can mean a second notification to the customer.

## Cross-skill connections

- Totals and trends across orders: `brainerce-analytics`.
- The morning view of what needs attention: `brainerce-daily-summary`.
- A store-wide sweep for orders stuck in one state: `brainerce-store-health`.
- Restocking after a cancellation: `brainerce-product-onboarding`.

Route once, and do not bounce back and forth.
