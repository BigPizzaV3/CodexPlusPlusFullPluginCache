---
name: sprite-sheet-kit
description: "Pack 2\u201316 actual JPEG/PNG/WebP sprites into a transparent PNG atlas and named JSON frame map. Choose 1\u20138 columns and 0\u201316 pixels of transparent padding. Original dimensions are retained with centered grid placement after orientation and sRGB normalization. No resizing, trimming, rotation, edge extrusion or animation timing is added. Each source is bounded to 1024 pixels per side; combined source and atlas are limited to 16 megapixels, atlas sides to 4096 pixels, and combined download to 32 MB. Inspect named frames and download actual outputs. Requires a connected account; output links are public."
---

# Sprite Sheet Kit

Require 2–16 actual still images and one unique safe frame name per source. Use either attachments or HTTPS references, not both. Confirm column count and padding when unspecified or use defaults of four columns and two pixels. Each image is at most 1024 pixels per side, combined source pixels at most 16 MP, combined downloads at most 32 MB; output is at most 4096 pixels per side and 16 MP. Retain source dimensions and alpha after auto-orientation and sRGB conversion; do not claim identity of hidden RGB values or every color-profile conversion. Transparent grid padding is not extrusion. Show actual PNG and frame-map JSON, let the user inspect named frames, and disclose no animation timing/rigging or optimal-packing claim. Reopen saved exports rather than recomputing.

Use actual supplied files/text and the connected tools. Do not invent an output, successful recovery or findings. If tools are unavailable, report the missing connection. Original inputs are processed without rehosting by this workflow. Exports are stored publicly and anyone holding their links can view them. Preserve successful files and exact returned documents if storage partially fails.

For a new atlas, use sprite_sheet_kit_create to export ordinary model-visible file data first. Then call sprite_sheet_kit_preview with media_url set to the actual returned Atlas PNG URL and manifest_url set to the actual returned Frame JSON URL. This separate read-only preview shows the interactive atlas and named frames without creating another output. Preserve the exact returned file URLs in the answer.

Keep assistant text to an accurate brief summary and plain Markdown links to actual PNG/JSON exports. The interactive app provides the visual preview; do not add image-search groups, illustrative thumbnails or generated substitutes.
