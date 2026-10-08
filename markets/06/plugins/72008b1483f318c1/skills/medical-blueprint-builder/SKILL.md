---
name: medical-blueprint-builder
description: Turn medical topics, curricula, lectures, textbooks, guidelines, exams, rotations, or supplied source documents into clinically aligned education and assessment blueprints. Use when the user wants learning outcomes, competencies, clinical-reasoning priorities, must-not-miss content, constructive alignment, assessment plans, tables of specifications, high-yield blueprints, or document-derived medical teaching frameworks.
---

# Medical Blueprint Builder

Use this skill to design medical education and assessment around what a learner must be able to recognize, interpret, reason through, decide, do, and reassess.

Core sequence:

**Know → Understand → Recognize → Interpret → Reason → Decide → Act → Reassess**

Prioritize:

- clinical relevance over encyclopedic completeness
- reasoning over memorization
- patient safety over trivia
- decision usefulness over factual density
- accuracy over completeness

Follow the user's explicit instructions on scope, language, format, and depth when they are compatible with safety and evidence constraints. Respond in the user's language unless they request another language.

## Workflow

1. **Identify the learner and purpose.** Infer learner level, clinical role, expected autonomy, teaching/exam context, and desired depth when possible. Ask at most one clarifying question only when a missing detail would materially change the blueprint; otherwise state a brief assumption and proceed.
2. **Choose the blueprint pattern.** Select the single best primary pattern from `references/blueprint-patterns.md`. Add only supporting modules that materially improve the result.
3. **Identify the core clinical work.** Ask what this learner must recognize, interpret, prioritize, decide, perform, communicate, or reassess. Do not turn the task into a chapter inventory.
4. **Prioritize.** Separate must-know / should-know / nice-to-know content, and make safety-critical or must-not-miss items explicit.
5. **Make reasoning visible.** When clinically relevant, organize around presentation → problem representation → prioritized differential → investigation → severity/risk → management → reassessment. Explain the purpose of investigations and the decision consequences of results.
6. **Convert content into observable outcomes.** Use action verbs and define competencies as observable performance in context. For course, rotation, or exam tasks, align outcomes, practice, assessment, feedback, and reassessment.
7. **Choose the output structure.** Use the most relevant template from `references/output-templates.md`; do not force every section into every answer.
8. **Quality-check before output.** Confirm learner fit, clinical relevance, explicit reasoning, safety-critical content, assessment alignment, evidence discipline, and feasibility.

## Source-based tasks

When the user supplies a guideline, textbook, lecture, syllabus, article, or other document:

- Treat the supplied source as the primary content source for document-derived claims.
- Preserve the source's terminology and framing when useful.
- Do not attribute outside knowledge to the source.
- Do not fill source gaps by guessing.
- If external knowledge is added, label it clearly as external or supplemental.
- If the source conflicts with current standards and verification is available, distinguish source content from updated external evidence.

## Clinical reasoning rules

When appropriate:

- Prioritize differentials as common, dangerous, easily confused, and context-specific rather than listing everything.
- Frame investigations as **test → clinical question → decision consequence**.
- Frame management as **situation → decision → rationale → reassessment**.
- If a scenario is unstable, stabilization and time-sensitive action come before diagnostic perfection; diagnosis can proceed in parallel.
- Close the loop: **decision → intervention → response → reassessment → continue / modify / escalate / reconsider**.

## Education and assessment rules

Use `references/medical-education-methodology.md` when the task involves CLOs, LOs, competencies, curriculum design, rotations, assessment blueprints, MCQ/SBA/OSCE planning, constructive alignment, weighting, Miller-type performance levels, or remediation.

Use `references/assessment-and-tos.md` when the user requests an exam blueprint or Table of Specifications.

Do not:

- claim that an MCQ directly demonstrates procedural or workplace performance
- present proposed weighting as an official validated distribution unless a source explicitly establishes it
- use educational terminology that does not improve clarity, alignment, or measurability

## Evidence discipline

Never invent a guideline, trial, citation, statistic, prevalence estimate, dose, cutoff, score, diagnostic criterion, sensitivity/specificity value, or recommendation class.

When current guidelines, standards, drug doses, diagnostic cutoffs, or recent evidence are material to the task:

- verify them with an appropriate reliable source when retrieval/search is available; or
- state that current verification is needed and avoid unsupported specifics when it is not.

Distinguish fact, inference, and hypothesis when uncertainty matters.

## Clinical safety and privacy

This skill is for medical education and assessment design, not individualized diagnosis or prescribing.

- Do not solicit or require protected health information, government identifiers, access credentials, or other restricted personal data.
- If a user supplies an identifiable patient case, ask them to remove identifiers before using the case for blueprint construction. Do not repeat unnecessary identifiers.
- For a real-person urgent clinical scenario, prioritize general safety guidance and appropriate direct evaluation rather than converting the request into a teaching blueprint.
- Do not present an educational blueprint as a substitute for local clinical judgment, institutional policy, supervision, or direct patient assessment.

## Final quality check

Before responding, verify:

- Is the learner, scope, and purpose clear?
- Is the core clinical work more prominent than trivia?
- Is reasoning explicit rather than merely a fact list?
- Does each important investigation have a purpose?
- Does management include decision logic and reassessment?
- Are must-not-miss risks and escalation triggers visible?
- Are competencies observable and assessment methods appropriate to the performance level?
- Are proposed weights labeled as proposals unless officially sourced?
- Are source-derived and external claims clearly separated?
- Are uncertain claims stated with appropriate confidence?
- Has unnecessary identifiable patient information been excluded?

A strong blueprint should help the learner answer:

**What matters? Why does it matter? How do I recognize it? What does it mean? What decision follows? What action is required? How do I know whether it worked?**
