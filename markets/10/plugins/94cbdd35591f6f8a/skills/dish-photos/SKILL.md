---
name: dish-photos
description: Adds, replaces or removes photos on CrumbPass menu dishes with set_menu_item_photo and remove_menu_item_photo, including photos the owner attaches, images you generate for a dish, and public https image links. Use when the owner wants dish photos, asks you to create or generate an image for a dish, wants to make the menu more visual, or wants to change or remove a dish's picture.
license: Proprietary
metadata:
  author: crumbpass
  version: "1.0"
---

# Dish photos

Photos show guests what will arrive at their table. A photo should never promise more than the kitchen serves.

## Steps

1. **Find the dish.** Use the exact dish name from `get_menu` (it also shows `hasPhoto`). If two dishes share a name, pass `categoryName`.
2. **Get the image.**
   - **The owner attached a photo:** use it.
   - **The owner asked you to create one:** generate a realistic, appetising photo of the dish as described, with its real ingredients, garnish and serving style. Use natural light, a plate or bowl that suits the restaurant, and no text, logos, hands or people. A square or 4:3 framing works best.
   - **The owner shared a link:** it must be a public `https://` image link.
3. **Show it and ask.** Show the owner the image and ask whether to use it for that dish. Only continue after they say yes.
4. **Set it.** Call `set_menu_item_photo` with:
   - `itemName` (and `categoryName` if needed)
   - `image` for an image in this conversation, or `imageUrl` for an https link
   - `aiGenerated: true` for any image you generated; `false` only for real photographs. Guests see an "AI image" label on generated photos. Never mark a generated image as a real photo.
   - `confirm: true` only after the owner approved that exact image for that dish.
5. **Confirm** what changed. To take a photo off a dish, show the exact dish to the owner, get approval, then call `remove_menu_item_photo` with `confirm: true` (the dish stays on the menu).

## Limits and failures

- PNG, JPEG or WebP, up to 5 MB. Larger or other formats are rejected.
- **"I didn't receive the image file":** the image did not reach the tool. This happens most on the ChatGPT mobile app. Ask the owner to attach the image again, ideally from ChatGPT on the web, or to share a public https link.
- **Download errors:** links can expire. Ask for the image again rather than retrying the same link repeatedly.
- **Several photos:** do them one dish at a time, confirming each image with the owner.
