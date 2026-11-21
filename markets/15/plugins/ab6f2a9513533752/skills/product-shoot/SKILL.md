---
name: product-shoot
description: Run a Masonry Studio product shoot. One photo of the person's real product goes in, four looks come back to choose from, then a matching set of finished photos. Use when someone wants photos of their own product for a store, ads or social posts and has, or can share, a photo of it.
license: MIT
---

# Studio product shoot

Use this when the photos must show the person's real product, not an invented
look-alike. For a one-off image with no real product, use `generate_image`
instead. When the person gives explicit instructions that differ from these
steps, follow the person.

## Inputs

- A photo of the product: an attachment, a direct image link, or a product
  page link. Required. If there is none, ask for one and stop.
- Optional: where the photos will be used (store listing, ads, social), a
  mood, a background. Don't ask for these when the person didn't mention
  them; Studio plans without them.

## Steps

1. Call `add_reference_image` with the attachment or link, and keep the id it
   returns. If it fails (not an image, a private link), say so and ask for
   another photo.
2. Call `start_product_shoot` with that id, plus any use, mood or background
   the person gave. It plans four looks and shows them as previews.
3. Ask which look to use, naming the four looks exactly as the tool returned
   them. Don't choose for the person. If they already named a look (for
   example "clean daylight"), confirm it in one line before continuing,
   because the set uses credits.
4. Call `choose_look` with the chosen look. It makes the set and returns the
   photos with an "Open in Masonry" link.
5. Show the set, then offer next steps: change one photo (`remix_image`), turn
   the hero photo into a short video (`animate_image`), or try another look.

## Rules

- Keep the product as photographed. Don't describe it with a different
  color, size, label, or brand.
- Use only the product photos the person gave. Don't look for other images
  of it.
- One shoot per request. Don't start a second shoot or another set unless
  asked.
- When a tool refuses because the workspace is out of credits, show its
  message as written and stop. Don't suggest purchases.
- When the person asks for something this flow doesn't cover, such as
  deleting photos or using another workspace, say Masonry can't do that here.
