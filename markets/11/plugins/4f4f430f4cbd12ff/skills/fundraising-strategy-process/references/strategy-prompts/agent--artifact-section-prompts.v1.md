Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Artifact section-helper prompts

Status: Chapter 3 **Find useful peers** is the only active implementation.
It uses the adapted P6 discovery → result → candidate set → owner decision
lifecycle. Chapter 5 and the remaining helpers stay prompt-library entries.
These helpers are optional improvements on an existing V4 strategy artifact.
They are not Fast Intake prerequisites and are not Consultant View.

This file was recreated on 2026-08-20 because it was absent from
`feat/strategy-v3-greenfield`. Chapter 3 and Chapter 5 prompts are the
owner-supplied section-helper language. Chapters 1, 2, 4, and 6 use the
same execution contract and the named actions; they are **defined, not
active**. Do not substitute `agent/strategy-framework/*.v1.md` or
Chapter Guidance consultant modules at runtime.

No helper is an active UI action until its authority and acceptance paths
are real. See `../v3_build/V4_SECTION_HELPER_AUTHORITY.md`.

## Execution contract

- Opening or refreshing an artifact makes zero model calls.
- A helper runs only after an explicit user action.
- One action authorizes one bounded task, not a document-wide analysis.
- Keep the existing strategy visible and editable whenever its document
  authority permits.
- Do not create an advisor turn, consultant review, maturity state, or
  Consultant View session.
- Return candidates, supporting notes, or an exact proposed replacement
  outside the document.
- Do not modify the document until the owner accepts a bounded change.
- Only the selected chapter may change. Unaffected chapters must remain
  byte-for-byte unchanged.
- Proposed document prose must be direct organizational language and
  immediately copy-ready.
- Reasoning, alternatives, confidence, gaps, and strengthening suggestions
  stay outside the document.
- Preserve durable accepted peers, owner decisions, and evidence even if
  the latest generated prose omitted them.
- Missing context narrows the output; it does not produce a refusal or
  research plan.
- Never invent financial metrics, amounts, dates, outcomes, peers,
  funders, relationships, eligibility, access, open programs, deadlines,
  or source support.
- Provider errors or stale revisions must leave the existing artifact
  intact.
- Preserve the current approved Terra/Luna policy. Do not add or change a
  model.
- The first request may call the provider once. Same-key replay after
  response loss must make zero additional provider calls.
- Conflicting key reuse must fail safely.
- A stale document revision or context binding must return a refresh-safe
  conflict before application.
- Provider failure before persistence writes no helper result and no
  document revision.
- Never automatically retry a provider generation.

## Registry

| Chapter | Action                         | Helper id                    | UI        |
| ------- | ------------------------------ | ---------------------------- | --------- |
| 1       | Clarify the ask                | `clarify_the_ask`            | inactive  |
| 2       | Sharpen the organization frame | `sharpen_organization_frame` | inactive  |
| 3       | Find useful peers              | `find_useful_peers`          | active P6 |
| 4       | Strengthen the evidence base   | `strengthen_evidence_base`   | inactive  |
| 5       | Build a simple case            | `build_a_simple_case`        | blocked   |
| 6       | Refresh the funder map         | `refresh_the_funder_map`     | inactive  |

Chapter 3 is active through the existing P6 job plane. `blocked` on Chapter 5
means Case Design remains deferred. `inactive` means the prompt is defined
only; do not expose an action. A generic `artifact_section_helper_results`
plane is not authorized.

## Chapter 1 — Clarify the ask

User-facing action: **Clarify the ask**

### Prompt: clarify_the_ask

```text
Based on the organization's goal and available evidence, write a clear fundraising ask that can organize this strategy. State what the organization is trying to fund and what the strategy must accomplish. Use direct organizational voice so the result can be pasted into Chapter 1 without rewriting. Do not invent an amount, deadline, outcome, funder interest, or organizational commitment. Keep alternatives, confidence, and strengthening suggestions outside the proposed document text.
```

## Chapter 2 — Sharpen the organization frame

User-facing action: **Sharpen the organization frame**

### Prompt: sharpen_organization_frame

```text
Based on what we know about this organization, write a fundraising-relevant organization frame: role, operating model, geography, constituency, and the distinction that should lead the case. Use direct organizational voice so the result can be pasted into Chapter 2 without rewriting. Do not invent financial metrics, outcomes, relationships, or commitments. Keep alternative frames and unsupported interpretations outside the proposed document text.
```

## Chapter 3 — Find useful peers

User-facing action: **Find useful peers**

### Prompt: find_useful_peers

```text
Based on what we know about this organization, its fundraising objective, operating model, geography, and available evidence, identify a small set of useful peer organizations. Include direct operating-model peers, adjacent role peers, and contextual references. For each, explain the specific comparison role and its limits. Do not invent financial metrics, relationships, funders, eligibility, or access. Clearly label unsupported candidates as provisional suggestions. If durable owner-accepted peers already exist, preserve and prioritize them.
```

Return five to eight cards when evidence supports that many. Each card needs:

- organization name and resolved identity when available;
- comparison role;
- why it is relevant;
- what it may benchmark;
- what it must not be used to infer;
- evidence locator and currentness when available;
- confidence;
- durable or provisional status; and
- `Keep`, `Reference only`, and `Remove` actions.

Required behavior:

1. Load durable accepted peers before generation.
2. Preserve and prioritize those peers in the result.
3. Clearly distinguish durable peers from provisional suggestions.
4. Do not use a provisional suggestion in document prose.
5. Candidate discovery does not change Chapter 3.
6. After owner decisions, prefer deterministic projection of accepted names, roles, and limits into a Chapter 3 proposal.
7. If deterministic projection is unsafe, require a second explicit action for one bounded composition call.
8. Accept through existing append-only document authority.
9. If the owner accepts no peers, state directly that peers do not set the strategy or target and describe only the limited posture use the evidence permits.
10. Never rerun or rewrite Chapters 1, 2, 4, 5, or 6.

Known empty-cohort regression to cover: a newer artifact must not claim
there is no accepted cohort when durable accepted peer decisions already
exist. Incorrect empty-cohort prose loses to durable accepted P6 peer
state. Do not read this fixture as the focal organization being its own
peer.

## Chapter 4 — Strengthen the evidence base

User-facing action: **Strengthen the evidence base**

### Prompt: strengthen_evidence_base

```text
Based on the strategy we are trying to support, identify which claims are strong enough to lead, which should be qualified, and which should remain parked. Use only available evidence and locators. Do not invent metrics, dates, outcomes, or source support. Keep the proposed Chapter 4 document text in direct organizational voice. Keep analysis, parked claims, and strengthening suggestions outside the proposed document text.
```

## Chapter 5 — Build a simple case

User-facing action: **Build a simple case**

### Prompt: build_a_simple_case

```text
Using the accepted fundraising ask, organization frame, peer choices, and strongest available evidence, write a simple, persuasive case for support. State the central argument, why it matters now when the evidence supports a timing claim, why this organization is positioned to act, and how the funding would be used. Use direct organizational voice so the result can be pasted into a strategy or case document without rewriting. Do not invent outcomes, urgency, an amount, funder interest, access, or organizational commitments. Keep the strongest credible alternative angle and the conditions that would change the case outside the proposed document text.
```

Return separately:

- the proposed Chapter 5 document text;
- supporting evidence;
- limitations;
- the strongest credible alternative;
- conditions that would change the case; and
- an exact no-change result when the existing case is already stronger.

The alternative and analysis never enter the center document. Accepting the
proposal changes Chapter 5 only.

## Chapter 6 — Refresh the funder map

User-facing action: **Refresh the funder map**

### Prompt: refresh_the_funder_map

```text
Based on the chosen case and current evidence, refresh the funder map with a small set of plausible candidates. For each, give a concise why-fit, route, available evidence, and a material caveat. Do not invent eligibility, invitation, warm access, open programs, deadlines, or acceptance. A visible relationship sample does not establish access. Keep analysis and set-asides outside the proposed Chapter 6 document text.
```
