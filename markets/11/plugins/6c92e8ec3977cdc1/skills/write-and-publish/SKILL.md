---
name: write-and-publish
description: Draft a Leafpad post, check its on-page SEO, and publish only after the user agrees.
---

Write with the user's own site, then stop before publishing.

1. Call `leafpad_list_organizations` and use the site the user names. If they have one site, use it.
2. Call `leafpad_get_company_data` with a question about the topic so the draft uses the site's own facts. If that returns nothing, say the knowledge base had no match and draft from what the user provided. Do not invent product facts, prices, or statistics.
3. Call `leafpad_list_tags` and reuse tags that fit. Then call `leafpad_create_post` with `published` left false.
4. Call `check_draft_seo` on the new post id. Tell the user the score and the checks that are not passing.
5. Ask whether to revise the draft or publish it. Call `publish_post` only after the user agrees to publish. Calling `leafpad_update_post` is for edits, not for going live.

Do not publish, schedule, or approve a refresh as part of saving a draft.
