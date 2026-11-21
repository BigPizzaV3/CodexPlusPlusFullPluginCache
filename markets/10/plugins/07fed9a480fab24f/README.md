# AnyShare for ChatGPT and Codex

Release candidate 1.0.1 packages the AnyShare remote MCP server, onboarding and document-sharing skills, including explanations of organization billing access. This ZIP is ready for local testing, not evidence of directory approval or public availability.

## Private testing

The endpoint is `https://share.anysoft.ai/mcp`. In [ChatGPT Plugins](https://chatgpt.com/plugins), choose the plus button and **Add custom MCP server**, enter the endpoint, review permissions, and use OAuth to sign in to AnyShare and select one organization. Availability depends on the client and administrator policy. A custom-server test verifies tools; test the packaged skills separately in a supported local marketplace.

For local ChatGPT desktop/Codex authoring, extract `anyshare` and point a repo or personal marketplace entry at this folder, following [OpenAI's packaging guide](https://developers.openai.com/plugins/build/plugins). Restart/refresh as documented by the client and test in a fresh conversation. Portable `plugin.json` and `mcp.json` are canonical; `.codex-plugin/plugin.json` and `.mcp.json` provide compatibility. Run the installed setup skill before a first task. Downloading this ZIP alone does not install it in ChatGPT web.

## Try it

- Upload this original document and create a protected share link.
- Add this document to my existing investor data room.
- Show measured engagement for my pitch deck this week.

Files must be no larger than 5,242,880 bytes. Supported host file references import original bytes directly. Other clients use an authorized exact-byte transfer or the authenticated browser upload handoff. This plugin does not grant filesystem access. Default reports show aggregates; requested session details and recorded viewer identities use explicit options. New links require verified email and disable downloads. Passwords are configured in the AnyShare website, never chat.

`get_connection` reports the effective billing state, subscription status, known reason and relevant dates. `can_use: false` pauses uploads, new share links and adding documents to rooms; document and engagement reads remain available with the required permissions. Blocked writes return the same billing explanation when available. Trial, paid access and renewal grace are distinct from paused access; scheduled cancellation or a past-due renewal does not itself mean current access has ended. Missing details are reported as unknown. Contact the organization owner or support to review billing access; the plugin does not change billing or initiate purchases.

## Public distribution

The release owner submits this ZIP using **With MCP** in the [OpenAI submission flow](https://developers.openai.com/plugins/deploy/submission), completes domain verification and review, and publishes only after approval. The full review needs real reviewer access, five positive/three negative cases and an accessible recording. No credentials, private reviewer instructions, registration placeholders or fabricated listing IDs belong in this package. Until approval there is no public directory install URL.

[Support](https://share.anysoft.ai/support) · [Privacy](https://share.anysoft.ai/privacy) · [Terms](https://share.anysoft.ai/terms) · [Connection settings](https://share.anysoft.ai/dashboard/settings#ai-connections)

Revoking a connection stops future access. Existing documents and share links remain unchanged. Package format checked against official documentation October 7, 2026.
