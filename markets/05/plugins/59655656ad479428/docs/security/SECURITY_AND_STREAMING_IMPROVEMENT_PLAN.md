# Security, API Speed, and Streaming Improvement Plan

Status: submission-ready hardening plan
OpenAI App Store approval: not asserted by this engineering record
Baseline version: 0.1.3

## Current verified baseline

- 187 of 187 offline regression tests pass.
- 311 of 311 endpoint URL and model-family fuzz cases pass.
- Seven of seven security audit checks pass.
- Bandit reports zero high- and zero medium-severity findings; 17 low-severity
  alerts were reviewed.
- Credential scanning reports zero credentials. Thirty-nine entropy alerts were
  verified SHA-256 asset digests.
- Marketplace readiness is 10.0/10 with all 20 gates passing.

These are point-in-time controls, not a guarantee of zero vulnerabilities or
permanent upstream-provider behavior.

## Priority 0 — streaming trust boundary

The paid-response durability and continuation contract is specified in
`docs/handoff/PAID_RESPONSE_RECOVERY_PROPOSAL.md`. Streaming implementations
must satisfy that contract in addition to the controls below.

- Version a `streaming` object for every stream-capable manifest operation.
- Declare the transport (`sse`, `json_stream`, `websocket`, or `poll`) and how
  streaming is activated (request field, query field, or dedicated endpoint).
- Declare start, delta, usage, keepalive, error, and terminal event mappings.
- Normalize provider events to `start`, `content_delta`, `tool_delta`, `usage`,
  `error`, and `done` without discarding the original provider identity.
- Enforce connect, first-event, idle, total, event-size, and stream-size limits.
- Permit retry or provider fallback only before the first user-visible delta.
- After output begins, return an attributable partial terminal result instead of
  mixing output from another request, model, or provider.
- Persist assistant-authored deltas before schema validation so a billable
  partial response survives truncation, parser failure, or process restart.
- Prohibit automatic paid continuation outside a disclosed cumulative cost
  authorization; default to saving the partial result and asking the user.
- Require requested model, served model, provider, request correlation ID,
  usage, settled cost, and terminal state in the final receipt.

## Priority 0 — streaming and parser adversarial tests

- Fuzz malformed SSE fields, data-only events, comments, unknown event types,
  invalid UTF-8, split multibyte characters, partial JSON, and non-JSON data.
- Test missing, duplicated, and contradictory terminal events.
- Test provider errors before the first delta and after partial output.
- Test oversized events, unbounded streams, idle gaps, slowloris delivery,
  connection resets, cancellation races, and truncated tool-call JSON.
- Prove zero post-output fallback, zero duplicate settlement, zero secret-shaped
  log output, and bounded memory growth.
- Retain minimized fixtures and rerun them for every adapter change.

## Priority 1 — comparable API speed benchmark

Run catalog probes before inference. Billable inference requires a documented
total ceiling and per-provider ceiling.

| Metric | Required publication method |
|---|---|
| Catalog latency | 5 warm-up and 20 measured requests per provider |
| Time to first token | 1 warm-up and at least 10 measured streams per model |
| Output throughput | Fixed synthetic prompt and 256-token output target |
| End-to-end latency | p50, p90, p95, minimum, maximum, and MAD |
| Reliability | Completion, retry, rate-limit, truncation, and error rates |
| Cost efficiency | Cost per success and per 1,000 output tokens |

Normalize every row by commit SHA, manifest digest, model snapshot, endpoint
role, region, protocol, streaming mode, prompt hash, output limit, timestamp,
sample count, timeout, and cost ceiling. Randomize provider order per round and
publish cold and warm distributions separately.

## Priority 1 — provider manifest expansion

- Add Kimi/Moonshot and GLM only from current first-party endpoint
  documentation.
- Give each provider an independent host allowlist, credential reference,
  catalog discovery contract, model-family pattern, endpoint-role map, streaming
  adapter, freshness TTL, and fuzz corpus.
- Keep OpenRouter as a separate explicit provider. A direct-only selection must
  generate zero OpenRouter dispatches.
- Fail closed when discovery is stale beyond policy, served identity is
  unproven, or the model/endpoint pair is incompatible.

## Priority 2 — runtime and supply-chain resilience

- Add DNS resolution and private-range revalidation before dispatch.
- Use connection pooling, bounded exponential jitter, per-provider circuit
  breakers, documented rate limits, and cancellation accounting.
- Produce an SBOM and signed release checksums for every release package.
- Run dependency, static-analysis, secret, and unsafe-code scans in CI.
- Record redacted health windows without prompts, responses, credentials,
  request bodies, or complete provider payloads.

## Release acceptance gates

- Zero unsafe endpoints, cross-family dispatches, secret findings, unapproved
  fallbacks, duplicate settlements, or post-output route changes.
- Every declared streaming adapter passes the full deterministic parser corpus.
- Do not publish a reliability claim until at least 30 comparable streams per
  provider achieve the stated threshold.
- Do not publish a speed ranking without p50/p95, throughput, completion rate,
  workload identity, model identity, region, cost, and sample provenance.
- Rerun the focused offline suite, 311-case fuzz suite, security checks, and readiness
  scorer after every implementation slice.
