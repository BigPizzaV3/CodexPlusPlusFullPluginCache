---
name: content-gap-to-article
description: Find content gaps hurting a brand's AI search visibility, then create, generate, and publish SEO/AEO-optimized articles to fill them — end to end, from gap analysis through CMS publishing. Use when the user wants to improve AI visibility with content, write articles, fill citation gaps, or publish to WordPress, Ghost, Webflow, Framer, or the ChatFeatured CMS. Not for analytics-only questions (use the visibility report).
---

# Content Gap → Published Article

Run ChatFeatured's content pipeline: identify what content is missing, create targeted article ideas, generate them, and publish.

## Steps

1. **Resolve the brand** via `list_organizations` → `list_brands`; confirm with the user if they have several brands.
2. **Find the gaps.** Use `query_analytics` (`source_mentions`, `cited_urls`) to see which topics and sources AI answers cite where the brand is absent, and `get_existing_opportunities` for gaps ChatFeatured has already identified. `list_articles` with `status: "published"` shows what the brand has already covered — don't propose duplicates.
3. **Create ideas** with `create_article_ideas`, targeting the specific gaps found. Show the user the ideas before going further.
4. **Approve with consent.** `approve_articles` consumes the plan's monthly article quota — tell the user how many articles this will use, and check the `articleLimits` (used/limit/remaining) in the response. If the quota is exhausted, stop and say so.
5. **Generate** with `generate_articles`. Generation is asynchronous: poll `list_articles` with `status: "review"` to see when drafts are ready (typically minutes). Tell the user they can come back later rather than blocking on it.
6. **Review pass.** When a draft is ready, fetch it with `get_article` and summarize it for the user. Apply requested edits with `update_article_content`.
7. **Optional featured image.** `search_pexels_images` for a relevant photo, then `set_article_featured_image` with the photo's attribution fields.
8. **Publish — only with explicit user confirmation.** `list_integrations` shows connected CMS platforms; if there are several, ask which one and pass its `integrationId`. Use `publish_article` for immediate publishing or `schedule_article` for a future date, then confirm success with `get_publish_status`.

## Boundaries

- Never call `approve_articles`, `publish_article`, or `schedule_article` without the user explicitly agreeing in this conversation — approval spends quota and publishing writes to their public website.
- If no CMS integration is connected, complete the draft and tell the user how to connect one instead of failing.
- One pipeline run per request; don't loop generating more articles than the user asked for.
