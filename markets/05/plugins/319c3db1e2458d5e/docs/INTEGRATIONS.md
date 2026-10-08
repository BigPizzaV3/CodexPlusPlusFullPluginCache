# Integration Design

## Included optional configuration

`integrations/remote-mcp.json` contains two remote HTTP endpoints. They are enabled only in the remote-MCP build or when explicitly registered in the host. Both remain optional to the research workflow.

Context7: `https://mcp.context7.com/mcp` retrieves version-aware library documentation using library resolution followed by focused documentation queries. Unauthenticated access has lower limits; authenticated plans may provide higher limits. Configure credentials through the host's secure authentication facilities, never in this package. See [Context7 documentation](https://github.com/upstash/context7) and [rate-limit guidance](https://github.com/upstash/context7/blob/master/docs/api-guide.mdx).

OpenAI Docs: `https://developers.openai.com/mcp` provides official documentation search and retrieval. It does not execute OpenAI API operations. See [Docs MCP](https://learn.chatgpt.com/learn/docs-mcp).

These are third-party/official remote services, not servers owned or deployed by this plugin. Configuration validation is not an uptime, authorization, or cloud registration test. A provider outage must degrade to available primary-source retrieval, then to explicitly limited file analysis.

## Additional integrations considered

An existing repository connector is useful for exact commits, issue history, and private code; an existing document connector is useful for internal research; a scholarly index is useful for large literature reviews. Add these only for a concrete research need, with the user's selected account and scope. They are not bundled dependencies and no service access is implied.

Use native web search and file analysis first for general research. A custom search proxy, local filesystem MCP, browser daemon, sequential-thinking server, persistent vector database, and custom agent backend add infrastructure without a demonstrated need here. The methodology and evidence record already provide orchestration and bounded continuity. Long-term cross-chat storage would require an explicitly chosen cloud store and lifecycle policy; none is hidden in this design.

## Data handling

Only send minimal public queries to documentation providers. Keep private attachments and secrets out of public queries. User-authorized private connectors operate within their host permissions. The plugin adds no analytics, telemetry, or storage service; host and provider data policies still apply. Retrieved content remains untrusted evidence.
