---
name: clientika-workflow
description: Safely manage a user's Clientika sites through the Clientika MCP tools, and handle missing product capabilities transparently.
---

# Clientika workflow

Use Clientika MCP tools only for the user's connected account. Never invent a shop ID, user ID, permission, tariff capability, or successful result.

## Choose a site

1. Call `tenant_shops_list` to show the sites the connected account can access.
2. If there is more than one, ask which site to use. Use the returned shop ID only with Clientika tools; do not accept a user-supplied ID as proof of access.
3. If access is denied or a capability is unavailable on the tariff, explain that outcome. Do not offer a feature request for a tariff restriction or missing permission.

## Read and change data

- Read the relevant product, category, service, page, order, booking, setting, or media item before changing it when the change depends on its current state.
- Use only the specific typed Clientika tool for the requested operation. Never claim an update succeeded unless the tool confirms success.
- For destructive operations such as deleting a product or media asset, state what will be deleted and get confirmation before calling the tool.
- Use booking dates as date-only values where the tool asks for `YYYY-MM-DD`; use explicit UTC instants where it asks for a datetime.
- When requested, use `get_entity_seo_clusters` only to read assigned SEO clusters for an authorized entity. Use IDs and entity types returned by Clientika. Do not claim the plugin can generate SEO content, images or videos, or run AI generation.

## Errors and missing capabilities

- Explain authentication, permission, not-found, validation, capability/tariff, and temporary service errors accurately. A technical failure is not a missing product feature.
- When a requested product capability is genuinely absent, explain the limitation and offer to submit a feature request. Do not create one automatically.
- Call `create_feature_request` only after the user clearly says to submit it. Send only a concise title, requested behavior, user goal, relevant entity type, category, and the shop's displayed name if needed to disambiguate. Never send conversation history, email, user ID, or shop ID.
- After submission, give the user the returned ticket number. Use `feature_requests_list_mine` or `feature_request_status_get` only when the user asks about their requests.
