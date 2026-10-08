# API endpoint benchmark results

Verified endpoint snapshot: `2026-07-26`. Manifest SHA-256: `3c4e15a2dd5bed083fe658b681281ec96e5b991c8edfb4507daa5d13a136888b`.

## Summary

| Metric | Result |
|---|---:|
| Providers | 6 |
| Cataloged URL records | 27 |
| Callable endpoint records | 21 |
| Offline fuzz cases | 311 |
| Offline fuzz passed | 311 |
| Offline fuzz failed | 0 |
| Live catalog probes executed | no |
| Billable inference executed | no |

## Recorded API-call speed evidence

These observations are retained because API-call speed is an important routing metric. They are different workloads and are not a direct-provider ranking.

| Observation | Route/model | Samples | Latency | Cost | Comparable provider benchmark? |
|---|---|---:|---:|---:|:---:|
| Bounded live review | openrouter / `nvidia/nemotron-3-super-120b-a12b:free` | 1 | 1,703.0 ms | $0.000000 | no |
| Free-route scout demo | openrouter / `google/gemma-4-26b-a4b-it:free` | 1 | 30,611.0 ms | $0.000000 | no |
| Blinded Empire evaluation mean | codex_plus_empire / `mixed_bounded_tasks` | 5 | 43,029.4 ms | $0.010295 | no |

A publishable provider comparison must use the same synthetic prompt hash, model class, requested output limit, region, streaming mode, warm-up policy, timeout, and measured sample count. Report DNS, connect, TLS, time to first byte, time to first token, output tokens per second, end-to-end latency, p50, p90, p95, median absolute deviation, completion rate, retry rate, rate-limit rate, and cost per successful request.

## Security validation snapshot

| Control | Result |
|---|---:|
| Offline regression tests | 184 / 184 passed |
| Endpoint URL and model-family fuzzing | 311 / 311 passed |
| Security audit checks | 7 / 7 passed |
| Bandit high-severity findings | 0 |
| Bandit medium-severity findings | 0 |
| Bandit reviewed low-severity alerts | 17 |
| Credentials detected | 0 |

The low-severity Bandit alerts were reviewed as subprocess argument-array/path warnings and one naming false positive. 39 detect-secrets entropy alerts were verified as SHA-256 asset digests. Passing results support the documented controls but do not prove that the software has zero vulnerabilities.

## Provider endpoint inventory

| Provider | Role | Method | Class | Callable | Verified |
|---|---|:---:|---|:---:|---:|
| anthropic | `count_tokens` | POST | inference | yes | 2026-07-26 |
| anthropic | `message_batch` | POST | inference | yes | 2026-07-26 |
| anthropic | `messages` | POST | inference | yes | 2026-07-26 |
| anthropic | `models` | GET | catalog | yes | 2026-07-26 |
| deepseek | `anthropic_compatible_base_url` | POST | inference | no | 2026-07-26 |
| deepseek | `base_url` | POST | inference | no | 2026-07-26 |
| deepseek | `beta_base_url` | POST | inference | no | 2026-07-26 |
| deepseek | `chat_completions` | POST | inference | yes | 2026-07-26 |
| deepseek | `models` | GET | catalog | yes | 2026-07-26 |
| google_gemini | `base_url` | POST | inference | no | 2026-07-26 |
| google_gemini | `count_tokens` | POST | inference | yes | 2026-07-26 |
| google_gemini | `generate_content` | POST | inference | yes | 2026-07-26 |
| google_gemini | `interactions` | POST | inference | yes | 2026-07-26 |
| google_gemini | `models` | GET | catalog | yes | 2026-07-26 |
| google_gemini | `stream_generate_content` | POST | inference | yes | 2026-07-26 |
| higgsfield | `base_url` | POST | inference | no | 2026-07-26 |
| higgsfield | `generation` | POST | inference | yes | 2026-07-26 |
| higgsfield | `request_cancel` | POST | job_control | yes | 2026-07-26 |
| higgsfield | `request_status` | GET | job_control | yes | 2026-07-26 |
| openrouter | `chat_completions` | POST | inference | yes | 2026-07-26 |
| openrouter | `models` | GET | catalog | yes | 2026-07-26 |
| xai | `base_url` | POST | inference | no | 2026-07-26 |
| xai | `chat_completions` | POST | inference | yes | 2026-07-26 |
| xai | `language_models` | GET | catalog | yes | 2026-07-26 |
| xai | `model` | GET | catalog | yes | 2026-07-26 |
| xai | `models` | GET | catalog | yes | 2026-07-26 |
| xai | `responses` | POST | inference | yes | 2026-07-26 |

## Interpretation

The offline result validates manifest structure, URL rejection behavior, and direct-provider model-ID boundaries. The recorded route observations above provide latency evidence, but a controlled provider-by-provider inference speed suite has not yet run. Live catalog latency remains opt-in, and billable inference latency requires a separate explicit cost ceiling.

> Point-in-time endpoint and latency evidence; no provider-wide performance guarantee.
