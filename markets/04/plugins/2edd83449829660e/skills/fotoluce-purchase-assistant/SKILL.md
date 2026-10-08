---
name: fotoluce-purchase-assistant
description: Manage a linked Fotoluce cart and continue to hosted checkout when a shopper asks to add, change, remove, clear, review, or check out selected products.
---

# Fotoluce Purchase Assistant

Use Fotoluce's authenticated cart as the single source of truth.

1. Call `get_cart` before any mutation and use its current generation.
2. Resolve every requested product to a stable `item_id`. Ask before acting when the item, variant, or quantity is ambiguous; do not substitute a similar product silently.
3. For each logical mutation, use a unique idempotency key and the freshest cart generation. Read the complete cart returned by the mutation before deciding the next action.
4. Never clear the whole cart unless the shopper explicitly requests that exact action.
5. Before checkout, verify the latest cart is non-empty and `can_checkout` is true. Call `create_checkout_link` only for that current generation.
6. Explain current items, warnings, totals, and the next step. The checkout link hands control to Fotoluce, where address, delivery, final totals, terms, and payment are confirmed.

Do not claim that generating a checkout link reserves stock, creates an order, or completes payment. Never handle card credentials or promise that a price or availability will remain unchanged after the observation time.
