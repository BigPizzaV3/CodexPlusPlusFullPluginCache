---
name: orpinn-media-workflows
description: Read exact Orpinn catalog or menu images, handle real uploaded or host-generated files, and prepare controlled product-image replacement with browser approval. Never substitute another image when source access fails.
---

# Orpinn media workflows

For an existing picture, resolve the exact authorized target. Call `get_catalog_product_image` for a POS catalog product or `get_menu_item_image` for an electronic-menu item. These sources can differ. Display only that tool's returned image bytes and explain which target/source they represent. The returned SHA-256 identifies actual source bytes; a bounded thumbnail is explicitly labelled as a display transformation.

If the result is missing, `image_unavailable`, access denied, a tool failure, or lacks image bytes, say the actual image could not be accessed. Do not fetch search results, use a stock image, show another product, generate an illustration or invent a URL to satisfy an existing-image request. Never claim to have seen an image based only on its filename, URL or catalog text.

If the user expressly requests a NEW image, use the host's native image-generation capability when actually available. Label it as newly generated, not as an existing Orpinn image. If generation is unavailable in this host, say so. Orpinn does not expose a server image-generation engine and cannot grant the host that capability.

After the user chooses an uploaded/generated image, pass only its actual host-provided file object to `import_product_image_file` through its advertised file parameter. Never fabricate a `file_id` or `download_url`, pass a local path, use a product-text URL or leak signed links. If native file handoff is unavailable, use `request_product_image_upload` and the authenticated upload page; explain the real limitation without claiming a transfer occurred.

Poll `get_product_image_upload_status` at most six times over two minutes, stopping on failed, expired, revoked or unchanged pending status after that bound. Ready means intake only. Call `prepare_product_image_change`, show the exact before/after card and wait for the user's browser click. The card performs the queued commit. Only `linked_action.status=committed` proves replacement; queued/processing remain pending.

Undo is separately prepared with `prepare_product_image_undo` using the original committed action ID and approved through a NEW browser card. Use its new undo action ID for any supported commit retry. Do not reuse forward approval, exceed the returned undo deadline or claim POS synchronization from server acceptance. Organization sharing may require additional explicitly advertised image capability; do not bypass a rejected shared-image action.
