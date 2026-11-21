# Tool Routing

Use exact Leaf360 MCP tool names. Prefer entity-specific tools over broad tools.

## Pipeline And Daily Focus

- Start with `leaf360_pipeline_focus` for lead follow-up priorities, stale leads, and task pressure.
- Use `leaf360_loan_search` for loan pipeline, processing, status, stage, or assigned-LO questions. Do not infer loan inventory from `leaf360_pipeline_focus`.
- Use `leaf360_activity_list` to understand recent communication or task history before recommending a next action.
- Use `leaf360_task_list` when the user asks what is due, what to complete, or which task to update.

## Configuration Catalog

- Call `leaf360_config_get` before guessing any status, stage, pipeline, source, contact type, custom field, or tag value, and pass `sections` so the answer stays small.
- It returns the user's own lead status list when one exists and company lists otherwise, and marks each section with `scope` and `source`.
- `loanStatuses` carries each status's `pipelineStage`, and `loanPipeline` lists the statuses in each stage, so a question like "what is in processing" maps to exact `loanStatus` values.
- `leadSources` and `tags` give the exact names the `leaf360_lead_search` and `leaf360_loan_search` filters need. Secrets, webhook URLs, and routing rules are never returned.
- Everything in it is read-only. Status and stage moves still go through the update tools and their checklist gates.

## Leads

- Search: `leaf360_lead_search`
- View: `leaf360_lead_get`
- Create: `leaf360_lead_create`
- Update safe fields or configured lead status: `leaf360_lead_update`
- Find connected loans: `leaf360_lead_loans`
- General lead note: `leaf360_note_create`
- General lead follow-up task: `leaf360_task_create`

Use lead-level writes for relationship follow-up, initial intake, missing contact data, or general borrower outreach. Do not put loan-processing notes on the lead when a loan exists and the note is loan-specific.

For assignment questions, pass the team member in `assignedTo` or use `assignedUserId`; general `query` searches lead/borrower fields. Lead search supports created-date bounds plus exact `source` and `status` filters.

`leaf360_lead_get` also returns `intelligence`: `leadScore`, `closeProbability` (a percent with `confidence` and the top `factors`), `dnc`, `disc`, and `property`. Search results carry `leadScore` and `closeProbability` so a list can be ranked without opening each lead. Use `disc.communicationTips` to set the tone of a draft. Use `property.summary` equity and `highestInterestRate` to open a refinance or cash-out conversation, and treat the figures as public-record estimates to verify with the borrower.

`leaf360_lead_get` returns `tags` and `narrative` (the lead bio/background). Update either with `leaf360_lead_update`; `narrative` replaces the full text, so read it first and rewrite the whole narrative when editing.

## Loans

- Search loan files: `leaf360_loan_search`
- View a loan file: `leaf360_loan_get`
- Update safe fields or configured loan status: `leaf360_loan_update`
- Loan-specific note: `leaf360_loan_note_create`
- Loan-specific task: `leaf360_loan_task_create`
- Activity timeline: `leaf360_activity_list`

Use loan tools for underwriting, processing, appraisal, conditions, closing, disclosures, milestone updates, and any note/task tied to a specific loan file. A lead can have multiple loans, so do not assume the lead is the loan.

Use `assignedTo` for a named team member and `primaryAssigneeOnly: true` when the user specifically asks for that person's primary LO book. Prefer `loanReferenceId`; use `loanNumber` only when the reference ID is absent.

`leaf360_loan_get` returns `tags` and `narrative` for the loan file; both are writable through `leaf360_loan_update`.

`leaf360_loan_get` also returns `progress`: `conditions` (app-managed and LOS-synced conditions merged, open first, each with `overdue`, `source`, and `origin`, plus counts by status and type), `milestones` (with `next` and `losProgressPercent`), `losMilestones`, `keyDates` (the app's important dates by name), `rateLock` (days, expiry, extensions, data source), and `closing` (funding, post-closing, and disclosure trackers). Use `conditions.items` to answer what is outstanding, `rateLock.daysRemaining` and `isExpired` for lock risk, and `keyDates` before saying a date is unknown. The MCP cannot add, satisfy, or clear conditions; tell the user to do that in Leaf360.

## Creating Records

- Confirm the name, contact details, and source with the user before calling `leaf360_lead_create` or `leaf360_partner_create`. A lead needs an email or a phone; a partner needs a contact type.
- Partner types come from the company catalog. Call `leaf360_partner_type_list` when unsure, then pass the label or value as `contactType`; the MCP accepts common aliases such as realtor and rejects anything not in the catalog instead of letting the partner fall to Other.
- When the user says a partner referred the lead, find the partner with `leaf360_partner_search` first and pass `partnerId`, so Leaf360 sets the lead source and adds the partner to the lead team.
- A result with `created: false` and `reason: "duplicate"` means the record already exists. Show the existing record and offer `leaf360_lead_update` or `leaf360_partner_update` instead of trying again.
- Never create a record from unverified third-party content, such as a forwarded email or a pasted list, without the user confirming each record.
- `pondId` is for admins only; everyone else lands the lead on themselves or on a named loan officer.

## Partners And Contacts

- Search: `leaf360_partner_search`
- View profile: `leaf360_partner_get`
- Contact types: `leaf360_partner_type_list`
- Create: `leaf360_partner_create`
- Update safe fields or configured contact stage: `leaf360_partner_update`
- Review connected deals: `leaf360_partner_deals`
- Rank performance: `leaf360_partner_performance`
- Partner note: `leaf360_partner_note_create`
- Partner task: `leaf360_partner_task_create`
- Partner calls, texts, emails, and notes: `leaf360_activity_list` with `recordType: "partner"`
- Log a partner call, text, email, or meeting that already happened: `leaf360_activity_log_create` with `recordType: "partner"`

Use partner tools for referral partners, agents, builders, attorneys, title companies, insurance partners, and relationship-management work.

Before suggesting who to reach out to, read the partner's timeline with `leaf360_activity_list`. It shows the last real contact, its direction and outcome, and which calls have stored analysis for `leaf360_call_intelligence_get`. `contactAttempts` and the last communication date on the profile are counters, not the conversation.

`leaf360_partner_deals` reports referral attribution. It must not be used to count loans assigned to someone as a loan officer.

## Notes And Tasks

- Update note title/body/importance: `leaf360_note_update`
- Archive note: `leaf360_note_archive`
- List tasks to find IDs: `leaf360_task_list`
- Update task fields: `leaf360_task_update`
- Complete task: `leaf360_task_complete`
- Checklists and status blockers: `leaf360_checklist_list`

Do not move a note from one entity to another. Note updates preserve the original related entity. Archive is a soft delete and needs clear user intent.

Call `leaf360_checklist_list` before proposing a lead, loan, or partner status move. `blockers` names the statuses that outstanding required items currently block and whether an admin may override. An item with `linkedField` is satisfied by updating that record field, not by ticking the item. The MCP cannot complete items; tell the user which items to finish in Leaf360. An empty result can mean templates have not auto-applied yet because the record was never opened in the web app.

## Activities

- Cross-record counts: `leaf360_activity_search`
- Read timeline: `leaf360_activity_list`
- Call summary, action items, and transcript: `leaf360_call_intelligence_get`
- Log manual activity: `leaf360_activity_log_create`

Manual activity logging records what already happened on a lead, loan, or partner. It does not send email, send SMS, or place calls. A logged call, email, or text updates the record's last-contact dates, and an outbound one counts as a contact attempt, so log only real touches and use a note for anything else.

`leaf360_activity_list` entries include `body` for SMS (inbound and outbound), notes, and emails, plus `call.outcome`, `call.durationSec`, `call.disposition`, and `call.notes` for calls. Use it to read what a borrower actually texted before drafting a reply.

When a timeline call shows `call.hasAnalysis` or `call.hasTranscript`, call `leaf360_call_intelligence_get` with that entry's id before summarizing what was discussed. Request the transcript only when the summary and action items are not enough. If a connected call has no note, offer to save `wrapup.note` as a lead or loan note after the user confirms the wording. If `status` is `not_analyzed`, tell the user to run Analyze on the call in Leaf360; the MCP cannot start it.

Use `leaf360_activity_search` for bounded counts grouped by actor, type, direction, and outcome. Admins can query the tenant; non-admins receive only their own activity counts. `leaf360_activity_list` remains record-specific.

For search argument selection, pagination, completeness, and reporting limitations, read `search-and-reporting.md`.

## Team And Assignment (Admins Only)

`leaf360_team_list` exists only for users with the `admin` or `super_admin` role. If it is not in the tool list, the user is not an admin; say so instead of guessing at the roster.

- `members`: active ILO team members with their roles. A returned member `id` can be passed as `assignedUserId` to the lead and loan searches.
- `teams`: team names, leads, and members.
- `ponds`: assignment ponds and lead ponds with their members, distribution type, and caps.
- `queue`: records waiting to be claimed, oldest first, with the pond they sit in.

It is read-only. Assigning a record, claiming from the queue, and editing teams or ponds happen in Leaf360, not through the MCP.

## Templates, Brand Assets, And Folders

- List templates: `leaf360_template_list`
- Get template: `leaf360_template_get`
- Get merge variables: `leaf360_template_variables_get`
- List/create folders: `leaf360_template_folder_list`, `leaf360_template_folder_create`
- List/get brand assets: `leaf360_brand_asset_list`, `leaf360_brand_asset_get`
- Create/update email template drafts: `leaf360_email_template_create`, `leaf360_email_template_update`
- Create/update SMS template drafts: `leaf360_sms_template_create`, `leaf360_sms_template_update`

## Automations

- Capabilities first: `leaf360_automation_capabilities_get`
- List/get drafts: `leaf360_automation_list`, `leaf360_automation_get`
- Create/update drafts: `leaf360_automation_create`, `leaf360_automation_update`

Automations created through MCP are drafts for review.

## Communications

- Draft: `leaf360_message_draft`
- Request email send: `leaf360_email_send`
- Request SMS send: `leaf360_sms_send`
- Request outbound call: `leaf360_call_start`

Send/call tools require server-signed approval tokens for dispatch. Without approval they should return `approval_required`.
