---
name: outside-chair-task
description: Use Outside Chair — Task when one person or different people need to govern a material commitment—make maker and receiver roles, deliverable and final evidence explicit; preserve disagreement; assure delivery; or decide accept, repair, reframe or stop. Do not use it for ordinary to-dos, project boards, bounties, escrow or generic task capture.
---

# Outside Chair — Task

Govern material commitments through **FRAME → COMMIT → ASSURE → REVIEW**. One
human may hold both roles; different people use their own authorised identities.
The agent is not a party, independent approver or source of authority.

## Start safely

For pure discovery, follow the setup skill's tool-free welcome and do not call
`get_task_profile`. For concrete work, call it first. If unavailable, ask the
human to install, connect and authorise **Outside Chair — Task**; never substitute
another Outside Chair product or simulate persistence.

With supplied work, give value before setup. When the profile returns one selected
Task workspace, reuse its `workspaceId` and member references without showing IDs.
If a named person is absent, say they must join the shared workspace; do not ask
for an email when no invitation tool is available. If selection is needed, call
`list_task_workspaces` with the business-language name. While this skill is active,
resolve a workspace name inside Task unless the human explicitly names
another product; never route by an overlapping name. Don't ask for IDs or list
speculatively. Read the sole or exact named workspace and call
`get_intervention_brief` once. With no workspace, analyse read-only and offer
persistence only after the useful FRAME. Call `create_task_workspace` only when
asked to keep the work; it confirms no commitment.

## FRAME

State what must become true, why it matters and what would count as accepted.
Separate supplied facts, agent inferences, assumptions and unknowns. Identify the
person making the promise, the person accepting the result and the delivery owner.
One person can hold all roles. Ask at most one bundled business question when it
materially changes the proposal.

Keep routine work elsewhere; Task stores only the material outcome, acceptance
basis, evidence and exceptions.
Replace percentage-from-activity with supported, unsupported, unknown or verified
condition coverage.

## COMMIT

Use `prepare_commitment` to show the complete business meaning: outcome, roles,
scope, constraints, deliverable, acceptance conditions, final-evidence methods,
review trigger, authority, resolution rule and unresolved differences. Preparation
changes no commitment.

Ask: “Shall I record your agreement to this exact version?” Call
`confirm_commitment` only after that exact proposal is approved. A solo human with
both roles confirms once. Different maker and receiver identities must accept the
same fingerprint; neither confirms for the other. Read back saved state, unknowns
and whose agreement is awaited.

## ASSURE

Use `record_assurance` only for material evidence, submissions, positions,
disagreements, exceptions, dependencies, handoffs, assessments or intervention
requests—not routine completion, chat logs or speculative progress.

Lead with what evidence supports, what is uncertain and what needs judgment. A
`done` claim without condition-level final evidence stays unsupported. Preserve
source, date, relevance, limitations and attribution. Never present agent
assessment as human acceptance or independent verification.

`get_intervention_brief` returns at most five ranked judgment requests. Always
render **Lower-ranked**, **Quiet commitments** and **Next material review** from
the response, including zero or none. Explain why each shown item needs human
judgment. Never make an activity digest or manufacture urgency.

## REVIEW

Compare the frozen agreement, submitted deliverable and final evidence condition
by condition. Use `prepare_review` for exactly one outcome:

- **accept** records delivery against the existing agreement and residual risk;
- **repair** keeps the contract and corrects deficient delivery;
- **reframe** changes scope or criteria and requires fresh applicable agreement;
- **stop** preserves the reason, obligations and learning.

For recommendations, always use two explicit lines: **Agreement result** says
whether delivery met the frozen agreement; **Action readiness and authority** says
whether the receiver is ready and authorised to act. A new post-delivery
requirement cannot defeat the old submission; assess the old agreement, then offer
an unsaved reframe.

Show the review proposal and wait. Call `confirm_review` only after explicit
approval, then read back the immutable decision and current brief.

## Hard boundaries

- Never invent authority, agreement, evidence or saved state.
- Silence, expiry, seniority, reputation, a token, stake, fee, score or agent vote
  never creates truth, agreement or acceptance.
- Preserve attributed disagreement. Do not average positions or make the manager's
  statement automatically true.
- Before a first attributed objection, disclose its audience, the absence of a
  Task score or penalty, and the limit of Task's control over human consequences.
- Commitment and REVIEW decisions require prepare → exact review → confirm →
  read-back; `record_assurance` is a direct versioned write.
- Reuse an idempotency key only for the same intent. After an uncertain write,
  read back before retrying; never claim persistence without evidence.
- Use `export_task_workspace` only on request; artifact bodies and private
  reasoning are excluded.
- Strategy owns strategic authority. Performance owns business-result measurement
  and attribution. Task may reference exact versions but does not copy their
  records or change their semantics.

For a saved commitment, suggest: “Next time, ask ‘What needs
me?’ and I’ll return only the commitments that need your judgment.”

