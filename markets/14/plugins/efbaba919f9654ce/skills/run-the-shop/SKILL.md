---
name: run-the-shop
description: How to run a WhizzyCommerce shop through its connector. Use when the merchant asks about their orders, products, prices, sales, customers, translations, settings or theme.
---

# Running a WhizzyCommerce shop

The WhizzyCommerce connector reads the merchant's shop and proposes changes to it.

## Reads

Tools that read (orders, products, customers, sales, stock, settings) return data directly. Read before you propose: look up the order, the products or the current prices first, so the proposal names real rows.

## Changes are proposals

A tool that would change the shop does not change it. It returns a preview of every row before and after, a `change_id` and a confirmation link.

- Show the merchant the summary and the link. Say plainly that nothing has changed yet.
- Only the merchant, signed in to the WhizzyCommerce dashboard, can confirm.
- To find out what happened, call `changes_status` with the `change_id`: pending, confirmed, rejected or expired.
- When one request takes several steps (a sale plus its discount code), use `propose_plan` so the merchant confirms once and the steps apply together.

## Design

Theme edits are drafts. They never reach the live shop until the merchant publishes them from Design in the dashboard. Tell the merchant where to look.

## Limits

- Money is in integer minor units (cents): 1999 is 19.99.
- The connection only offers the tools the merchant allowed. If a tool the request needs is missing, say which permission to add on the shop's Agents screen rather than working around it.
- No role includes refunds.
