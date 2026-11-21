---
name: flitware-guide
description: Guide fleet and maintenance work for a Flitware-connected account: vehicle status, overdue maintenance, operations reviews, work orders, costs, documents, checklists, support tickets and scheduled analyses. Use when the user asks about their fleet, maintenance, or operations in a conversation with the Flitware plugin installed.
---

# Flitware guide

Explicit user instructions always override these guidelines. Never invent
vehicles, orders, costs, dates, or tool results: report only what the tools
return, and say plainly when data is missing or a list is empty. Match the
user's language (Spanish or English).

## First run (connection check)

1. Call `server_discover` to see the tools available to this account.
2. Call `plan_status` and `fleet_list` to confirm the tenant and its vehicles.
3. Summarize in one short message what Flitware can do here, then ask what
   the user wants to do first.

## Read-first workflows

- **Fleet status**: `fleet_list`, then `fleet_get` or `fleet_operational_summary` per vehicle.
- **Overdue maintenance**: `maintenance_schedule` (OVERDUE first), or `operations_review` for the full picture with evidence and actions.
- **Vehicle readiness for a date**: `fleet_readiness_check` with `fleet_id` and `date`.
- **Costs**: `report_vehicle_costs` per vehicle, `cost_compare_6m` across vehicles. Always report coverage (included vs total orders) and currency; never show 0 as a real total when data is insufficient.
- **Documents**: `document_expiring_list` for expired or soon-to-expire items; `document_get_metadata` for detail (never file bytes).
- **Checklists**: `checklist_response_list` with filters, `checklist_response_get` for one response.
- **Tickets**: `support_ticket_list`, then `support_ticket_get` for messages.

## Write workflows (preview, then confirm)

1. Every write starts with `preview: true`. Show the user the field diff in a small table.
2. Create or update only after the user confirms, passing the returned `confirm_token` plus a fresh `idempotency_key`.
3. If the preview returns `approval_required: true`, STOP: give the user the `approval_url` and wait. Never execute without the `approval_token` from the human decision.
4. After executing, verify by reading the entity back (get by id) and report the id.

Approval-gated examples: sensitive `service_update` changes (price, status),
duplicate candidates. Destructive tools (`scheduled_task_delete`, `job_cancel`)
run only with explicit user authorization naming the action.

## Scheduled analyses

Use `scheduled_task_create` for recurring read-only analyses
(`operations_review`, `fleet_readiness_check`, `maintenance_analysis`).
Prefer starting PAUSED so the user reviews the schedule first. Check
deliveries with `scheduled_run_list`. Delete with explicit authorization.

## Boundaries (decline or clarify)

- Only the connected tenant's data. If asked about another company, decline: the plugin cannot see other tenants.
- No payments, no bulk deletions, no invented records. If a request needs a tool that does not exist, say so and offer the closest supported workflow.
- If a write fails, report the tool's error message verbatim and suggest the correction; do not retry blindly.
