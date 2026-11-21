---
name: vectorize
description: Use when the user wants to turn an existing raster image (PNG, JPG, WebP, BMP, GIF, TIFF) such as a logo, icon, sticker, illustration or scan into a vector file (SVG, PDF, EPS, DXF), for example for a website, print shop, cutting machine or laser.
---

# Vectorize an image with Shapesoda

1. Make sure the user has attached the image to the message. If they only gave a link or a description, ask them to attach the file.
2. Call `vectorize` with the attached image. Pass `colors` only when the user asked for a specific number of colors (for example 2 for a vinyl cutter), and `transparency` only when they asked for a white or transparent background.
3. The Shapesoda window shows the result. Tell the user they can change colors, background and smoothness in the window for free, and download SVG, PDF, EPS, DXF or PNG there.
4. If the user asks how many free images are left, call `get_usage`.

Do not use Shapesoda to draw a new image from a text description, to retouch or upscale photos, or to write SVG code by hand.
