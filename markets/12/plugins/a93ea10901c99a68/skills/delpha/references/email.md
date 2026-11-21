# Email — find, validate & enrich

## Table of contents
- When to use
- Tools
- Inputs & modes
- Reading the result
- Scores & thresholds
- Recipes
- Traps to avoid

## When to use
Use this capability to verify that a professional email address is deliverable and to qualify its
domain, or to discover the most likely address for a known person at a known company. Reach for it
before sending outreach, deduplicating a CRM, or enriching a lead. To validate the broader contact,
see the sibling [Name](name.md), [Phone](phone.md), and [Website](website.md) references; to push the
result into a record, see [Salesforce](salesforce.md).

## Tools
- `findAndValidateEmail` — submits a job, returns `{ job_id, message, status, status_code }`.
- `getEmailResult` — takes `job_id`, returns the final result envelope.

The MCP `getEmailResult` holds the connection open and polls the upstream job internally, so a single
call usually returns the final result. Typical end-to-end latency is ~5 seconds.

## Inputs & modes
All four input fields are optional individually, but at least one mode must be fully satisfied.

| Field | Type | Notes |
|-------|------|-------|
| `email` | RFC 5321 mailbox | The address to verify, e.g. `victor.goubet@delpha.io`. |
| `first_name` | string | Person's given name. |
| `last_name` | string | Person's family name. |
| `website` | company website URL | Company signal; the engine extracts and qualifies the domain. |

**Validation mode:** provide `email` alone to verify deliverability and qualify the domain.

**Recommendation mode:** provide `first_name` AND `last_name` AND `website` — all three are
required. Partial recommendation input (e.g. a name without a website) is rejected with `400`.

**Both paths:** supply an `email` and the full recommendation triple to run validation and
recommendation in the same job.

## Reading the result
Every `getEmailResult` call returns this envelope:

```json
{ "message": "...", "status": "SUCCESS", "status_code": 200, "result": { }, "process_time": 4.8 }
```

- `status_code`: `200` job done (`result` populated); `202` still running (`result` null). Error
  outcomes include `400` bad input plus the common auth, credit, lookup and delivery failures in
  the [REST status table](rest-api.md#status-codes).

On success, `result` contains:

- `normalized_value` — the validated/canonical email address.
- `email_status` — `"Valid"` | `"Invalid"` | `"Unknown"`.
- `email_domain_qualification` — `"nominative@pro"` | `"catchall@pro"` |
  `"nominative@perso"` | `"catchall@perso"` | `"Unknown"`. A `catchall` value means the domain
  accepts fake local-parts, so a `Valid` status is weaker evidence than on a nominative domain.
- `label` — top-level summary: `"OK"` | `"No"` | `"OddFormat"`.
- `email_domain` — the qualified domain (the field is `email_domain`, not `domain`).
- `provider` — the mail provider, when identified.
- `scores` — `validity`, `completeness`, `accuracy`, `consistency`.
- `suggestions` — ranked alternative addresses inferred from the input, each `{ value, score }`.
- `website_domain`, `website_domain_qualification` and `suggestions_from_website` — the same
  treatment applied to the company website you passed. Recommendation mode fills these; validation
  mode usually leaves them empty. When `suggestions` is thin, `suggestions_from_website` often is
  not.

When `email_status` is `Unknown` or `label` is `No`, surface the scored `suggestions` for review
rather than discarding the record — and **never silently replace the failed address** with the top
suggestion. A suggestion is a candidate for a person to accept, not a validated mailbox.

## Scores & thresholds

In the common score shape, `accuracy` is continuous (`-1..1`), `completeness` is continuous
(`0..1`), `validity` is the discrete integer `-1`/`0`/`1`, and `consistency` is the discrete
integer `0`/`1`. Treat `-1` as missing where allowed. Branch on the discrete fields exactly; apply
the tunable bands below only to `accuracy`, `completeness`, or a suggestion `score`:

- `>= 0.8` — auto-accept.
- `0.5` ≤ score < `0.8` — route to human review.
- `< 0.5` — reject.

## Recipes

Recommendation mode via MCP (`findAndValidateEmail` arguments):

```json
{ "first_name": "Victor", "last_name": "Goubet", "website": "https://delpha.io/" }
```

Then call `getEmailResult` with the returned `job_id`.

Validation mode via REST (POST then GET):

```bash
# Submit: HTTP 202
JOB=$(curl -s -X POST https://api.delpha.io/v1/email \
  -H "Authorization: Bearer $DELPHA_API_KEY" -H 'Content-Type: application/json' \
  -H 'User-Agent: my-integration/1.0' \
  -d '{"email":"victor.goubet@delpha.io"}' | jq -r .job_id)

# Poll: HTTP 202 while running, HTTP 200 when done
curl -s https://api.delpha.io/v1/email/$JOB \
  -H "Authorization: Bearer $DELPHA_API_KEY"
```

## Email body insights (REST only)

`POST /v1/email-insights` is a synchronous production route, not an MCP tool. Send
`{"email_bodies": ["..."]}`. It returns one result per successfully analyzed body with optional
`name`, `phone`, `mobile`, `title`, `company`, `department`, `address`, `social_media` and
`out_of_office`, plus required `confidence`. `social_media[].owner` is `"sender"` or `"company"`;
`out_of_office` carries `status`, optional `start_date` and optional `end_date`. The route returns
`200`, `400` or `500` and has no async `job_id`.

Email bodies can contain substantially more personal and confidential data than an address. Send
only bodies the user is entitled to process, minimize quoted history, and never log the payload.

## Traps to avoid
- **Do not call `getEmailResult` in a loop.** A single MCP call already polls internally for up to
  ~3 minutes to absorb slow anti-scraping domains (e.g. `anthropic.com`); re-calling early renders a
  duplicate result widget. Only re-call if `status_code` is STILL `202` after it returns, and wait
  at least 30 seconds first.
- **Do not treat a `-1` score as a bad address.** It signals "could not compute" — handle it as
  missing data and fall back to other scores or `email_status`.
- **Do not submit partial recommendation input.** A name without a `website`, or a `website` without
  both names, returns `400`. Send all three together or use validation mode with `email` alone.
- **Do not infer domain invalidity from the exact `500` message `"Failed to retrieve job."`.** That
  generic fallback means the puller could not retrieve, parse or render the stored result. A
  worker-supplied `500` may instead describe a domain-specific engine failure. Neither should be
  retried in a loop.
- **Do not trust a `Valid` status on a catch-all domain as a confirmed inbox.** `catchall@pro` and
  `catchall@perso` domains accept fake local-parts, so weight the result lower and check continuous
  `accuracy` plus the discrete consistency signal.
- **Do not retry `findAndValidateEmail` for fear of side effects.** Production submissions do not
  mutate your records, but each accepted call mints a fresh, separately charged `job_id`;
  `getEmailResult` is read-only and never charges or mutates.
