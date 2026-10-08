---
name: june-research-case
description: Research and summarize a legal matter in JUNE without changing data. Use when a user asks to find a case, inspect its context, documents, Case Facts, Document Facts, deadlines, appointments, tasks, notes, or messages, compare case records, or answer a case-related question from JUNE evidence.
---

# Research a JUNE case

Use JUNE as the source of truth and keep this workflow read-only.

## Find the case

1. Use `get_case_by_reference` when the user supplies a case reference.
2. Use `get_recent_cases` for a recent matter, `search_cases_by_casefact` for a known structured fact, or `azure_search` for a content search.
3. When more than one case matches, show the distinguishing reference, title, and parties and ask the user to choose. Never guess a case ID.

## Build the evidence

1. Start with `get_case_context` for the selected case.
2. Fetch only the records needed for the question:
   - documents: `get_all_documents_for_case`, then `get_documents_by_ids` or `get_document_content`
   - semantic document passages: `document_vector_search`
   - deadlines, appointments, tasks, notes, and messages: use the corresponding `get_*_for_case` tool
3. Page through long result sets when the answer depends on completeness.

## Interpret facts through their schemas

Treat Case Facts and Document Facts as different systems.

- For Case Facts, read values from `get_case_context`. Load `get_casefact_schema` once with the case's `mandate_id` and once with `mandate_id=-1` for global fields. If an entry has `is_fieldgroup=true`, call `get_fieldgroup_schema` with that field's GUID key before interpreting its rows.
- For a cross-mandate schema search, use `get_all_casefact_schemas`; use `list_mandates` to resolve a named mandate.
- For Document Facts, call `get_document_facts` for current values. Call `get_document_fact_schema(document_id)` when the answer depends on field type, allowed values, grouped status, or fields that are defined but currently empty.

Use schema labels for presentation and retain GUID keys or field keys for verification. Distinguish returned facts from interpretation. Do not invent missing dates, parties, amounts, field meanings, or legal conclusions.

## Respond

Answer in the user's language. Lead with the requested conclusion, then list the JUNE records supporting it. Include the case reference and useful record IDs or returned deep links so the user can verify the result. Minimize unnecessary personal data.

Do not call write tools in this skill. If the user asks to change facts, use `$june-manage-facts`; for other changes use the appropriate maintenance, document-creation, or correspondence workflow.
