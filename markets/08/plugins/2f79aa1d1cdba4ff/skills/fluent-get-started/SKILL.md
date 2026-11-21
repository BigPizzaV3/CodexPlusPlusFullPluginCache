---
name: fluent-get-started
description: Use right after someone connects Fluent, or whenever their Fluent closet is empty or nearly empty, to get their first clothes saved quickly and show what Fluent can do with them.
---

# Get started with Fluent

Fluent keeps the user's closet: the clothes they own, with photos. With it you can answer "what should I wear?" and "should I buy this?" from what they actually have.

## First turn

1. Call `fluent_get_closet_context(domain="style", intent="closet")` to see how many items are saved.
2. If the closet is empty or has only a few items, say in one or two sentences what Fluent does. Then offer the quickest ways to add clothes and let the user pick one. Don't start with setup questions.
3. If they already have a closet, skip setup and help with what they asked.

## Quickest ways to add clothes

- **Photos.** They can upload several at once: camera-roll pictures, mirror selfies, product shots or screenshots. Inspect each photo yourself. Save one item per distinct garment they own with `fluent_add_closet_item`, passing the uploaded photo as `image_file` when that parameter is available (otherwise as `image_data_url`, or save the item and add the photo with `fluent_set_closet_item_photo`). Treat several views of the same garment as one item, and skip clothes worn by other people. Pass one image per call.
  - **The cover is the garment alone.** The cover (`image_type="primary"`) is a product-only image: a product shot, flat lay, hanger or mannequin photo, with no person wearing it. A photo of someone wearing it, the user or a store's model, is a fit photo (`image_type="fit"`), never the cover; a close-up of a detail is `"alternate"`. Save each photo itself with `image_origin="user_source"`. Set `catalog_ready=true` only for a reviewed clean product image, such as a retailer's product photo; otherwise leave it out.
  - **Clean cover.** Fluent cuts out a new product photo itself where it can; the save result then says so, and there is nothing more to do. If the result says Fluent found a person in the photo, follow its `productOnlyCoverStep`: keep that photo as a fit photo and use a product-only image as the cover. If the save result says the item has no clean cover yet and you can generate or edit images, make one right away from the photo the user just shared, exactly as the result's `cleanCoverStep` describes: a faithful cutout of just that garment on a transparent background, with nothing invented and logos and text unchanged. Check its edges on light and dark backgrounds before saving it with `fluent_set_closet_item_photo`. Tell the user the cover is a cleaned-up cutout and their original photo is kept with the item. If you can't generate images, skip this; the closet shows their photo.
- **Retailer images and links.** The most reliable way to get a product photo is for them to paste the product image itself, or a screenshot of it. Treat it like any uploaded photo, so Fluent keeps its own copy. They can also paste links to clothes they own: read each page yourself (Fluent does not browse), then save the item with its name, brand, category and colour.
  - **Cover:** pick the listing's product-only image (often a flat or packshot further along the gallery, not the first model photo) and pass its URL as `image_url` with `catalog_ready=true` and `image_type="primary"`. Fluent copies the linked image into its own storage.
  - **Reference photos:** add the listing images that will help later with `fluent_add_closet_item_photo`: detail close-ups as `"alternate"` and views of a model wearing it as `"fit"`. Skip images that add nothing new.
  - **Product details:** save the link, product code and the listing's material and construction notes with `fluent_save_closet_item_product_details`.
  - If the save result says the photo was not attached (some retailers block the copy), the item is saved without a photo; ask them to paste the image. If you can't open a link, ask for the image, a screenshot or a short description.
- **A quick list.** They can name items in words, for example "navy chinos, white leather sneakers". Save each one without a photo. A photo can come later: a product photo becomes the cover with `fluent_set_closet_item_photo` (`image_type="primary"`), and more photos are added with `fluent_add_closet_item_photo`.
- **Order confirmations.** They can paste the text or a screenshot of an order confirmation. List the clothing in it and save only the items they confirm. Fluent never reads email.

Every save needs a `category` (TOP, BOTTOM, OUTERWEAR, SHOE, ACCESSORY or ONE_PIECE for dresses and jumpsuits) and a `subcategory`, such as "Chinos" or "Sneakers".

When the user asks you to add clothes, that request is their approval: save what they asked for right away, one call at a time with `approval="explicit_user_approved"`, then report what was saved. Don't ask them to confirm again. Check first only for items they didn't name themselves, such as the clothing found in an order confirmation or a photo where it isn't clear which garments are theirs.

- Keep one stable `client_token` per intended item.
- A possible-duplicate warning saves nothing. Keep saving the unrelated items and collect the matches for one short question. After the user answers: for a different garment, resend that item with `on_duplicate="force"` and the exact `duplicate_candidate_id` Fluent returned. For the same garment, do not create it again; keep the new photo on the existing item with `fluent_add_closet_item_photo` (or `fluent_set_closet_item_photo` with `image_type="primary"` if it has no photo yet).
- If a save is rate-limited, wait as the result suggests and retry only the unsaved items with their original `client_token`. If it keeps happening, stop and explain.
- Report new, matched-existing and unresolved items separately. A saved item can still need a photo; check the save result.
- Save only approved garment details and the chosen garment photos. Never copy full emails, addresses, payment details or other personal data into Fluent.
- Never invent details you didn't see or read, and claim a save only when Fluent returned it.

## Show the payoff right away

Once a few items are saved, offer one of these:

- **See the closet:** where you can show Fluent's closet view, call `fluent_show_closet`; otherwise describe what was saved.
- **An outfit from what they own:** use only items Fluent returned, and name each one.
- **Should I buy this?** They share a link or screenshot, and you compare it with the clothes they already own. Don't make try-on or on-you preview images.

## Keep it light

- Offer setup once. If they decline, help with their actual request.
- If a closet read lists items without a clean cover (`cleanCovers`) and you can generate images, offer once to make them, and ask before making many.
- Fluent does not track budgets. If price matters, ask the user.
