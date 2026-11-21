---
name: search-inventory
description: Search new BMW vehicle inventory by location, model, price, color, and features
---

# Search BMW Inventory

Help users find new BMW vehicles available at dealerships near them.

## How It Works

Use the `find-new-inventory` tool to search real-time dealer inventory. The search supports natural language queries.

## Gathering Information

Ask users for:
- **Location** (required): Zip code or city/state
- **Preferences** (optional): Model (e.g., X5, 3 Series, M4), color, price range, features, body style

## Tips

- Users can describe what they want naturally: "blue X5 under $70k with M Sport package"
- Results include pricing, mileage, exterior/interior colors, key features, and dealer info
- Suggest saving favorites when users find vehicles they like using `save-inventory-favorite`
- Use `get-inventory-favorites` to show saved vehicles and `remove-inventory-favorite` to remove them
- If no results match, suggest broadening the search criteria (wider radius, more models, higher budget)
