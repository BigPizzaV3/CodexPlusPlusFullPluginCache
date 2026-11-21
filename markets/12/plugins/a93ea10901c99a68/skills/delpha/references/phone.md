# Phone — validate, normalize & enrich

## Table of contents
- When to use
- Tools
- Inputs & modes
- Reading the result
- Scores & thresholds
- Recipes
- Traps to avoid

## When to use
Use this capability to validate, normalize, and enrich a single phone number. It
returns the number in canonical E.164 form, resolves the country, and adds line
type, carrier and timezone, with reachability expressed through the scores. Reach for it when cleaning CRM
records, gating sign-ups, or routing calls/SMS. For company or contact
attributes use a sibling capability — [email](email.md), [name](name.md), or
[Salesforce](salesforce.md) write-back.

## Tools
A submit/get pair, called in sequence (the tool does **not** search — it checks a number you already hold):
- `validateAndNormalizePhone(...)` — submits an async job and returns a `job_id`. It does not mutate
  your data, but every accepted production submission is a separate charged job.
- `getPhoneResult(job_id)` — returns the result envelope. Read-only; never charges or mutates.

The MCP `getPhoneResult` holds the connection open and polls the upstream job
internally, so a single call usually returns the final result. Typical latency is
~5 seconds. Do NOT re-call while it is returning — only re-call if `status_code`
is still `202` after it returns (rare), and wait 1-2s first. Re-calling early
renders a duplicate result widget.

## Inputs & modes
Pass these to `validateAndNormalizePhone`:

| Field | Required | Notes |
|---|---|---|
| `phone` | yes | The number to validate. |
| `country_code` | conditional | ISO 3166-1 alpha-2, e.g. `FR`, `US`, `GB`. The only country field the MCP tool accepts. |
| `country` | conditional, **REST only** | Country display name in English, e.g. `France`. `POST /v1/phone` accepts it as an alternative to `country_code`; the MCP schema is closed and rejects it. |

Two modes, decided by the form of `phone`:
- **E.164 form** (e.g. `+33672557378`) — self-locating. The country is
  auto-detected; do NOT pass `country` or `country_code`.
- **National form** (e.g. `0672557378`) — ambiguous. You MUST also pass `country_code`
  (or, on REST, `country`) so the number can be normalized.

Never invent other fields; the MCP schema accepts only `phone` and `country_code`, REST adds `country`.

## Reading the result
Every `getPhoneResult` returns this envelope:

```json
{ "message": "<human string>", "status": "SUCCESS" | "ERROR",
  "status_code": 200, "result": { ... }, "process_time": 4.9 }
```

- `status_code` `200` = done (`result` populated); `202` = still running (`result` null). Error
  outcomes include `400` bad input plus the common auth, credit, lookup and delivery failures in
  the [REST status table](rest-api.md#status-codes).

On success, `result` carries:
- `normalized_value` — the number in E.164 form (use this as the canonical value).
- `phone_type` — one of `FIXED_LINE`, `MOBILE`, `FIXED_LINE_OR_MOBILE`,
  `TOLL_FREE`, `PREMIUM_RATE`, `SHARED_COST`, `VOIP`, `PERSONAL_NUMBER`,
  `PAGER`, `UAN`, `VOICEMAIL`.
- `carrier` — carrier name.
- `timezone` — IANA timezone(s).
- `zone` — resolved country as ISO 3166-1 alpha-2.
- `area` — resolved country display name.
- `scores` — see below.

## Scores & thresholds

The common score shape has continuous `accuracy` (`-1..1`) and `completeness` (`0..1`), discrete
`validity` (`-1`/`0`/`1`) and discrete `consistency` (`0`/`1`). Treat `-1` as missing. Apply the
bands below only to continuous scores; branch on the discrete values exactly.

Suggested decision thresholds (tunable):
- `>= 0.8` — auto-accept.
- `0.5` ≤ score < `0.8` — route to human review.
- `< 0.5` — reject.

Require `validity == 1` to treat the number as valid; use `phone_type`
to gate channel (e.g. only SMS to `MOBILE` / `FIXED_LINE_OR_MOBILE`).

## Recipes
MCP — validate an E.164 number (no country needed):

```json
{ "phone": "+33672557378" }
```

MCP — validate a national number (country required):

```json
{ "phone": "0672557378", "country_code": "FR" }
```

Then call `getPhoneResult` with the returned `job_id`.

REST — submit then fetch:

```bash
# 1) Submit -> HTTP 202 { job_id, status, status_code, message }
JOB=$(curl -sX POST https://api.delpha.io/v1/phone \
  -H "Authorization: Bearer $DELPHA_API_KEY" -H "Content-Type: application/json" \
  -H 'User-Agent: my-integration/1.0' \
  -d '{"phone":"0672557378","country_code":"FR"}' | jq -r .job_id)

# 2) Poll -> 202 while running, 200 when done
curl -s https://api.delpha.io/v1/phone/$JOB \
  -H "Authorization: Bearer $DELPHA_API_KEY"
```

`$DELPHA_API_KEY` is a `dlp_…` key from `https://app.delpha.ai` → **Developer → API
keys**. See [rest-api.md](rest-api.md).

## The synchronous route

`GET /v1/phone` answers in the response — no `job_id`, no polling — and is the right call when you
need one number checked inside a request you are already serving.

```bash
curl -s -G https://api.delpha.io/v1/phone \
  -H "Authorization: Bearer $DELPHA_API_KEY" \
  -H 'User-Agent: my-integration/1.0' \
  --data-urlencode 'phone=0672557378' \
  --data-urlencode 'country=FR'
```

Same inputs as the async route (`phone`, plus `country` — a name or an ISO code — for national
format). The `result` is close but **not identical**: it carries `normalized_value`, `phone_type`,
`carrier`, `timezone`, `zone`, `area` and a boolean **`valid`**, and it has **no `scores` object**.
So the `>= 0.8` policy does not apply here; branch on `valid` and `phone_type`. It costs the same
one credit and can still return `402`.

Use the async pair when you are checking many numbers or want the score breakdown; use this one for
a single in-line check.

## Traps to avoid
- **Do not send national-format numbers without `country_code` (REST: `country` or `country_code`).** They cannot be normalized and the job returns a `400`.
- **Do not pass `country`/`country_code` alongside an E.164 number.** It is redundant; the `+` prefix is already self-locating and a mismatched hint can fight the detected country.
- **Do not treat a `-1` score as low quality.** It means the engine could not compute that dimension — handle it as missing data, not as a reject signal.
- **Do not re-call `getPhoneResult` while it is still returning.** Re-call only if `status_code` is still `202` after it returns, after a 1-2s wait; early re-calls render duplicate widgets.
- **Do not store the raw input as canonical.** Persist `normalized_value` (E.164) so downstream dialing, dedup, and matching stay consistent.
- **Do not infer SMS-capability from country alone.** Check `phone_type` — `FIXED_LINE`, `VOIP`, and `TOLL_FREE` are not reliable SMS targets.
