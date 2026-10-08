# API endpoint comparison and fuzz benchmark plan

Status: planned; no live inference or billable fuzz traffic has been executed.

Purpose: compare common direct API integration practice with Empire's provider-scoped, model-family endpoint manifest; then test every cataloged endpoint safely and publish reproducible tabular results.

## Hardened execution checklist

### Phase 0 — authority, cost, and safety gates

- [x] Freeze this plan before live execution.
- [x] Reconcile every endpoint against current first-party provider documentation and record `verified_at` and documentation URL; API-version/deprecation detail remains an extension field.
- [x] Resolve the apparent xAI conflict: `/models` is the basic catalog and `/language-models` is the richer language-model catalog, so both are retained with distinct roles.
- [x] Classify each operation as catalog/read-only, inference, job control, base URL, or unsupported for live probing.
- [ ] Confirm credentials only by presence and provider scope; never print, export, persist, or include secret values in benchmark data.
- [ ] Obtain an explicit total USD ceiling and per-provider ceiling before any billable request.
- [ ] Require a second explicit confirmation before asynchronous image/video generation; exclude generation from the default speed suite.
- [ ] Use dedicated low-limit test keys and provider-side spending limits where available.
- [ ] Define a conservative global request rate and provider-specific concurrency limits from first-party documentation.
- [x] Preserve OpenRouter as a distinct provider route; never silently substitute it for a selected direct provider.

### Phase 1 — normalized comparison dataset

- [x] Snapshot the release manifest and provider registry with SHA-256 digests.
- [x] Generate one row per provider and endpoint role; model-family/protocol expansion remains pending.
- [x] Compare common-practice routing with Empire family-bound routing using the table schema below.
- [x] Record authentication placement in executable provider adapters without persisting values.
- [ ] Record discovery support, model-ID constraints, modality, streaming, tool support, timeout class, retry class, and fallback semantics.
- [ ] Mark unknown, undocumented, preview, beta, legacy, and deprecated fields explicitly instead of inferring support.
- [ ] Validate that each direct-provider route can select only its own documented model family.
- [ ] Validate that OpenRouter fallback follows `disabled`, `same_model_only`, `same_family_only`, or `any_eligible` exactly.

### Phase 2 — offline manifest and parser fuzzing

- [x] Run deterministic manifest mutation tests without network access; full JSON Schema mutation remains pending.
- [x] Fuzz endpoint URLs for HTTP downgrade, embedded credentials, query/fragment injection, Unicode hostname confusion, localhost/IP literals, path traversal, encoded traversal, control characters, and overlong inputs; DNS-resolution and private-range hostname tests remain pending.
- [x] Fuzz direct-provider model identities for empty, cross-provider, Unicode-confusable, control-character, traversal, and overlong IDs; alias/snapshot expansion remains pending.
- [ ] Fuzz response parsers: missing fields, extra tool/instruction fields, wrong types, duplicate IDs, huge arrays, huge strings, malformed JSON, nested JSON, secret-like output, and non-finite numbers.
- [ ] Fuzz routing policy combinations and prove that invalid priority/fallback combinations fail closed.
- [x] Use a fixed seed and bounded examples; property-based minimization and corpus retention remain pending.
- [x] Require zero crashes and zero accepted unsafe URLs or cross-family model IDs in the current 311-case corpus.

### Phase 3 — safe live endpoint probes

- [ ] Run catalog and metadata endpoints first with one request, concurrency `1`, redirects disabled, TLS verification enabled, and response bodies size-capped.
- [ ] Record DNS, connect, TLS, time-to-first-byte, total latency, HTTP status, rate-limit headers, response size, and served-provider identity where available.
- [ ] Never send repository content in endpoint health probes.
- [ ] Use a fixed synthetic prompt for minimally billable inference only after cost approval.
- [ ] Send warm-up requests separately and exclude them from primary latency statistics.
- [ ] Run at least 10 measured repetitions per eligible text endpoint when budget allows; publish the actual sample count.
- [ ] Randomize provider test order per round to reduce time-of-day bias.
- [ ] Stop immediately on authentication anomalies, redirect attempts, unexpected provider identity, cost-ceiling breach, repeated 429s, or any secret-shaped response.
- [ ] Do not fuzz live authentication, billing, cancellation, or media-generation endpoints with malformed traffic unless the provider explicitly authorizes security testing.

### Phase 4 — speed, reliability, and optimization analysis

- [ ] Report median, p90, p95, minimum, maximum, median absolute deviation, error rate, retry rate, and rate-limit rate; do not rank by a single fastest sample.
- [ ] Separate catalog latency, time-to-first-token, token throughput, and end-to-end latency.
- [ ] Normalize results by prompt hash, requested output tokens, response tokens, region, timestamp, protocol, streaming mode, and model snapshot.
- [ ] Compare cold and warm behavior without combining the distributions.
- [ ] Compute cost per successful request and cost per 1,000 output tokens when provider-reported usage is available.
- [ ] Optimize only within safety constraints: bounded retries with jitter, family-correct routing, connection reuse, streaming, and provider-documented concurrency.
- [ ] Re-run the minimized fuzz corpus after every optimization and require no security or correctness regression.

### Phase 5 — publication gates

- [x] Keep the offline dataset free of request IDs, account IDs, credential values, raw prompts, and provider response text.
- [x] Publish offline measurements as JSON/CSV and a human-readable Markdown table.
- [ ] Include tool version, commit SHA, manifest digest, seed, environment, location, date, sample count, timeout, rate limit, and cost ceiling.
- [x] Label observations as point-in-time results, not permanent provider claims.
- [ ] Separate `passed`, `failed`, `blocked`, `unsupported`, and `not_run`; never convert missing data to zero.
- [ ] Add the benchmark command and acceptance thresholds to CI for offline tests only.
- [x] Keep live tests manual, credential-gated, explicitly acknowledged, and excluded from pull-request CI; billable inference remains additionally cost-gated by the plan.

## Common practice versus Empire family-manifest method

| Dimension | Common API integration practice | Empire endpoint-manifest method | Benchmark assertion |
|---|---|---|---|
| Provider selection | One configured base URL or an OpenAI-compatible URL supplied by the user | Explicit provider ID, allowed host, protocol adapter, and family policy | No request reaches a host outside the selected provider allowlist |
| Model selection | Free-form model string sent to the configured endpoint | Provider-scoped model pattern plus normalized family/version/edition/snapshot | Cross-family and malformed model IDs fail before transport |
| Discovery | Static documentation, manually maintained list, or one provider's model catalog | Per-provider discovery contract with TTL and signed local provenance fields | Fresh discovery updates only that provider's catalog |
| OpenRouter | Often treated as a drop-in global base URL | Separate route with explicit fallback mode and no implicit takeover | Direct-only mode performs zero OpenRouter dispatches |
| Endpoint compatibility | Assumed from an OpenAI-compatible shape | Endpoint role and protocol are declared per provider/model family | Unsupported endpoint/model pairs fail closed |
| Fallback | SDK retry or application-wide alternate provider | `disabled`, `same_model_only`, `same_family_only`, or `any_eligible`, with confirmation policy | Every fallback is policy-valid and attributable |
| Credentials | Environment variable or SDK configuration | Provider-specific environment/keyring lookup; manifest contains no values | Logs and artifacts contain no credential material |
| Freshness | Developer updates configuration manually | On-invocation discovery with TTL, exact-model cache-miss refresh, and receipts | Added/removed models are recorded without cross-provider contamination |
| Observability | Status, latency, and SDK exception | Route, requested/served model, provider, latency, cost basis, and freshness provenance | Every successful live row has sufficient attribution |
| Failure handling | Provider/SDK-specific retry defaults | Classified, bounded, budget-aware failure accounting | No infinite retry, duplicate settlement, or paid fallback without authority |

## Repository benchmark table schema

| Field | Meaning |
|---|---|
| `run_id` | Non-secret unique benchmark run identifier |
| `observed_at` | UTC timestamp |
| `commit_sha` / `manifest_sha256` | Tested source and endpoint snapshot |
| `provider_id` / `route_kind` | Direct provider or OpenRouter route |
| `model_family` / `requested_model` / `served_model` | Family and attributable model identity |
| `endpoint_role` / `protocol` / `api_version` | Catalog, responses, messages, chat, count-tokens, media, or status operation |
| `documentation_url` / `verified_at` | First-party endpoint provenance |
| `test_class` | Offline mutation, catalog probe, inference latency, or authorized live fuzz |
| `seed` / `case_id` | Reproducible fuzz identity |
| `result` | Passed, failed, blocked, unsupported, or not run |
| `status_code` / `error_class` | Redacted outcome classification |
| `dns_ms` / `connect_ms` / `tls_ms` / `ttfb_ms` / `total_ms` | Network timing components where measurable |
| `first_token_ms` / `output_tokens_per_second` | Streaming inference performance |
| `sample_count` / `p50_ms` / `p90_ms` / `p95_ms` / `mad_ms` | Robust aggregate statistics |
| `retry_count` / `rate_limited` | Reliability and throttling evidence |
| `input_tokens` / `output_tokens` / `cost_usd` / `cost_basis` | Normalized usage and cost evidence |
| `cross_family_dispatches` / `unapproved_fallbacks` / `secret_leaks` | Must remain zero |
| `notes` | Redacted limitations or provider-specific behavior |

## Initial acceptance thresholds

| Category | Required threshold |
|---|---:|
| Offline fuzz crashes or hangs | 0 |
| Secret disclosure findings | 0 |
| Cross-family dispatches | 0 |
| Unapproved OpenRouter fallbacks | 0 |
| Redirects followed with authorization | 0 |
| Unsafe/non-public endpoint URLs accepted | 0 |
| Parser acceptance of tool/instruction injection fields | 0 |
| Live success rate | Reported, not silently gated, until a baseline exists |
| Latency optimization | Must improve p50 or p95 without worsening safety gates or error rate |
| Reproducibility | Fixed seed, manifest digest, environment, and sample count present for every published run |

## Planned artifacts

- `readiness/api-endpoint-inventory.json` — normalized verified endpoint snapshot.
- `readiness/api-endpoint-comparison.csv` — common-practice versus Empire comparison data.
- `readiness/api-fuzz-results.json` — machine-readable offline/live case outcomes with no secrets.
- `docs/benchmarks/API_ENDPOINT_BENCHMARK_RESULTS.md` — public benchmark tables and limitations.
- `plugins/empire-llm-codex/scripts/endpoint_benchmark.py` — bounded offline and opt-in live harness.
- `plugins/empire-llm-codex/scripts/test_endpoint_benchmark.py` — deterministic regression suite.
