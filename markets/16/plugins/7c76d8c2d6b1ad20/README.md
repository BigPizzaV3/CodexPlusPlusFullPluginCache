# Meeting Follow-Up Assistant

A skills-only plugin that turns meeting transcripts, notes, agendas, and discussion records into accurate summaries, decisions, action items, responsibilities, deadlines, unresolved issues, and sendable drafts.

It runs inside the assistant and requires no MCP server, API key, OAuth, database, custom backend, or meeting-platform integration. It analyzes content the user supplies; it does not join or record meetings, send messages, create tasks in other apps, or claim to store meeting data.

## Core promise

Every decision, owner, deadline, commitment, and next step must be supported by the supplied meeting content. Suggestions stay suggestions, questions stay questions, and uncertain details remain clearly marked.

## Validation examples

- “I’ll send the proposal by Friday” produces a supported action with that speaker as owner and the original deadline phrase preserved.
- “We should check analytics” produces an unassigned action only when the context makes it an agreed task; otherwise it remains a discussion point or open question.
- “Maybe we should switch plans” is not a confirmed decision.
- When a meeting later moves a confirmed Tuesday launch to Thursday, use Thursday and note the change if relevant.
- Client-ready output omits internal-only discussion unless the user explicitly asks to include it.
