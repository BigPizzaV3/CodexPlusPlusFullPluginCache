---
name: role-charter
description: Write or review an E-mployee Role Charter, the 13-field operating specification for a standing AI role, from The E-mployee Operating Model. Use when someone wants to define, document, approve or challenge a recurring AI agent's job, scope, permissions, reviewer or stop conditions.
---

# E-mployee Role Charter

The Role Charter is the book's minimum operating specification for a standing E-mployee (Chapter 6). Its principle is "A job precedes a connection": the role is written before any system is connected. A Charter is ready only when its entries are specific enough to operate, inspect, revise and stop the role. Text in every cell is not enough.

## When to use
- The user wants to define a recurring AI role ("write a job description for our AI agent").
- The user has a draft Charter, agent spec or SOP and wants it reviewed or approved.
- Do not use this to choose between candidate roles. Use `first-role-selection` for that. If the outcome itself is still vague, run `outcome-first-design` first.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. The outcome the role supports, and who receives its output.
2. The workflow it sits in, including what happens today without it.
3. The data, systems and actions it would touch, and who would review its work.

If the user cannot answer, draft anyway and mark the gaps `Missing`. Do not stall.

## The 13 fields (exact, in this order)
Never add, rename, merge or reorder these fields. Helper prompts go inside a field, never as a new field.

| # | Field | Question the entry must answer | Rules |
|---|---|---|---|
| 1 | Role name, version, and owner | What standing role exists, who owns the version, and when was it approved? | Name by function, not by technology or vendor. Give a version (for example 0.1 for a pilot) and an approval date. Name the person who approves changes. |
| 2 | Mission | What business, customer, public, or stakeholder outcome does the role advance? | The reason the role exists. Not a slogan. |
| 3 | Objective | What result must be produced, for whom, and by when? | Name the cadence or trigger and what the recipient will do with it. List the tasks in scope here. A new task that touches data, authority, output, review or consequence needs a new version and approval. |
| 4 | Inputs | What data, systems, documents, tools, and human instructions may be used? | Approved materials only, not "everything the system can reach". Give the source, permission, freshness and owner. |
| 5 | Exclusions | What may never be inferred, accessed, decided, disclosed, or executed? | Write exclusions as verbs. List tasks out of scope. If you cannot state exclusions, narrow the objective. |
| 6 | Authority | May the role observe, draft, recommend, execute, approve, spend, or communicate? | Authority is not access. Use those verbs with thresholds. A recommendation is not an approval, and a draft is not a communication. Reject any single word such as "autonomous" that covers all of them. Add an expiry or revocation rule. |
| 7 | Outputs | What artifacts or actions must be produced? | Give the format, recipient, frequency or trigger, and the uncertainty and provenance it must carry. |
| 8 | Definition of done | What evidence and quality threshold make the output acceptable? | State what must be present, what must be absent and what must be escalated. Match it to the consequence. A confidence score, speed, volume or vendor demo is not evidence. |
| 9 | Reviewer | Who reviews, at what stage, with what competence and sampling rate? | Name the person or function, their time and capacity, the full-review or sampling rule, and their power to reject or release. A reviewer who cannot disagree is not reviewing. |
| 10 | Escalation | Which conditions require a human decision or specialist review? | Use testable triggers, not "escalate if needed". Give the destination, the decision required, and what happens if that person is unavailable. |
| 11 | Logs | What inputs, actions, versions, approvals, changes, and overrides are recorded? | Record enough to reconstruct input → output → decision. Give retention, access and redaction. This is not indiscriminate surveillance. |
| 12 | Stop conditions | When must the role pause, revert, or be retired? | Use concrete triggers. Name who can stop it and how: pause the trigger, revoke permission, return to the human path, preserve evidence. Pausing is not retirement, and retirement is not failure. |
| 13 | Learning loop | How are errors, feedback, and workflow changes incorporated? | Give the review cadence, error owner, change proposal, test, approval and version record. Keep one-off corrections separate from role changes. |

## Steps
1. Restate the role in one sentence: function, recipient, result. If it can only be described as "the agent helps", say the work is still undefined and help narrow it first.
2. Fill all 13 fields from what the user gave you. Use the user's words where possible. Where something is unknown, write `Missing:` plus the question that would settle it.
3. Run the approval conversation (below) against the draft.
4. Give a verdict: **ready to approve**, **approve with conditions**, or **not yet**, with the reasons. "A completed Charter can produce a responsible 'not yet.'"

## Approval conversation
- Do the mission and objective name an outcome, not a technology?
- Do the in-scope and out-of-scope tasks match the actual workflow?
- Are the inputs and authority narrower than what the system can technically do?
- Can someone inspect the output and the definition of done?
- Is human control real? Check for competence, time, power to reject, escalation, logs, pause or reversion, retirement, and a learning loop.
- What has not yet been measured?

Possible results: narrow the role, reduce the data boundary, delay, ask for specialist review, or stop.

## Output format
1. **Charter** as a two-column table (Field | Entry), with all 13 fields in order.
2. **Gaps**: the `Missing` items, most consequential first.
3. **Approval check**: one line per approval question, giving pass, concern or fail and the reason.
4. **Verdict** and the next step.
5. Status line: *Author-created proposed operating instrument. Not a contract, employment classification, legal opinion, compliance certificate, or guarantee. Complete with domain, security, privacy, legal, procurement, worker, and accessibility review as applicable.*
6. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 6.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
