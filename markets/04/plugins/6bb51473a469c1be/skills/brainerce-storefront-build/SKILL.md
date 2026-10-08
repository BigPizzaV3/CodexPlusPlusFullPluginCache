---
name: brainerce-storefront-build
description: "Build a storefront on Brainerce, a headless commerce platform, in whatever framework the project already uses. Use when a developer says build me a store, scaffold a storefront, I have a Brainerce connection id, wire up the shop, add commerce to this site, or start a Brainerce project. Covers the ordered build path from store capabilities through catalog, cart and checkout, and the rules that cause production incidents when skipped. For developers. Brainerce is framework agnostic: Next.js, Remix, Astro, Nuxt and plain React all work. Do not choose this for merchant tasks such as adding a product or running a sale, those are brainerce-product-onboarding and brainerce-launch-a-sale. Do not choose this for one SDK method's exact signature, use brainerce-sdk. Do not choose this for the checkout sequence, use brainerce-checkout-flows. Do not choose this for content pages or blog, use brainerce-content-and-navigation. Keywords: storefront, headless commerce, scaffold, build a store, connection id, vc_, integrate."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Build a working Brainerce storefront: the right calls, in the right order, with the failures that bite in production already avoided.

## Core principle

Brainerce is headless and framework agnostic. It supplies commerce; the project supplies the framework, the routing and the design. Never rewrite someone's stack to suit an example. Customise design, copy and layout freely; do not customise SDK call sequences, business flows or auth handling, because those are where correctness lives.

## When to use this skill first

- "Build a storefront", "scaffold a shop", "add commerce to this site".
- The developer has a `vc_` connection id and wants to start.
- Wiring catalog, cart or product pages into an existing app.
- "What do I have to build for this to be a complete store".

## When NOT to use this skill first

- The exact signature, arguments or return shape of one SDK method: use `brainerce-sdk`.
- The checkout, auth, cart persistence or inventory reservation sequence: use `brainerce-checkout-flows`.
- Auditing a build that already exists against the required checklist: use `brainerce-integration-verify`.
- Anything a shop owner does in the dashboard rather than in code: use the merchant skills.
- Static pages, footers, the header's navigation links, announcements and the blog: use `brainerce-content-and-navigation`, which also carries the payload shapes and the sanitisation rule.

---

## Before the first line of code

**Get the connection id.** Every storefront call is scoped by one. It looks like `vc_...`. Without it there is nothing to build against, so ask for it before doing anything else rather than scaffolding against a placeholder.

**Read the store's actual capabilities.** Payment providers, OAuth providers, whether discounts and multi-language are on, which shipping is configured: these differ per store and they decide which parts of the UI have to exist. When the Brainerce MCP server is connected (Claude Code, Cursor, or the CLI), `get-store-capabilities` and `list-store-products` return this live. In ChatGPT there is no such connection, so ask the developer what the store has rather than assuming a default.

## The build order

Do these in sequence. Each step assumes the one before it.

1. **Client setup.** One configured client, created once, reused. See `references/setup.md`.
2. **Catalog.** Listing, filtering, a product detail page that handles variants and modifier groups rather than assuming a flat product. See `references/products.md`.
3. **Cart.** Persistence across reloads is not optional; a cart that empties on refresh reads as a broken shop.
4. **Auth.** Registration, the six-digit email verification, login, forgot and reset password, and the OAuth buttons if the store has providers configured.
5. **Checkout.** The one sequence you must not improvise. `brainerce-checkout-flows` owns it.
6. **Order confirmation.** The step most often left half-built, and the one the customer judges you on.
7. **Discoverability.** Sitemap from the SDK helpers, robots, structured data, slug-redirect handling. See `references/seo.md`. This is a real requirement, not a nice to have: the listing API caps its page size, so a sitemap built from a plain product list silently truncates.
8. **Localisation**, if the store runs more than one language. See `references/i18n.md`.

## Rules that cause incidents when skipped

Read `references/critical-rules.md` in full before writing SDK code. The ones that catch people most often:

- **Prices come back as strings.** Parse before arithmetic. String concatenation instead of addition is a real bug that ships.
- **Never store an auth token in the browser** without a backend-for-frontend in front of it.
- **Never hardcode currency, locale or store id.** Read them from the store.
- **Do not invent SDK methods.** If it is not in the reference, it does not exist, and a plausible-looking call that 404s at runtime is worse than asking.
- **Line items are nested in some shapes and flat in others.** Check which one you have rather than assuming.

## Mandatory features

Some features have to be reachable in the finished build even when the store has them switched off today. They hide themselves at runtime and the owner enables them later, so a build that omits them breaks the day the owner turns the feature on. Coupon input in the cart, email verification, password reset, the OAuth button area and the reservation countdown are the ones most often missed.

`brainerce-integration-verify` carries the full checklist. Run it before you call the build done.

## Response shape

> ✓ Catalog and product pages are wired to your Brainerce store.
>
> Built: product listing with category filter, product detail with variant selection and modifier groups, cart with persistence across reloads.
>
> Not built yet, and all three are on the mandatory list: checkout, auth with email verification, order confirmation.
>
> Checkout next? It has a fixed sequence and I want to get it right rather than fast.

## Reference files in this skill

- `references/setup.md`: client creation and configuration.
- `references/products.md`: catalog, variants, modifier groups, product shape.
- `references/critical-rules.md`: the rules above, in full, with examples.
- `references/seo.md`: sitemap helpers, robots, structured data, slug redirects.
- `references/i18n.md`: multi-language routing and locale resolution.

These are snapshots taken from the Brainerce MCP server's own content. When that server is connected, prefer its live tools, which reflect the specific store. In ChatGPT it is not, and these files are the source of truth.

## Cross-skill connections

- One method's exact shape: `brainerce-sdk`.
- Checkout, auth, cart and reservation sequences: `brainerce-checkout-flows`.
- Auditing what you built: `brainerce-integration-verify`.
- Content entries, navigation and blog, including the fact that page and rich-text HTML arrives unsanitized: `brainerce-content-and-navigation`.
- Rendering custom fields and building a filter UI from the filterable ones: `brainerce-custom-fields`.

Route once, and do not bounce back and forth.
