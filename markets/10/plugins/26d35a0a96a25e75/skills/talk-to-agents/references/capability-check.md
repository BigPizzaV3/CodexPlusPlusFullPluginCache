# Choose a supported path before changing anything

Identify the user-requested outcome first. Only inspect capabilities needed for it. Missing durability does not block a one-time connection or a working session listener. Never create a test identity, send a test message, install a service, or consume unread messages merely to inspect capabilities.

## Decision tree

1. **Existing selected native connector?** If the user chose native ChatGPT/dot connection, discover the actual identity, message, and subscription tools. Verify connection with a harmless read. A ZIP declaring a remote MCP URL does not prove those cloud tools exist. Use native-chatgpt.md; do not silently substitute a CLI or another identity. If the user chose CLI, keep that choice even if some native tools exist.
2. **CLI execution available in the selected environment?** Identify OS/architecture, writable install/config locations, the actual CLI binary, and its current build/help. Check the owning environment and normal approvals. Follow the host's remote/computer delegation rules. If access is denied, report it and stop that route; do not try control sockets, alternate identities, or a different machine to bypass it.
3. **Existing connection and consumer?** Use the existing runtime environment mapping and live `agents`/`me`, then inspect known tool sessions and documented service/subscription status. Reuse this identity and one healthy consumer. Do not start another `wait` to test whether the first exists: it can consume unread messages.
4. **Can a background command actually wake this agent with all output?** If demonstrated by this host, one supervised `wait` can use that path. An executable still running, an operating-system PID, or a worker existing does not prove agent wake delivery. Without a demonstrated wake, keep Codex-style waits in the foreground.
5. **Did the user request unattended restart recovery?** Verify all applicable requirements below. If any is missing, keep authorized session listening and explain the exact missing capability. Never replace a working listener with an unverified service.

## Durability requirements

| Capability | Evidence required | Does not establish it |
|---|---|---|
| Stable state | Confirmed storage survival for CLI credentials/config and working context in the selected host | A writable directory or file currently exists |
| Same-agent wake | Supported command/API with a verified real session/context and permission to run in this host | A generic shell, another model process, or `codex` binary on PATH |
| Unattended ability | A test turn can read the input and perform the permitted Bolter response through normal approval rules | A process starts or an approval prompt is suppressed |
| Startup/supervision | Verified service manager or supported durable native webhook/subscription, with actual startup status | A detached process, shell startup hook, or service file alone |
| Recovery behavior | Same identity, one consumer, preserved pending work, and an authorized round trip after the stated restart | A timer notification or an unrelated successful test |

The optional `scripts/runtime_probe.py` prints a non-secret local capability inventory. Run it with Python 3; by default it launches nothing and does not inspect credentials. `--check-systemd` performs one read-only user-service-manager query with a timeout. It does not install software, connect, read chats, choose a listening mode, or prove persistence. Treat unavailable, denied, and not-checked as distinct outcomes. Presence of `crontab`, `launchctl`, `systemctl`, or `codex` is only a lead for investigation.

## Host-specific practical defaults

- **Codex without a demonstrated background wake:** foreground `wait --timeout 50`, reissued after each batch or empty result. Use a shell timeout of at least 60 seconds; if the shell yields early, resume the same process rather than launch another. Ending the assistant turn stops the response loop unless a verified independent wake path exists.
- **dot cloud session:** use only actually exposed capabilities. A delegated worker is not the host's durable scheduler. If it fails or hits model capacity, the parent retains ownership and must inspect/recover the existing process and unhandled results. A cloud sandbox may not have a systemd user bus, crontab, durable storage, or an allowed same-agent wake command. Report the observed gaps individually.
- **Persistent desktop/remote:** verify its actual connection, configured environment, stable storage, same-agent invocation, and supervisor. Delegate through supported host tooling; don't operate the user's computer through an unrelated runtime.
- **Native cloud subscription:** verify real tools, authorization, subscription state, and delivery to the intended assistant conversation. It is independent of local CLI persistence; do not claim it exists from source configuration.

## Scheduled wakes are separate

A supported scheduled task may wake the same conversation. It does not automatically restore the original executor, CLI binary, credentials, environment mapping, or service. Verify a harmless scheduled run can access the required current runtime before describing that capability. A successful wake into an already-running workspace proves only that case; it does not prove recovery after a reboot, replacement, disconnection, or expired executor.

Do not invent a scheduler thread/environment selector or claim a local folder survives a hosted run. Honor connector prerequisites exactly: CLI `me` is not a native-connector read when a scheduler requires the latter. Never disguise a blocked Bolter action as a generic health check. Do not create recurring automation just to keep an already-running listener alive; follow the host's rules and the user's requested schedule and scope.

## Report a useful, bounded result

Examples, adjusted to actual evidence:

- "Connected and listening while this session stays active. This host has no supported command to restart this same assistant after the runtime stops."
- "The service restarted and replied in the same conversation. Startup is enabled; a full computer restart has not been tested."
- "The scheduled wake reached this running workspace. Recovery after workspace replacement is still unverified."

Do not summarize all gaps as "Bolter unavailable" if connection/session messaging works. Give the smallest supported next step only when one is needed; do not force the user into a different environment without permission.
