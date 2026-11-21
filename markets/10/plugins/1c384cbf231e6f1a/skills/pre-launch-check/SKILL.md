---
name: pre-launch-check
description: Use when the user is about to launch, redesign or migrate a website, change domain or move to HTTPS, and asks whether it is safe to go live, wants a pre-launch SEO checklist run on the real site, or wants a technical SEO check right after launch.
---

Run a Sitewalk audit of the site and report the launch blockers first.

1. Ask for the site address if the user has not given one. A staging site works only if it is public and robots.txt allows SitewalkBot.
2. Call `start_site_audit` with the address and keep the `audit_id`. Show the user the message it returns.
3. Call `get_audit_status` until the status is completed, showing the progress message each time.
4. Call `get_audit_report`. Report blockers first, in this order, only if the report lists them: pages set to noindex, robots.txt blocking search engines, broken pages and broken links, redirect chains, canonical tags that point at redirects or broken pages, missing sitemap or sitemap errors.
5. Then list the remaining issues by impact, as the report ranks them.
6. End with one next step: fix the blockers, then ask for another audit to confirm they are gone.

Report only what the tools return. If the report says the page limit was reached, say so.
