---
name: ecommerce-store-builder
description: Build ecommerce storefront websites using the connected ecommerce.new MCP server.
---
<!--
Version: v1.0.1
Request: Prepare ecommerce.new for OpenAI Plugin Directory submission.
Changes: Added a minimal store-building skill referring to the existing ecommerce.new MCP connection.
Date: 2026-11-06
-->

Use the `ecommerce_new` MCP server to create an ecommerce website when the user explicitly asks for a store or storefront.

Ask for missing details only when needed to complete the request. Describe the outcome based on the actual MCP tool response, never claim a site was deployed if deployment was not confirmed.

Do not invent checkout readiness, payment-provider connection, inventory, products, or URLs. Do not collect card details or payment credentials in chat. If the user requests checkout setup, use only supported tools and explain any unavailable functionality.
