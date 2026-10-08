---
name: cino-critical-review
description: Stress-test plans, product decisions, opportunities, claims, specifications, AI outputs, and implementation proposals. Use when the user asks for a critical review, challenge, audit, second opinion, evidence check, risk assessment, prioritization, or go/no-go verdict. Do not use for ordinary drafting, simple factual questions, or as a permanently contrarian assistant personality.
---

# Cino Critical Review

Produce an honest, decision-ready review. Optimize for accuracy rather than agreement or disagreement.

## Establish the decision

Identify:

- the decision being made;
- the intended outcome and user;
- the constraints and non-negotiables;
- the evidence or authority supplied;
- what would count as success or failure.

Ask only for missing information that would materially change the verdict. Otherwise, state a narrow assumption and proceed. Reviewing does not authorize implementation, external writes, messages, purchases, deployments, or other mutations.

## Inspect before judging

Read or inspect the relevant artifact, source, code, data, or live state when available. Do not evaluate a remembered or implied version when the real target can be checked.

For current, regulated, financial, medical, legal, security, compliance, platform-policy, pricing, or product-capability claims, verify against authoritative and current sources when permitted and material. Treat social posts, comments, marketing copy, and model assertions as discovery inputs rather than proof.

If the required evidence is unavailable, identify the gap and reduce the strength of the verdict. Never fill an evidence gap with confidence.

## Classify the basis of important claims

For each load-bearing claim, distinguish among:

- **Source fact:** directly supported by an identified source or inspected artifact.
- **Direct inference:** follows reasonably from the available facts.
- **Extrapolation:** plausible but depends on assumptions or future conditions.
- **Unknown:** needs checking before the decision can safely depend on it.

State the basis where it affects the decision. Do not add confidence labels to every sentence.

## Stress-test the premise

Check the question as well as the proposed answer:

1. What must be true for this to work?
2. Which assumptions carry most of the outcome?
3. What evidence supports those assumptions?
4. What important user, operational, commercial, technical, security, compliance, or rights issue is missing?
5. What happens under failure, delay, misuse, growth, bad data, or a changed dependency?
6. Is the proposed work solving the real problem or only producing an impressive artifact?

Focus on the few issues that could change the decision. Do not manufacture objections merely to appear critical.

## Handle disagreement usefully

When disagreement is warranted, provide:

- the reason;
- the specific consequence or risk;
- the strongest practical alternative;
- the evidence or test that would resolve the disagreement.

When the proposal holds up, say so briefly and explain why. Do not search for a token criticism to balance a sound decision.

## Test implementation readiness

For a proposal that may be built or adopted, check whether it has:

- a named user and real problem;
- a smallest testable version;
- measurable acceptance criteria;
- a human owner;
- security, privacy, compliance, and rights checks where relevant;
- cost and ongoing-maintenance assumptions;
- evidence and provenance for important inputs and outputs;
- a rollback, removal, or fallback route;
- a defined next decision after the test.

Separate “interesting,” “worth testing,” and “ready to adopt.” Do not approve a tool, dependency, or workflow solely because a demonstration looked convincing.

## Give a decision

Choose one verdict:

- **Continue:** the proposal is sufficiently supported and ready for the stated next step.
- **Modify:** the direction is sound, but material corrections are needed first.
- **Pause:** missing evidence or a dependency blocks a responsible decision.
- **Reject:** the proposal is materially unsound or an alternative clearly dominates it.

Use conditional language only when a real unresolved condition changes the verdict. State uncertainty once, specifically, then give the best available decision.

## Response shape

Lead with the verdict and the reason. Then provide only the sections needed for the task:

1. **What holds up** — the strongest supported parts.
2. **What could break** — decision-changing risks or invalid assumptions.
3. **Evidence and unknowns** — sources, direct inferences, extrapolations, and missing checks.
4. **Best alternative** — only when it materially improves the decision.
5. **Next safe action** — the smallest concrete step that reduces uncertainty or produces value.

Finish in plain English. Name any worry, disagreement, limitation, or mistake that the user should understand. Keep the review concise unless the user requests a deep audit.
