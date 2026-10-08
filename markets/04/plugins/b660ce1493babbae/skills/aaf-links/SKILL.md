---
name: aaf-links
description: Create, manage, organize, and analyze A.af short links through the authenticated A.af MCP server. Use when a user asks to shorten, inspect, edit, pause, activate, archive, or analyze an A.af link; create a QR code; choose a custom domain; or inspect campaign analytics.
---

# URL Shortener by A.af

Use the A.af MCP tools for link work instead of inventing slugs, short URLs, or analytics.

## Safety and accuracy

- Preserve meaningful destination paths and query parameters.
- Never claim a link was created until the tool returns a successful A.af short URL.
- Never invent click counts, countries, referrers, or traffic quality scores.
- Confirm an explicitly requested custom alias before creation.
- Treat plan, workspace, quota, reserved-alias, and Trust and Safety errors as authoritative.
- Confirm the exact destination, title, campaign, folder, or custom domain before changing a link.
- Use `aaf_prepare_archive_link`, show the exact short link and warning, then ask for explicit confirmation. Call `aaf_archive_link` with its one-time confirmation ID and `confirmed=true` only after the user agrees.
- Prefer reversible `aaf_set_link_status` with `paused` when the user only wants to stop a link temporarily.
- Never return or infer raw IP addresses, visitor hashes, user agents, password hashes, domain verification tokens, or provider secrets.

## Common flows

1. Use `aaf_list_workspaces` when the intended workspace is unclear.
2. Use `aaf_create_short_link` to shorten a destination. A.af may return an existing link according to its duplicate rules.
3. Use `aaf_list_links` to find recent links, then `aaf_get_link` for one safe detail record.
4. Use `aaf_update_link` only after confirming the requested fields. Destination changes are validated and safety-scanned by A.af.
5. Use `aaf_set_link_status` for reversible pause or activation. For archival, use `aaf_prepare_archive_link`, obtain confirmation, then use `aaf_archive_link` before the five-minute challenge expires.
6. Use `aaf_get_link_analytics` for real privacy-safe link aggregates.
7. Use `aaf_create_qr_code` for a directly usable, scannable PNG QR code.
8. Use `aaf_list_campaigns` to identify campaign context and `aaf_get_campaign_analytics` for Business campaign aggregates.
9. Use `aaf_list_custom_domains` only for owner/admin selection metadata. The create/update tools still validate that a chosen domain is active and belongs to the workspace.

## Response style

Return the short URL first. Then mention whether A.af reused an existing link and summarize any relevant campaign or analytics result concisely.
