---
name: ga4-export
description: Set up and review recurring exports of the user's Google Analytics 4 (GA4) data to warehouses, databases, spreadsheets, or cloud storage through Windsor.ai (BigQuery, Snowflake, Google Sheets, PostgreSQL, S3, and more). Use for scheduled, daily, weekly, or automated exports and syncs. Do not use for a one-off answer.
---

# Export GA4 data on a schedule

Set up recurring exports of connected Google Analytics 4 data (connector id `googleanalytics4`) to a warehouse, database, spreadsheet, or cloud storage through Windsor.ai, for example daily sessions and conversions by channel to BigQuery, or a weekly landing-page report to Google Sheets.

## Stay in scope
- Use this skill for recurring, scheduled, daily, weekly, or automated exports and syncs, and for questions about existing export tasks.
- A one-off answer is $ga4-insights, not an export.

## Workflow
1. Call get_destination_tasks to see existing exports and avoid duplicates.
2. Call get_connectors to confirm the properties to export.
3. Call get_destinations to list destinations; note which have create_in_chat true and any reusable credentials.
4. Call get_destination_setup_info for the chosen destination to get its target fields, allowed schedules, and credential_id options.
5. Call get_fields for `googleanalytics4` to get the exact dimension and metric ids to export.
6. Confirm properties, fields, destination target, credential, and schedule with the user, then call create_destination_task once. If create_in_chat is false, hand the user the setup_url instead.

## Rules
- Prefer a rolling date_preset (for example last_7d) over fixed dates so each run stays fresh.
- Never put secrets in config; sensitive values are entered by the user in the setup_url form.
- Report the created task's id, schedule, and manage_url from the tool result.

## Hand-offs
- Reporting -> $ga4-insights. Connecting a property -> $ga4-connect.
