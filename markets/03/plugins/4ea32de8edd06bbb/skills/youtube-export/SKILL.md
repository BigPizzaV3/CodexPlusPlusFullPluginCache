---
name: youtube-export
description: Set up and review recurring exports of the user's YouTube channel and video analytics to warehouses, databases, spreadsheets, or cloud storage through Windsor.ai (BigQuery, Snowflake, Google Sheets, PostgreSQL, S3, and more). Use for scheduled, daily, weekly, or automated exports and syncs. Do not use for a one-off answer.
---

# Export YouTube analytics on a schedule

Set up recurring exports of connected YouTube data (connector id `youtube`) to a warehouse, database, spreadsheet, or cloud storage through Windsor.ai, for example daily video views and watch time to BigQuery, or a weekly channel summary to Google Sheets.

## Stay in scope
- Use this skill for recurring, scheduled, daily, weekly, or automated exports and syncs, and for questions about existing export tasks.
- A one-off answer is $youtube-insights, not an export.

## Workflow
1. Call get_destination_tasks to see existing exports and avoid duplicates.
2. Call get_connectors to confirm the channels to export.
3. Call get_destinations to list destinations; note which have create_in_chat true and any reusable credentials.
4. Call get_destination_setup_info for the chosen destination to get its target fields, allowed schedules, and credential_id options.
5. Call get_fields for `youtube` to get the exact field ids to export.
6. Confirm channels, fields, destination target, credential, and schedule with the user, then call create_destination_task once. If create_in_chat is false, hand the user the setup_url instead.

## Rules
- Prefer a rolling date_preset (for example last_7d) over fixed dates so each run stays fresh.
- Never put secrets in config; sensitive values are entered by the user in the setup_url form.
- Report the created task's id, schedule, and manage_url from the tool result.

## Hand-offs
- Reporting -> $youtube-insights. Connecting a channel -> $youtube-connect.
