---
name: drafting
description: Have Vincent write legal documents — memos, letters, clauses, agreements, motions — and then read, revise, or deliver them as Word or PDF. Covers what to put in the request so the draft is usable, retrieving the actual document rather than the prose summary of it, paging through long text, versions, and export links.
---

# Drafting with Vincent

Drafting runs on the same agent as research: `start_research`, or
`continue_conversation` to revise. The tool's name does not restrict it — the
agent drafts and analyses documents as well as answering questions. Put the
actual requested work in `question`.

## Asking for a draft that is usable

A draft is only as good as the framing, so carry into `question`:

- **Who is represented**, and what they are trying to achieve.
- **The facts as the user gave them** — verbatim where they matter. Do not
  summarise away dates, amounts, party names or defined terms.
- **The governing law**: country code as `jurisdiction`, and any state, province
  or forum in the question itself.
- **The form and length** if they said, and any authority they want cited.
- **What is missing.** Say which facts you are assuming rather than inventing
  them, and ask only for what actually blocks the draft.

Ask for supporting authorities and links where the draft asserts law, and for
contrary authority when it is material to the position.

## Getting the document, not a description of it

A completed turn's `answer` may summarise the draft; the draft itself is in
`files`. Do not relay the summary as the deliverable.

- `list_output_documents` names what exists, when `files` is not enough. An empty
  list means no draft yet — say so rather than inventing a filename.
- `get_output_document` reads one. Omit `version` for the latest. `available_versions`
  lists earlier drafts.
- Content is paged: `start` is a character offset, `max_chars` defaults to 50,000
  and caps at 200,000. When `truncated` is true, advance `start` by the length of
  the returned `content`. **Pin the returned `version` while paging** so a later
  edit does not mix two drafts into one read.
- Do not claim a complete review after reading only part of a document.
- `show_documents` displays what was produced, as a card. The authorities the
  draft rests on have their own card: `show_cited_authorities`.

The `citations` a document read returns are the authorities used **across the
conversation**, not the ones in that document or that passage. Do not attach the
conversation's authority list to individual sentences.

## Revising

Revisions are `continue_conversation` on the same `conversation_id`, describing
the change. There is no targeted-edit tool here: a request as narrow as "change
the third paragraph" still runs a full turn, so state exactly what should change
and what must stay.

## Delivering

`export_document` with the conversation id, file key and `format="docx"` or
`"pdf"`. Use the reviewed `version` when exporting a specific draft.

- `status="completed"` with `download_url`: give the user the link. It is
  pre-signed for **seven days, and anyone holding it can download without Vincent
  credentials** — keep it to the authorised audience and say so if that matters.
- `status="failed"` or an error: report the failure. Do not claim a file is ready.
- No URL yet: the render may still be running. Relay `guidance` and the real
  status, call `export_document` again to pick up a finished render, and do not
  loop rapidly or label an interrupted export complete.

Do not fetch the signed URL yourself or inline the document's bytes; large
payloads get truncated by the host. There is no need to rebuild a DOCX or PDF
locally because the answer arrived as prose — and never substitute a locally
reconstructed file for Vincent's export without saying that is what you did.

## What a draft is

Label it a draft for review, never as executed, filed or served. Describe the
document's text as Vincent's writing, separately from the conversation's `answer`
and from the user's own facts. For a review rather than a draft, connect each
finding to the clause or page it came from, explain its effect for the represented
party, and keep issues distinct from proposed wording.
