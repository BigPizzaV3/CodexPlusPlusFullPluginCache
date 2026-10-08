---
name: brainerce-integration-verify
description: "Audit a Brainerce storefront against the mandatory-feature checklist and the critical rules, and report what is missing, present but unreachable, or wrong. Use when a developer says is my integration complete, check my Brainerce build, did I miss anything, review this before launch, why is this feature not working, or before shipping a storefront to a real store owner. Walks the actual code rather than trusting that a file exists, with particular attention to the features that are almost always skipped. For developers. Do not choose this to build something new, use brainerce-storefront-build. Do not choose this for one method's signature, use brainerce-sdk. Do not choose this for the correct order of a checkout or login sequence while writing it, use brainerce-checkout-flows. Do not choose this for a merchant auditing their shop's products and promotions, that is brainerce-store-health. Keywords: verify, audit, checklist, did I miss anything, pre-launch, mandatory features, critical rules, ready to ship."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Check a Brainerce integration honestly, feature by feature, against what is actually required.

## Core principle

Reachable in the running UI, or it does not count. A component that exists in the repo but no route renders is not an implemented feature, and reporting it as one is how storefronts ship with no password reset. Walk the code and trace each feature to something a customer can actually get to.

## When to use this skill first

- "Is my integration complete", "did I miss anything", "check this before launch".
- Handing a build to a real store owner.
- "This feature is not working and I do not know why".
- After following `brainerce-storefront-build`, as the closing step.

## When NOT to use this skill first

- Building something new: use `brainerce-storefront-build`.
- One method's signature: use `brainerce-sdk`.
- Getting a sequence right while writing it: use `brainerce-checkout-flows`.
- A shop owner auditing products and promotions in their store: that is `brainerce-store-health`, a merchant skill on a different tool surface.

---

## How to run the audit

### 1. Establish what is required

`references/required-features.md` is the checklist. `references/business-flows.md` carries the sequences each feature has to follow, and `references/critical-rules.md` the rules that cause incidents.

When the Brainerce MCP server is connected (Claude Code, Cursor, or the CLI), `get-required-features` with the connection id returns the list tailored to that store's live configuration. Prefer that. In ChatGPT there is no connection, so use the reference file and say that the audit is against the general checklist rather than that specific store.

⛔ **Mandatory features must exist even when the store has them switched off today.** They auto-hide, and the owner turns them on months later without touching the code. A build that omits them is not complete, it is a delayed outage. Do not mark a feature as not applicable because the store currently has it disabled.

### 2. Walk the code, feature by feature

For each item, find the code, then find the route or component that makes it reachable. Both, not either.

Pay closest attention to the ones that are almost always skipped:

- Email verification with a six-digit code
- Forgot password and reset password
- The OAuth button area and callback handling, including when no provider is currently enabled
- Coupon input in the cart
- The inventory reservation countdown, visible to the customer
- `handlePaymentSuccess` followed by `waitForOrder` on the confirmation page
- Sitemap built with the dedicated SDK helpers rather than a plain product list
- Slug-redirect handling on product and blog not-found paths

### 3. Check the critical rules against the code

- Prices parsed before arithmetic, everywhere, including totals
- Nested and flat line-item shapes handled as they actually arrive
- No auth token in browser storage without a backend-for-frontend
- No hardcoded currency, locale or store id
- No invented SDK methods

### 4. Report, then fix only what is approved

## Report shape

Three states, and use all three. A report that is all ticks was not an audit.

> ✓ Audit of your Brainerce integration. 14 of 19 mandatory features are reachable.
>
> **Implemented and reachable**
> - Product listing, product detail with variants, cart with persistence
> - Checkout through payment, with the reservation countdown visible
> - Registration and login
> - Order confirmation
>
> **Present but broken or unreachable**
> - `ResetPasswordForm.tsx` exists and no route renders it. A customer who forgets their password has no way in. `src/components/auth/ResetPasswordForm.tsx`
> - Coupon input is in the cart component but is behind a flag that is never set. `src/components/cart/CartSummary.tsx:82`
>
> **Missing**
> - Email verification. Registration completes and the account cannot be used. This is mandatory.
> - OAuth button area. The store has no providers today, so it looks unnecessary, but the owner enabling Google later would need a code change.
> - Sitemap uses `getProducts({ limit: 1000 })`, which the API caps at 100. Your sitemap silently lists 100 products.
>
> **Critical rule violations**
> - `src/lib/totals.ts:14` adds `item.price` without parsing. Prices are strings, so this concatenates.
>
> Want me to start with email verification? It is the one that blocks real customers today.

## Rules

- Trace every feature to something reachable. A file is not a feature.
- Cite file paths and line numbers. An audit without references cannot be acted on.
- Use all three states. "Present but unreachable" is the most useful finding and the one a shallow check misses.
- Never mark a mandatory feature not applicable because the store has it disabled.
- Report before fixing, and fix only what the developer approves.
- Say what you could not check, and why. An audit that quietly skipped the payment path is worse than one that says it did.
- Order findings by what blocks a real customer today, not by checklist order.

## Cross-skill connections

- Building what the audit found missing: `brainerce-storefront-build`.
- Getting a sequence right while fixing it: `brainerce-checkout-flows`.
- A method signature you need mid-fix: `brainerce-sdk`.

Route once, and do not bounce back and forth.
