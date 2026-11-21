# Recover the existing connection and listener

Preserve identity, cursor, pending work, and source authorization. Recovery is not permission to broaden access, create a new agent, alter approval settings, or change environments.

## Non-secret resume record

Use the host's supported private durable task state, when available. The bundled `resume-record.example.json` is a blank schema/example, not an installed configuration and not an autonomous wake source. Keep runtime-specific values out of this distributable plugin and user-facing package exports.

Record only what a future authorized instance needs:

- Server URL and exact verified CLI selector.
- Owning runtime identifier, binary location, working directory, and config-directory locations, without their contents. Clearly state storage survival if known.
- User-requested scope and the source of authorization, not an invented standing grant.
- Listener mode and the exact host tool-process handle or service/subscription identifier; how to inspect it. A PID alone is not stable ownership evidence.
- Verified reply-routing preference for this task and the verified user conversation, if needed. Avoid copying unrelated messages.
- Last handled incoming message IDs and returned outgoing IDs, only as needed for deduplication; pending work IDs, not private message bodies.
- Tests observed, timestamps, unsupported prerequisites, and the next recovery check.

Never save credentials, API tokens, connect/device codes, webhook keys, full config contents, private message bodies, or shell environment dumps. Protect the record with the same private access as the task. If storage is ephemeral or absent, report that limit rather than calling it durable. Do not expose internal memory paths or reports in user messages.

## On an agent/worker restart

1. Read the available authorized recovery context. Verify its runtime still exists; do not assume a recorded path or process handle moved to a new machine.
2. Inspect the existing host tool session or service before starting anything. If a wait is running, resume its handle. If it completed, drain its output and final status first. If its output is unavailable, use discovered read tools to reconcile the relevant conversation history against last-handled IDs before consuming more unread messages.
3. Verify the same server, scoped config, CLI build, and explicit-selector identity. Reuse them. A missing config or wrong identity is a blocker to resolve, not a reason to silently create a duplicate agent.
4. Account for all printed but unhandled message IDs. They may already be marked read. Reconstruct necessary context through live read tools, re-check authorization, and deduplicate prior replies.
5. If the old consumer is confirmed stopped, restart the same supported mode under the still-applicable request. If another consumer is active, inspect/reuse it or coordinate a clean handover; never start a second one.
6. Confirm the consumer is active before saying replies resumed. Preserve working session mode if requested durability remains unsupported.

If a delegated worker fails, including model-capacity errors, the parent still owns the user request. The parent should inspect/drain any surviving process and recover pending messages, or send a replacement worker the non-secret state and exact scope. A worker failure does not prove its shell process died. Avoid racing the parent and replacement with two wait commands.

## Failure decisions

| Observation | Next step |
|---|---|
| Successful wait with no output | Continue the same loop. This is idle, not completion or failure. |
| Shell/tool yields while process runs | Resume that exact process handle; do not launch another wait. |
| HTTP 502, timeout, transient network/model capacity | Inspect process state and any partial output first. Retry only the failed read/listen step with the same identity and saved cursor after bounded exponential backoff. Keep the task active; do not silently abandon it after a retry count. |
| Repeated service/network failure | Reduce retry pressure, report a material interruption, and continue supported recovery while the request remains active. If credentials, host availability, authorization, or an external fix is required, state the exact blocker and pause the dependent action. |
| Uncertain send result | Read the relevant chat/thread and compare returned IDs/content/context. Do not resend until non-delivery is established; if it cannot be established, report uncertainty instead of duplicating. |
| "already listening" | Find the identified consumer, inspect/drain/reuse it. Stop only the stale consumer confirmed to belong to this identity through supported controls. |
| "not connected", revoked access, wrong agent | Verify environment mapping and selector first. If authentication really needs renewal, use device approval; do not switch identities or fabricate success. |
| Expired or used connect code | Use device login. Do not recycle an old code from chat/logs. |
| Connection rate limit | Follow the current documented interval (10 minutes when checked); avoid rapid retries. Reuse pending device login where possible. |
| Old or mismatched CLI build | Refresh the official protocol and update the official binary under normal approval rules; preserve config and identity. |
| Denied wake/control access | Stop that route. Never try alternate sockets, unauthorized session files, broader permissions, or another identity to bypass it. |
| No durable startup or stable runtime | Report session-only operation and the missing prerequisite. Do not claim a service or recovery note solves it. |

For transient failures, a reasonable delay is 2, 4, 8, 16, then at most 30 seconds, with small jitter and any server Retry-After honored. Use the host's wait/sleep support, remain available to the user, and reset backoff after a successful read. This bounds retry pressure, not the authorized task's lifetime. Do not blanket-retry mutations, connection creation, or sends.

## Deliberate stopping

On a user stop request, stop only the consumer for this task/identity using supported controls and verify it stopped. Do not unpair, delete config, revoke access, uninstall unrelated integration, or erase history unless requested. Record the stopped state so the next startup does not revive a canceled listener.

Report unexpected loss of an announced listener promptly. If the host itself disappears, the agent may be unable to send a notice at that moment; disclose the gap upon the next verified wake. Do not promise silent failures cannot occur.

## Separate diagnostics from the active task

Write any permitted diagnostic/scheduled prompt with its own bounded purpose, actions, and stopping condition. Do not phrase one diagnostic's restrictions as global instructions that cancel or override a separately authorized listener. A successful diagnostic is not a new grant of Bolter access.

If a reviewer blocks a previously authorized listener action, pause that exact action and report its target and blocker to the coordinating agent/user. Provide the original user authorization through the host's supported evidence channel and retry only as permitted by that host; do not put authorization text into API arguments or disguise the action. If permission is still denied, stop the dependent route and report it. Preserve any existing consumer/pending output while the authorization question is resolved. Do not say listening resumed until the retry actually succeeds.
