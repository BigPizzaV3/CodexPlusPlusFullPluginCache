---
name: technical-site-audit
description: Crawl a brand's website and report technical SEO problems. Use for running a site audit, checking crawl issues, broken links, page level fixes, sitemap imports, or managing the media library and image alt text. Do not use for keyword research or for writing content.
---

# Technical site audit

Crawl the brand's site, find what is technically wrong, and turn it into a fix list.

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: resolve the brand

Call `list_brands`. If more than one, ask which. Keep `brand_id` for every later call.

## Step 2: know which pages exist

Call `list_pages`.

If empty, populate it before auditing:

- `import_sitemap_urls` pulls the site's own sitemap. Try this first.
- `scan_urls` takes an explicit list when there is no usable sitemap.

## Step 3: run the audit

1. `start_audit` with `brand_id`. `max_pages` caps the crawl. Set it for large sites and tell the user what the cap excludes, because a capped crawl is a sample and reporting it as complete is wrong.
2. Poll `get_audit`. Do not poll faster than every 30 seconds. Crawls take minutes.
3. `cancel_audit` stops one that is no longer wanted.

## Step 4: read the results

- `get_audit_issues` is the core output: what is broken and where.
- `get_audit_pages` for per page detail.
- `get_audit_links` for internal and external link problems, including broken links.
- `get_audit_assets` for images and files, including ones that are oversized or missing alt text.

## Step 5: turn issues into a fix list

Group by cause, not by URL. Two hundred pages missing a meta description is one template problem, not two hundred problems, and reporting it as two hundred buries the real work.

Order by impact:

1. Issues blocking indexing, for example pages that cannot be crawled or are excluded.
2. Issues that break the experience, for example broken links.
3. Issues that weaken a page, for example missing metadata or alt text.

`get_page_suggestions` gives page level recommendations, and `update_page_suggestion` records that one has been handled. `check_page_frameable` tests whether a page can be previewed in an embed. `page_refresh_jobs` shows content refresh work already queued.

## Step 6: media

The media library is part of the same surface:

- `list_media_assets` to see what exists, `update_media_asset` and `delete_media_asset` to change it.
- `generate_alt_text` to fix missing alt text found by the audit.
- `import_assets_from_audit` to pull crawled images into the library.
- `manage_media_folders` to organise them.

## Boundaries

- `delete_pages` removes up to 5000 URLs in one call and cannot be undone. Always list what will be deleted and get explicit confirmation. Never infer this from a vague instruction to clean up.
- `delete_media_asset` is destructive in the same way. Confirm first.
- Never present a capped or partial crawl as a full one. State the page count crawled and the cap applied.
- Do not report an issue count without saying how many pages were crawled. The number is meaningless without the denominator.
