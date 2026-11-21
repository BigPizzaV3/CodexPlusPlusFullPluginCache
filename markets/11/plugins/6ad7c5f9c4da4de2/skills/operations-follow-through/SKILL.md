---
name: operations-follow-through
description: Turn restaurant analysis into explicitly confirmed native Team tasks and track execution, using Central Kitchen demand, batches and deliveries when relevant.
---

## State capability limits precisely

The plugin cannot edit, post, settle or mark Finance/Catering invoices paid, rewrite P&L, correct stock or recipes, send customer messages, make purchases or book travel. This remains true even when the user has evidence and native permissions. Offer analysis or the authorized native HoreX workflow, never promise that this plugin can perform those changes. Unsupported mutation requests require no business-data call. Supported Team tasks and advertising settings use only their dedicated proposal and native approval flows; they do not grant general editing or payment capabilities.

## Execute HoreX calls sequentially

For one connected HoreX account, wait for each call to finish before starting the next. Keep the result, source and billing status of each call separately. A busy/concurrency error applies only to the rejected call; it does not invalidate another successful result. Reuse successful results. Retry only the failed read once after the active call finishes, within the user's remaining successful-read budget. If no budget remains, report the partial result and ask before another charged read. Never broaden access or repeat a proposal/provider write to recover a read error.

# From evidence to follow-through

1. Establish the concrete problem, location, dates, evidence coverage and goal. Preserve quality and stockout constraints. Observations and suspected causes are different.
2. Check `list_team_tasks` for existing work. Read `get_team_task` to follow an existing task and its current assignees, deadline, comments and activity. Private tasks, project roles, active membership and feature permissions apply.
3. Use `get_team_workspace` to resolve the exact eligible assignee and optional existing project. Search a person by name when the directory is partial. A project observer cannot be assigned. Never add project members or select an invented ID.
4. When the user wants action, call `prepare_team_task` with one concrete task, exact assignee, due date, acceptance criteria, evidence-based baseline and optional branch/project. State any causal uncertainty in the description. Do not put unrelated private information into a task that will be shared with its audience.
5. This returns an immutable, expiring proposal. Show the returned review link and summarize the work, assignee, deadline, audience and expected verification. No task exists yet and no assignee has been notified. Only the proposing user can confirm the exact proposal in the authenticated HoreX page. The server rechecks native permissions, branch context, project role and assignee eligibility, then creates one native task atomically. Retries do not duplicate it. There is no model-accessible commit method.
6. Track the resulting native task via `get_team_task`, including comments and activity. Request fresh operational data for the agreed baseline/follow-up period and evaluate the acceptance criteria. Done means staff execution; it does not establish lower food cost, profit or causation. Keep missing evidence explicit. No autonomous task edits, stock posting, purchasing, production completion or customer messages.

# Central Kitchen evidence

Resolve `get_central_kitchen_workspace` first, then use the selected kitchen/date with `get_central_kitchen_day`. Orders use the selected delivery day; outstanding deliveries and unfinished older production are explicitly included separately. Read one `get_central_kitchen_item` for demand and allocations by branch, stock availability, production batches, output reconciliation, recipe and current estimated cost. Exact `get_central_kitchen_order` and `get_central_kitchen_delivery` preserve the original document and quantities.

Branch users can see their permitted orders/deliveries. Internal production and costs require planning/cooking permission and supplying-kitchen access. A measured output shortfall is not automatically physical waste. Missing cost is unknown; current estimate is not frozen historical actual cost. Central Kitchen production and Stock Batch Breakdowns are different accounting workflows. Never claim that these reads implement FIFO lot accounting or the separate breakdown module. Preserve units, loaded-row limits and source links verbatim.

Business data reads cost 1 AI Credit on success; failed requests are free. Proposal preparation also reads permissions/entities and uses the existing 1-credit request contract. Reviewing/confirming in HoreX and normal Team writes add no plugin read charge. Re-read only when needed; no background polling or subscription is started by this workflow.

After the user confirms in HoreX, call `get_team_task_proposal` with the returned proposal_id. Only committed status establishes execution. Read its task_id with get_team_task; pending, expired, blocked or dismissed does not mean success. Do not prepare a second proposal merely to check confirmation.

# Change an existing task

Read `get_team_task` first and use its exact task_id and current version with `prepare_team_task_action`. Only prepare changes the user requested. Action `update` accepts supplied title, description, status (`todo`, `in_progress`, `in_review`, `done`), priority, due_date or assignee_ids. Omitted fields stay as they are; `clear_due_date=true` removes the deadline, and `assignee_ids=[]` removes all assignees. Resolve new assignees with get_team_workspace for the task's existing project. Preserve acceptance criteria/baseline when editing description.

Action `comment` requires body; `follow` requires following and changes only the current user's following preference; `archive` requires archived (false restores). Supply only fields for that action. Each proposal targets one task and version. No project moves, project membership edits, private audience edits, file uploads or bulk mutations are supported. Native Team edit, comment and audience rules apply separately; read access never implies edit access.

Summarize the exact before/after changes or comment and the existing audience, then give the returned HoreX review link. Preparation changes no task and sends no notification. Only the proposing user can apply the reviewed proposal in HoreX; changes and native notifications commit atomically. If the version changed, read the task again and prepare a fresh proposal for review; never overwrite the newer task silently. Check get_team_task_proposal after approval and use its exact task_id. Repeated confirmation cannot duplicate comments or notifications. Use list_team_tasks status/tab/assignee/project filters and pagination to track execution; totals apply to those filters, not every task in the organization.

# Investigate stop-list availability

Use `get_stop_list_history` with an explicit Dubai date_from/date_to (at most 93 days), optional branch_id, dish search, employee search, current status and page. One row is an uninterrupted dish/location stop overlapping the period, with start/removal, staff, reason and full duration. Totals cover all matching periods before the fixed 50-row page; follow has_more before claiming a complete review. Use the returned source link to the exact filtered report.

Active/removed means current state; it is not the state at the selected end date. Durations are full stop durations, not clipped to the selected dates. Native branch permissions and global dish stops follow the same Operations Audit rules. History includes recording and backfilled active stops; previously removed stops and missing legacy staff cannot be reconstructed. Do not call unknown staff dishonest, infer misconduct from a stop alone or label stop duration as lost revenue. Compare permitted sales/stock evidence separately and prepare a Team follow-up only when requested. This tool cannot change availability.
