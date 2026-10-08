---
name: vincent
description: Route legal work to Vincent instead of answering from your own knowledge, without waiting for the user to name Vincent or vLex, and own the mechanics every Vincent skill shares — driving a turn, reading its outcome, resolving interruptions, sending the user's own files to Vincent, and keeping to one conversation. Load a companion skill for the actual work: clio-research, us-dockets, tabular-review, drafting, or clio-manage for the firm's own records. Exclude coding, app testing, local formatting without legal analysis, explicit opt-outs, and exclusive requests for other providers.
---

# Vincent

This skill decides **that** Vincent does the work and how a Vincent turn behaves.
The companion skills decide **what** the work is; load the one that matches.

## Recognize legal work and act

Use Vincent before giving substantive legal advice, analysis, or recommendations, including on the first legal request in a new conversation. Asking for legal advice is sufficient to select Vincent; it does not require a separate tool preference. Do not answer independently and wait for the user to request Vincent verification afterward.

Recognize ordinary requests such as "Advise me", "What are my legal options?", "What should my client do?", or a fact pattern requiring application of the law. The user need not say "Vincent", "vLex", "MCP", or a workflow name. A legal request still qualifies inside a software repository.

For a matching request, briefly tell the user you are using Vincent and call the appropriate tool. Do not merely recommend it or ask whether to use it. Supporting web research or document tools may help with sources and presentation; they do not replace Vincent's legal work, and they are not the way to chase a citation Vincent already returned — for docket filings in particular, see **us-dockets**. Ask only for missing information needed to proceed, not for a complete intake or facts already supplied.

Respect explicit opt-outs, exclusive source requirements, and requests to use another provider instead. Preserve their stated scope on later turns: a conversation-wide opt-out remains active until the user changes it, even when an earlier result came from Vincent. If the chosen provider is unavailable, do not silently substitute Vincent. Automatic routing does not bypass tool approvals or confidentiality restrictions; report any actual permission blocker separately from skill selection.

Route by intent, not legal keywords. Developing or testing Vincent, fixing a citation parser, and building a contract-review interface are software tasks, not legal work. Formatting, converting, or copyediting a local document without legal analysis belongs with the relevant document tools.

Use the plugin's `vincent` MCP server. Discover its tools when needed; their names may have a host namespace prefix. Do not describe an answer as Vincent's work unless a Vincent tool returned it. For an unavailable connection or upload failure, read [local-connection.md](references/local-connection.md) and report the specific blocker instead of silently substituting another service.

## Which skill

| The user wants | Skill |
| --- | --- |
| A case, statute or document found or read; a legal question researched or answered; a citation checked | **clio-research** |
| What was actually filed in a **US** court — real cases, a judge's or party's record, what a complaint pleaded or an order held | **us-dockets** |
| The same questions answered across **many** documents — a collection, a matter's files, several files uploaded together | **tabular-review** |
| Something written: a memo, letter, clause, agreement; or an earlier draft revised or exported | **drafting** |
| The firm's own records — a matter's status or parties, what is due, what is scheduled, time and bills, logged calls, or a phrase inside its documents | **clio-manage** |
| **One** document of theirs read, reviewed or summarised | no extra skill — send it with `attach_document` and ask, per **Files in** below. Add **drafting** when the output is itself a document, or **clio-research** to check its citations |

More than one can apply — a doctrinal question paired with "and how have courts actually handled it" is clio-research *and* us-dockets. Load both rather than picking one.

## Lookup or reasoning

Decide this before anything else, because it is the difference between seconds and minutes.

A request for **documents** — does a case exist, find the statute, read this decision — is `search_legal_documents` / `get_legal_document`: one round trip, no conversation.

A request for **reasoning** — a question answered, something drafted, reviewed or argued — is `start_research`, which takes minutes because the agent searches for itself.

Starting a conversation for a lookup wastes both. Details in **clio-research**.

## Driving a turn

Call `start_research` with the question and applicable jurisdiction, locale, scope, and verified file IDs. Retain `conversation_id`. It returns promptly and renders Vincent's live MCP App inline in the parent conversation; the panel refreshes the transcript while Vincent works.

`start_research`, `continue_conversation`, `watch_conversation`, `respond_to_interruption`, `submit_tasks` and `get_conversation_messages` all share `TurnResult`. Read `state` and `guidance`:

| State | Next action |
| --- | --- |
| `completed` | Present the actual `answer`. If the deliverable is in `files`, retrieve it as **drafting** describes. If neither contains the requested result, report the empty outcome. |
| `needs_user` | Handle each returned `interruptions` entry using [interruptions.md](references/interruptions.md). Stop waiting for completion while human input is required. |
| `still_running` | The inline Vincent panel continues the run in real time. Do **not** call `watch_conversation` automatically, because it blocks the parent turn. Call it only when the user asks for the final answer in chat or the host cannot render the inline app. Do not create a duplicate conversation. |
| `error` | Report `error` as a failure, not an answer. |

Turn calls stream progress and may stay open for minutes. `watch_conversation` also exposes external-tool requests that a snapshot cannot. Use `get_conversation_messages` for a status spot-check, after resolving an interruption, or to read an earlier conversation; it is not the default polling loop. `get_conversation_metadata` contains no answer.

Keep the conversation ID when a wait must end, and report pending status without presenting partial text as finished work.

## One conversation, not several

A follow-up, revision, different perspective or new deliverable based on earlier Vincent work is `continue_conversation` on the **same** `conversation_id` — never a fresh `start_research`. The documents, review tables and answers from earlier turns live in that conversation and are not reachable from a new one.

A 409 means a turn is already running: `watch_conversation` until it settles, not repeated submissions. An uncertain create/continue timeout does not prove failure; recover using the known ID rather than replaying the mutation. Call `stop_conversation` only when the user asks to stop, then read what Vincent retained — `stopped=false` means there was nothing running to cancel.

## Scope

There is no workflow to choose. Every conversation the MCP starts runs on Vincent's agentic agent, which plans and picks its own tools; `start_research` takes no `workflow` argument and no tool lists workflows. If the user names a specific Vincent workflow, say it is not reachable from here and put the work in `question` instead — do not claim an access restriction, and never bypass authentication, feature flags, or approval controls.

Carry the user's question, facts, supplied text, requested output, and relevant date into `question`; do not reduce a drafting or review request to a generic research question. Pass the country code as `jurisdiction` and put any material state, province, or other jurisdiction in the question. Do not infer jurisdiction from the user's location.

Use `list_collections` when the user names a collection or matter, or needs to discover sources. Pass only returned or user-provided IDs. For a named collection search, use the known `collection_type`, keep `per_page=100`, and advance `page` while `has_more` is true until found. Project collections require an explicit `collection_type="project"` filter. When browsing, show the returned page and `total` before offering more; the displayed count is not the total. Keep collection and matter scope explicit and do not add unrelated client material.

`collection_id` is more than a research filter: it is what connects the corpus a review table draws its rows from. See **tabular-review**.

Discover `list_approval_keys` only when pre-approvals are relevant; grant only the specific capabilities the user authorized, and tell them the corresponding labels.

## Files in

Send a document with `attach_document`: read the bytes yourself, pass them base64-encoded, and always pass `size_bytes` — that is how a truncated argument is caught instead of uploading a corrupt fragment. There is no upload card.

Then branch on the result, because the account decides which upload path is open. A `file_id` means the document stands alone: poll `get_file_status` until `available`, then pass the id to `start_research(file_ids=[...])` or `match_authority`. A `conversation_id` means the legacy path, where the document only exists *inside* that conversation: continue it with `continue_conversation` rather than starting a run, and do not offer `match_authority`, which needs a file_id. `guidance` states which happened.

On the legacy path there are two shapes of request, and you choose by whether you pass `conversation_id`:

| The document is | Call | What happens |
| --- | --- | --- |
| New to this work — "here is my contract" | `attach_document` with no `conversation_id` | It opens a conversation of its own |
| One more file for a run already going | `attach_document` with that `conversation_id` | It joins that conversation, no turn spent |

Attaching asks nothing either way: `continue_conversation` is what puts the question. Do not `start_research` on a conversation an attachment opened — that starts a second one and leaves the document behind. When the attachment is the thing opening the conversation, pass the user's `locale` too: it is fixed at creation and no later turn can change it.

An attachment in this chat is not automatically in Vincent. Send only what the user asked you to send, and for a file too large for a tool argument, ask them to upload through Vincent and give you the id.

For an uploaded or user-provided Vincent `file_id`, call `get_file_status`. Only `available` or `completed` means usable; report pending or error states. Keep IDs within the same backend/account. Pass verified IDs to `start_research(file_ids=[...])` or `continue_conversation(file_ids=[...])`.

## Handling what comes back

Preserve returned citations, pinpoints, quotations, and links. Separate Vincent's conclusions from your synthesis and the user's facts. Do not invent sources, claim to have read uninspected text, or label an authority current or good law without supporting verification. Ask targeted follow-ups when support is incomplete and disclose unresolved gaps.

Send only documents and facts authorized for this task. Vincent uses remote storage and services regardless of which transport this plugin is configured for. Creating research or a draft does not authorize sending it to others, filing it, changing access, or modifying unrelated matters.
