---
name: measure-usage
description: Prepare and inspect consented Remnant usage statistics when the user enables central measurement or asks to upload, read, withdraw or export their task report. Requires a separately authorized measurement-capable Agent connection. Never infer tokens or causal savings, upload local journals, or change a connection automatically.
---

# Consented task measurements

The public Remnant plugin has seven read-only tools. Installing it does not upload statistics or give this skill measurement tools. Discover actual capabilities first. The optional authenticated Agent connection must expose `get_my_usage_measurements` and `record_task_usage`, with `usage:read` and `usage:write`. If unavailable or the deployment has disabled collection, keep a local record and report that blocker. Do not switch accounts, endpoints, credentials or scopes silently. The host owns OAuth credentials; never ask for tokens in chat.

## Before a task

Respect project privacy, read-only/no-external-write instructions and later opt-outs. Global local-measurement consent, automatic lesson consent and permission to share aggregates are three separate choices. None substitutes for human central-collection consent.

Use a random stable 64-lowercase-hex project pseudonym stored locally, never the project name, path, repository URL or a hash of private text. Use a random stable 32-hex run ID per task, retained on resume. With the same authorized identity, the user reviews the private `/agent/usage?project=<projectKey>` page on their configured Remnant origin. They may enable private collection and independently choose optional aggregate sharing. No agent tool grants this human consent. Consent expires after 90 days; revocation disables its generation and renewal creates a new generation, stopping old queued reports. Never migrate old journals into a new consent.

Call `get_my_usage_measurements` for this pseudonym and check active consent, policy version and generation. An error or denied read is not an empty inventory. Respect capped results and follow explicit pagination for a complete inventory. Capture host-exposed quota snapshots before/after when available, with capture time, reset and window. They describe the shared account; a flat display does not mean zero consumption. Never convert quota to tokens or money. Do not launch additional inference, baselines, paired tasks, purchases or infrastructure to fill statistics. Memory remains optional.

## Complete one ordinary task

Use [the strict tool contract](contract.json). Build only its allowed structured fields, locally; preview audience and measured/missing fields. Do not forward an entire log, ledger, prompt, memory, source file, path, receipt content or provider account ID. Model/parameters/task/rubric/family/difficulty may be null when unavailable; do not invent them. Keep the local ledger's missing-data reasons locally.

Use `schemaVersion=remnant.task-usage/1`, `condition=ordinary`, `pairId=null`, the actual task status and interval, stable IDs and current consent generation. No ordinary usage report proves savings. Record discovery, inspection, requests, retrieval and actual application separately; a read alone is not reuse. Unknown counters, quality and costs stay null; zero requires an observation. Abstention, irrelevant results, errors and stale memories are distinct outcomes.

Exact token fields require provider-reported totals exposed by this host and digests of host-owned response evidence. Label them `provider_reported_by_host`: Remnant cannot independently verify their truth. Cached-input and reasoning-output are subsets, never additional totals. If no provider totals are exposed use `source=unavailable`, all numeric token fields null and `responseDigests=[]`. Do not inspect other tasks or infer from text length. Estimates only if explicitly requested, labeled `estimated_visible`, outside exact totals and economic claims. Included memory-service tokens use separate cost 0 only when inclusion is verified; otherwise unknown costs remain null.

The same inclusion check applies to assistance: `assistanceIncludedInTotal=true` requires separate `assistanceTokens=0`; use false only when the known assistance count is outside the provider total. Unknown inclusion or unmeasured assistance stays null and excludes the pair from a net calculation. Do not add cached, reasoning or already included assistance twice.

Recheck consent immediately before `record_task_usage`. On an ambiguous response retain the identical payload and run ID; do not invent success or create a replacement task. A retry with altered evidence conflicts. Verify the acknowledged hash and read back your own report, using pagination if needed. Distinguish local preparation, successful server acknowledgement and readback. Partial or failed work is reportable as such. Never manufacture successful memory use or lessons for a counter.

## Manage reports

`get_my_usage_measurements` returns only this reporting identity and project. Withdrawal uses `withdraw_task_usage` with the stable run ID and current generation; a correction withdraws the old run and sends a new linked local revision rather than replaying altered evidence. The human page provides complete export, revoke and erase. Revocation excludes retained reports from operator aggregates and stops upload; erasure removes project reports, pairs and deduplication indexes from the active DB. Reports expire after 90 days. Minimal consent/audit metadata expires twelve calendar months after the end of each consent generation (earliest expiration, withdrawal or renewal), in UTC; repeated withdrawal and reads do not extend it. Purge runs on access/startup or explicit maintenance, without a fixed-time scheduler. New candidate backup archives exclude all measurement state; external user exports cannot be recalled. The privacy addendum is still a local draft requiring approval. The operator sees only consenting aggregate populations of at least five reporting identities, not all installations, distinct people or anonymized proofs.

For an explicitly requested comparison only, preregister fixed model/parameters/tasks/rubric/order and amortized preparation costs with `preregister_usage_pair` before either task starts. Never reuse an ordinary task as a retrospective baseline. Quality, separate service costs and assistance gate descriptive differences. Causal quota/token savings and fully net economic savings remain null; host-declared reports are not commercial evidence.

Finish with actual memory use, known counters, missing values and explicit server/consent blockers. Do not claim a skill intercepts every task, that the public plugin exposes private tools, or that an unavailable host meter has been measured.
