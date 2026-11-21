---
name: tapnow-product-shots
description: Turn one product photo into a complete set of e-commerce listing images with TapNow (clean white background, lifestyle scene, alternate angle, detail close-up), framed for the target marketplace. Use when the user wants product shots, listing or marketplace images, a product photo set, or new images of a product they already have.
---

# Product shots

One real product photo in, a listing-ready set out. The product is the one thing that must not change: shape, color, material, logo and proportions stay true to the photo. Only the background, angle and light change.

## Ground rules

- `create_product_shots` makes the whole set in one call. Its description and parameters list the shot types, the marketplaces it frames for, and any other choices it offers. Read them from the tool each time instead of assuming them; they change more often than this guide.
- Ask once, in one short message, about anything the user has not said that the tool marks as worth asking (for example which shots or which marketplace). If they leave it to you, omit those options so the defaults apply.
- Each shot is a separate generation on the user's TapNow account, so make only the shots the user needs.

## 1. Get the product photo

The tool takes the photo by ID, not by URL, and the `product_image_id` description lists which IDs it accepts:

- At a public link, or attached to the conversation: bring it in with `upload_image`, then pass the returned image ID and project ID. If the photo was attached but `upload_image` only takes a link, ask the user to add the photo to their TapNow library instead.
- Already in the user's TapNow library: find it with `find_library_assets`. Pass its `file/<file_id>` if `product_image_id` accepts library files; otherwise bring it in with `upload_image` first.
- Made earlier in TapNow: pass its node ID and project ID.

No photo? Ask for one. Never invent a product from a text description and present it as a product shot: it will not match the real thing. If the photo is blurry, very small or the product is cut off, say the whole set will suffer and ask for a better one.

## 2. Describe the product

Always add a short product description, for example "matte black insulated bottle with a bamboo lid". It noticeably improves how faithfully the product is reproduced.

## 3. Run and deliver

1. Call `create_product_shots`. The ticket maps each shot type to a node ID.
2. Share the project link if there is one, then poll `get_production_result` with the node IDs and the same project ID until every shot is done or failed.
3. Deliver shot by shot with the label and format from the ticket. A failed shot will not recover: say which one, and offer to redo just that one.
4. Results stay in the TapNow project. Offer `save_to_library` into a folder named after the product.

## Beyond the standard set

- **A scene the standard shots do not cover** ("on a marble bathroom shelf"): `create_image` with the product photo as a reference image and a prompt that says to keep the product exactly as it is.
- **A format the marketplace list does not include**: crop a finished shot with `resize_for_platform`, or recompose it with `create_image` (finished shot as the reference) when the new shape needs more room around the product.
- **A new color or design of the product**: that is product design, not a product shot. Use `create_image` and say the result will not match the real product.
