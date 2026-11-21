---
name: draft-fixes
description: Turn the recommendations in a Glippy GEO report into ready-to-paste fixes, such as JSON-LD structured data, meta tags, heading outlines and robots.txt rules, for the user to apply to their own site.
---

# Drafting fixes from a Glippy report

Use this when the user asks for help fixing what a Glippy report found, for example "draft the fixes", "write the schema for me" or "how do I fix the top issues".

## Start from a real report

- Work from a report in this conversation. If there is none, ask which domain to check and run `analyze_domain` first. Do not draft fixes for a site you have not analysed.
- Each recommendation has a `priority` (high, medium, low), a `category`, a `label` and a `detail`. Fix high-priority items first, then medium. Low-priority items (Performance & Crawlability, Agent Interactivity) are optional.
- Draft three to five fixes per reply unless the user asks for more. Say which recommendation each fix addresses, using its label.

## How to write each fix

- Give the code or text the user can paste, then one or two lines saying where it goes (for example "inside `<head>` on the homepage" or "at the top of robots.txt").
- Use only facts you know about the site: from the report, from what the user told you, or from well-known public facts. For anything you do not know, such as a phone number, street address, founding date or social profile URL, use a clear placeholder like `"REPLACE: phone number"` and list the placeholders after the code. Never invent business details.
- JSON-LD: one `<script type="application/ld+json">` block, valid JSON, schema.org types that fit the page (Organization or LocalBusiness and WebSite on a homepage; Product, Article or FAQPage only when the page really is one). Do not add FAQPage markup for questions that are not visible on the page.
- Meta tags: a title under about 60 characters and a meta description under about 160, written from what the page actually offers.
- Headings and semantic HTML: show the outline (one `<h1>`, then `<h2>` sections) or the landmark wrapper (`<main>`, `<nav>`, `<footer>`), not a rewrite of the whole page.
- robots.txt: see the ai-crawler-policy skill. Keep existing rules the user did not ask to change.

## Limits to state

- Glippy is read-only. The user applies the changes; Glippy cannot sign in to or edit the site.
- The report covers the homepage only. Fixes for other pages are suggestions by analogy, so say so.
- After the user ships the changes, they can ask for the analysis again. Results are cached for about ten minutes, so a re-run straight away shows the old result.
- Do not suggest renaming or 301-redirecting existing URLs to make slugs more descriptive. Only redirect URLs that are actually broken.
