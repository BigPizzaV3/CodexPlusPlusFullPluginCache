# MCP protocol and runtime authority

This reference contains stable behavior rules. It does not define the current tool count, API version, schemas, fields, response versions, or limits. Use the live Chartrades MCP `tools/list` catalog and tool responses for those facts.

## Direct MCP tools

The plugin connects to `https://api.chartrades.com/openai-mcp` with the member's Chartrades OAuth account. ChatGPT discovers tools through MCP. Call the selected tools directly with the inputs in their current schemas. The old Custom GPT Action broker calls (`agent_tools`, `agent_tool_call_json`, `agent_tool_call_consequential`) and its `catalog_version` and `tool_args_json` wrapper are obsolete here.

Use the current `help` or `get_docs` tool if available for metrics, freshness, limitations, examples, wallet rules, or changelog. If tool metadata or a response conflicts with this reference, the live metadata or response is authoritative for current capabilities and facts.

## Execution and failure contract

Tool discovery does not answer a private-data question. Execute the relevant data tool before making a Chartrades claim. If connection, authorization, discovery, or execution fails, report the concrete observed error. Do not continue from examples, memory, expected schemas, or invented ranges. If no named data tool succeeds, return no market analysis.

For multi-asset requests, attempt each asset and report successful and failed coverage explicitly. If a tool name or schema has changed, refresh the live catalog and retry once; if it still fails, report the failure. Do not treat a transport or account error as a market signal.

Do not ask the member for an API key. The MCP OAuth flow connects their account. Account access, entitlement, and daily limits are enforced by the server, not by this skill.
