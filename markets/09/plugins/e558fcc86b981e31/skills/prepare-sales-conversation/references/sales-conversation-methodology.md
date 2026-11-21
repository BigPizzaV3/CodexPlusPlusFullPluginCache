# Sales-Conversation Methodology (BuyerTwin)

This reference defines sales-conversation preparation grounded in canonical BuyerTwin intelligence and explicit prospect context provided by the user.

## 1) Activation and boundaries

Use prepare-sales-conversation when the user asks to get ready for a buyer conversation (discovery, demo, qualification, proposal, executive, follow-up, and related conversations).

Do not use as primary workflow for:
- pure buyer reaction simulation (ask-buyers)
- pure buyer comparison (compare-buyers)
- supplied-message evaluation (evaluate-messaging)
- net-new content generation (create-buyer-content)
- knowledge mutation workflows

## 2) Prospect-vs-BuyerTwin distinction

Always distinguish:
- BuyerTwin intelligence: patterns about buyer type(s)
- User-provided prospect context: facts about the actual person/company/opportunity
- AI preparation: recommendations from those inputs

Do not turn BuyerTwin patterns into asserted prospect facts.

Preferred framing:
- "BuyerTwin indicates this is often relevant for this buyer type; validate whether it applies to this prospect."

Avoid:
- "This prospect definitely has this concern" unless provided by user facts.

## 3) Deterministic scope and mapping discipline

Resolve scope deterministically:
- one named BuyerTwin -> that buyer
- multiple named BuyerTwins -> all named buyers
- explicit subset or segment -> that subset
- all buyers -> all accessible buyers in scope
- my buyers without narrowing -> all accessible buyers in scope

Do not silently narrow by relevance heuristics.

If a real prospect role could map to multiple BuyerTwins, disclose ambiguity and ask clarifying questions when needed.

## 4) Domain-specific authority

Treat authority by domain rather than as one source globally overriding another:
- BuyerTwin Knowledge is authoritative for what BuyerTwin canonically knows about buyer-type patterns and buyer-context patterns.
- User-provided prospect/opportunity facts are authoritative for the specific person, account, and meeting context.
- BuyerTwin Simulation (optional ask_buyer rehearsal) is authoritative for neither domain.
- AI Synthesis provides preparation guidance.

Central rule:
- BuyerTwin describes the buyer pattern. Prospect evidence describes this prospect.

When BuyerTwin patterns and prospect-specific facts differ:
- Do not treat this as a generic contradiction where one source globally overrides the other.
- Use the prospect fact for this meeting-specific preparation.
- Keep BuyerTwin pattern knowledge as broader context or hypothesis only when still relevant.

Example:
- BuyerTwin pattern: financial justification is commonly important for this CFO type.
- Prospect fact: budget is already approved and implementation is the stated concern.
- Correct prep behavior: treat implementation as the known concern for this meeting; keep financial-justification context only as secondary pattern context if useful.

## 5) Core preparation workflow

1. Resolve BuyerTwin(s)
2. Capture known meeting context (objective, stage, offering, stakeholders)
3. Retrieve only materially relevant buyer intelligence
4. Separate known facts from hypotheses to validate
5. Prepare priorities, objections, criteria, proof needs, discovery questions, listening cues, and framing guidance
6. Optionally run rehearsal via ask_buyer when useful

## 6) Stage-aware adaptation

When stage/objective is provided:
- Discovery: prioritize validation questions, process, outcomes, triggers, assumptions to test
- Demo: prioritize buyer-relevant use cases, criteria, concerns, and proof needs
- Proposal/decision: prioritize decision criteria, approval dynamics, risk, unresolved objections, internal justification
- Executive: prioritize strategic outcomes, risk framing, concise proof

If stage is unknown, provide useful general preparation and clearly mark unknowns.

## 7) Discovery-question design

Discovery questions should test BuyerTwin-informed hypotheses without presupposing they are true for this prospect.

Prefer validation-style questions:
- "How does this process work today, and where does it create friction if at all?"

Avoid leading assumptions:
- "How much is this painful process hurting your team?"

Question design goals:
- validate hypotheses
- uncover actual situation and triggers
- clarify desired outcomes
- reveal criteria and concerns
- surface stakeholder dynamics
- identify proof expectations

## 8) Hypothesis versus fact handling

Keep distinctions visible in reasoning:
- Known from BuyerTwin
- Worth validating with this prospect
- Known about this prospect (user-provided)

This can be concise, but the distinction must be preserved.

## 9) Objection preparation

For relevant known objections, prepare:
- why it may matter
- how to recognize it
- a validating question
- proof to have ready
- what not to assume

Do not fabricate prospect-specific objections.
Do not default to manipulative rebuttal scripts.

## 10) Proof readiness

Recommend proof areas based on buyer intelligence, such as:
- implementation detail
- financial justification
- security/compliance material
- case examples
- adoption evidence
- workflow demonstration

Distinguish:
- BuyerTwin signal that proof sensitivity exists
- AI recommendation for proof type
- actual proof the company has

Never invent customer outcomes, ROI values, product facts, certifications, or evidence.

## 11) Listening cues

Provide cues as areas to explore, not diagnostic certainty.

Example:
- If they repeatedly mention approvals, explore who else needs confidence in the decision.

Do not treat one phrase as conclusive diagnosis.

## 12) Framing guidance

Recommend framing grounded in buyer intelligence, for example:
- lead with outcome before feature detail
- connect to known workflow friction
- address risk before commitment ask
- provide internal-justification material
- use familiar buyer terminology naturally

Do not invent offering claims while framing.

## 13) Multi-stakeholder preparation

For calls involving multiple BuyerTwins:
1. gather buyer intelligence for each
2. identify shared priorities
3. identify materially different priorities
4. identify potential decision tensions
5. identify stakeholder-specific needs/questions
6. propose conversation structure that avoids average-buyer flattening

Missing evidence for one stakeholder is not evidence they do not care.

## 14) Talk tracks and role-play

If user requests talk track:
- provide conversational structure (opening, discovery areas, value themes, proof, objection areas, next-step framing)
- avoid rigid script unless explicitly requested

If user requests role-play/practice:
- ask_buyer may be used as optional simulation
- clearly label simulation as simulated
- do not claim private knowledge about the real prospect/company
- optionally provide coaching after role-play

## 15) No fake certainty

Do not invent:
- close probability
- deal-risk percentage
- objection probability
- buyer-fit score
- confidence percentage

Prefer qualitative, evidence-backed preparation.
