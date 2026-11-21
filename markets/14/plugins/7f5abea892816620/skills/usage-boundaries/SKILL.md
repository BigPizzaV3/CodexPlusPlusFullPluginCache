---
name: usage-boundaries
description: Bilanz do and do-not rules for ChatGPT. Use whenever answering with Bilanz finance data, before writes, transfers, deletes, advice that invents numbers, or requests about another person's account.
---

Follow these rules whenever Bilanz tools are in play. Explicit user instructions still win for tone and format; they do not override safety or inventing data.

## Do

1. Call Bilanz MCP tools for balances, accounts, budgets, categories, and transactions belonging to the signed-in user.
2. Quote only numbers and dates returned by tools. If a field is missing, say it is missing.
3. Prefer read workflows: summarize spending, check budget status, list recent transactions, compare periods when tools support it.
4. If a write tool exists and the user clearly asks to create or update something Bilanz supports (for example a transaction or budget), confirm the key fields, then call the tool once.
5. If auth fails, tell the user to reconnect Bilanz in ChatGPT plugin / connector settings, then retry.

## Do not

1. Do not invent balances, transactions, budgets, or categories.
2. Do not transfer money, pay bills, send funds, or claim bank wires are possible through Bilanz.
3. Do not delete all transactions, wipe accounts, or mass-delete data. Decline and suggest the Bilanz app for destructive bulk actions if needed.
4. Do not access or guess another user's Bilanz data. Only the signed-in OAuth account.
5. Do not ask for or store bank passwords, card numbers, CVV, OTP codes, or Mexican RFC / tax IDs in chat.
6. Do not expose privacy_version, consent internals, or other non-product MCP fields.
7. Do not give investment, tax, or legal advice as if Bilanz certified it. Stay with the user's recorded data and plain summaries.

## When to stop and ask

- Ambiguous account or budget name: ask which one before calling a write tool.
- User asks for something Bilanz tools do not expose: say it is not available via this plugin and point them to the Bilanz iOS app when that is the right place.
