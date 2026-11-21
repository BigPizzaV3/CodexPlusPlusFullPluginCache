# Editing, honesty and previews

## Editing without regenerating

Editing the Markdown is free. Regenerating costs credits and makes a new document.

- `update_buyer_persona_document(ideaId, buyerPersonaDocumentId, name?, text?)`: `text` replaces the entire Markdown. Read the document, change the text, send the full result. Keep its headings and structure. Change only what the user asked.
- A landing page or deck does not update when its positioning changes later. To carry a change over, generate a new page or deck from the edited positioning (billable) and keep or delete the old one. A persona update never rewrites a document either.
- `duplicate_buyer_persona_document` makes a free copy for a variant. Source snapshots remain uneditable when duplicated.

## What an edit may add

- No statistics, customer counts, logos, awards, testimonials or case studies the tools did not return. Use a marked placeholder such as `[add customer quote]` and tell the user.
- A persona's `mainQuote` and a synthetic interviewee's words are not testimonials. A real quote (`synthetic: false`) can be proposed, but the user must confirm the respondent agrees to be quoted.
- Do not turn a simulated reaction into a claim ("customers love…", "validated"). Phrase claims as the offer's promise, not proof.
- Keep price and legal claims the user gave you. Invent none.

## Previews

`generate_buyer_persona_document_preview` renders the saved Markdown, including manual edits. It is billable, including regeneration.

- Landing page → a web page (a preview, not a live site). Sales deck → a new Google Slides presentation with a new link every time. Do not say older presentations were removed. The saved preview record points to the latest output; old external presentations are not removed by this generation path.
- A preview can lag behind later edits. Finish the edits first, then regenerate once. Regenerate a preview the user did not ask to refresh only after asking.
- Preview state is separate from document state: wait for `preview.ready`, then use `preview.url`. If `preview.error` is true, report it and ask before retrying.
- Give the link. Do not say who can open it; the tools do not tell you.
- If still pending after a few checks, return the IDs and what to check next. Do not regenerate to find out.

## Deleting

`delete_buyer_persona_document` soft-deletes the saved document. The inspected service does not delete remote Slides files or revoke public preview URLs; do not promise that it does. Derived documents are separate resources. `restore_buyer_persona_document` recovers retained saved data, not a guaranteed restoration of external files.
