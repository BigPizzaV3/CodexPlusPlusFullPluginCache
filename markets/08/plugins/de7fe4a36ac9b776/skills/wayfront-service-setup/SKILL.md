---
name: wayfront-service-setup
description: Design, create, audit, or update Wayfront services, including pricing, recurring billing, renewal order behavior, request allowances, intake and onboarding forms, task templates, deadlines, assignments, and add-ons. Use when deciding how a sold service should create and renew delivery work.
---

# Wayfront Service Setup

A service is both a catalog item and a template for the orders created when it is purchased. Confirm how the work should repeat before changing its billing or renewal settings.

## Inspect the current setup

Use `workspace-info` if service access is unavailable or the user is unsure which workspace is connected. Use `search-wayfront-docs` when the decision depends on current Wayfront behavior that is not present in the live service schema or records.

List and show the relevant service before proposing a change. Also inspect intake and onboarding forms separately: service responses do not include every attached-form relationship, while form responses show their linked services. Check active subscriptions when changing a recurring service.

Use `service-read` for `list`, `show`, and `get_task_templates`; use `service-write` for `create`, `update`, and `sync_task_templates`. Form inspection uses `form-read`; existing subscription inspection uses `subscription-tool`.

Recommend variants only when an option changes price or quantity but keeps the same forms, tasks, renewal behavior, assignees, and reporting. Use separate services when those workflows differ. Variants are visible through MCP but cannot be created or updated there; hand variant configuration to the Wayfront interface.

## Choose billing and renewal behavior

The MCP exposes raw service codes. Interpret them for the user instead of presenting the codes alone:

- `recurring = 0`: one-time service.
- `recurring = 1`: recurring service without a trial or setup period.
- `recurring = 2`: trial or setup-fee period followed by recurring billing.
- `recurring = 3`: legacy limited-recurring-count mode. Preserve an existing service with this value unless the user explicitly wants to migrate it, and use the Wayfront interface for that decision; do not select it for a new MCP-created service.
- `r_period_t`: `D` days, `W` weeks, `M` months, or `Y` years; `r_period_l` is the number of those periods.

For a recurring service, choose exactly one `recurring_action`:

- `0` — **reopen the same order:** use for one continuing engagement, such as ongoing SEO for one website. A successful renewal returns the existing order to the work queue, resets its due date when configured, resets its existing tasks to incomplete, and syncs order-level staff from the current service. It keeps the existing order tasks and their assignees rather than importing the latest service task template. The conversation and delivery history stay on that order.
- `1` — **create new order(s):** use when each billing cycle is independent work, such as a new article or design project each month. Each cycle gets a separate order and its own intake and task state. `multi_order` is the number of orders created per purchased quantity and renewal cycle when greater than one.
- `2` — **service requests:** the subscription grants client-requested orders. `request_orders` is the per-period allowance: `0` disables requests and `127` represents unlimited. `max_active_requests` limits simultaneous unfinished requests, with `0` meaning no active limit. Use an active-at-a-time limit when “unlimited” should still protect team capacity.
- `3` — **no delivery action:** use for billing-only renewals such as hosting when no new or reopened work is required.

Explain the recommended option in plain language and obtain confirmation before writing it. For recurring services, `r_period_l` and `r_period_t` are required. A trial/setup service also requires its initial period and price settings.

## Consequential settings

- Changing `recurring_action` changes what future successful renewals do, including renewals on existing subscriptions that still reference the service. Review active subscriptions first.
- Changing catalog pricing or billing periods does not update the payment amount or schedule of an existing processor subscription. Existing subscriptions must be changed through subscription management; the MCP subscription tool is read-only.
- Supplying `employees`, `parent_services`, `onboarding_form_ids`, or metadata on update replaces that complete collection. Service reads do not currently return employee or add-on-parent assignments, so do not write `employees` or `parent_services` unless the user supplies or explicitly confirms the complete desired list. Reconstruct intake and onboarding associations from form responses, preserve every verified association that should remain, and re-read the related forms after writing. `intake_form_id` replaces the current intake-form association.
- `sync_task_templates` replaces the service's entire reusable checklist. Template edits apply to newly created orders; they do not rewrite tasks already copied onto existing orders. Reopening an existing recurring order resets that order's existing tasks rather than importing a newer template.
- Making a service public changes what clients can discover and buy. Changing add-on parents changes where it can be offered. A deadline affects due-date behavior once work can begin.

Before a consequential update, show a concise before/after summary covering price, billing interval, renewal behavior, verified forms, tasks, known assignments, visibility, and affected active subscriptions. Mark relationships the MCP cannot verify as unknown rather than implying the audit is complete. After writing, show the service and related forms again and separately identify anything that still requires the Wayfront interface.

For a user-facing product explanation or interface walkthrough, search the current Wayfront documentation, retrieve the relevant result with `get-wayfront-doc`, and share its canonical source URL.
