---
name: ai-receptionist
description: Review InsertChat AI receptionist phone conversations, identify callers needing follow-up, and prepare callback briefs or replies from the recorded conversation. Use for receptionist call reviews and customer handoffs in a connected InsertChat workspace.
---

# Review your AI receptionist

Use the user's selected assistant when supplied. Otherwise `get_front_desk_brief` with `channel: "voice"` covers the accessible workspace; it does not require picking an assistant first. Queue counts describe current inbox state, not calls received today or missed calls.

For a named caller or a broader call-history request, use `list_agents` to resolve the assistant, then `search_conversations` with `channel: "voice"` and the relevant query or queue. Use returned IDs. Continue with `next_cursor` as `cursor`, preserving filters, when the requested coverage needs more results. State when a result is only a sample.

Read selected calls using `get_conversation`, passing each row's `agent_uid` and `uid` as `conversation_uid`. Prepare a concise handoff with the caller's request, commitments actually recorded, unanswered questions, and the next action. Cite the returned `app_path` as an InsertChat link under `https://app.insertchat.com`. Use contact details from the result; owners and admins can also use `list_contacts` and `get_contact` for a recorded inquiry.

Distinguish a suggested callback from a scheduled or completed callback. The tools cannot place calls, book appointments, change routing or hours, or send messages. A conversation marked urgent or needing help is not evidence of a missed call. Missing transcripts and truncated previews are not evidence that no request was made.

When asked for a reply, return a draft. If `draft_reply` and the relevant view navigation tools are available, open the chosen conversation and place the draft in its composer for review. Otherwise provide the draft in chat and the conversation link. Finish with the concrete handoff or draft the user requested, not an unsolicited setup flow.
