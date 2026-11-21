---
name: e-mployer-capability-audit
description: Audit whether a team or organization can direct AI work, using the five capacities of the E-mployee Doctrine from The E-mployee Operating Model, and list the missing work. Use when someone asks if they are ready to manage AI agents, or before announcing an AI operating model or agent rollout.
---

# E-mployer Capability Audit

The E-mployer is "the human person who directs E-mployees" (Chapter 4). The E-mployee Doctrine names the five capacities that practice requires: **Delegation, Direction, Discernment, Accountability, and Orchestration**. The audit asks one question per capacity and exposes the missing work. "An organization can be technologically ready and managerially unready." "The five capacities are not a score that creates permission. They are a way to find the missing work before the system receives consequence."

## When to use
- The user is about to launch, scale or announce an agent rollout or AI operating model.
- The user asks "are we ready to manage AI agents?" or "do we have the capability to direct this?"
- The user proposes a list of leadership capacities for AI and wants it checked.
- Do not use this to classify a single system. Use `e-mployee-inclusion-test` for that. To design the outcome itself, use `outcome-first-design`. To place owners, reviewers and stop authority on a chart, use `human-ai-org-chart`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. Which role or program is in scope, and what outcome it serves.
2. Who sets the objective, who reviews the output, and who can pause or retire the role.
3. How the output connects to human decisions, other systems and the people it affects.

If the user cannot answer, audit anyway and mark the gaps `Missing`. Do not stall.

## The E-mployee Doctrine (exact, in this order)
These are five **capacities**. Never add, rename, merge or reorder them. "The sequence matters."

| Capacity | Exact approved meaning | Executive behavior | Primary failure mode |
|---|---|---|---|
| **Delegation** | See the shape of work and decompose an objective into tasks. | Assign the right task to the right actor according to variance, stakes, reversibility, and capability. | Automating high-judgment work while humans retain routine work. |
| **Direction** | Specify purpose, context, constraints, evidence, and the standard of done. | Write the objective before choosing the tool. | Fluent but unusable output from ambiguous direction. |
| **Discernment** | Judge whether output is accurate, appropriate, and fit for consequence. | Match review to risk and use domain expertise. | Automation bias, ceremonial approval, or review without competence. |
| **Accountability** | Own the result and bear consequence. | Name a human who can explain, correct, and remediate. | Accountability theatre or an unqualified rubber stamp. |
| **Orchestration** | Compose outputs into one coherent end. | Coordinate roles, dependencies, handoffs, and quality gates. | Agent sprawl, context loss, and coordination cost. |

## Capability audit questions
| Capacity | Audit question | Evidence that answers it |
|---|---|---|
| Delegation | Can the team show which tasks are stable, variable, reversible, sensitive, or judgment-heavy? | The objective written as a bundle of tasks, each marked agent may perform, human must perform, joint work, or "cannot be delegated under the current evidence". Hidden human work (gathering, verifying, correcting, exceptions, explaining, maintaining) is counted. |
| Direction | Can the role state purpose, context, constraints, evidence, and standard of done? | All five written down, including what the system must not do, infer, disclose or change. "A prompt is not the whole direction." |
| Discernment | Who reviews the output, with what competence, time, and authority? | Independent grounds for review: sampling, source comparison, exception tests or specialist input. A reviewer who can say "This output is not ready," and explain why. |
| Accountability | Who can explain, correct, remediate, pause, or retire the role? | The organization can say who authorized the role, who supervised it, who inspected the output, who released the consequence, who explains it, and who remediates the harm. That person has real power to act. |
| Orchestration | How do the output, human decision, system update, and customer communication connect? | One owner of the coherent end. Handoffs and quality gates mapped. "The smallest set of human and artificial contributions" that can do the job, which is sometimes no agent at all. |

## Practical-obligation mapping
Description, Discipline, Development and Duty of Care are **not additional capacities** and must not be added to the canonical formulation. If the user lists them as capacities, say so and map them:

| Practical obligation language | Where it belongs in the approved Doctrine | Executive question |
|---|---|---|
| Direction | Direction | Have we specified purpose, context, constraints, evidence, and the standard of done? |
| Delegation | Delegation | Have we decomposed the objective and assigned each task according to variance, stakes, reversibility, and capability? |
| Description | Direction, supported by Delegation | Can we describe the objective, task, boundary, output, and handoff without relying on the tool's brand? |
| Discipline | Discernment and Accountability | Do we inspect the work against evidence, refuse weak output, and own the consequence? |
| Development | Orchestration and Direction | Are we improving the role, the human capability, the workflow, and the handoffs rather than merely adding features? |
| Duty of Care | Accountability and Discernment | Have we considered affected people, rights, safety, privacy, workload, and the ability to intervene? |

"This mapping is a clarification, not a revised Doctrine."

## Steps
1. Fix the scope: one role or program and the outcome it serves. Audit the arrangement, not a person. "The Doctrine is not a personality test for CEOs," and the E-mployer "is not a hero". The capacities must exist somewhere in the organization and connect to decision rights.
2. Take the five capacities in Doctrine order. Ask the audit question, record the evidence and its label, and write the finding: evidence present, gap, or `Missing`.
3. For each gap, check whether the capacity's primary failure mode is already visible, and name it.
4. If the user's own framework adds capacities, apply the practical-obligation mapping.
5. Check resources. "An organization cannot demand E-mployer behavior without providing access to training, tools, time, evidence, and authority." Flag any place where a person holds accountability without control, because that transfers risk rather than creating direction.
6. List the missing work with an owner for each. In the book's illustrative audit it was: decompose the work, write the objective and exclusions, staff the reviewer, assign stop authority, and map the handoffs.
7. Give the verdict in the book's terms: either the program can be presented as an E-mployer-ready operating model, or it is technologically ready but managerially unready and must not be announced as E-mployer-ready until the missing work is done. Never turn the capacities into a score, percentage or pass mark.

## Output format
1. **Scope**: the role or program and the outcome it serves.
2. **Capability audit**: a table (Capacity | Audit question | Evidence and label | Finding | Failure mode visible), five rows in Doctrine order.
3. **Mapping note**, only if the user listed extra capacities: where each belongs.
4. **Missing work**: a numbered list, each item with an owner or `Missing`.
5. **Resource check**: whether the named people have training, tools, time, evidence and authority.
6. **Verdict**: E-mployer-ready, or managerially unready, and what must be true before announcing.
7. Status line: *The E-mployee Doctrine is Dr. Jonah Tebaa's proprietary conceptual framework and research agenda. It is not established academic science, a legal standard, a certification, or a vendor methodology, and it is not empirically validated. The five capacities are not a score that creates permission.*
8. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 4.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
