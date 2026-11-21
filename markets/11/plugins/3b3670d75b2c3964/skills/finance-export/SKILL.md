---
name: finance-export
description: Set up and review recurring exports of Stripe, QuickBooks, PayPal, Xero, Chargebee, and Braintree data to warehouses, databases, sheets, or storage through Windsor.ai. Use for scheduled or automated exports and syncs. Do not use for a one-off answer.
---

# Export finance data on a schedule

Set up recurring exports of connected finance data (Stripe, QuickBooks, PayPal, Xero, Chargebee, and Braintree) to a
warehouse, database, spreadsheet, or cloud storage through Windsor.ai, for example
daily charges to BigQuery, or a monthly revenue summary to Google Sheets.

## Stay in scope
- Use this skill for recurring, scheduled, daily, weekly, or automated exports and syncs, and for questions about existing export tasks.
- A one-off answer is $finance-insights, not an export.

## Workflow
1. Call get_destination_tasks to see existing exports and avoid duplicates.
2. Call get_destinations to list destinations; note which have create_in_chat true and any reusable credentials.
3. Call get_destination_setup_info for the chosen destination to get its target fields, allowed schedules, and credential_id options.
4. Call get_fields for the source connector to get the exact field ids to export.
5. Confirm source, accounts, fields, destination target, credential, and schedule with the user, then call create_destination_task once. If create_in_chat is false, hand the user the setup_url instead.

## Rules
- Prefer a rolling date_preset (for example last_7d) over fixed dates so each run stays fresh.
- Never put secrets in config; sensitive values are entered by the user in the setup_url form.
- Report the created task's id, schedule, and manage_url from the tool result.

## Stay in scope (routing)
- Reporting -> $finance-insights. Connecting a source -> $finance-connect.
