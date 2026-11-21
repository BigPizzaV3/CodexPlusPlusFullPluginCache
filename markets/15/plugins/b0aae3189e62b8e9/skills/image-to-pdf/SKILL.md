---
name: image-to-pdf
description: Put JPG and PNG photos, phone scans and screenshots into one PDF, one image per page, turned upright from EXIF orientation, with the images_to_pdf and inspect_images tools.
---

# Zovo Photo to PDF

Use `images_to_pdf` when the user attaches JPG or PNG images and wants one PDF. Pass the images in the order the user gave. Use `inspect_images` when the user wants to check the images or the page plan first.

1. Pass all attached images in `images`, in the user's order. Up to 60 images and 20 MB in total.
2. `page_size`: `fit` (default, each page matches its image) or `letter`, `a4`, `legal` when the user wants paper pages or will print. Use `a4` or `letter` as the user says; ask only if printing matters and the size is unclear.
3. `orientation` (`auto`, `portrait`, `landscape`), `margin_mm` (0 to 25) and `fit` (`contain` shows the whole image, `cover` fills the page and crops) apply to paper sizes.
4. After the result, give the page count, any image that was turned upright, the warnings, and the download link. Say the link expires in about 1 hour.
5. If an image is HEIC, WebP, GIF or TIFF, the tool says so. Tell the user to export it as JPG or PNG and attach it again.

Do not use this skill for merging existing PDFs, converting a PDF into images, reading text from a photo (no OCR) or editing photos.
