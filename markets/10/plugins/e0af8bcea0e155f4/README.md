# Asking MCP

**English** | [Português (BR)](./README.pt-BR.md)
[![smithery badge](https://smithery.ai/badge/askinghq/asking-mcp)](https://smithery.ai/servers/askinghq/asking-mcp)

Plugin that connects AI assistants (Claude, ChatGPT, Cursor, VS Code and other
MCP-compatible clients) to your customer support in
[Asking](https://asking.com.br) through MCP.

With your permission, the assistant reads conversations, messages, contacts and
the reports your role allows, adds private notes and reply drafts, and updates
status, priority, labels and assignee. When the connection includes the send
scope, it also replies to and starts conversations on your behalf — always with
per-scope consent, audit records and instant revocation.

## Server

- URL (Streamable HTTP): `https://app.asking.com.br/mcp`
- Authentication: OAuth with scopes `mcp:read`, `mcp:write` and `mcp:send`

## How to connect

1. In your client, add a remote MCP server with the URL above.
2. The browser opens the Asking consent page — sign in with your usual account
   (email or Google).
3. If you belong to more than one account, select the account to connect.
4. Review the scopes and approve. Depending on the client, the first tool call
   is what opens the browser consent.

Menus and names vary between clients and versions; look for the option to add a
remote MCP server or a custom connector.

### Claude

Open **Settings > Connectors**, add a custom connector and paste
`https://app.asking.com.br/mcp`. Complete the consent in the browser.

### ChatGPT

Open **Settings > Connectors** and create a custom connector with the URL.
Custom connectors depend on your plan and on the rollout; if the option is not
available in your account, connection is not possible yet.

### Cursor

Open **Settings > MCP**, add a new MCP server, choose the HTTP option and paste
the URL. You can also add it to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "asking": {
      "url": "https://app.asking.com.br/mcp"
    }
  }
}
```

### VS Code

Open the Command Palette and run **MCP: Add Server**, choose **HTTP** and paste
the URL. You can also add it to `.vscode/mcp.json`:

```json
{
  "servers": {
    "asking": {
      "type": "http",
      "url": "https://app.asking.com.br/mcp"
    }
  }
}
```

### Claude Code

Add the server from the terminal:

```bash
claude mcp add asking --transport http https://app.asking.com.br/mcp
```

### Codex

Add the server from the terminal:

```bash
codex mcp add asking --url https://app.asking.com.br/mcp
```

### Other clients

Any MCP client that supports the Streamable HTTP transport can connect to the
URL above; the exact menu names vary by client.

## Documentation

Full setup guide and per-plan limits:
<https://docs.asking.com.br/hc/asking-documentation/articles/asking-connect-ai-assistants-via-mcp>

## License

MIT — see [LICENSE](./LICENSE).
