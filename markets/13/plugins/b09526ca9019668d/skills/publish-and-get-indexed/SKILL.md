---
name: publish-and-get-indexed
description: Publish ready Sight AI articles to the connected CMS, schedule them, submit them to IndexNow and Google Search Console, and check index coverage. Use when the user asks to publish or schedule an article, why a page is not indexed, or to get content indexed faster.
---

Use this skill when the user wants an article live or wants Google and Bing to pick pages up. Reads need no confirmation; publishing, scheduling, submitting and inspecting (which spends a daily budget) do.

## Pick the site and the article

1. Call `list_sites` and settle on one site. Every other tool takes its `siteId`.
2. Call `list_articles` with a `status` filter to find the article, and `get_article` for its title, body and SEO fields when the user wants to check it before publishing.
3. Call `get_cms_status` for the active CMS integration, whether the article is eligible to sync, and whether sync is manual-only (Framer). Call `get_article_sync_status` for a per-platform view of an article already synced.

## Publish now or later

4. To publish now, confirm the article and the destination, then call `sync_article` with the `articleId` (and `integrationType` when the user names one). It goes to the live site.
5. To publish later, call `schedule_article` with the `articleIds`, a future `scheduledDate` and optional `scheduledTime`. Call `get_planner` with `view` "scheduled" to show the publish queue, or "settings" for the daily sync limit and default publish time. To move or remove a queued item, confirm and call `update_scheduled_article` or `remove_scheduled_article` with the `queueId`.

## Get it indexed

6. After publishing, call `submit_article_indexnow` with the `articleId` so Bing and Yandex pick it up; `get_indexnow_status` with the `url` shows the submission state.
7. Call `get_gsc_status` for the Search Console connection, and `submit_sitemap_gsc` to resubmit the sitemap when new URLs were added.
8. Call `get_seo_indexing` for coverage from Google URL Inspection: indexed, not indexed, excluded, never inspected and stale URLs with the verdict and advice, plus today's inspection budget. Filter with `state` "not_indexed", "never_inspected" and the others.
9. To check specific pages now, confirm (it spends the daily inspection budget) and call `inspect_urls` with up to 20 `urls`; after a not-indexed verdict, `resubmit_urls` with up to 50 `urls` re-sends them through IndexNow.
10. When something is set up wrong (no CMS, Search Console disconnected, IndexNow key missing), call `get_account_health` and pass on its blockers.

## Do not

- Do not call `sync_article` or `schedule_article` without the user naming the article and confirming.
- Do not promise Google will index a page; report the verdict and the advice the inspection returns.
- Do not resubmit URLs that are already indexed.
