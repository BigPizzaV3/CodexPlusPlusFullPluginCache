---
name: get-started
description: How to use The Super Prime to search prime and super-prime homes for sale and read The Super Prime's property market research.
---

# Using The Super Prime

The Super Prime (thesuperprime.com) is a London-based publication on prime and super-prime real estate. It lists homes for sale from leading agencies and publishes market news and research.

## Tools
- `list_areas`: which areas have listings, and how many.
- `search_properties`: find homes by area, price, bedrooms, type and features (for example a pool or a garden).
- `get_property`: full details of one home: price, size, tenure, highlight, amenities, nearby stations and schools, photos, floorplan, brochure and the marketing agency.
- `search_articles` and `get_article`: The Super Prime's market news and research.

## Good practice
- Use only the facts the tools return. Do not guess prices, sizes or features.
- Always give the property or article URL, so the user can see the photos and contact the agent on The Super Prime.
- For an exact bedroom count, set `min_bedrooms` and `max_bedrooms` to the same number.
- When filtering by `features`, read `matching_amenities` to tell a private pool from a shared residents' pool.
- Prices are asking prices in the listing currency (usually GBP). `usd_approx` is a guide only.
- This plugin is read-only. It cannot book viewings, send enquiries or make offers.
