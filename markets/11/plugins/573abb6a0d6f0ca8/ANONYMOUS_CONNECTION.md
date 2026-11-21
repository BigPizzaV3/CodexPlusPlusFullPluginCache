# Anonymous Analyst connection

The public Analyst uses https://analyst.signalaf.com/api/plugins/sigrank/mcp with authentication set to none. It serves the existing five public Analyst tools and the same live SignalAF data.

This hostname exposes only the Analyst MCP and the OpenAI domain-verification challenge. Website OAuth discovery, login and submission endpoints are unavailable on it. SignalAF’s account and submission authentication remains on signalaf.com.

The original https://signalaf.com/api/plugins/sigrank/mcp remains compatible with existing private connections. The separate submission MCP is https://signalaf.com/api/mcp.

Deployment prerequisite: the anonymous hostname’s routing change must be deployed and DNS/HTTPS verified before uploading this package to the review portal. A successful portal connection and five-tool scan are required before submission. No final review attestations have been accepted by the agent.
