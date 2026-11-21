---
name: record-work
description: "Record or correct Otis billable time, services or reported AI usage, or start and stop a timer that tracks work time."
---

# Record work with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: clients_list, client_save, billables_list, billable_record, timer_start, timer_stop, timers_list.

1. When the user is starting work now, use timer_start for the client and task; when they say they stopped, use timers_list to find the running timer and timer_stop. Pass a reported time only if the user gives one. Ask for the hourly rate if it is not known, and pass rate_minor so the tracked hours are recorded as billable work. Several timers can run; never stop one the user did not mean.
2. Identify the client, description, kind, quantity/unit, supplied amount and optional rate/cost. AI usage must be explicitly measured or estimated; do not measure or price it automatically. Inspect existing records when the request might be an edit or duplicate.
3. Create with billable_record, or preserve item_id when correcting an unreserved, uninvoiced item. Do not edit linked expenses through this tool. Return the recorded facts and remaining billable amount; saving work does not invoice it.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
