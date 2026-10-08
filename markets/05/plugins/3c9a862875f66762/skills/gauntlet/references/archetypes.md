# Task Archetypes and Adaptive Rubrics

Classify the task before selecting tests and critics. Use multiple archetypes for hybrid work.

## Contents

1. Classification rules
2. Software and coding
3. Product, feature, and system design
4. Web, UI, and UX design
5. Research and fact finding
6. Writing and content
7. Analysis, strategy, and business
8. Data and spreadsheets
9. Visual and creative work
10. General tasks
11. Hybrid-task integration

## 1. Classification rules

Choose archetypes based on the deliverables and failure modes, not only keywords.

- Use a primary archetype for the main deliverable.
- Add a secondary archetype when it contributes critical requirements or validation.
- Assign each must-pass criterion to an archetype owner.
- Select only dimensions that matter to the user's outcome; do not mechanically score every dimension.
- Add task-specific dimensions whenever the generic rubric misses a critical constraint.

A strong rubric includes:

- must-pass requirements
- quality dimensions
- objective or observable checks
- likely expert objections
- benchmark comparison dimensions
- known limits of validation

## 2. Software and coding

### Core dimensions

- functional correctness
- requirements coverage
- architecture and separation of concerns
- maintainability and readability
- error handling and recovery
- edge cases and boundary conditions
- security and privacy appropriate to the context
- performance and resource use
- test quality and coverage of critical behavior
- integration compatibility
- configuration and dependency hygiene
- operational readiness and observability

### Strong success criteria

Derive criteria such as:

- required behavior is implemented on the critical path
- inputs are validated and failures are handled deliberately
- interfaces and data contracts are consistent
- tests cover normal, failure, and high-risk edge cases
- no obvious secret, permission, injection, or unsafe-default issue remains
- the implementation follows surrounding project conventions when a codebase exists
- deployment, migration, configuration, and rollback implications are addressed when relevant

### Validation options

Use the strongest available checks:

- unit, integration, end-to-end, regression, and smoke tests
- compilation, type checking, linting, formatting, static analysis, and dependency checks
- targeted reproduction of the original bug or requirement
- runtime inspection, logs, API calls, database queries, or browser checks
- performance measurements for actual bottlenecks
- security review focused on the stated threat surface
- diff review against project patterns and neighboring modules

### Critic focus

Ask:

- What breaks outside the happy path?
- Which requirement is only superficially implemented?
- What hidden state, concurrency, migration, authorization, or integration issue remains?
- Are tests proving behavior or merely mirroring the implementation?
- Is complexity justified?
- Can another maintainer understand and safely modify this?

### Critical failures

Examples include incorrect core behavior, data loss, security exposure, broken integration, unhandled destructive failure, missing required tests for high-risk behavior, or a change that cannot be operated safely in its intended context.

## 3. Product, feature, and system design

Use for feature discovery, product behavior, domain modeling, API or platform changes, system design, and implementation-oriented specifications. Combine with SOFTWARE, WEB/UI/UX, DATA, RESEARCH, or STRATEGY only where those failure modes matter. Read `implementation-pass.md` when the selected direction should become implementation-ready.

### Core dimensions

- user value and problem fit
- domain semantics and conceptual integrity
- architecture and separation of concerns
- data integrity and canonical-versus-contextual data
- edge cases and boundary behavior
- lifecycle state and transition complexity
- time, recurrence, conflict, and precedence semantics where relevant
- trust, verification, permissions, and misuse where relevant
- UX clarity and user-visible states
- explicit scope and domain boundary
- implementation feasibility and time-to-deliver
- migration and backward compatibility
- downstream and second-order system effects
- observability and operational support
- maintainability
- extensibility without premature generalization

### Strong success criteria

Derive criteria such as:

- the feature solves a specific user or system problem and its primary behavior is unambiguous
- the model preserves canonical existing semantics instead of overwriting them with temporary or contextual values
- the domain boundary states what the feature represents, excludes, and can plausibly extend to
- the chosen abstraction is the smallest one that correctly models known use cases and credible near-term extensions
- important entities, relationships, states, transitions, and invariants are explicit where they affect behavior
- scheduling, conflicts, trust, permissions, and ambiguity have defined behavior when relevant
- the design identifies which existing assumptions elsewhere in the system become false and adds safeguards
- architecture alternatives are genuinely viable and compared consistently when the choice is consequential
- V1 is implementable without silently creating a universal platform or blocking plausible extension
- migration, compatibility, rollout, and historical-data implications are addressed for an existing system
- acceptance criteria cover normal, boundary, invalid, conflict, and downstream behavior at an appropriate depth

### Validation options

- requirement-to-behavior traceability
- domain-model walkthrough using normal, edge, invalid, and conflicting cases
- state-transition and invariant review
- time-boundary, timezone, recurrence, and midnight-crossing scenarios where relevant
- conflict, precedence, duplicate, staleness, and trust scenarios
- second-order dependency audit across analytics, search, caches, reporting, jobs, integrations, and historical data
- architecture challenge using equally viable alternatives and the same criteria
- schema, API, query, permission, and observability review when technical context exists
- migration and backward-compatibility review against current records and contracts
- acceptance-criteria review and, when an implementation exists, execution of the corresponding tests

### Feature architecture challenge

When architecture is consequential, compare approximately three domain-appropriate models before commitment. A minimal patch, a broad generalized engine, and a domain-specific abstraction are common shapes, but never force them. Compare correctness, complexity, implementation cost, UX, data integrity, migration impact, maintainability, and plausible future requirements. State a real disadvantage and likely failure mode for every option. Reject both under-modeling and premature platform building.

### Critic focus

Ask:

- Is the feature modeled as the real domain understands it, or only as the first example was phrased?
- Which canonical data or existing behavior could be corrupted by this change?
- Which state, boundary, conflict, or stale-data case is undefined?
- If this feature is added, which existing assumptions in the rest of the system stop being true?
- Is the architecture a brittle patch, an unjustified universal engine, or the smallest correct abstraction?
- Is the scope boundary principled enough to resist future pressure without blocking near-term extension?
- Can an engineer implement the result without inventing material behavior?
- Are acceptance criteria observable, and are they correctly labeled as proposed or actually executed?

### Critical failures

Examples include corrupting canonical data, undefined behavior for common conflicts or state transitions, a model that cannot represent required cases, a migration that breaks existing records or clients, permissions or trust behavior that enables material abuse, second-order effects that contaminate analytics or downstream decisions, or a concept that remains too ambiguous to implement despite an implementation-oriented request.

## 4. Web, UI, and UX design

### Core dimensions

- information and visual hierarchy
- typography
- spacing and rhythm
- composition and alignment
- component consistency
- responsiveness
- usability and discoverability
- interaction design and feedback states
- accessibility appropriate to the product
- content and microcopy quality
- functional completeness
- loading, empty, error, and success states
- perceived polish and trust

### Strong success criteria

Derive criteria such as:

- the primary action and page purpose are immediately clear
- components follow a coherent visual and interaction system
- layouts work at relevant viewport sizes
- focus, labels, contrast, keyboard behavior, and semantics meet applicable accessibility expectations
- interactive states provide feedback and do not dead-end the user
- copy is specific, useful, and aligned with the audience
- no obvious placeholder, overflow, clipping, misalignment, or unfinished state remains
- the implementation matches supplied references where fidelity is required

### Validation options

- render and inspect the actual interface
- compare screenshots side by side with supplied references
- test relevant viewport sizes and responsive transitions
- exercise critical interactions and states
- inspect keyboard navigation, labels, semantics, contrast, and focus behavior
- check links, forms, validation, loading, error, and empty states
- review layout consistency, content density, and component reuse
- inspect source only as a complement to rendering, never as a substitute for visual validation

### Critic focus

Ask:

- What does a real user misunderstand or fail to notice?
- Where does the hierarchy collapse?
- Which screen looks generic, templated, or unfinished?
- What interaction lacks feedback or recovery?
- Which responsive state breaks the intended composition?
- Where does the candidate visibly lose against the reference?

### Critical failures

Examples include broken primary flows, inaccessible essential interactions, non-responsive critical layouts, unreadable content, misleading controls, missing states that trap the user, or a major fidelity miss when matching a supplied design is required.

## 5. Research and fact finding

### Core dimensions

- source authority and relevance
- source diversity and independence
- recency appropriate to the question
- factual accuracy
- completeness and coverage
- contradiction handling
- evidence strength
- citation accuracy and traceability
- uncertainty treatment
- distinction between fact, interpretation, and inference
- decision relevance

### Strong success criteria

Derive criteria such as:

- central claims are supported by appropriate primary or authoritative sources where available
- time-sensitive facts are current for the decision date
- material viewpoints and contradictory evidence are represented fairly
- conclusions follow from the evidence and do not overstate certainty
- every important citation supports the nearby claim
- unsupported assumptions are labeled
- the result answers the user's actual decision, not merely the topic

### Validation options

- verify important claims against original or authoritative sources
- triangulate central claims across independent sources
- compare publication date with event date and required recency
- inspect methodology, sample, definitions, and limitations of cited studies or datasets
- follow citations to confirm they support the stated proposition
- search for disconfirming evidence and credible alternative explanations
- distinguish reported fact from model inference in the final wording

### Critic focus

Ask:

- Which central claim rests on a weak or circular source chain?
- What relevant contrary evidence is missing?
- Is recency sufficient for a changing topic?
- Are statistics comparable, or do definitions and populations differ?
- Which conclusion is stronger than the evidence permits?
- What would change the recommendation?

### Critical failures

Examples include fabricated or irrelevant citations, stale time-sensitive facts, unsupported central conclusions, omission of decisive contradictory evidence, conflating correlation and causation, or presenting inference as verified fact.

## 6. Writing and content

### Core dimensions

- factual accuracy
- structure and logical flow
- clarity and precision
- audience fit
- tone and voice
- originality and specificity
- argument quality
- evidence and examples
- pacing and emphasis
- usefulness and actionability
- editing quality
- format and publication readiness

### Strong success criteria

Derive criteria such as:

- the opening establishes relevance and a clear promise
- each section advances the central purpose
- claims are specific and supported where evidence is required
- wording fits the audience, channel, and desired tone
- examples and details feel concrete rather than generic
- transitions and pacing maintain attention
- redundancy, filler, cliches, and unsupported superlatives are removed
- grammar, consistency, headings, and formatting are publication-ready

### Validation options

- outline reverse-engineering to test structure
- claim and evidence mapping
- fact and citation checks for research-backed content
- audience and tone review against examples or brand guidance
- line editing for ambiguity, repetition, rhythm, and unnecessary abstraction
- headline, opening, or call-to-action alternatives evaluated against the same goal
- read-aloud or scanability review when appropriate

### Critic focus

Ask:

- Where would a skeptical reader stop believing or caring?
- Which passages could belong to any article or brand?
- What is asserted but not demonstrated?
- What is structurally out of order?
- Which sentence carries too many ideas or hides the main point?
- Does the ending deliver a useful conclusion or merely stop?

### Critical failures

Examples include materially false content, missing required argument or section, plagiarism or uncredited copying, audience-inappropriate tone that defeats the purpose, incoherent structure, or a central claim unsupported by the supplied evidence.

## 7. Analysis, strategy, and business

### Core dimensions

- customer pain, urgency, and target segment
- willingness to pay and payment trigger
- distribution and realistic customer-acquisition path
- competition, substitutes, and likely competitor response
- differentiation and defensibility
- unit economics, cash timing, and incentive alignment
- operational feasibility and hidden delivery effort
- time-to-market and compatibility with the user's deadline
- founder effort, capabilities, and bottlenecks
- legal and regulatory exposure where applicable
- assumptions, dependencies, and evidence quality
- downside case and break-even thresholds
- alternatives and counterfactuals
- validation plan, leading indicators, and kill criteria
- implementation sequence, metrics, and decision usefulness
- internal consistency

### Strong success criteria

Derive criteria such as:

- the customer, painful job, urgency, buyer, and payment trigger are specific
- willingness-to-pay claims are tied to real evidence or clearly labeled assumptions
- at least one credible distribution path can reach the target segment within the required time and resources
- real competitors and substitutes are considered, including why a buyer would switch or act now
- differentiation is meaningful to the customer rather than cosmetic
- unit economics and cash timing are arithmetically consistent and include important variable costs, refunds, fees, direct labor, and acquisition assumptions
- operational effort, delivery burden, founder capacity, dependencies, and legal exposure are not hidden
- at least three viable strategic approaches are compared when a three-way challenge would materially improve the decision
- the recommendation survives a focused downside stress test or exposes its breakpoint
- the validation plan contains measurable signals, dates, thresholds, and kill criteria
- implementation has sequencing, dependencies, owners or founder actions, and success measures

### Evidence ladder

Keep these states separate:

1. **Mathematical possibility** - the model can produce the desired outcome under explicit assumptions.
2. **Market-supported plausibility** - current external evidence supports some assumptions, but no first-party proof exists.
3. **Actual validation** - first-party behavior such as paid sales, signed commitments, completed interviews with strong purchasing evidence, pre-orders, conversion data, or repeat usage supports the claim.

Never present mathematical possibility or researched plausibility as actual validation.

### Deadline-sensitive profitability

When the user specifies a deadline such as "profitable within 30 days," explicitly test whether the model fits that clock. Inspect:

- time to build or prepare the offer
- time to first reachable prospects
- sales-cycle length and decision friction
- acquisition channel setup and expected lead volume
- conversion assumptions and required number of sales
- delivery time, direct labor, support, refunds, and rework
- payment timing, fees, taxes where relevant, and cash collected by the deadline
- upfront tools, advertising, contractor, compliance, and opportunity costs
- founder availability and execution bottlenecks

Distinguish accounting profit from cash collected within the deadline when that difference matters. State the break-even condition and what would make the deadline incompatible with the model.

### Validation options

- current market, competitor, offer, pricing, and distribution research
- source triangulation for customer pain and demand proxies
- willingness-to-pay evidence review
- unit-economics and arithmetic checks
- cash-timing and break-even analysis
- scenario and sensitivity analysis
- focused downside stress tests on the most outcome-sensitive assumptions
- pre-mortem and failure-mode analysis
- feasibility checks against resources, capabilities, timing, founder effort, and dependencies
- legal or regulatory issue spotting where applicable
- three viable candidate models evaluated against the same constraints
- benchmark against real comparable offers, products, businesses, or strategies
- validation experiment design with measurable thresholds and kill criteria
- traceability from evidence to recommendation

### Stress-test examples

Choose only the assumptions with the greatest effect on the outcome, such as:

- conversion or close rate is materially lower
- lead volume or distribution access is weaker
- acquisition cost, refund rate, or delivery effort is higher
- payment arrives later than planned
- a required dependency fails
- a competitor responds more strongly
- legal or platform constraints delay launch

Recalculate the economics or operational plan, identify the breakpoint, and revise the recommendation, mitigation, or kill criteria.

### Critic focus

Ask:

- Is the problem framed to favor the preferred answer?
- Is the customer pain urgent enough to trigger payment now?
- What evidence supports willingness to pay rather than mere interest?
- Is distribution real, or does the plan assume customers will appear?
- Which credible competitor or substitute wins today, and why?
- Which assumption would reverse the recommendation?
- Are costs, sales timing, founder effort, and execution complexity understated?
- Does the stated deadline fit the actual sales, delivery, and cash cycle?
- What legal, platform, or operational blocker is ignored?
- Are kill criteria strong enough to prevent continued effort after evidence turns negative?
- Does the plan distinguish mathematical possibility, researched plausibility, and actual validation?

### Critical failures

Examples include mathematically inconsistent economics, no credible customer pain or distribution path, unsupported willingness-to-pay claims, a deadline incompatible with the sales or delivery cycle, missing decisive constraints, ignored legal or operational blockers, researched plausibility mislabeled as validation, a recommendation that does not follow from the evidence, or no viable validation and kill plan.

## 8. Data and spreadsheets

### Core dimensions

- source data integrity
- formula and calculation correctness
- methodology
- completeness
- reproducibility
- consistency
- edge-case handling
- auditability and traceability
- clarity of layout and labels
- visualization quality
- decision usefulness
- update and maintenance behavior

### Strong success criteria

Derive criteria such as:

- inputs, transformations, assumptions, and outputs are distinguishable
- formulas use correct ranges, references, units, signs, dates, and aggregation logic
- totals reconcile and key figures can be independently reproduced
- blanks, errors, duplicates, outliers, and boundary cases are handled deliberately
- repeated logic is consistent and maintainable
- charts encode the data honestly and answer a decision-relevant question
- the workbook remains understandable to a new reviewer

### Validation options

- inspect formulas and compare patterns across ranges
- calculate independent spot checks and reconciliations
- test boundary values, missing values, duplicates, date transitions, and sign conventions
- trace precedents and dependents for critical outputs
- verify data types, units, filters, named ranges, tables, and references
- refresh or recalculate where tools permit
- inspect charts for scale, labeling, aggregation, and misleading encodings
- compare outputs with source data or a known result

### Critic focus

Ask:

- Which number cannot be traced back to a source or assumption?
- Where could a copied formula silently drift?
- What happens when data volume, dates, or categories change?
- Are units and signs consistent?
- Does the visualization clarify or distort?
- Can another person reproduce the result?

### Critical failures

Examples include incorrect key formulas, broken references, unreconciled totals, hidden assumptions that materially change the result, data leakage, non-reproducible methodology, or a chart that misrepresents the decision-critical data.

## 9. Visual and creative work

Use this archetype for generated images, branding, illustration, art direction, visual campaigns, and creative artifacts where emotional or aesthetic effect is central. Combine it with WEB/UI/UX or WRITING when the output also has functional or narrative requirements.

### Core dimensions

- concept fit
- composition
- hierarchy and focal control
- style consistency
- color, value, and contrast relationships
- typography when present
- subject and reference accuracy
- technical artifacts
- originality and specificity
- production quality
- reference fidelity where required
- intended emotional effect

### Strong success criteria

Derive criteria such as:

- the concept clearly serves the stated message and audience
- composition directs attention intentionally
- style, lighting, perspective, anatomy, materials, and detail are internally coherent as relevant
- text is legible and correctly rendered when required
- no obvious generation artifacts, accidental tangencies, broken geometry, or unfinished areas remain
- resemblance and reference fidelity are sufficient when specifically requested
- output dimensions, crop, transparency, and technical format meet the use case

### Validation options

- inspect the actual image or rendered artifact at full view and useful zoom levels
- compare against supplied references on composition, style, subject, and technical requirements
- inspect edges, hands, faces, text, repeated patterns, geometry, lighting, and perspective where relevant
- test crop and readability in the intended placement
- compare three concept or composition directions for the highest-leverage decision
- check export dimensions, aspect ratio, transparency, and file integrity

### Critic focus

Ask:

- Does the concept communicate before explanation?
- What looks generic, synthetic, or inconsistent?
- Where does the eye go unintentionally?
- Which artifact would a viewer notice immediately?
- Is the emotional effect aligned with the brief?
- Where does the candidate lose against the supplied reference without a deliberate reason?

### Critical failures

Examples include wrong subject, unusable composition, major visual artifacts, illegible required text, failure to match a required identity or reference, incorrect technical format, or an image that communicates the wrong message.

## 10. General tasks

Use only when no specialized archetype dominates.

### Core dimensions

- correctness
- completeness
- usability
- consistency
- constraint adherence
- clarity
- quality of execution
- verification

Build a task-specific rubric by asking:

- What must be true for the result to work?
- What would make it unusable or misleading?
- What can be checked objectively?
- What would an experienced user notice immediately?
- What is the best available comparison target?
- What limitation would materially affect trust?

## 11. Hybrid-task integration

For hybrid tasks:

1. List the critical deliverables.
2. Assign each deliverable and must-pass criterion to one or more archetypes.
3. Deduplicate overlapping dimensions.
4. Identify cross-domain integration risks.
5. Choose one unified benchmark strategy where possible, plus specialized standards where necessary.
6. Run validation in an order that respects dependencies.
7. Make the judge consider the combined outcome, not isolated component scores.

Common integration risks:

- accurate research expressed through weak or misleading writing
- correct code wrapped in unusable UI
- visually polished slides containing unsupported analysis
- correct spreadsheet calculations presented with misleading charts
- strong strategy unsupported by feasible execution
- faithful design implementation with broken interactions

The final result passes only when the integrated deliverable works as a whole.
