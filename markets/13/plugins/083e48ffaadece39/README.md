# Zendesk Headless MCP

Connect ChatGPT to the Zendesk actions granted to your connected agent.
Available tools depend on your account's action catalog and agent permissions.

## MCP configuration

The root `.mcp.json` uses the OpenAI extension structure from the
"Use a registered OAuth client" example supplied during bundle preparation:

https://developers.openai.com/plugins/build/plugins#use-a-registered-oauth-client

```json
{
  "mcpServers": {
    "zendesk": {
      "type": "streamable-http",
      "url": "https://mcp.zendesk.com/integrations/mcp",
      "extensions": {
        "com.openai": {
          "auth": {
            "type": "oauth",
            "client": {
              "mode": "provided",
              "clientId": "zdg-plugin-chatgpt",
              "tokenEndpointAuthMethod": "none"
            }
          }
        }
      }
    }
  }
}
```

The `$schema` property is omitted because the submission uploader rejected
it with "Extra inputs are not permitted." The MCP hostname is updated to `mcp.zendesk.com`; the path and OAuth
settings are retained from the accepted v7 bundle.

The existing bundle discovers `.mcp.json` at its root. The documentation's JSON
example describes the file's contents. A file named `mcp.json` would need an
explicit manifest reference instead of this bundle's default `.mcp.json`
discovery. This bundle contains a single MCP configuration file.

OAuth settings belong under `mcpServers.zendesk.extensions["com.openai"].auth`.
This replaces the unverified `openai.auth` layout in v5 and the earlier `oauth`
configurations. The transport is `streamable-http`, as in the supplied example.

`tokenEndpointAuthMethod: none` matches the public-client method advertised by
this repository's `OAuthMetadataHandler.authorizationServerMetadataHandler`.
The production endpoint's deployed metadata and the registered client's type
have not been checked live. A confidential client requires its supported
method (`client_secret_basic` or `client_secret_post`) and a secret supplied
separately through connection setup.

Authorization/token endpoint and scope overrides are omitted so OAuth discovery
can supply them. No fixed callback URL, client secret, access token, or
caller-identity header is embedded. Register the callback URL supplied by the
connection flow with your OAuth provider. Associate the client with the
appropriate Connected Agent and user/action grants in Zendesk Admin Center.

## Submission

Upload `zendesk-headless-chatgpt-v9-with-icon.zip`. The single top-level
`zendesk-headless-chatgpt/` directory contains `.codex-plugin/plugin.json`,
`.mcp.json`, this README, and `assets/zendesk.png`. The supplied Zendesk PNG
is used for both the listing logo and composer icon without modifying its
image data. MCP and OAuth configuration bytes are identical to v8.
Screenshots were not supplied.

JSON syntax, exact connection settings, a single MCP server definition, and ZIP
integrity were checked locally. The current schema could not be downloaded
because DNS is unavailable. Full schema validation, live OAuth, tool discovery,
and portal acceptance have not been verified.
