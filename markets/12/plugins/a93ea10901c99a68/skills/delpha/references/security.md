# Security & responsible use

Governs credentials, PII, and safe write-back across every Delpha capability (both the MCP server and the REST API). Read this before wiring Delpha into any automation.

## Table of contents
- Credentials
- Least privilege & tenancy
- PII handling
- Write-back safety (CRM)
- Idempotency & rate
- Error hygiene

## Credentials

Delpha exposes two surfaces with identical semantics. Both accept a **Delpha API key** — a
`dlp_…` secret created at `https://app.delpha.ai` → **Developer → API keys** and sent as
`Authorization: Bearer dlp_…`.

- **MCP server** (`https://mcp.delpha.ai/mcp`): OAuth 2.1 + PKCE **or** an API key header. Prefer
  OAuth in a connector UI — the client runs the flow and you never paste a secret. Use a key where
  the client is header-configurable (Claude Code, Cursor, Windsurf, CI). See [mcp.md](mcp.md).
- **REST API** (`https://api.delpha.io`): an API key. OAuth 2.0 client-credentials against
  `https://secure.delpha.io/oauth2/token` (scope `api/access`) remains available for legacy
  Salesforce-org integrations. See [rest-api.md](rest-api.md).

**Traps to avoid:**
- **Never commit secrets.** Keep keys, client secrets and tokens in a secrets vault (AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager) — never in source, client-side/browser code, or a committed `.env`.
- **Never log tokens.** Strip `Authorization` headers and bearer credentials from request logs, traces, and crash reports.
- **Never put an API key in a browser or mobile app.** A `dlp_` key is a server-side credential and spends your credits. In a user-facing context, proxy the call server-side or use the MCP OAuth flow.
- **Rotate, don't accumulate.** A leaked or expiring key is rotated in place from the console; creating a parallel key instead leaves the old secret authenticating.

## Least privilege & tenancy

Signup at `https://app.delpha.ai` is self-service and provisions a team. Every credential is
validated **server-side, per team** — you only ever see your own team's data.

A key carries three restrictions, all set at creation and editable afterwards: **scopes**
(`dataquality.<usecase>.<single|batch>`), a **TTL**, and a **credit ceiling** per window. They
default differently, and the difference matters: **no scopes = full access**, **no ceiling =
unlimited within the team balance**, but a **TTL always exists** — omitting it means 365 days, not
forever.

**Traps to avoid:**
- **Scope every key you issue.** A key with no scopes can reach every capability; grant only the usecases the integration actually calls, on both `single` and `batch` only where it needs both.
- **Put a credit ceiling on any shared or embedded key.** It bounds the blast radius of a runaway loop or a leak to that key's window instead of the team balance. See [credits-and-limits.md](credits-and-limits.md).
- **Use separate keys per environment and per integration.** Never reuse one key across staging and prod; a leak is then contained and revocable without an outage elsewhere.
- **Rotate on staff departure.** Rotate keys when anyone with access leaves or changes role. Do not paste a key into a team chat.
- **Turn MCP off when you are not using it.** The team-level **MCP access** toggle under
  **Developer → MCP setup** is a clean kill-switch for every MCP client at once.
- **Grant only what's needed on the CRM side too.** Scope each integration's CRM write access (see [Salesforce](salesforce.md)) to the objects and fields it actually updates — never blanket admin.

## PII handling

Validation inputs and outputs **are personal data**: emails, phone numbers, names, and LinkedIn URLs (see [email](email.md), [phone](phone.md), [name](name.md), [LinkedIn](linkedin.md)). Delpha acts as a **processor** under your DPA — you remain the controller.

**Traps to avoid:**
- **Minimize what you send.** Submit only the fields a capability needs to validate; do not forward an entire CRM record "just in case."
- **Do not log PII.** Keep raw inputs/outputs out of application logs, analytics events, and LLM prompt traces. Log job IDs and scores, not the person.
- **Set retention limits.** Don't persist enrichment results longer than your DPA and lawful basis allow; honor data-subject access and deletion requests.
- **Only enrich data you're permitted to.** Don't send records you lack a lawful basis (GDPR) or contractual right to process. Delpha enriches; it does not grant you a basis.

## Write-back safety (CRM)

Validation results feed CRM updates via the [Salesforce](salesforce.md) tools. Automated writes are the highest-risk action in any pipeline.

**Traps to avoid:**
- **A threshold qualifies a value; it never authorises the mutation.** For continuous and
  recommendation scores, a typical policy is: propose at `>= 0.8`, route `0.5` ≤ score < `0.8` to
  human review, reject `< 0.5`. Branch on discrete validity/consistency values exactly. In either
  case get approval before writing, unless a standing, bounded write policy is already agreed.
- **Treat `score == -1` as missing where the schema permits it.** Never let it cross a "low score"
  branch and trigger a downgrade, flag, or deletion.
- **Require human approval for irreversible actions.** Merges, deletes, and mass updates must have a person in the loop — never fully automate them off a single score.
- **Write idempotently.** Key write-back on the source record + capability so a retried job updates rather than duplicates a record or activity.

## Idempotency & rate

Every capability is a `findAndValidateX` / `getXResult` pair. `findAndValidateX` mints a fresh `job_id` with no side effects; `getXResult` is read-only and never charges or mutates. The MCP `getXResult` holds the connection open and polls upstream internally, so a single call usually returns the final result.

**Traps to avoid:**
- **Retry submissions knowingly, not freely.** `findAndValidateX` has no side effects, so a retry cannot corrupt anything — but each accepted submission is a **separately charged** job, so retry an ambiguous network failure, never a response you received. `getXResult` is read-only — also safe — but re-calling it while it is still polling wastes quota and renders a **duplicate result widget**.
- **Re-call only on a lingering 202.** After `getXResult` returns, inspect `status_code`. Re-call only if it is **still** `202`, and wait before doing so. A `200` means done — stop.
- **Don't poll in a tight loop.** Let the single `getXResult` call block; do not fan out concurrent polls for the same `job_id`.

## Error hygiene

Errors are where secrets and PII most often leak — into logs, alerts, and analytics dashboards that have a wider audience than the request itself.

**Traps to avoid:**
- **Never dump tokens in errors.** Redact `Authorization` headers and bearer tokens before an exception is logged or sent to an error tracker (Sentry, Datadog, etc.).
- **Never dump full PII in errors.** Reference the `job_id` and `status_code` from the result envelope (`{ message, status, status_code, result, process_time }`) instead of echoing the email/phone/name that failed.
- **Surface the envelope, not the engine internals.** On `400` show the human `message` and the offending field; on `500`/`502`/`504` log the `job_id` and record the item as unresolved — **do not retry by default** (see [rest-api.md](rest-api.md)) — and do not expose raw upstream stack traces to end users.
