---
name: gauntlet
description: 'Turn requests that invoke Gauntlet as a quality-control workflow into rigorous, proportionate build-test-critique-benchmark-improve processes for arbitrary non-trivial tasks. Use when the user commands "Gauntlet this," "Run the Gauntlet," "Build a Gauntlet," requests a "Gauntlet prompt," asks to "Audit this with Gauntlet," or unmistakably requests an adversarial iterative quality-control loop. Support three modes: BUILD a self-contained copy-paste prompt, RUN the underlying task, or AUDIT/IMPROVE existing work. Adapt tests, critics, real benchmarks, stress tests, iteration evidence, conditional implementation translation, and stop gates across software, design, research, writing, strategy, data, visual, and mixed work. For qualifying product and software feature work, translate selected decisions into implementation-ready behavior without forcing a full specification. Do not trigger for ordinary quality requests or for literal, historical, or titled gauntlets unrelated to this methodology.'
---

# Gauntlet

Apply maximum useful rigor with minimum unnecessary process. Prioritize the user's actual deliverable, not narration about the method.

## Route the request

Choose exactly one primary mode before working:

1. **BUILD** - The user asks for a prompt, template, or reusable Gauntlet workflow to use elsewhere. Typical cues: "build me a Gauntlet prompt," "turn this into a Gauntlet," "make a copy-paste Gauntlet."
2. **AUDIT / IMPROVE** - The user supplies an existing candidate and asks to audit, critique, compare, repair, or improve it. Treat the supplied work as the baseline; do not rebuild from zero unless repair would be inferior or impossible.
3. **RUN** - The user invokes Gauntlet and wants the underlying task completed now. Typical cues: "Gauntlet this: create...", "use Gauntlet to build...", "run the Gauntlet on this task."

Routing precedence:

- A request for a **prompt/template/copy-paste workflow**, including "turn this into a Gauntlet," is BUILD.
- Otherwise, a supplied current result plus **audit/improve/critique** intent is AUDIT / IMPROVE.
- A supplied candidate plus "Gauntlet this" normally implies AUDIT / IMPROVE even when the user does not say "audit," unless they clearly ask for a replacement or new build.
- Otherwise, explicit Gauntlet execution is RUN.
- The word "build" alone does not imply BUILD mode. "Use Gauntlet to build a landing page" is RUN.
- If the user asks only for an audit, report prioritized findings and fixes without silently rewriting. If the user asks to improve, apply the improvements.

## Choose intensity

Infer the lightest intensity that can credibly meet the request:

- **QUICK** - Build or inspect, run one focused challenge, improve the weakest point, and verify. Maximum 1 improvement cycle.
- **STRONG** - Plan, build or inspect, validate, run a fresh domain and adversarial review, improve the highest-value weakness, re-validate, and judge. Maximum 3 improvement cycles.
- **GAUNTLET** - Define a real benchmark strategy, decompose, build or inspect, validate, run domain and adversarial critics, compare against the benchmark, stress outcome-driving assumptions where relevant, run a selective competitive three-way challenge, improve, re-validate, judge, and repeat when justified. Maximum 5 improvement cycles.

An explicit use of "Gauntlet" defaults to GAUNTLET intensity. Scale the ceremony down for a tiny task while preserving the core idea: define success, create or inspect, challenge the weakest point, improve, and verify. Never use the cycle cap as a target.

For any non-trivial STRONG or GAUNTLET task that can materially benefit from iteration, do not finalize the first candidate. Run at least one fresh adversarial pass before finalization. Name the strongest observed challenge. If it is material, apply the highest-value targeted revision and re-validate it. If no material revision is justified, explain why the strongest challenge is below the revision threshold, already mitigated, or not responsibly changeable. Never invent a weakness or improvement merely to prove that a loop occurred.

## Load only the references needed

- Read [references/core-loop.md](references/core-loop.md) for every RUN or AUDIT / IMPROVE request and when constructing a BUILD prompt.
- Read [references/archetypes.md](references/archetypes.md) to classify the task and select domain-specific quality dimensions, stress tests, and validation.
- Read [references/implementation-pass.md](references/implementation-pass.md) only for product, software, feature, API, or system-design work where translating the selected direction into implementation-ready behavior materially improves the requested result.
- Read [references/reviewers.md](references/reviewers.md) for critic separation, adversarial review, downside testing, second-order system review, visual review, or the three-way challenge.
- Read [references/benchmarks.md](references/benchmarks.md) whenever selecting, researching, deriving, or comparing against a benchmark.
- Read [references/output-patterns.md](references/output-patterns.md) for BUILD prompt construction and final response formats.
- Read [references/test-cases.md](references/test-cases.md) only when validating, maintaining, or regression-testing this skill.

Keep reference loading shallow. Do not load every file when the request only needs a subset.

## Maintain a private execution state

Track these items internally without exposing chain-of-thought or repetitive loop transcripts:

- intended outcome and audience
- deliverables, constraints, and non-goals
- observable success criteria
- task archetype or hybrid archetypes
- benchmark and why it is appropriate
- candidate alternatives, kept distinct from the benchmark
- validation plan and evidence status
- outcome-driving assumptions and stress-test results when relevant
- for qualifying feature work: domain boundary, selected implementation depth, invalidated system assumptions, and acceptance-criteria status
- known defects ranked by severity
- highest-leverage weakness
- iteration evidence: weakness challenged, revision made or no-change justification, and affected checks re-run
- cycle count, open stop gates, and final decision

Use concise user-facing updates only when the work is long enough that progress visibility is useful.

## Execute the core loop

Use each stage for a distinct purpose:

1. **UNDERSTAND** - Resolve the outcome, inputs, constraints, risks, and available validation. Ask only the smallest number of questions whose answers would materially change the result or avoid significant risk. Otherwise proceed.
2. **DEFINE SUCCESS** - Convert vague quality language into task-specific, observable criteria.
3. **CLASSIFY** - Select one or more archetypes and their relevant dimensions. Do not force a hybrid task into one category.
4. **DECOMPOSE** - Split meaningful workstreams; identify dependencies, high-risk areas, uncertainty, and components requiring specialized review.
5. **SET BENCHMARK AND TEST PLAN** - Choose the best honest comparison target and determine what can actually be validated. Keep internally generated candidate options separate from external or derived benchmarks.
6. **BUILD OR INSPECT** - Create the candidate, or inspect the supplied candidate in AUDIT / IMPROVE mode.
7. **VALIDATE** - Perform objective checks before claiming success. Record checks as passed, failed, not run, or unavailable. Stress the assumptions with the greatest outcome impact for forecasts, economics, business models, plans, and strategies.
8. **CRITIQUE** - Use fresh domain and adversarial passes. For non-trivial STRONG and GAUNTLET work, the adversarial pass must occur before finalization and produce a concrete material finding or an explicit no-material-change conclusion.
9. **COMPARE** - Ask where the candidate loses against the benchmark on critical dimensions. Do not call internally generated alternatives an external benchmark or claim a side-by-side comparison without a real reference.
10. **CHALLENGE IN THREES** - At GAUNTLET intensity, use three alternatives only where competition can materially improve quality. For foundational choices such as business model, architecture, or design direction, run the challenge before committing to the build direction; for repair choices, run it after critique. Make all three viable, materially different, subject to the same hard constraints, and competitive enough that none is a decoy. Evaluate each with the same rubric, include meaningful disadvantages for every option, then select, combine, or reject them.
11. **TRANSLATE TO IMPLEMENTATION WHEN USEFUL** - After selecting a product, software, feature, API, or system-design direction, use `references/implementation-pass.md` when the user asks how it should work or implementation semantics would materially improve the deliverable. Select only relevant dimensions. Establish the domain boundary, prefer the smallest domain-correct abstraction, capture critical entities, states, invariants, second-order effects, and observable acceptance criteria, and avoid unsupported stack detail. Treat acceptance criteria as proposed checks until executed.
12. **IMPROVE AND RE-VALIDATE** - Address the highest-value material weakness while preserving strong components. Link the revision to the finding that caused it, then re-run affected checks and relevant regressions. Re-check implementation semantics and downstream effects when the revision changes a feature or system model. If no revision is justified, record that honestly.
13. **JUDGE** - Apply the stop gates and choose PASS, PASS WITH LIMITATIONS, BAR NOT REACHED, or another targeted loop. Loop only when another cycle has meaningful expected value.

## Enforce honest validation

Distinguish:

- created from tested
- tested from passed
- plausible from verified
- mathematical possibility from market evidence and actual validation
- source inspection from rendered visual inspection
- candidate alternatives from benchmarks
- a derived professional rubric from an external benchmark
- proposed acceptance criteria from tests actually executed against an implementation

Use available tools, files, code execution, browser inspection, screenshots, calculations, citations, schemas, linters, compilers, or specialist skills when appropriate and actually available. Never invent a capability, test result, source check, visual inspection, benchmark comparison, iteration, improvement, or agent result.

For visual work, inspect the rendered or visible result whenever possible. Source code alone does not validate visual quality. If rendering or visual inspection is unavailable, mark visual validation as incomplete.

Use real delegation or sub-agents only when the environment actually provides them and delegation materially helps. Otherwise perform explicitly separated sequential review passes and describe them as passes, not agents.

## Apply stop gates and decide

Stop only when all applicable conditions are supported by evidence:

- all critical requirements and deliverables are addressed
- no known critical defect remains
- no unresolved high-severity defect remains unless the user explicitly accepts it
- all realistically available critical checks were performed and passed, or material limitations are disclosed
- for qualifying feature work, the selected direction is implementation-ready at the requested level: the domain boundary, critical semantics or invariants, important second-order effects, and observable acceptance criteria are addressed without unsupported stack detail
- no material avoidable gap remains against the chosen benchmark on critical dimensions
- for non-trivial STRONG and GAUNTLET work, an adversarial pass named the strongest observed challenge and its highest-value material finding was addressed and re-validated, or the no-revision threshold was explicitly justified
- the adversarial critic finds no remaining issue likely to materially change the user's outcome
- another iteration is unlikely to create meaningful value relative to its cost

Use one final decision:

- **PASS** - Critical requirements are satisfied, important checks were completed, and no material avoidable weakness remains.
- **PASS WITH LIMITATIONS** - The result is strong and usable, but one or more material points could not actually be validated. Do not use this for trivial caveats or when the missing evidence could overturn the core result; use BAR NOT REACHED in that case.
- **BAR NOT REACHED** - A material deficiency remains that prevents claiming the requested quality level.

Optional scores may diagnose weaknesses, but never use a self-assigned score as the sole stop reason. Translate demands for literal perfection or endless work into these defensible gates.

At the cycle cap, return the best achieved result and an honest gap report. Never declare victory when the evidence does not support it.

## Return the right output

### BUILD

Use [references/output-patterns.md](references/output-patterns.md). Return a polished, self-contained, copy-paste-ready prompt tailored to the task. Preserve the user's requirements, quality dimensions, validation plan, benchmark behavior, adversarial iteration evidence, stress testing where relevant, iteration cap, limitation handling, and final response expectations. For qualifying product or software feature tasks, encode a conditional implementation translation after the main direction is selected. Do not surround a clearly copy-oriented prompt with unnecessary commentary.

### RUN

Perform the underlying task. Put the actual deliverable first. Do not output a prompt instead of doing the work. For qualifying product or software feature tasks, continue from the selected direction into only the implementation dimensions that materially improve usefulness. Do not expose private reasoning, full critic transcripts, or repetitive loop history. For non-trivial STRONG and GAUNTLET work, normally add a compact **Gauntlet Verdict** unless the requested format would be harmed. Limit it to: **Validated**, **Challenged**, **Improved**, **Benchmark**, **Remaining gap**, and **Decision**. Report only real evidence. The Challenged field must name the strongest observed challenge. If no material revision was justified, explain that threshold decision instead of fabricating an improvement.

### AUDIT / IMPROVE

Use the supplied work as the current candidate. Identify material weaknesses before changing it. Target the highest-value deficiencies and preserve what already works. For product specifications or feature designs, inspect whether the selected direction is implementation-ready and repair only material gaps in domain semantics, states, invariants, downstream effects, migration, or acceptance criteria. For audit-only requests, provide prioritized findings and actionable fixes. For improvement requests, return the improved deliverable first, followed by a concise summary of material changes and an evidence-based verdict when useful.

## Non-negotiable rules

- Respect safety rules, privacy, permissions, tool restrictions, legal constraints, and all higher-priority instructions.
- Require no connector, backend, account, database, or external API; use only capabilities actually available in the current environment.
- Prefer action over questionnaires and do not repeatedly ask whether to continue.
- Perform checks directly when current tools allow; do not offload available validation to the user.
- Complete the work in the current response; never promise background or asynchronous continuation.
- Do not stop at a plan when the requested deliverable can be produced now.
- Do not overengineer simple tasks.
- Do not turn every product question into a technical specification; run or expand the implementation pass only when it materially improves the requested result.
- Treat the implementation pass as internal workflow; expose that label only when it usefully structures a substantial product or feature deliverable.
- Do not report proposed acceptance criteria, schemas, migrations, or API behavior as implemented or tested.
- Do not rewrite everything when a targeted fix is stronger.
- Do not praise at the expense of finding defects.
- Do not fabricate iterations, competitive alternatives, benchmark comparisons, or passed checks.
- Do not claim "world-class," "production-ready," "perfect," or equivalent without supporting evidence.
- Match the user's language and requested output format.
