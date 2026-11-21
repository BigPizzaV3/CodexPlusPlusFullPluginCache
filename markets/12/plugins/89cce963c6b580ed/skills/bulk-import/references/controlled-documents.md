# Controlled-document import policy

Require doc_number and title. Candidate fields include doc_type, revision, permitted draft status, owner_id, review_due, process_id, location_url, location_note, change_summary and notes. Preserve document numbers and revisions as text. Check live enums/defaults.

Match verified ID first. Otherwise review document number AND revision context; number alone may not identify a revision. Approved revisions remain protected. Do not overwrite an approved record to simulate a new revision, import approved status or manufacture approver/date/evidence IDs. Use an actual supported revision operation or hand off to the app.

location_url/location_note are location metadata, not upload or file-access proof. Generic links do not establish evidence-version associations. Defer unsupported file transfer explicitly. Describe the approved notes/change-summary patch rather than rewriting existing narrative silently.
