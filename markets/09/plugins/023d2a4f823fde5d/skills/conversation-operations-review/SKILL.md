    ---
    name: conversation-operations-review
    description: Review 33CRM conversation workload by channel and operational status, including active, waiting, escalated, resolved, timestamps, and message counters. Use for inbox workload, escalation volume, channel mix, stale-conversation checks, or conversation operations.
    ---

    Use this skill for conversation operations, not conversation-content analysis.

Workflow:
1. Resolve the period.
2. Call `get_conversation_report` for volume by current channel and status for conversations created in the window.
3. Call `list_conversations` for operational records filtered by channel, status, or activity dates.
4. Call `get_conversation` for one conversation's metadata and total/inbound/outbound/per-sender counters.
5. Use pagination when needed.

Output:
- Conversation volume
- Channel mix
- Status mix
- Escalated / waiting workload
- Specific conversation counters when requested
- Operational attention items
- Caveats

Rules:
- Never claim to have read message text: message bodies, attachments, and media are not returned.
- Current status is an as-of snapshot and may differ from status during the requested window.
- Do not infer customer intent, medical information, sentiment beyond the explicit stored field, or content not returned.
- Reply in the user's language.
- Read-only only.
