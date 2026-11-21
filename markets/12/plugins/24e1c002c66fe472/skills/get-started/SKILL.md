---
name: moa-get-started
description: How to use the moa connector well: find a meeting first, answer from its notes, quote the transcript only when asked, never invent decisions.
---

# Working with moa

moa holds the user's recorded meetings as **notes** (summary, decisions, to-dos with owners and due labels, related people and topics, moa's own remarks during the meeting) and **transcripts** (who said what, with timestamps). Notes are in the language the meeting was held in.

## Find the meeting first
- "Yesterday", "this week", "the last one": call `list_meetings` and pick by date.
- A topic, a person, a phrase: call `search_meetings` (every word must match, as a prefix). If nothing matches, say so; do not guess.
- Then `get_meeting` for the notes. Call `get_transcript` only when the user asks what was said, wants a quote, or the notes do not answer.

## Answer from the notes
- Quote decisions and to-dos as written. Keep owners and due labels exactly ("Mia · Friday").
- When several meetings are involved, say which meeting each point came from and link it (`url` in the results).
- For "what do I know about X", use `list_wiki_pages` and `get_wiki_page`; the wiki already gathers X across meetings.

## What the connector cannot do
- It is read-only. Meetings, notes and connections are managed in the moa app on iPhone.
- It reads only the connected account's backed-up meetings. Other people's meetings are not reachable.
- If a tool returns "The token is not valid", tell the user to reconnect moa.
