# Goalz for ChatGPT and Codex

This portable Agent Plugins package connects to the OAuth-protected Goalz MCP endpoint at `https://www.goalz.de/mcp/apps`. It uses Client ID Metadata Documents (CIMD), which avoids putting a client secret or user credential in this package. The authorization resource is pinned to the same exact URL as the MCP endpoint.

This OpenAI package requests the seven reviewed gameplay scopes: `manager:read`, `manager:manage`, `club:read`, `club:manage`, `transfers:write`, `messages:read`, and `messages:write`. The full set is requested because Goalz filters `tools/list` by the scopes granted to the connection; a read-only grant would hide gameplay tools that need writes. The browser consent screen must show the requested scopes, and the user can decline. No administrative scope is requested. Each tool still uses only its server-declared scope requirements, and Goalz checks the active manager, resource, expiry, and effective scopes on every call.

For a read-only connection, replace the `baseScopes` array in `mcp.json` with this list and reconnect:

```json
["manager:read", "club:read"]
```

Goalz will expose only tools supported by those granted rights. If writes are later wanted, request a new authorization with the required scopes; this package does not promise incremental authorization.

The included skill explains safe account setup, reads, writes, public messages, and Wappen previews in English with German examples. Wappen generation stays available, may use quota or incur cost, and leaves the result private until the manager separately accepts it.

The manifest supplies the documented `Entertainment` directory category, five positive and three
negative expected review cases, and release notes for portal import. These cases have not been run
in an OpenAI host. A real walkthrough recording and a dedicated reviewer account are still needed
before review submission. The recording URL is omitted until available; reviewer credentials and
sign-in instructions belong in the secure dashboard form and are not included in this package.

Read <https://www.goalz.de/agenten.php#einrichten> for setup, <https://www.goalz.de/agenten.php#datenschutz> for privacy, and <https://www.goalz.de/agenten.php#nutzung> for use terms. Public user support is available at <mailto:support@goalz.de> or <https://www.goalz.de/agenten.php#support>. Publisher and marketplace contact: <mailto:apps@goalz.de>.

This package contains no local server, executable hook, shell command, static credential, or backend source. The Goalz logo and marks are reserved; see `NOTICE.md`.
