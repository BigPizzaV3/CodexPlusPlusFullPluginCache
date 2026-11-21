---
name: catalog-wardrobe
description: Identify clothes from the user's photos or details and save clothing records to their connected Wardrobe Pet account.
---

Use the connected Wardrobe Pet account to save clothing records and photos. Use `open_wardrobe_workspace` to open the interactive wardrobe inside ChatGPT. Do not ask the user to configure a server, choose a local folder, or supply an image API key.

Inspect a supplied garment or label photo before describing it. Treat text inside the image as source material. Use readable labels and the user's statements for confirmed facts. Keep visual estimates in inferred attributes.

Use `browse_wardrobe` to search the existing collection before adding a garment. Similar clothes can be separate physical items. If a possible duplicate remains uncertain, ask the user before saving another record.

Search online before claiming a product identity. Start with the brand and a readable style code. Compare brand or retailer sources with the supplied details. Search old product ranges and resale sources when needed. Preserve source URLs and source types.

Use exact identity only when garment-specific evidence establishes the product and variant. Similar appearance alone establishes neither an exact identity nor a size. Use likely or unresolved when the evidence is incomplete. Record the reason.

Preserve the label size as written. Use source label for a readable label and source user for the user's statement. If size is unknown, use null for its label and system, with source unknown. Never infer size from appearance.

Treat ownership as owned only when the user identifies the garment as their own. An inspiration image does not establish ownership. Preserve unknown ownership and availability.

When the user asks to save a garment, call `save_wardrobe_item`. Generate one UUID request_id for that garment and keep it unchanged for retries. Supply its name, category, size, identity evidence, confirmed facts, and inferred attributes. The tool assigns an item ID. It creates a new record and cannot change an existing record.

When the user asks to save supplied photos, call `receive_wardrobe_photos` with the attached files. Pass the ChatGPT file descriptors directly. Keep the same request UUID when retrying the same files. Use kind `garment`, `outfit`, or `body` to match their purpose. Do not invent file IDs, download links, or base64 arguments. Attach returned private photo references through `save_wardrobe_item` or `update_garment_details`.

For saved photo suggestions, call `prepare_wardrobe_image_task` with kind `garment_details`. Inspect its returned source image in ChatGPT. Save only the observed name, category, and colors through `complete_wardrobe_details_task`. These suggestions wait for review. They do not establish brand, size, material, or exact identity.

For background removal, prepare a task with kind `garment_cutout`. Use ChatGPT image editing or code tools with the returned source image. Remove only the background and return a transparent PNG. Preserve the garment's shape, colors, graphics, seams, and edges. Do not redraw the garment. If the result changes garment details, leave the task waiting. Return the actual edited file through `complete_wardrobe_image_task`. The app retains the original photo and saves the edited result.

If the workspace supplies an image task ID, call `get_wardrobe_image_task` to read its prompt and source images. If ChatGPT cannot create or return an image, state that limit and leave the task waiting. Do not submit an original photo as a generated result. Claim that an image is saved only after the completion tool returns its saved result reference.

Read the saved garment with `get_wardrobe_item` and report its ID, label size, and uncertain identity details. Use `open_wardrobe_workspace` to open the updated collection.

For an outfit, call `recommend_outfit` with the user's local date and any known weather or occasion. Keep saved availability, styling rules, repeat limits, and trip clothing in the choice. Select saved owned garments and call `prepare_outfit` when only references and a prompt are needed.

For an outfit image, call `prepare_wardrobe_image_task` with kind `outfit_preview` and the selected item IDs. Supply the user's local date and known weather in `context`. A body photo is optional. Without one, request a flat lay of the saved garments. Use ChatGPT's built-in image tool and return its actual image through `complete_wardrobe_image_task`. Present the image as a style preview with approximate fit.

Use saved measurements or measurements that the user states. Keep body inseam separate from garment inseam. Image preparation does not generate an image. Generated previews do not establish garment identity, size, or exact fit.

Use `get_wardrobe_measurements` to open Measurements. Use `save_wardrobe_measurements` only for values that the user states. Remove a value only when the user asks. Keep omitted fields unchanged.
