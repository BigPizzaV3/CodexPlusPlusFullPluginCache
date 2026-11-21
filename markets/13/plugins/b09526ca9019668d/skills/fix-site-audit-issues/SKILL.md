---
name: fix-site-audit-issues
description: Read a site's technical SEO audit in Sight AI, show what is broken or got worse, find decaying and cannibalized content, and fix title, description, H1, canonical and schema issues on Sight-managed articles with a reviewed before/after. Use when the user asks about site health, audit errors, broken pages, or what to fix on the site.
---

Use this skill when the user wants to know what is technically wrong with the site and fix it. Reads need no confirmation; applying a fix changes a live article and does.

## Pick the site

1. Call `list_sites` and settle on one site. Every other tool takes its `siteId`.

## Read the audit

2. Call `get_seo_audit` for the latest crawl: status, on-page score, error, warning and notice counts, the previous audit for comparison, and the page issues. Use `severity` ("error", "warning", "notice" or "all") and `page` / `limit` to work through the list. Lead with errors.
3. Call `get_seo_audit_comparison` with `status` "new" to show what appeared since the previous crawl, "fixed" to confirm what was resolved, or "persisting" for what keeps coming back.
4. For one URL, call `get_seo_page_detail`: its keywords, rankings, Search Console queries, audit issues, backlinks and AI citations in one place. For the whole site by section, call `get_seo_pages`.
5. Call `get_seo_internal_links` for orphan and weakly linked pages and the suggested links with anchors.
6. Call `get_seo_content_health` with `kind` "decay" for pages losing clicks over the last 28 days with the reasons, or "cannibalization" for queries where several pages compete and the page to consolidate on.

## Fix what Sight manages

7. For a missing or long title or description, a missing H1, a canonical or a JSON-LD problem on an article Sight manages, call `propose_audit_fix` for that issue. It returns a before/after proposal and writes nothing.
8. Show the proposal and wait for the user to approve it. Then call `apply_audit_fix` with the proposal unchanged; the article is updated and re-synced to its CMS. Never apply a proposal the user did not see.
9. Issues on pages Sight does not manage cannot be fixed from here; say what to change and where.

## Re-check

10. To crawl again, call `run_site_audit` (optionally `maxPages`, `enableJavascript`, `lighthousePages`). It is queued and only one audit runs at a time, so tell the user results land in a few minutes and read them with `get_seo_audit` afterwards. Audits spend the site's SEO budget, so ask before starting one.

## Do not

- Do not call `apply_audit_fix` without an approved proposal from `propose_audit_fix`.
- Do not describe an issue as fixed until `get_seo_audit_comparison` or a fresh `get_seo_audit` shows it gone.
- Do not invent page speed or crawl numbers; report only what the tools return.
