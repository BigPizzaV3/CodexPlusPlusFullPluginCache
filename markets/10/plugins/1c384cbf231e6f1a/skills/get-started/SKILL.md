---
name: get-started
description: Use when the user wants a technical SEO audit, site audit, SEO health check or website crawl of a public website, or asks what is wrong with a site: broken links, redirect chains, pages not indexed, duplicate titles, missing meta descriptions, sitemap or canonical problems, or a site health score. Do not use for backlinks, keyword rankings or Search Console data.
---

Sitewalk crawls a website and ranks the technical SEO problems it finds, each with a plain fix.

1. Ask for the site address if the user has not given one.
2. Call `start_site_audit` with the address. Keep the returned `audit_id`.
3. Call `get_audit_status` every 20 to 30 seconds until the status is completed. A larger audit takes several minutes. Tell the user it is running and how many pages are done.
4. Call `get_audit_report` and present the ranked issues, highest impact first, with pages affected, an example URL and the suggested fix for each.
5. If the report says the page limit was reached, say so. If the user asks what was covered, use the report's `what_was_checked` and `not_checked` lists.

The first audit asks the user to connect, which confirms their email with a 6-digit code. Without a confirmed email an audit
covers up to 50 pages; with a confirmed email it covers up to 500. No domain verification is needed.
Report only what the tools return. Do not guess at issues the report does not list.
