# Installing Lukka Digital Assets Intel

## Requirements

- A supported ChatGPT or Codex plugin host and permission to connect MCP tools
  in your workspace.
- A Lukka account with access to the products needed for your requests.
- Browser access to complete Lukka OAuth sign-in.
- For local large-data processors, a supported execution environment with
  Python 3.10 or later and a verified way to capture or export the response.

Request Lukka access at [lukka.tech/plugin](https://lukka.tech/plugin/).
Contact [plugin-support@lukka.global](mailto:plugin-support@lukka.global) for
account or product-access problems.

## Public-directory installation

These steps apply **after the OpenAI edition has been approved and published**.
The current preparation does not establish a public listing.

1. Open **Plugins** in ChatGPT or the ChatGPT desktop app's Codex surface.
2. Find **Lukka Digital Assets Intel**, open its details and select the install button.
3. Connect Lukka when prompted and complete sign-in at `https://auth0.lukka.tech`.
4. Start a new conversation so the installed skills and tools are available.
5. Ask: "Resolve BTC and ETH and show their latest available USD prices,
   including sources and timestamps."

In Codex CLI, use `/plugins` to open the plugin browser. Install from an
available marketplace and start a new session. The IDE extension currently
does not support plugins. See
[OpenAI's installation guide](https://learn.chatgpt.com/docs/plugins).

## Development: connect Global MCP in ChatGPT

An MCP development connection lets you inspect and exercise the server's tools.
It does not by itself install the 21 bundled skills.

Use the custom MCP creation flow available to your account. In the
**New Plugin** form used for this integration, enter:

| Setting | Value |
|---|---|
| Name | `Lukka Global MCP` |
| Server URL | `https://global.mcp.lukka.tech` |
| Authentication | OAuth |
| OAuth client registration | Dynamic Client Registration (DCR) |
| Authorization server base | `https://auth0.lukka.tech` |
| Auth URL | `https://auth0.lukka.tech/authorize` |
| Token URL | `https://auth0.lukka.tech/oauth/token` |
| Registration URL | `https://auth0.lukka.tech/oidc/register` |
| Resource | `https://global.mcp.lukka.tech` |
| Base scopes | `openid`, `email`, `offline_access` |
| Default scope | `mcp` |
| OIDC discovery URL | `https://auth0.lukka.tech/.well-known/openid-configuration` |
| OIDC UserInfo endpoint | `https://auth0.lukka.tech/userinfo` |

Review discovered settings, create the connection and sign in. The packaged
[mcp.json](mcp.json) records the same public configuration. Access to developer
connections depends on your account and workspace settings. See
[OpenAI's connection guidance](https://developers.openai.com/plugins/build/plugins).

For development of the complete plugin, use the host's supported package or
marketplace distribution flow. A GitHub repository containing these files is
an editable plugin package; it is not automatically a registered marketplace
or a public OpenAI listing.

## Verify the connection

Start a new conversation, select the connection or installed plugin when
needed, then try:

- "Resolve BTC and ETH to canonical Lukka assets."
- "Show the latest available Bitcoin block height and its timestamp."
- "Summarize the latest available digital asset news digest."
- With the full plugin installed: "Check Lukka integration health and tell me
  which products were actually tested."

Check that results identify actual sources and data times. A visible tool does
not prove that your account can execute it or that every blockchain is supported.

## Troubleshooting

| Problem | What to check |
|---|---|
| Auth0 reports `Unknown client` for a `client.json` URL | Check the registration method. This package uses DCR; CIMD needs explicit support from the authorization server. |
| Auth0 reports a callback URL mismatch | The OAuth client's allowed redirect URI must exactly match the host's callback. Reuse neither another host's callback nor a changed local port. |
| DCR returns `too_many_entities` | Ask the Lukka identity administrator to resolve client-registration capacity or provision a client for the exact host callback. Repeated connection recreation does not resolve the quota. |
| A request returns 401 | Renew or reconnect the host's Lukka authentication. |
| A product is forbidden or unavailable | Check product entitlements and the current advertised tool inventory. |
| Tools appear but workflow skills do not | Confirm the full package is installed; a custom MCP-only connection does not include the skills. Start a new session after installation. |
| A parameter fails validation | Use the connected tool's required fields, enum values and JSON types. UDA transaction `limit` is an integer in the verified catalog. |
| A chain returns `Unsupported crypto symbol` | Check support for that exact endpoint. AML and UDA do not have identical coverage. |
| A report is too large | Use bounded data or a verified summary/export/capture path before requesting it. |

Do not paste passwords, OAuth tokens or client secrets into a conversation or
commit them to GitHub. Enter credentials only in the host's authentication flow.
