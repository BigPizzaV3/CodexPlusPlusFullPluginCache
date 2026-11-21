---
name: get-started
description: How to use Hangeul Fonts to pick a free Korean font that is allowed for the user's purpose and set it up in a design tool or local file.
---

When a user needs a Korean (Hangeul) font:

1. Ask what the design is for and where it will be used (web, print, video, logo, packaging, app embedding, PDF embedding) if they did not say.
2. Call search_fonts with their description and use case. Present the license verdict and condition for each font, and link the official license.
3. For a specific font and use, call check_license. Treat "unknown" as not verified and tell the user to check the official source.
4. For a design tool, call get_font_setup. If the font must be uploaded to the Figma account, say so before loading it.
5. For local files (PDF, slides, images, HTML), call get_font_files and get_local_usage, and keep the license file next to the font when redistributing.

Never state license terms that the tools did not return.
