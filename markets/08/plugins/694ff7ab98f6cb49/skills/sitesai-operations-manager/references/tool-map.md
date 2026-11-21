# Public SitesAI tool map

This map covers the public connection at https://app.sitesai.net/api/mcp/mcp. Tools below are
grouped by user goal; availability and schemas must still be checked at runtime. Do not switch
profiles or use another connection to bypass a missing tool or permission.

## Orient and find

- Snapshot and time/locale: `company_overview`.
- Unknown record: `search_records`.
- Telephone context: `lookup_by_phone`, `call_brief`, `get_job_detail`.
- Timeline: `list_activity`, `calendar_events`.

## Leads, quotes and CRM

- Leads: `list_leads`, `get_lead`, `create_lead`, `update_lead`, `delete_lead`.
- Lead contacts: `attach_lead_contact`, `detach_lead_contact`.
- Quotes: `list_quotes`, `get_quote`, `create_quote`, `add_quote_line`, `update_quote_line`,
  `delete_quote_line`, `update_quote`.
- Accounts: `list_accounts`, `get_account`, `create_account`, `update_account`.
- Contacts: `list_contacts`, `create_contact`, `update_contact`, `delete_contact`.
- Catalogue context: `list_services`.

Find before creating, inspect before changing, and read back after a write. Quote decisions need
the client's reported response. Sending quotes and deleting accounts are done in SiteAI.

## Tasks, people and sites

- Tasks: `list_tasks`, `create_task`, `update_task`, `delete_task`.
- Diary: `add_comment`, `update_comment`, `delete_comment`.
- People: `list_members`, `add_member`, `assign_to_site`, `move_crew_member`.
- Sites: `list_sites`, `get_site`, `update_site`.
- Record contacts: `list_record_contacts`, `attach_contact`, `detach_contact`.
- Customer live view: `send_tracking_link`.

Equipment relocation replaces custody/site state. Member invitations notify people. Re-attaching
a contact can overwrite flags; detaching can revoke tracking access. A live-view link is emailed
only when both a contact ID and an explicit email address are supplied.

## Roster, recorded shifts and evidence

- Roster: `list_shifts`, `get_shift`, `create_shifts`, `cancel_shift`, `list_no_shows`.
- Actual work: `list_worktime`, `get_worktime`, `worktime_summary`, `update_worktime`.
- Recorded operations: `list_action_entries`.
- Recorded trips: `movements_report`.
- Dockets: `list_dockets`, `get_docket`.

Planned offers and actual shifts are different records. Shift offers/cancellation may notify
people; signing/confirming evidence and answering/reassigning offers happen in SiteAI.

## Jobs, contracts, scope and progress

- Jobs: `list_jobs`, `get_job`, `create_job_site`.
- Contracts: `list_contracts`, `create_contract`, `send_contract_for_signature`, `void_contract`.
- Scope: `list_sow_items`, `create_sow_item`, `update_sow_item`, `import_quote_sow`.
- Variation approval: `send_variation_for_approval`.
- Claim reports: `list_progress_claims`, `issue_progress_claim`.

Signing requests and variation requests may email clients. Claims report completed value;
they do not execute payments or create an accounting invoice.

## Compliance, equipment and maintenance

- Compliance: `site_compliance`, `compliance_overview`, `operation_compliance`.
- Documents: `list_documents`, `create_document`, `submit_document`, `review_submission`.
- Equipment: `list_items`, `get_item`.
- Purchasing: `get_purchase_order`.
- Checks and history: `list_prestart_due`, `list_maintenance_logs`, `get_maintenance_log`.

Document resubmission can replace the previous document and review state. Requirements/types,
stock-ledger writes, historical maintenance imports, and physical prestart submission are
completed in SiteAI, not approximated with other public tools.

## Captures and attachments

- Capture inbox: `list_captures`, `get_capture`.
- Authorized filing: `file_capture`, `update_capture`.
- General attachment metadata: `list_files`.

Capture reads return photos and existing text without creating a voice transcript. Capture
filing creates a diary comment; moving, dismissing or reopening can move/remove that comment.
General file bodies are not exposed here. Never claim to have inspected unavailable content.

## Workflows

- Inspect: `list_workflows`, `get_workflow`.
- Define/update: `create_workflow`, `update_workflow`.
- Invitation access: `workflow_link`, `revoke_workflow_link`.

Use schema-supported recipes/steps only; obtain company-specific IDs from live records. Whole
step-list replacement, assignments, lock state, skipped steps and deactivation affect workers.
Confirm those consequences. Creating a link returns it; it does not send it to the recipient.

## Failure handling

- No match: broaden the lookup or ask for a distinguishing detail; never guess an ID.
- Several matches: show a small candidate list and ask which one.
- No write scope: explain the required access and allow user authorization.
- Dependency/conflict: report the refusal; do not cascade deletes, grants or reassignments.
- Uncertain mutation: read back before retrying.
- Unsupported capability: send the user to SiteAI rather than switching profile or inventing an action.
