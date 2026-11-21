# Workers Free deployment runbook

Prepared 11 October 2026. Source and local checks are ready; no production
account, endpoint or verification token has been configured. Commands below
are operator instructions, not actions performed by preparing this folder.

## 1. Select the account and hostname

Leave the Zero Trust MCP Portals screen. In the main Cloudflare account,
open Workers & Pages. Confirm Workers Free, the intended account ID, and the
account's existing workers.dev subdomain. Workers Free's 100,000 requests/day
is shared by account workloads, with a 10 ms CPU allowance per invocation.
Domain registration, model APIs and other paid products are not included here.

Use a distinct Worker name such as token-weather-budget only if it is unused.
If a Worker with that name exists, inspect it before choosing whether to update
that same project or use a different name. Do not overwrite an unrelated Worker.
The actual hostname is <worker>.<account-subdomain>.workers.dev, not the login
email. Its PUBLIC_ORIGIN is the HTTPS origin without a trailing slash or /mcp.

## 2. Connect locally when deployment is requested

Run from this source folder, using the pinned local Wrangler:

```sh
WRANGLER_SEND_METRICS=false node node_modules/wrangler/bin/wrangler.js login --scopes account:read user:read workers_scripts:write
WRANGLER_SEND_METRICS=false node node_modules/wrangler/bin/wrangler.js whoami
```

The operator signs into the intended account in the browser and grants the
Wrangler login. No browser automation or application modification is needed.
Passwords, OAuth access tokens and API tokens stay out of chat and archives.
Select the explicit account shown by whoami when multiple accounts exist.
This profile uses the scripts-specific permission rather than the broader
workers:write label. Missing unrelated scopes in whoami are not a reason to
request all default product permissions. offline_access is added by Wrangler
for credential refresh. The operator reviews the browser consent before grant.

## 3. Prepare a separate config and inspect it

Set these variables to the real, confirmed values; the strings here are labels
and cannot be deployed as written:

```sh
TOKEN_WEATHER_ACCOUNT_ID='REPLACE_WITH_CONFIRMED_ACCOUNT_ID'
TOKEN_WEATHER_ORIGIN='REPLACE_WITH_CONFIRMED_HTTPS_ORIGIN'
node scripts/configure-origin.mjs --origin "$TOKEN_WEATHER_ORIGIN" --account-id "$TOKEN_WEATHER_ACCOUNT_ID" --output wrangler.production.json
node scripts/preflight.mjs --config wrangler.production.json
npm run check
npm test
WRANGLER_SEND_METRICS=false node node_modules/wrangler/bin/wrangler.js deploy --dry-run --config wrangler.production.json --outdir build/production-dry-run
```

Config creation never overwrites an existing choice. It gives the two native
limiters separate integer namespace labels; inspect other Workers' limiter
configuration to avoid accidental reuse. Set --namespace-base to a confirmed
unused pair if needed. Random labels are not account/resource verification.
Do not include wrangler.production.json or operator secrets in a public ZIP.

## 4. Deploy after target/account confirmation

```sh
WRANGLER_SEND_METRICS=false node node_modules/wrangler/bin/wrangler.js deploy --config wrangler.production.json
```

This is the cloud mutation. It creates/updates the selected Worker. Deployment
does not upload a plugin ZIP or submit OpenAI review. Verify the returned URL
equals PUBLIC_ORIGIN; a mismatch is a configuration problem, not a reason to
disable origin protection. Inspect account request, CPU and error metrics using
synthetic calls. Local wall-clock timings and dry-run size do not establish
production CPU compliance. Optimise/pause on free-limit failures; no paid
upgrade is authorised by this runbook.

## 5. Complete OpenAI verification and final package setup

Use the real URL ending /mcp as a universal public MCP endpoint. The service
is anonymous numeric arithmetic; auth.type=none is truthful. It is not an
account login service, and no API key should be embedded in mcp.json.

When the OpenAI portal supplies the domain challenge, set its exact value:

```sh
WRANGLER_SEND_METRICS=false node node_modules/wrangler/bin/wrangler.js secret put DOMAIN_VERIFICATION_TOKEN --config wrangler.production.json
```

The command writes the operator-supplied challenge to this Worker. Serve the
exact plain text at the portal's URL, normally
/.well-known/openai-apps-challenge on the same hostname. It must be publicly
reachable without Cloudflare Access, a bot challenge or a login redirect.
The verification text is public, not an account credential. If the portal does
not permit this workers.dev host, use the user's controlled domain or ask
OpenAI about the permitted challenge origin; do not assert verification passed.

Before building the HTTPS plugin copy, independently verify /health,
initialisation, tools/list, and all five synthetic positive cases against the
actual endpoint. Run the existing outer build-cloudflare-mcp-package.py with
--public-endpoint and a fresh --output-dir; it also probes live schema and a
sample calculation. This source folder alone is not an upload-ready plugin.
Complete the real host cases and video, policy updates, portal scans, identity
and relevant local-helper review. An existing skills-only draft cannot simply
be converted by adding MCP; preserve it and confirm the initial With MCP path.

Choose the final hostname before public review. OpenAI's maintenance guidance
requires a new plugin when a published MCP origin changes. A later switch from
workers.dev to a personal domain therefore has a publication consequence,
even if using that already-owned domain adds no Workers hosting charge.

Sources: [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/),
[Workers routing](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/),
[OpenAI package format](https://developers.openai.com/plugins/build/plugins),
[OpenAI submission](https://developers.openai.com/plugins/deploy/submission),
[OpenAI review](https://developers.openai.com/plugins/deploy/app-review).
