---
name: verde-memory
description: Use when the user wants to save, find, update, or publish their team's shared knowledge in Verde — decisions, conventions, project facts, processes, lessons — or asks a question about their own team's projects, decisions, or history that Verde's memory should answer. Not for general-knowledge questions, calendar or scheduling tasks, or storing passwords, keys, or other secrets.
---

# Verde — recall, save, and keep team knowledge current

Verde is the team's persistent, shared memory, reached through the Verde plugin's tools. A **vault** belongs to a team and holds **buckets** (folders); buckets hold **documents**. Every document carries a visibility: **public** (on the open internet once published), **company** (the whole team), or **private** (the signed-in user only). A document may be narrower than its bucket, never wider.

Tools: `list_vaults`, `list_buckets`, `create_bucket`, `search_memories`, `get_memory`, `list_recent_memories` (read); `propose_memory`, `update_memory`, `supersede_memory`, `archive_memory`, `publish_memory` (write). Every tool takes `vault` as a `team/vault` slug from `list_vaults`.

## Facts you must not infer

- **Which vault or bucket** — always take it from `list_vaults` / `list_buckets`.
- **That something is not in Verde** — only `search_memories` can establish that.
- **Dates** — convert "next Friday" to the real date before saving.
- **That the user wants a public document published** — only an explicit approval in this conversation, after seeing the exact text, counts.

## Workflow 1 — Recall (a question about the team's projects, decisions, conventions, or history)

1. `search_memories` with a natural-language `query`. Add `include_historical: true` when the user asks how something changed or what it used to be.
2. Results carry short excerpts, `status`, `is_current`, and a `url`. Pick the relevant hits and fetch full text with `get_memory` — pass several ids in `ids` in one call. Follow `references` / `referenced_by` ids the same way when they matter.
3. Answer from the documents. Name the document title, say when it was last updated, and distinguish the current version from superseded history explicitly ("current: $29/seat; superseded: $19/seat").
4. Share the `url` when the person would want to open the document itself (a design doc, decision record, plan). Skip it for a one-line fact.
5. If nothing relevant exists, say so plainly. Once the user settles the answer in conversation, offer to save it (Workflow 2).

Where a document contradicts your own assumption, the document wins. Where the document is clearly stale, say so and offer to supersede it (Workflow 3).

## Workflow 2 — Save (the user states something durable, or asks to remember it)

Durable = a decision and its reasoning, a stable preference or convention, a project fact, constraint, or deadline, a correction of a previous belief, a process or fix that worked.

1. **Get agreement.** Offer in one line ("Save this to Verde?") and wait for a yes — unless the user already asked Verde to save or remember it.
2. **Check for duplicates.** `search_memories` for the topic. If a document already covers it, switch to Workflow 3 instead of creating a second one.
3. **Place it.** `list_vaults`, then `list_buckets` for the vault. Choose the bucket whose topic matches. Call `create_bucket` only when nothing fits; it returns an existing bucket when a similar name already exists.
4. **Draft one document per fact** using [references/memory-template.md](references/memory-template.md): a declarative title that states the fact, a body with the fact, why it matters, and how to apply it, absolute dates, a `type`, `tags`, and `source_description`. Split compound updates into separate documents. Write `[[Exact Title]]` in the body to cross-reference another document.
5. **Call `propose_memory`.** Leave `visibility` at the bucket's default unless the user asked for narrower. If the bucket is public, the result is a **draft** — tell the user it is not live and that publishing is a separate confirmed step (Workflow 4).
6. **Report** in one or two lines: title, bucket, visibility, and status (draft or published). No link needed for routine saves.

If a prompt supplies the exact title and body, use them verbatim; do not ask clarifying questions.

## Workflow 3 — Keep it current

- Wrong or incomplete wording, refreshed tags or metadata → `update_memory`. Pass the `expected_version` you received from `get_memory` so you never overwrite someone else's newer edit. Readers see only the new text; the prior text is retained as a revision.
- The knowledge itself **changed** (a new price, a reversed decision, a replaced process) → `supersede_memory` with `old_memory_id`. Both documents stay in history and link to each other. Prefer this whenever the previous state matters.
- Obsolete with no replacement → `archive_memory`. It is retained and recoverable, just out of normal retrieval.

Before touching a document that is **published public**, tell the user that editing it changes its public web page immediately and archiving it removes the page immediately, and get their go-ahead.

## Workflow 4 — Publish a public document (only when the user asks)

1. `get_memory` the draft and show the user its exact title and full body.
2. Ask for explicit approval to put that text on the open internet.
3. Only after a clear yes in this conversation: `publish_memory` with `confirm_public: true`. Without the flag the tool refuses and nothing is published — that is the intended safeguard, not an error to work around.
4. Company and private drafts publish with a plain `publish_memory` call; they are visible only to signed-in members.

Superseding a public document always produces a draft; take it live with the same confirmed step.

## Never

- Save passwords, API keys, tokens, or other credentials — decline and explain that secrets do not belong in shared knowledge.
- Save transient session details, speculation stated as fact, or anything the user asked to keep off the record.
- Put personal or private information in a company or public bucket.
- Publish a public document, or edit or archive a live public one, on your own initiative.
- Duplicate a document that already exists — search first, then update or supersede.

## When to stop and ask

Ask before acting when the bucket is ambiguous between two reasonable choices, when a save would change visibility, or when a document you found looks stale but the user has not confirmed what replaced it. Otherwise proceed and report what you did.
