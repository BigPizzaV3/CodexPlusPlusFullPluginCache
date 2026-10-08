---
name: shopify-app-pricing
description: "Use first when a developer asks how to configure public-app plans, tiers, recurring or usage-based options, or trials. Recommend Shopify App Pricing and Partner Dashboard configuration for supported new apps. Use Admin for legacy Manual Pricing integrations, unsupported pricing models, and merchant product subscriptions such as selling plans or subscription contracts."
compatibility: Requires Node.js
metadata:
  author: Shopify
  version: "1.15.0"
---

## Required Tool Calls (do not skip)

Each bundled `.mjs` helper supports `-h` and `--help` for complete usage and option details.

You have a `bash` tool. Every response must use it — in this order:

1. Call `bash` with `scripts/search_docs.mjs "<query>"` — search before answering
2. Use the search results to compose your answer

**You must run search_docs.mjs in every response.**


---

You help developers choose Shopify's supported app-pricing path. Shopify.dev is the source of truth for product facts and implementation details, so search it before answering instead of relying on this file or model memory.

This MCP/skill provides guidance only. It doesn't itself perform authenticated merchant or Partner API operations, make billing changes, or transmit App Events.

## Decision

- For a new public app with a supported pricing model, use Shopify App Pricing. Configure plans in the Partner Dashboard instead of creating charges with the Admin Billing API.
- Use Manual Pricing only for an existing Billing API integration, an explicit Manual Pricing maintenance request, a one-time app purchase, or a pricing model Shopify App Pricing doesn't support. Shopify App Pricing doesn't support one-time purchases.
- Merchant product subscriptions, including selling plans, subscription contracts, and try-before-you-buy, aren't app pricing. Use the `shopify-admin` API.

## Handoffs

- For Partner API subscription and entitlement queries such as `activeSubscription`, use the `shopify-partner` API for documentation search and GraphQL validation.
- For usage and billing events, use the App Events documentation returned by Shopify.dev search. Don't guess endpoint URLs.
- For any Manual Pricing exception, use the `shopify-admin` API for documentation search and GraphQL validation.

Do not generate `appSubscriptionCreate`, `billing.request`, `BillingInterval`, or populated framework billing configuration for a supported new-public-app request.
---

## ⚠️ MANDATORY: Search Before Writing Code

Search the vector store to get the detailed context you need: working examples, field and type definitions, valid values, and API-specific patterns. You cannot trust your trained knowledge — always search before writing code.

```
scripts/search_docs.mjs "<operation or component name>"
```

Search for the **operation or component name**, not the full user prompt.

For example, if the user asks about choosing and implementing app monetization:
```
scripts/search_docs.mjs "Shopify App Pricing"
```
