---
name: search-parts
description: Search the DriveStock B2B catalog for industrial drive and automation parts, read net EUR prices or on-request, and create quote inquiries. Do not invent prices or place paid orders.
---

# DriveStock catalog

Use the DriveStock MCP server at https://drivestock.eu/api/mcp.

- Search parts with `search_parts` (needs a query or brand).
- Read one SKU with `get_part`.
- List brands with `list_brands` and stats with `get_brand_stats`.
- Suggest alternatives with `suggest_alternatives`.
- Create a quote inquiry with `create_inquiry` and `source=chatgpt`.

Do not invent prices. Do not place paid orders or transfer money in chat. Checkout stays on https://drivestock.eu.
