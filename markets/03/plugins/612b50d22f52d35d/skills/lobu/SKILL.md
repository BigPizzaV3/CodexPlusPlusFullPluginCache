---
name: lobu
description: Use Lobu for durable, permission-aware workspace context, authorized connected data, governed actions, and human approvals. Trigger when the user asks what their workspace knows, wants to preserve a durable fact or decision, needs to query an authorized source, or asks Lobu to preview or perform an action.
---

# Lobu

Use Lobu for shared context that must survive one conversation, agent, or local workspace. Treat memory as durable append-only system events; keep temporary reasoning and scratch work outside Lobu.

## Choose the smallest safe tool path

1. Use `search_memory` for existing workspace knowledge.
2. Use `save_memory` only when the user wants a fact, decision, preference, note, or observation preserved. Search first; supersede stale facts instead of duplicating or overwriting history.
3. Use `search_sdk` before choosing an SDK method or connector operation. Never guess method names, identifiers, arguments, readiness, or returned URLs.
4. Use `query_sdk` or `query_sql` for read-only work.
5. Use `run_sdk` only for requested mutations or connector actions. Prefer `dry_run=true` when it can prove the intended change without executing it.

Stay within the identity, workspace, permissions, and connection readiness Lobu returns. Never request or expose connector credentials, and never claim an action completed from a preview or pending run.

## Approvals and rendered actions

When Lobu returns a pending approval, use `get_approval` with that exact run ID to render the canonical review card. Do not bypass the card or infer approval. `resolve_approval` may authorize an external or irreversible action, so use it only for the user's explicit approve or reject choice on that exact review card.

Use `invoke_event_action` only for an interaction declared by a rendered Lobu template and initiated by the user. It records the validated interaction as an append-only, idempotent workspace event; it is not a substitute for executing an external connector action.

If authorization, approval, or device readiness blocks the requested operation, report the exact waiting state and the safe next step.
