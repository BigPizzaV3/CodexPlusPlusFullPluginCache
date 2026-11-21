---
name: save-to-folio
description: Save a link, article, or written text to the user's Folio inbox so they can read it later on their e-ink device.
---

When the user shares a URL and wants to read it later, call the Folio `add_article` tool with that URL. Do not scrape or summarize the page first; Folio fetches and cleans the article itself.

When the user wants to save text that has no URL (your own answer, their notes, a draft), call `add_markdown` with a short human title and the text as GitHub-flavored Markdown.

If the user names a category, pass it through. Otherwise omit it.

After saving, confirm in one plain sentence using the article title, and mention it is now in their Folio inbox. Do not show ids, JSON, or raw URLs unless asked.
