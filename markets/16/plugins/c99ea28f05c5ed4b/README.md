# Binto plugins for AI assistants

Read your Binto Operations records from the assistant you already use. Ask what needs attention across your Locations, find a document or permit by a Location's name or address, or look up when a piece of equipment was last serviced.

- **Read-only.** The assistant can read records; it cannot change anything in Binto.
- **Your access, nothing more.** You sign in to Binto in your browser and approve the connection. The assistant sees only the Organizations, Locations and records you can open yourself.
- **No passwords or keys to copy.** Sign-in uses OAuth. Disconnect at any time from the assistant.

The server is `https://binto.ai/api/mcp` (Model Context Protocol, Streamable HTTP).

## What is in this repository

| Path | For |
| --- | --- |
| `.claude-plugin/marketplace.json` | The Claude Code marketplace named `binto` |
| `plugins/binto-operations/` | The Claude plugin: `.claude-plugin/plugin.json`, `.mcp.json`, `skills/`, its own README and LICENSE |
| `.agents/plugins/marketplace.json` | The Codex marketplace named `binto` |
| `plugin.json`, `mcp.json`, `skills/`, `assets/` | The ChatGPT and Codex plugin (this repository's root), in the portable Agent Plugins format |

The two `skills/` folders hold the same three skills and must stay identical:

- `attention-across-locations`: what needs attention across your Locations
- `find-document-or-permit`: find a document or permit at a Location by address or name
- `equipment-service-history`: when equipment was serviced, what was done and what it cost

## Install

### Claude Code

```text
/plugin marketplace add binto-app/binto-plugins
/plugin install binto-operations@binto
/mcp
```

`/mcp` lists `binto`. Choose it, then **Authenticate**: your browser opens Binto, you sign in and choose **Continue**.

Without the plugin, add the server on its own:

```bash
claude mcp add --transport http binto https://binto.ai/api/mcp
```

### claude.ai and the Claude desktop app

1. Open **Settings**, then **Connectors**.
2. Choose **Add custom connector**.
3. Name it `Binto` and paste `https://binto.ai/api/mcp`.
4. Choose **Connect**, sign in to Binto and choose **Continue**.

### ChatGPT

1. Open [ChatGPT Plugins](https://chatgpt.com/plugins).
2. Choose the plus button, then **Add custom MCP server**.
3. Name it `Binto`, paste `https://binto.ai/api/mcp`, and choose **OAuth** for authentication.
4. Read the warning, continue, then sign in to Binto and choose **Continue**.

### Codex

With the plugin:

```bash
codex plugin marketplace add binto-app/binto-plugins
codex plugin add binto-operations@binto
```

Or add the server directly in `~/.codex/config.toml`:

```toml
[mcp_servers.binto]
url = "https://binto.ai/api/mcp"
```

```bash
codex mcp login binto
```

## Try it

- "What needs attention across my Locations this week?"
- "Find the health permit for the Main Street Location. When does it expire?"
- "When was the walk-in cooler at Maple Street Market last serviced, and what did it cost?"

If your account belongs to more than one Organization, the assistant asks which one you mean.

## Disconnect

Removing the connector or plugin stops your assistant from calling Binto. It does not by itself end the access Binto granted: that ends when the assistant revokes its token, or when the token runs out.

- **Sign out in the assistant first.** An assistant may revoke its token when you disconnect or clear the sign-in (in Claude Code: `/mcp`, choose `binto`, then clear authentication). Do this before you remove the plugin. Binto cannot confirm from here that an assistant did so.
- **If you are not sure it was revoked,** change your Binto password. That signs out every connected app at once, including the Binto mobile app, and you sign in again where you still want access.
- **Left alone, access runs out on its own.** An access token lasts 15 minutes. The sign-in behind it ends 30 days after the assistant last used it, and 90 days after you approved it at the latest.

Developers can revoke a token directly (RFC 7009). `client_id` is the assistant's client id, and `token` is its access or refresh token:

```bash
curl -X POST https://binto.ai/api/oauth/revoke \
  -d "client_id=https://claude.ai/oauth/claude-code-client-metadata" \
  -d "token=$BINTO_OAUTH_TOKEN"
```

Set `BINTO_OAUTH_TOKEN` to the access or refresh token first.

Revoking either token ends that whole sign-in.

## Help, privacy and terms

- Help: https://binto.ai/contact
- Privacy Policy: https://binto.ai/privacy
- Terms of Service: https://binto.ai/terms

## License

The manifests and skills in this repository are released under the MIT License. See `LICENSE`. Binto itself, and the server at `https://binto.ai/api/mcp`, are not covered by it.
