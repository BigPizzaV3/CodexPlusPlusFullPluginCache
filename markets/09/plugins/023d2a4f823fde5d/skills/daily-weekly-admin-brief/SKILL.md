    ---
    name: daily-weekly-admin-brief
    description: Produce a concise daily or weekly operating brief from 33CRM. Use when a company admin asks what happened today, this week, yesterday, or over a short operating window and wants sales, bookings, marketing, pipeline, and conversation signals in one brief.
    ---

    Use this skill for short recurring operating briefs.

Period handling:
1. If the user says today, use today's UTC calendar date as both date bounds where supported.
2. If the user says yesterday, use yesterday as both bounds.
3. If the user says this week or weekly, use the requested calendar week when clear; otherwise use the most recent 7 days and say so.
4. If the user asks for a comparison, call the same report tools for the immediately preceding equal-length period.

Core tools:
- `sales_summary`
- `get_sales_report`
- `get_booking_report`
- `get_marketing_report`
- `get_conversation_report`
- `pipeline_summary` when a current pipeline snapshot is useful

Output:
- Period covered
- What changed / what happened
- Sales and lead pulse
- Bookings and attendance
- Marketing pulse
- Conversation workload
- Current pipeline snapshot when relevant
- 3-5 attention items based only on observed data

Rules:
- Reply in the user's language.
- Distinguish current snapshots from period metrics.
- Do not treat booked value as revenue or current amount paid as period cash flow.
- Do not claim causation between Meta spend and CRM conversion unless the returned data directly supports it.
- Do not read or summarize conversation content; only operational metadata is available.
- If data is empty, stale, or pagination-limited, say so explicitly.
- Read-only workflow; never claim to create, assign, send, book, or modify anything.
