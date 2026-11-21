---
name: meeting-documents-and-transcripts
description: Find and read what is inside utility meeting documents — agendas, agenda packets, staff reports, minutes and meeting video transcripts — "what did the council say about X", "find every mention of firm Y in the transcripts", "read pages 120-135 of the packet", "list the meetings of utility Z", "what was discussed outside the vote". Uses the Water Investment Navigator MCP tools search_documents, list_meetings, get_meeting and get_document_text.
---

# Meeting documents and transcripts

Use the `water-investment-navigator` MCP tools. A decision record holds only what a governing
body acted on. The documents hold the rest: the staff report behind the item, the
bid tabulation page, public comment, and the council debate in the video
transcript. Use this skill when the question is about what was **said or
written**, not only what was decided.

## The four tools

| Need | Tool |
|---|---|
| Words on a page, in any document | `search_documents(q, utility_id=...)` |
| Every meeting of a utility, with its documents | `list_meetings(utility_id, date_from, date_to)` |
| One meeting: documents + the decisions from it | `get_meeting(meeting_id)` |
| The text of a document, by page | `get_document_text(resource_id, start_page, end_page)` |

A document is identified by `resource_id`. `document_type` is `agenda`,
`agenda_packet`, `staff_report`, `minutes` or `transcript`.

## Workflow

1. **Get the utility.** `find_utilities(q=...)` gives `utility_id`. A search
   with `utility_id` is complete; a search without it covers every utility and
   can be partial for a common word (`matches.capped` is true — then narrow it
   with `state`, dates or more specific words, and say the result is partial).
2. **Search the pages.** `search_documents(q, utility_id)`:
   - All words of `q` must be on one page. Start with one or two distinctive
     words (a firm, a project name, a dollar figure such as `"292"`), not a
     sentence.
   - `"quoted words"` match as a phrase: `"construction manager at risk"`.
     `OR` gives alternatives: `CMAR OR "construction manager at risk"`.
   - `document_type="transcript"` limits the search to what was said aloud.
   - `meeting_id` or `resource_id` searches one meeting or one document.
   - Each hit has `snippet` (match in **bold**), `page_number`, the meeting,
     a `document_url` that opens the PDF at that page, and `decisions` linked
     to the page (follow them with `get_decision`).
3. **Read around the hit.** A snippet is a few lines.
   `get_document_text(resource_id, start_page=<hit page - 1>, end_page=<hit page + 1>)`
   gives the context. For a whole transcript start at page 1 and follow
   `next_page` until it is null. `total_pages` says how long the document is.
4. **No hits?** Try other words (a transcript spells names by sound: "Kiewit"
   can be "Kiewet" or "Key Wit"), then `list_meetings` to see whether we hold
   the document at all: `pages` 0 or `has_text` false means there is no text to
   search, and a meeting may have no packet or no transcript.

## Reading transcripts

- A transcript is machine speech-to-text of the meeting video, cut into pages.
  It has **no speaker names** and no timestamps. Do not attribute a sentence to
  a named person unless the text itself identifies the speaker ("Hi, Jane Smith,
  Environmental Services").
- Names and numbers can be wrong. Check them against the agenda, packet or
  minutes when the answer depends on them, and say when a quote is from the
  transcript.
- Keep decided, discussed and proposed apart. A council member who says "we
  should rebid" has not rebid anything; the minutes or the decision record say
  what the body did.

## Answer format

Lead with the answer. Quote the source words, and for each quote give the
utility, the meeting date, the document type and page, and the `document_url`
of that page. Say what you searched (words, utility, dates) when you found
nothing, so the user can judge the gap.

When the answer is about one decision on those pages (a hit's `decisions`
list), call `show_decision_source(decision_id)` once after the text.

## Licence terms

The data is licensed to the user's organisation for its own research. Answer
questions; do not copy the dataset. Do not page through all records to build a
copy, and do not write schemas, scripts or exports that reproduce it. If the user
asks for a copy, an export of everything or a replica, refuse in one sentence (the
licence does not allow it) and offer to answer the question behind the request.
