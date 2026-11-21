# Connect Noxi to an AI assistant

Noxi is one remote MCP server: `https://mcp.noxi.ai/mcp`. Every host signs in
with OAuth on `auth.noxi.ai` (you log in to Noxi in the browser and approve
the access); no API key or token is ever pasted into a chat or a config file.

The public, localized version of these steps is <https://noxi.ai/connect>
(`/ar/connect` in Arabic); it is the documentation URL of the directory
listings, so keep the two in step.

| Host | How to connect | OAuth client |
| --- | --- | --- |
| Claude (claude.ai, desktop, mobile) | Settings → Connectors → Add custom connector → URL `https://mcp.noxi.ai/mcp` → Add → Connect, sign in to Noxi and approve. No client ID is typed. Once listed, Noxi is also in Claude's connector directory. | Claude's Client ID Metadata Document `https://claude.ai/oauth/mcp-oauth-client-metadata` |
| ChatGPT | Settings → Apps & Connectors → Advanced → Developer mode → Create → URL `https://mcp.noxi.ai/mcp`, authentication OAuth | ChatGPT's own client identity |
| Codex | Install the Noxi plugin from this repository marketplace (`plugins/noxi`) | `https://chatgpt.com/oauth/codex/client.json` |
| Cursor | `~/.cursor/mcp.json` entry below, then Settings → MCP → Noxi → Connect | `noxi-cursor` |
| Claude Code | `claude mcp add` command below, then `/mcp` → noxi → Authenticate | Claude Code's Client ID Metadata Document `https://claude.ai/oauth/claude-code-client-metadata`, sent by Claude Code itself |

## Cursor

The **Add to Cursor** button on <https://noxi.ai/connect> installs the same
entry through Cursor's MCP install deeplink
(`cursor://anysphere.cursor-deeplink/mcp/install?name=noxi&config=<base64 of the server entry>`,
see <https://cursor.com/docs/context/mcp/install-links>). By hand, add to
`~/.cursor/mcp.json` (or a project's `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "noxi": {
      "url": "https://mcp.noxi.ai/mcp",
      "auth": {
        "CLIENT_ID": "noxi-cursor",
        "scopes": ["openid", "email", "profile", "offline_access"]
      }
    }
  }
}
```

Cursor opens the browser for the Noxi sign-in and returns to its fixed local
callback (`http://localhost:8787/callback`); Cursor's web and cloud agents
return to `https://www.cursor.com/agents/mcp/oauth/callback`. Both are
registered for `noxi-cursor`, a public client with no client secret.

## Claude

The authorization server accepts Client ID Metadata Documents from the
reviewed host domains (`NOXI_OAUTH_CLIENT_ID_METADATA_DOCUMENTS=trusted_hosts`),
so Claude identifies itself and the connector needs only the server URL; leave
the advanced OAuth fields empty.

## Claude Code

```sh
claude mcp add --transport http noxi https://mcp.noxi.ai/mcp
```

Then run `/mcp`, choose `noxi` and authenticate in the browser. Claude Code
sends its own Client ID Metadata Document, so no `--client-id` is needed.

If sign-in stops with a client registration error (a client that does not
identify itself), name Claude Code's identity explicitly:

```sh
claude mcp remove noxi
claude mcp add --transport http noxi https://mcp.noxi.ai/mcp \
  --client-id https://claude.ai/oauth/claude-code-client-metadata
```

## What the connection can do

The consent screen lists the exact actions: read presentations and templates,
create presentations, edit presentations and export them. A connection stays active for
up to a year while it is used at least once a month, and can be disconnected
from the host at any time.
