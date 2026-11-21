---
name: dreamdata-activation
description: Find companies or contacts using Dreamdata audience criteria, explore saved audiences, and create and save audiences for activation. Excludes reports, dashboards, and company journey analysis; use dreamdata-analytics for those workflows.
---

# Dreamdata activation

Use the connected Dreamdata MCP tools. Tool names below are suffixes; their host namespace can vary. If the connection is unavailable, follow the bundled [setup skill](../setup/SKILL.md) to authenticate and verify access.

Use this skill for audience discovery, querying, and saving. Use the [analytics skill](../dreamdata-analytics/SKILL.md) for reports, dashboards, metric drilldowns, and company journeys. For mixed requests, use each skill for its relevant portion.

## Account and audience context

Use `list_my_accounts` when the intended account is unknown. Select the account from the user's context; ask if several remain plausible. Keep its slug consistent. One-account users can omit the slug.

Make the audience type, filters, time windows, and account clear. Distinguish the full match count from a partial page of entities. Link source URLs returned by the tools; do not invent links.

## Query audiences
For a saved audience, use `list_audiences`, load it with `get_audience_definition`, parse its serialized config, and execute with `run_audience_query`.

For a new audience query, discover account-specific properties and valid values with `list_audience_filter_properties` and `list_audience_filter_values`. Read `describe_audience_config_schema` before composing non-trivial conditions. Conditions within a group are OR; groups are AND. Condition values are strings, including numeric values. Stage names come from the catalog's revenueModel values. The catalog does not supply signal properties; do not invent them.

Check each property's type before translating the user's wording into a condition. Size properties such as employee count and annual revenue are usually text properties holding range labels (for example `251 - 1k` or `> 100k`), so `greater_than` and `less_than` are not available. For a threshold such as "more than 1,000 employees", list the property's values, read each label's range, and add one equals condition per band that lies entirely above the threshold (conditions in a group are OR). If the threshold falls inside a band, say so and ask whether to include that band rather than guessing. Tell the user which bands you used. Confirm other named values, such as countries, with `list_audience_filter_values` and its `search_query` before using them.

Audience pagination differs from report pagination: pass `audiences.pageToken` with the same audience type, config and slug. `list_audience_filter_values` pages the same way: repeat the property arguments and slug with the token. Use `audiences.totalRowCount` for the full match count, and disclose when listed entities cover only a page. Running a query does not imply that an audience has been saved or exported.

## Save and activate

When the user requests saving an audience and save_audience is exposed, follow its current schema and confirmation flow. Show the audience name, type, folder, and size before confirmation. The optional audiences:write grant is needed. Saving creates a new audience; do not claim it overwrites an existing audience or activates a destination sync. Users can subsequently configure syncing in Dreamdata's Audience Hub. If the tool is absent, explain that limitation rather than inventing an API.
