---
name: orpinn-action-history
description: Read the current connection's real Orpinn action history and status, explain pending or failed work, and route a requested undo through a fresh exact preview and browser approval.
---

# Orpinn action history

Use advertised `list_ai_actions` with bounded pagination or `get_ai_action` with an actual returned action ID. Results belong to the current authenticated account/connection and live branch grant. Do not invent action IDs, retrieve another account's journal or infer success from a user's description.

`prepared` means awaiting approval; `queued`/`processing` mean pending; `failed`, `expired` and `canceled` are not successful writes. Only `committed` confirms server execution. It does not prove a POS device received the update. `undone` means the original action has been compensated by a separately recorded undo.

For an explicitly requested eligible undo, use the matching operation's advertised prepare-undo tool with the original committed action ID. Show the NEW exact preview and wait for its own authenticated browser click. Never reuse the original card or approval, bypass a stale version, claim undo after its returned expiry, or create a replacement forward action to imitate failed undo. Archived records retain business history.

If history, scope or a particular action is unavailable, report that limit explicitly. Do not say an action completed because its preparation, upload, comparison or approval succeeded.
