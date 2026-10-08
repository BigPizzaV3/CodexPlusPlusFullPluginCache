# Output Patterns

Use these patterns to keep Gauntlet useful to ordinary users while preserving rigorous execution.

## Contents

1. BUILD mode rules
2. Copy-paste Gauntlet prompt template
3. RUN mode final output
4. AUDIT mode final output
5. Verdict language
6. Limitation language
7. Process narration to omit

## 1. BUILD mode rules

A BUILD response must produce a prompt that works in a fresh ChatGPT conversation without hidden Gauntlet context.

Before writing the prompt:

- restate the user's task faithfully
- preserve supplied requirements, constraints, formats, references, and quality expectations
- identify files, images, URLs, or source material the fresh conversation must receive
- infer relevant archetypes, reviewers, tests, benchmark strategy, intensity, and stop gates
- replace generic quality words with task-specific criteria
- make tool use conditional on actual availability
- prevent false claims of tests, rendering, research, delegation, or compliance
- set a finite cycle cap and allow earlier stopping
- prioritize the final deliverable over workflow narration
- require adversarial iteration evidence for non-trivial STRONG and GAUNTLET work without exposing chain-of-thought
- keep candidate alternatives separate from real benchmarks
- add focused downside stress testing for forecasts, economics, business models, planning, and strategy
- for qualifying product or software feature work, encode a conditional implementation translation after the main direction is selected, scaled to the task
- omit implementation-specific stages and instructions entirely when they are irrelevant rather than retaining generic boilerplate

When the user's intent is clearly copy-paste use, return only the prompt, normally in one fenced block. Do not add an introduction, explanation, or offer after it.

Customize the template below. Do not leave bracketed placeholders that can be filled from the current request. When required source material cannot be embedded, name exactly what the user must attach or paste in the fresh conversation.

## 2. Copy-paste Gauntlet prompt template

Use all thirteen numbered sections unless a section is genuinely inapplicable. Tailor the content to the task rather than copying generic examples.

```text
You are to complete the task below using a rigorous Gauntlet quality-control workflow. The goal is not to produce a long explanation of your process. The goal is to create the strongest defensible deliverable available in the current environment, challenge it, improve it, and verify it honestly.

# 1. THE TASK

[Write the complete task in direct, unambiguous language. Include the required deliverable and what "done" means.]

# 2. CONTEXT & CONSTRAINTS

[Include all relevant audience, purpose, scope, format, tone, technical, legal, policy, time, brand, data, compatibility, and tool constraints. List supplied inputs and references. State what must not be changed or invented. If files or links are required, name them explicitly.]

Work within the capabilities actually available in this conversation. Respect all higher-priority instructions, safety rules, privacy, permissions, and tool restrictions. Never invent access, tools, test results, sources, visual inspection, or agent activity.

# 3. SUCCESS DEFINITION

Translate vague expectations into observable task-specific criteria. At minimum, the final result must satisfy these must-pass conditions:

[Insert tailored critical requirements.]

Evaluate these quality dimensions where applicable:

[Insert the tailored domain dimensions for this task.]

Separate must-pass criteria from optional polish. Do not declare success from a self-assigned score alone.

# 4. THE BUILD METHOD

Use this sequence as an operational workflow:

UNDERSTAND -> DEFINE SUCCESS -> CLASSIFY -> DECOMPOSE -> SET BENCHMARK AND TEST PLAN -> BUILD OR INSPECT -> VALIDATE -> DOMAIN CRITIQUE -> ADVERSARIAL CRITIQUE -> BENCHMARK COMPARISON -> THREE-WAY CHALLENGE WHERE USEFUL -> TRANSLATE SELECTED PRODUCT OR FEATURE DIRECTIONS INTO IMPLEMENTATION WHEN USEFUL -> IMPROVE -> RE-VALIDATE -> JUDGE -> LOOP OR FINISH

Each stage must serve a distinct purpose. Omit the conditional implementation stage when this is not a product, software, feature, API, or system-design task. Do not stop after planning when the deliverable can be completed now. Ask only the smallest number of questions whose answers would materially change the solution or avoid significant risk; otherwise state reasonable assumptions and proceed. Perform available checks directly rather than assigning them to the user. Complete the work in the current response and never promise background or asynchronous continuation.

Use [QUICK / STRONG / GAUNTLET] intensity with a maximum of [1 / 3 / 5] improvement cycles. Stop earlier when the evidence-based gates pass. The cycle limit is a cap, not a target.

For non-trivial STRONG and GAUNTLET work, do not finalize the first candidate. Run at least one fresh adversarial review pass and name the strongest observed challenge. If it is material, make a targeted improvement and re-validate it. If no material revision is justified, explain why the challenge is below the materiality threshold, already mitigated, or not responsibly changeable. Never invent an improvement.

# 5. DECOMPOSITION

Break the task into meaningful workstreams. Identify:

- dependencies and required order
- independent components
- high-risk or high-uncertainty components
- integration points
- for product or system changes, existing assumptions and downstream systems that the change may invalidate
- components requiring specialist, factual, technical, or visual review

Keep the decomposition proportional. Do not fragment trivial work.

# 6. REVIEWERS

Conceptually separate these roles:

- PLANNER: defines approach, risks, success criteria, benchmark, and validation plan
- BUILDER: creates or modifies the deliverable
- DOMAIN CRITIC: reviews against the task-specific professional rubric
- ADVERSARIAL CRITIC: searches for omissions, superficial compliance, brittle assumptions, generic output, contradictions, untested claims, and failure modes
- VERIFIER / QA: performs objective checks that are actually possible
- JUDGE: applies the stop gates and decides whether another targeted cycle has meaningful value

If genuine delegation or sub-agent functionality exists and materially helps, use it with bounded roles. Otherwise use fresh sequential review passes. Never fabricate independent agents or their results.

The critic should focus on:

[Insert task-specific harsh review questions and likely failure modes.]

Praise should consume review bandwidth only when it identifies something that should remain unchanged.

# 7. VALIDATION / TESTING

Before claiming success, perform the strongest relevant checks available for this task:

[Insert task-specific tests, inspections, calculations, source checks, render checks, compatibility checks, or file validation.]

Track each important check as:

- PASSED: actually performed and met the condition
- FAILED: actually performed and found a defect
- NOT RUN: feasible but not performed
- UNAVAILABLE: required tool, access, input, or environment was absent

Distinguish created from tested, tested from passed, and plausible from verified. Re-run affected checks after every material change and add regression checks where needed.

For forecasts, economics, business models, planning, or strategy, identify the assumptions with the largest effect on the outcome. Stress the top one to three with plausible downside values or failure conditions, recalculate or trace the consequences, identify breakpoints, and add mitigations, validation tests, or kill criteria. Do not attack every assumption randomly.

For visual outputs, inspect the rendered or visible result whenever possible. Source code or document structure alone is not visual validation. If rendering is unavailable, state exactly what remains unvalidated.

For product, software, feature, API, or system-design tasks where implementation detail materially improves the result, translate the selected direction into only the relevant implementation dimensions: domain boundary, entities, states, invariants, time or conflict semantics, trust or permissions, user-visible states, second-order effects, API or data implications, migration, and observable acceptance criteria. Prefer the smallest domain-correct abstraction over a generic engine. Do not output every category mechanically. Acceptance criteria and proposed tests are not executed validation.

# 8. BENCHMARK

Keep candidate alternatives and benchmarks separate. Internally generated options are candidates, not external validation.

Use this benchmark priority:

1. user-supplied real reference
2. applicable authoritative standard or established project convention
3. researched current real-world competitors or examples when tools are available and comparison is useful
4. a clearly labeled task-specific derived professional rubric

For this task, use:

[Name the primary benchmark, any secondary standard, or the exact derived-rubric strategy.]

For market, product, business, research, design, and strategy tasks, prefer credible real-world comparators where tools permit. When a real reference exists, compare the selected candidate side by side on the critical dimensions. Ask where the candidate loses against credible real alternatives and whether each difference matters to the user's outcome. Do not claim a comparison occurred if the reference was inaccessible. Do not copy protected expression merely to imitate a benchmark.

# 9. THE GAUNTLET LOOP

After the first complete candidate:

1. validate objective requirements
2. run a fresh domain-critic pass
3. run a fresh adversarial-critic pass
4. compare against the real benchmark
5. rank defects by severity and user impact
6. identify the single highest-leverage weakness
7. improve that weakness while preserving strong components
8. re-run affected validation and regression checks
9. retain a compact internal link: challenged weakness -> change or no-change decision -> re-validation result
10. let the judge apply the stop gates
11. repeat only when another cycle has meaningful expected value

At full GAUNTLET intensity, use a selective three-way challenge on a high-leverage decision only when alternatives can materially improve quality. For foundational choices such as business model, architecture, or design direction, run it before committing to the main build direction; for repair choices, run it after critique. Define the same hard constraints and viability floor first. Generate three genuinely competitive, materially different options; do not create a polished favorite plus two decoys. Evaluate all three against the same criteria and evidence. State an important disadvantage, dependency, and failure mode for every option. Select, synthesize, or reject them. Then compare the selected direction against the real benchmark separately.

For feature architecture, compare viable domain-appropriate models on correctness, complexity, implementation cost, UX, data integrity, migration impact, maintainability, and plausible future requirements. Avoid both an under-modeled patch and premature platform building. After selecting the direction, run the conditional implementation translation before final judgment when the task calls for a buildable specification.

# 10. THE BAR TO HIT

The result must be:

[Insert tailored bar: requirements-complete, correct, usable, coherent, audience-appropriate, benchmark-competitive, validated as far as the environment permits, and free of known critical or high-severity defects.]

Avoid empty claims such as "world-class," "perfect," or "production-ready" unless the evidence and task context support the precise claim.

# 11. STOP CONDITIONS

Stop only when all applicable conditions are satisfied:

- every critical requirement and required deliverable is addressed
- zero known critical defects remain
- zero unresolved high-severity defects remain unless explicitly accepted
- all realistically available critical checks were performed and passed, or material limitations are disclosed
- for qualifying feature work, the domain boundary, critical implementation semantics, second-order effects, and observable acceptance criteria are addressed at the requested depth without unsupported stack detail
- relevant outcome-driving assumptions were stress-tested
- candidate alternatives were not mislabeled as external benchmarks
- no material avoidable gap remains against the benchmark on critical dimensions
- for non-trivial STRONG and GAUNTLET work, an adversarial pass named the strongest observed challenge and its highest-value material finding was addressed and re-validated, or the no-revision threshold was explicitly justified
- the adversarial critic finds no remaining issue likely to materially change the user's outcome
- another cycle is unlikely to create meaningful improvement relative to cost and risk

Optional scoring may help diagnose quality but may not be the sole reason to stop.

The final decision must be exactly one of:

- PASS: critical requirements satisfied, important checks completed, no material avoidable weakness remains
- PASS WITH LIMITATIONS: strong and usable, but one or more material points could not actually be validated and the missing evidence is not likely to overturn the core result
- BAR NOT REACHED: a material deficiency remains

Do not use PASS WITH LIMITATIONS for trivial caveats. If the missing evidence could overturn the core recommendation, readiness claim, or primary outcome, use BAR NOT REACHED.

# 12. FAILURE / LIMITATION HANDLING

If the cycle cap is reached without passing, do not falsely declare victory. Return the best achieved deliverable and state:

- which material gaps remain
- their likely impact
- why they remain
- which input, tool, access, expertise, or decision would be needed to close them

If a validation step cannot be performed, mark it NOT RUN or UNAVAILABLE rather than implying it passed.

# 13. FINAL VERIFICATION

Before responding:

- confirm every required deliverable is present and in the requested format
- confirm critical requirements are traceable to the result
- confirm all success claims match actual evidence
- confirm the strongest observed challenge is recorded and the highest-value material finding caused a targeted change, or that the no-revision threshold is explicitly justified
- confirm affected checks were re-run after the last change
- confirm benchmark claims are accurate and appropriately limited
- confirm proposed acceptance criteria, schemas, APIs, migrations, and UI states are not described as implemented or tested unless those checks actually occurred
- confirm no hidden placeholder, unfinished state, unsupported assertion, or known critical defect remains
- confirm the response prioritizes the actual deliverable and does not expose private chain-of-thought or repetitive reviewer transcripts

# FINAL RESPONSE

Return the actual deliverable first in the requested format.

For non-trivial STRONG and GAUNTLET work, normally append a concise "Gauntlet Verdict" unless it would harm the requested format. Include only:

- Validated: checks actually performed
- Challenged: the strongest observed challenge; if no revision was justified, why it was below the materiality threshold
- Improved: the material change and re-check, or that no change was warranted
- Benchmark: the real reference, authoritative standard, researched comparator, or derived rubric
- Remaining gap: material unvalidated or weaker areas
- Decision: PASS / PASS WITH LIMITATIONS / BAR NOT REACHED

Never fabricate an improvement. Do not narrate every loop, role, discarded option, or private deliberation.
```

### Tailoring requirements

The generated prompt must replace the bracketed sections with specifics. It should normally name:

- the intended audience and use case
- the exact deliverable format
- the task's primary and secondary archetypes
- critical success criteria
- likely failure modes
- validation checks
- benchmark or derived rubric
- intensity and cycle cap
- conditional implementation translation and second-order review when the task is a product or software feature
- output structure

For a simple explicit Gauntlet, shorten the prompt while preserving the quality loop. Do not force all thirteen headings into a tiny two-sentence task if a compact self-contained version is more useful.

## 3. RUN mode final output

Put the deliverable first. Use the user's requested format exactly when possible.

For non-trivial STRONG and GAUNTLET work, normally use this compact evidence pattern:

```markdown
[ACTUAL DELIVERABLE]

## Gauntlet Verdict

**Validated:** [Only checks actually performed, including important re-checks.]

**Challenged:** [The strongest observed challenge and why it matters. If no material revision was justified, explain why it was below the materiality threshold, already mitigated, or not responsibly changeable.]

**Improved:** [What materially changed because of the review and what was re-checked, or "No material change made" when warranted.]

**Benchmark:** [The actual user reference, authoritative standard, researched real-world comparator, or "derived professional rubric." Keep internally generated alternatives separate.]

**Remaining gap:** [Material unvalidated or weaker area, or "None known within the checks performed."]

**Decision:** [PASS / PASS WITH LIMITATIONS / BAR NOT REACHED]
```

The verdict remains optional for tiny results, formats that prohibit appendices, or cases where it would add no trust value. Do not omit it merely to hide that no real iteration occurred.

For generated files or artifacts, deliver the file link or artifact first, then the concise verdict when appropriate.

## 4. AUDIT mode final output

### Audit only

Use:

```markdown
# Gauntlet Audit

## Verdict
[One concise statement of readiness or the most important conclusion, calibrated to evidence.]

## Material findings

### [Severity] - [Finding]
**Evidence:** [Specific observed issue.]
**Impact:** [Why it matters to the user's outcome.]
**Fix:** [Actionable repair.]

[Repeat only for material findings, ordered by severity and leverage.]

## Validation status
[What was checked, what passed, and what remains unvalidated.]

## Benchmark
[What was used and where the candidate loses or deliberately differs.]
```

Do not bury critical findings beneath general praise.

### Audit and improve

Use:

```markdown
[IMPROVED DELIVERABLE]

## Material improvements
- [Highest-value change and why it matters]
- [Second material change]
- [Third material change, if needed]

## Gauntlet Verdict
**Validated:** [Actual checks and re-checks.]
**Challenged:** [Strongest observed challenge and its impact; if no revision was justified, explain the materiality threshold.]
**Improved:** [Material change caused by the review, or no change warranted.]
**Benchmark:** [Actual benchmark and comparison scope; keep candidate alternatives separate.]
**Remaining gap:** [Material limits only.]
**Decision:** [PASS / PASS WITH LIMITATIONS / BAR NOT REACHED]
```

Preserve strong components. Do not list cosmetic edits as material improvements.

## 5. Verdict language

Use evidence-calibrated language.

### PASS

- "Decision: PASS. Critical requirements were met, the important available checks passed, and no material avoidable weakness remains within the tested scope."

### PASS WITH LIMITATIONS

- "Decision: PASS WITH LIMITATIONS. The result is strong and usable, but [material point] could not be validated, so [specific consequence]."

Do not use PASS WITH LIMITATIONS for minor preferences or negligible uncertainty. If the missing evidence could overturn the core result, use BAR NOT REACHED.

### BAR NOT REACHED

- "Decision: BAR NOT REACHED. The best achieved result still has this material gap: [gap]. It remains because [reason]."

### Iteration evidence

- "Challenged: the adversarial pass found [specific weakness and impact]."
- "Improved: [specific change] was made, then [affected check] was re-run."
- "The strongest challenge was [issue], but no material revision was justified because [threshold, mitigation, or constraint]; no change was fabricated."

### Strong validation evidence

- "The critical paths passed the executed test suite."
- "The rendered desktop and mobile views were inspected against the supplied screenshots."
- "The key formulas were independently recalculated and reconciled."
- "Central claims were checked against the cited primary sources."

### Partial evidence

- "The source structure passed static review; runtime behavior was not validated."
- "The document rendered successfully, but print output was not tested on a physical device."
- "The analysis is supported by current market evidence; actual sales validation was not available."

### Derived benchmark

- "Benchmark: a derived professional rubric based on the stated audience, constraints, and domain failure modes; no inspectable external reference was available."

Avoid unsupported phrases:

- flawless
- objectively perfect
- fully validated
- pixel-perfect
- production-ready
- industry-leading
- guaranteed
- market validated

Use them only when the exact scope and evidence make the claim defensible.

## 6. Limitation language

Name the missing evidence and its consequence.

Good:

- "Visual validation is incomplete because no rendered UI was available; spacing, typography, and responsive behavior were not inspected."
- "The code was reviewed and type-checked, but the external service integration could not be exercised without credentials."
- "Current demand signals were researched, but no first-party customer interviews or sales data were available."
- "The spreadsheet formulas were inspected, but recalculation in the target spreadsheet application was unavailable."

Weak:

- "Some limitations may remain."
- "Looks good but should be tested."
- "Probably works."

## 7. Process narration to omit

Do not expose:

- private chain-of-thought
- complete role-play conversations between reviewers
- repetitive iteration logs
- every rejected alternative
- self-congratulatory scores
- lengthy descriptions of obvious steps
- claims of independent agents when only sequential passes were used

Expose the deliverable, material findings, evidence, benchmark, and limitations.
