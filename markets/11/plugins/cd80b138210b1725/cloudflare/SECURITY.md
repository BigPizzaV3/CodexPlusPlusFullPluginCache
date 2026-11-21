# Security controls for the numeric budget service

Prepared 11 October 2026. This describes implemented controls, not an external
security audit or a guarantee of public availability.

## Public access and data boundary

The service has one read-only arithmetic tool and no private account data,
business database or outbound fetch. Anonymous access is intentional; the
plugin's MCP manifest declares auth.type=none. Adding account access, writes,
cloud synchronisation or persistent user settings requires an OAuth design.
Do not put a Cloudflare Access interactive login or browser challenge in front
of the MCP or domain-verification route for this public profile. Such a gate
can block OpenAI's clients and review scanners. Origin validation is a browser
defence, not authentication. Requests without Origin remain supported.

The Worker validates the exact configured HTTPS origin. Preview URLs are
disabled. Unknown routes, query parameters, Authorization headers, compression,
invalid JSON, duplicate keys and unsupported RPC calls are refused. Tool
arguments are bounded scalar counts and fixed source enums; extra properties,
arrays, paths, transcripts and credentials are rejected without being echoed.
Streamed bodies and Content-Length are limited to 16 KiB. No dynamic code
execution, filesystem access or arbitrary target URL is present.

Responses include no-store, nosniff, no-referrer and a restrictive CSP. HTTPS
responses include HSTS for the endpoint hostname, without includeSubDomains.
The JSON/SSE endpoint does not include an embedded UI.

## Abuse limits and their practical limits

Two Workers rate-limit bindings operate before body parsing on the configured
production origin, including health, domain challenge and invalid routes:

| Binding | Initial threshold | Scope |
| --- | --- | --- |
| MCP_IP_LIMITER | 120 requests per 60 seconds | IP digest at each Cloudflare location |
| MCP_SERVICE_LIMITER | 1,200 requests per 60 seconds | Whole service at each Cloudflare location |

The public edge supplies CF-Connecting-IP. X-Forwarded-For and arbitrary client
RPC IDs are never used for the key. An absent/invalid IP shares the unknown
bucket. Digests reduce raw-address exposure in limiter keys; they remain
potentially identifiable metadata. Missing/failing bindings return 503.
Excess traffic returns 429 with Retry-After: 60 and no request-body parsing.
Loopback development may run without bindings; this bypass is not allowed for
a public origin.

Cloudflare describes these counters as per-location, permissive and eventually
consistent. They are neither a global cap nor accurate monthly accounting.
An invocation rejected by application code still consumes Workers requests.
Distributed abuse can exhaust Free's daily quota. Shared client egress IPs can
also affect legitimate users; inspect aggregate metrics before adjusting limits.
This profile does not promise indefinite uptime or a hard 100,000/month cap.

With workers.dev, this source does not claim control of a zone WAF or enable
paid WAF/bot products. If a controlled custom domain is used in a future edition,
add applicable pre-Worker zone rules and protect/disable alternative routes.
Changing a published MCP origin requires a new OpenAI plugin review path;
do not silently repoint an approved version to a new hostname.

## Operations and credentials

Production config creation requires a selected account ID and exact hostname.
Local preflight refuses extra bindings, alternate entry points, enabled previews
and logging changes. Verify the account is on Workers Free before deploying;
the preflight cannot inspect billing. Never automatically upgrade the plan.

Use Wrangler browser OAuth in the operator's normal browser, or a narrowly
scoped token supplied through a local secret mechanism. Do not send passwords
or API tokens in chat, put them in a plugin ZIP, or alter an installed browser.
The domain-challenge token is deliberately public; use the secret/configuration
channel simply to keep operator configuration out of source releases.

Application observability is disabled and code does not log payloads or raw
errors. Cloudflare's provider logs and counters are outside this source's
retention control. Use account aggregate request/CPU/error metrics initially.
If enabling diagnostic logging later, update disclosure and review redaction
before use. Do not log numerical inputs, transcripts, headers or credentials.

On abuse or CPU-limit failure, pause/remove this Worker's route using its
dashboard controls, investigate and optimise. Preserve previous Worker
versions for rollback. Other Workers and installed local plugins are outside
the scope of these controls.

Sources: [Workers rate limiting](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/),
[Workers limits](https://developers.cloudflare.com/workers/platform/limits/),
[OpenAI authentication](https://developers.openai.com/plugins/build/auth),
[OpenAI review and maintenance](https://developers.openai.com/plugins/deploy/app-review).
