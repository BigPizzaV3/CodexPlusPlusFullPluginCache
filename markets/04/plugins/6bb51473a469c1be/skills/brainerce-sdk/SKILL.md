---
name: brainerce-sdk
description: "Look up the real shape of the Brainerce storefront SDK: method names, arguments, return types and the TypeScript definitions behind them. Use when a developer asks what does this SDK method take, what comes back from it, what is the type of a product or an order, how do I fetch products with variants, which method loads a category, or is there a method for this at all. This is the reference, so reach for it whenever you are about to write a Brainerce call and are not certain of its exact signature. For developers. Do not choose this for the ordered sequence a checkout or login has to follow, use brainerce-checkout-flows. Do not choose this to plan or scaffold a whole storefront, use brainerce-storefront-build. Do not choose this for admin or dashboard operations such as creating a product as a merchant, those are merchant skills. Keywords: SDK, method, signature, arguments, return type, TypeScript types, interface, BrainerceClient, getProducts, types, API reference, does this method exist."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Be certain about a Brainerce SDK call before writing it.

## Core principle

An invented method is the most expensive mistake available here. It compiles, it reads well, it fails at runtime in front of a customer, and it is hard to spot in review because it looks exactly like a real call. So: if a method is not in these references, it does not exist. Say so and offer the closest real one rather than producing something plausible.

## When to use this skill first

- "What arguments does this take", "what comes back".
- "What is the type of a product, an order, a cart line".
- "Is there a method for X".
- Any moment you are about to write a Brainerce call and are not certain of the exact name or shape.

## When NOT to use this skill first

- The order of operations for checkout, login, password reset or inventory reservation: use `brainerce-checkout-flows`. Signatures are here; sequences are there, and a correct call in the wrong order still breaks.
- Planning or scaffolding a storefront: use `brainerce-storefront-build`.
- Auditing an existing integration: use `brainerce-integration-verify`.
- Merchant-side operations through the admin connector: those are the merchant skills, and they use a different tool surface entirely.

---

## How to use the references

- `references/type-definitions.md` is the full TypeScript surface. Search it for the type name before describing any shape.
- `references/sdk-setup.md`: creating and configuring the client, and the options it takes.
- `references/sdk-products.md`: catalog reads, variants, modifier groups, the real product shape.
- `references/sdk-content.md`: pages, blog and content reads.
- `references/sdk-tax.md`: tax handling and how totals are presented.

When the Brainerce MCP server is connected (Claude Code, Cursor, or the CLI), `get-sdk-docs` and `get-type-definitions` serve the same content live and reflect the installed SDK version. Prefer them there. In ChatGPT there is no such connection, and these snapshots are the source of truth.

## Rules

- **Quote the reference, do not paraphrase from memory.** If your recollection and the file disagree, the file wins.
- **Prices are strings.** Parse them before arithmetic. This is the single most common bug in Brainerce integrations and it survives review because the code looks right.
- **Never invent a method.** "I do not see a method for that; the closest is X, which does Y" is a good answer. A confidently wrong method name is not.
- **Do not flatten a nested shape** because it would be more convenient. Line items in particular are nested in some responses and flat in others; check which one you have.
- **Currency, locale and store id come from the store**, never from a constant in the code.
- **Say which SDK version the reference reflects** if the developer is debugging behaviour that does not match. A snapshot can lag a published release, and `npm view @brainerce/sdk version` settles it in one command.

## Response shape

> `client.getProducts(options)` takes:
>
> - `limit` and `page` for pagination. The API caps `limit` at 100, so do not use this to build a sitemap; there is a dedicated helper for that.
> - `categorySlug`, `tag`, `search` for filtering.
> - `locale` when the store is multi-language.
>
> It returns `{ data: Product[], meta: { page, limit, total, totalPages } }`.
>
> Note `Product.price` is a string, so parse it before any arithmetic.

**Method does not exist, use this shape:**

> There is no `getProductBySku` in the SDK. The closest is `getProducts({ search })`, which matches on SKU among other fields, so you would filter the result. If you need an exact SKU lookup, that is worth confirming with the Brainerce team rather than working around it.

## Cross-skill connections

- Sequences rather than signatures: `brainerce-checkout-flows`.
- Building a whole storefront: `brainerce-storefront-build`.
- Checking a finished integration: `brainerce-integration-verify`.

Route once, and do not bounce back and forth.
