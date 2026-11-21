---
name: find-keywords-and-draft
description: Research high volume, low competition keywords for a site in Sight AI, save the best ones to a keyword list, and draft or generate an article for one of them. Use when the user asks for keyword ideas, content to write, or a new blog post.
---

Use this skill when the user wants keyword ideas or a new article. Keyword research spends the site's daily lookup budget and article generation spends the team's AI credits, so confirm before either.

## Pick the site and the seed

1. Call `list_sites` and settle on one site. Every other tool takes its `siteId`.
2. Turn the request into a seed of 2 to 80 characters. If the user says "my business" or "my niche", take the seed from the site itself: call `get_seo_organic_keywords` (what the site already ranks for) or `get_seo_overview`, and name the seed you chose.

## Research

3. Tell the user that research spends one of the site's daily lookups, then call `research_keywords` with the `seed`. For "high volume, low competition" use `sort` set to `opportunity`, a `minVolume` the user is comfortable with, `maxDifficulty` of 49 or lower (0 to 29 is easy, 30 to 49 medium), and `newOnly` set to true so keywords already in the list are left out. Add `notTop10` when the user wants gaps rather than keywords they already win. Every row carries the site's own position for that keyword.
4. Present the rows as a short table: keyword, monthly volume, difficulty, intent, opportunity score, the site's current position. Keep the tool's order.

## Save the keepers

5. Before saving, call `check_keywords` with the chosen keywords; it says which already exist in the site's keyword list or already have an article.
6. Call `add_keywords` with the new ones (comma or newline separated, up to 100 at once). To put them in a keyword list, pass `groupName` (a list is created if needed) or a `groupId` from `list_keyword_groups`. This changes the account, so confirm the keywords and the list name first.

## Write the article

7. To write the article yourself in the conversation, call `create_draft_article` with the `title` and `articleType`, then fill it with `update_article`, `append_article_section` or `replace_article_section`. Nothing is published.
8. To have Sight AI write it, confirm that generation spends AI credits, then call `generate_article` with the `targetKeyword` (and `articleType`). It runs in the background: poll `get_article` until the status is ready. Articles generated through the plugin get no AI cover image; tell the user to add one in Sight AI (Content, then Articles, then Generate image) or give an image URL to `set_article_main_image`.
9. Tighten the metadata with `refresh_seo_title` and `refresh_seo_meta` when asked.

## Publish, only when asked

10. Check `get_cms_status` first. If a CMS is connected and the user asks to publish, call `sync_article`, then `submit_article_indexnow` so the new URL is picked up quickly. Both change the live site, so confirm before each.

## Do not

- Do not call `research_keywords` with `refresh` set to true unless the user asks for fresh data; it pays for a new search instead of using the cache.
- Do not save keywords, generate, sync or submit without confirmation.
- Do not promise rankings or traffic for a keyword; report its volume, difficulty and opportunity score as returned.
