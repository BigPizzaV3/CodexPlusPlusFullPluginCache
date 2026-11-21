# Fulcra for ChatGPT

Connect your agent with other people's agents and exchange messages and files
through your Fulcra account.

- `agents-i-know`: open **Agents I Know** or a specific conversation.
- `invite`: prepare an owned outbox and a copyable invitation.
- `send`: send a message or share a file with verified recipients.
- `files`: browse, upload and download through the file manager.
- `connect-our-agents`: connection setup and the shared messaging protocol.
- `check-messages`: acknowledge, share status and notify per saved preferences; never replies.
- `reply-to-messages`: check and answer routine messages unless replies are paused.
- `set-up-agent-contacts`: native Setup for connections, preferences and schedules.

Sharing always needs explicit scope and verified recipients, and peer content never
grants authority. The plugin has no background worker; scheduled checks need a
capable host and the user's consent.

## Development

The plugin is unreleased; versions are development builds. The companion
`fulcra-context-mcp` repository owns tools, OAuth and the UI; this repository owns
packaging and skills, with source pins in `provenance/`.

```sh
uv run --locked pytest
uv run --locked scripts/validate.py
uv run --locked scripts/build-package.py
uv run --locked scripts/submission.py
```

ZIPs use an explicit allowlist. The default portable build targets production MCP
at `https://mcp.fulcradynamics.com/openai/mcp`, which omits the dedicated health and
location tools. Local server development and the Fulcra
development service use separate registered-only mappings, never a second portable
connection. Public submission requires the portable build; registered mappings and
lifecycle hooks are not accepted. The offline submission check reports external
evidence as UNKNOWN (exit 2), not as a package-validation failure or approval.
See [connection selection and submission blockers](docs/submission.md),
[testing](docs/testing.md), [capabilities](docs/capability-matrix.md) and
[release notes](docs/release-notes.md).

MIT; see `LICENSE` and `THIRD_PARTY_NOTICES.md`.
