# Ask-Buyers Methodology (BuyerTwin)

This reference supports the ask-buyers skill workflow and should be consulted when the request is not trivially single-buyer.

## 1) Activation intent

Use ask-buyers for questions about saved buyer intelligence and for hypothetical buyer reactions. Answer stored pains, priorities, objections and criteria canonically; reserve simulation for requests about what a buyer might think or do.

Prefer other workflows when the user primarily asks for:
- Stored-intelligence comparison (for example, direct category compare)
- Content generation
- Sales-call prep workflow assembly
- Knowledge mutation

## 2) Buyer resolution discipline

Resolve buyers from BuyerTwin tools, or reuse an unambiguous buyer already resolved in the same connected workspace. A workspace change or ambiguous reference requires fresh resolution.

Preferred sequence:
1. list_buyers
2. Optional list_segments for segment-constrained wording
3. Optional get_buyer for disambiguation and framing

Rules:
- Never invent buyers or IDs.
- If the user names one buyer, resolve that buyer.
- If the user names several buyers, resolve all named buyers.
- If the user specifies a segment or other explicit subset, use that subset.
- If the user explicitly asks for "all buyers", use all accessible buyers in the applicable workspace/scope.
- If the user says "my buyers" without further narrowing, default to all accessible buyers in scope.
- Do not silently select a subset based on model-defined relevance.
- Do not silently omit a buyer because its response seems redundant.
- If technical limits prevent processing the full requested set, disclose the limitation and what subset was used.
- If ambiguous and unresolved, ask a clarifying question.

## 3) Simulation discipline

Use ask_buyer as the simulation mechanism.

For multiple buyers:
- Call ask_buyer per buyer.
- Preserve response-by-response identity.
- Do not create one synthetic group quote.

## 4) Evidence model discipline

Maintain these boundaries in reasoning and wording:
- BuyerTwin Knowledge: canonical retrieved data
- BuyerTwin Simulation: ask_buyer outputs
- AI Synthesis: assistant conclusions across knowledge/simulations

Authority rule:
- Canonical BuyerTwin Knowledge has factual authority over BuyerTwin Simulation.
- If stored BuyerTwin knowledge and ask_buyer output conflict, do not let simulation override canonical facts.
- Use canonical knowledge for factual claims; use simulation as contextual reasoning.
- Surface materially important inconsistencies in the final answer.

Example conflict handling:
- Canonical knowledge: "Purchases above $100k require CFO approval."
- Simulation: "This buyer appears enthusiastic about moving forward."
- Correct synthesis: "The buyer may respond positively, but BuyerTwin indicates purchases above $100k still require CFO approval."
- Incorrect synthesis: "This buyer would approve the $150k purchase."

Do not present:
- Simulation as literal real-world quotes
- Synthesis as canonical stored data

Language guidance for simulated output:
- Prefer: likely, may, would probably, appears likely to, simulation suggests, based on known priorities.
- First-person simulated voice is allowed only when the user explicitly asks (for example, "answer as the buyer", "in their voice", "role-play").
- Even in first-person voice, clearly label the content as simulated.

## 5) Synthesis expectations

When multiple buyers are involved, include:
- Common ground
- Key disagreements
- Outliers
- Implications for the user question

Do not force consensus.
Do not convert majority views into universal consensus.

When useful (but not mechanically), classify synthesis as:
- unanimous
- majority
- mixed
- buyer-specific

## 6) Canonical versus simulation routing

ask-buyers primarily activates for perspective/reaction questions.

Use simulation-first for prompts like:
- "What would our CFO think about moving to monthly pricing?"
- "How would our Founder react to this positioning?"

Use canonical-first for prompts like:
- "What objections are stored for our CFO buyer?"

If a question can be answered directly from canonical BuyerTwin intelligence, prefer the canonical answer rather than simulated restatement.

Questions asking direct comparison of stored buyer attributes (for example, compare pains across buyers) are not primarily ask-buyers simulation.

## 7) Tool usage discipline

Do not fetch every available BuyerTwin dataset by default.

Only retrieve additional canonical intelligence when at least one is true:
- It directly answers part of the user question.
- It materially improves grounding.
- It is needed to understand or explain simulation output.
- It is required to resolve ambiguity.

Avoid blanket retrieval patterns such as always calling all buyer-intelligence endpoints for every ask-buyers invocation.

## 8) Explicit prohibitions

Do not:
- Use mutation tools in this skill
- Claim website alignment or page-review findings
- Claim Pull/Hold or belief/trust/clarity/risk scoring without exposed MCP data
- Fabricate unavailable MCP facts
