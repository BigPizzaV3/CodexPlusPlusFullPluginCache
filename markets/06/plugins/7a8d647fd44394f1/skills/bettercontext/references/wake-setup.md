# Optional wake helper

Both editions bundle the helper and service setup. Installation is opt-in through
`wake_setup` or plugin-root `scripts/wake_service.py install --alias <alias>`.
Add `--check` to validate without writing or starting anything. The alias must
refer to an actual Codex task owned by this computer, with its real UUID and local
history available. Synthetic IDs support mailbox relay only.

Windows uses a hidden Python process in a per-user, limited-privilege Scheduled
Task. Linux uses a systemd user service; macOS uses a LaunchAgent. Python and a
Codex CLI with `codex queue` support must already be installed. No API key or
publisher-operated server is required. Linux/macOS service code must be verified
on those operating systems before claiming tested support.

Use `wake_status`; for CLI management use `wake_service.py status`, `start`,
`stop`, or `uninstall`. Uninstall removes the service registration and retains
memory, configuration and diagnostic logs. Disabling the plugin does not stop
the separately installed helper. It has its own runtime copy outside the plugin
cache; reinstall wake setup after updating the plugin to refresh that copy.

Setup pins each allowed alias to its current task UUID. It refuses a task owned
by another computer. The helper blocks a queued message whose recipient no longer
matches the pinned identity. It never grants wider task permissions. A legacy
private installation is detected and must be migrated deliberately so two
helpers do not deliver the same mailbox.

Wake requires the host, selected database/share, and Codex app-server to be
available. It does not wake a sleeping computer or create a remote web ChatGPT
connection. Each computer sharing a database installs its own helper for only
its local destination tasks. Ordinary registration never enables a service.

Delivery is pending until Codex accepts the queue request, delivered after that,
and read after the recipient acknowledges it. Timeout/interruption is uncertain
and is not automatically resent. Failed queue calls retry with backoff. Inspect
the destination before explicitly retrying an uncertain delivery; never test by
sending messages to live unrelated chats.
