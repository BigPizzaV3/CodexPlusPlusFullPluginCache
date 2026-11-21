---
name: wordpress-content
description: Use when the user wants to write, review or improve content or on-page SEO on one of their brands' WordPress sites (posts, pages or custom post types), including the SEO title and meta description.
---

Work on a brand's WordPress content without ever changing published content directly. Reply in the user's language.

1. Call `list_brands` and confirm the brand. Call `get_brand` for its tone.
2. To find content:
   - `wp_list_post_types` for the available types (posts, pages and custom types).
   - `wp_list_posts` (with `type`, `status` and `search`) or `wp_list_pages`.
   - `wp_get_post` for the full content and `wp_get_seo_meta` for the SEO title, meta description and focus keyword.
3. **New content:** write it, show it to the user and call `wp_create_draft` with `title`, `content` (HTML) and, where relevant, `categories`/`tags` (from `wp_list_terms`) and the SEO meta. It is always saved as a draft.
4. **Improving existing content:** propose the changes, confirm them and use `wp_update_post` (content and SEO) or `wp_update_seo_meta` (SEO only). Send only the fields that change.
   - On a draft, the change is applied directly.
   - On published content, the live site is not touched: a proposal is created (`action = proposal_created`) that a person approves inside WordPress. Explain this to the user.
5. Summarize what was created or proposed and where to review it.

Rules:
- The connector never publishes: publishing is done by a person in WordPress or Abency.
- Each `wp_update_post` call on published content creates a new proposal; do not repeat it once it has been created.
- For keyword ideas, combine it with the `keyword-research` skill.
