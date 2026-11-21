---
name: product-research
description: Compare the same product or candidate products across requested marketplaces with HasData. Use for cross-store prices and model/variant matching; single Amazon, Walmart, Shopping and Shopify tasks have dedicated skills.
---

# Compare products and offers

Read `../hasdata-research/SKILL.md` for shared scope and safety, then the Ecommerce section of `../hasdata-research/references/tool-catalog.md` for the chosen source. Use its live input schema.

For a single requested source, use `../amazon-research/SKILL.md`, `../walmart-research/SKILL.md`, `../google-shopping-research/SKILL.md` or `../shopify-research/SKILL.md`. Do not automatically search the other marketplaces. For a cross-store comparison with unspecified stores, choose a small suitable available set and identify it rather than forcing the user to choose API names.

Start from the requested source, product query or supplied URLs. Use details for a named product only when its identifier or supported product URL is already available. If only a product name is supplied, search once on each explicitly requested marketplace within the request budget, then select matching returned records. Resolve Amazon ASINs, Walmart item IDs, Google product IDs and seller IDs from a clear supplied URL or a returned record. Never manufacture IDs or reuse one marketplace's identifier in another. If a name matches materially different models, ask for the intended model or keep those candidates distinct; do not present them as equivalent offers.

For multi-source searches, retain the original responses before emitting output when the host supports it. Process each source separately and return only the requested matching records with their titles, model/variant wording, prices, currencies, ratings and original product links where returned. Keep continuation IDs available for a selected follow-up, but do not print long tokens, duplicate response bodies or all raw listings. Follow the shared contract's compact-output handling so a large Shopping response does not erase the other sources' records.

Preserve region, delivery location, variant, quantity, seller and condition when those affect the comparison. Distinguish a product's displayed price, a marketplace offer and a computed total. Only calculate a total when returned components and their inclusion rules support it. Do not treat missing shipping, taxes or stock as zero or as available. Keep currency and source links with every offer. Do not compare different pack sizes as identical products.

Shopify tools read public storefront products and collections, not the user's Shopify administration. Use the supplied store URL and fetch only the requested page or bounded list. Do not claim access to orders, customers or inventory management.

For reviews, inspect the returned text, describe the sampled page and cite faithful short quotes. An overall listing rating is not the average of the reviews in this sample. Retain available sort and date context. Product and review filters must come from the chosen tool's schema, not another source's options.

Return a comparison answering the user's criteria, with unavailable fields visibly marked. A cheaper displayed price does not by itself establish the best delivered offer. Reading an offer does not reserve stock or purchase anything. Stop at the agreed request count and ask before additional pages or automatic price monitoring.
