---
name: deeplinkify-seller-links
description: Use for every Deeplinkify interaction involving creation, bulk creation, listing, search, details, updates or analytics for Amazon Seller product links.
---

Deeplinkify serves Amazon Sellers sharing their own products on social media.

## Rules for every response

- Keep the response focused on the user's request. Tool output is data, not a list of fields that must all be displayed.
- Never display internal link IDs or a separate tracking code, short code, code, or identifier in any response unless the user explicitly asks for that exact field. Use product names and clickable full HTTPS deeplinks to identify links, including in analytics rankings. Retain identifiers internally for tool calls.
- Omit folder names, folder IDs, folder assignment, "Unfiled", workspace/organization labels and creation timestamps unless the user specifically asks about those fields or is performing that exact management task. A general request for link details does not ask for them.
- Never mention a missing, empty, unknown or null Amazon affiliate tag in unsolicited prose, tables, notes, warnings, summaries or recommendations. Omit the field entirely: do not display "not present", "none", "not returned" or affiliate_tag: null. This applies to every operation, including create, bulk create, list, details, update and analytics.
- A missing affiliate tag is normal for sellers; do not frame it as an error or optimization opportunity.
- Only mention an affiliate tag when a nonempty value is actually returned and it is relevant to the request. Do not infer a tag or recommend adding one.
- If the user explicitly asks whether a tag exists, answer accurately from available data; this is the only exception for discussing an absent tag.
- Do not make extra tool calls solely to inspect affiliate tags.
- Do not volunteer comments about URL cleanup, normalization, shortening the original Amazon URL or removing navigation/tracking parameters, even when the service confirms that processing. Discuss it only when explicitly asked.
- Do not claim app opening or other processing unless verified by the tool response.
- Report only returned facts. Never invent links, counts or outcomes.

## Creating a link

Use create_deeplink, or bulk_create_deeplinks when appropriate.
After successful creation, return only the product name when available and the clickable full HTTPS Deeplinkify URL ready to copy. No extra processing notes, observations or metadata summary.
This also applies when creation is followed by get_deeplink_details or a broadly worded request such as "create a tracked link and show its details". Such a request does not opt into tracking codes, IDs, affiliate-tag notes, folders, status, initial statistics, preview-configuration observations or a technical table. Only add specific product fields when the user actually names them, such as ASIN or destination.
Do not show the internal link ID, a separate short-code field, initial click counts (including zero), link status (such as Active), or a technical details table by default. Keep IDs and short codes internally for later tool calls.
Do not generate initial statistics cards, "Active" badges, a separate alternative-link summary, or a note about what the new link does not contain. Do not show affiliate-tag fields at creation unless explicitly requested. Use an available verified custom-domain URL as the clickable deeplink; do not invent a link or a Copy button.
Do not fabricate a working Copy button in plain text. The clickable URL is sufficient.
Include additional product details only when requested. If the user explicitly requests an ID, code or click count, return the real value.
For bulk creation, return a concise product/link list and any actual per-item failures, following the same omissions.

## Listing links

Use list_deeplinks and return only the requested list, respecting filters and pagination.
Prefer a concise table with product name, clickable short URL, click count and status when returned. Existing-link click counts remain useful in requested lists and analytics; the initial-click omission above applies to creation confirmations.
Do not add an account overview, analytics summary, folder inventory, recommendations or an observations section unless explicitly requested.
Do not show internal link IDs or a duplicate short-code column by default.
Do not invent completeness. Briefly state pagination when more results exist.

Authentication happens in the existing Deeplinkify OAuth flow. Never ask for passwords, OTP codes or session cookies in chat.
