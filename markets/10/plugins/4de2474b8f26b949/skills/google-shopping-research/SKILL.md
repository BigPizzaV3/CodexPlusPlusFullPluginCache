---
name: google-shopping-research
description: Find Google Shopping offers, merchants and product cards or expand a selected returned product with HasData. Use for Google Shopping data, not ordinary Google rankings or an automatic multi-store search.
---

# Research Google Shopping offers

Read `../hasdata-research/SKILL.md` and the Ecommerce section of `../hasdata-research/references/tool-catalog.md`.

Call `hasdata_google_serp_shopping_getSearchResults` with q and supplied localization. Retain the response and extract compact shoppingResults records before printing. Large bodies, duplicate content blocks and immersive tokens must not crowd out the products being compared.

Compare actual title/model/variant, merchant, listed price/currency, rating and available original source links. A productId, immersiveProductPageToken or hasdataLink is not an original merchant URL. If only a returned search source is available, label that source and mark original product links unavailable.

For selected product details, use `hasdata_google_serp_product_getProductInformation` with the exact returned productId and requested searchType. Immersive expansion uses `hasdata_google_serp_immersive_product_getImmersive_e29f691177` with pageToken equal to the returned immersiveProductPageToken. Do not fabricate tokens or expand every listing. Inspect the current schema for follow-up options and any extra-request implications.

Unconfirmed model matches stay distinct; the lowest sampled displayed price is not a verified delivered offer. For comparisons across Amazon, Walmart and Shopping, use `../product-research/SKILL.md`.
