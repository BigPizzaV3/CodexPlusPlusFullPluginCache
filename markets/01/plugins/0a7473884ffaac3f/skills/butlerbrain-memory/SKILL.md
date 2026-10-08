---
name: butlerbrain-memory
description: Remember, save, and recall things for the user. Use when they say "remember this", "save this", "what do I know about", "search my brain", or reference earlier conversations, notes, documents, people, or their calendar. Searches and grows their ButlerBrain semantic memory.
---

# ButlerBrain: Semantic Memory

ButlerBrain gives this conversation a persistent memory. The user's brain stores their notes, saved thoughts, web pages, documents, imported conversations, and calendar events, and retrieves them by meaning rather than exact keywords. The connection is already authenticated through the plugin: no setup, keys, or configuration are needed here. Your job is to search the brain when it could inform an answer, and to save what the user wants remembered.

## The user's owner name

Every item in a brain is attributed to an owner name, a short label the user established when they set up their brain (often a first name in lowercase). Some brains are shared by a family or team, with one owner name per person.

- If you do not know the user's owner name, ask once ("What owner name do you use in your brain?") and reuse it for the rest of the conversation.
- Pass it as `owner` on every write tool. It is required for saves.
- Pass it as `requesting_owner` on every read tool so the user's own private items are included in results.
- Never guess an owner name from message content. Names mentioned in a question are search terms, not owners.

Here, this plugin serves the one person in this conversation. The owner name they give you when you ask once IS your configured identity for this session: treat it exactly as a configured identity and keep passing it as `requesting_owner` on every read. The shared-agent guidance in "Identity vs. search filters" below, about never adopting an identity and staying shared-only, applies to multi-user agent deployments, not to this conversation.

## When to search the brain

Search without being asked when:

- The user references a prior conversation: "as we discussed", "what did I tell you about", "remember when I asked you about". Users can import their past ChatGPT conversations into their brain, so earlier chats may be searchable even when you cannot see them in this session.
- The user asks "what do I know about X" or "do I have anything on X".
- The user mentions a person, project, or topic by name that might be in their brain.
- Context from their saved knowledge would meaningfully improve your answer.

Phrase queries semantically. Describe the content you want in natural language ("notes about the kitchen renovation budget") rather than a bare keyword. If a search comes back empty, rephrase with different wording before concluding the content is not there.

## Read tools

### search_brain(query, table?, limit?, owner?, requesting_owner?, sort?)

Semantic search across the brain.

**Table options:** `vault` (Obsidian notes), `web` (crawled pages), `docs` (documents and imported conversations), `thoughts` (saved thoughts), `all` (search everywhere, the default; includes calendar events). For date-range calendar questions, prefer `get_events`.

- `limit` (optional): max results, default 10. The parameter is named `limit`, not `top_k`.
- `owner` (optional, content filter): narrows results to content authored by that owner. It does NOT grant access to private items, and you should never infer it from names mentioned in the query. Omit it for general retrieval.
- `requesting_owner` (optional, identity claim): the user's own owner name. Pass it on every search so their private items are visible.
- `sort` (optional): `"relevance"` (default) returns the best semantic matches first. `"recency"` returns the same matches ordered most-recent-first by the content's original date (for example the original conversation date for imported chats), falling back to the date it was added. Use `"recency"` when the user asks for their latest or most recent items.

### get_context(topic, limit?, owner?, requesting_owner?, sort?)

Use for breadth: a gathered view of what the brain knows about a topic across all sources, rather than a narrow lookup. Reach for it on "what do I know about X" and open-ended background questions. Same `owner`, `requesting_owner`, `limit`, and `sort` semantics as `search_brain`.

### get_person(name, limit?, owner?, requesting_owner?)

Look up everything the brain knows about a person. Searches all tables with both semantic and literal name matching. Use for "what do we know about [name]" and before answering questions that hinge on a person's preferences or details.

### get_events(date?, range?, owner?, requesting_owner?)

Calendar queries: "what do I have today / this week / this month". `range` is `"day"` (default), `"week"`, or `"month"`; `date` defaults to today. Pass `requesting_owner` so the user's private events are included.

## Identity vs. search filters

The `owner` and `requesting_owner` parameters are different:

- `owner` is a **SEARCH FILTER**. It narrows results to content authored by that owner. It does **NOT** grant access to private items. Example use: "find Chris's grocery lists" means `search_brain(query="grocery", owner="chris")`.

- `requesting_owner` is an **IDENTITY CLAIM**. Set this to the human user's identity if you (the AI) are configured for a specific user. Private items owned by this identity become visible. Example: if you are Lily's personal AI, always pass `requesting_owner="lily"` on every read call.

If you are a shared AI agent with no specific user identity (e.g., a family agent that multiple humans chat with): do **NOT** pass `requesting_owner`. You will see only shared items. This is by design. It prevents accidentally exposing one family member's private content to another family member in the same chat session.

If you are configured for a specific user: always pass `requesting_owner` as that user's owner identifier on every read call. Never guess based on conversational context. Use your configured identity only.

The `search_brain` tool returns:
- All shared items matching the query
- If `requesting_owner` is set: the current owner's own private items matching the query
- If `requesting_owner` is set: a `hidden_private_count` field indicating how many OTHER owners' private items matched but were withheld

If `requesting_owner` is unset, `hidden_private_count` is **omitted entirely**. You made no identity claim, so there is nothing withheld "from you" to surface.

If `hidden_private_count > 0`, do NOT treat this as an error or missing data. It is working as designed: other family members have private items matching the query and you are correctly not seeing them. You can mention this to the user if relevant: "I found 3 shared results. Other family members have 2 private items matching this query that I can't access."

## Write tools

### save_thought(text, owner, tags?, private?)

Use when the user says "remember this", "save this", "note that", or wants information stored. Both `text` and `owner` are required.

Short thoughts come back with `{"stored": true, ...}` once the chunks are written. Document-sized pastes come back with `{"status": "queued", "chunks": N, ...}` and are processed in the background. Confirm the save to the user and let them know the content will be searchable shortly.

### crawl_and_save(url, owner, tags?, private?)

Use when the user shares a URL and wants it saved. Both `url` and `owner` are required. The crawl runs in the background.

**What the crawler can read.** It reads public web pages: articles, blog posts, docs, public product pages. It cannot read pages that show a sign-in wall, an app/workspace screen, or an AI-chat share link (for example a ChatGPT or Claude `share` or project link): those return only the sign-in chrome, so nothing is saved and you get an error back. When that happens, tell the user to import the source or upload it as a file instead.

### add_event(title, start_time, owner, end_time?, location?, recurrence?, tags?, notes?, private?)

Schedule events. `title`, `start_time` (ISO 8601), and `owner` are required. Recurrence patterns: `"daily"`, `"weekly:mon,wed,fri"`, `"monthly:15"`, `"yearly:03-15"`. Use `delete_event(event_id)` to cancel one; deleting a recurring event removes all future instances.

### Documents

For document content the user wants remembered in this chat, the paths that work directly here:

- A document on the public web: `crawl_and_save` with its URL. PDFs are detected automatically.
- Text the user pasted or attached that you can read: save the full text via `save_thought`.
- A scanned or image-only document: read it directly (you are multimodal) and save the full transcription via `save_thought`, noting it was transcribed.

**Save documents verbatim by default.** When the user wants a pasted or attached document remembered, save the full text word for word with `save_thought`. Do not condense, paraphrase, or summarize unless the user explicitly asks for a summary. Always include a provenance note naming the source document (for example `"(from attached PDF: <filename>)"`).

**Never pass a chat attachment's file path to any tool.** Files the user attaches in the chat exist only in the chat environment. A local or sandbox path (for example `/mnt/data/report.pdf`) is not a storage key: passing it as `s3_key` or as any other tool argument will always be rejected, and nothing is saved. Do not retry with a different path. Instead, read the attachment directly (you can read files and images) and save its full text with `save_thought`.

**The upload pipeline (`get_upload_url` then `ingest_pdf`) turns on one question: can you read the user's local file and perform an HTTP PUT?**

- If yes (agent runtimes, scripts, sessions with code execution): call `get_upload_url` to receive a temporary upload URL (valid for 5 minutes) plus the `s3_key`, PUT the file's bytes to that URL yourself, then call `ingest_pdf` with the `s3_key` to index it. The upload is not complete until `ingest_pdf` is called.
- If no (chat-only assistants with no file access or HTTP): do not call `get_upload_url` and do not attempt or offer the upload. Tell the user to upload the file through the Import tab of their dashboard at https://butlerbrain.ai/dashboard. For text you can read directly, save it verbatim with `save_thought` instead.

Both tools return these same two branches in their responses, so if you already called one and cannot complete the PUT, follow the second branch.

A chat attachment is never an upload: for any document attached in this chat, read it and save the full text verbatim with `save_thought`, as above.

## Async saves: be patient

Crawls, document ingests, and long saves are queued and processed in the background. A `"queued"` response means the save was accepted, not that it failed. Confirm the save to the user. If they immediately ask to verify, wait briefly before searching, and if the content has not appeared yet, retry the search shortly rather than concluding the save failed.

## Private items

Private items are visible only to the owner who saved them. Other people in a shared brain cannot see them.

Watch for these user intents:
- "Save this privately"
- "Don't share this with [other family member]"
- "Keep this between us"
- "Just for me" / "private note"
- Anything about medical appointments, gifts for family members, personal finances, or therapy
- Calendar events the user describes as "doctor," "therapy," or that they explicitly flag as sensitive

When the user's intent is clear, add `private: true` to the tool call. When it's ambiguous, ask: "Would you like to save this privately so only you can see it?"

All write tools accept an optional `private` parameter:

- `save_thought(text=..., private=true)`
- `add_event(title=..., private=true, ...)`
- `crawl_and_save(url=..., private=true)`
- `ingest_pdf(s3_key=..., private=true)`

Default is `false` (shared with all owners in the brain). Pass `true` to mark the item private to the current owner only.

For users with Obsidian syncing to ButlerBrain, vault files are marked private in two ways (the user controls this in Obsidian, not you):

1. Placing the file under a folder named exactly `private` at any level of the path (e.g. `Health/private/medical.md`). Folder names like `Private Notes` or `MyPrivate` do **not** match.
2. Adding `private: true` to the file's frontmatter:

   ```
   ---
   private: true
   ---
   # Note content...
   ```

Either trigger is sufficient. If a user asks how to make Obsidian notes private, recommend the frontmatter approach. It keeps their folder structure intact.

ButlerBrain operates on a "shared brain = shared trust" model. Owners in the same brain can see each other's shared content by default. That is the family-brain value proposition. Private is an explicit opt-in for individual sensitive items. For true isolation, the user should create a separate brain, not rely on private flags alone.

Private enforcement is a social-contract boundary, not a cryptographic one. The backend trusts the AI client's `requesting_owner` claim. A well-behaved client configured for a specific user always claims that user's identity. A shared client without per-user identity always leaves `requesting_owner` unset and sees only shared content.

## Tagging

Include 2 to 4 tags whenever calling `save_thought` or `crawl_and_save`. Tags improve retrieval and later filtering. Common categories: household, calendar, work, projects, school, activities, family, health, finance, people, food, ideas, learning, web. Prefer specific tags over generic ones.

## Saving people and relationships

When someone mentions a person with context worth remembering (preferences, relationships, contact info, important details), use `save_thought` with person-specific tags. Don't ask "should I save this?". If it is clearly personal context about someone, just save it.

**Tag format:** Always include `"person"` as the first tag, then the person's lowercase name, then descriptive tags.

**Examples:**

| User says | save_thought text | tags |
|---|---|---|
| "John loves sushi" | `John loves sushi` | `["person", "john", "food", "preferences"]` |
| "Sarah's birthday is March 15" | `Sarah's birthday is March 15` | `["person", "sarah", "birthday"]` |
| "My boss Dave prefers email over Slack" | `Dave prefers email over Slack for communication` | `["person", "dave", "work", "communication"]` |
| "Mom's new address is 123 Oak St" | `Mom's new address is 123 Oak St` | `["person", "mom", "contact", "address"]` |

**Retrieving person info:** Use `get_person` to look up everything the brain knows about someone. It searches across ALL tables (thoughts, vault, web, docs, and calendar) for mentions of that person, using both semantic and literal name matching.

The combination of `save_thought` with person tags for storage and `get_person` for retrieval gives you a living address book that grows naturally from conversation. Over time, asking "what do we know about Sarah?" returns her birthday, preferences, work details, and anything else that's been saved.

## Past ChatGPT conversations

Users can import their ChatGPT conversation history into their brain from the ButlerBrain dashboard (Dashboard, then Import). Imported conversations become searchable documents in the `docs` table, dated by their original conversation date.

- When the user references something from an earlier chat you cannot see, search the brain: `search_brain` with `table: "all"` or `table: "docs"`.
- For "my latest conversations" or "what was I working on recently", pass `sort: "recency"`.
- If the user asks whether they can bring their history in, point them to the Import tab on their ButlerBrain dashboard at butlerbrain.ai.

## When to save

**Save:**
- Anything the user explicitly says to save, note, or remember
- Shared URLs when the content is substantive (article, doc, reference)
- Decisions, conclusions, or outcomes of a conversation
- Grocery lists, task lists, or to-dos when asked

**Don't save:**
- Casual chitchat or greetings
- Content the user is just sharing for a reaction (memes, jokes)
- Redundant information already in the brain (check first if unsure)
- Login pages, one-time links, or ephemeral URLs
- The AI's own responses (save user content, not your output)

## Presenting results

| Indicator | Source |
|-----------|--------|
| 📝 | Note or Obsidian vault (`vault`) |
| 🌐 | Web page (`web`) |
| 📄 | Document or imported conversation (`docs`) |
| 💭 | Saved thought (`thoughts`) |
| 📅 | Calendar event (`calendar`) |

Format results as a brief summary with the source indicator. If results are sparse or below confidence threshold, say so honestly rather than fabricating context.

## Decision guide

| User says... | Use tool |
|---|---|
| "Search for / find / look up / what do I know about X" | `search_brain` |
| "What did we discuss before / in an earlier chat" | `search_brain` (`table: "all"`, consider `sort: "recency"`) |
| "Remember / save / note / store this" | `save_thought` |
| "Save this link / article / page / URL" | `crawl_and_save` |
| "Save this document" (public URL) | `crawl_and_save` |
| "Save this document" (pasted or scanned) | Read it, then `save_thought` with the full text verbatim |
| "Schedule / add to calendar / I have a meeting" | `add_event` |
| "What's on my calendar / what do I have today/this week" | `get_events` |
| "Cancel / delete [event]" | `delete_event` |
| "What do you know about X / give me context on X" | `get_context` |
| "What do we know about [person] / look up [name]" | `get_person` |
