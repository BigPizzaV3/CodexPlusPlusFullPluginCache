---
name: manage-account
description: Use when the user asks about their credit balance, account details, or profile.
---

# Account and credit

- `get_user_credit` — the current available credit balance.
- `get_user_details` — account profile (name, phone, credit, username, email).

## Notes

- Report the returned balance without inventing a currency or changing credit.
- Present requested profile fields accurately; omit internal roles, authentication secrets, and unnecessary internal IDs.
- Neither tool places orders or modifies the account.

## Out of scope

Invoice management, payments, refunds, credit purchases and subscriptions are not exposed in this plugin. Explain these limits when asked. If an order cannot run because of insufficient credits or another entitlement, explain the returned reason without initiating payment or promoting an upgrade. Do not provide checkout, top-up or purchase-initiation links. For billing questions, refer to the public IMEILookup support page.
