---
name: svg-new
description: Use when the user asks to convert a supplied raster image into editable SVG, recolor or simplify an SVG, remove an SVG background using its original image, or vectorize a batch. Activate for vector or SVG output requests even when SVG.new is not named.
---

# SVG.new

Use the SVG.new MCP tools connected to the user's SVG.new account. Start from an image or SVG the user actually supplied or authorized. Do not invent source pixels, SVG paths, conversion results, or private history.

For an image attached in ChatGPT, use `vectorize_file` with the host-provided file object. For other MCP clients, `vectorize` accepts a real PNG, JPEG, WebP, or AVIF image as a base64 data URL. Ask the user for an image when no source is available. SVG.new does not create images from text.

Use `recolor_svg` for explicit color replacements and `simplify_svg` for a requested palette limit from 1 to 256 colors. Use `remove_background_file` with an attached original image or `remove_background` with its data URL. Use `batch_vectorize_files` for attached images or `batch_vectorize` for data URLs, with 1 to 10 images. Report the returned batch ID and call `get_batch_status` to check its observed result. Use `list_vectorizations` only for the connected user's history when relevant.

Vectorization, background removal, and batches can consume SVG.new credits. Report credit and API errors faithfully. Return actual SVG content or a real saved SVG file when the host supports files, and state when a result is only a batch ID.
