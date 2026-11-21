# Knowledge: what the agent knows

Topic `knowledge` · version 2026-10-16 · served by `uirix_guide({ "topic": "knowledge" })`.

The knowledge of an agent: what it knows and what is missing, filling the gaps with the owner, adding a web page, a whole site or a pasted text, correcting a fact, and the paid refresh that makes added sources real. The knowledge summary is the only knowledge the agent uses.

```
GUIDE knowledge: what the agent knows

GOAL
The agent knows the true facts of the business and nothing invented: what customers ask about is in the knowledge summary, the gaps are known to the owner, and everything that was added is verified to be there.

FACTS THAT MISLEAD
- The knowledge summary is the ONLY knowledge the agent uses in a conversation, on every channel. A document that is "indexed" is stored, not known.
- Adding a document changes NOTHING the agent says until the summary is refreshed (reindex_kb). Nothing refreshes on its own, and until then the agent answers from the old summary.
- update_kb_summary REPLACES the whole text. Send the complete summary, never a part of it.
- A correction of the summary applies at once, on the next conversation. No refresh and no rebuild.
- A later refresh merges new sources into the summary. A fact that lives only in the summary can be lost then: save it as a document too.
- With no summary at all the agent answers from its instructions alone.
- When every source counts as waiting although a summary exists, the summary is older than the per source tracking: its coverage is unknown, not missing.

READ FIRST
- get_agent_setup(agent_id): the knowledge state: how many sources, whether some are waiting, the outline of the summary, its size, and the facts it marks as not found (the gaps).
- get_kb_summary: the text itself, in windows (max_characters up to 100000, offset, has_more). Search it for a topic and answer from it.
- list_documents: the sources, each with its status (processing, indexed, failed) and the reason of a failure.
- get_kb_status: the state of the summary (ready, out_of_date, not_built, absent), pending_sources, the version, the last refresh with its error, the last crawl with the pages that failed.

CHECKS
Start from the knowledge findings of get_agent_setup: sources with no summary, no knowledge at all, sources waiting, a summary older than its sources, facts marked as not found, a failed refresh, pages the crawl could not read, keep as is documents that do not fit in phone calls. Then add what a rule cannot see:
- A thin summary (under about 2,000 characters) for a real business.
- Questions the agent could not answer in recent conversations.
- The plan against the knowledge (knowledge.allowance of get_agent_setup, and the finding knowledge_room_left): how many pages the plan lets the crawl store and how many were crawled, how many files it allows and how many were uploaded. Room left on a thin knowledge is the recommendation to make: more pages of the website (add_document with mode "site" or "page"), or documents the owner holds (price list, procedures, FAQ). An allowance used up (knowledge_at_plan_limit) explains why adding more fails and points to the plan, in the dashboard.

RECOMMEND
- One fact to add or to fix: correct the summary (free, at once) and save the fact as a keep as is document so that it survives.
- A page, a site or a longer text: add it as a source, then the paid refresh.
- Wording that must stay exact (procedures, price lists, legal text): a text document with keep_verbatim true.
- A large change, such as a new line of business: after the refresh recommend a rebuild of the instructions (rebuild playbook).

ASK (one question per message)
What is missing or wrong? Where is the right information: a web page, a text to paste, or will the owner say it now? Only that page, or the whole site? Must the wording stay exact?

APPLY: what does the agent know
Answer from the summary, never from the list of documents. List the gaps. Say plainly when sources were added and are not in the summary yet.

APPLY: fill the gaps
Ask about the missing facts one at a time. NEVER invent an answer, and skip what the owner does not know. Then get_kb_summary with max_characters 100000 (every window), put each answer where its marker is, and save the same facts as a text document: add_document, keep_verbatim true, title "Owner facts" plus the date. Show the changed lines and, after a yes, send the COMPLETE summary back with update_kb_summary. A summary longer than 100,000 characters is not sent back: save the document only and offer the paid refresh.

APPLY: add a web page, a whole site or a pasted text
- The owner names a topic that lives on the website (the return policy, shipping, prices, opening hours): do NOT ask for the link. find_website_pages with the topic words, show the one or two pages that match, and add the right one with add_document(url, mode "page"). Ask for a link only when nothing matches or the site cannot be read.
- One page is the default. A site crawl (mode "site") is for a new agent or a site that changed everywhere; it is billed too: say so in one line and ask first.
- A text: add_document with title and text. Advise "keep as is" (keep_verbatim true) for anything the agent must quote exactly: policies, price lists, procedures, legal text, opening hours. Add "also in calls" (verbatim_in_calls true) only for the few texts a caller must hear word for word: without it the text is not on the phone; the phone prompt is small and drops what does not fit.
- A text that is kept elsewhere and synced again (a document of the owner's, a sheet, a CRM page): add_document with source_key, the owner's own stable name for that source ("pricing", a document id). The same key sent again REPLACES the previous document of that key on this agent (the answer names replaced_doc_id), so a source synced many times stays ONE document with the latest text. The language of a text defaults to the agent's; pass language when it differs.
- Every document starts "processing" and is not in the summary until the refresh below; the answer says so. A failure shows in list_documents with its reason.
- A document already added without the flags: set_document_verbatim.
- A document the agent should not know: an outdated or wrong page (another business, a cart or login page), an old file or a text that is no longer true: remove_page (pages doc_c, files and texts doc_f) after naming it and getting a yes; it cannot be undone.
- Then the refresh. It is paid: say so and get a yes before reindex_kb. NEVER run it on your own.

APPLY: correct a fact
get_kb_summary (the whole text), change only the passage concerned, show the change and, after a yes, send the COMPLETE summary back with update_kb_summary. Save the corrected fact as a keep as is document as well.

APPLY: refresh the knowledge now
reindex_kb adds every source not yet in the summary to it; the summary the agent has stays whole. It is paid and counts as a build in today's limits. It runs in the background: poll get_kb_status every 10 to 15 seconds until pending_sources is 0 and the version moved. Do not assume it finished; summary.last_job reports a failure. While one runs, a second reindex_kb answers kb_rebuild_in_progress: wait and poll, never call it again. A rebuild from scratch is the rebuild guide (from_step knowledge).

VERIFY
- After a refresh: find the new facts in get_kb_summary and quote two or three of them.
- After a correction: read the summary again and confirm the line.
- One test question on the channel the owner uses (test_chat, a billed turn) when the fact matters to customers.
- A failed document: say the reason from list_documents.

MONEY
Paid: reindex_kb (every refresh) and every test_chat turn. A whole site crawl is billed as well: one line, then the yes. Never name amounts or explain what is billed. Free: every read, update_kb_summary, a text or a single page saved with add_document. Every added document counts in the daily document limit (100 a day, in today's limits of get_account). One explicit yes per refresh.

MISTAKES TO PREVENT
- "Indexed" read as "the agent knows it".
- A part of the summary sent to update_kb_summary.
- A refresh without a yes, or "done" before the status says so.
- An invented answer to a gap.
- A price saved with no currency.
- A fact fixed in the summary only, and lost at the next refresh.

STOP WHEN
The facts the owner cared about are in the summary and verified, the remaining gaps are named, and no source is waiting unless the owner chose to postpone the paid refresh.
```
