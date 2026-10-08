---
name: june-prepare-correspondence
description: Draft or send controlled outgoing correspondence from a JUNE case and its filed documents. Use when a user asks to prepare or send an email or beA dispatch, select case attachments, resolve an eligible case participant's address, or start JUNE's outgoing-message and dispatch-check workflow.
---

# Prepare JUNE correspondence

Treat dispatch as an external, irreversible action. Never send to a guessed address, use documents from another case, or invent recipient, sender, or provider identifiers.

## Resolve the case and attachments

1. Resolve the case with `get_case_by_reference`, then call `get_case_context`. Stop if the case is archived or read-only instead of attempting a dispatch.
2. Select attachments from `get_all_documents_for_case`, `get_documents_by_ids`, or `azure_search`.
3. Verify every selected document belongs to the resolved case. Keep the first document as the master unless the user designates another one.

## Resolve the recipient and address

1. Select an active entry from `get_case_context.case.participants`. Retain its `id` as the participant ID and its `contact_id` as the recipient contact ID.
2. Call `get_contact(contact_id)` for the full contact. Read the available `emailAddresses` from that result; the case context intentionally does not include them.
3. If starting with `search_contacts`, call `get_contact` for the chosen match and verify that its contact ID occurs among the selected case's participants. A contact search result alone is not an eligible recipient.
4. If the contact is not yet a case participant, stop. Offer `add_case_participant` only when the user asks to add the contact, and resolve the role with `get_value_list("Roles")`.
5. If no E-mail address is stored, stop. Never substitute an address supplied outside the selected contact record.
6. If several addresses are stored, show them and ask the user to choose the exact destination.
7. Pass the chosen address as both `email` and `send_to` unless the user explicitly selects two different addresses from that same eligible participant. The server validates both fields independently.

## Resolve sender and channel

1. Use the case's `clerk_id` from `get_case_context` or the authenticated caller ID from `whoami`; no other sender ID is permitted.
2. For this tool contract, use provider type 2 for E-mail and provider type 1 for beA.
3. Draft subject and body in the user's language. Do not add unsupported factual or legal assertions.

## Confirmation boundary

If the user asks only to prepare or draft correspondence, return the draft and do not call `process_dispatch_document`.

Immediately before an actual send, show:

- case reference
- channel
- participant and contact ID
- recipient name and exact destination address
- subject and complete body
- document IDs, filenames, master document, and attachment order
- sender identity

Obtain explicit confirmation of that complete summary. An earlier general request to prepare correspondence is not permission to send.

## Send and report

Call `process_dispatch_document` once after confirmation. The tool starts the actual dispatch and creates the outgoing-message record before it attempts to create the later dispatch-check task. The check task is not a pre-send approval gate.

Never retry automatically after a timeout or ambiguous response. Inspect `get_outgoing_messages_for_case` and `get_tasks_for_case` first because the message may already have been dispatched even when task creation failed.

Report dispatch status, outgoing-message or dispatch ID, check-task status and ID, and any manual review still required. If validation rejects a recipient, address, sender, or attachment, stop and correct the verified JUNE record rather than bypassing the check.
