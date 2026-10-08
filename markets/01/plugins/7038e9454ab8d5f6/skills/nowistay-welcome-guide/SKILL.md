---
name: nowistay-welcome-guide
description: Create and edit structured Nowistay welcome guides while preserving headings, lists, images, videos, tables, separators, translations, and EditorJS formatting. Use for page creation, page updates, translations, reordering, image uploads, and guide-wide locale or intro changes.
---

# Nowistay Welcome Guide

Treat every page as structured content unless the full page proves it is paragraph-only.

Welcome guides contain reusable property information. Do not add guest-specific personal data, booking references, private messages, payment data, government identifiers, medical or biometric data, or account credentials.

## Find the page

1. Resolve the property once with `list_properties`.
2. Call `list_welcome_book_pages` once to get the page index, IDs, order, icons, and short previews.
3. Never edit from the list result. Its text is intentionally shortened and is not editable source.
4. Before every page update, call `get_welcome_book_page` for the target page and use its full `contents` and `editingGuidance`.

## Update a page safely

1. Copy the complete existing EditorJS document for every affected locale.
2. Change only the requested visible text or explicitly requested blocks.
3. Preserve block order, types, IDs, `data`, `tunes`, nested list item objects, inline HTML, media, tables, embeds, separators, and unknown fields.
4. Never flatten a structured page into plain text. Never stringify list item objects. Never paste escaped object representations into visible text.
5. Stage the full preserved structure with `update_welcome_book_page_preview`.

## Create a page

1. Use the `pageCreationGuidance.contentStructure.blockConstructionTemplates` returned by `list_welcome_book_pages`.
2. Build exact EditorJS content with `time`, `version`, and ordered `blocks` for each locale.
3. Choose `position=start`, `position=end`, or `position=after_page` with the correct reference page from the index.
4. Stage with `create_welcome_book_page_preview`.

## Add images

1. Call `upload_welcome_book_image` with the required property ID and either a direct public HTTPS `image_url` or exact-file `image_base64`.
2. Prefer the URL when both are available. Never invent, shorten, or repair base64.
3. Insert the returned `editorJsImageBlock` exactly into `content.blocks`. Never insert the URL or base64 directly as page text.

## Apply changes

Summarize the exact page, locales, placement, and changed blocks. If the user asked only for a preview, stop. If the user explicitly requested the change, continue through platform confirmation with the matching confirm tool and only the approval token. Do not reconstruct page content during confirmation.
