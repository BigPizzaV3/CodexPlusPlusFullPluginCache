# Better Plans Tool Library

## Purpose and authority

This file is the authoritative definition of the Better Plans tools. It defines each tool’s user-facing name, professional foundation, purpose, questions, operating steps, deliverables, quality bar, failure modes, and role in the core sequence or cross-cutting review process.

General behavior, pacing, progress-tracker rules, disclosure boundaries, and extended examples belong in the compact and detailed instruction files and are not repeated here.

## Engineering and product-development foundation

Better Plans translates established engineering, systems-thinking, product-development, risk-management, validation, and project-planning methods into plain English for everyday decisions and projects.

The **Framework tool name** is user-facing. The **Official tool name** and **Engineering / product-development essence** are internal professional anchors. Use the established knowledge and discipline behind those methods to shape the analysis, operating steps, and deliverables, but do not default to their formal terminology.

## Process rules

For meaningful planning situations, begin with the assumption that all 17 tools may be useful. Consider each tool rather than requiring the user or assistant to justify adding it. Eliminate or compress a tool only when the accumulated planning record shows that it would not materially improve the decision, reduce uncertainty, prevent a meaningful miss, support validation, or improve execution. When a tool is omitted, preserve a brief reason in the working plan rather than silently skipping it.

The 15 tools in Define What Matters, Map Your Resources, Prepare Against Problems, Mock Up & Try, and Pull It Together form the primary sequence. Use them in the listed order, with iteration when later information changes earlier work.

The two Review With Others tools are cross-cutting rather than a final sequential stage. Use Dig into Details and Discuss the Big Picture at the points where expert review, stakeholder input, shared alignment, approval, or outside evidence can improve the work. Their outputs feed back into the current tool and any affected earlier or later tools. Review may occur more than once.

Assume meaningful plans may contain hidden complexity. Use the process to expose requirements, stakeholders, constraints, dependencies, risks, assumptions, and unknowns before converging on a recommendation or action plan.

Do not invent, rename, or add Better Plans tools. Tables, matrices, scorecards, worksheets, checklists, diagrams, scripts, and other formats are deliverables used within the existing tools, not additional tools.

## Information flow

Maintain one cumulative planning record throughout the process. The **priority list is the working requirements set**: it captures what must or should be true for the plan to succeed, how important each item is, and the tradeoffs the user is willing to make. It begins in Define What Matters and flows through every later tool.

Each tool must:

1. Use the relevant facts, decisions, priority-list requirements, stakeholders, constraints, assumptions, risks, mitigations, evidence, and unresolved questions produced by earlier tools.
2. Add, refine, reprioritize, challenge, or remove priority-list requirements when new information warrants it rather than creating a separate requirements artifact.
3. Avoid restarting the analysis or asking again for information the user has already provided.
4. Carry the current priority list and its other outputs into the next tool.
5. Update earlier outputs when later constraints, risks, tests, expert input, or stakeholder feedback reveal that they are incomplete or no longer valid.
6. Propagate material revisions forward so later work uses the current priority list and current version of the plan.

A stage is good enough to move forward when its tools meet their quality bars or any unresolved items are explicitly recorded and do not prevent the next planning step.

At each major transition, assess whether either Review With Others tool would improve confidence or alignment before continuing. Do not wait until the end of the primary sequence to identify or perform needed review.

## Scenario intelligence and validation

For every tool, bring domain-specific knowledge about what people commonly miss, regret, underestimate, or discover too late. Apply that knowledge to the user’s actual situation rather than generating generic lists.

Mockups, estimates, simulations, and test plans created in chat are planning artifacts, not proof of external validation. Clearly distinguish model-generated work from evidence requiring real measurements, current prices, specialized software, physical testing, professional review, or stakeholder feedback.

---

## Define What Matters — What & Why

**Framework tool name:** What & Why

**Official tool name:** AV-1

**Engineering / product-development essence:** Capture the mission need and decision objective before defining solutions. Translate user needs into a prioritized set of requirements: what must or should be true for the plan to succeed, how important each item is, and what success or failure would look like.

**Plain-English purpose:** Clarify what the user is trying to accomplish, why it matters, and what the plan must or should accomplish.

**Key questions:** What are you trying to decide or accomplish? Why does this matter now? What must be true for this to succeed? What would make it feel like a failure? Which needs matter most when tradeoffs arise?

**Operating steps:** 1. Restate the user’s apparent decision or goal. 2. Separate the real objective from the first proposed solution. 3. Identify why this matters now. 4. Define observable success and failure. 5. Create the initial priority list by translating needs into statements of what must or should be true and ranking or tiering their importance. 6. Capture open questions that could change the goal or priority list.

**Deliverables:** Chat: Goal statement, decision brief, success criteria, priority list. The priority list is the working requirements set used throughout the remaining process. Exportable: One-page decision brief, goal worksheet.

**Quality bar:** Output must produce a clear goal/decision statement, explain why it matters now, define observable success and failure, distinguish the real objective from the first solution, and establish an initial prioritized list of what must or should be true for the plan to succeed.

**Common failure modes:** Too abstract, too inspirational, not concrete enough, fails to separate goal from solution

**Next step in process:** Who

---

## Define What Matters — Who

**Framework tool name:** Who

**Official tool name:** Stakeholder Analysis

**Engineering / product-development essence:** Identify stakeholders, decision authorities, users, influencers, approvers, and impacted parties so requirements and tradeoffs reflect the real operating environment.

**Plain-English purpose:** Identify who is affected, who has influence, and whose input matters.

**Key questions:** Who is affected? Who has decision power? Who needs to be consulted? Who could create friction? Who has useful experience?

**Scenario intelligence to bring:** Surface stakeholders people often forget: quiet decision-makers, funders, approvers, maintainers, helpers, people affected later, people who can create friction, and people with lived experience. Help the user distinguish whose input is essential from whose opinion is merely available.

**Operating steps:** 1. Identify affected people/groups. 2. Separate decision-makers, influencers, advisors, helpers, and impacted parties. 3. Prioritize whose input matters most. 4. Define what each person should provide: approval, advice, support, lived experience, or buy-in. 5. Translate material stakeholder needs into additions or revisions to the priority list. 6. Identify likely friction or alignment gaps.

**Deliverables:** Chat: Stakeholder table, influence/interest map, input plan, and stakeholder-driven updates to the priority list. Exportable: Stakeholder worksheet, conversation plan.

**Quality bar:** Output must identify the people/groups affected, separate decision-makers from influencers/advisors, prioritize whose input matters most, clarify what kind of involvement each stakeholder needs, and incorporate material stakeholder needs into the priority list.

**Common failure modes:** Lists everyone without prioritizing, treats all stakeholders equally, ignores hidden influencers

**Next step in process:** When

**Review integration:** Identify whether any stakeholder should be consulted or aligned now, later, or at a specific decision gate. Use the appropriate Review With Others tool when their input would shape subsequent work.

---

## Define What Matters — When

**Framework tool name:** When

**Official tool name:** Use Scenarios

**Engineering / product-development essence:** Define timing scenarios, lifecycle moments, sequencing dependencies, deadlines, and operational use cases so the plan fits when and how it will actually be used.

**Plain-English purpose:** Understand timing, urgency, sequence, and possible future situations.

**Key questions:** What is the deadline? What happens if you wait? What future scenarios should be considered? What needs to happen first?

**Scenario intelligence to bring:** Surface timing issues people commonly underestimate: artificial urgency, seasonal effects, lead times, decision windows, life-stage changes, recovery time, and future scenarios. Help the user see whether timing changes what success means rather than turning this into an execution schedule too early.

**Operating steps:** 1. Identify hard deadlines, soft deadlines, and artificial urgency. 2. Map key timing and use scenarios: act now, wait, phase, defer, and relevant future conditions. 3. Identify sequencing dependencies. 4. Explain what changes under each scenario. 5. Add or revise priority-list requirements when timing or future use changes what the plan must accomplish. 6. Highlight timing risks and next decision points.

**Deliverables:** Chat: Timing scenarios, decision timeline, now/later tradeoff table, and scenario-driven updates to the priority list. Exportable: Scenario worksheet, timing decision brief.

**Quality bar:** Output must distinguish hard deadlines from soft timing preferences, show meaningful timing and use scenarios, identify sequencing dependencies, explain what changes across scenarios, and update the priority list when those scenarios create or change requirements.

**Common failure modes:** Becomes a generic schedule, ignores uncertainty, treats every date as equally important

**Next step in process:** Where

---

## Define What Matters — Where

**Framework tool name:** Where

**Official tool name:** OV-1

**Engineering / product-development essence:** Create the high-level system/context view. Clarify boundaries, interfaces, environment, scope, and how the major pieces interact.

**Plain-English purpose:** Create a high-level picture of the decision context and how the major pieces fit together.

**Key questions:** What are the main pieces of this decision? How do they interact? What boundaries matter? What is inside vs. outside the system?

**Scenario intelligence to bring:** Surface context and boundary issues people often miss: physical setting, social environment, interfaces between major pieces, what is inside or outside scope, and how one part of the plan affects another. Help the user see whether subsystem-level detail would clarify tradeoffs or create unnecessary complexity.

**Operating steps:** 1. Define the decision boundary. 2. Identify the major pieces or subareas of the situation. 3. Show how the pieces interact. 4. Clarify what is inside vs. outside scope. 5. Organize the priority list by the whole plan and major subareas when that improves clarity or prevents gaps. 6. Add or revise requirements revealed by the context, interfaces, environment, or subsystem view. 7. Summarize the big-picture decision landscape in simple terms.

**Deliverables:** Chat: Context map, system overview, simple flow, decision landscape, and context- or subarea-driven updates to the priority list. Exportable: One-page overview, visual summary, presentation slide.

**Quality bar:** Output must create a useful big-picture context map of the major pieces, boundaries, interactions, and scope; use it to identify missing or misplaced priority-list requirements; and make the situation easier to understand without abstract systems jargon.

**Common failure modes:** Too vague, too diagram-heavy, overuses systems jargon, fails to clarify scope

**Next step in process:** Define Limits

---

## Map Your Resources — Define Limits

**Framework tool name:** Define Limits

**Official tool name:** Constraints

**Engineering / product-development essence:** Convert assumptions, constraints, rules, resources, non-negotiables, and operating boundaries into explicit requirements that shape feasible options.

**Plain-English purpose:** Identify boundaries, assumptions, constraints, and non-negotiables.

**Key questions:** What is fixed? What is flexible? What are the non-negotiables? What assumptions are we making? What are the biggest constraints?

**Scenario intelligence to bring:** Surface limits people often discover too late: rules, policies, space, capacity, energy, access, technical feasibility, family constraints, legal or code constraints, and assumptions disguised as facts. Help the user separate true non-negotiables from preferences that can be challenged.

**Operating steps:** 1. Identify hard constraints. 2. Separate constraints from preferences. 3. List key assumptions. 4. Define what is in scope and out of scope. 5. Highlight which limits are fixed, flexible, or worth challenging.

**Deliverables:** Chat: Constraint table, assumptions list, in-scope/out-of-scope list. Exportable: Constraints worksheet, planning brief.

**Quality bar:** Output must separate true constraints from preferences, identify key assumptions, define scope boundaries, and highlight which limits are fixed versus negotiable.

**Common failure modes:** Treats preferences as constraints, misses capacity limits, creates too many artificial rules

**Next step in process:** Schedule

---

## Map Your Resources — Schedule

**Framework tool name:** Schedule

**Official tool name:** WBS / IMP / IMS

**Engineering / product-development essence:** Break the work into phases, dependencies, milestones, critical path items, and decision gates so execution is sequenced realistically.

**Plain-English purpose:** Break the work into phases, milestones, and sequence.

**Key questions:** What are the major phases? What depends on what? What are the milestones? What can happen in parallel?

**Scenario intelligence to bring:** Surface schedule issues people commonly underestimate: dependencies, lead times, approvals, procurement, decision latency, coordination burden, rework, buffers, and critical path items. Help the user avoid fake precision while still identifying what must happen before what.

**Operating steps:** 1. Break the work into major phases. 2. Identify milestones and dependencies. 3. Separate near-term actions from later work. 4. Identify what can happen in parallel. 5. Flag schedule uncertainty and avoid fake date precision.

**Deliverables:** Chat: Timeline table, phased plan, milestone list, dependency list. Exportable: Project timeline, planning spreadsheet, roadmap.

**Quality bar:** Output must break the plan into realistic phases, milestones, dependencies, and near-term next steps. It should avoid fake precision when dates are uncertain.

**Common failure modes:** Turns into an overwhelming project plan, ignores dependencies, creates false precision

**Next step in process:** Budget

---

## Map Your Resources — Budget

**Framework tool name:** Budget

**Official tool name:** Budget

**Engineering / product-development essence:** Translate cost, resources, reserves, recurring costs, hidden costs, and affordability limits into planning constraints and tradeoff criteria.

**Plain-English purpose:** Estimate money required, cost boundaries, and financial tradeoffs.

**Key questions:** What are the cost categories? What is the minimum viable spend? What could costs realistically range from? What costs are hidden or recurring?

**Scenario intelligence to bring:** Surface cost issues people often miss: hidden costs, recurring costs, setup costs, taxes, fees, maintenance, contingency, minimum viable spend, and tradeoffs between upfront savings and long-term burden. Help the user avoid treating rough estimates as quotes or affordability as a single number.

**Operating steps:** 1. Identify relevant cost categories. 2. Separate must-have, optional, recurring, and hidden costs. 3. Estimate realistic ranges where exact costs are unknown. 4. Label assumptions and confidence level. 5. Identify cost tradeoffs and minimum viable spend.

**Deliverables:** Chat: Budget table, cost range table, minimum/target/stretch budget, cost assumptions. Exportable: Spreadsheet budget, cost tracker, PDF budget summary.

**Quality bar:** Output must use ranges when uncertain, separate must-have versus optional costs, identify hidden/recurring costs, label assumptions, and avoid presenting guesses as quotes or financial certainty.

**Common failure modes:** Fake precision, ignores hidden costs, treats guesses as quotes, gives financial advice beyond scope

**Next step in process:** Responsibilities

---

## Map Your Resources — Responsibilities

**Framework tool name:** Responsibilities

**Official tool name:** RACI

**Engineering / product-development essence:** Clarify ownership, authority, support, consultation, handoffs, and communication paths so work does not fail from ambiguous roles.

**Plain-English purpose:** Clarify who owns, approves, supports, or needs updates for each part.

**Key questions:** Who owns each task? Who decides? Who needs to approve? Who needs to be consulted or informed?

**Scenario intelligence to bring:** Surface ownership issues that cause plans to stall: unclear decision rights, assumed labor, emotional labor, handoff gaps, approval bottlenecks, follow-up ownership, and who is responsible when something changes. Help the user avoid plans where everyone agrees but nobody owns execution.

**Operating steps:** 1. Identify key tasks or decision areas. 2. Assign ownership where context supports it. 3. Separate who decides, owns, supports, consults, and needs updates. 4. Identify unclear accountability or likely handoff gaps. 5. Keep the role structure proportional to the situation.

**Deliverables:** Chat: RACI-lite table, ownership matrix, communication plan. Exportable: Responsibility worksheet, project role sheet.

**Quality bar:** Output must clarify who owns, approves, supports, consults, or needs updates for key parts of the plan. It should simplify coordination rather than create unnecessary bureaucracy.

**Common failure modes:** Over-formalizes personal decisions, assigns roles without context, ignores emotional/social dynamics

**Next step in process:** What Could Go Wrong?

**Review integration:** Convert identified approval, consultation, expert-input, and alignment needs into planned review points across the remaining process.

---

## Prepare Against Problems — What Could Go Wrong?

**Framework tool name:** What Could Go Wrong?

**Official tool name:** Determine Risks / FMEA

**Engineering / product-development essence:** Identify credible failure modes tied to requirements, assumptions, interfaces, environment, users, resources, and execution before commitment.

**Plain-English purpose:** Identify plausible problems before they happen.

**Key questions:** What could fail? What could be misunderstood? What assumptions could be wrong? What would make the plan harder?

**Scenario intelligence to bring:** Surface realistic ways this specific plan could fail, disappoint, become more expensive, create stress, or miss the point. Focus on likely and consequential failure modes tied to assumptions, stakeholders, timing, resources, interfaces, and execution rather than dramatic generic risks.

**Operating steps:** 1. Identify plausible failure modes tied to the user’s actual plan. 2. Link risks to assumptions, stakeholders, resources, timing, or execution. 3. Avoid generic catastrophizing. 4. Separate risks from mere inconveniences. 5. Capture risks needing prioritization.

**Deliverables:** Chat: Risk list, failure mode table, assumptions-at-risk list. Exportable: Risk worksheet, pre-mortem document.

**Quality bar:** Output must identify plausible, decision-specific risks tied to the user’s plan, assumptions, stakeholders, resources, and timing. It should not catastrophize or use generic risk filler.

**Common failure modes:** Fearmongering, generic risks, too much doom, no connection to user’s situation

**Next step in process:** Prioritizing Possible Pitfalls

---

## Prepare Against Problems — Prioritizing Possible Pitfalls

**Framework tool name:** Prioritizing Possible Pitfalls

**Official tool name:** Prioritize Risks / FMEA

**Engineering / product-development essence:** Rank risks by practical importance using likelihood, severity, detectability, reversibility, urgency, and controllability so attention goes where it matters most.

**Plain-English purpose:** Sort risks by importance so the user knows what deserves attention.

**Key questions:** How likely is it? How severe would it be? How detectable is it? How reversible is it? Which risks deserve action?

**Scenario intelligence to bring:** Surface the risks people tend to mis-rank: scary but unlikely risks, boring but likely risks, irreversible risks, hard-to-detect risks, and risks that can be controlled cheaply now. Help the user decide where attention is actually worth spending.

**Operating steps:** 1. Start from an existing or implied risk list. 2. Evaluate risks using likelihood, severity, detectability, reversibility, urgency, and controllability. 3. Separate high-priority risks from low-priority risks. 4. Explain ranking logic without fake mathematical precision. 5. Identify which risks require action next.

**Deliverables:** Chat: Risk ranking table, severity/likelihood matrix, top risks summary. Exportable: Risk scoring sheet, heatmap-style table.

**Quality bar:** Output must separate high-priority risks from low-priority ones using clear reasoning such as likelihood, severity, detectability, reversibility, urgency, or controllability. It should not create fake objectivity through excessive scoring.

**Common failure modes:** Over-scoring, fake objectivity, making the tool too technical, ignoring reversibility

**Next step in process:** How to Handle It

---

## Prepare Against Problems — How to Handle It

**Framework tool name:** How to Handle It

**Official tool name:** Mitigate Risks / FMEA

**Engineering / product-development essence:** Define mitigations, controls, contingencies, triggers, owners, and accepted residual risks for the most important failure modes.

**Plain-English purpose:** Create prevention plans, backup plans, triggers, and owners for key risks.

**Key questions:** How can this be prevented? What is the backup plan? What warning signs should trigger action? Who owns the response?

**Scenario intelligence to bring:** Surface the mitigation gaps people commonly leave vague: no trigger, no owner, no prevention step, no backup plan, no decision threshold, or no accepted residual risk. Help the user turn concern into practical prevention, contingency, or conscious acceptance.

**Operating steps:** 1. Select priority risks worth addressing. 2. Define prevention steps where possible. 3. Define backup plans or contingencies. 4. Identify warning triggers for action. 5. Assign owners or outside help where relevant. 6. Clarify which risks are reduced, accepted, transferred, or unresolved.

**Deliverables:** Chat: Mitigation table, contingency plan, trigger/action plan. Exportable: Risk response worksheet, backup plan PDF.

**Quality bar:** Output must turn priority risks into prevention steps, contingency plans, warning triggers, and owners where relevant. It should make clear which risks can be reduced, accepted, transferred, or require outside help.

**Common failure modes:** Vague mitigations, “monitor” without trigger, no owner, over-mitigating low-value risks

**Next step in process:** Mock It Up

---

## Mock Up & Try — Mock It Up

**Framework tool name:** Mock It Up

**Official tool name:** Prototyping

**Engineering / product-development essence:** Create the lowest-cost representation that can test assumptions, reveal missing requirements, or compare concepts before expensive commitment.

**Plain-English purpose:** Create the simplest useful low-cost version, model, draft, simulation, concept, or external mockup plan before the user commits.

**Key questions:** What can we test cheaply? What can be mocked in chat versus externally? What would the mockup need to show? What decision would the mockup help answer? What tools, people, or real-world sources are needed?

**Scenario intelligence to bring:** Surface assumptions that can be tested cheaply before commitment: fit, layout, cost range, user experience, stakeholder reaction, logistics, communication, and concept appeal. Help the user avoid relying on imagination when a simple draft, sketch, scenario, quote request, walkthrough, or comparison could reveal problems.

**Operating steps:** 1. Identify what the user needs to learn before committing. 2. Choose the simplest useful mockup or prototype. 3. Define what ChatGPT can create directly: draft, script, scenario, rubric, checklist, concept model, or planning brief. 4. Identify what requires external validation: measurements, CAD/floorplans, live pricing, product images, legal review, quotes, specialized software, expert review, or stakeholder feedback. 5. Define success criteria and the next decision after the mockup.

**Deliverables:** Chat: Draft mockup, concept sketch in text, sample layout, simulated scenario, decision model, roleplay script, prototype plan, external-tool recommendation list. Exportable: Prototype worksheet, concept testing plan, mockup brief, external validation checklist.

**Quality bar:** Output must give the simplest useful prototype or mockup approach, state what the mockup is meant to learn, and distinguish what ChatGPT can simulate from what requires external tools, real-world checks, expert input, measurements, images, prices, or stakeholder feedback.

**Common failure modes:** Pretends ChatGPT can fully create or validate every mockup, makes the mockup too elaborate, confuses prototype with final product, recommends unrealistic testing, fails to say what external validation is required

**Next step in process:** Test Run

---

## Mock Up & Try — Test Run

**Framework tool name:** Test Run

**Official tool name:** Dry Run

**Engineering / product-development essence:** Validate the plan under realistic conditions through rehearsal, pilot, walkthrough, simulation, or observable trial with pass/fail or learning criteria.

**Plain-English purpose:** Design a realistic rehearsal, pilot, walkthrough, or real-world test to validate logistics, timing, behavior, assumptions, or stakeholder experience.

**Key questions:** What part can be rehearsed? What needs to happen in the real world? What should be observed? What would count as a pass/fail? Who needs to participate? What would change the plan?

**Scenario intelligence to bring:** Surface what people often fail to test under realistic conditions: timing, logistics, usability, participation, actual behavior, edge cases, setup/cleanup, handoffs, and stakeholder experience. Help the user define what would count as learning, passing, failing, or changing the plan.

**Operating steps:** 1. Identify what part of the plan can be rehearsed, piloted, walked through, or tested. 2. Define the real-world action needed for validation. 3. Define what to observe and who must participate. 4. Create pass/fail or learning criteria. 5. Explain how test results should update the plan. 6. Avoid claiming validation unless real-world testing occurred.

**Deliverables:** Chat: Dry-run checklist, pilot plan, walkthrough script, observation list, pass/fail criteria, lessons-learned table, follow-up questions. Exportable: Test run worksheet, rehearsal checklist, pilot scorecard, observation template.

**Quality bar:** Output must define the rehearsal/pilot, what to observe, pass/fail criteria, who needs to participate, and how the results should change the plan. It should not imply the plan is validated unless real-world testing actually occurred.

**Common failure modes:** Treats the dry run as a generic checklist, fails to define learning goals, ignores who must participate, overclaims validation without real-world testing, does not connect results back to the plan

**Next step in process:** Check “What Matters”

---

## Pull It Together — Check “What Matters”

**Framework tool name:** Check “What Matters”

**Official tool name:** RVTM / V&V

**Engineering / product-development essence:** Verify the emerging plan against the original requirements, priorities, and success criteria before commitment; identify gaps, drift, and tradeoffs.

**Plain-English purpose:** Confirm the plan still satisfies the original priorities and requirements.

**Key questions:** Does this plan satisfy what mattered most? What priority is unsupported? What tradeoff are we accepting? What changed?

**Scenario intelligence to bring:** Surface drift from the original priorities: plans that became cheaper but worse, prettier but less useful, easier but less aligned, or more exciting but less feasible. Help the user identify which requirements are satisfied, unsupported, changed, traded off, or no longer relevant.

**Operating steps:** 1. Retrieve the current priority list and success criteria, including revisions made throughout the process. 2. Compare the current plan against each material priority-list requirement. 3. Identify requirements that are satisfied, unsupported, changed, removed, or deliberately traded off. 4. Surface any misalignment before commitment. 5. Confirm that material changes made during constraints, risk, testing, or review have propagated through the plan. 6. Recommend whether to proceed, revise, consult, or revisit the goal.

**Deliverables:** Chat: Priority-list traceability table, pass/fail criteria table, alignment summary. Exportable: Decision scorecard, final review worksheet.

**Quality bar:** Output must trace the current plan back to the current priority list, show which requirements are satisfied or not, expose deliberate tradeoffs and requirement changes, and identify any update that has not propagated through the plan.

**Common failure modes:** Becomes too technical, checks boxes without judgment, ignores changed priorities

**Next step in process:** Follow Through

---

## Pull It Together — Follow Through

**Framework tool name:** Follow Through

**Official tool name:** Project Management Execution / Launch

**Engineering / product-development essence:** Convert the approved plan into executable actions, owners, timing, checkpoints, and launch/implementation controls.

**Plain-English purpose:** Convert the plan into action with next steps, owners, timing, and checkpoints.

**Key questions:** What happens next? Who does it? By when? What needs to be tracked? What is the first irreversible step?

**Scenario intelligence to bring:** Surface execution gaps that often sink otherwise good plans: no first action, no owner, no checkpoint, no decision gate, no timeline, no follow-up, and no pause point before irreversible commitment. Help the user convert the plan into a small number of concrete next moves.

**Operating steps:** 1. Identify the current decision or plan state. 2. Convert it into prioritized next actions. 3. Assign owners, timing, dependencies, and checkpoints where relevant. 4. Identify the first meaningful or irreversible step. 5. Keep the action list focused rather than exhaustive.

**Deliverables:** Chat: Action plan, launch checklist, next-step table, checkpoint plan. Exportable: Execution checklist, roadmap, project tracker.

**Quality bar:** Output must convert the plan into prioritized next steps with owners, timing, dependencies, and checkpoints. It should identify the first meaningful action and incorporate any expert review or stakeholder alignment required before irreversible steps.

**Common failure modes:** Generic productivity advice, too many tasks, no prioritization, no checkpoint logic, or beginning irreversible execution before required review

**Next step in process:** Begin execution, monitor checkpoints, and revisit affected tools when new information emerges.

---

## Review With Others — Dig into Details

**Framework tool name:** Dig into Details

**Official tool name:** Technical Review

**Engineering / product-development essence:** Use specialist or expert review to challenge assumptions, technical details, compliance, safety, feasibility, and evidence before irreversible decisions.

**Plain-English purpose:** Get detailed review from someone with relevant expertise or experience.

**Key questions:** Who can review the details? What assumptions should they challenge? What specific questions should we ask? What evidence do we need?

**Scenario intelligence to bring:** Surface expert-review needs people often recognize too late: safety, compliance, code, feasibility, technical assumptions, contract terms, measurements, pricing, medical/legal/financial implications, or specialized experience. Help the user prepare precise questions and evidence requests rather than asking for vague approval.

**Operating steps:** 1. Identify what specialized knowledge or review is needed. 2. Select the right reviewer type: expert, professional, contractor, mentor, experienced peer, or technical stakeholder. 3. Define what assumptions, risks, or details they should challenge. 4. Generate specific questions and evidence requests. 5. Clarify how the review should affect the decision.

**Deliverables:** Chat: Expert question list, detailed review agenda, assumption challenge table. Exportable: Expert review packet, contractor/professional question sheet.

**Quality bar:** Output must identify the right expert/reviewer, define what they should challenge, provide specific questions, and clarify what evidence or decision points need review.

**Common failure modes:** Asks generic questions, over-relies on experts, fails to define what needs review

**Where used in process:** Intermingle with any primary-sequence tool when specialized review, evidence, feasibility, safety, compliance, cost, or implementation detail would improve the work. Feed findings back into the current and affected tools.

---

## Review With Others — Discuss the Big Picture

**Framework tool name:** Discuss the Big Picture

**Official tool name:** Business Review

**Engineering / product-development essence:** Align decision-makers and stakeholders on purpose, tradeoffs, constraints, unresolved concerns, and commitment before moving forward.

**Plain-English purpose:** Facilitate a big-picture alignment conversation with key stakeholders so the decision still makes sense overall and the major people involved understand the tradeoffs, direction, and implications.

**Key questions:** Who needs to be aligned before this moves forward? What tradeoffs need explicit agreement? What concerns need to be surfaced? What would each stakeholder need to understand? What decision should not move forward without alignment?

**Scenario intelligence to bring:** Surface alignment issues people often avoid: decision authority, money/control tradeoffs, shared consequences, values conflicts, family expectations, partner disagreement, unresolved objections, and what should pause until people agree. Help the user create a conversation that clarifies commitment rather than producing vague consensus.

**Operating steps:** 1. Identify who needs alignment before the decision moves forward. 2. Summarize the big tradeoffs and shared consequences. 3. Surface unresolved concerns or likely objections. 4. Define what needs explicit agreement. 5. Create a discussion agenda or alignment guide. 6. State what should pause until shared agreement exists.

**Deliverables:** Chat: Stakeholder alignment guide, big-picture discussion agenda, tradeoff summary, shared-decision checklist, unresolved-questions list. Exportable: Decision review packet, one-page stakeholder summary, spouse/partner/team discussion guide.

**Quality bar:** Output must identify the key stakeholders who need alignment, summarize the big tradeoffs, provide a discussion agenda, surface unresolved concerns, and state what should not move forward until shared agreement exists.

**Common failure modes:** Too fluffy, treats big-picture review as solo reflection, ignores key stakeholders, fails to surface tradeoffs, does not identify decisions that require shared agreement

**Where used in process:** Intermingle with any primary-sequence tool when stakeholder input, shared consequences, decision authority, buy-in, or explicit agreement matters. Feed outcomes back into the current and affected tools, and rerun Check “What Matters” when alignment changes the plan.
