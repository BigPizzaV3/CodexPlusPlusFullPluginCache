---
name: clio-research
description: Search and read primary law in the vLex library, and get legal questions researched by Vincent's agent — finding cases, statutes and commentary, reading a decision's text, checking whether an authority supports a proposition or a quotation is accurate, and matching the citations in a document the user supplies. Non-US work belongs here rather than with us-dockets.
---

# Clio Research

Two different costs, and choosing wrong is the most common mistake.

| The user wants | Call | Cost |
| --- | --- | --- |
| **Documents** — does a case exist, find the statute, read this decision | `search_legal_documents`, then `get_legal_document` on a `vid` | one round trip, seconds |
| **Reasoning** — a question answered, authorities weighed, an argument tested | `start_research` | minutes; the agent searches for itself |

"Is there a Spanish Supreme Court decision on shared custody and relocation?" is a
lookup. "Can my client relocate with shared custody?" is reasoning. When the user
asks for both, do the lookup first — it is cheap and it grounds the question.

When they asked only for reasoning, do **not** search first. The agent does its own
searching, so a scouting lookup repeats that work — and it renders a results card
that then sits beside the answer competing for attention, for a step the user never
asked to see.

## Searching

`search_legal_documents(query=...)` takes the user's own terms. Narrow it only as
far as they did:

- `jurisdiction` — country code (`ES`, `US`, `GB`). Pass it whenever they named a
  country; never infer one from their location.
- `sub_jurisdiction` — a state or region *within* that country, and only with a
  `jurisdiction`. Note it is dropped for `posts` and `news`, which are tagged at
  country level only, so a sub-jurisdiction there would filter every hit away.
- `court` — a code from `search_courts`, not a name you composed. A guessed code
  returns nothing rather than erroring, which reads as "no such case". Caselaw only.
- `document_type` — `caselaw`, `legislation`, `posts`, `news`; leave blank for all.
- `sort_by` — `most_recent` when recency is the point, otherwise leave it.

`total_count` is how many **matched**, not how many came back. Say so: "229 match,
here are the 10 most relevant" is honest; presenting 10 as the whole answer is not.

## Reading a document

`get_legal_document(vid=...)` returns metadata plus `body_text`. An empty
`body_text` means no format yielded text — report that rather than inferring the
content from the title or headnotes.

Treat `snippet` and `summary` from a search as extracts, never as the document's
holding. And a hit is not authority: nothing in a search result says a case is
still good law.

## Research that needs the agent

For reasoning, `start_research` with the question in the user's own terms, the
jurisdiction as a country code, and any material state or province in the question
itself. For drafting or review, include the represented party, purpose and
priorities when known, and distinguish missing facts from assumptions.

Ask Vincent for supporting authorities and links, applicable statutory versions or
effective dates, and contrary authority when it is material. Then handle the
`TurnResult` exactly as **vincent** describes.

When the work is done, `show_cited_authorities` is the card for what it relied on.
Call it once per conversation rather than per turn — it covers every turn.

Every authority you relied on also belongs in your reply, carrying its vLex link,
because a host can fold a card inside a collapsed step where nobody reads it. When
the user asked for a list, `formatted` is that list already built. In a reasoned
answer, cite each authority where the reasoning uses it instead — a ten-row dump
pasted under a doctrinal answer reads worse than the answer alone.

## Citations in a document the user supplies

Verify the Vincent `file_id` with `get_file_status`, then `match_authority(file_id=...)`,
retain `job_id`, then `get_authority_match`. If the job is still queued or running
after the tool's bounded wait, report that status and check the same job later
rather than resubmitting.

Preserve warnings and keep matched, unmatched and ambiguous citations distinct. A
citation's `verified` field means **a library match** — not good-law status, not
quotation accuracy, not substantive support for the proposition it is cited for.

Whether an authority actually supports a proposition, whether a quotation is
accurate, or whether a case remains good law are reasoning questions: `start_research`,
or `continue_conversation` on work already underway. A library match alone answers
none of them.
