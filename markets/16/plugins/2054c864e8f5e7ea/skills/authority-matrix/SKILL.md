---
name: authority-matrix
description: Draft or review an Authority Matrix that sets which of seven action powers an AI role holds, with thresholds, review, escalation, expiry and revocation, from The E-mployee Operating Model. Use when someone asks what an AI agent should be allowed to do, or whether it may send, spend, approve or act on its own.
---

# E-mployee Authority Matrix

The Authority Matrix makes an E-mployee's right to act "explicit, narrow, logged, time-bounded, and revocable" (Chapter 10). It starts from a layer separation: "Capability is not permission. Permission is not authority. Authority is not accountability. A reviewer's presence is not intervention capacity. A credential is not a decision right." The governing question: "What may this E-mployee do, with which data and tools, under whose review, for how long, and with what revocation path?" Trust is defined as "calibrated permission plus intervention capacity," and it "should narrow as consequence and irreversibility rise." Default posture: if an answer is unclear, keep authority lower.

## When to use
- The user asks what an AI agent should be allowed to do, or who approves what.
- A proposal lets an agent send messages, spend, approve, or write to records or systems.
- An existing grant is up for renewal, or something changed (model, source, audience, integration).
- Do not use this to judge whether performance justifies a different control arrangement. Use `autonomy-review` for that. For who answers when an action goes wrong, use `ai-incident-response`. For the role's risk tier and minimum controls, use `risk-classification`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. The role's outcome and recipient (or its Role Charter).
2. The data, systems and tools it would touch, and what the connector or platform technically exposes.
3. The reviewer and approvers, the performance evidence so far, and who can stop the role.

If the user cannot answer, draft anyway and mark the gaps `Missing`. Do not stall.

## Four questions, not one
| Question | Meaning | Failure when confused |
|---|---|---|
| Capability | Can the system perform the task under observed conditions? | A demo becomes a permission. |
| Reliability | Does it perform consistently enough for the proposed control arrangement? | One success becomes general confidence. |
| Permission | May the role use this data, system, or tool for this purpose? | Technical access is mistaken for legitimate use. |
| Authority | Has the organization granted the right to take this action? | A credential is mistaken for a decision right. |

Authority follows the outcome, not the platform's menu of functions. A useful refusal: "The system can do that, but the role does not need to."

## The seven action powers (exact, in this order)
| Action power | Meaning | Default control |
|---|---|---|
| Observe | Read approved data or status. | Least privilege, provenance, and logging. |
| Draft | Prepare content or a proposed action. | Human review before external or consequential use. |
| Recommend | Rank or propose a decision. | Decision owner reviews evidence and uncertainty. |
| Execute | Take a bounded reversible action. | Narrow scope, testing, logging, and rollback. |
| Approve | Commit an organizational decision. | Reserved for an authorized human or institution unless applicable law or policy says otherwise. |
| Spend | Commit money or resources. | Explicit limits, dual control, and transaction monitoring. |
| Communicate | Send external or internal messages as the organization. | Named approver, audience limits, and record retention. |

"These powers are not a ladder that every role should climb. They are distinct rights." Each Matrix entry records: task class, action power, review level, expiry date, escalation path, affected rights or data, stop authority, and the human or institutional authority that approved it. "'The system has access' is not an entry."

## Thresholds (seven dimensions)
"A right to act without a threshold is a blank cheque." "'Low risk' is not a threshold."

| Threshold dimension | Question |
|---|---|
| Object | What record, message, transaction, decision, or commitment is affected? |
| Action | May the role observe, draft, recommend, execute, approve, spend, or communicate? |
| Limit | What amount, volume, audience, geography, duration, or data class is allowed? |
| Review | Is review before action, exception review, sample audit, or human decision? |
| Exception | What condition requires escalation or blocks action? |
| Expiry | When must the permission end or be renewed? |
| Reversal | How is the action paused, undone, or returned to a human path? |

**Data authority is not tool authority.** Data scope: fields, sources, purpose, freshness, sensitivity, retention, owner. Tool scope: functions, environments, APIs, write access, external effects, credentials. "If the answer is 'the connector already exposes it,' the design has not begun."

## Segregation of duties
| Action sequence | Safer separation |
|---|---|
| Observe → classify | E-mployee observes approved fields; reviewer checks the classification and evidence. |
| Draft → release | E-mployee drafts; named human approves before external or consequential use. |
| Recommend → approve | E-mployee recommends; authorized decision owner decides. |
| Prepare → spend | E-mployee prepares a transaction; authorized humans approve and release under dual control. |
| Request → grant | Operating owner requests; separate security or data owner grants and can revoke. |
| Execute → reconcile | E-mployee performs bounded action; separate control or owner checks the resulting state. |

## Escalation, expiry and revocation
- **Escalation.** Use named triggers: missing data, conflicting sources, policy ambiguity, unusual value, a new segment or jurisdiction, an out-of-scope attempt, a privacy or security signal, a material complaint, a failed control, a model or vendor change. Name the recipient and expected response. Log the trigger, time, last permitted action, recipient, decision, and whether the role resumed, narrowed, paused or stopped.
- **Safe default.** When no reviewer responds: hold, revert, or route to a human process. Never "silent execution merely because a service-level clock has expired."
- **Expiry.** Every grant has an expiry or review date: time-, event-, version- or condition-based.
- **Revocation.** Name the owner, the mechanism and the time expectation. Can the trigger be disabled without waiting for the vendor? Are credentials revoked, queued actions identified, pending work returned to a human path? "A stop button that only the vendor can operate is not sufficient." Any material change returns the role to a constrained permission until reviewed.

## Steps
1. State the outcome. For each of the seven powers, ask whether the outcome requires it.
2. Answer the four questions separately for every power requested.
3. Write a threshold for each granted power across all seven dimensions. Separate the data scope from the tool scope.
4. Check segregation of duties. The more consequential the action, the less acceptable it is for one role to generate the evidence, decide, release and certify itself.
5. Set escalation triggers, the safe default, expiry and the revocation path.
6. Plan the intervention test: run a controlled action, observe the alert, identify the reviewer, measure the response time, and verify the reviewer can stop or reverse it. Say so if it depends on a vendor or on a manual fallback with no staff. "The right to act is inseparable from the right to stop."
7. Plan the revocation test, before activation: trigger the stop condition in a controlled environment and confirm that queued actions are visible, pending messages held, credentials disabled, and a human can resume the work. A failed test "is evidence that the proposed authority is larger than the control system can safely carry."
8. Run the authority review conversation:
   1. What exact outcome requires this power? If the role can meet its objective without it, do not grant it.
   2. What is the narrowest object and data scope? Reduce fields, records, systems, audiences, geography and duration.
   3. What evidence supports the permission? Use performance evidence, not a demo or confidence score alone.
   4. What review occurs and who can reject? Name a competent reviewer with time and authority.
   5. What happens at the threshold or exception? Define escalation and the safe default.
   6. How is the action logged, expired, and revoked? Make the control executable, not aspirational.
   7. How does the human process resume? Test rollback before the action is needed.

   If the answer is unclear, the authority should remain at a lower level: the role may observe, draft or recommend while the organization improves its data, review, process or evidence.

## Output format
1. **Authority Matrix** as a table: Task class | Action power | Review level | Expiry date | Escalation path | Affected rights or data | Stop authority | Approved by. List all seven powers; write "Not granted" where a power is withheld.
2. **Thresholds**: one seven-row table (Object to Reversal) for each granted power.
3. **Data scope and tool scope**, listed separately.
4. **Segregation check**: each consequential sequence and who holds the second step.
5. **Escalation, safe default, expiry and revocation**, with the intervention and revocation tests marked planned, passed or failed.
6. **Authority review**: the seven questions, each answered or marked `Missing`.
7. **Verdict per power**: grant at the stated threshold, keep lower (observe, draft or recommend) until named evidence exists, or do not grant. Close with a one-line answer to "what right to act has actually been granted?"
8. Status line: *Author-created authorization instrument. Managerial guidance, not legal advice. Not a universal authorization standard, legal opinion, regulatory classification, or guarantee.*
9. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 10.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
