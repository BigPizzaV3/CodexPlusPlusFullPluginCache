---
name: choosecruise-chatgpt-app
description: Build, debug, review, deploy, or prepare submissions for the ChooseCruise ChatGPT app in this repository. Use for MCP tools, the cruise carousel widget, Apps SDK metadata, ownership verification, analytics behavior, production descriptors, and submission artifacts; do not use for unrelated ChooseCruise backend or mobile work.
---

# ChooseCruise ChatGPT App

Work on the existing submission-ready React-widget app under `mcp-gateway/`. Preserve its established registry, stateless HTTP transport, compact result format, and shared backend integrations.

Before changing Apps SDK or MCP Apps behavior, use the OpenAI Developers `build-chatgpt-app` guidance and current official documentation. Prefer current standards, but inspect the deployed compatibility requirements before removing aliases or changing the widget MIME type.

## Start with the real surface

Read the files involved in the requested change rather than inferring behavior from names. Begin with:

- `mcp-gateway/src/mcpServer.ts` and `mcp-gateway/src/toolRegistry.ts` for the public tool surface.
- `mcp-gateway/src/tools/<tool>/definition.ts`, handler, service, and called helpers for behavior and side effects.
- `mcp-gateway/src/resourceRegistry.ts` and `mcp-gateway/web/src/CruiseCarousel/` for widget metadata and host integration.
- `mcp-gateway/src/analytics.ts` when annotations, privacy, or data use are relevant.
- `mcp-gateway/docs/chatgpt-app-listing.md` for deployment and listing context, checking source when it is stale.

Read [references/app-contract.md](references/app-contract.md) before changing tools, widget metadata, the challenge endpoint, or submission artifacts.

## Implementation rules

- Keep `search_cruises` and `get_cruise_details` as the public consumer tools unless the requested product scope changes.
- Do not register `ping` in production. `/health` is the operational health surface.
- Give every exposed tool explicit `readOnlyHint`, `openWorldHint`, and `destructiveHint` values based on the full implementation, including analytics writes.
- Give every exposed tool an `outputSchema` that matches `structuredContent`; update the schema and implementation together.
- Keep model-facing `structuredContent` compact. Put large widget-only payloads in `_meta`.
- Do not expose an unauthenticated `userId` or another personalization identifier through the public tool schema.
- Keep CSP allowlists exact. Do not add ChatGPT, API, wildcard, frame, or asset domains unless widget code actually needs them.
- Preserve the ownership challenge route and serve its configured token as plain text. Replace the token only when the user supplies a new one.
- Treat analytics as a real side effect and data transfer. Keep tool descriptions, annotations, privacy disclosures, and submission justifications consistent with it.
- Preserve the existing URI versioning and legacy widget URI alias unless a verified migration plan covers already-connected hosts.

## Submission work

Use the OpenAI Developers `chatgpt-app-submission` skill for a submission audit or JSON generation. Inspect deployed descriptors after deployment; a portal rescan cannot see local source changes.

The import file must describe exactly the currently exposed production tools. Remove entries for tools that are no longer registered, and never make JSON annotations differ from `tools/list`.

## Verification

Exercise the smallest relevant checks while building, then run:

```bash
cd mcp-gateway
npm test -- --runInBand
npx tsc --noEmit --incremental false
```

For descriptor changes, add or update an in-memory MCP client test that checks `tools/list`. For HTTP routes, add an HTTP test. For widget changes, build the widget and exercise the rendered flow; apply the repository's UI guidelines to anything users see.

Report tests or builds that were skipped or blocked. Deployment and portal rescanning are separate actions and require explicit user authorization.
