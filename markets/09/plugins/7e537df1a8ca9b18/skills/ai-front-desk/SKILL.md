---
name: ai-front-desk
description: Prepare an InsertChat AI front desk briefing, triage conversations needing human attention, inspect leads, draft customer follow-ups, and review monthly performance. Use for shared-inbox handovers and frontdesk operations across customer channels.
---

# Run your front desk review

Start with `get_front_desk_brief` for a workspace briefing. Omit `agent_uid` to cover every assistant the user can access, or supply the verified ID for an explicitly selected assistant. Use `channel` only when requested (`web`, `voice`, `whatsapp`, `email`, or `sms`). The first page includes queue totals; later cursor pages omit counts. Reuse the first-page totals rather than treating omitted counts as zero.

Explain which conversations need attention and link to their returned `app_path` under `https://app.insertchat.com`. Counts overlap: urgent and unassigned may include the same conversation, so do not sum queues. These are current inbox counts, not a daily activity report. If `has_more`, continue with `next_cursor` as `cursor` and unchanged filters when needed for the requested coverage; otherwise label the listed items as a selection.

For a specific request, use `search_conversations` with its query, queue, channel, or `contact_uid`. This tool needs an assistant: resolve it using `list_agents` or use the user's configured default. Read selected conversations with `get_conversation` before summarizing or drafting. Preserve each result's assistant ID; never apply one assistant's ID to another assistant's conversation.

For a lead or callback, owners and admins can search `list_contacts` and read `get_contact` for the submitted inquiry. Use its `agent_uid` and `contact_uid` with `search_conversations` to review context. Identify missing information rather than inventing customer details, deadlines, prices, or appointments. A draft is not a sent message. Place it with `draft_reply` only when the host exposes that view tool; otherwise return the text and conversation link for the user to review and send.

For performance, use `get_report_summary` with the requested month and year. It requires an owner/admin and analytics access. Compare periods only after reading each requested period and preserve the returned period and scope. Do not extrapolate resolution or satisfaction from a few conversations. If access is denied, report which part is unavailable and continue the authorized inbox task.

Deliver the requested brief, lead summary, draft, or comparison. Open the workspace with `open_insertchat` when the user wants to act there; do not interrupt an existing task with onboarding or preference questions.
