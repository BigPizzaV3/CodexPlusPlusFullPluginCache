---
name: finance-help
description: Explain what Windsor.ai for Finance covers (Stripe, QuickBooks, PayPal, Xero, Chargebee, and Braintree), what it does not, and which skill handles a request. Use when the user asks what the app can do or asks for something outside its scope.
---

# What Windsor.ai for Finance can do

This app covers analyzing payments, subscriptions, and accounting data on the six finance sources above. Sources on this app: Stripe, QuickBooks, PayPal, Xero, Chargebee, and Braintree
(connector ids stripe, quickbooks, paypal_transaction (PayPal), xero, chargebee, braintree). Changes are possible only where a source exposes write actions (call list_actions; Stripe does, the accounting sources do not) and only after the user confirms. It does not cover ads, social, CRM, e-commerce, and web analytics data (each has its own Windsor.ai listing).

## Route the request
- Reports, rankings, comparisons, trends -> $finance-insights
- Connecting, reconnecting, adding an account -> $finance-connect
- Recurring exports and syncs -> $finance-export

## Answering "what can you do"
- Call get_connectors with include_not_yet_connected=True and answer from it: which of the six sources are connected, which are available to connect, and (per connector) which write actions and options exist. Do not list capabilities the tool result does not show.
- Reads are available on the free plan; write actions need an account with permission and write actions enabled at https://onboard.windsor.ai/app/settings/account.

## Out of scope
- Data from sources outside this app: name the Windsor.ai listing that covers them instead of attempting the read.
- Generating creative assets, general advice unrelated to connected accounts, or anything about plans and pricing.
