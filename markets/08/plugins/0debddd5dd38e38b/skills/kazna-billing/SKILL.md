---
name: kazna-billing
description: Explain Kazna author balances, ledger operations, and payout request status using read-only MCP tools.
---

# Kazna billing

Use MCP server `Kazna`.

## Steps

1. Call `billing_summary` and explain available balance, pending payouts, lifetime earned, last payout.
2. If the user wants detail, call `list_billing_operations` (default limit 5–20).
3. Optionally call `list_payouts` to show existing payout requests and statuses.

## Constraints

- Never initiate, create, or cancel payouts.
- If asked to withdraw money, refuse and say payouts are started only on kazna.online.
