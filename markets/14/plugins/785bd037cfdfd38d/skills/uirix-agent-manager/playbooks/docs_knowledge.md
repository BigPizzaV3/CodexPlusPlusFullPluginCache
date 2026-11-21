# The agent's knowledge from the owner's documents

Topic `docs_knowledge` · version 2026-10-03 · served by `uirix_guide({ "topic": "docs_knowledge" })`.

Keeping the agent in step with documents the business keeps elsewhere (Drive, Notion, a sheet): which documents help, adding them with a source_key so a re-sync replaces instead of duplicating, the paid refresh, and the loop back: questions the agent could not answer become work on the documents.

```
GUIDE docs_knowledge: the agent's knowledge from the owner's documents

GOAL
The agent answers from the business's current documents, not from last quarter's. A document the owner keeps elsewhere is one document in the agent's knowledge, replaced on every sync, and the questions customers asked that the agent could not answer come back as a list of what the documents still lack.

FACTS THAT MISLEAD
- The agent reads the knowledge SUMMARY in every conversation, not the documents. add_document stores and parses; only reindex_kb (paid) puts the new text into the summary. Until then the agent answers from the old summary.
- Adding the same text again without a source_key adds another document: three syncs, three copies, the old prices still in the knowledge. With source_key the previous document of that key is replaced (replaced_doc_id in the answer).
- A source_key is a stable name for the SOURCE, not for the text: the document's id in the owner's app, or a name the owner will keep ("pricing-sheet").
- keep_verbatim true keeps a text exactly as written in the prompt (a price list, an exact answer); the flag carries over to the replacement unless the request sets it.
- The knowledge summary has a size the agent can carry; many long documents compete for it. Prefer the pages customers ask about.
- A question the agent could not answer shows in the conversation (an evasive or wrong answer) and, when the site search ran, in the briefing's tool problems (site searches without result). There is no "unanswered questions" list beyond that.

READ FIRST
- get_agent_setup and get_kb_summary: what the agent knows today, in the owner's words.
- list_documents: the documents it has, their status, which carry a source_key.
- get_briefing(period this_week or last_7_days): unresolved conversations, site searches without result; get_conversation on a few to see what was asked.

ASK
1. Which document (or page or sheet) in which app, and what it is for the customer (prices, hours, procedure, FAQ).
2. The key to use (propose the document's id or a plain name) and whether to keep it as written.
3. How often it changes, so the sync can become a routine.

APPLY: a document into the knowledge
1. Read the document from the owner's app. Judge it: customer-facing facts in, internal notes out. Say what you leave out and why.
2. add_document with title, the text (plain, headings kept), source_key = the chosen key, keep_verbatim true for lists of facts that must be exact. The answer names replaced_doc_id when a previous version went.
3. Ask for the refresh: reindex_kb (paid) after the owner's yes; poll get_kb_status until pending_sources is 0 and the summary version moved.
4. Read get_kb_summary and check the new facts are in it, in the agent's words. A fact that did not make it: update_kb_summary with the correction, or shorten the document.
5. Report: what changed in the knowledge, in two lines.

APPLY: the loop back, what the documents lack
1. From get_briefing and the unresolved conversations: the questions customers asked that got no answer. Group them by topic.
2. Search the owner's documents (in this chat) for each topic. Found: propose the passage as a knowledge addition (step APPLY above). Not found: a to-do line for the owner, "the documents do not say X; customers asked N times".
3. Write the to-do where the owner keeps such things (a note in the document app, a task, a message) only when asked; otherwise present it in the chat.

APPLY: make it repeat
Offer a routine (routines playbook): weekly, read the document, compare with the agent's version (list_documents shows the date), add_document with the same source_key when it changed, and ask the owner for the refresh. The routine never pays: it prepares and asks.

VERIFY
- list_documents shows ONE document per source_key, the new one, status indexed.
- get_kb_status shows the summary refreshed; get_kb_summary carries the new facts.
- A test question through test_chat on the changed fact, when the owner wants certainty (billed like chat).

MONEY
Paid, explicit yes first: reindex_kb (the refresh). Metered like a chat: test_chat. Free: get_agent_setup, get_kb_summary, list_documents, add_document, get_kb_status, get_briefing, get_conversation, update_kb_summary, uirix_guide.

MISTAKES TO PREVENT
- Syncing a document again without its source_key.
- A key that changes with the title or the date: the old version stays.
- Internal documents (salaries, passwords, drafts) pushed into customer-facing knowledge.
- Reporting "the agent now knows it" before the refresh ran and the summary moved.
- Running the paid refresh from a routine without a yes.

STOP WHEN
The agent's knowledge holds one current copy of each synced document, the refresh ran, the summary says the new facts, and the owner has the list of what the documents still lack.
```
