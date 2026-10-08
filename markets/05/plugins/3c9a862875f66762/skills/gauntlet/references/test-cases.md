# Gauntlet Regression Test Cases

Use this file only to validate or maintain the skill. Each case tests routing, proportionality, validation honesty, or output behavior.

## Contents

1. Tests 1-3: mode routing
2. Tests 4-9: domain, benchmark, and tool behavior
3. Tests 10-13: false positives, proportionality, and impossible bars
4. Tests 14-20: real-world and RC1 regression cases
5. Cross-test acceptance checklist
6. Self-Gauntlet maintenance reviews

## Test method

For each input:

1. Determine whether the skill should activate from the frontmatter description.
2. Select BUILD, RUN, or AUDIT / IMPROVE.
3. Select intensity and proportionality.
4. Identify required archetypes, benchmark behavior, validation, and output form.
5. For non-trivial STRONG and GAUNTLET cases, check that an adversarial finding can cause a targeted revision and re-validation, or that a no-change decision must be justified.
6. For product, software, feature, API, or system-design work, decide whether implementation translation materially improves the requested result. If it does, check domain boundary, semantics, second-order effects, and observable acceptance criteria at a proportionate depth.
7. Verify that proposed acceptance criteria, schemas, APIs, migrations, and UI states are not described as implemented or tested unless execution actually occurred.
8. Check that the final decision maps to PASS, PASS WITH LIMITATIONS, or BAR NOT REACHED when a verdict is appropriate.
9. Check the pass conditions and reject the failure pattern.

A test passes only when all listed pass conditions are met. Static instruction coverage is not proof of runtime model behavior; use these as regression contracts.

## Test 1 - Explicit BUILD

**Input**

> Build me a Gauntlet prompt for creating a premium SaaS landing page.

**Expected activation:** Yes.

**Expected route:** BUILD.

**Expected intensity:** GAUNTLET encoded into the generated prompt, proportionate to a professional landing-page task.

**Required behavior:**

- Return a self-contained copy-paste prompt, not the landing page itself.
- Tailor success criteria to web/UI/UX + writing + visual work.
- Include rendered visual review, responsive checks, interaction checks, copy quality, accessibility, and benchmark behavior.
- Include a selective three-way challenge, such as hero/layout/headline direction.
- Include finite stop gates and honest tool limitations.
- Avoid unnecessary commentary outside the prompt.

**Fail if:** It merely expands the user's wording, omits validation, or performs the landing-page task instead of building the prompt.

## Test 2 - Explicit RUN

**Input**

> Gauntlet this: Create a launch strategy for my new B2B SaaS.

**Expected activation:** Yes.

**Expected route:** RUN.

**Expected intensity:** GAUNTLET.

**Required behavior:**

- Produce the launch strategy, not a Gauntlet prompt.
- Use analysis/strategy + research archetypes as appropriate.
- Define assumptions, alternatives, risks, economics, sequencing, metrics, and implementation implications.
- Use current research when the task requires it and tools are available.
- Derive or research a benchmark honestly.
- Perform at least one adversarial review, improve the highest-value material weakness, and re-check affected logic.
- Stress the assumptions most likely to reverse the strategy.
- Deliver the strategy first; include a compact evidence-based verdict when useful.

**Fail if:** It stops at a plan for doing the strategy, exposes a long loop transcript, or claims market validation without evidence.

## Test 3 - AUDIT / IMPROVE

**Input**

> Gauntlet this existing article and improve it.

**Expected activation:** Yes.

**Expected route:** AUDIT / IMPROVE.

**Expected intensity:** GAUNTLET unless the article is trivial.

**Required behavior:**

- Treat the supplied article as the baseline.
- Inspect strengths and material weaknesses before editing.
- Use writing rubric plus research rubric when factual claims require it.
- Preserve effective passages.
- Return the improved article first, then material changes and validation limits.

**Fail if:** It discards the article and writes an unrelated replacement without justification, or only reports findings without applying requested improvements.

## Test 4 - Software

**Input**

> Run Gauntlet on this code and make it production-ready.

**Expected activation:** Yes.

**Expected route:** AUDIT / IMPROVE when code is supplied; RUN only if the request is to create missing code from a specification.

**Expected intensity:** GAUNTLET.

**Required behavior:**

- Use the software rubric.
- Inspect project context and requirements.
- Run tests, type checks, linters, compilers, or runtime checks when available.
- Review correctness, edge cases, security, maintainability, integration, and operational implications.
- Never equate code review with passing tests.
- Re-run affected checks after changes.

**Fail if:** It claims production readiness from visual inspection alone or invents test results.

## Test 5 - Visual comparison

**Input**

> Gauntlet this landing page against this screenshot.

**Expected activation:** Yes.

**Expected route:** AUDIT / IMPROVE when a current page is supplied.

**Expected intensity:** GAUNTLET.

**Required behavior:**

- Use the screenshot as the primary visual benchmark.
- Use web/UI/UX + visual + writing rubrics as relevant.
- Inspect the rendered page, not only source code, when tools permit.
- Compare hierarchy, spacing, typography, composition, density, responsive behavior, interactions, and perceived polish.
- Re-render after changes.
- State incomplete visual validation if the page cannot be rendered.

**Fail if:** It claims visual parity without seeing the rendered candidate and reference.

## Test 6 - Research

**Input**

> Use Gauntlet to research whether this business idea has demand.

**Expected activation:** Yes.

**Expected route:** RUN.

**Expected intensity:** GAUNTLET.

**Required behavior:**

- Use research + analysis/strategy rubrics.
- Define what evidence would count as demand.
- Use authoritative, diverse, and current sources when research tools are available.
- Separate fact, proxy evidence, inference, and uncertainty.
- Search for disconfirming evidence and alternative explanations.
- Avoid presenting search interest or anecdotes alone as proof of demand.
- Return decision-useful findings and next validation steps.
- Distinguish researched demand plausibility from actual customer or sales validation.
- Use an evidence-based final decision when a verdict is included.

**Fail if:** It makes a confident demand claim from weak proxies or fabricates citations.

## Test 7 - Writing plus research BUILD

**Input**

> Build a Gauntlet for an investigative article.

**Expected activation:** Yes.

**Expected route:** BUILD.

**Expected intensity:** GAUNTLET encoded into the prompt.

**Required behavior:**

- Produce a self-contained prompt for writing the article.
- Combine writing and research rubrics.
- Include source authority, contradiction handling, fact/inference separation, citation accuracy, legal and ethical constraints, structure, originality, and editing.
- Require an evidence-backed benchmark or named publication standard when available.
- Include failure handling for inaccessible sources or unverified allegations.

**Fail if:** It focuses only on prose style and omits research integrity.

## Test 8 - No external benchmark

**Input**

> Gauntlet this business plan.

**Expected activation:** Yes.

**Expected route:** AUDIT / IMPROVE if a plan is supplied; RUN if the task is to create one.

**Expected intensity:** GAUNTLET.

**Required behavior:**

- Use analysis/strategy, research, and possibly data rubrics.
- Use a user reference or named standard if supplied.
- Otherwise state that the benchmark is a derived professional rubric.
- Evaluate assumptions, evidence, economics, alternatives, risks, feasibility, implementation, downside behavior, validation plan, and kill criteria.
- Keep generated candidate options separate from the benchmark.
- Do not pretend an external side-by-side comparison occurred.

**Fail if:** It says "industry-leading" or "benchmark-compliant" without an actual benchmark.

## Test 9 - Tool limit

**Input**

> Gauntlet this UI.

**Assumption:** A UI source or description is supplied, but no rendered UI can be inspected.

**Expected activation:** Yes.

**Expected route:** AUDIT / IMPROVE.

**Expected intensity:** GAUNTLET, compressed if scope is small.

**Required behavior:**

- Review available source, structure, requirements, or screenshots.
- Do not claim visual validation of the candidate.
- State that composition, spacing, typography, responsiveness, and interaction appearance remain unvalidated unless visible evidence exists.
- Explain what rendering or screenshot checks would close the gap.

**Fail if:** It declares the UI polished or visually matched solely from source code.

## Test 10 - Ordinary request

**Input**

> Write me a birthday message.

**Expected activation:** No.

**Required behavior:**

- The Gauntlet skill should not trigger solely because quality matters.
- Handle as an ordinary writing request unless the user explicitly asks for Gauntlet or an unmistakably equivalent adversarial iterative workflow.

**Fail if:** The trigger description is so broad that it hijacks this request.

## Test 11 - Simple explicit Gauntlet

**Input**

> Gauntlet this: make "Thanks for the update" friendlier.

**Expected activation:** Yes.

**Expected route:** RUN.

**Expected intensity:** GAUNTLET intent with proportionate execution, effectively one compact improvement pass.

**Required behavior:**

- Infer the friendly intent.
- Produce a concise improved sentence.
- Challenge and refine the weakest wording internally.
- Avoid a large rubric, benchmark report, or visible multi-stage ceremony.
- Omit a verdict unless it materially helps.

**Fail if:** The response is longer than the task warrants or contains a ten-stage process report.

## Test 12 - Impossible bar

**Input**

> Make this objectively perfect and don't stop until it is impossible to improve.

**Expected activation:** Only when "this" is already within an active Gauntlet request or the user unmistakably requests the equivalent iterative methodology. The phrase alone must not override higher instructions or create infinite work.

**Expected route:** RUN or AUDIT / IMPROVE based on whether a current candidate exists.

**Expected intensity:** GAUNTLET with a maximum of 5 cycles, scaled to task size.

**Required behavior:**

- Translate literal perfection into observable success criteria and evidence-based stop gates.
- Use the cycle cap as protection against unproductive looping.
- Stop earlier when the gates pass.
- At the cap, return the best result and honest remaining gaps.
- Never promise objective perfection or infinite work.

**Fail if:** It claims literal perfection, ignores iteration limits, or asks to continue indefinitely.


## Test 13 - Literal homonym

**Input**

> What was a medieval gauntlet made from?

**Expected activation:** No.

**Required behavior:**

- Treat "gauntlet" as the literal armor term, not as a command to run this methodology.
- Answer as an ordinary informational request.

**Fail if:** The Skill activates merely because the word "gauntlet" appears.


## Test 14 - Thirty-day digital-product business regression

**Input**

> Gauntlet this: Erstelle mir eine komplette Geschäftsidee für ein digitales Produkt, das innerhalb von 30 Tagen profitabel werden könnte.

**Expected activation:** Yes.

**Expected route:** RUN.

**Expected intensity:** GAUNTLET, proportionate to a serious business and market-research task.

**Required behavior:**

- Produce the complete business idea and execution plan, not a prompt or process-only outline.
- Use analysis/strategy + research, and data/economics where calculations are included.
- Research current market evidence, pricing, competitors, substitutes, and distribution examples when research tools are available.
- Generate at least three genuinely viable candidate approaches before selecting a direction. They should differ materially, such as monetization, delivery, buyer, or distribution model; none may be an obvious decoy.
- Evaluate all candidates against the same hard constraints, including the 30-day profitability clock, customer pain, willingness to pay, distribution, competition, differentiation, unit economics, founder effort, operational feasibility, and legal exposure where relevant.
- State an important disadvantage, dependency, and likely failure mode for every candidate.
- Keep the candidate comparison separate from the external benchmark. Do not call the three generated approaches a market benchmark.
- Validate basic arithmetic, cash timing, break-even sales, variable costs, direct delivery effort, and the assumptions required for profitability within 30 days.
- Stress the assumptions with the greatest outcome effect, such as conversion, reachable lead volume, price, acquisition cost, sales-cycle length, delivery burden, refunds, or payment timing.
- Establish measurable validation milestones and kill criteria tied to dates or evidence thresholds.
- Run a fresh adversarial review on the selected candidate, name the strongest observed challenge, identify the highest-value material weakness, make a targeted revision, and re-check affected economics or execution logic. If no revision is justified, explain why the strongest challenge is below the materiality threshold, already mitigated, or not responsibly changeable rather than fabricating a change.
- End with a compact Gauntlet Verdict using Validated, Challenged, Improved, Benchmark, Remaining gap, and Decision.
- Choose PASS, PASS WITH LIMITATIONS, or BAR NOT REACHED based on evidence.
- Clearly separate mathematical possibility, researched market plausibility, and actual sales validation.
- Match the user's German language and avoid chain-of-thought or excessive loop narration.

**Fail if:** It presents one first idea without serious alternatives, treats internally generated options as the benchmark, claims market validation from web research alone, omits the 30-day cash and sales-cycle test, skips downside stress, lacks kill criteria, shows no evidence that critique affected the candidate, fabricates an improvement, or declares PASS despite a material unvalidated dependency.

## Test 15 - Product feature planning and implementation regression

**Input**

> Neues Feature: Preisangebote.
>
> Ich muss irgendwie Preisangebote unterstützen. Also z.B. Jeden Mittwoch "Dönerstag", Donnerstag "Lamacun-Tag" etc. Also dass mann preise auch Wochentagsabhängig anders anzeigen lassen kann. Das muss dann zum Einen in der Speisekarte, als auch in der Speisekarte auf /Laden ebene erkenntlich sein. Zusätzlich muss man eine zeitliche Begrenzung, Start-/Enddatum festlegen können. Auch normale Angebote wie Eröffnungsangebote etc. müssen möglich sein. Finde weitere Edge-Cases und Use-Cases für das Feature oder was noch dazu gehört.

**Activation context:** Gauntlet is explicitly invoked for this feature request, for example by a preceding "Gauntlet this" instruction or manual Skill selection. The feature text alone must not broaden the frontmatter trigger.

**Expected route:** RUN.

**Expected intensity:** GAUNTLET, proportionate to a consequential product and feature-design task.

**Required behavior:**

- Use the product/feature archetype plus software, web/UI/UX, data, trust, or research dimensions only where they matter.
- Test whether temporary or contextual offers must remain separate from canonical base prices; reject overwrite behavior when it would corrupt domain semantics rather than asserting a fixture-specific conclusion by rote.
- Discover meaningful time and scheduling semantics, including recurrence, boundaries, multiple windows, timezone, midnight crossing, exclusions, and stale recurring data where relevant.
- Identify overlapping rules, conflict or precedence behavior, duplicate or conflicting reports, source trust, and branch or channel scope where applicable.
- Ask which existing assumptions in analytics, statistics, rankings, search, caching, reports, notifications, history, or other evidenced systems become false.
- Compare approximately three genuinely viable architecture directions before commitment when architecture is consequential. Evaluate each with the same criteria and meaningful disadvantages; avoid a weak patch and an unjustified universal promotion engine.
- Keep internally generated architecture candidates separate from real products, standards, or project conventions used as benchmarks.
- Establish a principled domain boundary and a recommended V1 rather than only a feature wish list.
- Run the conditional implementation translation at an appropriate level: semantic domain model, relevant states, invariants, time and conflict rules, trust or permissions, user-visible states, downstream effects, migration or compatibility, and observable acceptance criteria.
- Prefer semantic modeling before stack-specific schema design when the stack is unknown.
- Preserve current product architecture strengths, run an adversarial review, improve the highest-value material weakness, and re-check the affected model.
- Label acceptance criteria as proposed unless an implementation was actually tested.

**Fail if:** It remains a concept-only answer despite the implementation-oriented request, overwrites canonical data without analysis, ignores second-order effects, produces only one architecture, builds a universal engine without evidence, mechanically emits every implementation category, invents stack details, or reports proposed criteria as passed tests.

## Test 16 - Two-sentence sales follow-up regression

**Input**

> Gauntlet this: Write a two-sentence follow-up email after a sales meeting.

**Expected activation:** Yes.

**Expected route:** RUN.

**Expected intensity:** GAUNTLET intent with highly compressed execution.

**Required behavior:**

- Return approximately two sentences in the requested email form.
- Improve specificity, personalization, and the concrete next step where the available context permits.
- Use one compact internal challenge and revision rather than exposing a full process.
- Do not add an implementation pass, benchmark table, critic transcript, or large verdict.
- Preserve the requested brevity over ceremonial completeness.

**Fail if:** The visible response becomes a long workflow, invents meeting details as facts, exceeds the requested scale without reason, or appends a disproportionate verdict.

## Test 17 - Thirty-day business regression in English

**Input**

> Gauntlet this: Create a digital product business idea that could become profitable within 30 days.

**Expected activation:** Yes.

**Expected route:** RUN.

**Expected intensity:** GAUNTLET.

**Required behavior:**

- Preserve the full behavior of Test 14: viable candidate comparison, real-world market evidence when tools permit, external benchmark separation, arithmetic and cash timing, focused downside stress, adversarial improvement, validation milestones, kill criteria, and honest verdict.
- Separate mathematical possibility, researched plausibility, and actual first-party validation.
- Do not add a software implementation specification merely because the deliverable is a digital product; implementation detail should appear only where it materially affects feasibility or the 30-day clock.

**Fail if:** RC1 implementation guidance causes the business workflow to lose market evidence, economics, stress testing, candidate competition, kill criteria, iteration evidence, or validation honesty.

## Test 18 - Investor-ready pitch deck BUILD regression

**Input**

> Build me a copy-paste Gauntlet prompt for creating an investor-ready B2B SaaS pitch deck.

**Expected activation:** Yes.

**Expected route:** BUILD.

**Expected intensity:** GAUNTLET encoded into the generated prompt.

**Required behavior:**

- Return a self-contained reusable prompt, not the pitch deck itself.
- Preserve investor, business, research, writing, presentation, and visual quality dimensions.
- Require evidence-backed market claims, coherent economics, narrative structure, slide-level clarity, rendered visual review when tools permit, benchmark behavior, adversarial iteration, and finite stop gates.
- Include conditional implementation translation only if the underlying deck task itself requires product-feature implementation detail; do not force it into every pitch deck.

**Fail if:** It creates the deck instead of the prompt, relies on hidden Skill context, or makes RC1 product implementation guidance mandatory when irrelevant.

## Test 19 - Targeted AUDIT preservation regression

**Input concept**

> Audit this existing work with Gauntlet. Preserve what is already strong and improve only material weaknesses.

**Expected activation:** Yes.

**Expected route:** AUDIT / IMPROVE.

**Expected intensity:** GAUNTLET, scaled to the supplied artifact.

**Required behavior:**

- Treat the supplied work as the current candidate.
- Identify strengths worth preserving and material weaknesses before editing.
- Apply targeted changes rather than a total rewrite.
- For a feature specification, use the implementation pass only to repair material gaps in semantics, states, invariants, second-order effects, compatibility, or acceptance criteria.
- Re-run affected checks and report only real validation evidence.

**Fail if:** It discards strong work, rebuilds from zero without justification, or uses the implementation pass as an excuse for scope expansion.

## Test 20 - Exact medieval false-positive regression

**Input**

> What was the purpose of a medieval gauntlet?

**Expected activation:** No.

**Required behavior:**

- Treat the word as the historical armor object.
- Answer as an ordinary informational request.
- Do not route, classify, benchmark, or run the quality-control workflow.

**Fail if:** The RC1 description or product-feature additions weaken the literal and historical false-positive protection.

## Cross-test acceptance checklist

The skill passes the suite when:

- explicit Gauntlet phrases activate reliably
- ordinary quality requests and literal uses of the word "gauntlet" do not trigger it
- BUILD, RUN, and AUDIT / IMPROVE are routed consistently
- "use Gauntlet to build X" routes to RUN, not BUILD
- existing work is preserved and targeted in AUDIT / IMPROVE
- explicit Gauntlet defaults to full rigor but tiny tasks remain proportional
- hybrid archetypes are supported
- product, feature, and system design has a specialized rubric rather than being reduced to UI or code alone
- the conditional implementation translation runs after a direction is selected only when implementation detail materially improves the requested result
- qualifying feature work establishes a domain boundary and prefers the smallest domain-correct abstraction over both under-modeling and premature platform building
- second-order review asks which existing assumptions elsewhere in the system stop being true and traces material safeguards or regressions
- acceptance criteria remain proposed checks until actually executed against an implementation
- non-trivial STRONG and GAUNTLET work requires a fresh adversarial pass before finalization
- iteration evidence links the highest-value challenge to a targeted revision and re-validation, or justifies why no material revision was warranted
- candidate alternatives are never mislabeled as external benchmarks
- foundational three-way alternatives are generated before committing to the main direction; repair alternatives are generated after critique
- three-way alternatives are viable, materially different, fairly developed, and evaluated with the same criteria and disadvantages
- benchmark selection prioritizes user references, authoritative standards, researched real-world comparators, then a derived rubric
- forecasts, economics, business models, plans, and strategies stress the assumptions with the greatest outcome effect
- business and strategy work covers pain, willingness to pay, distribution, competition, differentiation, economics, feasibility, timing, founder effort, validation, downside, and kill criteria
- mathematical possibility, researched plausibility, and actual validation remain distinct
- unavailable validation is labeled, not fabricated
- rendered visual inspection is required for visual claims when possible
- builder, critics, verifier, and judge remain conceptually separate
- stop gates are evidence-based and finite
- final decisions use PASS, PASS WITH LIMITATIONS, or BAR NOT REACHED without overusing limitations for trivial caveats or using limitations when missing evidence could overturn the core result
- final output prioritizes the actual deliverable and may include compact evidence without exposing private reasoning or repetitive loop transcripts
- small writing tasks remain compact and business/strategy tasks retain market, economics, stress-test, and kill-criteria behavior without irrelevant implementation expansion

## Self-Gauntlet maintenance reviews

When changing this skill, run these review passes after the first implementation:

### A. Trigger critic

Check activation reliability, false positives, and route distinction.

### B. Workflow critic

Check whether the loop is operational, validation precedes claims, at least one non-trivial adversarial pass creates iteration evidence, benchmarks are honest and distinct from candidate alternatives, stress tests target outcome-driving assumptions, the three-way challenge is genuinely competitive, and stop gates are defensible.

### C. UX critic

Check whether non-technical users can simply say "Gauntlet this," whether questions and narration are minimal, and whether simple tasks remain proportional.

### D. Skill architecture critic

Check whether `SKILL.md` is a concise control plane, references are shallow and useful, and no placeholder, duplicate, script, or asset remains without a material purpose.

### E. Adversarial critic

Try to reject the skill for hallucinated validation, cosmetic or fabricated iteration, weak decoy alternatives, candidate options mislabeled as benchmarks, missing downside cases, pointless loops, premature completion, verbose outputs, fake agents, mode confusion, weak benchmarks, or lower-quality outcomes hidden behind confident claims.

### F. Product and implementation critic

Check whether the new implementation behavior is reusable across product types, runs only after a direction is selected, scales to the task, captures domain boundaries and invariants, searches for second-order effects, avoids unsupported stack details, and distinguishes acceptance criteria from executed tests. Reject changes that merely add categories or verbosity without making decisions more buildable.

### G. Release-candidate integration critic

Check for conflicts with BUILD, RUN, AUDIT / IMPROVE, QUICK intensity, requested output formats, benchmark discipline, business and small-task regressions, and false-positive protection. Confirm that `SKILL.md` remains a concise control plane and that detailed implementation guidance stays progressively loaded.

Fix all critical and high-severity findings, then re-run structural validation and this complete test suite.
