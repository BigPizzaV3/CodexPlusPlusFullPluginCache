---
name: grocery-prices
description: Find or compare Vynn grocery and household-product prices by product name, brand, or barcode near a supported Canadian city or postal code. Use for Vynn price searches and barcode comparisons. Unsupported requests include locations outside Canada, historical charts, all-retailer catalogues, purchases, and deliveries.
---

# Vynn Grocery Prices

Use the connected Vynn MCP server for read-only Canadian product lookups.

1. Determine exactly one location: a supported Canadian city or the Canadian postal code supplied by the shopper. Ask for a location if missing. Suggest only city names in the tool's `city` enum. For another Canadian city, ask for a Canadian postal code; do not replace it with a supported city.
2. Use `search_products` for a product name or brand, or `lookup_product` for a UPC, EAN, or GTIN barcode. Send the supplied postal code only in the tool's `postal` argument. Send a city only in `city`.
3. Respect the shopper's requested count. Search supports 1–5 results, default 5; barcode lookup supports 1–10 offers, default 10. Return no more than the requested count or the tool's ceiling, including across multiple searches. If the shopper asks for more, explain the ceiling. Prefer fewer relevant matches over padding a list with duplicates or unrelated products. For food or drink requests, omit non-food items such as oat-milk shampoo; household-product searches remain supported when requested.
4. Report only identities, prices, retailer names, sizes, observation dates, and offers actually returned by the tool. A normalized requested barcode is not proof of a matched product. If the result has no offers, say no observed offers were returned. If a search has no matches, say no matching products were returned. An authentication failure, rate limit, timeout, or server error is an error; never describe it as an empty successful result.
   - If a package size is missing, write "size unavailable". Never reconstruct it from rounded unit prices, product familiarity, or another listing. Returned unit prices may still be quoted; calculate a new comparison unit price only from an explicitly returned package size.
   - Use each displayed result's observation timestamp. A combined date range must include every displayed observation across all tool responses. Do not substitute today's date or the request date for an observation date. If dates are incomplete, omit the aggregate range rather than guessing it.
   - Name a retailer only when its returned identity provenance is `observed` or `inferred`. Preserve `unknown` and `conflicting` identities. A nearby retailer location does not prove the observed price came from that exact branch.
5. In every price answer, include: "Prices are nightly observations, not real-time checkout quotes, and may differ at your exact store." Preserve any more restrictive freshness or scope qualification returned by the tool. Describe the 25 km location scope without claiming coverage of every store or retailer.
6. Refer to a postal-code location as "near your postal code". Keep complete postal codes out of the answer and continuation links, including when the shopper supplied one in the prompt. Do not echo account details, internal IDs, logs, or credentials.
7. Include the `open_in_vynn_url` returned by the tool when available. Explain that Vynn recalculates near the shopper's saved or entered postal code if that matters to the comparison. Use the returned link as-is; do not add a postal code.

For locations outside Canada, historical price charts, all-retailer catalogues, purchases, or deliveries, explain the unsupported request without calling a Vynn tool. Vynn cannot place orders or arrange delivery. Distinguish the lowest returned offer from a claim about the cheapest product everywhere; pack sizes can differ.
