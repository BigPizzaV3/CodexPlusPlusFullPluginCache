---
name: e-mployee-inclusion-test
description: Classify a proposed AI system or agent with the E-mployee inclusion test from The E-mployee Operating Model and decide whether to include, defer or exclude it as an E-mployee role. Use when someone asks whether an agent, copilot or "digital worker" is a real role, or how to classify entries in an AI registry.
---

# E-mployee Inclusion Test

Chapter 3 turns the canonical definition into six necessary operating conditions and a CEO inclusion/exclusion test that ends in Include, Defer or Exclude. The canonical definition: an E-mployee is "an AI agent an individual directs like a member of a personal workforce by delegating objectives, supervising and reviewing output, and remaining personally accountable for what it produces." "The status belongs to the relationship, not to the model." A modest system can qualify. A sophisticated one can fail.

## When to use
- The user asks whether a system, agent, copilot or "digital worker" counts as an E-mployee role.
- The user is building an inventory or registry of "AI employees" and needs each entry classified.
- A vendor or team calls something "autonomous" and the user wants to test the claim before it shapes permissions.
- Do not use this to write the role's full specification. After an Include, use `role-charter`. To check whether an AI rollout produces real work at all, use `ai-access-audit`. To choose which candidate goes first, use `first-role-selection`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. What the system does, how often or on what trigger, and for whom.
2. What data it can reach and what actions it can take (read, draft, write, send, pay).
3. Who reviews its output, and who can correct, pause or stop it.

If the user cannot answer, classify anyway and mark the gaps `Missing`. Do not stall.

## Category boundary map
| Category | What it describes | What it does not establish |
|---|---|---|
| Software | A technical system or feature | A job, authority, or responsibility |
| Assistant | A system that supports a person's work | A standing objective or independent authority |
| AI agent | A system capable of a task or multistep workflow with some autonomy | Personhood, reliability, or permission to act |
| E-mployee | An AI agent placed in a standing human-directed role with objective, authority boundary, output, review, and retained human accountability | Legal employment, consciousness, moral agency, or independent liability |
| E-mployer | The human person who directs E-mployees | A guarantee that one person personally performs every control activity |
| Legal person | A category defined by applicable law | A status created by an operating metaphor |

Watch for the two category errors: **product-brand substitution** (accepting a vendor's "agent", "copilot" or "digital worker" label as an operating fact) and **anthropomorphic substitution** (treating fluent language as intention, judgment or status).

## Six necessary operating conditions (exact, in this order)
| # | Condition | What must be true | Sign it is absent |
|---|---|---|---|
| 1 | A standing role | Exists beyond a single prompt or demonstration; runs on a cadence or trigger; named by function, not vendor or model. "Recurrence with purpose." | One-off or occasional use; a name like "Autonomous Finance Employee" that "says too much". |
| 2 | A delegated objective | States what, for whom and under what conditions; bounded enough to evaluate; can be revised. "Delegation is not abandonment." | The purpose is "use AI". "A role that cannot be corrected is not being directed; it is being left to continue." |
| 3 | A defined authority boundary | Explicit and revocable; covers data and action (observe, retrieve, draft, recommend, execute, approve, spend, communicate); names exclusions. | The technical integration defines the managerial role. "Capability becomes permission by accident." |
| 4 | A defined output | Format, timing, evidence expectation and recipient; carries uncertainty, missing evidence and unresolved conflicts. Need not be final. | Polished output with no decision use. "Fluency is not a definition of done." |
| 5 | Supervision and review | Proportionate to consequence; the reviewer has knowledge, time, authority to reject or pause, and a route to escalate. | "Human in the loop" exists only in policy. "A reviewer who cannot disagree is not supervising." |
| 6 | Retained human accountability | A human or institution directs, supervises, reviews, corrects, explains and remediates; control points stay visible. Managerial accountability, not legal liability. | A named person without control. "Naming a person without providing those conditions is not accountability. It is exposure." |

## The CEO inclusion/exclusion test
| Test question | Include as a candidate E-mployee when… | Exclude or defer when… |
|---|---|---|
| Is there a standing role? | The work recurs or is triggered by a defined process. | The use is occasional, personal, or a one-off experiment. |
| Is there a delegated objective? | The role supports a named result for a named recipient. | The purpose is only "use AI" or "increase adoption." |
| Is authority explicit? | Observe/draft/recommend/execute limits are documented and revocable. | The technical integration silently determines what the system may do. |
| Is the output defined? | Format, evidence, recipient, timing, and acceptance condition are clear. | The system produces fluent activity with no decision use. |
| Is review real? | A competent reviewer has time, authority, and an escalation path. | "Someone checks it" is the only control. |
| Is accountability retained? | A human or institution can explain, correct, remediate, and stop the role. | The organization points to the system or a powerless reviewer. |
| Are legal and rights boundaries addressed? | The role is screened for applicable law, data, labor, safety, IP, and contractual issues. | The label is being used to avoid or pre-empt those questions. |

The three decisions:
- **Include**: a candidate E-mployee role that must receive the relevant role, authority, review and measurement controls.
- **Defer**: the idea may be useful but is not yet sufficiently specified or reviewable.
- **Exclude**: do not place it in the E-mployee category, because the use is ordinary assistance or the risks and controls do not justify the role.

**Necessary is not sufficient.** "Classification is the beginning of disciplined evaluation, not a promotion." Inclusion is not approval, and exclusion is not a rejection of AI. A role that passes can still fail on value, data, review cost or consequence. No fixed technical architecture is required. "Excluding a proposed role is a management decision, not a failure of imagination."

## What the E-mployee does not claim
Check that no one is using the label to claim **personhood**, **consciousness**, **employment status**, **moral agency**, a **transfer of human accountability**, or **universal autonomy**. The vocabulary must never be used to avoid consultation, wages, worker protections or data duties.

## Steps
1. Place the system on the boundary map. Name any product-brand or anthropomorphic substitution.
2. Test the six conditions in order. Mark each met, not met or `Missing`, and label the evidence.
3. Run the seven rows of the CEO test. On the legal and rights row, record only whether screening has happened and by whom. Do not give a legal conclusion.
4. Decide. If any row falls in the right-hand column, do not Include. Choose Defer when specification or staffed review could close the gap. Choose Exclude when the use is ordinary assistance or the risks and controls do not justify the role.
5. Write the minimum registry record: role name and version, objective, owner, approved inputs, exclusions, authority, output, reviewer, escalation route, status, and stop condition. Here it is a classification device only. The full Role Charter comes later.
6. Close with the boundary decision discipline: "Name the role. State the objective. Limit the authority. Define the output. Staff the review. Retain accountability. Then decide whether the E-mployee term clarifies the work or merely flatters the software."

## Output format
1. **Category**: where the system sits on the boundary map, and any category error.
2. **Six conditions**: a table (Condition | Status | Evidence and label).
3. **CEO test**: a table (Test question | Answer | Include or exclude/defer column).
4. **Decision**: Include, Defer or Exclude, with reasons. For Defer, list what must be specified or staffed. For Include, state what remains unproven.
5. **Registry record**: the eleven minimum items, with `Missing` where unknown.
6. **Label check**: one line confirming none of the six non-claims is being made, or naming the one that is.
7. Status line: *The book's proposed inclusion test. Not a legal test, an academic consensus, or a certification standard.*
8. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 3.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
