# Buyer-Content Methodology (BuyerTwin)

This reference defines buyer-centered content creation grounded in canonical BuyerTwin intelligence.

## 1) Activation and boundaries

Use create-buyer-content for content briefs, finished writing and revisions based on BuyerTwin insights, plus company/person voice-only writing for a supplied audience or text. Apply buyer-research requirements when buyer grounding is part of the task; see Conversation continuity for voice-only work.

Do not use as primary workflow for:
- pure buyer reaction (ask-buyers)
- pure buyer comparison (compare-buyers)
- supplied-message diagnosis (evaluate-messaging)
- sales-call preparation workflows
- knowledge mutation workflows

## 2) Deterministic buyer scope

Resolve scope deterministically:
- one named buyer -> that buyer
- multiple named buyers -> all named buyers
- explicit subset or segment -> that subset
- all buyers -> all accessible buyers in scope
- my buyers without narrowing -> all accessible buyers in scope

Do not silently narrow scope by relevance heuristics.

## 3) Buyer-first grounding before writing

Before drafting, establish enough buyer context to answer:
- Who is this for?
- What buyer situation makes this relevant?
- What problem, trigger, goal, or decision is involved?
- What must the buyer understand, believe, decide, or do?
- What resistance/questions likely matter?
- What proof may be needed?
- What language/terminology should shape framing?
- What next-step movement should content support?

Retrieve only intelligence needed for the requested artifact.

## 4) Topic validation and angle selection

For user-supplied topics:
- If BuyerTwin grounding is strong, choose the most relevant buyer angle.
- If grounding is weak, disclose weak relevance and suggest stronger buyer-linked alternatives.

Do not manufacture buyer interest.

Angle selection should prioritize BuyerTwin-grounded signals such as:
- urgent pain
- trigger
- misconception
- desired outcome
- objection
- decision difficulty
- workflow friction
- internal approval challenge

Avoid sensational framing that is not buyer-grounded.

## 5) Intended buyer movement

Define what the artifact should help the buyer do, such as:
- recognize a problem
- evaluate an approach
- reduce uncertainty
- justify action
- prepare for internal decision
- take a next step

Do not force a rigid funnel stage when unsupported.

## 6) Buyer tensions and key questions

Identify relevant tensions only when supported by evidence, such as:
- pain vs desired outcome
- urgency vs perceived risk
- change desire vs implementation concern
- champion enthusiasm vs approval barriers

Use canonical intelligence to identify key questions the content should answer.
Do not auto-generate generic FAQ content.

## 7) Proof requirements and evidence boundaries

Distinguish clearly:
- known buyer need for proof
- AI recommendation for proof type
- actual company evidence supplied by the user

Potential proof needs may include implementation detail, financial justification, examples, security/compliance, and operational feasibility.

Authority rule:
- BuyerTwin establishes buyer relevance, buyer context, and buyer perspective.
- BuyerTwin does not establish factual truth of company, product, competitor, customer, or market claims.

Never fabricate:
- statistics
- customer quotes
- case-study outcomes
- ROI values
- product capabilities
- competitor facts
- analyst findings
- market data

## 8) Language and terminology

Use BuyerTwin terminology to improve resonance and precision.
Avoid keyword stuffing and awkward research phrase copying.
Aim for natural language that reflects buyer understanding.

## 9) Mode selection: brief vs finished content

If user asks for a brief/strategy, provide brief mode output (not forced full draft).
Potential brief fields include:
- target buyer(s)
- buyer situation
- content objective
- key tension
- recommended angle
- key questions
- evidence to use
- objections/risks to address
- proof needed
- framing/terminology
- structure
- desired next step

If user asks for finished content:
1. establish grounding
2. determine objective and angle
3. draft artifact
4. avoid fabricated evidence
5. preserve writing quality and buyer relevance

## 10) Multi-buyer creation strategy

For one artifact across multiple buyers:
1. identify genuinely shared intelligence
2. identify material differences
3. set a central message that can be shared safely
4. determine where variants/sections/personalization are needed
5. avoid unsupported universal claims

If buyer needs materially diverge, recommend variants instead of forcing an average buyer message.

## 11) Selective simulation policy

ask_buyer is optional.
Useful after canonical grounding for:
- angle stress-testing
- likely interpretation of novel claim
- likely follow-up questions

Do not use ask_buyer as a substitute for canonical research or by default on every request.

## 12) Artifact adaptation guidance

Adapt approach by artifact type:
- Article: insight, nuance, questions, proof, and practical next step.
- Landing page copy: relevance, value, decision support, proof, risk reduction, and action.
- Email: situation recognition, concise relevance, and credible next step.
- Social: buyer-relevant observation, concise perspective, and useful insight.
- Sales messaging: decision concerns, outcomes, objections, and credible movement.

These are guidance patterns, not rigid templates.

## 13) Evaluate-vs-create boundary

Create-buyer-content builds net-new strategy/content from BuyerTwin intelligence.
Evaluate-messaging diagnoses supplied copy against BuyerTwin intelligence.

If user asks to evaluate existing copy, evaluate-messaging is primary.
If user asks to create new content, create-buyer-content is primary.

## 14) Website/page boundary

This skill may write or refine page copy but must not claim Website Alignment scoring/reactions/page-analysis unless such outputs are exposed via MCP tools.


## Conversation continuity

Use the conversation to carry forward the connected workspace, resolved buyer IDs, selected concern/angle, retrieved evidence and its source type, audience, format, purpose, supplied facts and chosen voice. This is ordinary conversational context, not new persisted state or a save instruction. Resolve an ambiguous “that” only when the choice materially changes the output; do not ask the user to repeat a clear preceding selection.

Reuse relevant canonical buyer findings already retrieved for this task. Fetch additional or refreshed intelligence when the question changes, evidence is missing/stale, or the connected workspace/target changes. Do not repeat a full retrieval cycle for each draft revision, carry private context across organizations, silently expand one buyer to all buyers, or replace a simulated reaction with a stored buyer fact. If the user chooses one buyer from a comparison, narrowing to that buyer is explicit scope.

Turn the selected finding into a useful angle: what the buyer faces, what they need to understand/decide/do, and what supported evidence can move that decision. Make the selection briefly clear when useful, then provide the requested artifact. Do not force an intermediate strategy document, generic template, extra questionnaire or simulation before writing.

A request for a different format or named voice normally retains the buyer, selected insight and factual boundaries. Load applicable published company/person/channel guidance and actual example prose through [the shared writing reference](../../manage-writing-guidance/references/use-saved-writing-guidance.md). Resolve a newly requested voice; do not silently reuse the old narrator. Company-only narration must not make a named person speak as the company. Freshness checks are distinct from repeating buyer research.

For voice-only writing or rewriting, use the supplied audience/topic/text and saved voice without requiring an unrelated buyer lookup. Ask only when a missing audience or task materially prevents useful writing. Do not claim buyer grounding if none was retrieved. A prospective content format does not create an unsupported tool parameter.

When a follow-up asks to evaluate the draft, diagnose against the established buyer evidence; when it requests a rewrite, retain those findings and the chosen voice. Keep evidence labels in the accompanying explanation where useful, rather than littering finished copy with internal tool metadata. Simulated language is not a real customer quote or product proof. Temporary tone edits, drafts and examples remain unsaved unless the user explicitly requests the separate reviewed update workflow.
