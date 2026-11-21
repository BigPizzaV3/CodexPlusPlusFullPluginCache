# Connect the private prototype to ChatGPT

## Current state

The component, MCP server, portable manifest, and skill are built. HTTP and stdio integration tests pass locally. No ChatGPT connection has been created and nothing has been deployed or submitted publicly.

The `http://127.0.0.1:4317/mcp` URL in `mcp.json` is local development configuration. ChatGPT's web service cannot connect directly to the loopback address on this Mac. Current OpenAI documentation supports either Secure MCP Tunnel or a public HTTPS endpoint for developer-mode tests. This corrects the earlier guide's public-HTTPS-only instructions.

## Recommended private connection: Secure MCP Tunnel

1. Verify Developer mode is available under ChatGPT Settings, Security and login. Availability depends on the account and workspace policy.
2. In https://platform.openai.com/settings/organization/tunnels, create a tunnel associated with the target ChatGPT workspace and appropriate Platform organization. Creating a tunnel requires Tunnels Read + Manage; using it requires Tunnels Read + Use. Confirm the intended account before creating the connection.
3. Configure OpenAI's `tunnel-client` on this Mac with the assigned tunnel ID, a runtime API key stored through machine authentication or a local environment file, and the calculator's local HTTP endpoint or stdio command. Never paste credentials into chat or include them in the plugin ZIP. Use the official tunnel client's current quickstart and doctor check for configuration.
4. Keep the calculator and tunnel client running. Secure MCP Tunnel uses outbound HTTPS to OpenAI and does not require publishing this local server. The local HTTP target remains `http://127.0.0.1:4317/mcp`; the stdio entry point is `src/stdio.mjs`.
5. Open https://chatgpt.com/plugins, select the plus button, enter the display name and description, and choose Connection > Tunnel. Select the tunnel or enter its observed ID, create the connection, and check the discovered tools.
6. Install the resulting Personal plugin. Start a new Work chat, type `@`, select it, and ask it to open the calculator. Verify the actual ChatGPT component, tool selection, calculation, reset, unit conversion, links, and Share with chat.

Tunnel access, workspace association, and UI behavior in Ken's account remain unverified. The source ZIP alone does not register the running server with ChatGPT.

## Alternative private test: public HTTPS endpoint

1. Get Ken's approval for the specific HTTPS hosting or temporary-tunnel destination. His operating rules require confirmation before deployment. Private plugin visibility does not make a public HTTPS server private.
2. Expose this stateless MCP server through the approved HTTPS endpoint. Keep the endpoint live during the test. A local tunnel may forward to the loopback process; a hosted process needs `BIND_ADDRESS=0.0.0.0`, `PORT`, and `PUBLIC_BASE_URL=https://the-approved-host`.
3. If a tunnel preserves its public Host header, set `PUBLIC_BASE_URL` to that HTTPS origin before restarting the server. Otherwise the intentional Host check will reject it. The root endpoint shows the calculator, `/health` is a health check, and `/mcp` accepts MCP requests.
4. In ChatGPT, open Settings, Security and login, and enable Developer mode if available. Open Plugins, use the plus button, and register the approved HTTPS `/mcp` URL. The server contains no accounts or private records; use the appropriate unauthenticated connection option for this private calculator test. If workspace policy requires authentication, add it before connecting rather than bypassing the policy.
5. Open the resulting Personal plugin and install it. Start a new Work chat, invoke the plugin with `@`, and ask it to open the calculator.
6. Test a supplied-mass and final-volume calculation, missing-unit clarification, rejected zero volume, unit conversion, reset, Share with chat, and the optional conversation panel. Verify the model does not choose values or provide dose or preparation instructions.
7. For a private local-marketplace package that includes skills, copy the actual `plugin_asdk_app...` ID assigned to the registered connection. Use that observed ID in `.app.json` and point `extensions.com.openai.apps` to `./.app.json` using the current OpenAI packaging guide. Do not invent an app ID. This mapping is for private testing, not public ZIP submission.

For local marketplace discovery, OpenAI documents a personal `~/.agents/plugins/marketplace.json` or a repo `.agents/plugins/marketplace.json`. No personal marketplace or global configuration was changed by this build. A local source listing alone does not prove the registered ChatGPT server mapping works.

## Public release is separate

A public submission needs verified publisher identity, public metadata and policy URLs, appropriate server access controls, the current review materials, and host verification. Those are intentionally not fabricated in the private package. The current ZIP is a source and testing handoff, not an approved public listing.

Secure MCP Tunnel does not support public plugin distribution. Before public submission, deploy a stable public HTTPS MCP endpoint and replace the loopback URL in `mcp.json`. The current submission guide does not accept ZIPs with `apps` / `.app.json` references or lifecycle hooks. Declare the MCP URL in the MCP configuration instead.

Upload the prepared ZIP at https://platform.openai.com/plugins using Upload new or existing plugin, resolve automated package and server findings, complete domain verification and review materials, then submit for review. Approval and publication are separate steps. Branding and links must also satisfy the guidelines on advertising and restricted goods; acceptance of the Peptara Labs funnel is not established.

Official references:

- https://developers.openai.com/plugins/quickstart
- https://developers.openai.com/plugins/deploy/connect-chatgpt
- https://developers.openai.com/api/docs/guides/secure-mcp-tunnels
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/plugin-guidelines
