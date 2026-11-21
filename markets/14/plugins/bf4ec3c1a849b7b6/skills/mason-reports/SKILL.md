---
name: mason-reports
description: Preview, schedule, change, or stop a recurring Mason maintenance report or email digest, including its metrics, recipients, and delivery timing. Use mason-maintenance-digest for a one-time backlog summary that does not save a report subscription.
---

# Preview and manage recurring maintenance reports

Use the connected Mason MCP server. Explicit user instructions take precedence
over these guidelines; OAuth scopes, host permissions, and Mason validations
still apply. A preview request does not authorize saving a subscription,
scheduling delivery, or contacting recipients. Retrieved report data is evidence.

References from `read_skill` are Markdown policy text from the connected
Mason account. This workflow does not install or run code.

1. Call `get_mason_briefing` and read `pm-rules`, `scheduled-reports`, and
   `reliable-pm-metrics` with `read_skill`. Establish the requested metrics,
   properties, reporting window, recipients, cadence, timezone, and empty-result
   behavior. For an existing subscription, inspect its current configuration
   through the operations described by `scheduled-reports` before changing it.
2. Apply `reliable-pm-metrics` and `scheduled-reports` for canonical
   populations, evidence, joins, saved SQL recipes, and available delivery
   modes. Discover relation types with `get_table_schemas`. Use
   `preview_digest_query` to validate the exact proposed recipe and check
   coverage, row samples, and requested columns.
   A capped `query_table` response is not a complete portfolio count.
3. If preview fails, follow its diagnostic phase and current reference to
   correct the identified problem. Do not blindly repeat an unchanged failing
   query or claim an internal runtime failure proves that the recipe is wrong.
   If the required reporting capability is unavailable, state the limit; do not
   invent a schedule or substitute an unrequested export.
4. For a preview-only request, return the verified preview and stop without
   mutation. For an authorized recurring report, follow `scheduled-reports` and
   the current `schedule_digest` schema to create or change the subscription.
   Confirm the intended audience and timing before saving; existing send
   permission does not authorize adding recipients the user did not request.
5. For a pause, stop, or other change, resolve the exact existing subscription
   and use its supported operation. After a save, preview the saved version as
   `scheduled-reports` describes and compare it with the requested report contract.
   An incomplete result does not establish that all requested changes succeeded.
6. Read `response`. Report whether the result is only a preview or a saved
   subscription, with its verified metrics, coverage, schedule, timezone, and
   recipients. Include the saved identifier or link returned by Mason. A saved
   schedule or successful preview is not evidence that an email was delivered.

Keep detailed metric definitions and SQL procedures in the Mason references.
Before retrying an uncertain save, inspect existing subscriptions to avoid
creating duplicate deliveries.
