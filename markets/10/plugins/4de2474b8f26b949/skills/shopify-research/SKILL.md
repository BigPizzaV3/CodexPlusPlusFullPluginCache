---
name: shopify-research
description: Read public products or collections from a supplied Shopify storefront with HasData. Use for catalog research and product comparisons, not Shopify orders, customers, private inventory or store administration.
---

# Read a public Shopify catalog

Read `../hasdata-research/SKILL.md` and the Ecommerce section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_shopify_products_getProducts` with the supplied public storefront url for products, or `hasdata_shopify_collections_getCollections` for collection discovery. Ask for the store URL when absent, not an admin connection or API key.

Start with the requested bounded limit/page. The products tool's collection field takes a collection handle, not a numeric collection ID. Use a clearly supplied handle, one returned by collection discovery, or the unambiguous handle in the store's /collections/<handle> URL. Do not pass a numeric ID as a handle. Do not fetch every collection followed by all its products when one page answers the request.

Return observed product/variant names, prices/currencies and original links where available. Keep variant prices and availability separate rather than collapsing different options into a single invented offer. Public storefront records are not access to orders, customer lists, unpublished products or warehouse stock. No admin writes or checkout.
