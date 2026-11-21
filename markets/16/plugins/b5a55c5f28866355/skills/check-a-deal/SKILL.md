---
name: check-a-deal
description: "Check whether a price is a good deal: Deal.ai finds the exact item at every big US store right now. Use when the user shares a store link, asks whether a price is good, or asks if a sale or 'was' price is real."
---

# Check a deal

## How to run it

1. Call `check_deal` with the product: a link to it at any store, or its name (with model and size if the user gave them). Pass `price` when the user says what they were offered.
2. It answers at once with a `check_id`. Tell the user it's checking (it takes 20 to 70 seconds), then call `get_deal_check` with the `check_id`. Call it again every 10 to 15 seconds while its status is `running`.
3. When it's done, give the verdict sentence first (cheaper elsewhere, the lowest price, or the only store), then the stores' prices with their links, and whether the store's "was" price holds up when the answer has one.
4. End with the result page link: it's shareable.

## Rules

- A check that didn't finish says so: tell the user and offer to check again.
- Don't guess a verdict before `get_deal_check` returns one.
