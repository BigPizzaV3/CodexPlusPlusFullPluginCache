---
name: autonomy-review
description: Run a periodic E-mployee performance review with the ten-dimension scorecard and the Autonomy Ladder, ending in a promote, hold, demote, retrain/redesign or retire decision, from The E-mployee Operating Model. Use when someone asks whether an AI agent should get more autonomy, be pulled back, or have its performance reviewed.
---

# E-mployee Autonomy Review

This workflow reviews an E-mployee's performance and decides its control arrangement (Chapter 9). The central rule: "Autonomy is earned, conditional, and reversible. It is not a property declared at purchase." Performance is not value. The Value Ledger asks whether the work pays (go, revise, pause, retire). This review asks whether the role performs its assigned work within its current controls (promote, hold, demote, retrain, retire). "Usage or confidence is not reliable performance." "The next level is never owed."

## When to use
- A scheduled (for example quarterly) performance review of a running role.
- A proposal to reduce human review or "let it run on its own".
- A change (new model, vendor, source, volume, recipient) or a warning sign such as rising correction time.
- Do not use this to decide whether the role pays. Use `value-ledger` for that. Which actions the role may take (send, spend, approve) is a separate decision for `authority-matrix`: "A Level 3 performance decision does not itself grant the right to act." After an actual incident, use `ai-incident-response`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. The Role Charter (version, owner, objective, definition of done), the current Ladder level and the reviewer.
2. The period and the evidence: samples, counts, logs, review hours, exceptions, incidents and changes.
3. The move being considered, and any thresholds already set.

If the user cannot answer, draft anyway and mark the gaps `Missing`. Do not stall. Never supply a threshold the user has not set. Write `Missing: threshold` and name who should set it.

## The E-mployee scorecard (ten dimensions)
Derive it from the Charter's objective and definition of done. Each measure states its period, sample, numerator, denominator, data source, owner, reviewer, threshold, and consequence of a miss.

| Dimension | Question | What to measure |
|---|---|---|
| Outcome attainment | Did the role produce the specified result for the intended recipient? | Completed outcomes, acceptance decisions, missed objectives, and recipient use. |
| Quality | Did the output meet the definition of done and domain standard? | Accuracy, completeness, appropriateness, provenance, correction, and rework. |
| Reliability | Did the role behave consistently across relevant cases and conditions? | Performance across time, volume, data variation, model/version, and normal exceptions. |
| Exception rate | How often did the role encounter or create exceptions, and did it surface them? | Exception frequency, severity, detectability, routing, and missed exceptions. |
| Human review burden | Can a competent reviewer inspect and correct the work at actual volume? | Review time, correction time, escalation time, fatigue, sampling quality, and queue age. |
| Cycle time | Did the workflow complete within the required period without shifting delay? | Time to draft, review, release, resolve, and recover. |
| Cost | Does the operating cost remain inside the approved economic case? | Supervision, correction, maintenance, integration, support, and exit exposure. |
| Traceability | Can the organization reconstruct what happened? | Inputs, sources, versions, instructions, actions, approvals, corrections, and overrides. |
| User/customer effect | Did the recipient experience the intended service or decision effect? | Acceptance, complaints, confusion, downstream rework, accessibility, and distribution. |
| Risk indicators | Did exposure remain within the role's approved boundary? | Privacy, security, legal, safety, rights, reputation, trust, and scope-change signals. |

"No dimension is sufficient alone." Keep **observed performance** ("Ninety-six percent of sampled claims were traceable," with the sample and rule visible) separate from **interpretation** ("The role is trustworthy").

**Measure the right denominator.** Include escalated, corrected-before-release, abandoned, difficult and rejected cases. Do not define quality as the absence of a complaint, or hide specialist time spent on exceptions. Record the sample, the missing cases and the confidence. Test at the length and complexity the role will actually face.

## Leading indicators and responses
| Leading indicator | Why it matters | Possible response |
|---|---|---|
| Review queue age rising | Review capacity may be failing before quality is visible. | Hold or reduce volume; add capacity; redesign. |
| Correction time rising | The role may be producing more hidden work. | Retrain, narrow task, or demote. |
| Missed exception trigger | The role may be silent precisely where it should be cautious. | Immediate rollback or tighter review. |
| Source/data freshness failure | Reliability may be illusory because inputs changed. | Pause; verify data owner and freshness rule. |
| Incomplete traceability | The organization may be unable to inspect or explain output. | Hold or demote until logs are restored. |
| Scope drift | The role may be doing a different job from the Charter. | Reauthorize, narrow, or stop. |

A role should not stay at a higher level because no incident has yet occurred. "Absence of an incident is not clearance."

## The Autonomy Ladder (exact)
It "describes what the human system does around the role," not intelligence or trust.

| Level | Human role | Entry evidence | Exit or rollback trigger |
|---:|---|---|---|
| 0 | Monitor after execution | Low stakes, reversible state, detectable exceptions. | Undetected errors, drift, or consequence expansion. |
| 1 | Review exceptions | Stable outputs and tested exception triggers. | Missed exception, review overload, or new failure mode. |
| 2 | Sample and audit | Reliable post-hoc detection and sufficient sample design. | Quality drift, sampling blind spot, or rising rework. |
| 3 | Review before action | Action affects money, customers, reputation, rights, or irreversible state. | Reviewer lacks time, competence, or authority; rollback required. |
| 4 | Human decides; AI researches | High variance, high stakes, thin evidence, or unresolved legal/rights issues. | Evidence improves only after a new approval cycle. |

- The levels are "not a one-way staircase." Every level needs a named reviewer, adequate time, competence, escalation, logs, and the power to reject or stop.
- The numbers are labels, not a score. In the book's example, moving from Level 1 to Level 2 is a promotion and moving from Level 1 to Level 4 is a demotion. Describe every move by the human control it adds or removes.
- Level 0 is not permission to ignore the role. Level 2 sampling "is not a discount version of review." Level 4 "is not a punishment."

## The five gates
| Gate | What must be true | What must be recorded |
|---|---|---|
| Promote | Next-level evidence, sustainable review, acceptable risk, tested rollback. | New level, scope, conditions, expiry, reviewer, stop trigger. |
| Hold | Current-level performance acceptable; evidence incomplete or mixed. | Missing evidence, unchanged boundary, next sample/date. |
| Demote | Material failure, drift, overload, or consequence expansion. | Trigger, immediate reduction, owner, remediation, re-entry condition. |
| Retrain / redesign | Role remains plausible but needs controlled change. | Change proposal, test, version, approval, post-change evidence. |
| Retire | Outcome or control case no longer justifies continuation. | Exit plan, fallback, logs, notifications, learning record. |

"Promotion and demotion should be symmetric." Demote before harm expands; a critical failure may need immediate rollback even when the average looks good. Retraining is "not simply asking the same system to try harder." It is a versioned, tested, approved change. Gates can combine, as in the book's "hold at Level 1 and retrain/redesign."

## Performance/autonomy worksheet
It connects the written job to a control decision. It does not replace the Role Charter, Value Ledger or Authority Matrix.

| Worksheet block | Required entry |
|---|---|
| Role and period | Role Charter version, owner, current level, measurement period, and reviewer. |
| Outcome | Objective, recipient, definition of done, and outcome-attainment result. |
| Quality | Sample, standard, error, omission, rework, and correction result. |
| Reliability | Conditions tested, variation, versions, data changes, and unexplained failures. |
| Exceptions | Rate, severity, detection, routing, missed exceptions, and response. |
| Human review | Reviewer competence, hours, queue, correction, escalation, and stop power. |
| Cycle time | Draft, review, release, resolution, and recovery timing. |
| Cost | Supervision, maintenance, correction, integration, and exit signals. |
| Traceability | Inputs, sources, instructions, versions, actions, approvals, corrections, and overrides. |
| User/customer effect | Acceptance, complaints, downstream work, accessibility, and distribution. |
| Risk indicators | Privacy, security, legal, safety, rights, reputation, trust, and scope changes. |
| Decision gate | Promote, hold, demote, retrain/redesign, or retire. |
| Conditions | New level, unchanged or narrowed boundary, review date, evidence, and rollback. |

## Steps
1. Confirm the role, Charter version, owner, current level, period and reviewer.
2. Fill the scorecard. For each dimension give the observation with its sample, numerator and denominator, then the threshold, then the interpretation. Check the denominator.
3. Check the leading indicators and note the response each one calls for.
4. Check the change log. A new model, vendor, data source, policy, volume, language, interface, recipient or workflow reopens the question without waiting for an incident. "Regression is not a contradiction of autonomy. It is what reversibility looks like in operation."
5. Check review for automation bias. The reviewer needs a reason, method, time and authority, and some independent verification (check a source, reconstruct a calculation, compare a separate record, test a sample). "An explanation is not proof." Measure review as work: too fast to be credible, too slow to be sustainable or too weak to change the outcome means the level is wrong.
6. Check thresholds as operating choices: each tied to consequence, sample, reviewer and fallback, with an owner and an expiry, and ordinary variation kept apart from a material trigger.
7. Compare the evidence with the entry evidence of the proposed level and the exit triggers of the current one. Choose the gate, confirm what must be true, and fill what must be recorded.

## Output format
1. **Scorecard**: Dimension | Observation (sample, numerator/denominator) | Threshold | Interpretation | Evidence label.
2. **Leading indicators** triggered, and the response for each.
3. **Ladder position**: current level, proposed level, entry evidence met or not, exit triggers hit, in terms of human control.
4. **Performance/autonomy worksheet**: a two-column table (Worksheet block | Entry) with all 13 blocks in order.
5. **Gate decision** with every "what must be recorded" item filled, or marked `Missing`.
6. Status line: *Author-created operating instrument. Not a benchmark, certification, regulatory classification, legal category, or guarantee.*
7. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 9.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
