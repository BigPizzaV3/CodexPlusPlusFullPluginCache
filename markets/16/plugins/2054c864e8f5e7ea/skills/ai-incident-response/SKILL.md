---
name: ai-incident-response
description: Map who authorized, supervised, inspected, released, can explain and will remediate an AI result, and run the nine-step incident sequence from The E-mployee Operating Model. Use when an AI agent got something wrong, for a post-incident review, or to map accountability before launch.
---

# Accountability Chain and Incident Response

Chapter 11 opens with a warning. The sentence "the AI made a mistake" can be accurate and still be useless, because it names nobody who can correct the result. Naming one powerless manager is no better. The book calls that "blame transfer". This workflow maps the human and institutional control points behind an AI-enabled result and runs a response in proportion to the harm. The practical question is: **"Who could authorize, supervise, inspect, release, explain, and remediate this result—and who can do so now?"**

## When to use
- An AI agent produced a wrong result, sent something it should not have or changed a record, and the user asks who is responsible and what to do now.
- A post-incident review, or a request to assign an incident owner.
- Before launch, when the user wants to map who holds each accountability link for a role.
- Do not use this to set a risk tier or minimum controls. Use `risk-classification` for that. To decide which action powers a role should hold, use `authority-matrix`.

## Inputs to gather
If the incident is live, give the first-hour actions below before asking anything.
Otherwise ask only for what is missing, at most three questions at a time:
1. What happened, when, to whom and in which workflow? Is the role still running?
2. Which role was involved, who reviewed the output and who released it? Is there a Role Charter or Authority Matrix?
3. What evidence survives (inputs, versions, logs, approvals, overrides, communications)? Was a vendor involved?

If the user cannot answer, proceed anyway and mark the gaps `Missing`. Do not stall.

## First hour and first week
Incident response has "two clocks".
- **First hour:** identify the active trigger, stop or contain the role, protect the fallback, preserve the current state and set up a communication channel. The safe action may be a pause, a queue freeze, a permission revocation, a switch to a human path, or a hold on only the affected workflow. Do not ask the affected team to keep operating as normal while an investigation is "being planned."
- **First week:** move from stabilization to scope and remedy. Separate what is known, suspected and missing. Establish who was affected, which decisions were made, which records can be corrected and what specialist advice is required. Distinguish confirmed impact from possible exposure, and give the reason for each. A preliminary record can be updated, but it must not silently become the final story. "Missing evidence is itself a control finding." Protect the people who raise concerns.

## The incident sequence (nine steps, in order)
Assign one incident owner to coordinate. That person or function needs authority, resources and a deadline. Coordinating does not make them the legally liable party.
1. **Detect and stabilize.** Stop or contain the role, preserve the human fallback, block further propagation and identify pending work.
2. **Assign an incident owner.**
3. **Preserve evidence.** Secure inputs, instructions, model and tool versions, access records, outputs, review decisions, overrides, timestamps and communications. Do not rewrite the original. Record corrections as new evidence.
4. **Assess affected scope.** Identify the people, customers, records, jurisdictions, decisions and possible consequences.
5. **Correct the immediate result.** Repair records, rerun or reverse work, route cases to humans and document the correction.
6. **Review notification.** Obtain legal, privacy, customer, labor, safety, compliance and communications advice, and apply the relevant rules and facts.
7. **Review root cause.** Separate role design, data, model, tool permission, reviewer, workflow, vendor, policy and institutional causes.
8. **Redesign controls.** Narrow authority, change review, repair data, retrain, revise the Charter, add escalation or retire the role.
9. **Record learning and decide** whether to go, revise, pause, demote, retrain or retire.

The order can change with immediate danger or legal direction. The principle does not change: "stabilize first, preserve evidence, correct people's reality, then learn and redesign."

## The Accountability Chain (exact)
**Authorize → supervise → inspect → release → explain → remediate.**

| Link | Meaning | What to establish |
|---|---|---|
| Authorize | The decision to create or continue the role, set its objective, grant its permissions and place it in a workflow. | Can the authorizer show the Role Charter, intended outcome, Authority Matrix, reviewer, evidence gate and stop condition? Record separately who authorized the role, who approved the data use and who approved the system change. |
| Supervise | The continuing work of operating the role: monitoring, staffing review, tracking exceptions, maintaining data and instructions, responding to change and preventing silent scope expansion. | Did the supervisor have resources and authority? Could anyone receive the warnings? |
| Inspect | Examining whether the output meets the standard and whether the evidence is sufficient to release it. | Was the output "accurate, complete, appropriate, traceable, authorized, and fit for the decision"? Could the inspector reject it? |
| Release | The moment the output becomes an organizational action, communication, decision, record or commitment. | Who released it, and is that point visible in the Authority Matrix? If the E-mployee acted outside its authority, record both the action and the permissions that allowed it. |
| Explain | An operational reconstruction, not an account of model internals. | Input, instruction, version, output, review, release, observed effect and known gap. "'The model hallucinated' may be a hypothesis." State where the record is missing. |
| Remediate | Restoring the affected work and changing the conditions that produced or permitted the failure. | An owner, time frame, evidence and decision gate. "An apology without correction is not remediation." |

## Ten responsibility dimensions
| Responsibility dimension | Question | Failure when omitted |
|---|---|---|
| Ownership | Who owns the outcome and can allocate resources to correct it? | A named sponsor cannot change the system. |
| Operation | Who configured, ran, maintained, or changed the role? | The operating path cannot be reconstructed. |
| Review | Who inspected the output, with what competence, time, and authority? | Human presence becomes ceremonial. |
| Approval/release | Who decided that the output could affect a person, customer, record, or institution? | Release is attributed to "the system." |
| Vendor role | What did the vendor provide, represent, change, or control? | Local diligence disappears behind a contract. |
| Specialist accountability | Which legal, privacy, security, safety, compliance, or domain function had a defined role? | Specialist review is assumed rather than assigned. |
| Institutional responsibility | Which company or public body designed policy, incentives, staffing, and controls? | Individual blame hides system design. |
| Affected party | Who experienced error, delay, disclosure, loss, or reduced opportunity? | Remedy is designed without the person affected. |
| Evidence | What inputs, versions, logs, approvals, overrides, and communications survive? | Root cause becomes speculation. |
| Remedy | Who corrects, notifies, restores, and prevents recurrence? | The incident ends with an apology instead of redesign. |

Keep three questions apart. **Managerial accountability** asks who must act. **Institutional responsibility** asks what the organization designed, enabled, rewarded or failed to control. **Legal liability** asks what applicable law, contract and facts assign. "They are not interchangeable."

## Reviewer, vendor and language checks
- **Human crumple zone.** Ask these questions before blaming a reviewer or assigning one. Can the reviewer see the inputs, evidence, uncertainty and version? Do they have time in proportion to volume and consequence? Can they reject, pause, redirect or escalate? Are they trained for the domain and the type of failure? Is good-faith escalation protected? Is there a separate owner with resources to correct the system and the workflow? If not, "reduce authority, narrow the role, redesign the process, or stop."
- **Vendor.** Record the vendor's identity, the product or service version, the representations relied on, contractual commitments, change notices, incident support, data processing, access and the evidence supplied. Keep that separate from the company's own decisions to deploy, configure, grant access, staff review and release. "'Vendor error' may be relevant. It is not a complete incident analysis."
- **Say** "managerial accountability" for the operating response, "institutional responsibility" for policy, staffing, incentives and control design, and "legal liability requires jurisdiction-specific analysis" for legal questions. **Do not say** that the named manager bears all legal liability, that the vendor is always responsible, that the AI is responsible in the human sense, or that compliance follows from keeping a human in the loop.

## Responsibility and incident map
| Map block | Required entry |
|---|---|
| Incident and affected outcome | What happened, when, to whom, and in what workflow? |
| Authorize | Who approved the role, objective, data, authority, and deployment? |
| Supervise | Who monitored operation, change, review capacity, and exceptions? |
| Inspect | Who reviewed the output, using what evidence and standard? |
| Release | Who approved or released the consequential result? |
| Explain | What can be reconstructed; what is missing or uncertain? |
| Remediate | Who stabilizes, corrects, notifies, redesigns, and decides? |
| Vendor role | What was supplied, represented, changed, contracted, or supported? |
| Specialist review | Which legal, privacy, security, safety, compliance, labor, or domain review applies? |
| Affected parties | Who needs correction, communication, remedy, consultation, or voice? |
| Root causes | Which role, data, model, tool, reviewer, workflow, vendor, policy, or institutional conditions contributed? |
| Decision | Go, revise, pause, demote, retrain, retire; why and with what evidence? |

## Steps
1. If the incident is live, give the first-hour actions and ask who the incident owner is. Keep it to a few lines. Everything else can wait.
2. Fill the map from what the user gave. Write `Missing:` plus the question that would settle each gap. Before launch, fill the map forward by naming who *would* hold each block.
3. Walk the chain one link at a time. Name the person or function, say what they could actually do, and record the gap.
4. Run the crumple-zone check on every reviewer and on anyone being blamed.
5. Sort root causes into the nine categories and mark each as confirmed or possible. Apply the vendor rule.
6. List the specialist reviews the facts trigger. Never state who is legally liable, and never decide a notification duty.
7. Recommend one decision (go, revise, pause, demote, retrain or retire), with its owner, evidence and date.

## Output format
1. **Stabilize now**: live incidents only, and always first. The first-hour actions in five lines or fewer, plus the incident owner or `Missing`.
2. **Responsibility and incident map** as a two-column table (Map block | Entry), with all 12 blocks in order.
3. **Chain check**: one line per link, giving the holder, whether they could act, had a concern, or could not act, and the reason.
4. **Root causes** by category, each marked confirmed or possible.
5. **Specialist reviews triggered**: which reviews apply, not what they will conclude.
6. **Decision**, with its owner, evidence and next review date.
7. Status line: *Author-created managerial synthesis. Not legal advice, a universal liability rule, or a formula that decides how a court, regulator, contract, or employment regime will assign responsibility.*
8. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 11.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
