---
name: static-winner-analysis
description: Analyze an ad account's static-ad performance through the platform's marketing API under a strict read-only contract, to select fresh winning static concepts for iteration. Use when retrieving insights, ads, creatives, and previews to rank winners, deduplicating localized executions into unique concepts, maintaining an unused-winner ledger, or verifying a winner's creative before it becomes a generation reference — without creating, editing, publishing, pausing, budgeting, or otherwise mutating anything in the account.
---

# Static Winner Analysis — read-only

Retrieve what is working, prove it, and hand the pipeline a deduplicated,
evidence-backed winner list. This skill holds the permission boundary and the
credential rules for every ad-account read the statics pipeline performs.

## The permission contract

- The account, its identifier, and the API access token are **inputs supplied
  in the active conversation or session** — never stored in a skill, config,
  manifest, or artifact.
- Once supplied, read-only retrieval for winner analysis is
  **standing-authorized**: run the GET requests the analysis needs without
  re-asking per query. If the session holds no usable credentials, ask once;
  a platform connector or signed-in browser is the fallback, not the norm.
- **Read-only means read-only.** Retrieve account metadata, campaigns, ad
  sets, ads, creatives and previews, insights, actions, spend, and conversion
  fields. Never call anything that creates, updates, publishes, pauses,
  resumes, deletes, duplicates, uploads, or adjusts any object, budget,
  audience, billing, or delivery state. A write requires a separate explicit
  user request and its own confirmation — never inferred from a
  creative-production request.
- State the read-only boundary in the run's manifest so the contract is
  visible in the record.

## Credential hygiene

- Never write the token into a file, URL, log, filename, summary, command
  echo, or recorded artifact of any kind. Pass it at runtime only, and redact
  it from anything persisted.
- Treat a token found in client-side or public configuration (for example a
  browser-exposed environment variable) as compromised: flag it and advise
  rotation.
- Retain no login state, cookies, or session material after the run.

## Retrieve and rank

1. Query insights for the requested lookback window, restricted to static
   image ads — media type is part of the query, not a post-filter hope.
2. Parse results from the actual action/conversion fields; do not trust a
   pre-aggregated column whose definition you have not checked.
3. Rank on meaningful conversion volume **and** cost efficiency together.
   Exclude under-delivered ads; never promote an ad because one conversion
   produced a flattering cost figure.
4. Open each shortlisted ad's creative preview and visually confirm it
   corresponds to its performance row before treating it as a winner.

## Deduplicate into concepts

Cluster by underlying creative concept before filling any slot: language,
translated copy, localized names, and target market are execution attributes.
One concept, one slot — the strongest execution becomes the visual reference;
the other executions are cross-market validation, not additional winners.

## The unused-winner ledger

Maintain a dated ledger of ranked winners not yet iterated: concept, best
execution, evidence, and why it was passed over. It feeds the next cycle's
repeat-versus-explore decision, per the workspace evidence conventions
(`juicylucy` skill, `evidence.json` § retention).

## Record the evidence

Per selected winner: account (by name, not token), reporting window, ad
name/ID, results, spend, cost per result, return metrics when available,
preview confirmation, concept-cluster name, deduplicated siblings, and the
reference image path or capture. This record is what makes "we iterated a
winner" auditable later.

## One winner, five variations

A confirmed winner seeds a review cycle, not a clone: five materially
distinct variations — different composition, setting, typography, or copy
angle around the same hypothesis — so the next report can say *why* it won,
not merely that it did. The mutation modes and master QA live in
`static-ad-production`.

## Guardrails

- Product truth outranks performance: a winning claim the brand's
  `product-truth.md` does not support is a rejected claim, however well it
  converted. Resolve the brand skill before turning any winner into copy.
- Never expose account data beyond what the run needs, and never paste raw
  API responses containing identifiers into shipped artifacts.
- A stale local asset is not a winner; when live access exists, the live
  numbers decide.
