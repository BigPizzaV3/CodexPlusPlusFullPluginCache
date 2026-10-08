---
name: get-electricity-price
description: Get the current electricity price or spot price for a supported electricity market. Use for factual present-moment electricity price questions, not timing, cheap/expensive judgments, EV charging decisions, or contract comparisons.
---

# PRICE — Current Electricity Price

## Description (for discovery/routing)
Answers a single factual question: "What is the electricity price right now?" Returns the current wholesale spot price for a specified or resolved electricity market — nothing more. Does not judge whether the price is cheap or expensive, does not recommend waiting or acting, does not compare contracts. If the user's question requires any of those, this is not the right skill.

## When to use this skill
Use PRICE when the user wants a plain, present-moment price fact:
- "What's the electricity price right now?"
- "How much does electricity cost now?"
- "What's the current spot price in Germany?"
- "What's electricity trading at right now?"
- "What's the electricity price right now for my EV charger?" (a domain word is present, but the task is still a plain fact request, not EV-specific reasoning)
- "What's the current electricity price at our data center?" (same — domain named, but no scheduling/optimization reasoning required)

## When NOT to use this skill
- The user asks a *relative* judgment — "is it cheap/expensive right now?", "is now a good time?" → route to **TIMING**. `spot_price` has no cheap/normal/expensive classification. Do not invent one.
- "Should I use electricity now or wait?" → **TIMING**.
- A general or trending cost concern — "my bills have gotten so expensive lately", "electricity is ridiculous these days" → **SAVE**. This is not a present-moment fact request.
- Contract or tariff comparison, or switching providers → **CONTRACT**.
- A domain-specific question that actually needs domain reasoning (target SOC, deadline, scheduling a load) rather than a plain number — e.g. "Is now cheap for charging my EV?" → **EV**, not PRICE. The presence of a domain word (EV, data center, fleet, etc.) does not by itself redirect a plain fact request away from PRICE, and it does not by itself send a genuinely domain-reasoning question to PRICE either. What decides it is whether the task needs domain-specific reasoning to answer — not whether a domain word appears.

## Tool
Use `spot_price` only. Never call `cheapest_hours` from PRICE. Relative judgment and forward-looking reasoning are outside PRICE's scope.

## Zone resolution (shared logic — do not improvise a different version here)
Resolve the electricity market in this order, stopping at the first that applies:
1. An explicit electricity location stated in the request — this is the location the *price* is about, which may differ from where the user physically is.
2. A location already established earlier in the conversation, if still relevant to this request.
3. Reliable location context provided by the product/platform, only if nothing more specific applies.
4. If none of the above resolves it reliably, ask one short clarifying question. Do not guess.

Do not treat the tool's technical default zone as a user default. Zone persists across a conversation by semantic continuity (the same target is still being discussed), not by a message-count or time limit — re-resolve only when the target changes or becomes ambiguous again. Getting the zone wrong here is just as much a wrong answer as getting it wrong in a timing or contract decision, even though PRICE itself is a simple skill — do not simplify this logic because the rest of the skill is thin.

**Do not call `spot_price` with a guessed or default zone when the location is genuinely unresolved — ask first.** Calling the tool on a guessed zone "to get something" and only checking for ambiguity afterward is the failure mode this rule exists to prevent.

## Core invariant
**Never invent a market/zone, a staleness/confidence judgment, or a price interpretation merely to complete an answer.** Every rule below is an application of this.

## Data quality / freshness handling
`spot_price` returns `age_seconds`, `stale`, `source`, `fallback`, and `disclaimer`.
- If `stale: true` or `fallback: true`, say so plainly in the answer — do not present the number as live current-moment ground truth without that caveat.
- Surface the content of `disclaimer` in your own words whenever it materially affects how the number should be read (most commonly: this is a wholesale price, retail price includes taxes/transmission/distribution on top). Don't drop it for brevity when it matters.
- Do not invent your own staleness threshold from `age_seconds`. Rely only on what `stale` and `fallback` themselves indicate.

## Output behavior
- State the resolved market (and unit/currency) on the first answer in a conversation, or whenever the market changes or could otherwise be ambiguous. Don't repeat it mechanically on every follow-up turn that's clearly still about the same market ("what about now?").
- Only mention freshness/source context when it changes how the number should be read (stale, fallback, or a disclaimer that matters here). Don't pad a fresh, unremarkable answer with it.
- If the requested market/zone isn't covered by `spot_price`, relay what the tool actually returns (or say plainly that it can't be retrieved) rather than guessing a plausible-sounding number.

## Examples

**Positive**
- "What's the electricity price right now?" → `spot_price`, resolve zone, state price/unit/currency/market.
- "What's the current spot price in Germany?" → `spot_price` for DE, no judgment added.
- "What's the electricity price right now for my EV charger?" → `spot_price`, plain fact, no EV-specific reasoning added.

**Negative (must route elsewhere, not answered by PRICE)**
- "Is electricity expensive right now?" → TIMING (`cheapest_hours`), not PRICE.
- "Electricity has gotten so expensive lately, it's ridiculous." → SAVE, not PRICE.
- "Is now cheap for charging my EV?" → EV, not PRICE — this needs the timing/domain reasoning `spot_price` alone can't supply.
- "Should I switch electricity contracts?" → CONTRACT, not PRICE.

**Data-quality edge cases**
- Tool returns `stale: true` → flag staleness explicitly in the answer.
- Tool returns `fallback: true` → note the fallback explicitly rather than presenting it as a normal live read.
- Zone ambiguous or conflicting with the user's physical location (e.g. user is physically in Stockholm asking about Finnish electricity) → resolve to the *electricity location* actually asked about, not the user's physical location; ask if genuinely unresolved.
