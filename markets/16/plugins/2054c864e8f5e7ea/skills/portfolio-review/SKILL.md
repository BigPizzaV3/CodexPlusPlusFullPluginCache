---
name: portfolio-review
description: Review a portfolio of AI agents against the E-mployee Maturity Curve, the role registry, dependencies and review capacity, and decide what to scale, narrow, hold, pause or retire. Use when an organization has several AI agents to manage or scale, or for a board review of its AI portfolio.
---

# Artificial Workforce Portfolio Review

Chapter 14 starts from a simple observation: "One E-mployee is a role. Ten E-mployees are a management problem." An **artificial workforce** means several bounded artificial-labor roles, "each with a human owner, an objective, limits, review, evidence, and a decision about whether to continue." "The workforce is artificial; the accountability is not." Scale "is multiplication of accountable roles with shared controls", and "A pilot is evidence, not permission." This workflow places the portfolio on the Maturity Curve, checks the registry, shared controls, dependencies and review capacity, and produces a board decision for each role.

## When to use
- "We have several AI agents. How do we manage or scale them?"
- A quarterly or board review of an AI portfolio, or an intake decision on a new role.
- A successful pilot is about to be copied to other teams.
- Do not use this for a single role's first launch. Use `ninety-day-roadmap` for that. For one role's tier and controls, use `risk-classification`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. Which AI roles exist, at what stage, and who owns each one?
2. What do they share: vendor, model, data source, connector, identity, reviewer, specialist or fallback?
3. What is being proposed: more volume, a new audience, new authority or new roles?

If the user cannot answer, build the review anyway and mark the gaps `Missing`. Do not stall.

## E-mployee Maturity Curve (exact)
**Access → task → standing role → supervised workforce → governed portfolio.** Each stage requires a new control gate. The curve is "not a score of intelligence, autonomy, productivity, or organizational virtue." "The most dangerous transition is from standing role to supervised workforce."

| Stage | What exists | Required executive question | Gate to the next stage |
|---|---|---|---|
| Access | A person can use a model or tool. | Who is allowed to experiment, with what data and environment? | Access is bounded, logged, and not confused with a business role. |
| Task | A system performs a defined task. | What is the task, its output, its exclusions, and its reviewer? | Outcome, acceptance condition, source permission, review, and stop path exist. |
| Standing role | The task is repeatedly assigned to a named E-mployee role. | Who owns the role, the result, the evidence, the cost, and the retirement decision? | Role Charter, Authority Matrix, performance evidence, risk classification, and ownership are current. |
| Supervised workforce | Several standing roles operate together under human supervision. | What is common, what is local, and can reviewers, specialists, and human fallback carry the load? | Registry, shared controls, capacity, dependency map, change route, and portfolio review exist. |
| Governed portfolio | Roles are managed as an interdependent institutional system. | Is the portfolio creating credible value without exceeding its risk, capacity, concentration, or exit tolerance? | Board-level scale, narrow, pause, redesign, and retirement decisions are evidenced and repeatable. |

## Portfolio role registry
The registry is "the institution's memory". It is not a software inventory or a compliance database. Each role's record holds: role name and version, outcome owner, Role Charter, task bundle, data sources, tools, model, vendor, connectors, environment, authority powers, reviewer, risk tier, affected parties, worker effects, economics, dependencies, performance evidence, incidents, changes, open controls, stop conditions, retirement authority and next review.

- **Friday-afternoon test:** "if the role behaves unexpectedly on a Friday afternoon, can the organization find the person who can stop it and the evidence needed to understand what happened?" "A stale registry is not a clerical defect. It is evidence that the portfolio cannot describe itself."
- **Intake rule:** the proposing team shows the outcome, workflow, Role Charter, data permission, authority boundary, reviewer, risk tier, baseline, counterfactual, dependencies, common controls, human fallback, stop condition and exit path. If any item is unresolved, the role may remain an experiment, but it is not counted as a governed standing role.

## Reuse controls; do not copy assumptions
"A common control is not a common decision." Ask whether two roles share the same consequence, data exposure, authority, review capacity and rollback path. If they do not, the common control needs a local layer.

| Reuse across the portfolio | Keep local to the role or business owner |
|---|---|
| Identity, credential, access-review, and revocation patterns | Purpose, objective, exclusions, and definition of done |
| Logging, provenance, version, and evidence mechanisms | Domain quality threshold and human judgment |
| Connector inventory, change notification, and incident intake | Data use, audience, affected-party consequence, and fallback |
| Reviewer training, sampling methods, and escalation templates | Review decision, exception interpretation, and release authority |
| Procurement, vendor due diligence, and security baselines | Continue, narrow, pause, redesign, or retire decision |
| Portfolio inventory and board-report structure | Workforce effect, job-quality decision, and local legal/domain question |

## Dependencies and concentration
For each dependency, record the asset, owner, criticality, alternatives, shared roles, change route, exit cost, fallback and blast radius. One role on a common model has a dependency. Ten roles on the same model, contract and untested connector have **concentration**.

| Dependency | Portfolio question | Evidence before scale |
|---|---|---|
| Vendor or model | What happens when price, terms, behavior, availability, or policy changes? | Change notification, alternative, contract review, fallback, exit estimate. |
| Data source | Which roles rely on its quality, permission, schema, or geography? | Data owner, source permission, lineage, change route, correction path. |
| Connector or tool | Can one defect or update affect multiple roles? | Version record, test environment, blast-radius analysis, rollback. |
| Identity and access | Can access be revoked across all affected roles? | Role-to-credential map, expiry, revocation test, emergency path. |
| Reviewer or specialist | Who handles peaks, absence, disputes, and high-stakes exceptions? | Capacity ledger, backup, queue health, intervention power. |
| Human fallback | Can work return to people without unsafe delay or lost knowledge? | Manual process, staffing, training, data access, exercise. |
| Platform team | Does support capacity match the portfolio's change and incident load? | Service capacity, response route, ownership, escalation, retirement support. |

## Observability, change and capacity
- **Observability is more than uptime.** Show role status, version, volume, exceptions, review time, rejection and correction patterns, data-access events, authority use, unresolved escalations, incidents, workforce signals, economic confidence and change history.
- **Change record:** which roles changed, which assumptions changed, which controls were retested, which humans were informed, and who decided whether the roles could continue.
- **Review capacity:** total the review volume, exception volume, average review time, peak demand, queue age, competence, backup and intervention power across roles, because one reviewer may appear on five charts. There is no universal reviewer-to-role ratio.
- **Four economic distinctions for the board:** (1) displacing or avoiding a cost is not the same as releasing capacity; (2) released capacity has value only if it is redeployed, used to meet demand or otherwise attributed; (3) portfolios create coordination and concentration costs that a single-role case does not show; (4) uncertainty widens as dependencies and change surfaces multiply. Do not hide shared costs in another budget.

## Portfolio operating cadence
| Cadence | Questions | Typical decision |
|---|---|---|
| Intake review | Is the role defined, bounded, staffed, permitted, and reversible? | Experiment / reject / narrow / prepare for standing role. |
| Weekly operating review | What changed in volume, exceptions, review load, quality, access, or queue health? | Continue / add capacity / correct / pause. |
| Monthly risk and change review | Which models, vendors, data, tools, audiences, authorities, or workers changed? | Retest / reclassify / escalate / restrict. |
| Quarterly portfolio review | Is the portfolio creating credible value without exceeding capacity, concentration, risk, or exit tolerance? | Scale / hold / redesign / retire. |
| Event-triggered review | Did an incident, rights concern, control failure, outage, material change, or repeated exception occur? | Stop / stabilize / investigate / redesign / decide. |
| Retirement review | Does the role still create value, retain a defensible purpose, and have a supported fallback? | Retire / archive / transfer / redesign / re-enter experiment. |

The board should ask "What are we learning and what are we stopping?", not "How many agents did we add?" "Contraction can be evidence of control."

## Failure conditions
| Failure condition | Scale response that is not permitted | Responsible portfolio response |
|---|---|---|
| Role is missing an owner, version, or stop authority | Count it as governed because the tool is active | Do not scale; complete the registry or pause. |
| Reviewer queue exceeds safe capacity | Treat human approval as a rubber stamp | Narrow, add capacity, shift review, or pause. |
| Common control hides a different local consequence | Assume standardization proves fitness | Add a local control, reclassify, or do not scale. |
| Vendor, model, data, or connector changed without test | Continue because the old role performed well | Hold release, retest, reclassify, or roll back. |
| Concentration lacks alternative or fallback | Expand dependency because it is efficient | Limit growth, add redundancy, or retire. |
| Economics depend on unreleased capacity | Report time saved as profit | Revise the Value Ledger and require attribution. |
| Repeated quality, incident, rights, or workforce failure | Add volume to "learn faster" | Narrow, redesign, pause, or retire. |
| Human fallback cannot operate | Call the role resilient because it is automated | Restore capability, fund fallback, or stop. |

"Increasing volume is different from increasing authority." Adding an internal audience is different from entering a customer workflow.

## The board decision: seven questions
1. Which roles are active, experimental, standing, supervised, changed, paused, or retired?
2. Which roles share a vendor, model, data source, connector, identity, reviewer, specialist, or fallback?
3. What changed since the last decision, and which controls were retested?
4. Where is review capacity below expected or peak demand?
5. Which economic claims are measured, attributed, redeployed, or still uncertain?
6. Which workforce, customer, rights, privacy, security, legal, or contractual effects require action?
7. What will we scale, narrow, hold, pause, or retire—and who has the authority to do it?

## Steps
1. Build a registry row for each role and mark unknown fields `Missing`. Run the Friday-afternoon test on every row.
2. Place each role on the Maturity Curve, then the portfolio as a whole, and name the gate not yet met. Apply the intake rule to any proposed role.
3. Map dependencies and flag concentration. Total the review capacity against peak demand.
4. Check which controls are shared and which decisions must stay local. Test each economic claim against the four distinctions.
5. Check each failure condition. Where one is present, give the responsible response and never the response that is not permitted.
6. Answer the seven board questions. Decide for each role whether to scale, narrow, hold, pause or retire. Scope every scale decision to the exact expansion the evidence supports. Treat a role's success as "relevant but not contagious".

## Output format
1. **Registry summary** as a table (Role | Stage | Outcome owner | Version | Risk tier | Reviewer | Stop authority | Next review | Friday test).
2. **Maturity position**: the portfolio's stage and the gate it has not met.
3. **Dependency and concentration map**, the **review-capacity view**, and the **failure conditions found**, each with its responsible response.
4. **Board decision**: the seven questions answered, then a per-role table (Role | Proposed change | Evidence | Decision | Conditions | Who decides).
5. Status line: *Author-created instruments. The Maturity Curve is a proposed diagnostic, not a score of intelligence, autonomy, productivity, or organizational virtue. The registry is not a software inventory or a compliance database. "Artificial workforce" is not a legal category or a guarantee of productivity, safety, compliance, or value.*
6. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 14.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
