# Dedicated public MCP contract

**Endpoint:** `https://signalaf.com/api/plugins/sigrank/mcp`  
**Exact machine-readable source:** `sigrank-app/lib/mcp/plugin/contracts.json`, served by `app/api/plugins/sigrank/mcp/route.ts`, `lib/mcp/plugin/{server,service}.ts`. The older `/api/mcp` remains separate and retains measurement/submission capabilities.

All five tools have `noauth` security schemes. Success and error responses provide `contract_version: "1.0.0"`, `status`, `data`, `provenance`, `warnings` and `error {code,message,retryable}` in `structuredContent`, plus matching text. Tool errors are not empty successful results.

| Tool | Inputs | Structured success data |
|---|---|---|
| `get_leaderboard` | `window` `7d/30d/90d/all` default `30d`; `view` `total/platforms`; `platform`; `cohort=public`; `limit` 1–100 | `entries`, `scope`, `board_url`, `returned_count`, `total_eligible`, `gated`, `next_cursor=null`, `sort_metric=yield`. Each entry has public identity/link, class/rank, pillars, cascade metrics, operating ratio and provenance. |
| `get_operator` | public `codename`, window and optional view/platform | `profile_status` (`measured` or `no_measurement`) and `operator`. Does not infer ownership. |
| `compare_operators` | two public codenames and common scope | `operator_a`, `operator_b`, `comparable`, `reasons`, `scope`, `delta_a_minus_b`. Deltas compare the published board values; a warning marks different snapshot observation dates. |
| `get_field_stats` | window, optional view/platform | `scope`, population and inclusion counts, cohort definition, per-metric distributions, archetype counts, measurement-class counts. Defaults to broader By platform / All; pass `view=total` to align with the claimed Total board. |
| `report_beta_bug` | summary, 1–5 steps, expected/actual, surface, optional version/window/tool/reply email, `consent_confirmed=true` | `reference` beginning `SRB-`, `sent_at`, destination support inbox, redaction flag. No email on missing consent; validation, redaction and rate limit apply. |

`view=total` requires platform `all`. A platform filter selects `view=platforms`. Tool category is `all`; website Operator and + Outliers controls are not tool scopes. Unsupported evidence cohorts return `UNSUPPORTED_SCOPE`. No cursors in V1. Null means unknown, not observed zero. Unclaimed public rows must not automatically be called seeds.

Provenance includes `source_urls`, `retrieved_at`, `observed_at` if known, `dataset_version`, `methodology_version`, `ruleset_version`, `adapter_version`, `taxonomy_version`, `window {label,start,end}`, `platforms`, `models`, `data_origin`, `measurement_class`, `verification_status`, `ranking_eligible`, `coverage`, `reconstruction_method`, and `unknown_fields`. The website board does not publish per-row verification state or evidence class, so this read-only plugin leaves both fields null. Field stats count these rows under `measurement_class_counts.Unknown`.

The four reads set `readOnlyHint=true`, `openWorldHint=true`, `destructiveHint=false`, `idempotentHint=true`. `report_beta_bug` sets `readOnlyHint=false`, `openWorldHint=true`, `destructiveHint=false`, `idempotentHint=false`. Its email side effect requires user approval even though no login is needed.

`total_eligible` counts measured ranked board rows, and operator-row `ranking_eligible=true` means included in that published ranking. It says nothing about the underlying measurement method. The aggregate envelope is not an operator and can carry `ranking_eligible=false`.
