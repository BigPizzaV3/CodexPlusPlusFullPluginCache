---
name: review-site
description: "Read every page of a Beste site and list what still reads like demo content, missing SEO, repeated sections and broken links, without changing anything. Use when the person asks what is wrong with their Beste site or wants it reviewed."
---

Review a Beste site and report, do not fix anything yet. Findings as a list, no
preamble around it.

1. list_websites, get_site, list_pages.
2. get_page_markdown for every page.
3. Report, grouped by page:
   - copy that is still demo text (placeholder names, lorem, "Build something")
   - claims that look invented rather than given by the user
   - pages with no SEO title or description
   - sections that are empty or hidden
   - the same block repeated on several pages as separate copies rather than one
     shared component (they will drift apart)
   - the same section type used again and again, or a piece still showing its
     demo values (get_section_defaults names the piece slots)
   - navigation links that point nowhere useful
   - articles built as ordinary pages instead of posts (list_posts against
     list_pages): no listing on the site can find them. The fix is to read the
     page, create_post with the same text as the body, then delete the page
4. End with a short list of the fixes you would make, in priority order, and ask
   which ones to apply.
