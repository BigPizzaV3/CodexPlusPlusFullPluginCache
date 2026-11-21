---
name: abconvert-experiments
description: Inspect, create, and analyze Shopify A/B experiments using the connected ABConvert tools when a merchant asks about their experiments or wants to prepare a test.
---

# ABConvert experiments

Use the ABConvert tools available in the current connection. If the connection is missing or unauthorized, explain how to connect ABConvert before attempting store operations. Do not request Shopify administrator credentials in chat.

Resolve experiment names using `list_experiments` and product choices using `list_shop_products`. Follow pagination when the user requests a complete list. Use returned identifiers rather than constructing them or assuming names are unique. Resolve ambiguity before changing the wrong experiment.

For headline experiment results, use `get_experiment_results`. For device/country comparisons use `get_experiment_breakdown` with the supported dimensions. A pending snapshot is not a result: follow the tool's retry instructions and report pending work if it does not complete. Preserve missing metrics, date ranges, sample-size warnings, and uncertainty. Do not invent conversions, uplift, statistical confidence, or winners.

New price tests use `create_price_experiment_v2` with `saveAsDraft=true` unless the merchant explicitly requests immediate launch. Resolve the product, prices, control and variant, and traffic split from the request and tool schema. Creating a draft does not authorize a later launch. If a write times out or its outcome is ambiguous, look up the experiment before retrying to avoid duplicates.

Only use the tools and permissions available for the connected store. Do not attempt cross-store access or invent a permanent-delete capability. Do not replace an unsupported destructive request with a different store-changing action without user direction.

Use `ping` only when the user asks to check the connection or when diagnosing a failed operation. Do not invoke tools solely because this skill loaded.
