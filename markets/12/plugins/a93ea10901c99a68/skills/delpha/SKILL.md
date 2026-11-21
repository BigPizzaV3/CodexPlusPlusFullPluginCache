---
name: delpha
description: >-
  Use when validating, cleaning, deduplicating or enriching contact and company
  data with Delpha — email, phone, name, website, LinkedIn, company legal ID
  (SIRET, SIREN, ABN, CIK), ultimate parent — or wiring its MCP server or REST
  API into an agent.
---

# Delpha

Delpha finds, validates and enriches the people and companies in your data. This skill routes a
request to the right tool and keeps you from misusing the asynchronous API.

## Rules

1. Pick the tool from the routing table below and **read its reference before writing code**.
2. Submit with `findAndValidate*`, read with the matching `get*Result` — **call the result tool
   once**; it polls for you.
3. Read the score's declared type. In the common shape, `accuracy` is continuous (`-1..1`),
   `completeness` is continuous (`0..1`), `validity` is discrete (`-1`/`0`/`1`) and `consistency`
   is discrete (`0`/`1`). Treat `-1` as missing where allowed; use decimal bands only for
   continuous or recommendation scores.
4. Never write a value back to a CRM below your confidence threshold, and never auto-merge or delete
   records without human approval.
5. Never hardcode a credential. See [references/security.md](references/security.md).

## Surfaces

Two surfaces, same engines, same payloads:

- **MCP server** — `https://mcp.delpha.ai/mcp`. Prefer this from an agent. Auth is OAuth 2.1 + PKCE
  (the client discovers everything) **or** an `Authorization: Bearer dlp_…` Delpha API key. The team
  must have MCP enabled in the console. See [references/mcp.md](references/mcp.md).
- **REST API** — `https://api.delpha.io`. Prefer this from code and pipelines. Auth is
  `Authorization: Bearer dlp_…`. See [references/rest-api.md](references/rest-api.md).

Get a key at `https://app.delpha.ai` → **Developer → API keys**. Signup is self-service and a new
team starts with free credits.

## Tool routing

| The request is about… | Use | Reference |
|---|---|---|
| An email — deliverable? personal or professional? find it from a name | `findAndValidateEmail` → `getEmailResult` | [email.md](references/email.md) |
| A phone number — valid? E.164? line type, carrier (does **not** search) | `validateAndNormalizePhone` → `getPhoneResult` | [phone.md](references/phone.md) |
| A person's name — normalize spelling/casing (does **not** search) | `validateAndNormalizeName` → `getNameResult` | [name.md](references/name.md) |
| A LinkedIn profile — validate a URL, or search | `findAndValidateLinkedInProfile` → `getLinkedInProfileResult` | [linkedin.md](references/linkedin.md) |
| A LinkedIn company page — validate a URL, or search | `findAndValidateLinkedInCompanyPage` → `getLinkedInCompanyPageResult` | [linkedin.md](references/linkedin.md) |
| A company website — validate, resolve redirects, or search | `findAndValidateWebsite` → `getWebsiteResult` | [website.md](references/website.md) |
| A company legal ID (SIRET/SIREN/ABN/CIK/…) + firmographics | `findAndValidateLegalID` → `getLegalIDResult` | [legal-id.md](references/legal-id.md) |
| Who owns a company — parent, holding, ownership chain | `findAndValidateUltimateParent` → `getUltimateParentResult` | [ultimate-parent.md](references/ultimate-parent.md) |
| Hundreds or millions of rows | the REST batch API + webhooks | [rest-api.md](references/rest-api.md) |
| What a call costs, and what happens at zero | credits, `402`, per-key ceilings | [credits-and-limits.md](references/credits-and-limits.md) |
| Reading from / writing back to Salesforce | the Delpha Salesforce MCP + the loop below | [salesforce.md](references/salesforce.md) |

A request that spans several fields — "clean up this account" — is several independent jobs: submit
them all, then read them all.

Production MCP serves the split LinkedIn pairs above and hides the deprecated generic
`findAndValidateLinkedin` / `getLinkedinResult` pair. Generic REST routes remain for compatibility.

## The find → get pattern

1. `findAndValidate*(...)` submits a job and returns a `job_id`. It mutates nothing of yours, so a
   retry is safe — but it is **not billing-idempotent**: each accepted submission is a new,
   separately charged job. Retry an ambiguous transport failure knowingly; never retry a response
   you received.
2. `get*Result(job_id)` returns the outcome. The server **polls the upstream job internally** and
   holds the call open, so a single call usually returns the final result.

**Do not loop on `get*Result`.** Re-call only if `status_code` is **still `202`** after it returns,
and wait first.

## Reading the result

```json
{ "message": "…", "status": "SUCCESS", "status_code": 200, "result": { }, "process_time": 4.7 }
```

`status_code`: `200` done · `202` still running · `400` bad input · `401` missing Authorization
header · `402` out of credits or key ceiling spent · `403` rejected credential or scope · `404`
job not found · `409` expired reservation · `422` unprocessable input · `500`/`502`/`504` server
or engine failure. Only transport failures are retryable by default — see
[references/rest-api.md](references/rest-api.md).

The common `result.scores` model has continuous `accuracy` (`-1..1`) and `completeness` (`0..1`),
discrete `validity` (`-1`, `0`, `1`) and discrete `consistency` (`0`, `1`). Treat `-1` as missing
where allowed. Suggested policy for a continuous or recommendation score, tuned per use case:
**`≥ 0.8` auto-accept · `0.5` ≤ score < `0.8` human review · `< 0.5` reject**. For discrete
fields, branch on the exact value instead of applying a decimal band.

## Writing back to a CRM

Read → validate → **show the proposed changes as a table and get approval** → write, only above your
threshold and never a value scored `-1`. Full recipe, including the Salesforce tool pairing, in
[references/salesforce.md](references/salesforce.md).

## Critical rules

- **`validateAndNormalizeName` and `validateAndNormalizePhone` do not search.** Each checks and normalizes a value you already have. To *find* a
  person use email recommendation mode or LinkedIn search mode.
- **Legal ID lookups need a registry.** Pass `legal_id_type` *or* `address.country`, or the job
  returns `400`.
- **Email recommendation mode is all-or-nothing.** `first_name` + `last_name` + `website` together,
  or `400`.
- **Ultimate parent needs both `company_name` and `website`,** and is the most expensive operation.
  Prices differ per operation and are live configuration: read them from
  `GET https://api.delpha.io/v1/pricing` (no credentials) or the console, and never hardcode one.
- **`-1` is not zero where a score field permits it.** Never write it back and never read it as a
  rejection.
- **Treat every input and output as personal data.** Don't log emails, phones or names; respect
  retention and DPA terms.

## Key documentation

- [Delpha API & MCP overview](https://help.delpha.io/delpha-api-and-mcp/delpha-api-and-mcp)
- [Delpha MCP server](https://help.delpha.io/delpha-api-and-mcp/mcp)
- [Delpha Help Center](https://help.delpha.io) · [app.delpha.ai](https://app.delpha.ai)
