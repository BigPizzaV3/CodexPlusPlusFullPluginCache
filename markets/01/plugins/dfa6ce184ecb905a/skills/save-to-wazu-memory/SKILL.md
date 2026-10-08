---
name: save-to-wazu-memory
description: Save, remember, ingest, archive, or commit user-authorized information into an explicitly resolved Wazu cohort. Use for structured summaries, decisions, updates, tasks, meeting notes, raw text, transcripts, documents, images, audio, video, or other supported media that the user wants stored in Wazu.
---

# Save To Wazu Memory

Write only after the user has requested persistence and the target Wazu cohort is unambiguous. Report the complete storage and enrichment lifecycle rather than collapsing every accepted request into “saved.”

## Load the Wazu contract

- Read [references/wazu-data-model-and-scope.md](references/wazu-data-model-and-scope.md).
- Read [references/ingestion-routing-and-safety.md](references/ingestion-routing-and-safety.md).

## Execute the workflow

1. Confirm write intent and target.
   - A direct request to save or remember is sufficient write intent.
   - Call `account_context` when the connected actor or current scope is unknown.
   - Resolve a named target using `list_cohorts`; use only an authorized returned cohort UUID.
   - Stop when the target is missing or ambiguous.
   - Personal ingestion is not supported while Wazu requires a real cohort target.
2. Choose the correct write lane.
   - Use `commit_summary_to_cohort` for a structured summary, decision, update, task, or note.
   - Use `ingest_text` for raw text, transcripts, or document text.
   - Use `ingest_media_base64` for supported document, image, audio, or video bytes.
3. Prepare one intentional write.
   - Preserve the user's meaning and source context.
   - Add useful tags only when they are supported by the content.
   - Reuse a stable idempotency key when one exists.
   - Do not automatically retry a timed-out write until server-side duplicate suppression is confirmed.
4. Verify the result.
   - Capture the returned item and cohort identifiers.
   - Distinguish stored, replicated, enriched/indexed, graph-linked, and retrieval-verified states.
   - Use `get_item` for read-after-write verification when the response does not already prove retrieval readiness.
5. Report the exact outcome.
   - Say what was stored, where, and which lifecycle stages succeeded.
   - State plainly when enrichment, graph linking, or retrieval verification is pending or failed.

## Guardrails

- Never write to an ambiguous target.
- Never substitute a synthetic Personal selector for a cohort UUID.
- Do not expose raw media bytes, credentials, bearer tokens, payer identifiers, internal file paths, or debug dumps.
- Do not claim success for a lifecycle stage that the server did not confirm.
- Do not delete, overwrite, or edit existing Wazu evidence from this skill.
