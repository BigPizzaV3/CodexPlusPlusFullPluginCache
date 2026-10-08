# Changelog

## 1.7.2 — submission remediation candidate

- Removes external web-provider dispatch, remote browser actions, document
  uploads, provider credential setup, and provider endpoint guides from the web
  skill after the portal reported access-control circumvention and security risk.
- Retains native public-source research and explicit stopping at access controls.
- Rejects legacy provider commands before any credential or network access.
- Adds release guards against restoring a web-provider adapter to the ZIP.
- This is a replacement candidate for rescanning, not an approval or publication.


All notable changes to Empire LLM for Codex are documented here.

## 1.7.1 — Adversarial hardening (submission candidate)

This candidate is locally packaged for validation, not published or newly
approved. Release-specific external gates are tracked in
`docs/handoff/RELEASE_1_7_1.md`.

- Scan the exact HTML upload bytes before Firecrawl dispatch, including decoded
  entities and split text. PDF, Office, RTF and opaque uploads now fail closed
  until converted locally to inspectable UTF-8 HTML.
- Validate output destinations and browser action arguments before paid web
  work. Deliver files atomically, refuse unintended overwrites, and retain
  captured bytes when delivery fails.
- Persist Review and Handoff responses before fallible provider-reference or
  health bookkeeping; preserve recoverability during reconciliation failures.
- Share collision-rejecting exact model-ID joins, preserve free-route suffixes
  and case, and require explicit provider input/output capability evidence.
- Score cost only from measured USD/task, retaining missing values and metric
  provenance rather than substituting token prices.
- Advance normalized catalog schema to 1.9.0 to invalidate older assumptions.
- Reject named pipes without blocking recovery reads, repair hashing or event
  append; enforce the content byte ceiling throughout streamed recovery reads.
- Remove invalid optional benchmark skill icon overrides; shared chart/model
  artwork remains in its canonical packaged location. Keep the three supported
  manifest starter prompts.
- Test review, response recovery, handoff preview and benchmark rank/render
  against the extracted production ZIP with isolated synthetic fixture state.
- Make CI request a nonzero exit when the readiness gate fails.
- Explain missing Free-tier route identity evidence; preserve unverified
  research charts without inventing OpenRouter matches or changing subscriptions.
- Verify 305 regression tests and all eleven original adversarial probes. See
  `docs/handoff/ADVERSARIAL_HARDENING_2026-09-04.md` for the completed checklist,
  acceptance criteria, scores, and remaining live-validation limits.

## 1.7.0 — Live benchmark visualization

- Added `$empire-benchmarks`, a read-only skill for current Artificial Analysis
  model evidence, named scoring profiles, explicit weight overrides, modality
  requirements, and route-qualified OpenRouter views.
- Migrated Artificial Analysis access to the current paginated
  `/api/v2/language/models` and `/api/v2/language/models/free` endpoints with
  bounded page retrieval, tier and index-version validation, a narrow automatic
  free-tier fallback, and redacted rate-limit receipts.
- Replaced permissive benchmark-to-provider matching with exact
  `openrouter_api_id` identity joins; ambiguous or fuzzy names remain ineligible
  for dispatch.
- Added a self-contained vertical chart fragment with local model chips,
  adjustable weights, responsive and reduced-motion behavior, and a Markdown
  fallback for Codex surfaces without interactive visualization rendering.
- Kept browser-side credentials and network access out of the chart. The
  visualization can ask Codex a follow-up question but cannot invoke a model,
  reserve budget, or authorize a later review.
- Added deterministic benchmark fixtures and focused tests for pagination,
  credential redaction, exact joins, fuzzy-match rejection, modality failures,
  weight normalization, and sandboxed rendering.
- Added a human-review update article with practical benchmark, modality, value,
  and accessible-fallback prompt examples.

## 1.6.0 — Governed web escalation

- Added `$empire-web-escalation`, keeping the Codex native browser first and
  using Firecrawl as the credit-aware recovery layer.
- Cataloged the current Firecrawl v2 free-plan API-key surface and excluded the
  Enterprise-only threat-protection policy endpoint from the adapter.
- Added Bright Data Unlocker and managed Browser API as explicitly approved paid
  last resorts for public, authorized targets.
- Added hidden native-keyring setup, redacted diagnostics, public-target checks,
  secret-bearing payload rejection, bounded uploads/responses, redirect refusal,
  and no silent POST retries.
- Added a complete 62-identity local model-icon manifest covering all 425
  entries in the 2026-09-03 OpenRouter catalog snapshot, with compact response
  assets, cached lookup, and a safe future-model fallback.
- Made the plugin `assets/llm-icons/` directory the single physical icon source
  so GitHub marketplace and release installs remain self-contained; the root
  `llm-icons/` path is a convenience symlink rather than a duplicate copy.
- Preserved the Python skills-only architecture: no MCP server, no repository
  access for web providers, and no external mutation or decision authority.

## 1.5.1 — Deterministic skill-scan hardening

- Replaced the scanner-facing 213 KB Review monolith with a stable sub-1 KB
  compatibility entry point and moved the unchanged implementation to the
  plugin-level runtime. This preserves every Review command while keeping
  future routing and recovery growth outside the per-skill scanner surface.
- Split durable response recovery and secret policy out of the oversized Review
  router module while preserving its public behavior and fault-injection tests.
- Promoted budget, context-policy, recovery, secret-policy, and Windows
  credential helpers to the shared plugin runtime used by Review, Handoff, and
  Media instead of redundantly exposing them in one skill's scan surface.
- Kept the required 256 px Review icon inside the skill while retaining the
  complete model-icon catalog once at plugin level.
- Added fail-closed release validation for every catalog asset hash, every
  compact 14 px RGBA footnote icon, all aliases, and the core collaborator
  model-family icons so future scan optimizations cannot silently remove UI.
- Added deterministic release guards for per-file size, total Review scan size,
  file count, shared-runtime placement, and forbidden generated/private paths.
- Shortened the stable directory subtitle to `Route reviews and handoffs`.

## 0.1.5 — Context-safe routing and recovery hardening

- Replaced the binary credential check with explicit `present`, `missing`, and `inaccessible` states so sandbox-denied Keychain access is never reported as credential loss.
- Added post-save keyring readback; setup reports `configured` only after verification and otherwise returns a safe `configured_unverified` state.
- Updated review, handoff, media, and direct-provider paths to request a narrowly authorized keyring retry instead of repeatedly prompting for an API key.
- Hardened Windows Credential Manager lookup so access errors remain distinguishable from a genuinely absent item.
- Added regression coverage for macOS sandbox denial, verified absence, redacted doctor output, and unverified post-save behavior.
- Added a shared, side-effect-free context policy with confidence-aware usage
  measurements, threshold projections, capped reserves, and micro, compact,
  standard, and artifact response-class recommendations.
- Added measurement-only `context_preflight` receipts to Review and Handoff.
  Unknown usage fails into conservative recommendations, caller-reported usage
  requires both limit and used tokens, and no response-class recommendation
  changes provider dispatch in this release slice.

## 0.1.4 — App Store scan remediation

- Removed an obsolete cron/LaunchAgent persistence installer and destructive legacy self-installer from the public plugin tree.
- Removed `interface.screenshots` from the skills-only manifest, matching the OpenAI submission contract.
- Added deterministic release guards that reject persistence installers and skills-only screenshot metadata.
- Reduced the scan surface by excluding unreferenced screenshot files from the public ZIP while preserving the tested seven-skill runtime.

## 0.1.3 — Paid response no-loss hardening

- Persist assistant-authored provider output to an owner-only, hashed Markdown recovery artifact before billing settlement or schema validation.
- Classify token-limited output as `partial_recoverable`, readable schema failures as `completed_degraded`, sensitive output as `blocked_sensitive`, and paid empty output as `failed_empty` with compensation pending.
- Attach recovery paths and bounded 12,000-character chunk plans to model synthesis records so Codex can review large responses without injecting them into one context window.
- Recover truncated handoff `artifact.content` prefixes and preserve oversized handoffs instead of discarding already-billed output.
- Prohibit automatic paid retries and continuations; partial results must be synthesized first, then any missing-work continuation requires separate authorization.

## 0.1.2 — Security hardening candidate

- Refused provider redirects and non-public HTTPS targets to prevent authorization-header leakage and server-side request forgery.
- Added secret and size validation for outbound tasks, media prompts, and inbound partner responses.
- Projected untrusted model responses onto a bounded allowlist, dropping tool-call and instruction fields.
- Replaced predictable private-state temporary files with owner-only atomic writes.
- Added a deterministic source and release-archive security audit with hostile regression fixtures.
- Mapped documented controls to OpenAI submission checks, OWASP Top 10 for LLM Applications 2025, and NIST SP 800-218 SSDF without claiming certification.
- Added a current, first-party-documented comparison of 27 provider endpoint records across six providers.
- Added a 311-case offline endpoint/model-ID fuzz benchmark that exercises the production transport validator.
- Hardened URL handling against Unicode hostname confusion, encoded traversal, control characters, and oversized endpoints.
- Expanded the deterministic offline release loop to 183 tests across eight suites.

## 0.1.1 — Hardened release candidate

- Reconciled and contract-tested the exact seven-skill public inventory.
- Added durable dispatched and pending-reconciliation budget states, conservative expiry, idempotent settlement, and late cost adjustments.
- Added privacy-preserving process-crash and ambiguous-outcome evidence across 98 router tests.
- Added explicit budget reconciliation commands for uncertain provider billing outcomes.
- Hardened image and video routing to exclude pinned OpenAI models inside Empire and use installed plugin-root paths.
- Bounded asynchronous video polling to resumable 45-second waits, capped at 60 seconds per call.
- Added a blinded comparative-utility harness and frozen evaluation thresholds without claiming an unexecuted live result.
- Enforced truthful readiness scoring: no failed mandatory gate can report 10.0.
- Expanded the deterministic offline release loop to 160 tests.

## 0.1.0 — Private beta

- Added bounded OpenRouter and direct-provider review routing.
- Added optional Artificial Analysis benchmark enrichment.
- Added native macOS, Windows, and Linux credential storage.
- Added project budget reservation and settlement controls.
- Added quarantined checklist and single-file handoffs.
- Added model badges, normalized Markdown tables, and Codex-native contribution footers.
- Added evidence-backed Codex Plugins Directory readiness scoring.
- Validated 65 focused offline tests and controlled live routing evidence.
