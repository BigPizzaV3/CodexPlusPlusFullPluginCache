---
name: human-ai-org-chart
description: Draw a Human + AI Organization Chart and a Role Redesign Canvas showing who directs, reviews, can stop and can retire each AI role, and what changes for the people around it. Use when restructuring a team or org chart around AI agents, or when asking what happens to people's jobs.
---

# Human + AI Organization Chart

Chapter 13 makes a structural point: "If the organization chart remains unchanged, the work has not remained unchanged." The first E-mployee changes a job, and the second change is to the organization around that job. This workflow maps where ownership, review, data, voice, escalation and retirement authority sit, and what happens to the human work around each role. The E-mployee is a bounded operating role performed by technology under human direction. It is "not a legal person". Never draw it as a person, an employee, a manager or a box with reports.

## When to use
- "How do we restructure the team, or the org chart, around AI agents?"
- "What happens to people's jobs?" This means mapping the human roles before and after.
- Checking that review capacity, worker voice and stop authority are real before a role is added.
- Do not use this to write the E-mployee's own job specification. Use `role-charter` for that. To govern many roles across the organization, use `portfolio-review`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. Which E-mployee roles are involved, what bounded work does each do, and who owns the business outcome?
2. Who does this work today, who would review the output, and who owns the data and tools?
3. How are workers and affected people heard today, and who could pause or retire the role?

If the user cannot answer, draw the chart anyway and mark the gaps `Missing`. Do not stall.

## The right question
Do not ask "Where does the AI report?" That question "imports personhood and confuses execution with authority." Ask: **"Who directs this role, who reviews its work, who can intervene, who owns the data, who supports the tools, who hears affected people, and who can stop or retire it?"**

## The eight chart nodes
| Chart node | What it makes visible | What it must not imply |
|---|---|---|
| Human decision owner | The person accountable for the business outcome and final decision | That the person automatically carries every legal liability |
| E-mployee role or roles | The bounded objective, workflow, outputs, and exclusions | That software is a person, employee, manager, or independent actor |
| Reviewer or quality function | Competence, time, context, rejection power, and review route | That a named reviewer guarantees safety or correctness |
| Risk/legal/security | Specialist questions, controls, and escalation; privacy and domain review where applicable | That one specialist function replaces local legal or domain analysis |
| Data owner | Source permission, quality, retention, access, and provenance | That data approval authorizes every possible use |
| Worker voice | A route for workers and affected people to report burden, harm, bias, or design failure | That consultation is a formality or universal legal procedure |
| Escalation route | Where uncertainty, exceptions, incidents, and rights concerns go | That escalation can be left to an unowned mailbox |
| Retirement authority | Who can pause, narrow, roll back, prohibit, or retire the role | That continuation is the default after launch |

"A box without a decision is decoration. A line without a handoff is ambiguity. A reviewer without capacity is an aspiration. A retirement authority without a stop path is a title without power."

## Draw decisions, not software
Draw three things as separate elements: the person who can make the decision, the role that performs the bounded work, and the function that can challenge the result. Read the chart as a control and interface map, not a reporting hierarchy. "Shared services must not silently become business owners."

| Shared service may standardize | Business owner must still decide |
|---|---|
| Identity, access patterns, environment controls, logging, and retention mechanisms | Whether the role's objective is worth pursuing |
| Connector patterns, version records, evidence preservation, and change notification | Whether the output meets the business definition of done |
| Training, playbooks, evaluation methods, and incident intake | Whether a specific exception should be released |
| Common procurement, vendor review, and security baselines | Whether the role's human and customer effects are acceptable |
| Portfolio inventory and board reporting format | Whether to continue, narrow, pause, or retire the role |

## Span of control is a workload question
"There is no responsible universal ratio." Pair the chart with a review-capacity view recording role count, expected volume, exception rate, average review time, peak demand, queue age, required expertise, backup coverage, and the reviewer's power to reject or stop. Run the two executive tests:
- **Remove the most experienced reviewer for a week.** Is there a competent backup? Does the queue stay safe? Can the role be narrowed or paused?
- **Double the exception volume without changing staffing.** If quality falls or review becomes ceremonial, the span has been exceeded.

Look at how the load is distributed. When a small group absorbs the exceptions, corrections, emotional labor and after-hours escalation, that cost belongs on the chart.

## Role Redesign Canvas (10 fields, exact)
The Canvas is "not a second Role Charter". The Charter defines the E-mployee role. The Canvas maps the human role around it, before and after the E-mployee is introduced.

| Canvas field | Executive question |
|---|---|
| Before-state human work | What do people do today, including judgment, coordination, correction, and relationship work? |
| E-mployee contribution | Which bounded tasks move to the E-mployee, and which remain outside it? |
| Retained human judgment | Which decisions still require human interpretation, discretion, empathy, negotiation, or accountability? |
| New human work | What review, exception handling, source checking, escalation, training, or maintenance is created? |
| Removed or reduced work | Which tasks genuinely stop, and which merely move or become less visible? |
| Review load | Who checks the output, how often, with what evidence, and with what power to reject? |
| Skill formation | What knowledge, practice, training, and career path does the redesigned work require? |
| Job-quality effect | What happens to discretion, workload, pace, monitoring, learning, dignity, pay, and meaningfulness? |
| Worker and affected-party voice | Who can report harm, bias, unsafe pressure, confusing output, or a bad workflow? |
| Escalation and retirement | Who can change the design, pause the role, or return work to a human process? |

Name the **new human work**. Work that goes unnamed is "either staffed, degraded, or transferred to someone with less power."

## Skills, job quality and worker voice
- **Skill formation.** Will reviewers be trained to challenge outputs? Will people be rewarded for finding errors rather than approving volume? Will someone whose routine tasks shrink get a credible path to new work? Can people report that a workflow is unsafe or degrading without being treated as resistant to innovation?
- **Job quality is a design variable.** Does the redesign increase discretion or only monitoring? Does it build learning or deskill the role? Is the pace set by customer need or by machine capacity? Who absorbs errors? Can affected people get an explanation or remedy through a human route? Is released capacity improving the work, or hiding a reduction in staffing?
- **Worker voice is a control.** The channel "needs an owner, response time, evidence, and escalation. Otherwise it is a suggestion box attached to a machine."
- **Resist two stories:** that every E-mployee is "a hidden layoff program", and that every E-mployee "will elevate human work". Both are "forecasts pretending to be operating plans." "Non-adoption is a valid organizational outcome."

## Regional capability (where relevant)
When language, local practice or uneven infrastructure matter, for example in a MENA setting, add these as questions on the chart and never as claims about any country. Who can review Arabic, English or domain-specific language? Who understands local customer practice? Who can challenge an output that is technically fluent but socially wrong? Who can maintain the system when the vendor changes? Who has authority to stop a workflow when the formal owner is unavailable? Separate observed labor-market signals from assumptions about organizational readiness. "The region should not be treated as a single market, and local constraints should not be used as an excuse to omit controls."

## The executive decision: seven questions
1. Who owns the outcome, and what decision can that person actually make?
2. What bounded work does the E-mployee perform, and what remains human?
3. Who reviews the output, with what competence, time, context, and power to reject?
4. Which shared services are truly common, and which decisions must stay with the business owner?
5. Who owns the data, the evidence, the worker effect, the escalation, and the retirement decision?
6. What new human work has been created, and where is it staffed?
7. What would cause the organization to redesign, narrow, pause, or refuse the role?

If the answers "cannot be drawn, the role is not yet an organizational capability. It is a tool looking for a home."

## Steps
1. Describe each E-mployee role in one line: its bounded work, outputs and exclusions. Give no person-like title, no reporting line and no direct reports.
2. Assign every node for every role to a named person or function, with the decision or control it owns. Write `Missing` for any unheld node. Treat one person holding conflicting nodes, such as technical owner and business decision owner at once, as a finding.
3. Split what shared services standardize from what the business owner must still decide.
4. Build the review-capacity view and run both stress tests.
5. Fill the Role Redesign Canvas for each affected human role. Name the new human work and where it is staffed.
6. Check skills, job quality and worker voice. Add the regional questions if they apply.
7. Answer the seven questions and give a verdict: add the role as drawn, redesign, narrow, pause or refuse.

## Output format
1. **Org chart** as a table (Node | Assigned to | Decision or control owned), with one block per E-mployee role. An optional text diagram may show each E-mployee role attached to its human decision owner as a bounded role, never as a report.
2. **Shared service vs business owner** split.
3. **Review-capacity view** and the results of both stress tests.
4. **Role Redesign Canvas** as a two-column table (Canvas field | Entry) for each affected human role.
5. **Findings**: single points of failure, unheld nodes, unstaffed new human work and worker-voice gaps.
6. **Executive decision**: the seven questions, each marked pass, concern or fail, then the verdict and next step.
7. Status line: *Author-created organization-design instrument. Not an established management standard, a legal organization chart, a labor classification, or a forecast of employment outcomes. The E-mployee is not a legal person.*
8. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 13.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
