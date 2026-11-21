---
name: get-started
description: Get started with aclipp in ChatGPT. Use when the user first connects aclipp, asks what aclipp can do, or asks about their media coverage, PR analytics, AI visibility, outlets, journalists, reports or dashboards.
---

# Get started with aclipp

aclipp is a PR analytics platform. A workspace holds projects; each project tracks one brand with its media coverage (clippings), competitors, tags, AI visibility prompts, reports and dashboards.

## First steps

1. Call `me` to see which workspace, permissions and project restrictions this connection has. If a tool the user needs is missing, the connection lacks that scope: tell the user to reconnect aclipp and approve the permission.
2. Call `list_projects` and ask the user which project they mean when there is more than one. Pass its ID to every project-scoped tool.
3. When the user belongs to several organizations, `list_organizations` returns their IDs. Without `organizationId`, tools act in the default organization.

## Answering questions

- **Coverage:** `list_clippings` with a filter for date range, channel, outlet, tag, country or sentiment; `get_clipping` for one item in full.
- **Numbers and trends:** call `get_analytics_catalog` first to see which metrics and dimensions the project offers, then `query_analytics` with the `shape` that fits: `scalar` or `scalars` for totals, `series` for trends, `breakdown` or `table` to compare groups. Report the numbers the tools return; do not estimate missing values.
- **AI visibility:** brand mentions by brand, provider or prompt come from the analytics tools. `list_geo_chats` and `get_geo_chat` show individual AI answers; `search_geo_domains` and `search_geo_urls` show the sources AI answers cite.
- **Outlets and journalists:** `list_outlets`, `get_outlet`, `list_authors`, `get_author`.

## Changing data

- Add coverage from a link with `clip_url`, then check its state with `get_clipping_import`. Use `create_clipping` only for coverage without a fetchable link, such as print or broadcast.
- `create_report` makes an empty report; lay it out with `replace_report_blocks`. `replace_report_blocks` and `replace_dashboard_charts` replace the whole collection. Fetch the current version first and keep everything the user did not ask to remove.
- Confirm with the user before deleting anything or replacing report or dashboard content. Every `delete_*` tool also asks for confirmation itself.

## Limits

aclipp does not email journalists or post on your behalf. Say so instead of attempting a workaround.
