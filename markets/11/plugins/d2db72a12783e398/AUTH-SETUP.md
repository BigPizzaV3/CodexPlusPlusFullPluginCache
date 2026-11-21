# OAuth setup (live)

| Value | URL |
| --- | --- |
| MCP server | https://scale.asselabs.com/mcp |
| Authorization endpoint | https://scale.asselabs.com/connect/ |
| Token endpoint | https://scale.asselabs.com/oauth/token |
| Dynamic client registration | https://scale.asselabs.com/oauth/register |
| Protected-resource metadata | https://scale.asselabs.com/.well-known/oauth-protected-resource |
| Authorization-server metadata | https://scale.asselabs.com/.well-known/oauth-authorization-server |

OAuth 2.1 with PKCE (S256), public clients (no client secret), refresh-token rotation, RFC 9207 `iss` parameter. Tokens are bound to one scale.

## How a customer signs in
The box has a QR code. Scanning it opens a page that remembers which scale it is; later, when ChatGPT opens the authorization page, the scale is already selected and the person only taps **Connect**. No account, no typing. As a fallback the authorization page has a field for the 8-character code printed on the sticker.

## Reviewer access (demo scale)
The demo scale is virtual (no hardware). To connect: add the app, and on the authorization page type the demo code from the secure reviewer-access field of the submission form, then tap **Connect**. The real code is deliberately NOT stored in this package.

Demo behaviour: `wait_for_weight` with target 123 g simulates an overshoot (`over`), 321 g simulates a timeout (`timeout`); any other target is reached.
