# LinkedIn — find, validate & enrich

## Table of contents
- When to use
- Tools
- Inputs & modes
- Reading the result
- Scores & thresholds
- Recipes
- Traps to avoid

## When to use
Use this capability to resolve a person or company to its canonical LinkedIn URL, or to confirm that a URL you already hold belongs to the right person/company. Reach for it when enriching a CRM contact or account, deduplicating profiles, or vetting an inbound lead. For finding the person's name itself see [name](name.md); for the company website see [website](website.md); to sync results back, see [Salesforce](salesforce.md).

## Tools

- People: `findAndValidateLinkedInProfile` → `getLinkedInProfileResult`.
- Companies: `findAndValidateLinkedInCompanyPage` → `getLinkedInCompanyPageResult`.

These are the names production MCP serves. The generic `findAndValidateLinkedin` /
`getLinkedinResult` operations remain deprecated REST compatibility routes, but production MCP
hides them. Do not call the generic names through MCP.

The MCP result tool holds the connection open and polls the upstream job internally, so a single
call usually returns the final result. Typical latency is ~10 seconds.

## Inputs & modes
All fields are optional in the schema; you must supply enough to pick a mode. Document only these fields — do not invent others.

| Field | Type | Use |
|-------|------|-----|
| `url` | URI | A LinkedIn profile (`.../in/...`) or company page (`.../company/...`) to validate. |
| `first_name` | string | Person's given name. |
| `last_name` | string | Person's family name. |
| `email` | email | **REST only** (profile route). Contributes only its domain, like `website`; the MCP schemas are closed and reject it. |
| `company_name` | string | Company name for a company-page lookup. |
| `website` | URI | Company website. Strong signal for a company page, and the employer domain for a person search. |
| `country` | string | ISO 3166-1 alpha-2 code or plain English country name, to disambiguate. |

**Two modes:**
- **Validate an existing URL** — supply `url` (profile or company). The tool runs in validation mode and checks the page matches the other signals you pass. Add `first_name`/`last_name` (profile) or `company_name`/`website` (company) to strengthen the match.
- **Search** — omit `url`. For a person, supply `first_name` + `last_name` **plus company context** (`company_name` and/or `website`); company affiliation is what separates people who share a name. On REST, an `email` adds its domain as company context. For a company page, supply `company_name` (+ `website` for precision). The tool returns the best-matching URL.

## Reading the result
Every LinkedIn result-tool call returns this envelope:

```json
{ "message": "...", "status": "SUCCESS" | "ERROR", "status_code": 200, "result": { ... }, "process_time": 9.4 }
```

- `status_code` 200 = done (`result` populated); 202 = still running (`result` null). Error outcomes
  include 400 bad input plus the common auth, credit, lookup and delivery failures in the
  [REST status table](rest-api.md#status-codes).
- The `result` payload carries the canonical LinkedIn `url` plus a `scores` object.
- When the match is uncertain, `result` also includes a `recommendations` array of candidates. Each
  carries `url`, `score`, `title`, `rank`, `desc`, `company_name`, `location`, `profile_name`,
  `position`, `match_score` and `ambiguity_n`. `position` is the LinkedIn headline rendered as the
  job-title label in the console; it can be free text or clipped, and is `null` for company pages.
  `match_score` is the pure candidate match and `score = match_score / ambiguity_n`; an
  `ambiguity_n` above 1 means several candidates were within 10% of the best match. Surface these
  fields for human disambiguation rather than auto-picking.
- `recommendation_status` — how to read that array: `confident` (one clear winner), `ambiguous` (several candidates match comparably well) or `no_match` (nothing credible). **The vocabulary may grow — treat an unknown value as informational, never as an error.** Prefer this over inferring ambiguity from the scores yourself.
- `fallback_used` — `true` means no credible profile was found **at the company you asked about**, and the candidates are same-name profiles found elsewhere. Read it as a **possible job-change signal**, and never write such a candidate back to the record as the person's LinkedIn without a human check.

## Scores & thresholds

For LinkedIn, `accuracy` is continuous (`-1..1`) while `validity` is the discrete integer
`-1`/`0`/`1`. Treat `-1` as missing. Branch on `validity` exactly; apply the tunable bands below to
`accuracy`, `recommendations[].score` or `match_score`:

  - `>= 0.8` → auto-accept the URL.
  - `0.5` ≤ score < `0.8` → route to human review (use `recommendations` to choose).
  - `< 0.5` → reject.

## Recipes

**MCP — search for a person (arguments):**
```json
{ "first_name": "Victor", "last_name": "Goubet",
  "company_name": "Delpha", "website": "https://delpha.io/" }
```

Then call `getLinkedInProfileResult` with the returned `job_id`. Do not re-call it while it is
returning; only re-call if `status_code` is still `202` after it returns, and wait 1–2 seconds first.

**REST — validate an existing company URL (async POST then GET):**
```bash
# POST -> 202 + { job_id, message, status, status_code }
JOB=$(curl -s -X POST https://api.delpha.io/v1/linkedin-company-page \
  -H "Authorization: Bearer $DELPHA_API_KEY" -H "Content-Type: application/json" \
  -H 'User-Agent: my-integration/1.0' \
  -d '{"url":"https://www.linkedin.com/company/delphainc/","company_name":"Delpha","website":"https://delpha.io/"}' \
  | jq -r .job_id)

# GET -> 202 while running, 200 when done
curl -s https://api.delpha.io/v1/linkedin-company-page/$JOB -H "Authorization: Bearer $DELPHA_API_KEY"
```

## Traps to avoid
- **Do not pick a mode by accident.** Passing `url` switches the tool into validation mode; omit it when you want a search. Sending both a `url` and person/company signals validates that URL against those signals — not a fresh search.
- **Do not put `validity` in a decimal review band.** It is `-1`, `0` or `1`; use the continuous
  `accuracy` and recommendation scores for thresholding, then read `recommendations` when they
  disagree or sit in the review band.
- **Do not treat `-1` as a low score.** It means the engine could not compute that dimension; handle it as missing data and avoid rejecting on it.
- **Do not re-call the LinkedIn result tool while it is still returning.** A single call usually
  yields the final result; re-call only if `status_code` is still `202` after it returns, after a
  1–2 second wait. Early re-calls render a duplicate result widget.
- **LinkedIn is the one documented 5xx exception.** This upstream occasionally returns a genuinely transient error, so a single re-submission after a short delay is reasonable here — but it is a **new, separately charged** job, so retry once, never in a loop. Everywhere else treat `500`/`502`/`504` as final ([rest-api.md](rest-api.md)).
- **Do not omit the employer when searching for a person.** `company_name` / `website` disambiguate namesakes; leaving them out is the main cause of a wrong profile. What you must not do is search for a *person* with no name, or a *company page* with no company name.
- **Do not guess an `email` (REST only).** Pass one only if it came from the user, the CRM or a prior verified lookup. An address constructed from `first.last@domain` corrupts the match.
- **Verify the returned profile's company before accepting it.** For a common name a namesake can still rank first even with company context.
