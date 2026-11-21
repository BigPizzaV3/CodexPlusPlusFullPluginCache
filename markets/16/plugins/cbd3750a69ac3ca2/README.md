# Datadog ChatGPT Plugin

Query your Datadog data directly from ChatGPT using natural language. Ask about logs, metrics, traces, dashboards, monitors, and more.

This is a **templated plugin**: a ChatGPT workspace administrator creates an instance of it and points that instance at their organization's Datadog MCP endpoint. Users then connect to and use the configured instance.

## What you need

- A [Datadog](https://www.datadoghq.com/) account
- A ChatGPT workspace where an administrator can configure plugin instances

## Setting up an instance

When creating an instance, enter the MCP endpoint for your Datadog site:

| Site | MCP endpoint                                                               |
| ---- | -------------------------------------------------------------------------- |
| US1  | `https://mcp.datadoghq.com/v1/mcp?toolsets=chatgpt`     |
| US3  | `https://mcp.us3.datadoghq.com/v1/mcp?toolsets=chatgpt` |
| US5  | `https://mcp.us5.datadoghq.com/v1/mcp?toolsets=chatgpt` |
| EU   | `https://mcp.datadoghq.eu/v1/mcp?toolsets=chatgpt`      |
| AP1  | `https://mcp.ap1.datadoghq.com/v1/mcp?toolsets=chatgpt` |
| AP2  | `https://mcp.ap2.datadoghq.com/v1/mcp?toolsets=chatgpt` |
| UK1  | `https://mcp.uk1.datadoghq.com/v1/mcp?toolsets=chatgpt` |

Authentication uses OAuth with your Datadog account.

## Using the plugin

Once connected, just ask anything about your Datadog data:

```
Show me error logs for the "checkout" service from the last hour
```

```
What monitors are currently alerting?
```

```
Find traces for service "api-gateway" with latency > 500ms
```

## Good to know

- Only the Datadog MCP server's `chatgpt` toolset is enabled, requested through the `toolsets` query parameter in the endpoint URL. Enter the endpoint exactly as listed above.
- No Datadog credentials are sent to the AI model provider.

## Support

- [Datadog MCP Server Documentation](https://docs.datadoghq.com/mcp_server/)

## Legal

See the [LICENSE](LICENSE) and [NOTICE](NOTICE) files included with this plugin.

For details on how Datadog handles your data, see the [Datadog Privacy Policy](https://www.datadoghq.com/legal/privacy).
