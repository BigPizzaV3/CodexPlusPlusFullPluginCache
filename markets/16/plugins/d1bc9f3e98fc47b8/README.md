# Atomscale ChatGPT plugin

The ChatGPT plugin package (Agent Plugins format) for the AtomCloud MCP server.
The plugin bundles no skills or UI: it is the same `/mcp` server Claude connects to.
Its tools and their annotations come from `mcp_tool_specs()` in `../server.py`, so
editing the server changes the plugin without a new upload. OpenAI rescans the
server daily, and new tools need approval before ChatGPT can use them.

| File | What it holds |
|---|---|
| `plugin.json` | Identity, listing text, links, starter prompts, review test cases, release notes (`extensions.com.openai`) |
| `mcp.json` | The one remote server `https://api.atomscale.ai/mcp/` (trailing slash matches the protected-resource metadata), OAuth with CIMD registration |
| `assets/logo.png` | 512×512 square icon, padded from `react-frontend/public/static/AtomscaleLogoIcon.png` |

The `extensions.com.openai.auth` block in `mcp.json` follows OpenAI's documented
shape, which the generic agent-plugins.org `mcp.schema.json` rejects (its server
objects allow no extra keys). OpenAI's portal is the validator that counts.

`ads/tests/test_chatgpt_plugin.py` checks the listing limits, the assets, and that
every tool named in a review case is still registered on the server.

## OAuth

ChatGPT registers with CIMD (`client_id=https://chatgpt.com/oauth/client.json`,
`private_key_jwt`). The client document's only redirect is
`https://chatgpt.com/connector_platform_oauth_redirect`, so that URI and the
per-connection fallback `https://chatgpt.com/connector/oauth/*` are in
`_ALLOWED_CLIENT_REDIRECT_URIS` (`../oauth.py`). Without them the proxy refuses
ChatGPT's authorization request.

## Build the ZIP

```bash
cd backend/ads/mcp_server/chatgpt_plugin && zip -r ../atomscale-chatgpt-plugin.zip plugin.json mcp.json assets README.md
```

## Try it before submitting

In ChatGPT, open **Plugins**, click **+**, choose **Add custom MCP server**, enter the
URL `https://api.atomscale.ai/mcp/` and choose OAuth. Then mention `@Atomscale`
in a chat. This creates a personal plugin, which needs no review.

## Still needed before submission

- Deploy the ChatGPT redirect allowlist to prod. Until it is deployed, ChatGPT's sign-in fails.
- OpenAI platform org: submitter is an owner (or has Apps Management Write); business verification done.
- Domain verification: serve the portal's token at `https://api.atomscale.ai/.well-known/openai-apps-challenge`, or on the parent domain `atomscale.ai`.
- Reviewer account: dedicated, no MFA, seeded with the demo data the review cases name (`RHEED-Anomaly-Test-B`, `MCV1-210922A-NT`, `V-WSe2-Growth-Run40`, notebook "RHEED Growth Qualification", as in the Claude reviewer org). Enter its credentials in the portal under **Review details**, never in the package.
- `review.demo_recording_url`: a video walkthrough, required for MCP review.
- `category`: confirm `Productivity` against the dashboard's list.
- Privacy policy: OpenAI asks for categories of personal data (account/contact details), retention of active customer data, and user controls. The current page covers sharing and log retention but names neither.
- Review risk: `query_data` runs read-only SQL. Reviewers may treat it as a generic executor.
