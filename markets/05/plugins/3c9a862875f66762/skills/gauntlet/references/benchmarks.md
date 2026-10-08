# Benchmark Selection and Comparison

Benchmarking makes Gauntlet harder to satisfy with its own first attempt. Use the strongest honest comparison target available.

## Contents

1. Benchmark priority
2. Candidate alternatives versus benchmarks
3. Suitability test
4. User-supplied references
5. Authoritative standards
6. Researched real-world benchmarks
7. Derived professional rubrics
8. Side-by-side comparison
9. Gap severity and action
10. Benchmark failure modes
11. Reporting benchmark evidence

## 1. Benchmark priority

Select in this order:

1. **User-supplied real reference** - screenshot, site, product, codebase, article, document, specification, competitor, example, or other target supplied by the user.
2. **Authoritative applicable standard** - accessibility specification, platform guideline, design system, academic or professional convention, file-format standard, accounting rule, project convention, or other named standard relevant to the task.
3. **Researched real-world competitors or examples** - current, credible, comparable products, strategies, designs, businesses, research, or implementations found with available research tools.
4. **Task-specific professional rubric** - a clearly labeled derived standard when no suitable real reference or authoritative standard can be inspected.

A later option does not automatically replace an earlier one. Combine benchmarks when they govern different critical dimensions. Example: use the user's screenshot for visual fidelity, a named accessibility standard for interaction quality, and real competitors for market positioning.

For market, product, business, research, design, and strategy work, prefer real-world comparators when tools permit and the comparison would materially improve the result. For feature design, use real products, standards, and established project conventions to challenge observed behavior and scope; do not treat internal architecture options as external benchmarks or import a competitor's entire platform complexity without evidence.

## 2. Candidate alternatives versus benchmarks

Keep these concepts separate:

- **Candidate alternatives** are options generated or considered inside the Gauntlet, such as three architectures, business models, layouts, headlines, or interpretations.
- **Benchmarks** are external references or standards, or an explicitly derived professional rubric used to judge quality.

Three internally generated options are not an external benchmark. Comparing them can select the best internal candidate, but it does not establish market competitiveness, standard compliance, reference fidelity, or real-world validation.

Use candidate comparison and benchmark comparison as distinct steps:

1. Compare candidate alternatives against the same task rubric.
2. Select, synthesize, or reject them.
3. Compare the selected direction against the real benchmark.
4. Report external comparison limits honestly.

## 3. Suitability test

Before using a benchmark, check:

- **Relevance** - Does it measure the user's intended outcome?
- **Comparability** - Are audience, scope, platform, scale, time horizon, and constraints sufficiently similar?
- **Authority** - Is it credible for the dimension being judged?
- **Recency** - Is freshness material, and is the benchmark current enough?
- **Accessibility** - Can it actually be inspected, not merely named?
- **Legality and permissions** - Can it be used appropriately without bypassing restrictions?
- **Bias** - Does it unfairly favor a style, architecture, or business model unrelated to the task?

Reject or qualify a benchmark that is famous but not comparable.

## 4. User-supplied references

Treat a supplied reference as primary unless it conflicts with safety, law, hard constraints, or the user's stated outcome.

Determine what the user wants to preserve, match, or outperform:

- exact fidelity
- structural pattern
- visual quality
- tone or voice
- interaction behavior
- architecture or code convention
- evidence standard
- content density
- economics or delivery model
- level of polish

Do not assume the goal is literal copying. Identify dimensions to match, dimensions to improve, and dimensions intentionally allowed to differ.

When the reference is a file, image, screenshot, site, codebase, or document:

- inspect the actual content with available tools
- use rendered or visible inspection for visual claims
- cite or point to concrete comparison evidence when appropriate
- do not claim the reference was inspected if it was inaccessible

## 5. Authoritative standards

Use named standards only when applicable to the task and available enough to apply accurately.

Examples include:

- accessibility requirements
- platform interface guidance
- project coding conventions
- language or framework standards
- file-format specifications
- academic citation and reporting conventions
- accounting, financial, or data methodology rules
- brand or design systems
- professional document formats

For each named standard:

1. State which dimensions it governs.
2. Use the relevant version when version matters.
3. Apply mandatory requirements separately from recommendations.
4. Avoid claiming full compliance unless the required checks were actually performed.
5. Report partial or unvalidated compliance precisely.

## 6. Researched real-world benchmarks

Research real comparators when current external examples materially improve the result and research tools are available.

### Research method

- Search for examples comparable in audience, category, scale, business model, maturity, and use case.
- Prefer primary, authoritative, or directly inspectable sources.
- Verify recency when the field changes quickly.
- Use more than one comparator when a single example could distort the rubric.
- Extract patterns and standards rather than copying protected expression.
- Record why each comparator is relevant.
- Search for contrary or alternative patterns when professional practice is contested.
- For business and strategy, inspect real offers, pricing, distribution, proof signals, delivery model, and operational implications when available.

### Research honesty

- Cite sources when the environment and task require citations.
- Distinguish fact from inference.
- Do not imply market-wide consensus from a few examples.
- Do not call a benchmark current without checking its date when recency matters.
- Do not claim direct comparison when only summaries or metadata were available.
- Do not confuse researched plausibility with actual user demand, paid sales, or first-party validation.

## 7. Derived professional rubrics

When no suitable external benchmark is available, create a task-appropriate professional rubric.

Label it explicitly as a **derived professional rubric**, not an external comparison.

Build it from:

- the user's requirements and intended outcome
- domain archetype dimensions
- obvious failure modes
- stable professional conventions
- available validation methods
- the cost of errors in the stated context

A derived rubric should include:

- must-pass requirements
- critical quality dimensions
- observable evidence for each dimension
- severity definitions
- stop gates

Avoid empty standards such as "world-class," "best-in-class," or "excellent" without observable meaning.

## 8. Side-by-side comparison

When a meaningful reference exists, compare the candidate directly.

Use a compact internal matrix:

| Dimension | Benchmark behavior | Candidate behavior | Evidence | Gap | Action |
| --- | --- | --- | --- | --- | --- |
| [critical dimension] | [what the benchmark does] | [what the candidate does] | [inspection, research, or test] | None / Low / Medium / High / Critical | Preserve / Improve / Accept deliberate difference |

Ask:

- Where does the candidate lose against credible real alternatives?
- Is the loss visible, measurable, researched, or only speculative?
- Does the benchmark advantage matter to the user's outcome?
- Is the candidate's difference deliberate and better suited to constraints?
- What single change would close the largest material gap?

### Domain-specific comparison examples

For visual work:

- hierarchy
- typography
- spacing
- composition
- density
- consistency
- responsiveness
- interactions
- perceived polish

For code:

- correctness
- simplicity
- architecture
- tests
- readability
- failure handling
- security
- operational quality

For writing:

- clarity
- structure
- specificity
- evidence
- originality
- persuasive force
- pacing

For research:

- source authority
- coverage
- recency
- contradiction handling
- citation traceability
- uncertainty calibration

For strategy and business:

- customer pain and urgency
- willingness to pay
- distribution and acquisition path
- competition and differentiation
- economics and time horizon
- operational effort and feasibility
- downside behavior
- validation and kill criteria

For data:

- integrity
- methodology
- formula correctness
- reproducibility
- visualization honesty
- decision usefulness

## 9. Gap severity and action

### Critical gap

The candidate cannot satisfy its core purpose or violates a must-pass standard. Fix before passing.

### High gap

The benchmark materially outperforms the candidate on a dimension likely to change the user's outcome. Fix unless the user explicitly accepts the trade-off.

### Medium gap

The gap is meaningful and worth fixing when the expected value is good. It does not necessarily block delivery.

### Low gap

The gap is cosmetic, preferential, or low impact. Avoid endless churn after the stop gates pass.

### Deliberate difference

The candidate differs for a reason grounded in user constraints or a better intended outcome. Preserve it and document the rationale only when useful.

## 10. Benchmark failure modes

Avoid:

- naming a benchmark without inspecting or applying it
- comparing against a reference that is not actually accessible
- calling internally generated alternatives an external benchmark
- using a vague professional standard while implying external validation
- copying surface style while missing the reference's functional strengths
- treating popularity as proof of quality or demand
- using one example as universal truth
- ignoring the user's constraints to chase benchmark similarity
- declaring parity based on a self-assigned score
- hiding benchmark losses with general praise
- claiming compliance with a standard after only a partial check
- claiming market validation from researched examples alone

## 11. Reporting benchmark evidence

Keep user-facing benchmark reporting concise and factual.

Good examples:

- "Benchmark: the supplied desktop and mobile screenshots; compared hierarchy, spacing, typography, and responsive behavior."
- "Benchmark: the repository's existing service pattern and test conventions."
- "Benchmark: three researched competitors for offer, pricing, distribution, and delivery comparison. The internally generated options were candidate alternatives, not the benchmark."
- "Benchmark: a derived professional rubric because no inspectable external reference was available."
- "Benchmark comparison remains incomplete because the linked page could not be accessed."

Do not say:

- "Now world-class."
- "Matches industry best practices" without naming and applying them.
- "Pixel-perfect" without actual rendered comparison at relevant dimensions.
- "Fully compliant" when only some checks were performed.
- "Market validated" when no first-party behavior or sales evidence exists.
