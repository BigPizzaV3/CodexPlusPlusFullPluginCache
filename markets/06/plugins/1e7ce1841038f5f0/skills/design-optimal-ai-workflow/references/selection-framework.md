# Tool Selection Framework

## Decision sequence

0. Inspect the active method decision. If it is closed, applicable and conflict-free, keep it and skip candidate comparison unless a canonical reopen trigger exists.
1. For an open or validly reopened decision, eliminate tools that fail mandatory constraints.
2. Compare surviving tools on the actual stage and artifact, not their general reputation.
3. Select the simplest chain that meets acceptance criteria.
4. Design a provider-independent fallback for critical stages.
5. Verify the chain with a representative pilot before scaling.

## Mandatory filters

- required modality and input/output formats;
- language and quality requirements;
- regional and account availability;
- data sensitivity, retention, training, residency, and access controls;
- commercial-use, copyright, attribution, and licensing requirements;
- API, automation, export, and integration requirements;
- volume, latency, reliability, and rate limits;
- budget ceiling and procurement restrictions;
- accessibility and human-approval requirements.

Reject a candidate when a mandatory filter fails or cannot be verified for a high-risk workflow.

## Weighted comparison

Use project-specific weights totaling 100%. Recommended dimensions:

| Dimension | What to examine |
|---|---|
| Output quality | Fidelity to the exact artifact, consistency, controllability, error profile |
| Workflow fit | Inputs, exports, APIs, batch support, editing, collaboration |
| Reliability | Availability, reproducibility, rate limits, recovery, support |
| Speed | Generation time, queueing, editing time, review burden |
| Total cost | Subscription, usage, seats, integration, review, rework, storage |
| Privacy/security | Data use, retention, access controls, residency, auditability |
| Rights/compliance | Commercial terms, licensing, attribution, regulated use |
| Usability | Learning curve, team skills, maintainability, accessibility |
| Portability | Standard formats, export, provider substitution, lock-in |

Show weights, evidence, uncertainties, and disqualifiers. Do not create a numeric winner from unsupported scores.

## Total-cost model

Estimate only when enough inputs exist:

`total cost = subscriptions + usage + integration + human review + expected rework + storage/transfer + switching risk`

Label currency, tax treatment, period, volume assumptions, included allowances, and review date. Prefer a range when usage or pricing is uncertain.

## Evidence hierarchy

This ordering evaluates tool fit while a selection is open or validly reopened. It does not replace the canonical method-evidence hierarchy and closure rules in the shared decision-authority model.

Prefer:

1. official documentation, pricing, terms, security and status pages;
2. direct representative tests on user artifacts;
3. reproducible independent benchmarks matching the task;
4. credible specialist reviews;
5. community reports as weak signals.

Never treat leaderboard rank or social popularity as sufficient evidence of workflow fit.

## Selection outcomes

- **Primary:** best verified fit for the current constraints.
- **Fallback:** preserves critical output when the primary fails.
- **Specialist:** justified only for a stage where it materially outperforms the primary.
- **Watchlist:** promising but insufficiently verified, unavailable, or unnecessary now.
- **Rejected:** fails a mandatory requirement; state the reason.
