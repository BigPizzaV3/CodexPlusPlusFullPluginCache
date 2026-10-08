# Core Gauntlet Loop

Use this reference to make the workflow operational rather than ceremonial.

## Contents

1. Working state
2. Stage protocol
3. Clarification policy
4. Intensity and cycle budgets
5. Defect prioritization
6. Stop gates
7. Failure and limitation handling
8. Proportionality examples

## 1. Working state

Maintain a compact internal state throughout the task:

| Item | What to record |
| --- | --- |
| Outcome | The real result the user needs, not merely the literal wording |
| Audience | Who will use, read, judge, or act on the result |
| Deliverables | Required artifacts, formats, and completion boundaries |
| Constraints | Time, scope, style, technical, legal, policy, data, and tool constraints |
| Success criteria | Observable conditions that distinguish a strong result from a plausible first draft |
| Archetypes | One primary archetype plus any secondary archetypes needed for a hybrid task |
| Benchmark | User reference, authoritative standard, researched real-world comparator, or explicitly derived professional rubric |
| Candidate set | Internally generated alternatives; never relabel these as an external benchmark |
| Domain boundary | For qualifying feature work: what the feature represents, deliberately excludes, and can plausibly extend to |
| Implementation scope | Selected implementation dimensions plus known stack and existing-system context; avoid unsupported detail |
| Second-order effects | Existing assumptions invalidated, downstream impact, safeguard, and acceptance-criteria status |
| Validation plan | Checks that can actually be performed in the current environment |
| Evidence ledger | Passed, failed, not run, or unavailable for each important check |
| Stress assumptions | Outcome-driving assumptions, downside values, breakpoints, and mitigations when relevant |
| Defect register | Defect, severity, evidence, likely impact, and proposed fix |
| Current weakest point | The issue with the highest expected impact on the user's outcome |
| Iteration evidence | Adversarial finding, targeted revision or no-change justification, and re-validation evidence |
| Cycle and decision | Current improvement cycle, maximum cycles, open gates, and PASS / PASS WITH LIMITATIONS / BAR NOT REACHED |

Do not expose this state as chain-of-thought. Surface only concise decisions, results, evidence, material changes, and limitations that help the user.

## 2. Stage protocol

### UNDERSTAND

Purpose: identify the intended outcome and avoid solving the wrong problem.

Determine:

- what success enables for the user
- required deliverables and formats
- target audience and context of use
- supplied inputs, references, files, links, and existing work
- explicit constraints and implied non-goals
- major risks, unknowns, and dependencies
- available tools and realistic validation methods
- for feature or system work, whether this is greenfield or an existing product, what stack or contracts are known, and what level of implementation detail the user actually needs

Exit when there is enough information to take a useful next action. Do not require exhaustive certainty.

### DEFINE SUCCESS

Purpose: turn vague quality expectations into observable conditions.

For each important expectation, derive one or more criteria that can be inspected, tested, compared, or defended. Favor criteria tied to user outcomes.

Examples:

- "professional" can become complete, coherent, internally consistent, audience-appropriate, free of obvious errors, and formatted to the conventions of the domain
- "production-ready" can become requirements-complete, tested on critical paths, resilient to expected failures, maintainable, secure enough for the stated context, and operationally documented
- "beautiful" can become clear hierarchy, deliberate composition, coherent typography, balanced spacing, consistency, and lack of unfinished visual states
- "investor-ready" can become clear thesis, evidence-backed market framing, credible economics, explicit assumptions, risk treatment, and decision-useful presentation

Separate must-pass criteria from desirable improvements. Do not manufacture false precision.

### CLASSIFY

Purpose: select the right quality dimensions and validation methods.

Choose one or more archetypes from `archetypes.md`. Hybrid classification is normal. Examples:

- a research-backed article is RESEARCH + WRITING
- a SaaS landing page is WEB/UI/UX + WRITING + VISUAL
- a financial model is DATA/SPREADSHEETS + ANALYSIS/STRATEGY
- a product prototype is PRODUCT/FEATURE + SOFTWARE + WEB/UI/UX + VISUAL
- a feature specification is PRODUCT/FEATURE plus SOFTWARE, WEB/UI/UX, DATA, or STRATEGY only where those failure modes matter

Identify which archetype owns each critical requirement so important checks do not fall between categories.

### DECOMPOSE

Purpose: make complex work reviewable and prevent high-risk components from hiding inside a monolith.

Split the task into meaningful workstreams. Mark:

- dependencies that determine order
- independent work that can be handled separately
- high-risk components where failure would invalidate the result
- high-uncertainty components that need research or experiments
- components requiring specialist or visual review
- integration points where individually good parts could conflict
- for product or system changes, existing assumptions and downstream consumers that the new behavior could invalidate

Decomposition should improve execution and review. Do not fragment trivial work.

### SET BENCHMARK AND TEST PLAN

Purpose: define how quality will be challenged before building.

Choose the benchmark using `benchmarks.md`. Keep two concepts separate:

- **Candidate alternatives** are options being considered or generated inside the task.
- **Benchmarks** are user-supplied references, authoritative standards, researched real-world comparators, or a clearly labeled derived professional rubric.

Three generated options can compete with each other, but they do not become an external benchmark merely because there are three of them.

Map each must-pass criterion to the strongest realistic validation method available. Examples:

- executable tests, linters, compilers, type checks, static analysis, or smoke tests
- browser interaction, rendering, screenshots, responsive checks, or accessibility inspection
- source triangulation, citation checks, recency checks, contradiction analysis, or real-world comparator research
- calculations, formula inspection, reconciliation, schema checks, sensitivity analysis, or reproducibility checks
- document rendering, slide inspection, layout review, link checks, or file-format validation
- structured comparison against a supplied reference or authoritative standard
- expert-style review when objective testing is not possible

For market, product, business, research, design, and strategy work, prefer credible real-world comparators when current research tools are available and the comparison would materially improve the decision.

Decide in advance what cannot be validated. Label it later as NOT RUN or UNAVAILABLE rather than allowing it to disappear.

### BUILD OR INSPECT

Purpose: produce the strongest initial candidate or establish an accurate baseline.

In RUN mode:

- build the complete requested deliverable, not merely a plan or sample, unless scope prevents full completion
- satisfy critical requirements first
- make high-risk assumptions explicit enough to verify
- preserve traceability from requirements to implementation
- for product or feature work, select the product and architecture direction before expanding implementation detail; establish a domain boundary so V1 scope is principled rather than merely shorter

In AUDIT / IMPROVE mode:

- inspect the current candidate before changing it
- identify strengths worth preserving
- locate defects and omissions against requirements, tests, and benchmark
- avoid a zero-based rebuild unless targeted repair would be less reliable, more expensive, or structurally impossible

### VALIDATE

Purpose: establish evidence before critique and success claims.

For every important check, use one status:

- **PASSED** - the check was actually performed and met its condition
- **FAILED** - the check was actually performed and found a defect
- **NOT RUN** - the check was feasible but was not performed; state why when material
- **UNAVAILABLE** - the environment, access, input, or tool needed for the check does not exist

A check cannot pass by plausibility. Source review is not runtime testing. Code review is not browser inspection. A citation list is not source verification. A successful file creation is not proof of layout quality.

For forecasts, economics, business models, plans, or strategies, add a focused stress-test pass:

1. Identify the assumptions with the largest effect on the user's outcome.
2. Rank them by impact and uncertainty.
3. Stress the top one to three with plausible downside values or failure conditions.
4. Recalculate or trace the resulting operational consequences.
5. Identify the breakpoint, mitigation, contingency, or kill criterion.

Do not attack every assumption pessimistically. Stress the assumptions that matter most.

### CRITIQUE

Purpose: search for reasons the candidate would fail an expert or real-user review.

For non-trivial STRONG and GAUNTLET intensity, run at least two logically separate passes before finalization:

1. **Domain critic** - evaluates the candidate against domain standards and success criteria.
2. **Adversarial critic** - searches for shortcuts, hidden assumptions, omissions, inconsistencies, untested claims, generic output, brittle behavior, and benchmark gaps.

The adversarial pass must produce one of these evidence states:

- a concrete material weakness, its likely impact, and the highest-value response; or
- the strongest observed challenge plus an explicit conclusion that no material revision is justified because the issue is below the materiality threshold, already mitigated, or not responsibly changeable, supported by the checks and benchmark comparison already performed.

Do not fabricate a weakness merely to force visible iteration. Use `reviewers.md` for the detailed protocol. Do not let praise consume review bandwidth unless it identifies something that should be preserved.

### COMPARE

Purpose: replace vague self-approval with a concrete quality challenge.

Ask where the candidate loses against the selected benchmark on critical dimensions. For market-facing or strategic work, ask where it loses against credible real alternatives, not only against an abstract rubric. Record gaps as:

- critical - likely to invalidate the result or cause material harm
- high - likely to materially reduce the user's outcome
- medium - meaningful but not outcome-determining
- low - polish or preference with limited practical impact

Do not penalize deliberate differences that better serve the user's constraints. The goal is to survive comparison, not copy the reference.

Keep candidate alternatives distinct from benchmarks. An internally generated option may beat another option, but that does not prove competitiveness against the market, an external standard, or a real reference.

### CHALLENGE IN THREES

Purpose: introduce real competition where the first idea is likely to be sticky or mediocre.

At full GAUNTLET intensity, select one high-leverage component such as architecture, layout direction, monetization and delivery model, headline, strategy, explanation, research interpretation, formula design, or critical interaction. Run the challenge before committing to a foundational direction such as business model, architecture, or design concept. Run it after critique when comparing repairs or treatments for an existing candidate.

Create three alternatives only after defining the same hard constraints and comparison rubric. Every alternative must:

- have a credible path to satisfy the user's objective
- differ materially in governing approach, not only wording or cosmetics
- be developed enough for fair comparison
- include its strongest advantage, important disadvantage, key dependency, and validation burden
- avoid serving as an obvious decoy for a preferred option

Evaluate all three against the same criteria and evidence, preferably without privileging generation order. Select one, synthesize compatible strengths, or reject all three if none passes the viability floor.

Skip or compress the challenge when:

- the task is tiny
- only one viable solution exists because of hard constraints
- the expected quality gain is lower than the cost
- generating alternatives would create risk without improving evidence

Candidate alternatives are not automatically benchmarks. Compare the selected direction against the real benchmark separately.

### TRANSLATE TO IMPLEMENTATION WHEN USEFUL

Purpose: turn a selected product, software, feature, API, or system-design direction into a buildable result at the level the user actually needs.

Run this stage when the user asks how the feature should work, requests edge cases, behavior, architecture, data structures, technical implications, or is clearly designing something that will be built. Skip or compress it for casual brainstorming, purely strategic work, small writing tasks, concept-only scope, or thin context where technical detail would be speculative.

Read `implementation-pass.md`. Select only relevant dimensions. Common high-value outputs include:

- a domain boundary and the smallest abstraction that correctly models the known domain
- important entities and relationships
- state transitions and invariants
- time, conflict, trust, permission, or user-visible semantics where relevant
- the second-order question: which existing assumptions in the rest of the system stop being true?
- downstream safeguards, migration, or compatibility implications
- observable acceptance criteria

Prefer semantic domain modeling before database-specific design unless the stack is known. Do not default to a universal rules engine or platform abstraction. Do not invent fields, APIs, indexes, caches, migrations, or permissions that the context does not support. Treat acceptance criteria as proposed checks until they are executed against an implementation.

After this translation, validate and critique the expanded candidate. If architecture was consequential, the competitive challenge must have occurred before committing to the implementation model.

### IMPROVE AND RE-VALIDATE

Purpose: fix what matters without destroying strong work and create evidence that the loop affected the result.

For an audit-only request, do not apply changes. Use this stage to formulate and prioritize concrete fixes, then judge the supplied candidate as-is. For an audit-and-improve request, apply the selected fixes and re-validate them.

Prioritize by expected quality gain:

`impact on user outcome x confidence in diagnosis x fix leverage / cost and risk`

For every material cycle, retain a compact internal link:

`adversarial finding -> selected change -> affected checks re-run -> result`

Fix critical and high-severity defects first. Preserve components that already pass. Re-run every validation affected by the change, plus regression checks for adjacent components. For feature or system changes, re-check domain invariants, state transitions, second-order effects, migration assumptions, and acceptance-criteria consistency when the revision touches them.

If the review finds no material revision worth making, do not churn the work. Still record the strongest observed challenge and why it is below the revision threshold, already mitigated, or not responsibly changeable. Never invent an improvement.

Do not perform random full rewrites or cosmetic changes merely to create another cycle.

### JUDGE

Purpose: decide whether evidence supports stopping.

The judge must be willing to reject the current candidate. If a material deficiency remains and another cycle has meaningful expected value, choose a targeted loop and route back to the relevant stage rather than restarting mechanically.

When finalizing, choose exactly one external decision:

- **PASS** - critical requirements are satisfied, important checks were completed, and no material avoidable weakness remains
- **PASS WITH LIMITATIONS** - the result is strong and usable, but one or more material points could not actually be validated; the missing evidence is not likely to overturn the core result
- **BAR NOT REACHED** - a material deficiency remains that prevents claiming the requested quality level

Do not use PASS WITH LIMITATIONS for immaterial caveats. Minor preferences or negligible uncertainty can coexist with PASS. If the missing evidence could overturn the core recommendation, readiness claim, or primary outcome, choose BAR NOT REACHED.

## 3. Clarification policy

Prefer action over questioning.

Ask a question only when the missing answer would:

- materially change the solution direction
- create significant safety, legal, privacy, financial, or operational risk
- determine an essential deliverable or format
- make validation impossible or meaningless
- force a choice between incompatible outcomes

Ask the smallest number of highest-value questions. Do not send a questionnaire. When reasonable defaults can be stated and safely used, proceed with those defaults.

In BUILD mode, unresolved assumptions can be encoded explicitly into the copy-paste prompt so the fresh conversation can resolve them at execution time.

## 4. Intensity and cycle budgets

### QUICK

Use for moderate or small tasks where one challenge pass can materially improve quality.

Sequence:

`build or inspect -> focused review -> optional compact implementation translation when requested -> improve weakest point -> final verification`

Maximum improvement cycles: 1.

### STRONG

Use for serious professional work that benefits from objective testing and a separate adversarial review.

Sequence:

`understand -> define success -> plan -> build or inspect -> validate -> domain critique -> adversarial critique -> optional implementation translation for qualifying feature work -> improve highest-value weakness -> re-validate -> judge`

For non-trivial work, at least one adversarial pass must occur before finalization. Maximum improvement cycles: 3.

### GAUNTLET

Use for explicit Gauntlet requests and high-quality or high-stakes work that is not prohibited or safety-sensitive in a way that limits assistance.

Sequence:

`understand -> define success -> classify -> decompose -> benchmark and test plan -> build or inspect -> validate and stress-test relevant assumptions -> domain critic -> adversarial critic -> benchmark comparison -> selective competitive three-way challenge -> conditional implementation translation for qualifying feature work -> improve highest-value weakness -> re-validate -> judge -> loop if justified`

Maximum improvement cycles: 5.

The cap prevents endless iteration. Stop earlier when the gates pass. A tiny explicit Gauntlet may compress the stages into one short pass while retaining adversarial improvement. Do not finalize a complex first candidate without the required adversarial pass.

## 5. Defect prioritization

Use severity and evidence rather than aesthetic preference alone.

### Critical

The result is unsafe, unusable, invalid, materially wrong, missing a required deliverable, or likely to fail its primary purpose.

### High

The result may work but has a serious weakness likely to change the user's outcome, such as an untested critical path, unsupported central claim, broken responsive layout, incorrect formula, or major benchmark gap.

### Medium

The weakness is meaningful and should be fixed when the expected value is good, but it does not invalidate the primary outcome.

### Low

The issue is minor polish, preference, or optimization. Do not let low-severity churn delay delivery after the stop gates pass.

When several defects share a severity, prioritize the one with the broadest downstream effect or highest leverage.

## 6. Stop gates

Pass only when all applicable gates are satisfied:

### Requirements gate

- every critical requirement is addressed
- every required deliverable exists in the requested format
- intentional exclusions are explicit

### Defect gate

- zero known critical defects remain
- zero unresolved high-severity defects remain unless the user explicitly accepts them

### Validation gate

- all realistically available critical checks were performed
- performed critical checks passed
- unavailable or unperformed checks are disclosed when material
- outcome-driving assumptions were stress-tested when the task contains forecasts, economics, business models, plans, or strategy

### Implementation gate

For product, software, feature, API, or system-design work where implementation detail materially affects usefulness:

- the selected direction is translated to the requested implementation depth, not merely named
- the domain boundary is explicit when scope or future extension could otherwise be ambiguous
- critical entities, states, invariants, conflicts, or time semantics are addressed where relevant
- important second-order effects and invalidated system assumptions are addressed or explicitly left unvalidated
- acceptance criteria are observable and are not mislabeled as executed tests
- stack-specific details appear only when supported by the known environment

### Benchmark gate

- the benchmark is a real reference, authoritative standard, researched comparator, or explicitly derived professional rubric
- candidate alternatives were not mislabeled as external benchmarks
- no material avoidable gap remains on critical dimensions
- deliberate deviations are justified by user constraints or a better outcome

### Iteration-evidence gate

For non-trivial STRONG and GAUNTLET work:

- a fresh adversarial pass occurred before finalization
- it named the strongest observed challenge and identified a concrete material weakness, or explicitly justified why that challenge did not warrant revision
- the highest-value weakness was addressed when a change was justified
- affected checks and relevant regressions were re-run after the change

### Critic gate

- the adversarial critic identifies no remaining issue likely to materially change the user's outcome

### Marginal-value gate

- another cycle is unlikely to produce meaningful improvement relative to its cost, risk, and delay

Scores can summarize diagnostics but cannot override a failed gate.

Final decision:

- **PASS** when all critical gates are supported and no material avoidable weakness remains
- **PASS WITH LIMITATIONS** when the result is strong and usable but a material point could not be validated and the missing evidence is not likely to overturn the core result
- **BAR NOT REACHED** when a material deficiency remains

Do not downgrade to PASS WITH LIMITATIONS for trivial caveats. If missing evidence could overturn the core result, choose BAR NOT REACHED.

## 7. Failure and limitation handling

When the cycle cap is reached without passing:

1. Return the strongest achieved deliverable or audit.
2. State which stop gates remain open.
3. Identify the material gaps and their likely impact.
4. Explain why they remain: missing input, unavailable tool, lack of access, unresolved contradiction, expertise boundary, time or scope cap, or a hard trade-off.
5. State what additional input, tool, access, expertise, or decision would close the gap.

Never replace this with a fake perfect score.

When a required validation is unavailable, use precise language such as:

- "Created, but runtime behavior was not validated because execution was unavailable."
- "Source structure was reviewed; rendered visual quality remains unvalidated."
- "The claim is plausible from the supplied material, but no independent source check was possible."

## 8. Proportionality examples

### Two-sentence email

Define the intended tone, produce the message, challenge the weakest phrase, revise once, and verify clarity. Do not expose a ten-stage report.

### Production code change

Map requirements, inspect surrounding code, choose tests, implement, run objective checks, review architecture and edge cases, compare against project conventions, fix material defects, and re-run tests.

### Landing page against a screenshot

Treat the screenshot as the primary benchmark, inspect the rendered page when possible, compare hierarchy, spacing, typography, density, responsiveness, copy, and interactions, then improve the largest visible gap and re-render.

### Product feature planning

Select the domain and architecture direction, establish a scope boundary, then translate only the implementation semantics needed to make the feature buildable. Review state, invariants, edge cases, second-order system effects, migration, and observable acceptance criteria. Avoid both a one-field patch that corrupts existing semantics and a universal engine the known domain does not justify.

### Research-backed strategy

Define the decision the research must support, establish evidence criteria, gather and triangulate sources, separate fact from inference, compare against credible real alternatives, stress the assumptions with the greatest outcome effect, improve the highest-value weakness found by the adversarial pass, re-check the affected economics or logic, and disclose uncertainty.
