---
name: google-images-research
description: Find Google Images results and their source pages, image URLs or returned dimensions with HasData. Use for image discovery, not generating images, taking screenshots or establishing reuse rights.
---

# Find image sources

Read `../hasdata-research/SKILL.md` and the Search sources section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_google_images_images_getImageSearchResults` with q and relevant supplied localization. Apply only actual supported filters; do not invent tbs strings or dimensions. Start with one result page.

Return a bounded set of actual image-result records, keeping image URL distinct from thumbnail and source-page URL. Include titles and dimensions only when present. Do not claim visual inspection unless the host actually displayed the image.

Image search metadata does not grant a license or prove ownership. Say when rights need checking at the original source; do not treat a search filter as a complete permissions assessment. Additional pages require the user's bounded scope.
