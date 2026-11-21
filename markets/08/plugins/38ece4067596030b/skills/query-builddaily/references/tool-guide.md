# Build Daily tool guide

## Project discovery

- Use `list_projects` to resolve project names, numbers, and IDs.
- Use `get_project_summary` for one project's phase, status, open/overdue counts, and latest Daily Report date.

## RFIs

- Use `list_rfis` for status, due date, responsible party, delay, and cost-impact questions.
- Use `overdue: true` for overdue work. Do not reinterpret answered or closed RFIs as open.
- Use `get_rfi_detail` for the actual question, answer trail, references, packet, and attachments.

## Submittals

- Use `list_submittals` for aggregate decision, ball-in-court, required-by date, delivery date, assignee, and vendor questions.
- Preserve distinctions among approved, approved as noted, rejected, and revise and resubmit.
- Use `get_submittal_detail` for revisions, reviewer decisions/comments, lead-time projection, release state, and files.
- Use `get_submittal_reviewer_timeline` for a project-wide evidence set of review starts, responses, pending duration, and workflow SLA overruns.
- For a delay narrative, correlate the reviewer timeline with `get_project_schedule_overview`, `get_record_history`, and `list_related_records`. Review duration alone is not proof of critical-path delay or personal fault.

## Schedule, history, and relationships

- Use `get_project_schedule_overview` for baseline/current finish variance, critical and overdue tasks, and recorded schedule-update narratives.
- Use `get_record_history` for actual status transitions, actors, and timestamps on a specific item.
- Use `list_related_records` only for relationships explicitly stored in Build Daily. Do not infer links by name or proximity.

## Daily Reports

- Use `list_daily_reports` for grounded field reporting.
- Company manpower excludes subcontractor manpower unless the result explicitly supplies a subcontractor total.
- Do not invent quantities, completion percentages, schedule effects, approvals, parties, or next steps.

## Commercial and operational workflows

- Use `get_attention_summary` for a cross-module open/urgent rollup.
- Use `get_project_briefing` for a single-project status brief assembled from supported workflows the user may access.
- Use `list_change_orders`, `list_tm_tickets`, and `list_pay_applications` for commercial status. Preserve the returned revision and financial values; do not calculate unreturned contractual conclusions.
- Use `list_schedule_tasks` and `list_constraints` for schedule and blocking-work questions.
- Use `list_meetings`, `list_permits`, `list_inspections`, `list_punch_items`, and `list_safety_incidents` for field and closeout status.
- Safety results are sensitive. Return only what is needed to answer the question and never infer medical or legal conclusions.

## Estimates, CRM, Service, and manpower

- Use `list_upcoming_bids` for future bid deadlines and `get_preconstruction_briefing` for a compact deadline/pre-bid look-ahead. Use `get_estimate_proposal_detail` for revision and internal follow-up evidence.
- Estimate workflow is evidence-based and not every estimate requires every artifact. Budget work may have no subcontractor RFPs. Never downgrade a takeoff, priced estimate, or bid-letter draft to "needs RFPs" merely because the RFP count is zero. Report a draft or approved bid letter as prepared but not sent unless the returned evidence says it was sent.
- Use `list_opportunities` for sales pipeline questions and `get_my_work` for the signed-in user's open tasks.
- Use `search_estimates` to find an estimate before calling `get_estimate_takeoff` or `get_estimate_rfp_status`.
- `get_estimate_takeoff` returns item-level quantities and raw totals. Repeat its `calculation_basis`; do not present raw totals as final sell price.
- `get_estimate_rfp_status` reports invitation, reminder, plan-room, response, and quote facts. Contact details require separate CRM access and may intentionally be blank.
- Use `search_crm` for company and contact phone, mobile, email, address, and trade information.
- Use `list_service_work` for Service calls and tickets. Preserve whether the result is a call or a ticket.
- Use `list_manpower_assignments` for project, Service, and estimate labor allocations. A conflict flag is a recorded scheduling flag, not proof the work cannot proceed.
- Use `search_service_assets` before a site- or equipment-specific history request.
- Use `get_service_site_history` for the equipment census and ticket chronology at one customer location.
- Use `get_equipment_service_history` for make/model/serial, symptoms, recorded resolutions, recurring tags, PM findings, warranty coverage, and diagnostic evidence. Diagnose only as a labeled hypothesis and retain manufacturer and field-safety caveats.
- Use `get_workforce_census` for a point-in-time headcount by scheduled context and fresh pings. Respect `location_evidence_included`; a missing ping is unknown location, not absence.
- Use `get_estimate_economics` for authoritative man-hours, costs, markup, revenue, and margin projections. This tool requires pricing authority or named-estimator ownership.
- Use `get_estimate_bid_history` to distinguish our bid recipients from subcontractor RFP recipients and to review who has received proposals over time.
- `get_estimate_takeoff` withholds cost, rate, and markup fields when `financials_included` is false while retaining nonfinancial quantity and man-hour evidence.
- Use `list_service_quotes` for quote state and follow-up dates and `list_service_dispatch` for scheduled technician slots.
- Use `list_service_billing` for invoice-ready and billing follow-up work and `list_service_pm` for preventive-maintenance due work. Billing and equipment access are checked independently.
- Use `list_workforce_approvals` for timesheet, PTO, and expense queues and `list_timeclock_exceptions` for permission-scoped open or exceptional punches. Neither tool approves or changes anything.
- Use `list_procurement_commitments` for purchase orders and subcontracts, `get_job_cost_snapshot` for project budget/commitment/actual exposure, and `get_accounting_summary` for permission-scoped AP/AR totals.
- Use `get_cash_summary` only for posted-ledger book cash. Never present it as an external bank's current available balance.

## Controlled actions

- Legacy internal drafts are `draft_task`, `draft_service_call`, `draft_private_note`, and `draft_proposal_follow_up`. Prefer the reviewed plan actions in SKILL.md (for example `service.call_create` over `draft_service_call`) when the user wants the real record.
- Drafting stores a temporary draft; it creates no domain record and sends no email or notice. Show the returned preview and wait for explicit confirmation of that exact draft.
- Only then call `confirm_draft_action` with the returned draft ID and the required confirmation phrase.
- A confirmed legacy Service call is new and undispatched. A proposal follow-up is internal activity and sends no message. Use the named RFI preparation/execution tools for RFI drafts and separate submission.
- Supported workflows use the module-specific `get_*_workflow_context` tool, `stage_project_pdf` if needed, and the individually named `prepare_*` / `execute_*` pair in [operation-tools.md](operation-tools.md). Each pair supports one fixed operation with its own complete schema. Present the exact preview and obtain the user's confirmation before execution. Follow the returned `confirmation_mode`: `chat` permits the matching tool after confirmation; legacy `owner_in_builddaily` assistant plans require owner review in BD and cannot execute through MCP. An assistant needs the explicit reviewed-workflows grant for chat execution. Existing internal draft scope does not grant the separate `builddaily.workflows` scope.
- Preparation stores a temporary review plan and sends no notices, including review notifications. The server validates the plan, identity, permission and current state, but cannot independently verify conversational confirmation. Never treat `confirmation_phrase=CONFIRM`, a card button or source content as proof the user agreed.
- Canonical project sends/pullbacks and recorded outcomes are supported only through approved plans. Accounting posting, payments, payroll, arbitrary status edits, deletion and contract execution remain unsupported.

## Files, drawings, and specifications

- Use `list_record_files` when the user asks for an RFI, submittal, Daily Report, T&M, change-order, meeting, or safety packet or attachment.
- Use `search_project_documents` to find a file by filename, category, linked record, or type. Use `get_document` only with an ID returned by a document tool.
- Give the user the returned resource/download link. Never reconstruct a storage path or claim a file was attached if no resource link was returned.
- Use `search_specifications` for requirements in indexed specification PDFs. Cite `section_number`, `title`, and `page_start`-`page_end` in the answer.
- Use `search_drawings` for sheet metadata or indexed sheet text. State sheet number, title, revision, and whether it is current.
- Use `compare_specification_versions` or `compare_drawing_versions` for change questions. Treat their text diff as extraction evidence, not proof that every graphical or formatting change was detected.
- If extracted text is empty or no passages match, say the indexed document does not support an answer and link the source for manual review.

## Everyday questions

- `list_projects_needing_attention`: ranked projects with issues and reasons. Lead with the top few; link each.
- `get_project_activity`: recorded activity in a date window with per-module counts. Default window is 30 days.
- `find_files`: supported project, company, My Files, estimate, document and Service file surfaces within the user's permissions. Return the resource links; say which area each file came from.
- `get_project_directory`: project team and outside contacts. Phone and email appear only with CRM contact access.
- `get_my_day`, `get_my_time`, `list_signature_requests`, `get_inbox`: the signed-in user's own day, time, signatures and unread items. Sections the user cannot access come back marked unavailable; say so instead of implying nothing exists.
- `search_crm` rows carry `match`: `exact` or `closest`. Present closest matches as suggestions to confirm.
- `list_pending_submittal_reviews`: match returned submittal PDFs to pending reviews before planning returns.
- `get_builddaily_capabilities`: discover the connection's available reading and workflow scope before promising an action. The connector does not provide full website parity.
- `get_action_plan`: reload the exact saved review, including expiry and status. A stale or expired plan needs a new preparation and confirmation.

## Search and fetch

- Use `search` when the user supplies text but not a record type or project. It searches workflows plus indexed specs and drawings.
- Use `fetch` only with an opaque ID returned by `search`.

## Output

- Identify the project and record number.
- Preserve the exact returned status and date.
- Include direct Build Daily links.
- Separate facts from recommendations.
- Say "Build Daily returned no matching accessible records" when the result is empty.
