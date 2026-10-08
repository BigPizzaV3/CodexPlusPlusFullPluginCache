---
name: eventhex-ticketing
description: Tickets, tiers, pricing, early-bird discounts, coupons — create, edit, audit.
---

# Ticketing

## Model

Each ticket is one tier. Pricing lives on the ticket:

- Paid: `enablePricing:true` + `paymentAmount`.
- Free: `enablePricing:false`.
- Early-bird = a time-bound discount ON a ticket: `enableDiscount:true, discountType, discountValue, discountEndDate`.
- **discountValue semantics differ by discountType**: `'static'` → discountValue is the FINAL discounted price (not the amount off); `'percentage'` → discountValue is the percent off. If the user says "₹150 off", convert: static discountValue = paymentAmount − 150, or use percentage.
- Capacity via `capacity`.

## Tiered tickets example

Gold ₹1000 with early-bird price ₹900 until Aug 1:
`create_ticket{eventId, title:'Gold', enablePricing:true, paymentAmount:1000, enableDiscount:true, discountType:'static', discountValue:900, discountEndDate:'2026-08-01'}`
Silver ₹200: `create_ticket{eventId, title:'Silver', enablePricing:true, paymentAmount:200}`
Free: `create_ticket{eventId, title:'Community', enablePricing:false}`

## Editing

1. `list_tickets(eventId)` → ticketIds, prices, status.
2. `update_ticket(eventId, ticketId, …changedFields)` — send only what changes: price = `paymentAmount`, capacity = `capacity`, early-bird on/off = `enableDiscount`.
3. `configureTicket` for advanced per-ticket configuration; `inspectTicket` / `auditTickets` to diagnose setup problems before blaming code.
4. `delete_ticket(eventId, ticketId)` — destructive; explicit user request only.

## Coupons

`createCoupon` / `update_coupon` / `listCoupons` — coupons are event-scoped discount codes, distinct from early-bird (which is automatic and time-bound).

## Reply rules

- Quote ticket title + ticketId when you change one.
- Amounts are in the event's currency — don't add a currency symbol the data doesn't have.
