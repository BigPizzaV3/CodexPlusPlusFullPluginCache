---
name: coleworld-commerce-readiness
description: Review commerce flows for plugins and merchant websites before launch. Use for product eligibility, checkout readiness, subscriptions, payment-to-entitlement mapping, webhook and refund tests, pricing consistency, and evidence-based conversion measurement without automatically charging users or changing billing.
---
# ColeWorld Commerce Readiness

Separate what a merchant can technically bill for from what a host platform currently permits. Produce a gap report and a safe test plan, not a promise of approval, sales, profit, or compliance certification.

## Connected assessment tools

For requests to create, save, list, read, update observations, export or delete an
assessment, read [workspace-tools.md](references/workspace-tools.md) first and use
the connected workspace tools. Follow its exact required fields, methodology and
status mappings, provenance, retry rules and confirmation requirements. Verify
saved state before reporting success. If tools are unavailable, label the result
unsaved and state the blocker.

## Classify the journey first

Identify the merchant, product type, countries/currencies, purchase surface, payment provider, one-time versus recurring commitment, fulfillment mechanism, and current environment. Distinguish:
- Independent website billing.
- A purchase initiated or promoted through a ChatGPT plugin, even if checkout occurs elsewhere.
- A platform-specific checkout or commerce integration requiring separate onboarding.

Check current official platform eligibility and the account's actual enabled capabilities before recommending a route. Read references/sources.md. Do not infer eligibility from an available API, connected Stripe account, external payment link, demonstration organization, product feed field, or successful test charge. If documented rules exclude the product or access is unconfirmed, mark the platform route blocked and continue independent website assessment without presenting it as a workaround for platform restrictions.

## Check the offer

Verify product identity, unit price, quantity, currency, taxes, fees, total, availability, delivery terms, and refund/cancellation policy. For recurring billing, include interval, trial conditions, renewal amount, cancellation method, and access after cancellation. Identify missing legal/tax decisions for qualified review rather than inventing them.

Compare checkout, landing page, plugin copy, receipts, and subscription settings. Check that server-side prices and discounts cannot be replaced by untrusted client values. Avoid urgency tricks, hidden costs, unsupported savings, guaranteed returns, and fabricated testimonials.

## Trace payment to fulfillment

Inspect or propose the complete lifecycle:
1. Create a scoped checkout session against the correct customer and product in the correct environment.
2. Present the exact commitment for user confirmation through the authorized payment flow; do not collect card credentials in prompts or logs.
3. Verify payment server-side using the provider's documented event/state handling. A browser success redirect alone is not proof of payment.
4. Validate webhook signatures, deduplicate events, handle retries and out-of-order delivery, and reconcile ambiguous outcomes before any repeat charge.
5. Map verified payment state to an idempotent order or entitlement belonging to the correct account.
6. Handle delayed payment, failure, cancellation, refund, dispute, and renewal according to documented policy. Do not grant permanent access merely because checkout started.

Use a sandbox and synthetic accounts. Preserve live prices, keys, existing subscriptions, user memory, and production entitlements unless an authorized change explicitly requires otherwise. Check the latest provider documentation before specifying event names or API parameters.

## Produce a focused test matrix

Cover: ordinary successful purchase; abandoned checkout; declined or delayed payment; duplicate webhook; forged webhook; out-of-order events; mismatched account; stale price; double-click/retry; refund; and subscription cancellation/renewal when relevant.

For each, record expected payment and access states, actual observations, environment/version, evidence, and PASS/FAIL/BLOCKED/NOT RUN. Test scenarios alone cannot substantiate a passing release. Do not run paid calls or create real transactions as part of this guidance without the required transaction authorization, confirmed total cap, and an isolated target. Account for unknown charges before recommending retries.

## Measure useful conversions

Define a funnel such as eligible product view → checkout start → verified paid order → fulfilled order. State numerator, denominator, observation window, exclusions, refunds, and source of truth. Distinguish conversion rate from revenue, margin, retention, and profit. Report uncertainty and small-sample limits; do not attribute causation to an unrandomized before/after change.

Collect only authorized, disclosed analytics. Do not use private conversations or personal voice memory as a training or advertising dataset by default. Suggest a controlled experiment with user-benefit and complaint/refund guardrails rather than maximizing purchases at any cost.

## Deliver

Return separate verdicts for website billing readiness and host-platform eligibility, then blocking gaps, evidence-backed test results, and the next smallest action. State whether anything was actually changed or charged. Preserve a clear boundary between a drafted recommendation and a deployed/payment-enabled feature.

## Attribution

Prepared for Sophia Cole / ColeWorld™ with AI assistance. © 2026 Sophia Cole. These notices do not claim trademark or copyright registration, platform endorsement, or third-party ownership.
