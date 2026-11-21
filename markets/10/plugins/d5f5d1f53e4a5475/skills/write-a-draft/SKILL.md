---
name: write-a-draft
description: Write a new WordPress post or page as a draft with real editor blocks (headings, paragraphs, lists, images, buttons). Use when the user asks to write, draft or prepare an article, page or announcement for their site.
---

# Writing a draft

1. Ask only what is missing: topic, audience, rough length, post or page. Use `wp_get_posts` on a few recent posts to match the site's tone and length when the user has no preference.
2. Create the item with `wp_create_post`: a clear `post_title`, `post_status` left as draft, `post_type` "page" only for pages.
3. Lay out the content with `wp_write_blocks` on the new ID: one heading block per section, paragraphs, lists where they help, an image block only with a real image URL from the Media Library (`wp_get_media`).
4. Optionally set categories and tags with `wp_get_terms` and `wp_add_post_terms`, and a featured image with `wp_set_featured_image`.
5. Reply with the title, the sections you wrote and the post link, and say it is a draft. Publish only when the user explicitly asks, with `wp_update_post` setting `post_status` to publish.

Never invent facts about the user's business (prices, opening hours, names). Ask, or leave a clear placeholder in the text.
