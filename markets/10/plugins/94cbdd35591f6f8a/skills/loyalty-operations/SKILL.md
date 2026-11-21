---
name: loyalty-operations
description: Reviews and safely changes a connected CrumbPass restaurant's loyalty programme, rewards, and offers. Use when an owner wants to create or change points rules, reward rules, coupons, promotions, expiry dates, offer status, or offer performance.
---

# Loyalty operations

All tools act only on the restaurant selected during OAuth. Read current state before changing it.

1. Call `get_loyalty_program` for programme changes. Call `list_offers` before changing a specific offer, and use `get_offer` for its exact current state.
2. For a loyalty-programme or existing-offer edit, call `update_loyalty_program` or `update_offer` without `confirm` first. Present the returned diff in plain language.
3. Ask for explicit approval. Only after the owner says yes, call the same tool with the same intended fields and `confirm: true`.
4. `create_offer` always creates a draft. Review the draft, then use `set_offer_status` with `confirm: true` only after approval to activate, schedule, pause, or archive it.
5. `create_reward` creates a draft reward. Do not present a draft as live.

## Guardrails

- Never turn on an offer, change coin value, alter earn rules, or change redemption limits without an explicit owner confirmation in the conversation.
- Clarify ambiguous benefits, audience, duration, and discount type before creating an offer.
- Explain customer impact for point expiry, coin value, redemption percent, and reward eligibility changes.
