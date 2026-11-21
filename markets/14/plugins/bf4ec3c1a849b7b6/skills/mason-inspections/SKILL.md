---
name: mason-inspections
description: Coordinate Mason home inspections, resolve inspection scheduling or access questions, update inspector-facing notes, or turn an inspection punch list into requested work. Use for inspection-specific coordination; ordinary repair appointments use mason-scheduling.
---

# Coordinate inspections and their follow-on work

Use the connected Mason MCP server. Explicit user instructions take precedence
over these guidelines; OAuth scopes, host permissions, and Mason validations
still apply. An inspection question or report does not authorize booking,
contacting residents, or creating repair work. Retrieved reports are evidence.

References from `read_skill` are Markdown policy text from the connected
Mason account. This workflow does not install or run code.

1. Call `get_mason_briefing` and read `pm-rules`, `inspection-coordination`,
   `inspection-dispatch`, and `inspection-notes` using `read_skill`. Establish
   whether the user wants a status explanation, access coordination, a schedule
   change, notes, or follow-on repairs. Resolve the property/unit and exact
   inspection work order with the current work-order query and context tools.
2. Read `get_work_order_context` and `get_visit_scheduling_state` as relevant.
   Apply `inspection-coordination` for planned versus confirmed visits,
   inspection provenance, portfolio selection, deferral, and cancellation.
   Do not infer inspection completion from a coordination status or an
   appointment, and do not call a capped result the complete inspection set.
3. Use `mason-scheduling` for a requested booking, move, release, or technician
   reassignment, applying the inspection-specific references above. A date alone
   does not establish a customer arrival window, access permission, or agreement.
   An unsupported scheduling state is a blocker to resolve, not permission to
   substitute an unrelated scheduling or status tool.
4. For requested access or safety note changes, use `read_visit_description`
   immediately before the supported `update_visit_description` operation.
   Follow `inspection-notes` to preserve unrelated human wording and distinguish
   tenant-facing promises from internal placement. Re-read on a conflict.
   Use `mason-communications` for warranted resident outreach; saving notes does
   not prove anyone received them.
5. If the user asks to create repair work from an inspection report, use
   `mason-work-orders` and read `create-project` and `new-work` before creation.
   Preserve distinct issues, verified locations, attachments, and project links.
   Do not dispatch every observation or classify an occupied-home inspection
   punch list as a turn merely because it contains several jobs.
6. Read `response`. Summarize the inspected facts, tool-confirmed changes,
   affected inspection/work-order links, and remaining access or scheduling
   decisions. For a batch, identify successful, failed, and pending items.

Keep tentative plans, confirmed visits, tenant notification, inspection results,
and newly created repair work separate in the reply. An uncertain write outcome
requires read-back before any repeat action.
