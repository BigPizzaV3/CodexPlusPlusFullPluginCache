---
name: qi-prd-acceptance
description: "Review, revise, and explicitly accept a QI application PRD draft after provide_prd and before create_project. Use after provide_prd saves a draft, the user asks to inspect or edit the pending PRD, or create_project reports that a draft still needs acceptance."
---

# QI PRD acceptance

Use the server draft as the source of truth. Call `get_prd_draft` at the start, even when the documents were just submitted. Do not reconstruct the draft from conversation memory.

Present the complete persisted documents to the user before requesting approval. Use clearly labelled `Product Requirements Document` and `Technical Requirements` sections and include the full markdown returned by `get_prd_draft`. Do not summarize, abbreviate, elide sections, replace content with placeholders, or merely offer the complete documents on request. A short introduction may precede them, but it cannot replace either document.

After displaying both complete documents, ask whether the exact draft is approved or needs changes. This is an approval gate: silence, moving to another topic, a general request to continue, or approval given before the complete current documents were displayed is not approval. Accept only an explicit statement that the displayed PRD and Technical Requirements are approved, accepted, correct, or ready to create.

If the user requests edits, update whichever document is affected, preserve unaffected content, and call `update_prd` with both complete replacement documents. Then call `get_prd_draft` again and display both refreshed documents in full before asking for approval again. Repeat until the user explicitly approves the exact current documents. Never call `accept_prd` in the same response that first displays a new or edited draft.

If the user asks a question about the draft, answer it without treating the question as approval. If the answer changes either document, update the persisted draft and display both complete refreshed documents again before returning to the approval question.

After explicit approval, call `accept_prd` exactly once. Report that the documents are locked, then return to the `qi-remote-dev` workflow and call `create_project` with the agreed name and description. If the server reports the draft is already accepted, do not attempt edits; continue to project creation. If it reports expiry, restart through `start_prd_discovery` and explain that the prior draft expired.

The `skip_prd` path is outside this skill and remains valid only when the user explicitly asks to skip PRD discovery.
