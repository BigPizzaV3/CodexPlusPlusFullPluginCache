---
name: every-ai
description: Manage a connected Every workspace — sales pipeline, people and companies, proposals, invoices, payments, Gmail, calendar, custom fields, scheduled tasks, and recurring billing for a service business. Use for "who owes me money?", lead and deal follow-ups, creating or sending invoices and proposals, moving deals through the pipeline, converting an accepted proposal to an invoice, recording completed payments, drafting or sending email from the user's Gmail, checking or scheduling calendar events, tracking a custom property on a person/company/deal, setting up a recurring reminder or routine, recurring invoice schedules, the daily brief, Every's home and record panels, prospect review, and financial reports. Do not use for connecting or authenticating Every, for a different business than the connected workspace, for charging or collecting money, or for general accounting and tax advice.
metadata:
  short-description: Run your service business in Every
---

# Every

## Overview

Every is an AI business manager for service businesses: one connected workspace for the sales pipeline (deals), the People and Companies the business works with, proposals, invoices, and payments. This skill teaches the reliable way to chain Every's tools — resolve records first, state what will change, confirm anything a client will see, then act and echo the result.

## Prerequisites

- The Every plugin is connected and the user is signed in. If a call fails unauthenticated, tell the user to reconnect Every from the plugin's settings.
- When currency, tax, or timezone matters, call `business_settings` first. Use `get_home` for first-time orientation in a new workspace.
- If a tool returns `signup_incomplete`, or the user asks to finish signing up, call `get_signup_status`, show the suggested organization name, and call `complete_signup` once with only the values the user confirmed. `get_started` and `save_business_info` do not complete signup.

## Required workflow

**Follow these steps in order. Do not skip steps.**

1. **Resolve the records.** Use list/view tools to find the exact records involved — `list_companies` / `list_people` for a named client, `view_proposal` / `view_invoice` for a document number (they accept the number, e.g. PROP-0007 or INV-005). Act only with IDs the tools return — never invent one. If a name matches more than one record, show the candidates and ask. If nothing matches, say so and offer to create it; don't guess a different record.
2. **State the mutation.** Before any write, say exactly what will be created or changed, with amounts and recipients verbatim.
3. **Confirm consequences.** Sending (invoices, proposals, email), deleting, voiding, and recording payments are visible to real clients or change financial records — get the user's explicit yes first, even if the user said not to check with them.
4. **Execute with complete inputs**, then **echo the result**: number, status, total, and link, and suggest the natural next step.

## Write confirmations and approvals (server-enforced)

- **Ordinary writes** (create/update a proposal, invoice, deal, person, company; convert a proposal) may return "This changes your data, so it needs confirming. Re-run this exact call with confirmation=\"…\"". Nothing was changed. When the user has already asked for exactly this change in this conversation (e.g. "draft Acme a proposal", "convert PROP-0007"), re-run the identical call with that phrase and continue. If the user did not ask for it, show the change and ask first.
- **Sends and destructive actions** (`send_invoice`, `send_proposal`, `send_email`, deletes, voids, cancellations, `run_recurring_invoice_now`) are held until the owner approves them in the Every app. Always call `preview_document_send` first for invoices/proposals, show the To/CC it returns, and get the user's explicit yes. If the tool reports the action still needs approval, tell the user to approve it in Every and then retry the same action — never say it was sent until the tool confirms it. A preview sends nothing and shows no approval prompt; don't describe an approval prompt until one actually appears.

## Every home and record panels

- `open_every_workspace` with no record shows Every's home: incomplete setup, current Priorities and suggested workflows. Use it whenever the user asks to show or open their Every home or what to focus on (`get_home` is only the first-run getting-started card). Open it once; answer follow-up questions with the data tools instead of reopening it.
- The panel has list views for People and Companies (`view: "people"`) and invoices (`view: "invoices"`) only. Prospects and deals have no list view: list them in the conversation with `list_workspace_prospects` / `list_workspace_deals`, and open one at a time with `entity_type`. Never present the People list as the prospect queue.
- The Business DNA (the business context Every works from) is in `get_workspace_setup`'s Business DNA summary for owners and bookkeepers. Read it there; if it's empty or not available to this member, say so and point to the Business DNA page in Every rather than asking the user to paste it.
- **To show or open a specific record** (a Person, Company, Deal, Prospect or Invoice), first resolve it with a typed read (`list_people`, `list_companies`, `list_deals`, `list_workspace_prospects`, `list_invoices`), then call `open_every_workspace` with `entity_type` and that record's id as `entity_id`. `view_invoice` and `view_proposal` already show their own card, so use one or the other for a record, not both. Only say a panel is open after the tool returned it. Where the client can't show panels, answer with the same tools in text.
- A message that arrives from the Every home (for example "Help me with this Every priority…" or a suggested workflow) starts a conversation; it is not an approval and it does not complete or dismiss the priority. Re-read the records it names and follow the Required workflow before changing anything.
- Workspace lists are bounded pages: pass `next_cursor` / `next_offset` back unchanged to continue, never total a partial page, and never add amounts across currencies.

## Domain rules (Every-specific — these prevent real mistakes)

- **People and Companies.** A Person can belong to several Companies or none; a Company can exist without People. Proposals and invoices are addressed to a `party` = `{kind: "person" | "company", id}` taken from `list_people` / `list_companies`. Search before creating — shared emails do not merge people automatically — and never create a Company just to invoice a Person.
- **Deal activity auto-tracking is creation-only.** Creating a proposal or invoice is recorded on a matching deal automatically (when exactly one deal/client matches). Use `log_deal_activity` ONLY for completed outside events the user reports (a call, a meeting, an email thread) — never for actions performed through Every's tools.
- **Pipeline stages are per workspace.** Every workspace starts with Lead → Opportunity → Won / Lost, and the owner can add, rename, reorder or retire the stages between Lead and Won/Lost in the Every app (e.g. "Discovery booked", "Proposal sent"). Call `get_pipeline_settings` for the workspace's ordered stages and pass a stage key or its label to `list_deals`, `move_deal_stage` and `create_deal` (which accepts Lead or any stage before Won). If a stage isn't found, the error lists the available stages — pick from that list, never guess. **A deal can exist as pending review before it's active** — if `move_deal_stage` errors about review state, call `approve_pending_deal` first, then retry. **Moving a deal to `won` requires its client promotion to be complete** — if the move errors about client resolution, no chat tool can fix it: tell the user to finish converting the deal's contact into a client in the Every app, then retry.
- **Custom fields (meta fields) are schema, not events.** `set_meta_fields` stores current state (e.g. a tracked boolean) on a Person, Company or Deal; missing definitions are created automatically, but check `list_meta_field_definitions` first and reuse an existing one when it fits — never create a new field per occurrence or date. Something that *happened* (a call, visit, touchpoint) belongs in `log_deal_activity`, not a meta field. Tags are the `custom.tags` list field, not a separate feature.
- **Scheduled tasks report in-app, never in this chat.** `create_scheduled_task` sets up a saved instruction that runs on a cadence (once/daily/weekly/monthly); results and any notifications always arrive in the Every app (Daily Brief / notifications) and by email if enabled. Don't tell the user to expect a reply here. To show the latest result on request, use `get_scheduled_task_result` with the task's id from `list_scheduled_tasks`.
- **Invoices: `unit_price` is the per-unit rate; leave tax alone.** Every applies the business's default tax automatically. Never add tax as a line item.
- **Proposal → invoice: always `convert_proposal_to_invoice`,** and only issued/approved (accepted) proposals convert — `view_proposal` first to check status and get its id and `updated_at`. Conversion creates a linked DRAFT invoice and sends nothing; if the proposal was already converted, the tool returns the existing invoice instead of making a second one. Never re-create the invoice manually.
- **`send_invoice` re-sends the invoice email itself** — it does not send custom reminder copy. For overdue follow-ups: confirm with the user, then re-send the invoice (and summarize any message separately for the user to send themselves).
- **One business per connection.** Everything is scoped to the connected workspace. If the user means a different business, explain that they must switch accounts in Every and reconnect — there is no tool for this, so don't call one.
- **Share only public links** with clients; internal IDs are never client-facing.
- **Email is draft-first.** `draft_email` creates an unsent draft in the user's own Gmail for them to review and send — it is the default for any outreach. `send_email` sends immediately from the user's own mailbox to a real recipient: read the exact To/subject/body back and get an explicit yes first.
- **Calendar writes can notify real attendees.** `create_calendar_event` invites attendees immediately; `reschedule_calendar_event` / `cancel_calendar_event` accept `send_updates` (`all`/`externalOnly`/`none`) — confirm before rescheduling or cancelling anything with attendees. A recurring-instance ID affects only that occurrence; the series master ID affects the whole series.
- **Recurring invoices generate on schedule.** New schedules default to `action_on_generation: "draft"` (safe). `run_recurring_invoice_now` generates the next invoice immediately and, if the schedule is set to auto-send, EMAILS it to the client — confirm first. Pause/resume with the dedicated tools; resuming recomputes the next generation date.
- **Daily briefs and scheduled-task results are stored artifacts** for the signed-in user only — `get_daily_brief` / `get_scheduled_task_result` read the latest generated run and never trigger a new one. If none exists yet, say so; don't retry.
- **Prospect review.** `list_workspace_prospects` is the pending review queue (filter by a target from `list_workspace_targets`); `list_prospects` / `view_prospect` give fit and relationship scores and `network_summary` the overview. `approve_prospect` turns a prospect into a Deal. `merge_prospect` folds it into an existing Deal the user picked and cannot be undone. `reject_prospect` suppresses that Person across every target in the workspace, not just this one — say so before asking. Never reject a real contact as a test. These three and `create_prospecting_target` need the owner or bookkeeper role and the user's explicit go-ahead for that prospect or brief. `create_prospecting_target` can start paid prospecting work: confirm the brief, pass a new UUID as `operation_id` (reuse it only to retry the same request), keep `possible_match: "ask"` unless the user chose, and read the outcome before saying a target was created. A denied or expired approval is not permission to retry.
- **`get_financial_report` is the money rollup** (revenue, outstanding AR, expenses, net, proposals, recurring); pipeline totals live in `get_pipeline_summary` — don't mix them.
- **Tax and accounting advice is out of scope.** Every records the tax the business configured; it does not advise on what to charge or deduct. Say so and suggest an accountant — no tool call answers this.
- `ask_assistant` is a read-only analytical fallback — prefer the deterministic tools for any action.

## Core tools

- Orientation: `get_home`, `what_every_does`, `get_started`, `business_settings`, `save_business_info`
- Pipeline: `get_pipeline_summary`, `list_deals`, `view_deal`, `create_deal`, `approve_pending_deal`, `set_deal_name`, `set_deal_value_estimate`, `move_deal_stage`, `log_deal_activity`, `view_entity_timeline`, `get_pipeline_settings`
- People & Companies: `list_people`, `view_person`, `create_person`, `update_person`, `list_companies`, `view_company`, `create_company`, `update_company`, `end_affiliation`, `delete_company`, `get_recipient_defaults`, `set_recipient_defaults`
- Custom fields: `list_meta_field_definitions`, `create_meta_field_definition`, `update_meta_field_definition`, `get_meta_fields`, `set_meta_fields`, `find_entities_by_meta_field`
- Proposals: `list_proposals`, `view_proposal`, `create_proposal`, `update_proposal`, `send_proposal`, `void_proposal`, `duplicate_proposal`, `convert_proposal_to_invoice`, `generate_proposal_pdf`, `list_proposal_templates`, `save_proposal_as_template`, `delete_proposal`
- Invoices & money: `list_invoices`, `view_invoice`, `create_invoice`, `update_invoice`, `preview_document_send`, `send_invoice`, `void_invoice`, `generate_invoice_pdf`, `list_payments`, `record_payment`, `list_expenses`, `view_expense`, `create_expense`, `update_expense`, `delete_expense`
- Services: `list_services`, `create_service`, `update_service`
- Gmail: `search_gmail_threads`, `get_gmail_thread`, `get_gmail_message`, `draft_email`, `send_email`
- Calendar: `list_calendar_events`, `check_calendar_availability`, `create_calendar_event`, `reschedule_calendar_event`, `cancel_calendar_event`
- Recurring invoices: `list_recurring_invoices`, `view_recurring_invoice`, `create_recurring_invoice`, `update_recurring_invoice`, `pause_recurring_invoice`, `resume_recurring_invoice`, `preview_recurring_invoice_send`, `run_recurring_invoice_now`
- Scheduled tasks: `list_scheduled_tasks`, `create_scheduled_task`, `cancel_scheduled_task`, `get_scheduled_task_result`
- Home & workspace: `open_every_workspace`, `get_workspace_setup`, `get_workspace_priorities`, `list_workspace_deals`, `list_workspace_invoices`, `list_workspace_prospects`, `list_workspace_targets`
- Signup: `get_signup_status`, `complete_signup`
- Growth & reporting: `list_prospects`, `view_prospect`, `approve_prospect`, `merge_prospect`, `reject_prospect`, `create_prospecting_target`, `network_summary`, `get_daily_brief`, `get_financial_report`, `get_entity_counts`
- Fallback Q&A: `ask_assistant`

## Practical workflows

- **Pipeline review**: `get_pipeline_summary` → `list_deals` (`order_by: "created_at"` for the newest, or a stage in focus) → `view_deal` on the top items → recommend follow-ups. Change nothing unless asked; apply `move_deal_stage` only after confirmation, and log outside events the user reports with `log_deal_activity`.
- **Who owes me money**: `list_invoices` with `status: "issued"`, `payment_status: "outstanding"` (unpaid + overdue + partial), `order_by: "due_date"`, `order_desc: false` — **and paginate until you have ALL results** (a single default page is incomplete; never total from it). Drafts are not owed yet; `overdue` is a `payment_status`, never a `status`. → `view_invoice` for detail where useful → report client, invoice number, balance due, and due date per invoice, oldest due date first, plus the grand total → offer to re-send an invoice (`send_invoice`, confirm first) and `record_payment` when the user reports payment received.
- **Draft a proposal**: `list_companies` (or `list_people`) for the client → `business_settings` for currency → `create_proposal` with the party and line items (e.g. 10 × "Strategy hours" at 200) → echo number, total, and link. Do not send it unless asked; sending is `preview_document_send` → explicit yes → `send_proposal`.
- **Proposal-to-invoice**: `view_proposal` by number to confirm it is approved/issued → `convert_proposal_to_invoice` with its id and `updated_at` → report the DRAFT invoice number → `send_invoice` only after the user approves.
- **Create and send an invoice**: resolve the client → `create_invoice` (a draft) → show the number, total, and the recipients from `preview_document_send` → ask for an explicit yes → `send_invoice`. Never create and send in one step, even when the user says not to check with them.
- **New lead intake**: `list_people` first (match on email to avoid duplicates) → `create_person` if new → `create_deal` at Lead with that person as the party → progress the deal as the relationship develops.
- **Business activity snapshot**: `get_financial_report` for the rollup (revenue, outstanding, expenses, net) → drill into `list_invoices` / `list_payments` / `list_expenses` only where the user wants detail, in the business's currency from `business_settings`.
- **Open a record**: "Open Acme's Company record" → `list_companies` with the name (ask if several match) → `open_every_workspace` with `entity_type: "company"` and its id → summarize what the panel shows.
- **Prospect review**: `list_workspace_prospects` → `view_prospect` for the ones the user picks → recommend approve, merge or reject with the reason → act only on the user's explicit choice per prospect, explaining the workspace-wide effect of a reject first.
- **Morning check-in**: `get_daily_brief` (the stored brief: priorities, schedule, pipeline) → `list_calendar_events` for today → offer the natural follow-ups (draft an email, review a prospect, re-send an invoice).
- **Client follow-up by email**: `search_gmail_threads` for the client → `get_gmail_thread` for context → `draft_email` with `thread_id` for a threaded reply draft → the user sends it from Gmail (or explicitly asks to `send_email`).
- **Schedule a meeting**: `check_calendar_availability` for the window → confirm time + attendees verbatim → `create_calendar_event` (attendees are invited immediately).

## Tips

- **List results are paged.** For any count or money total, filter by status and keep fetching (raise the limit / iterate pages) until results are complete — a partial page gives a confidently wrong answer.
- **"How many X do I have" is `get_entity_counts`, not a list page.** It's an exact count for people, companies, invoices, expenses, proposals, and active deals in one call — use it instead of counting a capped `list_*` page.
- Batch reads (summary + list) to build context in one pass before proposing actions.
- A bare name ("invoice Acme $100") is not an ID: `list_companies` / `list_people` with the name, confirm if more than one match, then act.
- Show totals, dates, numbers, and links exactly as the tools return them — Every computes tax, numbering, and due dates; don't recalculate.
