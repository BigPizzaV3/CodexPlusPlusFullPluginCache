---
name: june-manage-facts
description: Read, interpret, create, and update Case Facts and Document Facts in JUNE using their live schemas. Use when a user asks about structured case data, extracted document fields, fact schemas, field groups, allowed values, or requests a change to a Case Fact or Document Fact.
---

# Manage JUNE facts

Treat Case Facts and Document Facts as separate systems. Always read the live schema before writing, use exact keys from that schema, and preserve unrelated current values.

## Work with Case Facts

1. Resolve the case with `get_case_by_reference`, then call `get_case_context`.
2. Read from the context:
   - `mandate_id`
   - mandate-specific values and version in `case_facts`
   - global values and version in `case_facts_without_mandate`
   - `is_archived` and `is_read_only`; do not write facts when either blocks changes
3. Load both applicable schema scopes:
   - `get_casefact_schema(mandate_id=<case mandate>)`
   - `get_casefact_schema(mandate_id=-1)` for global Case Facts
4. Use `get_all_casefact_schemas` only for cross-mandate discovery. Use `list_mandates` when a mandate name must be resolved.
5. Match the requested field by schema label, then retain its exact `guid_key`, `data_type`, allowed values, `disabled`, `is_fieldgroup`, and source mandate. Never guess a GUID or treat a global field as mandate-specific. Do not write a disabled field.

For a scalar Case Fact:

1. Check allowed values in the schema.
2. Call `format_casefact_value` with the schema's data type and the user's raw value.
3. Stop if formatting fails or an enum value is not allowed. If the user includes a unit or currency but the schema field is numeric, confirm that only the numeric component will be stored; do not silently encode the unit in a number field.
4. Use the version from the matching current facts block. If no block exists, use a version only when the matching schema or tool result establishes it; otherwise ask instead of guessing.
5. Call `update_casefact` with the exact case ID, GUID key, formatted value, matching mandate ID, and version.

For a Case Fact with `is_fieldgroup=true`:

1. Call `get_fieldgroup_schema(field_group_keys=[<casefact guid>])`.
2. Use only returned column GUID keys and data types.
3. Read and preserve the current `fieldGroupValues`. The tool replaces the complete row collection for that field; never send only a partial row update.
4. Show the full resulting row collection and obtain explicit confirmation before calling `update_casefact` with `{"fieldGroupValues": [...]}`.
5. Stop if the field-group schema is missing or the current rows cannot be represented without loss.

## Work with Document Facts

1. Resolve the document and verify that it belongs to the intended case. Read that case with `get_case_context` and do not write facts when the case is archived or read-only.
2. Call `get_document_facts(document_id)` for current values.
3. Always call `get_document_fact_schema(document_id)` before a write. Use the exact returned field label or key, type, `allowed_values`, and `group` flag.
4. Stop for `group=true`; the exposed create and update tools support only single-value Document Facts.
5. Use `create_document_facts` only for schema-defined fields that are currently absent.
6. Use `update_document_facts` only for fields that already exist, with labels or keys exactly as returned by `get_document_facts`.
7. If the stored value already equals the requested value, make no write.
8. Treat each mapping as all-or-nothing: an unknown, grouped, already-present, or invalid field rejects the complete request. Do not mix creates and updates in one call.

## Confirm, write, and verify

Before `update_casefact` or `update_document_facts`, show the old value, new value, target case or document, schema field, and scope, then obtain explicit confirmation unless the latest user instruction already states that exact change. For creates, summarize the exact new fields and target.

Call each write once. Separate Case-Fact and Document-Fact calls are not one transaction: execute them in the confirmed order, verify each result, and stop the remaining writes after a failure while reporting any partial success. After an error or timeout, read the facts again before retrying. After success, re-read with `get_case_context` or `get_document_facts` and report the stored value, target ID, field label, and field key.
