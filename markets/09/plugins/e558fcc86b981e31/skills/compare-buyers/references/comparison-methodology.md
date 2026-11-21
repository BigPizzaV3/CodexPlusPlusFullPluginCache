# Compare-Buyers Methodology (BuyerTwin)

This reference defines how to compare buyers using canonical BuyerTwin intelligence as the system of record.

## 1) Activation and boundaries

Use compare-buyers when the user asks for similarities, differences, patterns, or implications across two or more buyers.

Typical fits:
- "Compare our CFO and Founder."
- "What pains do all of our buyers share?"
- "Where should our messaging be universal versus personalized?"

Do not use compare-buyers as the primary workflow for:
- simulated reaction questions (route to ask-buyers)
- role-play requests (route to ask-buyers)
- content generation workflows
- messaging evaluation workflows
- knowledge mutation workflows

## 2) Deterministic scope resolution

Resolve scope explicitly and deterministically:
- Named buyer: resolve that buyer.
- Several named buyers: resolve all named buyers.
- Explicit segment/subset: compare that exact subset.
- "All buyers": include all accessible buyers in scope.
- "My buyers" without narrowing: default to all accessible buyers in scope.

Do not silently narrow scope by relevance heuristics.
Do not silently drop buyers due to apparent redundancy.
If technical limits prevent full scope, disclose what subset was compared.

A meaningful comparison requires at least two buyers. If fewer than two can be resolved, say comparison is not possible with current scope.

## 3) Canonical data-first evidence model

Use the BuyerTwin evidence hierarchy:
1. BuyerTwin Knowledge: authoritative stored/retrieved facts.
2. AI Synthesis: comparison and implications derived from those facts.

BuyerTwin Simulation is not the normal mode for compare-buyers.
Do not use ask_buyer as the default comparison mechanism.

If the question is directly answerable from canonical intelligence, answer from canonical data without simulation restatement.
If needed evidence is missing, identify missing data instead of inventing differences.

## 4) Targeted retrieval (no tool enumeration)

Retrieve only dimensions needed for the asked comparison.

Examples:
- "Compare objections" -> retrieve objection-relevant intelligence.
- "Compare biggest pains" -> retrieve pain intelligence.
- "How are these buyers different?" -> retrieve a high-value set of dimensions sufficient for meaningful contrasts.

Do not call all available buyer-intelligence endpoints by default.

## 5) Comparison pattern labels

Use labels only when evidence supports them:
- Shared or universal: present across every buyer in scope.
- Majority: present across most but not all buyers.
- Buyer-specific evidence: explicitly supported for one buyer or subset, but not established across the remaining buyers.
- Contrasting: requires affirmative evidence that buyers prioritize materially different criteria, concerns, or perspectives.
- Missing or unknown: insufficient canonical intelligence for reliable comparison.

Do not turn majority into universal consensus.
Missing data for one buyer is not sufficient to establish a contrast.

## 6) Absence and missing-data rules

Absence is not negative evidence.

If Buyer A contains an item and Buyer B lacks it in retrieved data, do not conclude Buyer B rejects or does not care about it.
Prefer wording such as:
- "BuyerTwin explicitly identifies this for Buyer A; it is not present in retrieved intelligence for Buyer B."

If one buyer has richer intelligence than another, disclose that uneven coverage may influence apparent differences.

## 7) Normalization discipline

Concepts with different wording may be grouped when that improves usefulness, but preserve meaningful nuance.

Reasonable conceptual grouping example:
- implementation complexity
- difficult rollout
- resource-heavy onboarding

Potential shared theme: implementation friction.

Do not over-normalize materially distinct concepts.
For example, keep distinctions between:
- price concern
- procurement approval
- ROI proof
when those distinctions matter to the decision.

## 8) Frequency and ranking discipline

Do not treat repetition counts as formal ranking unless ranking/weight evidence exists in canonical data.

Prefer language like:
- "appears repeatedly"

Avoid unsupported language like:
- "is their #1 priority"
unless canonical ranking evidence explicitly supports it.

## 9) Output strategy and implications

Answer the user's question directly.

For broad comparison prompts, useful structure often includes:
- strongest shared themes
- biggest differences
- buyer-specific concerns
- meaningful outliers
- implications

For focused prompts, stay narrow and dimension-specific.

Strategic recommendations (for example, universal vs personalized messaging) should be clearly labeled as AI synthesis grounded in canonical BuyerTwin evidence.
Do not present recommendations as stored BuyerTwin facts.

## 10) Universal versus personalized messaging

When asked what messaging can work across buyers:
1. Identify evidence that is genuinely shared across all buyers.
2. Identify materially different priorities.
3. Recommend what can remain common.
4. Recommend what should vary by buyer.
5. Explain why, grounded in canonical evidence.

Do not generate final copy unless explicitly requested and still compatible with workflow boundaries.
