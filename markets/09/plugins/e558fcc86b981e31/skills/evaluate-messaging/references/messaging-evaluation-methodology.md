# Messaging-Evaluation Methodology (BuyerTwin)

This reference defines how to evaluate supplied messaging against canonical BuyerTwin intelligence.

## 1) Activation and boundaries

Use evaluate-messaging when the user provides messaging and asks how well it aligns with buyer intelligence.

Do not use as primary workflow for:
- pure reaction simulation (route to ask-buyers)
- pure cross-buyer comparison without message evaluation (route to compare-buyers)
- net-new content generation
- sales-preparation workflows
- knowledge mutation workflows

## 2) Deterministic buyer scope

Resolve scope deterministically:
- one named buyer -> that buyer
- multiple named buyers -> all named buyers
- explicit subset or segment -> that subset
- all buyers -> all accessible buyers in scope
- my buyers without narrowing -> all accessible buyers in scope

Do not silently narrow scope by relevance heuristics.

## 3) Evidence hierarchy and authority

Use BuyerTwin evidence hierarchy:
1. BuyerTwin Knowledge: canonical facts
2. BuyerTwin Simulation: ask_buyer output (optional)
3. AI Synthesis: diagnosis and recommendations

Canonical knowledge has factual authority.
Simulation may enrich interpretation but does not override canonical facts.
Never present synthesis as stored BuyerTwin data.

## 4) Canonical-first evaluation sequence

First determine the apparent job of the supplied message artifact (for example headline, value proposition, CTA, positioning statement, short ad, email opener, objection-handling paragraph, or sales message).
Evaluate relative to what that artifact can reasonably accomplish.
Do not penalize a headline for failing to include every objection, proof point, or decision criterion.
If purpose is uncertain, constrain conclusions instead of inventing purpose.

Begin with canonical evidence relevant to the message:
- pains and triggers
- motivations and desired outcomes
- buying factors/criteria
- objections and risk concerns
- terminology/language
- decision dynamics and context

Then evaluate message alignment against that evidence.
Use ask_buyer only when simulation materially deepens evaluation (for example, ambiguous claim interpretation).
Do not make simulation mandatory.

## 5) Evaluation dimensions

Use only dimensions supported by the supplied message and available evidence.

### 5.1 Relevance
Assess whether message connects to known buyer priorities, pains, triggers, situations, and outcomes.
Identify matches and meaningful gaps.

### 5.2 Buyer value alignment
Assess whether value framing matches known motivations, outcomes, factors, jobs/use cases, and context.
Avoid generic copywriting heuristics without BuyerTwin grounding.

### 5.3 Objection and resistance coverage
Assess whether known objections/concerns are addressed, ignored, contradicted, or unknown from available evidence.
Do not invent objections.

### 5.4 Proof and credibility needs
If evidence indicates proof requirements, recommend appropriate substantiation (for example ROI support, implementation evidence, security/compliance reassurance, customer examples).
Label such recommendations as analysis when not explicit canonical fields.

### 5.5 Language and terminology fit
Compare supplied language with known buyer terminology and framing.
Identify aligned or potentially mismatched wording without forcing keyword copying.

### 5.6 Specificity
Assess whether claims are specific enough to connect to known buyer concerns.
Tie specificity recommendations to actual buyer evidence.

### 5.7 Decision relevance
When decision dynamics are available, assess whether message supports option evaluation and internal justification.
Do not invent stakeholders or approval rules.

### 5.8 Differentiation boundary
Do not claim competitive differentiation from buyer intelligence alone unless competitor evidence is available from current MCP tooling.
If absent, state that differentiation is not established by available evidence.

## 6) Diagnostic labels (qualitative only)

Useful labels include:
- Strong alignment
- Partial alignment
- Missing
- Potential mismatch
- Needs substantiation
- Buyer-specific tension

Terminology distinctions:
- Buyer relevance not established: retrieved BuyerTwin intelligence does not establish that a message element is materially relevant for this buyer.
- Needs substantiation: the claim may matter to the buyer, but available evidence suggests stronger proof or explanation is likely needed.
- Claim factual truth undetermined: BuyerTwin buyer intelligence alone cannot verify whether a company/product claim is objectively true.

These are analysis labels, not stored BuyerTwin fields.
Do not fabricate numeric scores.

## 7) Missing vs mismatch vs unknown

Keep these separate:
- Missing: BuyerTwin contains intelligence materially relevant to the message objective, and omitting it weakens the message.
- Contradictory or mismatch: message conflicts with canonical buyer intelligence.
- Unknown: insufficient BuyerTwin evidence to assess confidently.

Missing does not mean every known BuyerTwin priority must appear in every artifact.

Do not collapse unknown into negative judgment.

## 8) Multi-buyer evaluation method

For multi-buyer prompts:
1. evaluate each buyer against relevant canonical evidence
2. identify broad strengths
3. identify buyer-specific strengths and gaps
4. surface tradeoffs/conflicts
5. recommend what can remain universal versus personalized

Do not average away differences.

## 9) ask_buyer usage policy

Good uses (optional):
- ambiguous claim interpretation
- novel proposition reaction stress test
- emotional reasoning context after canonical diagnosis

Bad uses:
- replacing available canonical evidence
- mandatory per-buyer simulation by default
- generating factual claims
- manufacturing missing canonical data

## 10) Recommendation discipline

Recommendations should directly resolve diagnosed buyer-alignment issues.
Prefer specific, evidence-grounded recommendations over generic persuasion advice.
Do not auto-rewrite full messaging.
If user asks for revision after diagnosis, provide concise improvements tied to diagnosed findings. Keep the selected buyer and factual boundaries, and apply the requested saved voice through the shared writing reference linked from SKILL.md; diagnosis alone does not need voice retrieval.

## 11) Website/page boundary

This skill may evaluate supplied copy extracted from a page.
It must not claim Website Alignment or page-analysis outputs unless those capabilities are exposed through MCP tools.
