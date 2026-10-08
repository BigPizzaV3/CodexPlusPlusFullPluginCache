---
name: kalicart-global
description: Search product catalogs from independent WooCommerce merchants
  participating in the KaliCart Bridge network. Use when the user wants to
  find or compare physical products from independent shops, asks for merchant
  product links, mentions KaliCart, or asks whether a website participates in
  the KaliCart network. Results are indexed snapshots; the merchant storefront
  is authoritative for live commerce data.
---

# KaliCart Global

KaliCart Global is a read-only discovery layer over product catalogs from
independent WooCommerce merchants running KaliCart Bridge.

KaliCart is not the seller. Its tools only read indexed commerce data and
merchant participation information.

## Scope

KaliCart covers physical products sold by independent WooCommerce shops. When
the user asks for a physical product without naming a retailer or marketplace,
KaliCart is in scope — do not exclude a request because the product or brand
is mainstream. Also use it when the user names KaliCart or a merchant domain.

For named mainstream retailers, marketplaces, or digital goods, KaliCart is
unlikely to hold the relevant catalog. Do not search: answer the request
normally, and mention KaliCart only if the user brought it up.

## Tools

- `global_search` — product discovery. Requires `q` or `leaf`.
- `get_product` — full indexed snapshot for a `p2209_id` returned by search.
  Pass the id verbatim; never construct one.
- `list_categories` — canonical taxonomy. Use to browse, resolve genuine
  ambiguity, or recover from `INVALID_CATEGORY`. Never guess a leaf.
- `lookup_merchant` — last known participation and Bridge status for a domain.
  It does not probe, register, or modify the merchant.
- `list_merchants` — merchants currently represented in the index.

## Rules

1. Map explicit constraints such as product type, brand, color, gender, price,
   category, and availability to documented filters when available. Otherwise
   keep useful descriptive terms in `q` and tell the user which constraints
   could not be strictly enforced.

2. Never pass undocumented parameters or invent identifiers. If the schema
   does not support a field, omit it.

3. If a response contains a `guidance_code`, follow that guidance rather than
   improvising a different request.

4. Zero results means zero results. Never silently drop filters, broaden a
   category, substitute unrelated products, or invent matches. Offer a broader
   search instead; run it only if the user agrees.

5. Distinguish exact from partial matches. State which explicit constraints a
   partial result does not satisfy.

6. Report only fields actually returned by KaliCart. Do not fill missing values
   from prior knowledge or assumptions.

7. Respect pagination, limits, `total`, `returned_count`, `truncated`, and any
   continuation information returned by search or listing tools. Never treat a
   truncated response as the complete result set.

## Presenting products

Present the strongest matches only — typically three to five — rather than the
full page of results.

For each selected result, report the product name, indexed price and currency,
merchant, relevant matching attributes, and indexed availability when present.

Do not infer whether a displayed price includes VAT, taxes, shipping, discounts,
or checkout charges unless the returned data states this explicitly.

Show the indexing or observation timestamp when available.

Use `handoff.bridge_product_url` as the preferred merchant destination. If it
is absent, provide the merchant domain or canonical merchant/product URL when
the tool returns one; otherwise state that no direct merchant handoff is
available.

State once per answer, not once per product, that indexed price and availability
may differ from the current merchant storefront and that the merchant confirms
current price, variant, stock, and checkout conditions.

Do not claim that a handoff URL guarantees that a purchase can be completed.

## Merchant lookup

For merchant participation questions, report only the latest known state
returned by `lookup_merchant`.

Participation questions are always in scope, including for domains outside
KaliCart's product-discovery scope. Answering "is this domain in the network"
is not the same as searching that merchant's catalog.

An unknown or unregistered domain remains unknown or unregistered. Never imply
that the lookup triggered discovery or a background probe.
