# Verified Minz capabilities
Exported from catalog 1.9.0 (60 functions). Check the capabilities and schema of the selected Minz app at run time when needed; this list is not a promise for every future version. Tools marked **write** exist in the connector but this plugin's skills never call them.

| Group | Function | Tool name | Effect | Purpose |
|---|---|---|---|---|
| CRM | crm.accounts.search | crm_accounts_search | read | Search CRM accounts visible to the delegated user and return bounded public business metadata |
| CRM | crm.care.search | crm_care_search | read | List after-sales customer-care tickets (Customer Care console) visible to the delegated user, with category, account id, status, priority and SLA breach flag |
| CRM | crm.contacts.search | crm_contacts_search | read | Search contacts visible to the current user in the current workspace |
| CRM | crm.contracts.search | crm_contracts_search | read | Search sales contracts visible to the current user by start month or expiry window; contract value and notes are excluded |
| CRM | crm.deals.follow | crm_deals_follow | write | Follow or unfollow one deal the delegated user can see |
| CRM | crm.deals.history | crm_deals_history | read | Read the bounded history projection for one visible deal |
| CRM | crm.deals.lookalike | crm_deals_lookalike | read | List recently won deals (optionally by industry) usable as look-alike references: title, account, industry, products and masked value |
| CRM | crm.deals.search | crm_deals_search | read | Search deals visible to the current user in the current workspace |
| CRM | crm.deals.win_patterns | crm_deals_win_patterns | read | Aggregate analysis of recently won deals in the caller's scope: top activity channels, top products, deal count and a few example won deals |
| CRM | crm.kpi.progress | crm_kpi_progress | read | Read KPI/quota plans (target, stored actual, progress percent) visible to the delegated user: team-level plans in their org scope and their own individual plans |
| CRM | crm.leads.search | crm_leads_search | read | Search leads visible to the delegated user and return only bounded business fields; lead name, email, and phone are excluded |
| CRM | crm.meetings.last | crm_meetings_last | read | Read metadata and a short summary of the most recent meeting (or one meeting by id) visible to the delegated user |
| CRM | crm.notes.search | crm_notes_search | read | Search CRM notes visible to the current user and return a truncated preview; other users' personal notes, tags and full content are excluded |
| CRM | crm.pipeline.health | crm_pipeline_health | read | Report visible open-deal pipeline health: counts of stale, stuck and soon-to-close deals with the top 10 of each |
| CRM | crm.pipeline.summary | crm_pipeline_summary | read | Return the Core-computed pipeline aggregate for the current workspace |
| CRM | crm.pipelines.list | crm_pipelines_list | read | List sales pipelines visible to the current user with stage names and visible open-deal counts |
| CRM | crm.products.search | crm_products_search | read | Search the product catalog visible to the current user; price is null when the user lacks sensitive-financial access |
| CRM | crm.quotes.search | crm_quotes_search | read | Search quotes visible to the current user by status, deal or contact; amount, notes and contact details are excluded |
| CRM | crm.team.search | crm_team_search | read | Search team members inside the current user's org-chart scope and return only id, display name and role; email, phone and credentials are excluded |
| Work | general.activities.search | general_activities_search | read | Search bounded activities visible to the delegated user, optionally within a date range and sorted by date |
| Work | general.approvals.search | general_approvals_search | read | List workflow approval tasks assigned to the delegated user (open by default) |
| Work | general.calendar.create_event | general_calendar_create_event | write | Create a native calendar event owned by the delegated user |
| Work | general.calendar.delete_event | general_calendar_delete_event | write | Delete ONE native calendar event the delegated user may delete (their own, or any with admin authority), notifying invitees of the cancellation and removing it from their connected Google Calendar |
| Work | general.calendar.respond_event | general_calendar_respond_event | write | Set the delegated user's own RSVP (accepted, declined or tentative) on a calendar event they are invited to |
| Work | general.calendar.search | general_calendar_search | read | Search bounded native calendar event rows visible to the delegated user, by explicit from/to or by a range shortcut (today, this_week, next_7_days) |
| Work | general.calendar.update_event | general_calendar_update_event | write | Change the title, time, location, description, meeting URL or visibility of ONE native calendar event the delegated user may edit (their own event, or any when they hold admin authority) |
| Work | general.notes.search | general_notes_search | read | Search the delegated user's general notes (personal or tenant-shared notes that are not attached to a deal, contact, activity, account, meeting or chat thread) |
| Work | general.notifications.search | general_notifications_search | read | List the delegated user's recent in-app notifications (type, title, read state and time only) |
| Work | general.requests.search | general_requests_search | read | List the workflow requests submitted by the delegated user (My Requests) with state and SLA deadline |
| Work | general.tasks.create | general_tasks_create | write | Create one task owned by the delegated user |
| Work | general.tasks.search | general_tasks_search | read | Search tasks visible to the delegated user, including personal-task privacy rules, with overdue, deal, contact, due-date range and due-date sort filters |
| Work | general.tasks.update | general_tasks_update | write | Update one existing task the delegated user is allowed to edit (title, description, status, priority, due date, assignee, linked deal or contact) |
| MinzSpend | finance.expenses.search | finance_expenses_search | read | Search MinzSpend expense records visible to the verified user |
| MinzSpend | finance.reports.search | finance_reports_search | read | Search MinzSpend expense settlement and reimbursement reports |
| Operations | ops.cases.detail | ops_cases_detail | read | Read one workflow case visible to the delegated user, including its active tasks and SLA state |
| Operations | ops.cases.search | ops_cases_search | read | Search workflow cases (tickets) visible to the delegated user with the full /cases filter and sort surface: state, workflow, step, object type, assignee, SLA state, date ranges, duration, archive/acknowledge flags, sort and offset paging |
| Operations | ops.sla.summary | ops_sla_summary | read | Summarize SLA health of the running workflow cases visible to the delegated user: completion time, on-time rate, bottlenecks and cases at risk |
| Operations | ops.workflow_definitions.search | ops_workflow_definitions_search | read | Search active workflow definitions (names and categories only) for context when reading cases |
| Operations | ops.workflow_instances.search | ops_workflow_instances_search | read | Search workflow instances visible to the delegated user by definition, state or target object type |
| Operations | ops.workflow_tasks.search | ops_workflow_tasks_search | read | Search workflow tasks on cases visible to the delegated user, with assignee and SLA state |
| Company | company.assignments.search | company_assignments_search | read | Search current position assignments (who holds which position, primary flag, FTE, reports-to) |
| Company | company.org_edges.search | company_org_edges_search | read | Search active relations between organization nodes (contains, reports_to, ...) |
| Company | company.org_nodes.search | company_org_nodes_search | read | Search active organization nodes (legal entities, departments, teams, positions) with their type and parent |
| Company | company.people.search | company_people_search | read | Search active people in the company by name or position: display name, job title, primary position and unit only |
| Company | company.profile.get | company_profile_get | read | Read the profile of the delegated user's own company: name, tagline, industry, size, mission, vision and values |
| Omni inbox | omni.channels.list | omni_channels_list | read | List connected omni channels (Zalo, Zalo OA, Facebook pages) in inboxes the delegated user can view, with enabled flag and connection state |
| Omni inbox | omni.conversations.detail | omni_conversations_detail | read | Read the metadata of one omni-channel conversation the delegated user can view: channel, status, assignee, tags, bot state and CRM links |
| Omni inbox | omni.conversations.search | omni_conversations_search | read | Search omni-channel inbox conversations in inboxes the delegated user can view, returning channel, contact display name, status, assignee, unread count and CRM links |
| Omni inbox | omni.inboxes.list | omni_inboxes_list | read | List the omni inboxes the delegated user can view (id, name, default flag), to scope conversation and channel queries |
| Team chat | chat.conversations.search | chat_conversations_search | read | List internal team chat conversations (direct messages and groups) the delegated user is an active member of, to pick a target for chat.messages.send |
| Team chat | chat.messages.send | chat_messages_send | write | Post a text message to an internal team chat conversation the delegated user is a member of |
| OKR | okr.context.get | okr_context_get | read | Load the full OKR context for the delegated user in one call: company profile, who the user is (position, units led), the active cycle (elapsed %, days left) and every visible objective with its key results, progress and latest self-assessed confidence |
| OKR | okr.key_results.checkin | okr_key_results_checkin | write | Check in one key result: record the user's confidence (ON_TRACK, AT_RISK, OFF_TRACK) and an optional blocker note |
| OKR | okr.objectives.draft | okr_objectives_draft | write | Create a DRAFT objective with 2-4 measurable key results in the active cycle, owned by the delegated user |
| OKR | okr.quality.review | okr_quality_review | read | Score the quality of an OKR: flags key results that are unmeasurable, vague, or too many |
| Documents | docs.acknowledgements.pending | docs_acknowledgements_pending | read | List issued documents the verified user still has to acknowledge as read, overdue first |
| Documents | docs.books.list | docs_books_list | read | List the active document books (registers) of the workspace with their numbering pattern, reset cycle and accepted document types |
| Documents | docs.numbers.explain | docs_numbers_explain | read | Explain a document number: how the numbering book's pattern is composed and whether the number belongs to a readable document, was burnt (voided or expired reservation), is unreadable to the caller, or is unused |
| Documents | docs.register.search | docs_register_search | read | Search the issued-document register (decisions, regulations, announcements, official letters) that the verified user may read |
| Documents | docs.templates.search | docs_templates_search | read | Search document template metadata (name, type, status, version) |

Schemas and limits: [minz-contracts.json](minz-contracts.json). Keep totals, units and scope as the source reports them; never infer write permission from a tool name.
