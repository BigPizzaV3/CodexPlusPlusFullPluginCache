---
name: 3chat-customer-growth
description: Use 3Chat for startup guidance; finding, segmenting, or analyzing customers and their one-to-one conversations; preparing or sending explicitly confirmed customer messages and attachments; and tracking customer batch sends. Guide missing setup steps without configuring Agents or channels.
---

# 3Chat Customer Growth

Use this skill to work with customer records and one-to-one communication in the connected international 3Chat workspace at app.3chat.ai.

## Dependency

Use the MCP server named `3chat-customer-growth`. Use only its exposed tools and parameters in the live `inputSchema`.

## Available Tools

- `get_3chat_workspace_readiness`: Read historical Agent-publication and channel-connection milestones; guide missing setup steps.
- `search_3chat_customers`: Find customers by supported standard fields, custom fields, and latest inquiry time.
- `search_3chat_conversations`: Filter and page one-to-one conversation entities; no message details.
- `search_3chat_customers_context`: Read customer memory, conversations, messages, custom fields, and optional `agent_logs`.
- `upload_3chat_attachment`: Upload a file when no valid final download URL is available.
- `send_3chat_customer_message`: Send a confirmed message to one customer.
- `send_3chat_customer_messages`: Create a confirmed customer batch-send task.
- `get_3chat_batch_send_status`: Read progress and item results for a customer batch task.

## Startup Guidance

Use [references/startup-readiness.md](references/startup-readiness.md) for triggers, result reuse, and rechecks. A request such as "How do I start managing customers with 3Chat?" is a usage-guidance request; do not search customers merely to answer it.

When `ACTION_REQUIRED` first needs guidance, read that reference before answering. If both milestones are missing, include the product capability and reason to set up, three quick-start steps, and an improvement suggestion. If only one is missing, show that step only. Present each step's explanation followed by a prominent named link using [references/guidance-links.md](references/guidance-links.md). Keep the declared onboarding skill as the host's setup entry point.

Reuse `READY` within this conversation, without claiming current operational availability. After `ACTION_REQUIRED`, recheck on a later 3Chat-dependent user turn, when the user reports setup progress, or when they ask to refresh. Check at most once per assistant turn or business workflow. Respect a request to postpone setup. Never treat readiness as permission to send.

## Core Rules

1. Classify the request before selecting tools: setup, customer search, conversation search, context retrieval, analysis, drafting, sending, or task tracking.
2. Use canonical customer and conversation IDs from tool results, not display names or invented identifiers.
3. Keep multiple matches for lists and analysis. Ask the user to choose only when the next action requires one customer and the target is ambiguous.
4. Before any send, show the recipients, sender account or channel, final content, attachments, and scope, then obtain explicit confirmation. Drafting and audience selection do not authorize sending.
5. Use an existing final HTTP/HTTPS download URL only if it needs no authentication or custom headers and is not a preview or redirect-only URL. Otherwise upload and prefer reusing the complete `data.attachment`.
6. After a batch returns `job_id`, query that job; do not recreate the batch.
7. Follow structured errors and `aiAction`. Retry a send only when explicitly permitted, with identical business parameters and the original idempotency key.
8. Separate returned facts from inference. Do not equate `accepted`, `sent`, or `COMPLETED` with delivery or read status. Do not expose raw JSON by default.

## Detailed Guidance

- Startup milestones and rechecks: [references/startup-readiness.md](references/startup-readiness.md).
- Setup link presentation: [references/guidance-links.md](references/guidance-links.md).
- Customer filters and communication context: [references/customer-intelligence.md](references/customer-intelligence.md).
- Conversation search: [references/conversation-search.md](references/conversation-search.md).
- Before uploading or sending: [references/outbound-messaging.md](references/outbound-messaging.md).
- No data, partial results, errors, and retries: [references/errors-and-retries.md](references/errors-and-retries.md).
- End-to-end examples: [references/use-cases.md](references/use-cases.md).

## Current Boundary

Use only the eight tools above for customer one-to-one workflows. The plugin can guide setup but cannot configure an Agent or connect a channel for the user. Current business eligibility is validated by the relevant tool. Do not claim customer-record updates, campaign or scheduling objects, internal channel lookup, or server-side aggregate analytics not exposed by these tools.
