# MCP server — connect, authenticate, tools

Delpha hosts a **remote MCP server** at `https://mcp.delpha.ai/mcp` (streamable HTTP). It exposes the
same engines as the [REST API](rest-api.md) as agent tools.

## Two ways to authenticate

| | How | Best for |
|---|---|---|
| **OAuth 2.1 + PKCE** | The client discovers the authorization server and runs the flow; you sign in with your `app.delpha.ai` account and approve. Nothing to paste. | Claude Desktop, Claude.ai, ChatGPT and other connector UIs |
| **API key** | Send `Authorization: Bearer dlp_…` on every request. | Claude Code, Cursor, Windsurf, CI, anything header-configurable |

Both paths resolve to the same team and bill the same credits. A key used here obeys the same
[scopes and ceilings](rest-api.md#key-restrictions) it obeys on REST — gating only REST would leave
MCP as a bypass, so it does not.

**The team must have MCP enabled.** In the console, open **Developer → MCP setup** and turn on
**MCP access**. The key path is fail-closed on this flag; leaving it off is a clean kill-switch for
all MCP access.

## Connect

**Claude Code**

```sh
claude mcp add delpha --transport http https://mcp.delpha.ai/mcp \
  --header "Authorization: Bearer $DELPHA_API_KEY"
```

**Cursor** — `.cursor/mcp.json` (or `~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "delpha": {
      "url": "https://mcp.delpha.ai/mcp",
      "headers": { "Authorization": "Bearer <DELPHA_API_KEY>" }
    }
  }
}
```

**Windsurf** — `~/.codeium/windsurf/mcp_config.json`, same shape with `serverUrl` instead of `url`.

**Claude Desktop, Claude.ai, ChatGPT and other connector UIs** — add a custom connector with the URL
`https://mcp.delpha.ai/mcp` and complete the sign-in. No key to manage.

The console renders these same snippets with your key already injected, at **Developer → MCP setup**.

## Tools

A submit/poll pair per capability (the two `validateAndNormalize*` tools check a value you already hold and never search):

| Submit (returns `job_id`) | Poll result |
|---|---|
| `findAndValidateEmail` | `getEmailResult` |
| `validateAndNormalizePhone` | `getPhoneResult` |
| `validateAndNormalizeName` | `getNameResult` |
| `findAndValidateLinkedInProfile` | `getLinkedInProfileResult` |
| `findAndValidateLinkedInCompanyPage` | `getLinkedInCompanyPageResult` |
| `findAndValidateWebsite` | `getWebsiteResult` |
| `findAndValidateLegalID` | `getLegalIDResult` |
| `findAndValidateUltimateParent` | `getUltimateParentResult` |

The surface is generated from the published OpenAPI document at server start and then filtered by
MCP policy. Publishing the spec object is a manual operator step and it can lag code, so ask your
client for `tools/list` rather than assuming — that is the reliable production surface and why no
count is written down here.

Not every REST route is a tool. The synchronous `GET /v1/phone`, `POST /v1/email-insights` and
every [batch](rest-api.md#batch) route are REST-only by design. The MCP surface is the curated
find/validate set above.

Production serves the two specific LinkedIn pairs above. The generic `findAndValidateLinkedin` /
`getLinkedinResult` operations remain deprecated in REST for compatibility, but MCP's production
policy hides them. Do not hard-code the generic MCP names.

## Using them

Same [find → get pattern](rest-api.md#the-async-pattern) as REST, with one MCP-specific rule:

**`get*Result` polls upstream for you and holds the call open, so one call normally returns the
finished result.** Do not loop on it. Re-call only if it returned with `status_code` still `202`,
and wait first. Early re-calls waste a round-trip and render a duplicate result widget.

Submissions are independent — for a record needing several checks, submit them all, then read them
all.

## Result widgets

Most result tools ship an MCP-Apps UI widget, so a client that renders them shows a formatted card
instead of raw JSON. The widget is a view of the same `result` payload — read the JSON, not the
card, when you are deciding something.

## See also

- [rest-api.md](rest-api.md) — the same capabilities from code.
- [credits-and-limits.md](credits-and-limits.md) — what a tool call costs.
- [Delpha MCP docs](https://help.delpha.io/delpha-api-and-mcp/mcp)
