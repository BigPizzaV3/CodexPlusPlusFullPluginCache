---
name: after-sale-support
description: Work through a brand's after-sale side in Veribl: product registrations, warranty plans, warranty claims and support tickets. Use when the user asks about claims, registrations, warranty coverage or customer tickets.
---

# After-sale support

- **Overview:** `list_registrations`, `list_warranty_plans`, `list_claims`, `list_tickets` (filter by status where the user asks, e.g. open or overdue).
- **One case:** `get_claim` or `get_ticket` shows the messages, photos, proof of purchase and history. Summarize what the customer reported, what's missing and what the warranty plan covers.
- **Replying:** draft the reply in the chat first. Only send with `reply_to_claim` / `reply_to_ticket` after the user approves the exact text: the customer receives it.
- **Decisions:** `act_on_claim` (approve, deny, ask for information…) only on the user's explicit instruction, never on your own judgment.

Never promise a refund, replacement or repair the user hasn't decided.
