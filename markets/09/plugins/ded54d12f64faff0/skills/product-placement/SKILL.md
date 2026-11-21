---
name: product-placement
description: Place an exact real product (sofa, bed, rug, lamp, tile, wallpaper) into a room photo with MeltFlex. Use when the user shares a product photo or link and wants to see that specific item in their space.
---

# Exact product placement

## Steps

1. Get the room photo and a clear photo of the product, ideally on a plain background.
2. Call `generate_interior` with the room as `image` and the product photo(s) in `reference_images` (up to 10).
3. Write the prompt as one sentence naming where it goes: "Place this exact sofa against the left wall facing the window."

## Tips

- One product per call gives the most faithful result; for a full set, place the largest piece first and build on that render.
- For flooring, tiles or wallpaper, say which surface: "Use this exact tile on the bathroom floor only."
- If the result changes the product, retry with a tighter crop of the product photo.
