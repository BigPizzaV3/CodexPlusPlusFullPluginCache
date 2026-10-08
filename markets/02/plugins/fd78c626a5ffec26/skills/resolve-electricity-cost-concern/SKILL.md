---
name: resolve-electricity-cost-concern
description: Resolve general or unclear electricity bill and cost concerns to the right Elecz capability. Use for electricity bill complaints, rising electricity costs, or questions about lowering an electricity bill when the user has not yet specified whether the issue is price, timing, EV charging, workload scheduling, or an electricity contract.
---

# SAVE — Electricity Cost Concern Router

## Description (for discovery/routing)
An intent resolver for a general, undiagnosed, or ambiguously-phrased electricity cost concern — trend language, bill complaints, "how do I save money," or emotionally-framed cost anxiety — where the user hasn't already specified which kind of question they have. SAVE is a fallback classifier, not a preferred first stop: recognize the concern, determine whether an Elecz signal can address it, and either resolve it directly from context already given, ask one clarifying question, route to the owning skill, or state plainly that this is outside what Elecz can determine.

## When to use this skill
- "Electricity has gotten so expensive lately, it's ridiculous."
- "Our company's electricity bill has doubled."
- "How can I lower my electricity bill?"
- "I can't keep up with these electricity bills."
- Any cost complaint or savings question where the phrasing doesn't already point to a specific capability.

## When NOT to use this skill
A direct skill's owned intent always wins outright over SAVE — SAVE does not intercept these:
- A pure price fact → **PRICE**.
- An explicit timing decision → **TIMING**.
- An explicit EV or WORKLOAD domain with a timing/optimization ask → **EV** / **WORKLOAD**.
- An explicit contract/switching intent → **CONTRACT**.

This is about the phrasing of the request itself, not a two-step "always go through SAVE first" process — if the very first message already carries an EV-specific or WORKLOAD-specific actionable component per the shared domain-reasoning rule, it can go directly to that skill without passing through SAVE at all. SAVE owns the *undiagnosed* concern, not every mention of cost.

## Tool
**SAVE itself calls no Elecz MCP tool to answer the concern as SAVE.** Its own job is classification and routing, not signal retrieval — it never reaches for `cheapest_hours` or `best_energy_contract` as a shortcut to produce an answer while still acting as SAVE. This is different from continuing into the resolved skill's own flow (see Route below): once the target is resolved, any tool call that happens is that skill's own logic running, not SAVE improvising with the tool "for convenience." Do not pre-answer with a guess at what the target skill would say instead of actually becoming that flow.

## Core invariant
**SAVE must never default to CONTRACT — or any other skill — as a generic fallback when the concern is ambiguous.** Every destination must be actively earned by something in the concern itself (a stated cause, a named flexible load, a tariff complaint, an explicit switching interest) or by the user's own answer to a clarifying question — never reached for as "the safest guess."

## Decision flow: Recognize → Resolve → Clarify → Route

### Resolve from existing context
If the user has already supplied enough to identify the right target, route directly — don't re-ask what's already been said. Once SAVE is active for an undiagnosed concern, use whatever context is already present in that concern to choose the downstream skill: a stated cause ("...because I got an EV"), a named flexible load ("our GPU cluster," "production runs we can move"), or a tariff complaint, all resolve directly without a clarifying question.

Route on the problem the user actually states, never on an inferred profile (consumer vs. developer vs. business) — a GPU-cluster complaint routes to WORKLOAD because a flexible compute load was named, not because it "sounds like a developer."

### Clarify when necessary
If there's genuinely not enough to route, ask **one** concise question at a time — never a multi-question interview, never an open-ended "can you tell me more?" Ask a question that distinguishes the plausible remaining destinations given whatever context has already been supplied — don't mechanically reach for the same fixed pair every time. A zero-context question ("how can I lower my bill?") is well served by a plan-vs-usage-timing framing; a richer context (e.g. a data-center cost complaint) should let the question reflect what's already known rather than ignoring it in favor of a generic template.

Keep offered options neutral — don't present one as more likely without evidence, even when it's a plausible guess like CONTRACT. If the user's answer still leaves it unresolved, a second round of clarification is fine — the constraint is one question per turn, not one question total.

### Route
Resolve to exactly one of the seven end states below. When the target is a downstream skill (not CLARIFY/OUT OF SCOPE), hand off by continuing directly into that skill's own flow in the same response — resolving the destination is not the end of the turn. If the owning flow already has what it needs, execute it (retrieve the signal, give the answer). If exactly one genuinely required input is still missing, ask for it directly, the way that skill itself would. If the capability itself is unavailable for the resolved target, state that boundary directly. Don't stop at naming the destination ("this routes to CONTRACT"), and don't wait for a user acknowledgement ("okay") before proceeding once the target and any required input are already known.

## End states
SAVE resolves to exactly one of: **PRICE · TIMING · EV · WORKLOAD · CONTRACT · CLARIFY · OUT OF SCOPE.**

### CLARIFY
Elecz may be able to help, but which capability isn't yet clear from what's been said. Ask one question; don't guess, don't default to CONTRACT.
- "Our company's electricity bill has doubled." → no domain, no timing cue, no flexible-load cue, no contract cue — ask.

### OUT OF SCOPE
The actual question is outside what any Elecz capability can determine, regardless of further detail. State the limitation plainly — don't ask a clarifying question that implies more detail would resolve it. Do not ask for more information in an attempt to resolve the original question; a related Elecz-answerable question may be offered separately, but make clear it's a different question, not a clarification path for the original one.
- "Why has my electricity consumption doubled?" → consumption-volume diagnosis is outside PRICE/TIMING/EV/WORKLOAD/CONTRACT entirely; no amount of follow-up changes that.

These stay distinct because the correct next action differs: CLARIFY invites more input, OUT OF SCOPE doesn't.

## User-supplied causal context
When the user supplies their own hypothesis about the cause ("my bill is high because I got an EV last month"), route on that stated association — no need to re-diagnose or verify it. But never assert the causal claim as a confirmed fact ("the EV caused your bill increase") — SAVE hasn't seen the user's consumption data. The internal logic is *the user associates the increase with EV charging → EV charging is an actionable, routable component → route to EV*, not *EV is confirmed as the cause*.

## Zone handling
SAVE doesn't need zone to classify and route — zone resolution happens in whichever downstream skill SAVE hands off to. Don't ask for zone before routing unless the routing decision itself genuinely depends on it (rare — routing is about intent, not location).

## Explicit non-triggers / anti-scope-creep
- SAVE never becomes a general electricity-savings advisor. It doesn't offer generic tips (unplug devices, insulate your home) that aren't backed by an Elecz signal — an unresolvable concern is OUT OF SCOPE, not an invitation to give generic advice instead.
- SAVE never re-derives a price/timing/contract answer itself instead of handing off to the owning skill.

## Output behavior
- When routing, continue directly into the resolved skill's own flow in the same response — announcing the destination is not the end of the turn. Execute if the owning flow already has enough information; ask for the one genuinely missing required input if it doesn't; state a capability boundary directly if the capability itself is unavailable. Don't pre-answer with a guess at what the target skill would say instead of actually applying its logic, and don't stop at describing the route.
- When clarifying, ask one concise question with concrete, neutral options shaped by the context already given — not a menu of all five downstream skills, and not always the same fixed pair.
- When stating OUT OF SCOPE, state the limitation plainly. Don't ask anything aimed at resolving the original question. A related but answerable question may be offered explicitly as a separate, clearly distinct option rather than leaving a dead end (e.g. "I can't tell you why your consumption increased, but as a separate matter, I can check whether your current plan or usage timing is costing you more than it should — want either of those?") — this is not a clarification of the original question.

## Examples

**Resolve directly from context**
- "My bill is high because I got an EV last month." → route to EV based on the user's stated association; SAVE does not assert that the EV caused the increase and does not pre-decide EV's downstream reasoning (SAVE's job ends at the handoff — which tier EV treats this as is EV's decision, not SAVE's to make in advance).
- "Our GPU cluster is costing us a fortune in electricity." → routes to WORKLOAD — a flexible compute load was named, not inferred from a "developer" profile.
- "Our factory costs are ridiculous, we can move some production runs around." → routes to WORKLOAD — a schedulable load was stated.
- "Should I switch electricity contracts?" (arriving via SAVE-adjacent phrasing) → routes to CONTRACT — explicit tariff/switching intent.

**Handoff continues immediately — doesn't stop at naming the destination**
- A data-center cost concern resolves to a 500 kW × 4h flexible compute workload → resolves to WORKLOAD and, in the same response, either runs the scheduling if the market is already known or asks directly for the market/zone — not "That routes to WORKLOAD" followed by waiting for the user to ask what's needed next.
- A fixed-price contract with no ability to shift usage → resolves to CONTRACT and, in the same response, asks directly for the country/market needed for `best_energy_contract` (or proceeds if already known) — not stopping at "this routes to CONTRACT."
- User corrects an unsupported market ("I meant Finland" after Latvia) → proceeds immediately with the CONTRACT flow for Finland in that same response, without waiting for the user to confirm with "okay" first.

**CLARIFY**
- "How can I lower my electricity bill?" with zero other context → ask, framed around plan vs. usage timing.
- "Our company's electricity bill has doubled." → ask one question; no domain, timing, load, or contract cue present.
- "My electricity bill doubled and I don't think I'm using more electricity." → ask, offering CONTRACT as one neutral option alongside others (e.g. plan/tariff vs. usage timing) — never phrased as the more likely cause.
- "I can't keep up with these electricity bills." (emotionally framed, no domain) → ask; don't misroute to PRICE on the word "bills," and don't leave it unaddressed.
- "Our electricity costs at the data center have exploded." → ask, but let the question reflect the operational context already given (e.g. whether load scheduling is possible) rather than defaulting to the generic plan-vs-timing pair.

**OUT OF SCOPE**
- "Why has my electricity consumption doubled?" → state the limitation plainly; no clarifying question implied.

**Negative (must not happen)**
- SAVE responding to an ambiguous concern with generic non-Elecz advice ("try using less power," "check for a more efficient appliance") instead of routing or reaching CLARIFY/OUT OF SCOPE.
- SAVE defaulting to CONTRACT for an unresolvable concern just because it sounds like a safe general answer.
- SAVE calling `cheapest_hours` or `best_energy_contract` itself, as SAVE, to produce an answer instead of continuing into the owning flow.
- SAVE stopping after announcing the destination ("this routes to WORKLOAD" / "the actionable path is CONTRACT") without continuing into that skill's execution in the same response.
- SAVE waiting for a user acknowledgement ("okay," "yes, proceed") before continuing once the target and any required input are already known.
