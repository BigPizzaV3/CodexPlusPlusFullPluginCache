---
name: windsor
description: Analyze marketing and business data and run supported write actions across 350+ sources through Windsor.ai. Use when the user asks about performance, metrics, or spend from any connected platform (ads, analytics, SEO, CRM, e-commerce, payments, warehouses), wants to compare channels, connect a source, run a supported action such as pausing a campaign or setting a budget, or schedule a recurring data export. Do not use for writing marketing copy or for general advice unrelated to the user's connected accounts.
---

# Windsor.ai

Windsor.ai exposes live data (read) and supported write actions across 350+
connected sources through MCP tools. Every tool takes a `connector` id, a
lowercase slug such as `google_ads` for Google Ads, `facebook` for Meta Ads
(Facebook and Instagram Ads), or `googleanalytics4` for GA4. This app is not
scoped to a single connector, so always discover the right slug and accounts
first.

## Golden rules
- **Never guess** connector slugs, account ids, field ids, action ids, or option
  ids. Get them from `get_connectors`, `get_fields`, `list_actions`, and
  `get_options`, and call those before `get_data` or `execute_action`.
- **Reads are safe; writes change live platform state.** Only call
  `execute_action` after the user confirms the specific change.

## Core read workflow
1. `get_connectors` shows connected accounts and, per connector, the available
   `actions` and `options`. Pass `include_not_yet_connected=True` to list every
   available source.
2. `get_fields` (and `get_options` for date-filter columns and connector
   options) returns valid field ids for the chosen connector. Field ids passed
   to `get_data` must come from `get_fields`.
3. `get_data` reads the metrics for the connector, fields, accounts, and date
   range, then you analyze the result.

## Write actions
- `list_actions` returns the write actions a connector supports and each action's
  parameter schema. The set is whatever it returns, so do not assume an action
  exists.
- `execute_action` runs one action id against one account id with params matching
  its schema. It modifies external platform state, for example pausing or
  enabling a campaign, setting a budget or bid, managing an audience list or
  flow, or posting content, so confirm the exact change with the user first.

## Connecting a source
For any request to connect, authorize, add, or reconnect an account, call
`get_connectors(include_not_yet_connected=True)` for the slug, then
`get_connector_authorization_url` for a ready-to-open setup link, or
`get_connector_connect_info` for the auth type and the manual credential fields.
Sensitive credentials are entered by the user in that form, never pasted into
chat.

## Scheduled exports (destinations)
- `get_destinations` lists where data can be exported on a schedule (BigQuery,
  Google Sheets, Snowflake, databases, storage) and any reusable credentials.
- `get_destination_setup_info` describes a destination's target fields and
  allowed schedules. `create_destination_task` sets up a recurring export;
  confirm the source, destination, and schedule with the user first.

## Support and account
- `get_current_user` returns the authenticated Windsor.ai user.
- `get_windsor_login_url` returns an auto-login link into the dashboard.
- `contact_windsor` files feedback, a support request, or a feature request.
