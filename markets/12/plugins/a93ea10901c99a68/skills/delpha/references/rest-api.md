# REST API — auth, routes, batch, webhooks

Base URL: `https://api.delpha.io`. Same engines as the [MCP server](mcp.md), same payloads.
Prefer REST from code and pipelines; prefer MCP from an agent.

## Authenticate

```sh
curl -s https://api.delpha.io/v1/email \
  -X POST \
  -H "Authorization: Bearer $DELPHA_API_KEY" \
  -H 'User-Agent: my-integration/1.0' \
  -H 'Content-Type: application/json' \
  -d '{"email":"victor.goubet@delpha.io"}'
```

- **Delpha API key** (`dlp_…`) — the current path. Create one at `https://app.delpha.ai` →
  **Developer → API keys**. Signup is self-service; a new team starts with free credits.
- **OAuth 2.0 client-credentials** — the legacy path for Salesforce-org callers. Exchange
  credentials at `https://secure.delpha.io/oauth2/token` for a bearer token with scope
  `api/access`. Existing integrations keep working; new ones should use a key.

⚠️ Two gotchas that cost real time:

- **Always send an explicit `User-Agent`.** The API sits behind a WAF that rejects some default
  client user-agents with a `403` that is not an auth failure.
- **The published OpenAPI document only declares the legacy `oauth2` scheme.** The `dlp_` bearer
  path is real and is what the console issues; the spec has not caught up.

## Key restrictions

A key can carry three optional restrictions, set at creation and editable in the console:

| Restriction | Absent means |
|---|---|
| **Scopes** — `dataquality.<usecase>.<single\|batch>` | full access |
| **TTL** — 1–730 days, default 365 | — |
| **Credit ceiling** — per `forever`/`day`/`week`/`month` window | unlimited |

`single` covers a usecase's submit route, its result puller and its synchronous route; `batch`
covers the batch pair. Usecases: `email`, `website`, `phone`, `name`, `legal-id`, deprecated
`linkedin`, `linkedin-profile`, `linkedin-company-page`, `ultimate`. A scoped key that reaches a
route it does not hold gets `403`.

One wrinkle in that list. The generic `linkedin` scope and routes are **deprecated, not removed**:
the console no longer offers that scope, but existing keys keep working and stay editable. New
integrations use `linkedin-profile` or `linkedin-company-page`.

The same key authenticates the MCP server, and the same scopes apply there.

## The async pattern

```
POST /v1/<usecase>            → 202 { "job_id": "…", "status": "SUCCESS", "status_code": 202 }
GET  /v1/<usecase>/{job_id}   → 202 while running, 200 with "result" when done
```

Submission mutates nothing of yours, so retrying an ambiguous transport failure is safe — but it
is **not billing-idempotent**: each accepted submission is a new, separately charged job. Poll the
result route with backoff, or register a [webhook](#webhooks) and stop polling.

## Routes

| Usecase | Submit | Poll |
|---|---|---|
| Email | `POST /v1/email` | `GET /v1/email/{job_id}` |
| Phone | `POST /v1/phone` | `GET /v1/phone/{job_id}` |
| Name | `POST /v1/name` | `GET /v1/name/{job_id}` |
| Website | `POST /v1/website` | `GET /v1/website/{job_id}` |
| Legal ID | `POST /v1/legal-id` | `GET /v1/legal-id/{job_id}` |
| Ultimate parent | `POST /v1/ultimate` | `GET /v1/ultimate/{job_id}` |
| LinkedIn profile | `POST /v1/linkedin-profile` | `GET /v1/linkedin-profile/{job_id}` |
| LinkedIn company page | `POST /v1/linkedin-company-page` | `GET /v1/linkedin-company-page/{job_id}` |

`GET /v1/phone` is **synchronous** — no `job_id`, the answer is in the response.
`POST /v1/email-insights` is also synchronous and REST-only; see
[email.md](email.md#email-body-insights-rest-only).

The generic `POST /v1/linkedin` and `GET /v1/linkedin/{job_id}` routes, plus their batch pair,
remain in production for compatibility but are marked deprecated. Do not start a new integration
on them.

## Batch

The validation usecases have batch pairs:

```
POST /v1/<usecase>/batch      { "items": [ …1..100 single-route payloads… ] }  → 202 + job_id
GET  /v1/<usecase>/batch/{job_id}
```

Current batch pairs exist for `email`, `website`, `phone`, `name`, `legal-id`, `ultimate`,
`linkedin-profile` and `linkedin-company-page`. The deprecated generic `linkedin` batch pair also
remains for compatibility.

More than 100 items is a `422` — chunk the list and submit many batches. The pull returns:

```json
{ "status_code": 200, "message": "97/100 items succeeded",
  "counts": { "total": 100, "succeeded": 97, "failed": 3 },
  "result_url": "https://…presigned…",
  "result_data": { "items": [ { "dispatch_key": { "record_id": "<job_id>#0" }, "result": { } } ] },
  "item_count": 100, "processed_count": 100 }
```

- `result_data` is inlined only when the payload is small; otherwise fetch `result_url` (presigned,
  expiring).
- **Results correlate to inputs by position** — `record_id` is `<job_id>#<index>`. Keep your own
  index → source-row map; there is no caller-supplied correlation id.
- A batch charges price × item count and settles only the items that succeeded; the rest are
  refunded. See [credits-and-limits.md](credits-and-limits.md).
- Batches can run for hours. Use webhooks rather than a polling loop.

## Webhooks

Register an endpoint in the console under **Developer → Webhooks** and subscribe it to
`dataquality.<usecase>.<sent|done|error>`. A batch run is the usecase plus a `-batch` suffix
(`dataquality.email-batch.done`). This is how a pipeline learns a job finished without polling.

## Status codes

| Code | Meaning |
|---|---|
| `200` | Job done — `result` populated. |
| `202` | Accepted (on submit) or still running (on poll). |
| `400` | Bad input. Fix the arguments; do not retry unchanged. |
| `401` | The `Authorization` header is missing, so API Gateway never invokes the authorizer. |
| `402` | Out of credits, or the key's own ceiling is spent. Not retryable — top up. |
| `403` | A present credential was rejected (malformed, invalid, expired or revoked), the key lacks the route scope, or the WAF rejected the request. |
| `404` | No job exists for that id. Do not infer whether another tenant owns it. |
| `409` | The credit reservation expired before the completed result could be delivered; resubmit knowingly as a new charged job. |
| `422` | Unprocessable input — for example more than 100 batch items or a positively identified unsupported legal-ID registry. |
| `500` | A worker/engine reported a domain failure, or the puller could not parse/render the stored result. The exact generic fallback `"Failed to retrieve job."` is a delivery failure, not proof the underlying record is invalid. Do not retry by default. |
| `502` | Submission could not dispatch to the backend. The accepted job was not created; investigate before retrying. |
| `504` | The job exceeded the puller's timeout. Record it and do not loop. LinkedIn is the one documented case where one charged resubmission can be reasonable; see [linkedin.md](linkedin.md). |

## Development preview — not available on production

As of **2026-09-09**, DDQ-3227 is on DelphaAPI `dev` but not `main`, and none of its contract is
served by `api.delpha.io`. Do not put these behaviors into production code yet:

- optional `Idempotency-Key` on submit routes, scoped to the caller for 24 hours; an identical body
  can replay the original `job_id`, while reuse with another body or an in-progress claim is `409`;
- documented `429` rate-limit responses and `Retry-After` guidance;
- typed error bodies with `code`, `request_id` and optional `doc_url`;
- the declared OpenAPI `apiKey` security scheme and the `x-polling` / `x-mcp-annotations` metadata.

## See also

- [mcp.md](mcp.md) — the same capabilities as agent tools.
- [credits-and-limits.md](credits-and-limits.md) — what a call costs.
- [security.md](security.md) — credential handling and PII.
