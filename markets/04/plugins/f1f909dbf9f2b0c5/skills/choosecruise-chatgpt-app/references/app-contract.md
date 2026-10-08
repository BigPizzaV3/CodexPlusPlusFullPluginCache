# ChooseCruise ChatGPT app contract

Read this reference when changing public tools, widget metadata, ownership verification, analytics, or submission files.

## Architecture

- Primary archetype: submission-ready React widget.
- MCP endpoint: stateless `POST /mcp` in `mcp-gateway/src/httpServer.ts`.
- Public tools are registered centrally by `MCPGatewayServer` through `ToolRegistry`.
- `search_cruises` renders `ui://widget/cruise-carousel-<content-hash>.html`.
- `get_cruise_details` returns compact structured details without a separate widget.
- The carousel receives results through the ChatGPT host bridge and can call `get_cruise_details` or open a ChooseCruise web URL.

## Public tools

### `search_cruises`

- Searches ocean or river cruise inventory using natural-language ports, regions, lines, date ranges, price, sorting, and pagination.
- Maps names to internal IDs, queries the internal ChooseCruise API, inlines visible card images when possible, and returns a compact result set.
- Records filters, result summary, request origin, and timing in RudderStack.
- Required annotations: `readOnlyHint: false`, `openWorldHint: true`, `destructiveHint: false` while that analytics behavior remains.

### `get_cruise_details`

- Accepts a master cruise ID from a search result and retrieves itinerary, ship, cabins, price, and booking URL.
- Records a cruise-view analytics event, including failed views.
- Must not expose `userId` on the public unauthenticated schema.
- Required annotations: `readOnlyHint: false`, `openWorldHint: true`, `destructiveHint: false` while that analytics behavior remains.

### `ping`

- Internal diagnostic implementation only.
- Do not register it in the public MCP server and do not include it in submission JSON.

## Widget and security invariants

- Tool descriptors publish both `_meta.ui.resourceUri` and the `openai/outputTemplate` compatibility alias.
- Resource descriptors publish both MCP Apps `ui` metadata and required OpenAI compatibility aliases.
- Widget bundle URIs include a content hash; the unversioned alias remains readable for existing connectors.
- Resource domains are derived from the configured ChooseCruise webapp image origin plus the supplier fallback `https://images.cruisec.net`.
- The current widget makes no direct network connections, so it should not declare `connectDomains`/`connect_domains` without a corresponding code change.
- Avoid `frameDomains` unless embedding becomes a product requirement.
- The repository currently retains `text/html+skybridge` for verified ChatGPT compatibility. Treat migration to `text/html;profile=mcp-app` as a tested compatibility change, not a mechanical cleanup.

## Ownership verification

`GET /.well-known/openai-apps-challenge` must return the configured OpenAI ownership token as `text/plain` with status 200. The current token is:

```text
VwfWPAkSOvfg-pDqOu5-29kL6Gz5zRxhlqMUZktweZE
```

If OpenAI issues a replacement, update the route and its regression test together.

## Submission invariants

- Production `tools/list` is the source of truth for imported annotations and schemas.
- Every exposed tool has an `outputSchema` matching its actual `structuredContent`.
- Submission JSON contains exactly five positive and three negative test cases when generated through the repository's submission workflow.
- Tool descriptions and privacy policy explain analytics data use.
- Deploy before rescanning in the submission portal; local edits do not affect scan results.
