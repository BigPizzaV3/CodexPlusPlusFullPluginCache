# Reviewer Separation and Adversarial Review

Use distinct review passes so creation and approval do not collapse into self-congratulation.

## Contents

1. Role model
2. Separation and iteration-evidence protocol
3. Domain critic
4. Adversarial critic
5. Downside and stress-test pass
6. Product and system second-order review
7. Verifier and evidence ledger
8. Judge
9. Competitive three-way challenge
10. Visual reviewer
11. Real delegation versus review passes
12. Review output discipline

## 1. Role model

Conceptually separate these roles:

### Planner

Define the outcome, constraints, success criteria, dependencies, risks, benchmark, and validation plan. Identify what evidence would justify stopping before the candidate exists.

### Builder

Create or modify the deliverable. Optimize for requirements coverage and a coherent complete result, not for defending every first choice.

### Domain critic

Evaluate the candidate using the task-specific rubric and professional standards. Look for defects an experienced practitioner would reject.

### Adversarial critic

Actively try to disprove readiness. Search for omissions, brittle assumptions, superficial compliance, generic work, contradictions, untested claims, failure modes, and benchmark losses.

### Verifier / QA

Perform objective checks that are actually possible and record evidence. Do not convert plausible behavior into a passed test.

### Judge

Decide whether the stop gates are supported. Require another targeted cycle or return an honest final decision.

## 2. Separation and iteration-evidence protocol

When true independent agents are unavailable, create separation through fresh sequential passes:

1. Finish the current build or modification pass.
2. Restate the success criteria and benchmark without using the builder's justifications as evidence.
3. Inspect the candidate from the domain-critic role.
4. Run a separate adversarial pass and record defects before proposing fixes.
5. Rank findings by severity, user impact, confidence, and leverage.
6. Select the highest-value material weakness.
7. Apply a targeted change when justified.
8. Re-run affected checks and relevant regressions.
9. Let the judge review requirements, evidence, open defects, benchmark gaps, and iteration cost.

For every non-trivial STRONG or GAUNTLET task, keep this compact internal record:

| Challenged weakness | Evidence and impact | Revision or no-change decision | Re-validation |
| --- | --- | --- | --- |
| [specific material weakness] | [what showed it and why it matters] | [targeted change, or why no change was justified] | [affected checks and result] |

The final answer may summarize this record, but must not expose private chain-of-thought or a full review transcript.

Fresh-pass discipline:

- evaluate the artifact, not the intention behind it
- require evidence for success claims
- prefer specific failure examples over vague unease
- identify what should be preserved as well as what should change
- do not let prior effort create resistance to replacement
- do not invent independence, defects, or revisions

## 3. Domain critic

Use the relevant archetype rubric. Answer:

- Which requirements are missing, weakly implemented, or only technically satisfied?
- What violates domain conventions or the supplied specification?
- What would an expert reject first?
- Which edge case or integration point is underdeveloped?
- What is confusing, generic, inconsistent, or unfinished?
- Which component is strong and should be preserved?
- What is the single highest-leverage domain improvement?

Use severity labels:

- **Critical** - invalidates the result or creates unacceptable harm
- **High** - likely to materially change the user's outcome
- **Medium** - meaningful but not outcome-determining
- **Low** - polish or preference

A domain critique is incomplete if it only produces a score or adjectives.

## 4. Adversarial critic

Assume another expert is trying to reject the result. Ask:

- Where would an expert say "this is not ready"?
- What looks generic, copied, templated, or predictable?
- What feels unfinished despite nominal requirements coverage?
- Which requirement was satisfied literally but not effectively?
- Which assumption has the weakest support and the largest consequence?
- What can break under realistic use, stress, ambiguity, or change?
- What important validation has not actually happened?
- What claim is stronger than the evidence?
- Where does the candidate lose most clearly against the benchmark or credible real alternatives?
- What would a real user notice or struggle with immediately?
- Which improvement now has the highest leverage?
- What new defect might the proposed fix introduce?
- For product or system changes: if this feature is added, which existing assumptions in the rest of the system stop being true?

For non-trivial STRONG and GAUNTLET work, the pass must conclude with one of two states:

1. **Material challenge found** - name the concrete weakness, evidence, likely impact, and highest-value response.
2. **No material revision justified** - still name the strongest observed challenge, then state why it is below the materiality threshold, already mitigated, or not responsibly changeable. This is valid only after a real review, not as a shortcut.

Adversarial rules:

- Do not spend review bandwidth on generic praise.
- Do not manufacture defects merely to force another cycle.
- Distinguish evidence-based defects from taste.
- Search for disconfirming evidence and alternate interpretations.
- Challenge both the artifact and the rubric if the rubric is too weak.
- Re-open a passed area only when new evidence or a change creates regression risk.

## 5. Downside and stress-test pass

Use for forecasts, economics, business models, planning, launch strategies, and other work where assumptions determine the outcome.

Protocol:

1. List the assumptions that drive the result.
2. Rank them by outcome sensitivity and evidentiary uncertainty.
3. Stress the top one to three with plausible downside cases, not arbitrary catastrophe.
4. Recalculate the economics or trace operational consequences.
5. Identify break-even thresholds, failure triggers, hidden effort, dependencies, or legal and competitive exposure.
6. Add a mitigation, contingency, validation test, or kill criterion.
7. Re-check the recommendation after the stress test.

Possible stresses include lower conversion or sales, higher acquisition or delivery cost, slower sales and payment cycles, refunds, founder-time constraints, dependency failure, regulatory uncertainty, missing distribution, or stronger competitor response.

Do not attack every assumption. Concentrate on those most likely to reverse the decision.

## 6. Product and system second-order review

Use for product, software, feature, API, and system-design tasks. Review the change as part of a living system rather than in isolation.

Ask the core question:

> If we add this feature, which existing assumptions in the rest of the system stop being true?

Inspect only components that plausibly exist or are evidenced in the supplied context. Common areas include analytics, statistics, rankings, search, filtering, caching, reports, exports, notifications, scheduled jobs, recommendations, authorization, onboarding, history, billing, moderation, imports, APIs, and integrations.

For every material effect, record:

- the previous assumption
- why the new behavior invalidates or qualifies it
- the likely failure, contamination, or user impact
- the safeguard, migration, new data dimension, filter, observability, or regression test needed

Classify each reviewed assumption as invalidated, conditionally true, unaffected, or unknown. Do not invent nonexistent subsystems merely to fill a checklist. Unknown material dependencies should become explicit limitations or clarification targets.

Use the highest-impact second-order effect as an adversarial finding when it materially changes the design. Re-check affected downstream behavior after revision when an implementation exists; otherwise convert the safeguard into proposed acceptance criteria and label runtime validation as not run.

## 7. Verifier and evidence ledger

Map important claims to actual checks.

Use this internal structure:

| Requirement or claim | Check performed | Evidence | Status | Limitation |
| --- | --- | --- | --- | --- |
| [critical behavior] | [test, inspection, calculation, source check] | [concise result] | PASSED / FAILED / NOT RUN / UNAVAILABLE | [only if material] |

For changed areas, add a compact before/after record:

| Finding | Change | Re-check | Result |
| --- | --- | --- | --- |
| [material weakness] | [targeted revision] | [affected check or regression] | [passed, failed, not run, unavailable] |

Verification principles:

- The check must be capable of detecting the relevant failure.
- A check that never ran cannot pass.
- A passing narrow check does not prove broader behavior.
- Re-run affected checks after changes.
- Add regression checks when a fix could damage adjacent behavior.
- Treat acceptance criteria, proposed schemas, API designs, and migration plans as unexecuted until they are tested against a real implementation.
- State tool, access, or input limitations precisely.

Examples of false verification to avoid:

- "The code looks correct, so tests pass."
- "The HTML is clean, so the design looks polished."
- "The sources are reputable, so every citation is accurate."
- "The spreadsheet opened, so the formulas are correct."
- "The file was generated, so its page layout is good."
- "Three options were generated, so market benchmarking occurred."

## 8. Judge

Review:

- requirements coverage
- defect severity and unresolved issues
- validation and re-validation evidence
- benchmark comparison
- adversarial finding and resulting revision or no-change justification
- stress-test results where relevant
- for qualifying feature work, implementation readiness, domain boundary, second-order effects, and acceptance-criteria status
- regressions after improvement
- current cycle and remaining budget
- expected value of another cycle

During iteration, choose **TARGETED LOOP** when a material deficiency remains and a specific improvement has meaningful expected value. Name the weakest area and route back to the relevant stage; do not restart everything.

When finalizing, choose exactly one:

### PASS

Use when critical requirements are satisfied, important checks were completed, no material avoidable weakness remains, and the evidence supports the requested claim.

### PASS WITH LIMITATIONS

Use when the result is strong and usable, but one or more material points could not actually be validated and the missing evidence is not likely to overturn the core result. Name the consequence. Do not use this for trivial caveats, minor preferences, or negligible uncertainty. If the missing evidence could overturn the primary recommendation or readiness claim, use BAR NOT REACHED.

### BAR NOT REACHED

Use when a material deficiency remains that prevents claiming the requested quality level, even if the best achieved result is still useful.

The judge must not use a round number, a self-assigned score, fatigue, or a polished appearance as the sole reason to stop.

## 9. Competitive three-way challenge

Use in full GAUNTLET mode only where alternatives can improve the most important decision. For foundational choices, run it before committing to the main build direction; for repair choices, run it after critique.

### Select the challenge target

Choose one component with:

- high impact on the user's outcome
- real uncertainty or multiple plausible approaches
- a meaningful benchmark gap or first-answer anchoring risk
- a manageable comparison cost

Examples:

- three viable architectures
- three credible layout or composition directions
- three materially different treatments of a weak section
- three repairs for the highest-severity defect
- three research interpretations
- three realistic monetization, delivery, or distribution models
- three formulas or modeling approaches
- three implementations of a critical interaction

### Establish a viability floor

Before generating options, define the hard constraints and minimum viability conditions. Every option must plausibly satisfy them. Reject an option before comparison if it violates a hard constraint or lacks a credible path to the objective.

### Generate competitive alternatives

Make the options materially distinct in governing strategy, not merely wording, color, or packaging. Give each enough detail to compete fairly. Do not construct one polished favorite and two weak decoys.

For every option, identify:

- strongest advantage
- important disadvantage
- key dependency or assumption
- validation burden
- likely failure mode

### Evaluate consistently

Use the same criteria, evidence, assumptions, and time horizon for all three. For feature architecture, include domain correctness, complexity, implementation cost, UX, data integrity, migration impact, operational burden, maintainability, plausible future requirements, risk of under-modeling, and risk of premature generalization. A domain-specific abstraction may be a strong option, but never preselect it as the winner. When feasible:

- label options neutrally
- assess before deciding which is preferred
- avoid rewarding the first option for familiarity
- compare trade-offs, downside behavior, and implementation burden
- allow the result that none passes

### Select, synthesize, or reject

Choose the strongest option, combine compatible strengths, or reject all three and revisit the framing. Record why the selected direction wins on the rubric and what disadvantage remains.

### Keep alternatives separate from benchmarks

The three options are candidate alternatives. They are not an authoritative standard, market benchmark, competitor set, or external validation. Compare the selected candidate against the real benchmark separately.

### Skip wasteful variants

Do not create three full versions of a large deliverable unless the user requests alternatives or the architecture genuinely requires competing prototypes. Do not run the challenge on a trivial component merely to satisfy a ritual.

## 10. Visual reviewer

Use a separate visual review for websites, UI, dashboards, presentations, documents with meaningful layout, branding, generated images, and other visual outputs.

### Evidence requirement

Inspect the rendered or visible artifact whenever tools permit. Source code, slide XML, document structure, or a prompt alone cannot validate visual quality.

If actual inspection is unavailable, state:

- what was inspected instead
- which visual properties remain unvalidated
- what render, screenshot, device, viewport, or application check would be needed

### Review dimensions

Inspect at least the applicable dimensions:

- composition
- visual hierarchy
- spacing and rhythm
- typography
- alignment
- consistency
- density and scanability
- contrast and legibility
- responsiveness or page-size behavior
- interaction and state feedback
- image quality and artifacts
- obvious unfinished states
- fidelity to the supplied reference
- benchmark gap in perceived polish

### Visual critic questions

- Where does the eye go first, and is that intentional?
- What looks misaligned, crowded, empty, inconsistent, or accidental?
- Which type size, line length, spacing, or density harms comprehension?
- What breaks at different viewport or page sizes?
- Which component looks like a placeholder?
- What does the benchmark handle more convincingly?
- Is the issue visible in the render or only inferred from source?

### Re-test

After visual changes, re-render and inspect the affected views. Check for regressions in neighboring layouts, pagination, clipping, overflow, and responsive behavior.

## 11. Real delegation versus review passes

Use real delegation only when the current environment exposes it and it materially improves quality.

When real delegation is available:

- give each delegate a bounded role, rubric, inputs, and expected output
- avoid redundant agents that repeat the same review
- reconcile disagreements using evidence and the judge's criteria
- preserve an auditable summary of what was actually delegated

When real delegation is unavailable:

- use the sequential separation protocol
- call the work "review passes," not "agents" or "sub-agents"
- do not fabricate independent opinions, identities, or execution logs

The value comes from role separation and adversarial standards, not from pretending parallelism exists.

## 12. Review output discipline

Keep internal review detailed enough to guide improvement, but keep user-facing narration proportional.

For non-trivial RUN or AUDIT + IMPROVE work, a compact verdict may expose only:

- **Validated** - checks actually performed
- **Challenged** - the strongest observed challenge and its impact; if no revision was justified, include why it was below the materiality threshold
- **Improved** - what materially changed and was re-checked, or that no change was warranted
- **Benchmark** - the real reference, authoritative standard, researched comparator, or derived rubric
- **Remaining gap** - material unvalidated or weaker areas
- **Decision** - PASS / PASS WITH LIMITATIONS / BAR NOT REACHED

For AUDIT-only mode, expose prioritized findings with evidence and actionable fixes.

Do not expose private chain-of-thought, simulated debate transcripts, every discarded alternative, or repetitive iteration logs. Share conclusions and evidence, not hidden deliberation.
