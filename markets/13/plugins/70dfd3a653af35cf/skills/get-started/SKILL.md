---
name: rankbolt-get-started
description: How to work with a user's RankBolt blog through the RankBolt tools (sites, articles, SEO, publishing).
---

# Working with RankBolt

RankBolt manages SEO blog content for one or more websites. Every tool acts on
one site.

1. Start with `whoami` or `list_sites`. If the account has exactly one site the
   tools use it automatically; otherwise pass `site_id` on every call and ask
   the user which site they mean when it is unclear.
2. To answer questions about existing content use `search` (keywords) and
   `fetch` (full text) or `list_articles` + `get_article`.
3. To create content, `generate_articles` writes complete SEO-optimized drafts
   from a brief and saves them; `create_article` saves text you wrote yourself
   (Markdown). Both create drafts unless a status is given.
4. Scheduling: set `status: "scheduled"` and an ISO 8601 `scheduled_at`;
   RankBolt publishes to the connected CMS at that time. `status: "published"`
   publishes immediately.
5. `update_article`, `humanize_article` and `delete_article` change or remove
   content. Confirm with the user before deleting or overwriting a whole body.
6. Generation tools (`generate_articles`, `generate_featured_image`,
   `humanize_article`) take 30-90 seconds and use the account's credits; only
   call them when the user asked for that outcome.

If a tool answers "Subscription required", tell the user their RankBolt plan
does not cover that site and point them to https://rankbolt.ai/#pricing. Do
not offer to upgrade from inside the chat.
