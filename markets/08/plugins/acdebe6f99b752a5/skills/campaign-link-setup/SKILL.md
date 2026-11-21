---
name: campaign-link-setup
description: Build correctly tagged UTM links and optional short links in LeadJourney for a new campaign, so every click is attributed to the right channel and campaign.
---

Use this skill when the user wants a tracking link for a campaign, asks to "create a UTM", "make a short link", or is about to launch an ad, email, or social post and wants it tracked.

## Inputs to establish

Ask for anything missing before building. Required:

- **Destination URL** — the page the click should land on.
- **Channel / source** — where the link will be posted (LinkedIn, Google Ads, newsletter, etc.).
- **Campaign name** — a short slug the user will recognize in reports.

Optional: medium (cpc, email, social, organic), content (creative variant), term (keyword).

## Steps

1. Call `get_current_workspace` and switch if the user names another brand.
2. Call `list_utm_channels` to see the source/medium vocabulary the workspace already uses. Reuse an existing pairing when one matches the requested channel; consistent naming is what keeps reports clean. Do not introduce a new source spelling ("linkedin" vs "LinkedIn") when one already exists.
3. Call `build_utm_link` with the destination, source, medium, campaign, and any optional fields.
4. If the user wants a short link or the destination is long, call `list_tracking_domains` and then `create_short_link` on one of the workspace's own tracking domains. If no tracking domain exists, tell the user and offer `create_tracking_domain` rather than creating one unasked.
5. If the user is launching several variants (A/B creatives, multiple placements), build one link per variant with a distinct `content` value.

## Output

- The full UTM link, and the short link if created, each on its own line in a code block.
- A one-line breakdown of the parameters used so the user can verify.
- One reminder: which campaign name to look for in `get_campaign_report` once traffic arrives.

## Do not

- Do not create tracking domains, custom traffic channels, or tags without the user explicitly asking.
- Do not change the destination URL's path or query string beyond appending UTM parameters.
- Do not shorten links on domains the workspace does not own.

Explicit user instructions override these defaults.
