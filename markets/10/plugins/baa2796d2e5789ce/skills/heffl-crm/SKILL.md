---
name: heffl-crm
description: "Find, summarize, create, update, import, or delete records in a connected Heffl CRM workspace, including leads, clients, deals, tasks, notes, and reminders."
---

# Work with Heffl CRM

Use the connected Heffl MCP tools. Read [operating rules](references/operating-rules.md) before this workflow. The server exposes the complete available MCP action surface; discover unfamiliar tools through heffl_search_actions and schemas through heffl_describe_action. Never require the CLI for an MCP workflow.

For an unknown object call records_catalog; use its canonical key. Known objects can be read directly with records_list or records_details. Describe unfamiliar fields, relations, operators or aggregates with records_describe, surface:"read". Select only needed fields, filter server-side and follow returned cursors. If you stop early, disclose that results are partial.

Resolve names with records_resolve; use positive integer IDs returned by tools. Resolve ambiguous candidates with the user. users_list finds teammates. Read notes with notes_list/notes_details and record history with records_timeline when needed for a customer briefing. Report only supported facts, amounts, dates and source links.

For writes describe the object's write surface with mode:"create" or "update". Use records_create/update/delete for ordinary CRUD. Use records_upsert only for an explicit exact-match import; multiple matches are a conflict, never a merge. records_bulkUpdate accepts up to 25 explicit IDs; do not infer a broad update from a vague request. leads_convert creates a deal, transfers history and archives the lead.

Reminders are separate notifications, not task due dates. Use reminders_list/create/snooze/dismiss. Resolve the parent and recipients, supply an ISO timestamp with timezone, and clarify an ambiguous time. Recipients must belong to the workspace; snooze and dismissal require the creator. A reminder may deliver through email, push or Cliq according to recipient preferences.

Preserve date ranges, requested billing filters and currency semantics. Use relative date tokens such as $last_week with op:"between" where supported and report returned timeScope. Never add invoiceRequired=true without user intent. Scheduled visit dates differ from completion timestamps. Missing visit invoice links do not prove a job is unbilled; never sum repeated parent job totals across visits. Answer list requests directly. Create exports only when requested, using structured results.
