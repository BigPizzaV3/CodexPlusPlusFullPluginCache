# CrumbPass ChatGPT plugin

This package contains the portable Agent Plugins manifest and the remote MCP server mapping used for public submission.

## Before submission

1. Deploy the Convex HTTP routes and confirm `https://mcp.crumbpass.in/mcp` is stable. That host is the `crumbpass-mcp` Cloudflare Worker (`mcp-proxy/`), which forwards to the Convex deployment; production sets `MCP_PUBLIC_ORIGIN=https://mcp.crumbpass.in` so OAuth metadata and token audiences use it. OpenAI does not allow changing a listed app's MCP URL, so keep this host stable; moving Convex deployments only needs the Worker's `CONVEX_SITE_URL` changed.
2. Set Convex `SITE_URL=https://owner.crumbpass.in` so the OAuth consent screen is hosted on the owner app.
3. Verify `https://crumbpass.in/privacy`, `/terms`, and `/support` are publicly reachable.
4. Connect the MCP URL in ChatGPT developer mode and run read, write, edge-case, and destructive-action tests.
5. Zip this folder without credentials and upload it in the Plugins dashboard.

The plugin uses OAuth 2.1 authorization code flow with PKCE and scopes `menu:read`, `menu:write`, `loyalty:read`, `loyalty:write`, and `insights:read`. Users select the restaurant during consent; tokens are scoped to that restaurant and owner membership is re-checked on every tool call. Newly issued OAuth credentials are stored as SHA-256 hashes; pre-existing plaintext token rows remain compatible and are converted to hashes on refresh or removed on revocation.

Changes with financial, loyalty, activation, availability, or destructive impact are confirmation-first: tools return a preview where possible, ChatGPT presents the exact effect, and execution requires explicit owner approval plus `confirm: true`.

The insights scope can return customer names, last four phone digits, point balances, visit/spend patterns, referral performance, feedback comments, and business analytics; the tools do not return full phone numbers or email addresses. Referral tools are read-only analytics today: Refer & Win campaign creation/editing and permanent offer deletion are not supported yet.
