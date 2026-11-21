---
name: gyft-commerce
description: Use the connected Gyft MCP server exclusively for gift-card discovery, filtering, selection, and supported checkout workflows. All Gyft product data must originate from Gyft MCP tools. Prefer the Gyft-provided interactive UI over ChatGPT-generated shopping interfaces.
---

# Gyft Commerce

## 1. Mandatory Gyft MCP Usage

When a user invokes, mentions, or interacts with the Gyft application for gift-card discovery or commerce, the connected Gyft MCP server MUST be the exclusive source of gift-card product and commerce data.

### Strict Tool Selection Rules

- MUST use Gyft MCP product-search or catalog tools for all gift-card discovery requests.
- MUST NOT invoke ChatGPT's native product search or shopping search for Gyft gift-card requests.
- MUST NOT use external web searches, third-party shopping APIs, or marketplace searches to supplement Gyft results.
- MUST NOT combine Gyft results with products from other providers.
- MUST NOT substitute another provider when Gyft returns empty results or errors.
- MUST use only the tools actually advertised by the connected Gyft MCP server.

These restrictions apply to Gyft commerce workflows, not to unrelated requests or explicit requests to compare Gyft with external providers.

## 2. Product Discovery

When the user asks to find, browse, search, or filter gift cards:

1. Invoke the appropriate Gyft MCP product-search or catalog tool.
2. Preserve user-provided constraints, including:
    - Merchant or brand
    - Physical or digital delivery
    - Denomination or price range
    - Category
    - Recipient preferences
3. Treat Gyft MCP responses as the authoritative source of available Gyft products.
4. Preserve product IDs, variant identifiers, prices, denominations, currency, availability, and delivery types exactly as returned.
5. Do not fabricate, modify, or infer missing product information.
6. If Gyft returns no results, display the empty state through the Gyft UI when available.
7. Do not perform external searches to fill missing product information.

## 3. Gyft UI Rendering — Highest Priority

The Gyft-provided interactive UI is the preferred interface for gift-card discovery, product selection, and supported commerce operations.

### Mandatory UI Behavior

- MUST prioritize the UI resource associated with the Gyft MCP tool when available.
- MUST NOT independently generate alternative product galleries, product grids, shopping cards, or product comparison widgets when the Gyft UI is available.
- MUST NOT retrieve replacement product images from external image search providers.
- MUST use Gyft-provided product images within the Gyft shopping experience.
- MUST NOT duplicate the product catalog in the conversational response when the Gyft UI already displays it.
- MUST keep product filtering, denomination selection, quantity selection, and other supported interactions inside the Gyft UI whenever possible.
- MUST NOT generate a separate ChatGPT shopping experience as a replacement for an available Gyft UI.

### Conversational Output

When the Gyft UI successfully renders, avoid repeating its product data in conversational text.

Use only minimal supporting conversational text when necessary.

If the Gyft UI cannot render, provide a concise text-based fallback using only the Gyft MCP response. Never perform external product or image searches to build that fallback.

## 4. UI and MCP Tool Integration

Use the UI metadata advertised by the Gyft MCP server to identify the associated interactive application.

When a Gyft MCP tool provides an associated UI resource, prefer rendering that resource with the tool's returned data.

Do not create a substitute interface when the server-provided UI is available.

Respect the MCP server's advertised tool schemas, UI resources, and capabilities.

Do not assume that a tool supports interactive UI unless the relevant UI integration is actually advertised.

## 5. Checkout Workflows

When the user wants to configure, add, update, review, complete, or cancel a gift-card purchase:

- Use only the checkout, cart, or session tools advertised by the Gyft MCP server.
- Preserve product IDs, quantities, denominations, and other selected values.
- Prefer Gyft UI interactions for supported shopping steps.
- Do not substitute third-party checkout providers.
- Do not invent checkout sessions, totals, taxes, shipping costs, fulfillment options, or payment status.
- Follow the MCP tool schemas for required inputs and supported operations.

Before committing a purchase or performing another consequential external action, ensure that the user has provided or confirmed the required details.

Do not store OAuth credentials, payment secrets, or other sensitive credentials in plugin files.

## 6. Tool Availability and Failure Handling

MCP tool discovery is authoritative.

If a required Gyft tool is unavailable:

- Do not fabricate the missing tool.
- Do not silently substitute an external provider.
- Explain the unavailable capability briefly.

If Gyft product search fails:

- Do not retry using ChatGPT native shopping search.
- Do not retry using external web search.
- Do not fabricate fallback product results.
- Surface the error or empty state through the Gyft UI when supported.

## 7. Product Data Integrity

All Gyft product information must originate from Gyft MCP responses.

This includes:

- Product names and descriptions
- Product identifiers and variants
- Denominations and prices
- Availability and inventory
- Product image URLs
- Digital or physical delivery information
- Cart totals and checkout details

Do not enrich Gyft product results using external providers unless the user explicitly requests external comparison.

## 8. Interaction Boundaries

The Gyft UI should own supported in-app interactions.

When a user can select a product, denomination, quantity, or fulfillment option within the Gyft UI, prefer that interaction over generating an equivalent ChatGPT control.

Do not initiate a purchase without the required user authorization.

Keep the shopping workflow within Gyft MCP and its associated UI to the extent supported by the host application and advertised capabilities.

## 9. Priority Summary

For Gyft commerce requests:

1. Gyft MCP tools are the exclusive product and commerce data source.
2. Gyft-provided interactive UI is the preferred presentation surface.
3. Do not invoke external product, shopping, web, or image search tools.
4. Do not generate duplicate ChatGPT shopping interfaces when Gyft UI is available.
5. Do not fabricate missing product or checkout information.
6. Use only capabilities advertised by Gyft MCP.
7. Keep supported shopping interactions inside the Gyft UI.
