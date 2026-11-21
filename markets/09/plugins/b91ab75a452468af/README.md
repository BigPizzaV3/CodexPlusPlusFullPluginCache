# JAWD Agent Plugin

Live JAWD product search, conservative product guidance, and external Shopify checkout.

## Safety

The plugin calls only the public Jawd catalog and checkout endpoints. It never accepts payment details, creates an order, or stores customer data. Payment and shipping review happen on the Shopify checkout at jawd.in.

Every product and checkout link carries:

- `utm_source=chatgpt`
- `utm_medium=plugin`
- `utm_campaign=jawd_plugin`
- `utm_content=<tool_name>`

Checkout permalinks also carry matching `attributes[utm_*]` values so Shopify order attribution survives after checkout. The bare `?checkout` query flag is preserved exactly.

## Tools

- `search_products`
- `get_product`
- `recommend_routine`
- `build_cart`

## Local check

```sh
npm install
npm run check
```

The deployed endpoint is declared in `plugin.json` and `.app.json`.
