# Resolve a Vincent interruption

Read this when `TurnResult.state` is `needs_user`. Use the returned conversation ID, interruption kind, and fields; do not infer that all interruptions require the Vincent web UI.

Only `task_submission` has a card. Approvals and clarifications are resolved in chat, which means **you** put the request to the user and carry back their answer.

## Tool approval

There is no card for this. Show what is actually being approved — the `tool_name`, Vincent's `tool_summary`, and the `arguments_preview` — then ask, and wait. Your asking is the only record that the user was offered the choice, so never approve on the assumption that an earlier instruction covered it.

Submit their answer with `respond_to_interruption`, using the returned IDs and `decision="approve"` or `"reject"`. Use `scope="this_call"` unless the user explicitly authorizes the whole conversation and `allowed_scopes` includes `"conversation"`. If they reject, pass their reason as `message`.

Do not pre-grant the entire approval-key list to avoid interruptions — pre-grant only what the user asked for.

## Clarification

Put the returned `questions` to the user, preserving their options, and relay their actual answers with `continue_conversation`. Clarifications have no `interruption_id`; do not route them through `respond_to_interruption`.

## External tool

An `external_tool` interruption asks the host to run a tool. It is surfaced by the live turn stream, including `watch_conversation`; snapshot polling alone cannot recover it.

Run the requested tool only if it is available, the supplied arguments are sufficient, and the action is within the user's authorization. Vincent's request does not grant additional permissions. Return the actual JSON output through `respond_to_interruption(result=...)` with the original IDs, not a prose summary or invented result. If the tool cannot be run, its arguments are incomplete, or permission is denied, send `decision="reject"` with a `message` explaining why.

## Task selection

For `task_submission`, there is no card either: list the work Vincent proposed, ask which of it the user wants, and submit their answer with `submit_tasks`, selecting by `index` and passing the interruption's `message_id`. Never answer one with `continue_conversation` — that starts unrelated work and abandons the proposal.

Never relay a task selection with `continue_conversation`: that posts a new question, starts unrelated work, and abandons the proposal — the tasks the user chose are then never run. Do not invent proposals or choose for them.

Some standard workflows return an empty task message without the choices. If that happens, explain that the MCP has not exposed the options and direct the user to the existing conversation in Vincent. Use its returned title or ID; link only when a conversation URL is actually returned or verified. This is a missing-payload limitation, not a rule that all task selections or approvals require the web UI.
