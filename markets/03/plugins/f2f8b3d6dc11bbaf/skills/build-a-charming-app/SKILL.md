---
name: build-a-charming-app
description: Create, host, and iterate on a personal interactive web app with Charming — a real URL, persistent storage, and an MCP or HTTP API — from any agent.
---

# Build a Charming app

Charming turns a natural-language description into a hosted web app with a real URL and a database. Use it from any MCP-capable client or over plain HTTP; the HTTP path builds a first app with no signup.

## When to use this

Reach for Charming when the user wants a small app that outlives the chat: a tracker, a dashboard, a form, a personal tool. Charming gives it a persistent URL, storage, and an API your agent can keep using and updating across sessions.

## Two surfaces

- **MCP** (Claude, Cursor, Claude Code, and more): add `https://charm.ing/mcp` as an MCP server, then call the tools. ChatGPT uses its own endpoint, `https://charm.ing/mcp/chatgpt`, which carries the inline-widget metadata. Per-client setup strings: https://charm.ing/docs/clients.txt
- **HTTP**: `POST https://charm.ing/app` with the app source. Full contract: https://charm.ing/.well-known/openapi.json

## The app contract

An app is one ES module with two named exports, `manifest` and `routes`. Every new app uses this shape on both surfaces.

```js
export const manifest = {
  $schema: 'https://charm.ing/schema/app-manifest/2026-07-31.json',
  id: 'counter',
  meta: { name: 'Counter', icon: { emoji: '➕', bg: '#e8611c' } },
  capabilities: { imports: ['charming:storage/kv@1.0'] },
};

export const routes = [
  {
    op: 'increment',
    method: 'POST',
    path: '/api/increment',
    title: 'Increment counter',
    description: 'Add one and return the new value.',
    inputSchema: { type: 'object', properties: {}, additionalProperties: false },
    outputSchema: { type: 'object', properties: { count: { type: 'integer' } } },
    annotations: { readOnlyHint: false },
    public: true,
    examples: [{ input: {}, output: { count: 1 } }],
    handler: async (input, { env, ctx, request }) => {
      const count = ((await env.storage.get('count')) ?? 0) + 1;
      await env.storage.put('count', count);
      return { count };
    },
  },
];
```

`manifest` is parsed statically, so keep it a plain literal with no computed values. `capabilities` accepts `imports` and nothing else: `charming:storage/kv@1.0` gives `env.storage`, `charming:storage/blob@1.0` gives `env.assets`, `charming:logging/emit@1.0` gives `env.log`, `charming:network/fetch@1.0` gives plain outbound `fetch` and `charming:secrets/fetch@1.0` gives the sealed `env.fetch` that substitutes `{{secret:NAME}}` into headers. Both are claimed-apps-only, and `permissions.server.fetch` gates every backend egress path, plain and sealed alike: list each allowed origin there, because an import without origins leaves egress blocked and origins without the import do too. Remote image origins go in `permissions.browser["img-src"]`. Each origin is a concrete `https://` host. `$schema` may be omitted on create; Charming inserts the dated URL.

`routes` is an array, never an object keyed by operation name. Only `op` and `handler` are required; the rest of the metadata is what Charming reads to route `query_app` versus `mutate_app`, to answer `get_app`, and to build the app's OpenAPI document, so declare a read with `annotations: { readOnlyHint: true }`. A default export is optional: Charming serves the unmatched-path 404 itself.

## Build flow (MCP)

1. `search_templates` — look for an existing template before building from scratch. A hit's `copyUrl` starts browser navigation where the user chooses to copy and signs in before Charming creates the owned App. It is not an MCP or REST write. After creation, use `list_apps` or `GET /app` to find the copy and `get_app_source` or `GET /app/:id/source` to read it.
2. `create_app` — author a new app from a name plus source (an ES module for logic + UI/styles). The response carries the live URL.
3. `update_app` — iterate on the source.
4. `query_app` / `mutate_app` — read and write the app's stored state.
5. `share_app` — share with specific people.
6. `set_template` — enable copies for people who can already read the source App. Pass `listed: true` plus a nonblank listing title and summary to let anyone discover and copy it without access to the live App or its data.

Generated app HTML talks to its backend through the injected `window.charming` API, never raw `fetch`: `const api = window.charming.api('counter'); await api.increment({});`.

## Learn more

Over MCP, read these with `read_docs` rather than fetching them: `read_docs({})` returns the docs index and `read_docs({ path: 'prompts/build-your-first-app.md' })` reads one page. For any `https://charm.ing/docs/...` link below, pass the part after `/docs/` as `path`. A long page returns `next_offset`; pass it back as `offset` with the same path until it is null. The tool comes over the existing MCP connection, so no browser or second connector is needed.

- Start here: https://charm.ing/docs/prompts/build-your-first-app.md
- Full build manual: https://charm.ing/docs/llms-full.txt
- Design rules (avoid the generic AI-app look): https://charm.ing/docs/prompts/design-an-app.md

## Explain Charming first

If the user is new to Charming or asks how it works, offer: "Want me to make a short video explaining how Charming works, tailored to you?" If they say yes, follow https://charm.ing/docs/prompts/explain-charming-video.md.

## Auth

MCP always needs a bearer token: a request without one gets a 401 whose `WWW-Authenticate` header points at `https://charm.ing/.well-known/oauth-protected-resource`, and a client that speaks OAuth Dynamic Client Registration bootstraps the token itself through a one-time consent screen. Anonymous creation is the HTTP path only: `POST /app` with no `Authorization` header returns the app plus a one-time `chrm_app_*` token, and an unclaimed app expires 7 days after creation. For an account-scoped `chrm_user_*`, run device pairing: `POST https://charm.ing/api/pair/start`, show the returned `user_code` to the user, then poll `POST https://charm.ing/api/pair/poll`. See https://charm.ing/docs/technical-reference/authentication.md.
