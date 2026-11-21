# Media, alt text and digital contents

Plan media around buyer understanding, not arbitrary image count. Use only seller-owned/authorized assets. The MCP connector manages existing media; it does not generate photos/video itself. If the host has separate generation tools, use only available authorized capabilities, disclose relevant cost, and keep them distinct from MakeBox transport.

## Physical gallery plan

1. Hero: accurate product and offer, readable at thumbnail size, no misleading accessories/quantity.
2. Detail: material/finish/technique close-up that matches verified facts.
3. Scale: real dimensions or credible context with clearly stated measurements; a mockup is not measurement evidence.
4. Options/customization: actual colors/fonts/sizes, matching inventory labels.
5. Use/ordering: appropriate context, included contents and essential customization instructions.

Add care, packaging or other views only when they answer real questions. Preserve the exact product geometry, engraving, text and features in edited/generated scenes. Do not replace the seller's product with a prettier different item. Label digital mockups clearly where needed; do not present props as included.

Alt text describes the visible image in useful natural language: product, visible design, view and relevant detail. No keyword pile, sales pitch or claims invisible in the photo. Different views need different alt text. Validate the live field length and retain intended rank/hero order.

## Upload and verify

Obtain `get_upload_link` or an Asset Library upload for an authorized file; use its tenant-owned `asset_id`. Direct multipart examples are in [operation recipes](etsy-operation-recipes.md). Local paths and base64 text are not valid direct file arguments.

Use `etsy_upload_listing_image` → `etsy_get_listing_images`, `etsy_upload_listing_video` → `etsy_get_listing_videos`, `etsy_upload_listing_file` → `etsy_get_all_listing_files`. Check final IDs, order, alt text and partial failures. An accepted listing does not prove its media completed. Do not automatically replay uncertain uploads or remove current assets before replacements are confirmed.

Current Etsy form allows up to 20 photos and two 5–15 second videos. MakeBox upload transport currently limits images/files to 20 MB and videos to 100 MB; these are transport limits, not a guarantee Etsy accepts every format/codec. Inspect current Etsy requirements and existing count. The single-video read endpoint may return empty; use the list endpoint.

## Digital release checklist

Record file count, exact filenames/formats, actual contents, page count/design sizes, resolution where relevant, editable parts, required software/account, fonts/license, delivery method and usage rights. “Editable” does not imply every element is editable. Do not promise a Canva link, vector source, commercial license or software compatibility absent from the actual product.

Check that files open, contain the intended item, match the description and contain no customer-specific or unauthorized assets. Downloadable listings support up to five files; current MakeBox transport uses a 20 MB limit per file. If a legitimate product uses an instruction PDF with an external editing link, make access and permissions clear and test the supplied link; do not invent it. Do not buy or generate missing content as an undisclosed fulfillment step.

Offline: supply a media shot list, alt-text table and file/compatibility worksheet. Copy-ready listing text must accurately describe the files actually supplied. Save a draft until release blockers are resolved. Never say files were uploaded when only a worksheet exists.

Reference checked 2026-10-04: [Etsy listing form](https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing?segment=selling). Live tools and official requirements decide accepted formats/counts at execution time.
