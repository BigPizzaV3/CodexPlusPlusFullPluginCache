# Token Weather budget MCP for Cloudflare Workers

Version 1.0.0. Offline source preparation for Workers Free; nothing is deployed
by installing dependencies, building, testing or creating a plugin ZIP.

The only business tool is `plan_context_budget`. Its inputs are five optional,
bounded scalar token counts and fixed source enums. It calculates current
headroom, next-task increase plus a separate output reserve, and five future
turns from a supplied growth-rate estimate. It accepts no chat/turn records,
prior-turn arrays, local paths, model names, account identifiers or credentials.
It does not call a model, inspect local Codex data, change settings or persist
business data. MCP's required transport metadata is separate from tool inputs.

## Local verification

Use Node.js 22+ and the checked-in lockfile:

```sh
npm ci --ignore-scripts --no-audit --no-fund
npm run check
npm test
npm run dev:local
```

The last command starts only `http://127.0.0.1:8787/mcp`; stop it with Ctrl+C.
It does not register a plugin or connect to Cloudflare. Tests use synthetic
values in the real local Workers runtime and both legacy/modern MCP clients.
The preserved Python reference is used only for arithmetic regression tests;
Python and all local weather/replay/checkpoint modules are excluded from the
Worker bundle. Generated dev files and dependency directories are not releases.
The arithmetic oracle test needs Python 3.9+; TOKEN_WEATHER_TEST_PYTHON can select
an existing interpreter. Python is not a cloud runtime dependency.
Wrangler local developer tools may record diagnostic traces; use synthetic
values for development and keep `.wrangler/` out of public archives.

`PUBLIC_ORIGIN` is blank in the source config. A non-local origin is rejected
until an explicitly chosen HTTPS origin is configured. `/health` provides a
fixed diagnostic response; `/.well-known/openai-apps-challenge` returns only
the exact separately supplied public domain token, otherwise 404. No token or
Cloudflare account ID is supplied by this preparation.

See [security controls](SECURITY.md) and the [deployment runbook](DEPLOYMENT.md).
The screenshot's Zero Trust MCP Portals page aggregates existing MCP servers;
this source is deployed through Workers & Pages with Wrangler instead.

## Free-plan scope

No Workers AI, database, KV, Durable Object, queue, scheduled task, paid model
API or private-account integration is configured. Application observability
is disabled by default and source code logs no request bodies, numeric inputs,
headers or raw errors. Cloudflare can still process transport/provider metadata
under its policies and the operator's settings; this is not a zero-log promise.
Two native rate-limit bindings keep short-lived infrastructure counters keyed
by an IP digest and a fixed service key. They do not store business inputs.
The digest is pseudonymous metadata, not an anonymity guarantee.

Workers Free currently allows 100,000 requests/day and 10ms CPU per invocation.
Local functional tests and wall-clock timings do not certify production CPU
usage, availability, abuse resistance, residency or future pricing. After a
separately authorised deployment, confirm the account remains on Free and
measure real CPU before treating the endpoint as production-ready. If it fails
the free limits, optimise or pause rather than silently enabling a paid plan.

## Later deployment and package finalisation

Deployment is a separate action. First confirm the intended account and actual
Worker hostname. Inspect any existing Worker with that name before replacing
it. Prepare a separate config with the confirmed origin using:

```sh
node scripts/configure-origin.mjs --origin "$TOKEN_WEATHER_ORIGIN" --account-id "$TOKEN_WEATHER_ACCOUNT_ID" --output wrangler.production.json
node scripts/preflight.mjs --config wrangler.production.json
```

This only writes a new config and checks its syntax; it does not deploy or
verify ownership. Supply the portal's exact public domain challenge value
through the operator's configuration when that later setup is authorised.
The generated config assigns two local namespace integers; check that they
are unused in the chosen account. These are limiter labels, not provisioned
cloud resources or verified account details. The preflight is local and does
not establish Free-plan status. Existing files are never overwritten.
The prepared plugin ZIP points only at the tested loopback endpoint. It is
not a public upload candidate. Once the real service is separately deployed,
the outer package builder's `--public-endpoint` mode verifies health and the
actual tool schema, writes a fresh HTTPS MCP configuration and creates a new
archive. Never insert a guessed production URL or overwrite an old ZIP.

See the release's review cases, privacy draft and recording plan. There is no
OAuth login in this numeric-only service. Adding private account data, writes
or a new capability requires a separate implementation and review.

Original project software uses MIT. Bundled SDK dependencies retain their
own licences; run `npm run build` to produce the licence notices alongside
the deployable bundle.

Sources: [Cloudflare MCP handler](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/),
[Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/),
[OpenAI submission](https://developers.openai.com/plugins/deploy/submission).
