# Store check

Use this when the user has a store connected and has not said exactly what to do: when they start, ask what it can do, or ask for ideas. It turns "what can I do?" into one click.

## Let the screen read the store

If you know the store's web address (from the store tools' shop details, or ask the user for it once), call `show_store_check` with only `store`. It reads the store's public catalogue itself in one call and builds the findings itself: there is nothing else to pass, and nothing extra in the conversation. Say one sentence first ("I'll check your store, about 20 seconds.") and nothing after the screen.

If the result says the catalogue is not public (a store still being set up, or password-protected), say so in one sentence. Then offer the same actions by reading the user's products through their store tools and showing them with `show_products`, as in "After the user picks" below. Never build a findings screen yourself.

## After the user picks

The click comes back as "Let's do this: <action> (<title>)". Start that work straight away with the main skill, without asking again what they meant:

- **Make their photos**: list the products with colours that have no photo in `show_products` (one card per product, with the missing colours said in one short sentence before the screen), then recolour each product's photo of the garment being worn into each missing colour, and continue as for colour variants.
- **Put them on a model**: `show_products` with the garment-only products, then `references/on-model.md`.
- **Add photos on a model** (from the store's own check: products with fewer than 4 photos): `show_products` with those products, saying their photo counts in one short sentence before the screen; for those that only show the garment on its own, follow `references/on-model.md`.
- **Suggest colours**: `show_products` with those products, then `show_colours` for the first one picked. If the store lists each colour as its own product, say so and suggest colours that are not in the store yet.
