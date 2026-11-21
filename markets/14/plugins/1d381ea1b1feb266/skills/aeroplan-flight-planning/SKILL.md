---
name: aeroplan-flight-planning
description: Use when a signed-in AeroPlan IQ user asks to find or review their saved drone operations, inspect flight-planning readiness, retrieve current planning context, or prepare explicitly authorised draft changes.
---

# AeroPlan IQ Connect — safe operation planning

Use the attached **aeroplan-iq** MCP connection. It is an owner-scoped planning and decision-support service, not an authority to operate an aircraft.

## Identity and consent

- Use `aeroplan_connected_profile` or `aeroplan_my_account` to establish the connected account and paid entitlement when needed.
- Only access the authenticated user's own AeroPlan records. Never seek records from other customers or bypass access controls.
- Default to read-only. Ordinary planning drafts require a separate, explicit OAuth-client grant; unsigned professional document proposals require a distinct Pro-only grant.
- When an action is unavailable, revoked, or not included in the subscription, explain the limitation instead of trying other credentials or unrelated APIs.

## Read workflow

- For historical or upcoming plans, call `aeroplan_list_operations` with relevant filters and bounded paging.
- Resolve exact IDs from returned records, then `aeroplan_get_operation` and `aeroplan_check_readiness` as needed. Prefer the latest saved revision.
- Use the weather/NOTAM tools only where an operation supplies a usable date and location, and state the authoritative source, time coverage and any unavailable or stale result exactly as returned.
- Never infer that a green check, clear map or absence of notices proves legal permission to fly.

## Prepare / approve / commit boundary

- Treat the Remote Pilot as the final decision-maker. Do not approve flights, sign RAMS or SORA, grant aviation/airspace permission, or certify legal compliance.
- For a requested ordinary change or repeat, first obtain the exact owned operation and saved revision; use the matching `aeroplan_prepare_operation_change`, `aeroplan_prepare_operation_repeat` or `aeroplan_create_operation_draft` tool with a fresh idempotency UUID.
- For professional documents, use the Pro-gated context and `aeroplan_prepare_document_draft` only with distinct document permission. Mark uncertain site conditions, permissions and external evidence as unverified; never fabricate evidence.
- Preparing a proposal is NOT a saved operation change. Describe the exact proposed change and direct the pilot to review/approve the immutable proposal in AeroPlan IQ. Only then may `aeroplan_save_operation_draft` or `aeroplan_save_document_draft` commit the exact approved proposal ID, if the live server authorises it. Do not substitute a conversational 'yes' for the first-party pilot approval.
- If a tool rejects a revision, authorisation or entitlement, do not retry with a different identity or bypass the boundary; have the pilot refresh/review the record in AeroPlan.

## Integrity and limitations

- Keep AeroPlan IQ's cloud operation as the system of record; never treat chat history as the official flight record.
- Show critical planning gaps without granting clearance. Always direct the pilot to verify current official airspace restrictions, NOTAMs, weather, local site access, permissions, insurance and applicable aviation rules.
- Do not reveal account secrets, personal contact data, signed documents or full safety evidence unnecessarily.
