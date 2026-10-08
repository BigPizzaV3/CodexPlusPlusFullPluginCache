---
name: june-maintain-casework
description: Create and update ordinary case-management records in JUNE safely. Use when a user asks to create or modify a case, contact, case participant, note, deadline, appointment, or document metadata. Use the dedicated facts skill for Case Facts or Document Facts.
---

# Maintain JUNE casework

Resolve the target and required identifiers before changing data. Use JUNE's current record as the source of truth.

## Prepare the change

1. Identify the authenticated user and relevant permissions with `whoami` or `get_user_permissions` when authorization is material.
2. Resolve the case with `get_case_by_reference` or another read tool. Never infer a case ID.
3. Read the current target record before updating it.
4. Resolve controlled values instead of inventing IDs:
   - mandates: `list_mandates`
   - roles, deadline types, appointment types, document types, and other reference values: `get_value_list`
   - contacts: `search_contacts`, then `get_contact` for the selected match
5. If multiple targets or values remain plausible, ask the user to choose.

## Apply the requested operation

Use the narrowest matching tool:

- new records: `create_case`, `create_contact`, `add_case_participant`, `create_note`, `create_deadline`, or `create_appointment`
- existing records: `update_case`, `update_document`, or `update_appointment`

For `add_case_participant`, select an existing contact or create one first, resolve the exact role with `get_value_list("Roles")`, and never confuse contact ID with participant ID.

Use `$june-manage-facts` for `update_casefact`, `create_document_facts`, or `update_document_facts`; those operations require their own schemas and version rules.

Before a destructive-hint update, summarize the exact target and replacement values and obtain explicit confirmation unless the user's latest instruction already states that exact target and change. Do not silently overwrite existing values. Never broaden a requested change to adjacent fields or records.

Create operations may produce duplicates. Do not retry a successful or ambiguous write automatically; read the record back first.

## Report the result

State what changed, identify the case and affected record, and include returned IDs or deep links. If the tool returns an error or an ambiguous outcome, preserve the current state and explain the next safe check.
