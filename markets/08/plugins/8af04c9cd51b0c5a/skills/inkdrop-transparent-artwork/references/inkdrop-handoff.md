# Inkdrop artwork handoff

Use this reference only when taking prepared artwork into an Inkdrop product workflow. The current MCP tool descriptions and schemas govern supported inputs; the tool names below were checked against the production server on 2026-09-29.

## A new product

If artwork must first be created or edited, explain before the image step that the user should reply “Choose my Inkdrop product” when the finished artwork is ready. Wait for that product-selection follow-up. If the request already includes ready artwork and asks to choose a product, selection can begin directly.

Call `list_products` once with relevant filters and the normal limit of 12, then wait for the user's exact product, color, size, print side, and scale. Do not open duplicate pickers. Preserve reviewed choices. An explicit catalog-only request may browse without artwork.

Before importing, obtain the image-link sharing agreement required by Inkdrop: previews are unlisted, but anyone with an image URL can view the media. Reuse agreement already given for the same ongoing workflow unless revoked. Selecting a product alone is not that agreement or a request to make a mockup.

After the disclosed “Apply my artwork” action or an equivalent explicit agreed request, call `import_artwork` with the actual finished image. Use a real host-provided file reference or a user-authorized image URL; a local sandbox path is not a downloadable URL. Never invent a file ID, image URL, or image bytes. Pass the returned new `artworkId` into `apply_design` with the exact reviewed product options.

## Editing an existing preview

Preserve the selected product and options while changing the artwork. For an explicit edit requested directly in chat, call `prepare_artwork_edit` if no fresh card reservation exists. If the card already supplied a reserved `workflowId` and `workflowRevision`, reuse that pair. Keep the returned pair unchanged through import, apply, and retries; do not invent or increment it.

Use the standalone source identified by `get_artwork_for_edit`. Follow Inkdrop's supported assisted-edit flow by default. A direct native edit requires the user's explicit request and a host that can edit the actual source; if necessary, ask for that exact source as an attachment.

Wait for the user to explicitly continue with the finished edited image. Import that new image and apply its new `artworkId`. The old `artworkId` or `sourcePreviewId` still refers to the original artwork and must not stand in for the transparent edit.

## Finish the preview

Start one apply operation for the user's action. Preserve its idempotency key and creation inputs on a genuine retry. When pending, follow the existing operation using the current status tools and suggested timing instead of starting another render. On failure or canceled intent, preserve the existing preview and follow the returned recovery action.

Display only a real completed mockup or returned preview. For a completed direct-chat edit without a waiting card, follow the tool guidance to show the new preview once. Product or artwork changes do not authorize checkout or an order.
