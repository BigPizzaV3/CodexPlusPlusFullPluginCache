# OfferUnderway

Connect your OfferUnderway account to check your career profile, tailor application materials and manage your job search from your AI assistant.

This package includes portable, Codex and Claude Code plugin manifests, a remote MCP connection and setup/application skills. It contains no credentials or executable hooks. Source and releases: [LeeTheBuilder/offerunderway-mcp](https://github.com/LeeTheBuilder/offerunderway-mcp).

## Install in Claude Code

In Claude Code, run:

```text
/plugin marketplace add LeeTheBuilder/offerunderway-mcp
/plugin install offerunderway@offerunderway
```

Open `/mcp`, choose the OfferUnderway server and authenticate with your OfferUnderway account. Run `/offerunderway:setup` to check the connection. The plugin includes no API key and uses the host's OAuth sign-in flow.

## Connect

Server URL: `https://api.offerunderway.com/mcp`. Authentication: OAuth. Sign in to OfferUnderway and review the permissions shown by the consent screen.

- ChatGPT: open Plugins → + → Add custom MCP server, choose OAuth, create the plugin and install it. If the deployed server rejects published-identity registration, select Dynamic Client Registration (DCR) in Advanced settings.
- Claude: open [OfferUnderway in the connector directory](https://claude.ai/directory/offerunderway), choose Connect, and sign in to your OfferUnderway account.
- Codex: run `codex mcp add offerunderway --url https://api.offerunderway.com/mcp`, then `codex mcp login offerunderway`.
- Claude Code: run `claude mcp add --scope user --transport http offerunderway https://api.offerunderway.com/mcp`, then use `/mcp` → offerunderway → Authenticate.
- Cursor: add an HTTP MCP server with the URL in MCP settings and follow its OAuth prompt.

Select OfferUnderway in a new conversation and ask: “Use OfferUnderway to call get_offerunderway_context and tell me whether my career profile is ready. Do not generate materials or submit applications yet.”

Hosted tool availability depends on the deployed server. The bundled workflow skill discovers available tools and supports both workflow and application-pack interfaces. The current release exposes twelve profile, search, document-pack and application-tracking tools. Installation alone does not verify that a tool call succeeds. OfferUnderway is published in Claude's directory as a Community connector, which undergoes automated review and does not carry Anthropic Verified status. OpenAI developer identity verification is complete; the ChatGPT directory listing is uploaded as a draft; domain verification, automated checks and provider review remain pending.

## Privacy and support

OfferUnderway permissions can include selected career-profile/contact details, saved answers, document generation and application records. Review the requested permissions before connecting. Revoke access in [connection settings](https://offerunderway.com/integrations/ai/connections).

[Setup](https://offerunderway.com/integrations/ai) · [Privacy policy](https://offerunderway.com/privacy) · [Terms](https://offerunderway.com/terms) · [Connector security](https://offerunderway.com/integrations/ai/security). Support: admin@offerunderway.com.
