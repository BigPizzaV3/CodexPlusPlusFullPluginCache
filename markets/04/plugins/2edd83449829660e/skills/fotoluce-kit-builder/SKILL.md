---
name: fotoluce-kit-builder
description: Build a Fotoluce camera, lens, and accessories kit when a shopper wants compatible components, a complete setup, or additions for a specific camera or model.
---

# Fotoluce Kit Builder

Build an evidence-based kit from current Fotoluce products. Keep compatibility evidence distinct from merchandising recommendations.

## Establish the base

1. Identify the camera or other base item, intended use, total budget, and required components. If the base item is unclear, use `search_products` and let the shopper disambiguate materially different models.
2. Call `get_product` for the selected base and inspect its attributes and relationships.
3. Treat `included_in_box` relationships as already included, not as extra purchases.

## Select components

Use the following evidence order:

1. An explicit model compatibility attribute on the candidate is strong evidence for that exact model.
2. An exact shared lens-mount attribute, such as the same `attacco-mirrorless` or `attacco-reflex` value, supports a mount match. Also check sensor-format attributes when present and disclose missing coverage information.
3. An `often_bought_together` relationship is a curated Fotoluce recommendation, not proof of technical compatibility. Call `get_product` on the candidate and look for stronger attribute evidence before calling it compatible.
4. Brand-level compatibility alone is insufficient for model-level compatibility. Present it only as requiring confirmation.

Search for lenses using the exact returned mount value plus the shopper's use case, then inspect each candidate with `get_product`. Prefer in-stock options unless the shopper accepts unavailable items. Never infer compatibility from similar names, descriptions, brand, price, or category alone.

## Present the kit

Separate the result into:

- base item;
- included-in-box items;
- compatibility-confirmed components and the evidence for each;
- curated or generic recommendations that still need confirmation;
- current total for items that must be purchased, excluding included items;
- availability, promotion, and compatibility caveats.

If reliable evidence is missing, say that compatibility cannot be confirmed and link the candidate for human verification. Do not add items to the cart unless the shopper explicitly asks; hand off cart actions to the purchase workflow.
