# Infobip plugin

ChatGPT plugin for researching Infobip and sending or monitoring customer messages.

| MCP server | Endpoint | Authentication | Purpose |
| --- | --- | --- | --- |
| Discover | `https://mcp.infobip.com/deep-research` | None | Research Infobip products and implementation requirements. |
| Message | `https://mcp.infobip.com/message` | OAuth 2.1 with DCR | Send customer notifications. |
| Observe | `https://mcp.infobip.com/observe` | OAuth 2.1 with DCR | Analyze delivery, traffic, errors, and billing usage. |

## Authentication

Message and Observe use Dynamic Client Registration (DCR). No client ID or client secret belongs in this package: the MCP client registers during connection setup. OAuth endpoints, registration settings, and scopes are discovered from the servers.

## Local testing

Add `./infobip-plugin` to the repository marketplace, restart ChatGPT desktop, install the plugin, and connect Infobip when prompted. Try:

- “Send an SMS to [recipient] with this message: [message].”
- “Use Infobip to research requirements for sending [channel] messages in [country].”
- “Compare messaging performance trends across [channels] over [time period], including volume, delivery, and channel-specific engagement where supported.”

Confirm recipients, channel, final content, and timing before sending a message.
