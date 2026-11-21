---
name: information-gain
description: Research and score how much genuinely new, evidence-backed information a page or content plan adds beyond table-stakes competitor coverage. Use RefreshAgent's Spider/JEV evidence collector before the deterministic assess_information_gain operator.
---

# Information Gain

Use this skill when the user asks whether content is differentiated, what a page should add that ranking competitors do not already repeat, how to improve an existing page beyond generic expansion, or when Computed Knowledge SEO reaches the claim-comparison stage.

## Required evidence flow

Do not ask the user to manually gather competitor pages when a target query and current URL are known.

1. Call `collect_information_gain_evidence` with the target query and current URL.
   - RefreshAgent discovers actual ranking competitors with Spider search.
   - It fetches the current page and distinct competitor domains using Spider SmartMode + readability.
   - If a page fetch is weak or fails and a supported Jev provider is configured, RefreshAgent automatically uses a bounded TypeSafe Jev Browser fallback.
   - Jev is retrieval/navigation infrastructure only. Typing is disabled and it does not perform semantic claim extraction or scoring.
2. Read only the returned evidence. Treat pages marked `unavailable`, weak fallback notes, truncation, or unusual JEV statuses as incomplete evidence.
3. Extract atomic factual claims from the current page and each usable competitor page.
4. Assign semantically equivalent claims the same normalized `key`, even when wording differs.
5. Label current/proposed claims as `observed`, `derived`, or `inferred`.
6. Attach each current claim's returned `source_id` plus meaningful source classes such as `current_page`, `gsc`, `ga4`, `noaa`, `first_party_survey`, or another real dataset.
7. Set `cross_dataset_joins` and `historical_observation_count` only from evidence actually used.
8. Call `assess_information_gain`.
9. Explain the component breakdown, separate table-stakes gaps from genuine novelty, and turn the result into concrete research/computation/content tasks.

## What the score is

`assess_information_gain` is a transparent RefreshAgent prioritization heuristic. It is **not** a Google ranking factor and must never be presented as one.

The score rewards evidence-backed novelty such as:

- genuinely new atomic claims;
- deterministic calculations or comparisons;
- joins across independent datasets;
- historical observations and change-over-time evidence;
- first-party or proprietary observations;
- clear provenance and independent source diversity.

It does not reward verbosity, section count, keyword density, or rephrasing the same competitor claims.

## Retrieval policy

Prefer the collector rather than ad-hoc browser research because it preserves provenance and keeps retrieval consistent across ChatGPT, Claude, and Codex.

Spider is the default because it is faster and cheaper for ordinary pages. Jev Browser is a fallback for JS-heavy, awkward, interstitial, or otherwise weak extractions. Do not force JEV on every page.

If `jev_configured=false`, continue with usable Spider evidence and explicitly note where competitor comparison is incomplete. Never pretend the fallback ran.

## Guardrails

Do not manufacture novelty by splitting one idea into many claims. Do not call a competitor gap “information gain” merely because the current page omits it; table-stakes gaps and differentiation are separate concepts.

Do not treat snippets, titles, or headings alone as proof that a competitor makes a substantive claim when page content is available.

If ranking-page evidence cannot be inspected, say the comparison is incomplete. You may still assess first-party/computed-knowledge depth, but do not pretend the novelty comparison is exhaustive.

Prefer conclusions like “add a computed seasonality comparison using your own GSC history” over “add an FAQ section.”
