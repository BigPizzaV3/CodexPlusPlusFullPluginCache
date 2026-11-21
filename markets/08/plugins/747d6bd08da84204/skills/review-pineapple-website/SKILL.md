---
name: review-pineapple-website
description: Review a connected Pineapple website's available analytics, page content, SEO or launch readiness and recommend improvements. This workflow is read-only; it does not apply changes or publish.
---

Give a short, evidence-based review matched to the user's question. Follow their requested scope rather than running an all-purpose audit for every request.

Identify the exact website or page using supplied context, `pineapple_list_workspaces`, or `search` as needed. Ask the user to choose when the target is ambiguous. Use `fetch` only with a Pineapple URI returned by `search`. Use actual returned document IDs for other structured tools, never guesses.

Read only the evidence needed:
- For SEO, use `pineapple_get_page_seo`; use `pineapple_list_page_blocks` if content is relevant.
- For traffic, use `pineapple_get_website_analytics` and a supported date range matching the user's request. If none is specified, state the range used.
- For readiness, use `pineapple_get_website_checklist` and, when requested, `pineapple_get_publication_review`.
- Read business profile, theme or listings only when relevant to the requested review and permitted by the connection.

Respect per-category Read permissions. Basic `mcp:read` only permits minimal discovery; it does not grant all private reads. If a needed category is denied, explain the missing access and offer the normal reconnect flow for that category. Never request Write to perform a review or use mutations as a read fallback. Continue with available evidence when a useful partial answer is possible, clearly stating the gap.

Separate observed facts from recommendations. Disabled, missing or unavailable analytics does not mean zero visits. Visits and pageviews do not prove conversions, revenue or causation. SEO fields do not prove search indexing or rankings. A draft, an authenticated preview, publication state and a working public domain are different facts. Mark stale translation evidence rather than silently regenerating it.

Return a one-sentence assessment, the few supporting facts with their date range or freshness, and the smallest useful next improvement. Ground suggested copy in supplied business facts; do not invent services, testimonials, prices, contact details or guarantees. Say when something was not inspected. Do not apply recommendations automatically. An explicit later request to edit belongs to the reviewed-change workflow and its existing permissions and approvals.
