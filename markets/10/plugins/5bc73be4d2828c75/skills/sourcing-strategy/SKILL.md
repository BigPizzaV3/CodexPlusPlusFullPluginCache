---
name: sourcing-strategy
description: "Translate an agreed hiring brief into candidate search hypotheses, search queries, channels, and a measurable sourcing plan."
license: MIT
metadata:
  version: "0.2.4"
---

# Sourcing strategy

## Inputs

Use the job brief, scorecard, target geography and work arrangement, recruiter capacity, approved channels, and any spending limit. Distinguish existing ATS candidates from new external discovery. An unspecified budget does not authorize paid enrichment or searches.

## Procedure

1. Define the capability signals that predict the agreed work outcomes. List equivalent titles, adjacent industries, and transferable experience.
2. Search the existing talent pool first when relevant. Separate a prior applicant's current interest from historic status; do not assume availability.
3. Build a small set of search hypotheses. For each, record role synonyms, capability terms, geography, channel, and expected tradeoff between recall and precision.
4. Draft a broad query and a focused variant using the target channel's supported syntax. Do not invent operators or treat a Boolean query as portable across all services.
5. Review an initial sample against the scorecard, documenting false positives and missed profiles. Adjust one major filter at a time. Do not narrow by protected characteristics or convenient proxies.
6. Plan outreach capacity, deduplication, contact provenance, and stop conditions. Honor opt-outs and existing contact restrictions. Define success as relevant, contactable prospects, not raw profile counts.

## Output

Return search hypotheses, channel-specific query drafts, a sampling checklist, daily capacity, approved spend, deduplication keys, review checkpoints, and assumptions to test. Mark unexecuted queries as plans.

## Example

For a backend reliability role, test “backend engineer,” “platform engineer,” and “site reliability engineer” against incident-analysis evidence. A Boolean-capable channel might start with `(backend OR platform OR SRE) AND (observability OR incident OR reliability)`. Verify the channel supports that syntax and use its dedicated geography filter rather than assuming keyword matches prove location.

## With Vitae

Use `search_ats_candidates` for existing records if it appears in the live connector. External sourcing tools may be unavailable even when a description mentions them. If absent, return the search plan for Vitae's Sourcing surface. Never substitute broad ATS search for an external search and claim new prospects were found. Ask before exceeding an authorized search or enrichment budget.

## Completion and handoff

Hand evidence-backed profiles and provenance to `candidate-screening`, along with duplicate checks and unknowns. Do not scrape restricted sources, invent emails, or send messages as part of planning.
