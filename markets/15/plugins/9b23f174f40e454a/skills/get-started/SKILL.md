---
name: get-started
description: Start with DrUrls in ChatGPT - see your sites' SEO health, read the issues with their fixes, and run a first audit when an account has none yet.
---

# Getting started with DrUrls

DrUrls audits websites for SEO. Use its tools to answer questions about the person's own sites.

1. Call `list_sites` to see which sites the account has and their latest score and grade.
2. If the account has no audited site yet, offer to audit one: `start_scan` takes the site's URL, and `get_scan_status` reports progress until it completes (a crawl takes a few minutes).
3. For a site that has an audit, `get_site_report` gives the overview, `find_issues` lists issues by severity with an example page, and `check_google_visibility` explains what blocks Google indexing.
4. For "what should I fix first?", `get_improvement_plan` ranks the fixes by how many pages each one touches.
5. To look at a single public page without an account, use `free_page_check`.

`start_scan`, `get_improvement_plan` and `generate_report` use credits from the person's DrUrls account; the other tools only read. Tell the person before calling one of those three, and let them decide. If a tool answers that the account does not have enough credits, say so plainly; credits are managed in the DrUrls account, not here.
