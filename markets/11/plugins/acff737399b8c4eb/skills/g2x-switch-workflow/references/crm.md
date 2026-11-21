# GovCon CRM

Work in the signed-in user's G2X CRM. Find and read a record before changing it. Match companies and people with stable IDs and supporting identity evidence. Do not create a duplicate because a display name varies. If the answer asks which record the user meant, show them the choices and let them pick. Call again with that G2X id, or with `create_new` only if they say it is new. Never choose for them.

Use the smallest action that satisfies the request. Preserve existing fields the user did not supply. Record meeting content faithfully, and distinguish what a participant said from what they committed to. Sending an email is separate from writing a note; these tools send nothing. Nothing here can delete, archive or merge records, or edit a note that is already there.

### `g2x_crm_find`

Search the user's CRM for accounts and contacts. Use it before adding a note, logging an interaction or setting a next step.

- Inputs: `query` (required, name, UEI, website, email or G2X id); `record_type` (`account` or `contact`).
- Output: each match with its G2X id and the fields that tell records apart, how many records match, and which fields were searched. A search returns at most the plan's rows per call.
- Plan: all plans. Read only. On the research endpoint: no.
- Example: `{"query": "Acme Federal Solutions"}`

### `g2x_crm_get_record`

Read one account or contact as G2X shows it now, before making a change.

- Inputs: `record_type` (required: `account` or `contact`); `record_id` (required, the record's G2X id).
- Output: the record's fields, next step, people or account, linked pursuits and latest notes.
- Plan: all plans. Read only. On the research endpoint: no.
- Example: `{"record_type": "account", "record_id": "<id from CRM find>"}`

### `g2x_crm_save_account`

Add an organization to the user's CRM, or update one they have. Only the fields given change.

- Inputs: `account_id` (to update by id); `uei` (for a company) or `agency_code` (for a government agency) so G2X finds exactly that organization; `name`; `account_type` (`company`, `government_agency`, `consultant`, `university`, `state_government`, `local_government`, `school_district`, `other`); `cage_code`, `website`; `lifecycle_status`; `relationship_health` (`strong`, `warm`, `cold`, `unknown`); `company_relationship` (`subcontractor`, `teaming_partner`, `competitor`); `create_new` (true only after the user confirmed this is a new account). With only a name, G2X writes into the one account with that name.
- Output: the record as G2X shows it after the write. Given fields replace what was there.
- Plan: all plans. Write. On the research endpoint: no.
- Example: `{"uei": "<12-character UEI>", "lifecycle_status": "target", "company_relationship": "teaming_partner"}`

### `g2x_crm_save_contact`

Add a person to the user's CRM, or update one they have. Only the fields given change. A new email or phone is added to the person.

- Inputs: `contact_id` (to update by id); `last_name` (needed to add someone new), `first_name`, `email`, `phone`, `title`; `account_id` (the account they belong to); `contact_type` (`government`, `partner`, `competitor`, `consultant`, `other`); `relationship_strength` (`strong`, `warm`, `cold`, `unknown`); `create_new` (true only after the user confirmed this is a different person). Without an id, G2X matches by email, then phone, then by name within the account given.
- Output: the record as G2X shows it after the write. Do not merge namesakes.
- Plan: all plans. Write. On the research endpoint: no.
- Example: `{"last_name": "Lee", "first_name": "Jordan", "title": "Program Manager", "account_id": "<account id from CRM find>"}`

### `g2x_crm_add_note`

Add a relationship note to an account or contact, written as the user. The same words on the same record again return the existing note.

- Inputs: `record_type`, `record_id`, `body` (all required; the note in the user's words); `title`.
- Output: the note on the record's notes and timeline. It only appends; it never edits or deletes a note.
- Plan: all plans. Write. On the research endpoint: no.
- Example: `{"record_type": "account", "record_id": "<account id>", "body": "Interested in teaming on the next recompete."}`

### `g2x_crm_log_interaction`

Record a call, meeting, email or event that already happened. For something planned, set a next step or add a task instead.

- Inputs: `kind` (required: `call`, `meeting`, `email`, `event`, `other`); `occurred_at` (required, a date or a time with its offset, in the user's own time zone); `summary` (required, what was discussed and agreed); `account_id`; `contact_ids` (up to 10 people involved).
- Output: one note on the account and on each person involved. Each person's last-contacted date moves forward. It sends nothing.
- Plan: all plans. Write. On the research endpoint: no.
- Example: `{"kind": "call", "occurred_at": "2026-10-12", "summary": "Discussed the upcoming industry day and teaming roles.", "account_id": "<account id>"}`

### `g2x_crm_set_follow_up`

Set the next step on an account or contact, replacing the current one. An empty action clears it.

- Inputs: `record_type`, `record_id`, `action` (all required; the next step in a few words, empty clears it); `due_at` (when it is due). Resolve dates and time zones with the user. Do not invent an owner.
- Output: the record with its new next step.
- Plan: all plans. Write. On the research endpoint: no.
- Example: `{"record_type": "account", "record_id": "<account id>", "action": "Send capability statement", "due_at": "2026-10-16"}`

### `g2x_crm_add_task`

Add a task, assigned to the signed-in user, to one of their pursuits. The same subject and due day again return the existing task. It shows on the pursuit and on the timeline of the account it is linked to.

- Inputs: `pursuit_id` (required, a linked pursuit on an account); `subject` (required, what needs doing); `due_date`; `priority` (`urgent`, `high`, `medium`, `low`); `description`.
- Output: the task on the pursuit. It does not perform the task.
- Plan: all plans. Write. On the research endpoint: no.
- Example: `{"pursuit_id": "<pursuit id from the CRM record>", "subject": "Draft the past performance section", "due_date": "2026-10-20"}`

Read back after a change, especially after a timeout, before retrying. An accepted request is not proof the record changed. Return the changed fields and the record link, or explain the exact action that did not complete.
