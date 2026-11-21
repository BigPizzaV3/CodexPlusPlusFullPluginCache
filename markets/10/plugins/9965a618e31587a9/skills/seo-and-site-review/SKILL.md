---
name: seo-and-site-review
description: Check a UiChemy website before launch, for SEO (meta titles and descriptions, headings, indexing, social preview images, broken buttons, thin pages) and for design quality (empty or overlong copy, repeated layouts, inconsistent navigation, stock photos), then fix what the user approves, including each page's SEO settings. Use when the user asks for an SEO check, a site audit, a review before launch, or to set a page's title, description, slug, social image or indexing.
---

Use this skill when the user wants a project checked or wants to change a page's SEO settings.

Steps:
1. Identify the project with `uichemy_list_projects` if the user did not name it.
2. Run the checks the user asked for, or all of them for a general "check my site":
   - SEO: `uichemy_seo_audit`.
   - Design and content: `uichemy_review_site`.
   - Hidden faults and phones: `uichemy_validate` and `uichemy_check_responsive`.
3. Report the findings most important first, in plain words, and offer to fix them. Each finding names the tool that fixes it.
4. For page SEO settings, read them with `uichemy_get_page_settings`, then change only the fields the user wants with `uichemy_set_page_settings`: slug, meta title, meta description, social image, canonical URL, language, whether the page shows in Google, and whether AI crawlers may use it. The WordPress and Astro exports carry these settings.
5. After fixing, run the same check again and report what is left.

Rules:
- Hiding a page from Google (no-index) or changing a slug can hurt a live site. Name the page and wait for a clear yes first.
- Write titles and descriptions from the brief and the page's real copy. Do not invent claims, ratings or prices.
- These checks change nothing. Only the fix tools change the project.
