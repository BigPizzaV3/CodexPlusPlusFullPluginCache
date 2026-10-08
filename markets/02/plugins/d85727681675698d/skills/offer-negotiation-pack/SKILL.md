---
name: offer-negotiation-pack
description: "Use when an estate agent is handling a UK residential property offer, counteroffer, best-and-final position, buyer-vendor price gap, rejected offer, or negotiation strategy. Ground property-value arguments in Propalt valuation, comparable, history, and local-market data; keep party motivations and limits as user-supplied context."
---

# Offer Negotiation Pack

Build an internal negotiation strategy grounded in property evidence without inventing buyer or vendor circumstances.

## Workflow

1. Resolve the subject property with `address_lookup` if needed.
2. Pull relevant facts: `get_property`, `get_property_history`, `get_valuation_by_property_id`, `get_comparable_by_property_id`, and local context from `get_monthly_market` or `get_quarterly_market`. Use `get_leaseholds` and `get_epc_fabric_by_property_id` only when they materially affect the discussion.
3. Ask only for missing negotiation context that Propalt cannot know: offer amount, asking/target position, buyer proceedability/chain status, vendor priorities, competing interest, deadlines, and any declared limits.
4. Diagnose the evidence:
   - offer broadly supported and vendor expectation high;
   - offer low relative to evidence;
   - bridgeable middle ground;
   - gap currently unbridgeable.
5. Give a realistic evidence range rather than a false single-point certainty. Distinguish Propalt AVM output, comparable evidence, asking price, and the parties' negotiation positions.
6. Recommend sequencing and talking points. Use only genuine competing interest or urgency supplied by the user; never manufacture leverage.
7. Provide the internal strategy first. If requested, also produce a concise vendor call flow, buyer call flow, or draft message.

## Guardrails

- Never invent a party's maximum, motivation, chain position, affordability, or willingness to move.
- Do not state an AVM unless `get_valuation_by_property_id` returned one.
- Do not claim that a listing price equals market value. Prefer achieved comparable evidence when discussing market support.
- Avoid legal or financial guarantees. Keep the output as negotiation support for the agent.

## Output

Summarize: property evidence, offer gap, diagnosis, likely evidence-supported range, who may need to move and why, recommended sequence, key phrases, fallback if no agreement is reached, and uncertainties.
