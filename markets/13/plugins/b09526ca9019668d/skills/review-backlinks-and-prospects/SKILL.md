---
name: review-backlinks-and-prospects
description: Review a site's backlink profile in Sight AI, spot lost or toxic links, build the disavow file, and work the link prospects (competitor link intersect, unlinked brand mentions, broken links) toward outreach. Use when the user asks about backlinks, referring domains, toxic links, disavow, or where to get links.
---

Use this skill when the user asks about links pointing at the site or how to earn more. Reads need no confirmation; review decisions, refreshes and queuing outreach do.

## Pick the site

1. Call `list_sites` and settle on one site. Every other tool takes its `siteId`.

## The profile

2. Call `get_seo_backlinks` for the summary with deltas against the previous snapshot and the referring pages; `status` "live" (default) or "lost" for recently lost links.
3. Call `get_seo_backlink_profile` with `section` "profile" for the 24-month timeseries and the anchor and velocity health, "anchors" for the anchor text mix, "referring_domains" for every domain with spam score and review state, "toxic" for the candidates with reasons, "new" for links first seen in the last 30 days, or "broken" for links to pages that no longer resolve.
4. Call `get_seo_history` when the user wants the monthly trend of backlinks and referring domains next to organic keywords and traffic.

## Toxic links and the disavow file

5. Walk the toxic list with the user. For each domain they decide on, call `manage_seo_backlinks` with `action` "review", the `domain` and `status` "keep", "disavow", "reviewed" or "none". Confirm the decision first; disavowing is a signal to Google.
6. Call `get_seo_disavow_file` for the disavow text built from the domains marked "disavow", and tell the user it is uploaded in Google Search Console, not by Sight AI.

## Link prospects

7. Call `get_seo_link_prospects` for the prospects on file: `source` "intersect" (domains linking to competitors but not the site), "mention" (unlinked brand mentions) or "broken" (broken links to the site); `status` "open", "added", "dismissed" or "all". The rows include the proof-of-value attribution of links won through outreach.
8. To act, confirm and call `dismiss_link_prospects` or `reopen_link_prospects` with the `prospectIds`, or `refresh_link_prospects` to run the intersect, mention and broken-link scans again (queued). Handing prospects to the outreach agent is done in Sight AI (Backlinks, then Link prospects), not through the plugin.

## Refresh the data

9. Call `refresh_backlinks` to pull the profile again (`mode` "one_per_domain" or "as_is"). It is queued and spends the site's SEO budget, so ask first.

## Do not

- Do not mark a domain "disavow" without the user naming it.
- Do not say an email was sent or that outreach was started; the plugin only dismisses, reopens and refreshes prospects.
- Do not estimate domain authority yourself; use the domain rank and spam score the tools return.
