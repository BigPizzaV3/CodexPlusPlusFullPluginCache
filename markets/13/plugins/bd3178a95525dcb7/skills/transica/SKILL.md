---
name: transica
description: "Use Transica when someone asks whether a webpage is accessible and usable by AI agents, or when someone asks whether an MCP server meets ChatGPT or Claude directory requirements."
---

# Transica

AI readiness and MCP checks

## Tools that read

- `scan_webpage_ai_readiness`: Returns a readiness score, passed and failed checks, category results, top fixes, limitations, and a report link for one public webpage. Use it when someone asks whether a webpage is accessible and usable by AI agents; for checking an MCP server's directory compliance, use check_mcp_server_directory_rules instead. Pass url to scan the page directly, or use the reportUrl to revisit the detailed results.
- `check_mcp_server_directory_rules`: Returns server details, tool counts, directory-specific results, individual checks, and a full report link after connecting to a public remote MCP server and reading its tool list without calling tools. Use it when someone asks whether an MCP server meets ChatGPT or Claude directory requirements; for scanning a regular webpage's AI readiness, use scan_webpage_ai_readiness instead. Pass url as the public MCP server address to check its connection, sign-in, domain, and tool rules.

## Example requests

- Check the MCP server at https://mcp.context7.com/mcp against the directory rules
- Is https://example.com ready for AI agents? What should I fix first?
- Scan https://transica.dev for AI agent readiness
