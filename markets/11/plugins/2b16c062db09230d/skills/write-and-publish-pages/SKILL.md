---
name: write-and-publish-pages
description: Write, edit and publish pages on an Aveiro website, such as blog posts, docs pages and landing pages. Use when the user asks to draft a page, change an existing page, add images to a page, or publish site changes.
---

# Write and publish pages

Pages are drafts until they are published. Explicit instructions from the user take priority over these steps.

## Before writing

1. Find the site with `aveiro_list_sites`, unless its ID is already known in this conversation.
2. Call `aveiro_authoring_guide` once per conversation, before the first `aveiro_create_page` or `aveiro_update_page`, and follow it. Pages use Aveiro's MDX dialect: content pages are headings and prose with registered components only where they help; landing pages are built from page sections. Never write raw HTML layout.
3. Ask for what you can't know: the topic, the audience, key facts, links. Don't invent product details, numbers, quotes or dates.

## Change an existing page

1. Find it with `aveiro_list_pages`, then read it with `aveiro_get_page`.
2. Call `aveiro_update_page` with the complete new body in `content`; it replaces the whole body, so keep every part the user didn't ask to change. Pass the revision from `aveiro_get_page` as `if_match`, so an edit made in the meantime isn't overwritten.
3. To change only the title, summary, tag, image or display date, send `metadata` and leave `content` out. `publishedAt` must be a real date (YYYY-MM-DD).

## Add a page

1. Pick a path inside the right folder, for example `/blog/spring-update.mdx`. If the folder doesn't exist, create it with `aveiro_create_collection` first.
2. Call `aveiro_create_page` with the path, the MDX body and metadata (at least a title and a summary).

## Images

- Check `aveiro_list_media` first and reuse an existing image's URL.
- For a new image from a public HTTPS URL, call `aveiro_import_media_from_url` and embed the `mdx` it returns.
- For a screenshot of a real web page, call `aveiro_media_create_screenshot` with `estimate_only` true first, tell the user the credit cost, and render only after they agree. Then poll `aveiro_media_get_screenshot` until it is done.
- Never invent an image URL.

## Publish

1. Show what is waiting with `aveiro_list_changes` and summarize the changes.
2. Call `aveiro_publish_site` only when the user has asked to publish in this conversation. Name the pages that will go live, and pass their `content_ids` so nothing else is published by accident.
3. If the site has translations, ask whether to publish them too and set `locale_scope` to match.

Delete a page (`aveiro_delete_page`) only when the user asks for it and confirms which page.
