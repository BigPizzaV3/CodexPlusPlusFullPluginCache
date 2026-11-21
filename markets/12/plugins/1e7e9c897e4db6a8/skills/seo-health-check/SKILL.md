---
name: seo-health-check
description: Find what to fix first on a site that SeoVision tracks. Use when the person asks why their site does not rank, what is wrong with their SEO, what to fix first, or for an SEO audit of their site.
---

# SEO health check

1. Pick the project: `seovision_list_projects`, then use the chosen project's `projectId` in every call.
2. Read the latest audit: `seovision_list_audits`, then `seovision_get_audit` for the newest one. Group the failed checks by area (technical, on-page, structured data, off-page, AI readiness, AI visibility) and order them by impact.
3. Add what search data shows:
   - `seovision_get_search_console_status`. When Search Console is connected, `seovision_list_search_console_quick_wins` gives pages close to the first page of Google.
   - `seovision_list_ai_search_gaps` gives questions where AI assistants answer without naming the brand.
   - If the `seovision_get_technical_seo` tool is available, it gives the technical fixes SeoVision can apply to the site.
4. Answer with a short list: the five most important problems, why each one matters, and who acts on it (SeoVision does it on its own, it waits for the person's approval, or it needs the site's developer).
5. If the newest audit is more than about a month old, offer a fresh one with `seovision_run_audit`. Say first that a run counts toward the account's daily audit limit, and start it only after the person agrees.

Use only what the tools return. If a source is not connected or has no data yet, say so in one line instead of guessing.
