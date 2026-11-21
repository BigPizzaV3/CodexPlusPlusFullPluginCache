# Website — find, validate & enrich

## Table of contents
- When to use
- Tools
- Inputs & modes
- Reading the result
- Scores & thresholds
- Recipes
- Traps to avoid

## When to use
Use this capability to verify a company's web presence: confirm a URL is live and canonical, or discover the most likely website from other entity signals. Typical jobs: cleaning a CRM `Website` field, deriving a domain before running [email](email.md) validation, or cross-checking a company against its [LinkedIn](linkedin.md) and [legal ID](legal-id.md).

Submit the job, then fetch the result. Typical latency is ~10 seconds, so a single `getWebsiteResult` call usually returns the final payload.

## Tools
- `findAndValidateWebsite` — submits a job and returns a `job_id`. It does not mutate your data,
  but every accepted production submission is a separate charged job.
- `getWebsiteResult` — read-only; takes the `job_id` and returns the result envelope. Never charges or mutates.

## Inputs & modes
All fields are optional, but you must supply enough to identify one entity. Two modes are selected by what you pass:

| Field | Type | Notes |
|-------|------|-------|
| `website` | URL | The URL to validate. Setting it runs **validation mode**. |
| `name` | string | Entity name to search for. Combine with `country`. |
| `country` | string | Disambiguates same-named entities (e.g. `France`). |
| `email` | email | **REST only.** Its domain is a strong website signal; the MCP schema is closed and rejects it. |
| `linkedin` | URL | Company LinkedIn URL; strong signal. |

**Validation mode** — supply `website`. The tool checks reachability, resolves redirects, and matches the resolved site against any other signals you pass.

**Search mode** — omit `website` and supply entity signals: `name` + `country`, OR `linkedin` (OR `email`, on REST). Pass several together to improve accuracy and consistency.

Tip: in validation mode, still pass `name`/`country`/`linkedin` (and `email` on REST) when you have them — they feed the `accuracy` and `consistency` scores and tell you whether the live site actually belongs to your entity.

## Reading the result
`getWebsiteResult` returns the standard envelope:

```json
{ "message": "...", "status": "SUCCESS", "status_code": 200, "result": { ... }, "process_time": 9.7 }
```

- `status_code` 200 = done (`result` populated); 202 = still running (`result` null). Error outcomes
  include 400 bad input plus the common auth, credit, lookup and delivery failures in the
  [REST status table](rest-api.md#status-codes).
- Do not re-call while it is returning. Re-call only if `status_code` is still 202 after the call returns, and wait 1–2 seconds first. Early re-calls render a duplicate result widget.

The `result` payload contains:
- `normalized_value` — the canonical URL, post-redirect and normalized. Write this back, not the raw input.
- `label` — short verdict string (e.g. `OK`).
- `scores` — `validity`, `completeness`, `accuracy`, `consistency` (see below).
- `recommendations` — array of alternative URLs, each ranked by confidence. In search mode the top entry is usually `normalized_value`; consult the rest when the lead score is borderline.

## Scores & thresholds

`accuracy` is continuous (`-1..1`), `completeness` is continuous (`0..1`), `validity` is discrete
(`-1`/`0`/`1`) and `consistency` is discrete (`0`/`1`). Treat `-1` as missing where allowed.

- `validity` — the URL is well-formed and reachable.
- `completeness` — how fully the site was resolved/normalized.
- `accuracy` — the site matches the entity signals you supplied.
- `consistency` — agreement across signals (name, country, email domain, linkedin).

Suggested decision thresholds for continuous `accuracy`, `completeness` and recommendation scores
(tunable): `>= 0.8` auto-accept; `0.5` ≤ score < `0.8` route to human review; `< 0.5` reject.
`validity == 0` means invalid and `consistency == 0` means the supplied signals disagree; do not
put either integer into a decimal review band. When `accuracy == -1`, you passed too few signals to
judge ownership — add `name`/`country` or `linkedin` and re-run before trusting `normalized_value`.

## Recipes

Search mode via MCP — find the website from a name and country:

```json
{ "name": "Delpha", "country": "France" }
```

Then call `getWebsiteResult` with the returned `job_id`.

Validation mode via REST — confirm a known URL and cross-check the domain:

```bash
# 1) submit
JOB=$(curl -s -X POST https://api.delpha.io/v1/website \
  -H "Authorization: Bearer $DELPHA_API_KEY" -H "Content-Type: application/json" \
  -H 'User-Agent: my-integration/1.0' \
  -d '{"website":"https://delpha.io/","email":"victor.goubet@delpha.io"}' \
  | jq -r .job_id)

# 2) poll: 202 while running, 200 when done
curl -s https://api.delpha.io/v1/website/$JOB \
  -H "Authorization: Bearer $DELPHA_API_KEY"
```

The MCP and REST surfaces share identical semantics; only auth and transport differ.

## Traps to avoid
- **Do not write the raw input URL back to your record.** Persist `normalized_value` instead — it is post-redirect and canonical, so it dedupes and resolves cleanly.
- **Do not treat a `-1` score as a failing site.** It means the engine lacked inputs to compute that dimension; supply more signals and re-run rather than rejecting.
- **Do not validate a URL in isolation when you can prove ownership.** A reachable site with too
  few entity signals can yield `accuracy == -1` or `consistency == 0` — you confirmed it exists,
  not that it is the right company.
- **Do not poll `getWebsiteResult` in a tight loop.** It internally polls upstream for ~25s; re-call only if it returns `status_code` 202, after a 1–2s wait.
- **Do not assume the first recommendation is correct on a borderline lead.** When the top score sits in the review band (`0.5` ≤ score < `0.8`), inspect lower-ranked `recommendations` and route to human review.
- **Do not pass conflicting signals expecting silent resolution.** A mismatched `email` domain and
  `linkedin` can produce `consistency == 0`; that disagreement is the answer, not a decimal score.
