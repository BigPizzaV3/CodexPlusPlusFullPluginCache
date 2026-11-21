---
name: public-fees-and-fx
description: Look up Payvora's public fee schedules and dated indicative FX snapshots when the user asks about Payvora pricing or reference exchange rates.
---

Use the Payvora MCP server's advertised read-only tools for the user's public-information request. No account connection or credentials are needed.

For fees, call query_fee with a small limit and a relevant filter when supported by the published data. Report the exact fee type, amount or percentage, currency and conditions returned. Distinguish published indicative fees from a personalized or executable payment quote. Do not invent fees for a missing service or corridor.

For reference exchange rates, call query_fxratesnapshot with a small limit and descending snapshot date. Identify the returned snapshot's date, base currency and source when available. These snapshots are daily reference data, not live executable quotes. Explicitly state if a snapshot is stale, its source is absent, or the requested currency is unavailable. Never claim that a tool returned a current live rate when it only returned a historical snapshot.

If deriving a cross-rate from a USD-based snapshot, use the same snapshot for both currencies. Divide the target currency's USD-based rate by the source currency's USD-based rate, state that the result was calculated, and round only for presentation. State that this excludes fees and does not reserve or execute an exchange.

Request only the fields needed for the question. Do not include platform record metadata, creator identifiers or unrelated fields in the answer. An empty result is an absence of published data, not proof that a product is offered or unavailable.

This plugin has no tools to access private accounts, wallets, cards, personal transactions, logs, KYC or application records. It cannot create or execute payments, money transfers, crypto transfers or investment trades. If the user requests such an action, explain the limitation and direct them to Payvora's own website without collecting passwords, verification codes, card details, account numbers or identity documents.

Payvora is operated by Dune Payments Limited, a financial technology company, not a bank. State service eligibility and provider-approval limitations when relevant. Do not infer regulatory approval, deposit insurance, guaranteed settlement, investment suitability or returns from public marketing information.
