---
name: outcome-first-design
description: Design an AI use outcome-first with The E-mployee Operating Model and produce a one-page outcome brief, or decide whether a technology-first AI pilot should be deferred. Use when someone says "we want to use AI for X", asks "should we run this AI pilot?", or has picked a tool and needs to define the work.
---

# Outcome-First Design

Chapter 5 starts with the result, not the tool. The book's order of operations is: **"Outcome → workflow → task bundle → dependencies → authority boundary → acceptance condition → tool choice."** It is the practical form of Direction and Delegation, and it produces a one-page outcome brief before any Role Charter exists. "An outcome without an acceptance condition is an aspiration." The same chapter gives the conditions for deferring a technology-first pilot.

## When to use
- The user wants to "use AI for" a function, team or goal and needs it turned into designed work.
- The user has chosen a tool or vendor and is looking for something for it to do.
- The user is deciding whether to approve, run or extend an AI pilot or demo.
- Do not use this to write the standing role's full specification. When the brief is solid, hand off to `role-charter`. To choose between several candidate outcomes, use `first-role-selection`. To audit a rollout that already exists, use `ai-access-audit`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. The result wanted, who receives it, and what they will decide or do with it.
2. What happens today: delay, quality, risk and human effort.
3. The tool or pilot proposed, if any, and the data and systems it would touch.

If the user cannot answer, draft anyway and mark the gaps `Missing`. Do not stall. If the request starts with a tool, record it under "Tool question" and start from the outcome.

## Outcome questions
Write the outcome so "a skeptical colleague can challenge" it.

| Outcome question | What the answer must make visible |
|---|---|
| What result is needed? | The change the organization wants, not the tool it wants to deploy. |
| For whom? | The customer, worker, leader, citizen, team, or decision recipient affected by the result. |
| By when? | The timing that makes the result useful rather than merely complete. |
| Against what baseline? | The current process, quality, delay, cost, risk, or human effort that gives the outcome meaning. |
| What happens if it fails? | The operational, financial, relational, rights, safety, or reputational consequence. |
| What must remain human? | Judgment, approval, relationship, exception handling, or accountability that the role must not absorb. |
| What would make it not worth doing? | The cost, risk, review burden, or weak evidence that should cause a pause or rejection. |

**Acceptance condition.** Answer five questions: Is the output complete enough for its recipient? Is the evidence traceable? Is the quality threshold appropriate to the consequence? Is uncertainty visible? Can a human use the result within the required time? Then write the negative space: the result must not conceal missing evidence, expose restricted data, turn an inference into a fact, or make a decision reserved for a human. "'Looks useful' is not an acceptance condition. Nor is 'the model was confident.'"

## Workflow map
Map the ordinary path and the exception path. This is "the pre-charter map that reveals whether a Role Charter can be written."

| Stage | Work performed | Actor | Input or dependency | Decision/hand-off | Failure exposure |
|---|---|---|---|---|---|
| 1 | Gather approved information | Human, system, or agent | Source list, permission, freshness | Is the evidence admissible? | Missing, stale, or restricted data |
| 2 | Transform or classify | Human, system, or agent | Defined rules and context | Is the transformation fit for purpose? | Omission, distortion, or false certainty |
| 3 | Prepare output | Human, system, or agent | Format and standard of done | Does the output answer the decision? | Fluent but irrelevant result |
| 4 | Review and resolve exceptions | Named human or specialist | Time, competence, escalation | Release, revise, or stop | Ceremonial approval or overload |
| 5 | Use the result | Decision owner or recipient | Output plus uncertainty | What action follows? | Wrong decision or untraceable use |
| 6 | Learn and change | Role owner and team | Logs, feedback, incidents | Reapprove, narrow, or retire | Silent drift |

**Direction asks:** What is the purpose? What context does the role need? What constraints are non-negotiable? What evidence is allowed? What does done mean? **Delegation asks:** What tasks compose the objective? Which are stable or variable? Which are reversible? Which require judgment, relationship or specialist authority? Which actor suits each task "under the current evidence"? Without both, the design falls into **tool-first design** or **outcome fantasy**.

## Dependency register
| Dependency | Question for the outcome-first design |
|---|---|
| Data | Who owns the information, and is the intended use permitted, relevant, current, and sufficiently complete? |
| People | Who supplies context, reviews exceptions, resolves ambiguity, and maintains the workflow? |
| Systems | Which upstream or downstream systems must work, and what happens when one changes? |
| Policy | Which internal rules, contracts, sector requirements, or external duties shape the work? |
| Language and access | Can affected people and reviewers understand the material and use the system effectively? |
| Vendor | What changes if the provider changes the model, terms, interface, pricing, location, or retention behavior? |
| Reversibility | Can the process pause, roll back, or return to a human path without losing control? |
| Distribution | Who gains capacity, who bears review or monitoring, and who may be excluded? |

"A dependency is not automatically a reason to stop. It is a reason to design a condition." For example, fail closed or escalate when data freshness cannot be established, limit volume when the reviewer is scarce, and add a revalidation trigger when a vendor feature may change.

## One-page outcome brief (design canvas, 10 blocks)
| Design block | Required decision |
|---|---|
| Outcome | What result should change? |
| Recipient and decision | Who will use it, and what will they decide or do? |
| Timing | When must the result be available? |
| Baseline | What currently happens, including delay, quality, risk, and human effort? |
| Workflow | What stages, tasks, handoffs, and exceptions produce the result? |
| Actor allocation | What belongs to a human, an agent, or a joint process? |
| Dependencies | What data, systems, people, policies, or vendors can affect the result? |
| Acceptance | What evidence and quality condition make the result usable? |
| Exclusions | What may not be inferred, accessed, decided, disclosed, or executed? |
| Tool question | What capability is needed after the role is clear? |

## Defer a technology-first pilot when any of these is true
| Defer condition | Why it matters |
|---|---|
| No named recipient or decision | The output cannot be judged against a consequence. |
| No measurable or discussable acceptance condition | The team will confuse activity or fluency with completion. |
| Workflow is not mapped | Hidden human work, dependencies, and exceptions remain unowned. |
| Data permission is assumed from technical access | The role may exceed lawful, contractual, or ethical boundaries. |
| Review is described as "someone will check" | Human presence is not the same as meaningful oversight. |
| Authority follows the integration | The system may act because it can, not because the role permits it. |
| No reversible path or stop condition | A weak pilot can compound its own errors. |
| Only the vendor's success story supports the value | Promotional evidence cannot establish a company-specific result. |

Deferral need not be permanent rejection. Offer a narrower alternative: a narrower objective, a smaller data boundary, a draft-only role, a stronger reviewer, a shorter test, or a decision to learn without deploying. Exploration in a sandbox "is allowed to be uncertain". The danger is promoting it into a role without changing the design.

## Steps
1. Write the outcome with the seven outcome questions, then the acceptance condition and its negative space.
2. Map the workflow, including the exception path and the hidden human work.
3. Apply Direction asks and Delegation asks. Allocate each task to a human, an agent or joint work.
4. Fill the dependency register and design a condition for each dependency.
5. Fill the one-page outcome brief. Leave the tool question last.
6. If a pilot is proposed, test the eight defer conditions. If any is true, defer and offer a narrower alternative.
7. Answer the CEO's eight questions: "What outcome matters? Who receives it? What decision or action does it support? What does acceptable work look like? Which tasks and exceptions produce it? Which dependencies can break it? What should remain human or joint? Under what conditions should the company defer the role?" If they are unanswered, "the next meeting should not be a vendor selection meeting. It should be a design meeting."

## Output format
1. **Outcome brief**: a two-column table (Design block | Decision) with all 10 blocks in order.
2. **Acceptance condition**: the five checks and the negative space.
3. **Workflow map**: the six-stage table filled in for this outcome, with the exception path.
4. **Dependency register**: the eight rows, each with the condition designed for it.
5. **Pilot check**, only if a pilot is proposed: each defer condition marked true, false or `Missing`, the decision, and a narrower alternative.
6. **CEO's eight questions**: one line each, answered or `Missing`.
7. **Verdict**: **ready for `role-charter`**, **design meeting needed**, or **defer the pilot**, with the reasons and the next step.
8. Status line: *Author-created design instrument, not an established management standard or a guarantee of value.*
9. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 5.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
