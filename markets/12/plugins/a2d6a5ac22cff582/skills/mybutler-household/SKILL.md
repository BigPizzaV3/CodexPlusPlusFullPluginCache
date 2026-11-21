---
name: mybutler-household
description: Use the connected MyButlerDid.it v2 MCP operations for authenticated household memory, lists, tasks, important dates and decisions, respecting access controls.
---

# MyButlerDid.it — OpenAI v2 review skill

This skill applies **only** to the explicit-tool OpenAI review endpoint `/mcp/openai-v2`. It does not describe the wider Butler product or other MCP surfaces.

ChatGPT handles conversation, reasoning and source interpretation. Butler stores and retrieves authorised household state. Call only tools that actually appear in the connected server's `tools/list`; never call or emulate old multi-action Butler routers.

## Available operations

- Household: `get_household`.
- Memory: `find_memory`, `remember`, `update_memory`, `forget_memory`.
- Lists: `create_list`, `get_list`, `add_list_item`, `complete_list_item`.
- Tasks and reminders: `get_tasks`, `create_scheduled_task`, `complete_task`.
- Important dates: `get_important_dates`, `create_important_date`.
- Decisions: `get_decisions`, `record_decision`.
- Existing Pages and notifications: `get_shared_spaces`, `get_notifications` (read only).

Follow each tool's actual declared argument schema. Do not fabricate required values or substitute one operation for another. Resolve an existing object before editing/completing it if identity is ambiguous.

## Review-surface limitations

This v2 catalogue **does not** offer watch creation or checking, recommendation gateway links, profile bootstrap, a general workflow router, Pages creation/editing/sharing, household sharing/visibility changes, purchases, messaging or other external transactions. If requested, explain that the connected review surface cannot execute the operation and do not claim success. Do not call `butler_go`, `butler_memory`, `butler_lists`, `butler_tasks`, `butler_dates`, `butler_decisions` or any other legacy `butler_*` router.

## Privacy and accuracy

Work only within the authenticated user's authorised household/member visibility; a `not found or not accessible` response is a completed read, not permission to broaden searching. Never ask for government identifiers, credentials, or secrets for review. Do not widen visibility or infer private records from another household. Use only genuinely verified facts; clarify uncertain consequential dates. Store only structured durable outcomes when the user intends a save, and confirm a write only after the tool reports success.

Use natural, concise responses. Do not expose database IDs or tool-routing details in ordinary answers. Read `references/workflows.md` and `references/acceptance-prompts.md` for examples scoped to these 18 operations.
