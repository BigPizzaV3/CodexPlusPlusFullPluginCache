<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/preismonitoring-logo-negativ.svg">
    <img src="assets/preismonitoring-logo.svg" alt="PREISmonitoring" width="340">
  </picture>
</p>

# PREISmonitoring MCP — Agent Plugin

The official agent plugin by **PREISmonitoring**. It connects AI clients to the PREISmonitoring API over the Model Context Protocol and exposes your market price, observation and item data as tools.

The package includes the OpenAI listing, public support and policy links, an app icon, and review scenarios. Directory approval and publication are separate from package availability in this repository. Sign in through your client's OAuth flow; account access details are never included in the package.

The portable OpenAI MCP manifest declares mixed authentication using Client ID Metadata Documents and requests the `mcp` and `offline_access` scopes. Codex and Claude Code continue to use the shared `.mcp.json` server configuration.

**API documentation:** <https://api.preismonitoring.de/docs#description/introduction>

| | |
| --- | --- |
| Endpoint | `https://api.preismonitoring.de/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth 2.1 with PKCE, interactive in the client |
| Package format | [Agent Plugins 1.0](https://agent-plugins.org/specification) |
| Credentials in this package | none |

## Requirements

- A PREISmonitoring account for the protected data tools. The public
  `submit_inquiry` tool does not require an account or sign-in.
- An AI client that speaks MCP over Streamable HTTP with OAuth redirection.
- A local environment that can open a browser and accept a callback on `127.0.0.1`.

No access yet? A time-limited free API account can be requested at
<https://www.preismonitoring.de/en/contact>.

## Installation

This package ships several manifest layouts because clients read different locations. The declared server is identical in all of them.

### Claude Code

```bash
claude plugin marketplace add PREISmonitoring/preismonitoring-mcp-plugin
claude plugin install preismonitoring-mcp@preismonitoring-mcp
claude mcp login plugin:preismonitoring-mcp:preismonitoring-mcp
```

### Codex

```bash
codex plugin marketplace add PREISmonitoring/preismonitoring-mcp-plugin
codex plugin add preismonitoring-mcp@preismonitoring-mcp
codex mcp login preismonitoring-mcp
```

### Visual Studio Code

Run **Chat: Install Plugin From Source** and enter
`https://github.com/PREISmonitoring/preismonitoring-mcp-plugin`. Plugin support requires `chat.plugins.enabled`.

### Goose

Goose follows the Open Plugins specification, whose package format has no concept of MCP servers; this plugin is **not** installable there. Configure the server as an extension in `~/.config/goose/config.yaml` instead:

```yaml
preismonitoring:
  enabled: true
  type: streamable_http
  name: PREISmonitoring
  uri: https://api.preismonitoring.de/mcp
  timeout: 300
```

Note Goose's own key names: `streamable_http` with an underscore, and `uri` rather than `url`.

### Claude Desktop and claude.ai

These surfaces do not consume plugins. Enter `https://api.preismonitoring.de` in the connector settings. On claude.ai an organisation-level approval is required as well.

## First sign-in

On first use the client opens a browser.

1. Sign in with your PREISmonitoring account.
2. If the wrong user is signed in, switch accounts directly on the consent screen.
3. Approve the request — or deliberately decline it.
4. The final screen tells you that you can close the window.

The protected data tools are then available in your client. The public
`submit_inquiry` function uses the same `/mcp` connection and does not require
the sign-in step.

## Permissions

OAuth access grants no additional rights. Over authenticated MCP calls you see
exactly the data your account sees elsewhere, bounded by your business
permissions. The anonymous `submit_inquiry` call returns no account data. There
are no API keys, no service tokens and no password grant for this endpoint.

Clients using Client ID Metadata Documents can advertise their supported token
authentication methods in `token_endpoint_auth_methods_supported`. The supported
public-client method is `none` with mandatory PKCE/S256, customer sign-in and
consent. A valid non-empty list must include `none`, even if its legacy preference
names another method. Without a list, only the legacy `none` preference (or its
omitted-field default) is accepted. Empty, null or malformed lists and unsupported
JWT assertions are rejected; `private_key_jwt` is not implemented.

## Security

- This package contains no tokens, passwords or other secrets. Configured headers are literal, publicly visible package data and never carry credentials.
- Authorization Code with PKCE, method `S256`, is mandatory.
- Access tokens are valid for 24 hours, refresh tokens for 30 days. Refresh tokens are rotated on redemption.
- Rotation is protected against reuse: redeeming an already rotated refresh token is treated as a compromise and revokes the entire token family. Never redeem a refresh token from two processes in parallel.

Please report security findings confidentially via the contact on <https://preismonitoring.de> rather than as a public issue.

## Verified clients

We call a client supported only once PREISmonitoring has connected it successfully. Without a verified run we make no compatibility claim — not even when the client speaks MCP and OAuth in general.

| Client | Status |
| --- | --- |
| Codex | verified against `live`; tool listing and a business read call succeeded |
| Claude Code | verified against `live`; tool listing and a business read call succeeded |
| Visual Studio Code | verified against `live`; tool listing and a business read call succeeded |
| Goose | not a plugin consumer, see the extension route above |

The verified-client rows are historical evidence for the named runs; they are
not a current availability claim. The inquiry addition keeps the endpoint and
client setup unchanged and does not by itself extend those older runs.

## Support

For business questions and account topics, contact your usual PREISmonitoring representative. Technical questions about the API are answered by the [API documentation](https://api.preismonitoring.de/docs#description/introduction).

## Provenance

This repository is a build artifact. It is generated from PREISmonitoring's internal development repository, and every release commit references the corresponding source commit. Please do not edit files here — they are overwritten by the next release.

## License

MIT. See `LICENSE`.
