---
name: brainerce-checkout-flows
description: "Get the non-negotiable Brainerce sequences right: checkout, registration and email verification, login, password reset, cart persistence, inventory reservation and order confirmation. Use when a developer is building or debugging any of those, or asks why is my order not appearing, the payment succeeded but nothing happened, my reservation expired, the cart empties on refresh, or what order do these calls go in. These flows are fixed regardless of framework, and improvising one produces orders that never complete and stock that never releases. For developers. Do not choose this for the signature of a single method, use brainerce-sdk. Do not choose this to plan a whole storefront, use brainerce-storefront-build. Do not choose this for a merchant asking where a specific customer order is, use brainerce-order-handling. Keywords: checkout, payment, order confirmation, handlePaymentSuccess, waitForOrder, reservation, cart persistence, login, email verification, reset password, OAuth callback."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Implement the sequences that have to happen in a fixed order, in the fixed order.

## Core principle

These flows are not conventions and they are not style. Each step exists because the step after it depends on state the step before it created. Reordering them, or dropping a step that looks redundant, produces failures that are silent at build time and expensive at runtime: payments taken with no order attached, stock held forever, customers stranded on a spinner.

Framework is irrelevant here. The sequence is the same in Next.js, Remix, Astro, Nuxt and plain React.

## When to use this skill first

- Building checkout, cart, auth or order confirmation.
- "What order do these calls go in".
- Debugging: payment succeeded but no order, reservation expired mid-checkout, cart empties on refresh, verification email never arrives, OAuth callback lands nowhere.
- Anything where the calls look individually right and the outcome is wrong.

## When NOT to use this skill first

- One method's arguments or return type: use `brainerce-sdk`.
- Planning or scaffolding the whole storefront: use `brainerce-storefront-build`.
- Auditing what is already built: use `brainerce-integration-verify`.
- A merchant asking about a real customer order in their shop: use `brainerce-order-handling`, which is a different tool surface entirely.

---

## The flows, and where each one is written down

`references/business-flows.md` is the authoritative sequence list. Read the relevant flow there before writing code, not after the first bug.

| Flow | Reference | The step people drop |
|---|---|---|
| Checkout end to end | `references/checkout.md` | Confirming the order after payment returns, rather than assuming payment success means order created |
| Payment | `references/payment.md` | Handling the provider callback and the return path separately |
| Order confirmation | `references/order-confirmation.md` | `handlePaymentSuccess` followed by `waitForOrder`; without the wait the page renders before the order exists |
| Cart | `references/cart.md` | Persistence across reloads and across login |
| Inventory reservation | `references/inventory.md` | Showing the countdown, and releasing the hold when the customer leaves |
| Registration and login | `references/auth.md` | The six-digit email verification step, forgot and reset password, and the OAuth callback |

## The four failures worth naming up front

**"Payment succeeded but no order appeared."** The confirmation page rendered before the order existed. Payment success and order creation are not the same event and they do not land at the same moment. Call `handlePaymentSuccess`, then `waitForOrder`, then render. A confirmation page that reads the order straight out of the URL will work in testing and fail under real latency.

**"Stock is held and never comes back."** The reservation was created and never released. Reservations expire on their own, but a customer who abandons checkout should not wait out the timer, and the countdown has to be visible or they will not understand why the item vanished.

**"The cart empties when the page reloads."** Cart state was kept only in memory. Persistence is part of the flow, not an optimisation, and the cart also has to survive a customer logging in mid-session.

**"Customers cannot finish signing up."** Email verification with a six-digit code is a required step, and it is the single most commonly omitted piece of a Brainerce auth build. Registration without it produces accounts that exist and cannot be used.

## Rules

- Follow the reference sequence exactly. If a step looks redundant, it is load-bearing for something further down.
- Never treat a payment provider's success signal as proof the order exists.
- Always show the reservation countdown to the customer, and release the hold on abandonment.
- Build email verification, forgot password and reset password even if the brief did not mention them. They are mandatory features, not extras.
- Build the OAuth button area and callback handling even when the store currently has no providers configured. The area hides itself, and the store owner turns providers on later without touching the code.
- Never store an auth token in the browser without a backend-for-frontend in front of it.
- Prices are strings. Parse before arithmetic, including inside totals on the confirmation page.
- When debugging, walk the sequence in order and find the first step that did not happen. The visible symptom is almost never at the broken step.

## Response shape

> The order is missing because the confirmation page renders before it exists. Payment success and order creation are two separate events.
>
> The sequence has to be:
>
> 1. Provider returns to your confirmation route
> 2. `handlePaymentSuccess` with the payment reference
> 3. `waitForOrder`, which polls until the order is really there
> 4. Only then render the order
>
> Right now step 3 is missing, so under real network latency you render an empty page. It passes in testing because local round trips are fast enough to hide it.

## Reference files in this skill

`business-flows.md`, `checkout.md`, `payment.md`, `order-confirmation.md`, `cart.md`, `inventory.md`, `auth.md`.

These are snapshots of the Brainerce MCP server's own content. When that server is connected (Claude Code, Cursor, or the CLI), `get-business-flows` and `get-sdk-docs` serve the same material live. In ChatGPT it is not connected, and these files are the source of truth.

## Cross-skill connections

- Method signatures and types: `brainerce-sdk`.
- Planning the whole build: `brainerce-storefront-build`.
- Checking a finished build against the mandatory list: `brainerce-integration-verify`.

Route once, and do not bounce back and forth.
