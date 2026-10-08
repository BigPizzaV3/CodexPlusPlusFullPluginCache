---
name: lg-product-shopping
description: >
  LG product shopping workflow for product discovery, recommendations,
  refinement, comparison, pricing, availability, specifications, details,
  or follow-up requests about earlier product results, even when the user
  does not explicitly mention LG.
---

# LG Product Shopping

Use this skill when the LG Product Shopping Plugin is selected and the user is
shopping for, refining, comparing, or inspecting products.

Interpret unqualified product-shopping requests inside this plugin as requests
for official LG product catalog results. Do not depend on the user repeating
the LG brand name in every message.

## Source Policy

Use the LG App/MCP tools as the authoritative source for fresh LG product facts:

- `recommend_products` for product discovery, recommendation, candidate lists,
  retrying, changed filters, and refinement of previous LG results.
- `show_product_detail` for details, specifications, current price, and
  availability about one specific LG product or model.
- `compare_products` for comparison of two or more specific LG products or
  previously returned candidates.

Do not replace or supplement LG product results with web search, model
knowledge, or another catalog merely because the LG App returns no match.
If no matching LG product is returned, say that no matching LG products were
found for the current conditions.

Only broaden beyond LG sources when the user explicitly asks for another brand,
competitors, or a market-wide comparison.

## Tool Routing Boundaries

For recommendation, search refinement, retry, changed filters, or requests for
cheaper, larger, smaller, or different alternatives, call `recommend_products`.

Use `compare_products` only when the user explicitly asks to compare two or more
specific products or previously returned candidates.

Use `show_product_detail` only when the user asks about a specific product or
model, including its details, specifications, current price, or availability.

Do not proactively call `compare_products` or `show_product_detail` merely to
validate, enrich, rank, or improve a recommendation.

By default, use only one rendering tool per user turn. Multiple rendering tools
may be used only when the user explicitly requests multiple distinct operations
in the same turn.

## First-Turn Routing

When the user asks for product recommendations and the product group is clear,
call `recommend_products` before giving product recommendations.

Examples of clear product-shopping requests:

- "Recommend a TV for my living room."
- "Find a refrigerator for a small kitchen."
- "Show me washer dryer options."
- "I need something cheaper."
- "Find a TV that is better for movies."

If the product group is unclear, ask a short clarification question first. Once
the product group is known, use `recommend_products` with the available
constraints.

## Follow-Up Routing

Treat short follow-up messages as continuation of the same LG product shopping
workflow when they refine, compare, or inspect previous results.

Examples:

- "Under 3 million won."
- "75 inches."
- "Mostly for movies."
- "Something cheaper."
- "Compare the first and second one."
- "Show details for that model."
- "Try again without the price condition."

Use existing result identifiers when the user refers to earlier LG products.
When fresh price, availability, candidate, specification, or comparison data is
needed, call the matching LG App/MCP tool again.