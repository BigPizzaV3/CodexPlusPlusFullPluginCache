---
name: get-started
description: Introduce SERPHub to a new user and run their first request. Use when the user asks what SERPHub can do, how to start, or has just connected SERPHub and has not yet named a site.
---

Use this skill when someone is new to SERPHub in this conversation: they ask what it does, how to use it, or they have just connected it and have not asked for anything specific.

1. Call `list_sites` to see which websites the signed-in account has.
2. If it returns no sites, say that the SERPHub account has no websites yet. Offer to add one with `create_site` if the user gives a public URL, and ask before calling it. Explain that Google Search Console, Google Analytics and Google Business Profile are connected in the SERPHub web app, not from here.
3. If it returns sites, name them, with each site's SEO health score and whether Search Console is connected.
4. Offer three concrete next steps that fit what `list_sites` returned. For example: the site's top SEO issues, its top Search Console keywords, or whether it is up. Only offer search-data questions for sites where Search Console is connected.

Keep the introduction short: two or three sentences about what SERPHub covers (SEO audits and issues, search performance from Google, Bing and Yandex, uptime, backlinks and local SEO for the user's own sites), then the site list.

Do not invent sites, scores or connection status: report only what `list_sites` returned. SERPHub only covers websites in the user's own account; if the user asks about a website that is not listed, say so rather than guessing a `site_id`.

If the user's own instructions conflict with this skill, follow the user.
