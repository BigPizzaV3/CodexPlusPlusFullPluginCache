---
name: sitecheck
description: Check one public web page for speed, accessibility, search and social previews and security settings, get a list of fixes in priority order, or preview a draft title, description and share image before a page is published. Use when a user gives a web address and asks to check, review or audit it, asks about its basic SEO, how it performs, what to fix first, or how it looks in Google or when shared.
---

# SiteCheck workflow

Use the connected SiteCheck tools when the user names a public web page and asks what to fix on it, or wants to see a draft share card.

## Tools
- `check_site`: scans one page and saves the result at a public report link. Use mobile unless the user asks for desktop. A result under 24 hours old is reused; set `rescan` only when the user changed the page or asks to check again.
- `get_report`: shows a report that already exists, by `job_id` or address. It never starts a scan. Use it for speed results that were still running and when the user asks for the saved or last report of a site.
- `preview_meta`: shows how a draft title, description and image will look in Google and on social media. It visits no page except the image.

## Behaviour
- Keep the reply to six lines at most: the scores, the top three fixes, anything still running and the report link. The card shows the details, so do not repeat the full fix list.
- If the result is reused, say how old it is and that asking for a rescan gets a new one.
- Say that automated checks find only some problems and that a result is not a legal compliance check when the user asks about legal accessibility or compliance.
- Tell the user the report is saved at a public link when they ask about privacy or sharing, or before scanning an address that looks private.
- Do not send addresses that contain passwords, tokens or other secrets, and do not use the tools for pages behind a login.
- Report the tool's refusal in plain words if a page cannot be scanned, for example when its owner has opted out.
