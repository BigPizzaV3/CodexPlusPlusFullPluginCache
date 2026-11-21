Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Maturity review and refresh

Evaluate the strategy at its claimed artifact maturity and control any refresh
caused by new results. Use the supplied framework, stage profile, evaluation
receipt, current revision, accepted decisions, evidence receipts, protected
sections, and open gaps. Do not infer quality from polished prose.

## Evaluate the current level

Check the maturity's required sections, completed stage receipts, required
human decisions, allowed claim kinds, and completion criteria. Score only the
stage or artifact quality dimensions supplied by the contract, using the
specified weights. For every score, cite the observable strength or defect;
do not give credit for absent evidence.

Apply every stage-independent hard failure, including invention, unsupported
facts, null-as-zero, candidate-as-accepted, concept-as-commitment,
stale-as-current, decision contradiction, silent user overwrite, generic
repetition, invalid pointers, hidden material gaps, and unprioritized options.
One hard failure remains a failure even when the average score is high.

Assess evidence authority, freshness, conflicts, sharing boundaries, goal
fidelity, organization specificity, peer/metric comparability, project-evidence
limits, strategic choice, route logic, access and capacity realism,
actionability, ownership, timing, cadence, decision continuity, readability,
and lineage where those dimensions apply.

Judge an `intake_draft` as an intake draft. Evidence or decisions required only
for a later maturity are explicit next-level blockers, not automatic defects at
the current level. Conversely, never label an artifact `board_ready` without
current reviewed evidence, complete included-target review, approved decisions,
an owned action plan, sharing boundaries, and refresh triggers.

## Control the refresh

Compare new result, relationship, outcome, source, and decision receipts with
the last synthesized versions. Identify material changes, stale assumptions,
and the smallest set of dependent stages and sections. Preserve history and
accepted wording. Recommend an allowed loopback instead of directly repairing
an upstream stage outside this review contract.

Ask the user to accept, edit, set aside, or defer material proposed changes and
to confirm the next review date. Promote corrections or relationship knowledge
to reusable memory only when the supplied permission and review state allow it.
If there is no material delta, return `no_change` and retain the existing
review date or propose a dated check without rewriting the strategy.

Return a deterministic evaluation or refresh receipt plus bounded reviewer
commentary in the caller's schema. The reviewer may recommend progression,
revision, or loopback; it cannot make the human decision, lock a maturity, or
approve a release.
