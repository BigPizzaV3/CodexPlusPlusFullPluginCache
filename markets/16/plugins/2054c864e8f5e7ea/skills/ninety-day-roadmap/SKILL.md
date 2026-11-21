---
name: ninety-day-roadmap
description: Build a 90-Day E-mployer Roadmap that moves one bounded AI role through six evidence and decision gates to a go, revise, pause, stop, retire or refuse decision. Use when someone asks for a 90-day plan, a pilot plan or a launch plan to get a first AI agent or role live.
---

# 90-Day E-mployer Roadmap

Chapter 15 (headed "90-Day E-mployee Plan") turns the operating model into a first sequence. Choose one bounded outcome, write the role, assign the human authority around it, measure the work before changing it, govern the risk, and make a decision that can be reversed. The **90-Day E-mployer Roadmap** "is not a promise that an implementation will succeed in ninety days." It is "a sequence of evidence and decision gates", and "The periods are therefore gates, not calendar promises." The CEO's job is "to make the first decision small enough to learn from and serious enough to matter."

## When to use
- "Give me a 90-day plan to get our first AI role live," or "Plan our pilot."
- A transformation team needs gates, owners and artifacts for one bounded outcome.
- Preparing the Day 76–90 decision memo or the handoff package.
- Do not use this to choose between candidate roles. Use `first-role-selection` first. For several roles, use `portfolio-review`. If the user is unsure where to start, use `get-started`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. What is the one outcome, who is its business owner, and who is the CEO or E-mployer sponsor?
2. What is explicitly excluded, and who would review the output?
3. What are the constraints: data, available specialists, decision date and jurisdictions?

If the user cannot answer, draft the plan anyway and mark the gaps `Missing`. Do not stall.

## The mandate
Before anyone configures a model, the sponsor issues a mandate. It states the outcome, business owner, boundaries, resources, decision date and **right to stop**, plus what will not be attempted. "Exclusions are not a sign of weak ambition. They are how ambition becomes testable." "Use an E-mployee to help our strategy team prepare a weekly evidence brief" is governable. A mandate to "transform research with agents" is not.

## The six phase gates (exact)
| Days | Leadership action | Required artifact | Decision owner | Gate question |
|---:|---|---|---|---|
| 0–15 | Choose one bounded outcome and authorize a narrow experiment | Leadership mandate; outcome statement; initial Opportunity Matrix record; affected-party, worker-voice, specialist, and stop map | CEO / E-mployer sponsor | **Choose one bounded opportunity—or refuse or hold it.** |
| 16–30 | Define the role, baseline, risk, authority, review, and diligence | Role Charter; baseline/counterfactual; Risk Classification; capacity plan; vendor/tool diligence; authority and stop design | Outcome owner with required specialists | **Approve the objective, permissions, evidence plan, reviewer, and stop conditions.** |
| 31–45 | Build the smallest observable and reversible version | Test set; source/data permission; logs; provenance; acceptance criteria; rollback and human fallback | Role owner | **Is the role testable, bounded, observable, and reversible?** |
| 46–60 | Run a controlled pilot and monitor what matters | Pilot log; quality and exception sample; review queue; authority-use record; workforce feedback; incident/escalation record | Role owner and reviewer | **Continue, narrow, correct, pause, roll back, or stop?** |
| 61–75 | Review economics, performance, authority, and human effects | Value Ledger; scorecard; Autonomy Ladder decision; Authority Matrix review; worker-impact record; updated risks | Finance, outcome owner, reviewer, risk and workforce owners | **Is evidence sufficient for a bounded next decision?** |
| 76–90 | Decide what happens next | Go/revise/pause/stop memo; board dashboard; updated registry; next experiment or retirement record | CEO / board or delegated portfolio authority | **Scale supported scope, revise, pause, stop, retire, or refuse.** |

"The first gate should be difficult enough to reject a vague opportunity. The final gate should be humble enough to reject a successful-looking one." Each gate names who decides, the evidence they will inspect, the risks still open and the action that follows if the gate is not passed.

## Days 0–15: choose one outcome
- Revisit the nine Opportunity Matrix factors with `first-role-selection`: business value, task stability, reversibility, data readiness, review burden, regulatory and customer stakes, human-skill effects, implementation and exit cost, and time to credible learning. Write the outcome in business language with `outcome-first-design`.
- The sponsor asks five questions:
  1. What decision or human outcome would improve if this role worked?
  2. What work is included, and what work is explicitly excluded?
  3. Who can review the output with enough competence, time, context, and power to reject it?
  4. What would make us pause or stop before the pilot begins?
  5. What would we learn in ninety days even if we do not scale?
- Name a worker-voice owner, with a response owner and an escalation path. Triage the legal, privacy, security, labor, procurement, contract, intellectual-property, accessibility, safety and sector questions, and know when each becomes a gate.
- The phase ends with one bounded opportunity, a hold or a refusal. "'Several promising opportunities' is not a gate decision."

## Days 16–30: write the role and expose the baseline
| Days 16–30 artifact | Minimum content | Owner | Failure condition |
|---|---|---|---|
| Role Charter (`role-charter`) | Objective, inputs, exclusions, authority, outputs, definition of done, reviewer, escalation, logs, stop, learning loop | Outcome owner / role owner | The role cannot be described without naming a tool or vendor. |
| Baseline and counterfactual (`value-ledger`) | Current workflow, volume, quality, effort, errors, cycle time, risk, human alternative, time horizon | Finance / outcome owner | The business case contains only projected time savings. |
| Risk Classification (`risk-classification`) | Stakes, reversibility, rights/data exposure, blast radius, tier, minimum controls, reclassification triggers | Risk owner with specialists | The team labels risk by tool brand rather than consequence. |
| Capacity and review plan (`human-ai-org-chart`) | Competence, available time, peak demand, backup, rejection power, human fallback | Reviewer / operations | Approval depends on a reviewer who has no capacity or stop power. |
| Vendor/tool diligence | Purpose, terms, data use, security, model/tool version, change notice, exit path | Procurement / security / privacy / legal as applicable | The team cannot explain what changes or how access is revoked. |
| Authority and stop design (`authority-matrix`) | Allowed and denied powers, thresholds, gates, escalation, logs, expiry, revocation, rollback | Outcome owner / authority owner | Capability is treated as permission or authority. |
| Workforce and worker-voice record (`human-ai-org-chart`) | Affected work, training, workload, monitoring, feedback, remedy, response owner | Workforce owner | People affected by the change have no route to challenge it. |

Start a **decision log** recording the decision, date, owner, evidence inspected, dissent, unresolved question, next review and stop condition.

## Days 31–45: build the smallest reversible role
Build only what tests the agreed outcome. Use approved data, keep the audience narrow, deny authority the role does not need, record versions and environment, and enable logs and provenance before the first meaningful output. The test set covers ordinary items, ambiguous items, incomplete inputs, edge cases and refusal cases. Acceptance tests more than fluency: traceability, omissions, unsupported claims, formatting, escalation, refusal, data handling, permission boundaries and recovery.

| Build/test control | Evidence to preserve | Stop or revise trigger |
|---|---|---|
| Source and data permission | Approved sources, access record, retention and provenance | Unapproved data, unclear source rights, or missing lineage |
| Role and authority boundary | Allowed actions, denied actions, thresholds, reviewer gate | Output attempts an unassigned action or reaches a denied audience |
| Quality and refusal test | Test set, expected behavior, omissions, corrections, rejection | Repeated unsupported output, unsafe release, or unhandled ambiguity |
| Logging and observability | Version, input/output record as permitted, decision, reviewer, escalation | The team cannot reconstruct what happened or which version acted |
| Change control | Model/tool/prompt/connector record and retest | A material change occurs without impact review and retest |
| Rollback and fallback | Reversal exercise, manual route, responsible person, timing | Human fallback cannot operate or stop authority is unclear |

"Resist the desire to add integrations." Exercise the fallback, because "A fallback that exists only in a document is not a fallback. It is a hope."

## Days 46–60: pilot under supervision
| Pilot signal | Leading measure | Lagging measure | Decision use |
|---|---|---|---|
| Review capacity | Queue age, available hours, exception volume, backup coverage | Missed review, rushed approval, unresolved correction | Add capacity, narrow scope, or pause. |
| Quality | Sample results, rejection, traceability, error pattern | Rework, downstream correction, customer or user effect | Correct, retrain/redesign, or restrict. |
| Authority | Denied attempts, escalation, gate adherence | Unapproved release, financial or operational consequence | Remove power, tighten threshold, or stop. |
| Data and security | Access events, provenance completeness, permission tests | Exposure, loss of lineage, unresolved security issue | Revoke, isolate, reclassify, or escalate. |
| Workforce | Feedback volume, training completion, workload, monitoring signal | Sustained burden, skill erosion, job-quality deterioration | Redesign, compensate, narrow, or stop. |
| Economics | Utilization, realized redeployment, cost run-rate, attribution quality | Measured value after the agreed horizon | Update Value Ledger; do not convert time to profit. |

Declare a stop date even if everything looks positive. Record incidents and escalations with `ai-incident-response`. The gate asks: "Under what conditions did it work, what did the humans have to do, what failed, what changed, and is the supported scope clear?"

## Days 61–75: separate owner reviews
Run four reviews and never merge them into "one composite number". The **finance or Value Ledger owner** uses `value-ledger`. The **performance owner** uses `autonomy-review` for the ten scorecard dimensions and the Autonomy Ladder decision. The **authority owner** uses `authority-matrix` to review which powers were used, denied, escalated, approved, expired, revoked or rolled back. The **workforce owner** reviews training, workload, monitoring, skill formation, job quality, worker voice and remedy. Test control effectiveness, not control presence.

## Days 76–90: make the next decision
| Decision | When it is appropriate | What the memo must authorize |
|---|---|---|
| Go / bounded scale | Evidence supports the exact proposed expansion; capacity and controls remain adequate | Scope, owner, review, budget/capacity, next gate, and stop condition |
| Revise | Outcome is promising but role, data, authority, review, or economics are incomplete | Specific redesign, owner, evidence, deadline, and re-entry gate |
| Pause | A material question or change prevents safe continuation | Stop authority, evidence preservation, specialist review, and restart condition |
| Stop | The role is not credible, controllable, or worth the exposure | Shutdown, fallback, notification review, owner, and learning record |
| Retire | The role no longer creates defensible value or cannot be supported | Retirement record, access revocation, data/evidence disposition, and replacement decision |
| Refuse / do not adopt | The consequence, dependency, or human effect is not acceptable | Decision rationale and any safer alternative |

"A go decision should not be broader than the evidence." The memo states exactly what was tested and what was not. Update the registry and board dashboard with `portfolio-review`.

## Handoff package and Day 91
The minimum package holds: mandate, outcome statement, Opportunity Matrix record, Role Charter, baseline and counterfactual, Value Ledger, Risk Classification record, Authority Matrix, reviewer-capacity plan, data and permission map, vendor/tool diligence, test set, logs and provenance, pilot results, performance scorecard, worker-impact review, legal/privacy/security decisions, dependency map, stop and retirement record, decision log and board dashboard. Name which artifact is authoritative when records disagree, and set the review calendar. Name an owner for each handoff area: Role (role owner), Outcome (outcome owner), Evidence (finance / transformation lead), Performance (reviewer / quality owner), Authority (authority owner), Governance (risk / security / privacy), Workforce (workforce owner), Dependencies (portfolio owner), Decision (CEO / board authority) and Next gate (transformation lead). "A roadmap that ends at Day 90 without an owner for Day 91 is an experiment with a deadline, not an operating handoff."

## Regional addendum (offer it, do not assume it)
Ask whether a configurable regional addendum applies, and never assume a country. A MENA deployment, for example, may need checks for data residency, cross-border transfer, language, connectivity, identity, local labor practice, formal versus informal work, gender and youth inclusion, training access, public-sector requirements and country-specific approval. The applicable jurisdiction, affected people, data, contract and sector determine which specialist reviews are required. Regional evidence is "not a regional readiness score."

## Steps
1. Draft the mandate from what the user gave and mark gaps `Missing`.
2. Fill the six-gate table with named decision owners and target dates. Label the dates as gates, not promises.
3. For each phase, list its artifacts, owners and failure conditions, and the sibling skill that produces each one.
4. Set the pilot stop date and the Day 76–90 decision date. Offer the regional addendum.
5. If the user is already at Days 76–90, write the decision memo from the evidence and choose one decision from the table.
6. Apply the CEO's decision rule. The roadmap is complete "when it makes a decision possible, not when every uncertainty has been eliminated." It guards against reckless acceleration and bureaucratic delay through "proportionate controls with explicit owners, dates, evidence, and stop power."

## Output format
1. **Mandate**: outcome, business owner, boundaries, resources, decision date, right to stop and exclusions.
2. **Gate plan**: the six-gate table with names and target dates.
3. **Phase checklists**: artifacts, owners, failure conditions and the sibling skill for each.
4. **Decision log** template, with the first entries filled in.
5. **Day 76–90 memo**, when the user is at that stage: the decision, what was and was not tested, and what the memo authorizes.
6. **Handoff package** checklist and the named Day 91 owner.
7. Status line: *Author-created sequence of evidence and decision gates. Not a promise that an implementation will succeed in ninety days. Not legal advice; completing its fields does not establish legal compliance.*
8. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 15.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
