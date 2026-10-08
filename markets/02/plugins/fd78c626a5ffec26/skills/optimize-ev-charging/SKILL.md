---
name: optimize-ev-charging
description: Optimize EV charging timing using electricity prices. Use when the user asks when to charge an electric vehicle, whether to charge now or wait, or how to schedule EV charging around a deadline, required charging duration, battery state of charge, or charger power.
---

# EV — Electric Vehicle Charging Timing

## Description (for discovery/routing)
Answers electricity-price-relative charging decisions for a stated EV context, at whatever level of specificity the user provides — from a simple "when's cheap to charge tonight?" through a fixed deadline, up to full duration/SOC-constrained optimization. EV is not "TIMING plus the word EV," and it is not a full EV energy calculator: Elecz supplies the price/timing signal only; the agent does arithmetic (e.g. kWh ÷ kW) on inputs the user actually supplies. EV must never invent a missing input — SOC, battery capacity, charging power, or duration — to complete an optimization it wasn't given enough information to solve.

## Core invariant
**A charging deadline tells EV when charging must finish. It does not tell EV how long charging takes.** These are two different pieces of information — never let one substitute for the other, and never derive a duration from a deadline alone.

## When to use this skill
Any "when should I charge my EV" question, at any of three specificity tiers, where the task genuinely involves EV-charging timing reasoning:
- "When should I charge my EV tonight?" / "Is now cheap for charging my EV?" (Tier 1 — no constraints given)
- "I need the car ready by 7 AM — when should I charge?" (Tier 2 — deadline given, duration unknown)
- "I'm at 30%, need 80% by 7 AM. When should I charge?" (Tier 3 — energy/SOC-constrained)
- A fleet or business-scale EV-charging task that requires EV-specific charging reasoning stays EV, not WORKLOAD — scale or business framing does not override the task-relevant EV domain.

## When NOT to use this skill
- A pure current-price question that happens to mention EV/charging, with no timing or optimization request → **PRICE** ("what's the price right now for my EV charger?" — the task is a plain fact request, not charging-timing reasoning).
- A generic timing question with no stated device or charging context → **TIMING** ("should I wait before charging?" with nothing identifying an EV).
- A general cost complaint the user associates with EV ownership, with no timing question yet → **SAVE** routes here; EV doesn't self-trigger on the complaint alone ("my bill is high because I got an EV" is SAVE's routing decision to make, not EV's to intercept).
- A domain-word mention alone, on a task that doesn't actually need EV-specific reasoning, does not pull the question into EV — the deciding factor is always whether the task needs EV reasoning (deadline, SOC, charging schedule), not whether the word "EV" appears.

## Tool
Use `cheapest_hours` only — the same tool as TIMING; there is no separate EV-specific tool. Never invent data the tool doesn't provide (no SOC, battery capacity, charging-power, or efficiency data exists in Elecz).

## Zone resolution (shared logic — do not improvise a different version here)
Same hierarchy as PRICE/TIMING: explicit electricity location → established conversation context → product-provided location → clarify. The charging location may differ from the user's stated physical location (e.g. charging at a second home or workplace in a different zone) — resolve to the charging location, not the user's presence. Ask before calling the tool if genuinely unresolved; never treat the tool's technical default zone as a resolved answer.

## Tier 1 — Generic charging timing (no constraints given)
Give a useful charging-context price signal without inventing duration or continuity: surface the cheapest available hour(s) within the horizon the request specifies or naturally implies (`cheapest_hours[]`) — the same rule TIMING uses for deadlines. If the request states or implies a horizon ("tonight," "tomorrow"), use it. If no horizon is stated or implied at all, don't invent one (e.g. don't default to "tonight") — use the tool's own default coverage as-is. The returned hour count is a query default, not a stated duration requirement — phrase the answer as "these are the lowest-price hours available," never as "you should charge for these N hours."

If the user might want the full charging session optimized as one continuous block, **offer** that explicitly rather than assuming it: "here are the cheapest charging hours available in that period; if you tell me how many hours of charging you need, I can find the best single window for that." Don't silently guess a duration or continuity requirement on their behalf.

## Tier 2 — Deadline-constrained charging (duration unknown)
A deadline is a horizon boundary, not a duration — see the core invariant above.
- Resolve the deadline in the **charging location's local time** before converting it to the tool's hour-count `window` parameter. Never treat a user-stated local clock time as if it were already UTC or as if it directly matches the tool's parameter units — compute hours-until-deadline in local time first.
- With duration unknown, use the deadline only to bound the search horizon and surface the cheapest available hour(s) before it. Do not construct a complete charging plan and do not call `best_window` with an invented duration.
- Ask for the required charging duration only when the user is specifically asking for the optimal timing of the *entire* charging session — deadline proximity alone is not a reason to ask.

## Tier 3 — Energy/SOC-constrained charging
This tier needs a charging *duration*, which Elecz doesn't have on its own. Duration confidence, strongest to weakest:
1. **Stated duration** ("it usually takes about 4 hours") — use as-is.
2. **Stated energy + charging power** ("I need 40 kWh, charger does 11 kW") — the agent calculates duration (kWh ÷ kW), not Elecz.
3. **SOC + battery capacity + nominal charger power** — an *estimate only* (ignores losses and charge-rate tapering near full). Present it explicitly as an estimate, not a guarantee.

If the user hasn't supplied enough for at least level 3, ask for the **minimum missing input set in one concise question** — not a multi-round interview (e.g. ask for battery capacity and charging power together, not one at a time). Never invent typical battery capacity, charging power, or efficiency figures.

### Rounding for non-integer required duration
`cheapest_hours`'s `hours` parameter is an integer — a required duration that isn't a whole number (whether **stated** directly by the user, e.g. "charging takes about 3.5 hours," or **derived** by the agent from kWh ÷ kW) can't be passed to the tool as-is.
- **Required duration** (stated or derived): preserve the actual duration value in what you tell the user, but round the *search* up (ceil) to the next whole hour of `hours` slots. Disclose this as conservative slot-level scheduling, not sub-hour optimization — e.g. "your ~3.5h charging need is optimized across four hourly price slots," never phrased as if a 3.5-hour window itself was found.
- **Deadline/search horizon**: never round in a way that admits slots beyond the user's actual deadline. If the deadline is 6h20m away, the horizon must not be extended to 7h to reach a clean integer — round the horizon down/conservatively if anything, never past the stated constraint.
- These round in opposite directions for opposite reasons: required duration rounds up to guarantee enough search coverage; horizon never rounds past what the user actually allowed.

## `best_window` field handling
`best_window.end` is the start of the final slot, not the physical end of the covered interval — a requested 3-hour window returning `start: 21:00, end: 23:00` actually covers 21:00–00:00 (three full hourly slots). Never present `end` as the physical end time of charging; derive the actual end of coverage from slot count when telling the user when charging will finish.

## Missing-data handling
| Missing | Behavior |
|---|---|
| Zone | Resolve per shared hierarchy; ask if unresolved — required |
| Duration/deadline (Tier 1) | Not needed — surface cheapest available hours; offer, don't assume, a full-session window if duration is given |
| Deadline only, duration unknown (Tier 2) | Use deadline as search horizon only; never construct a full plan or call `best_window` with an invented duration |
| Charging duration inputs (Tier 3) | Never invent capacity, power, efficiency, or duration; ask for the minimum missing input set in one question if below confidence level 3 |
| Non-integer required duration (stated or derived) | Preserve the actual duration; round the search up, round horizon conservatively (never past the deadline); disclose the rounding |
| `data_complete: false` | Hedge the answer, same as TIMING |
| `available: false` | Relay the tool's `reason`; never substitute another signal |

## Output behavior
- State the resolved market on the first answer in a conversation; don't repeat it mechanically on follow-ups about the same target.
- Tier 1: cheapest available hours, framed for charging, with an explicit invitation — not an assumption — to specify a duration for a full-session window.
- Tier 2: cheapest hours before the deadline, explicitly not presented as a complete charging plan; invite duration only if the user wants full-session optimization.
- Tier 3: show the derived duration and its confidence level (stated / calculated / estimated) briefly so the user can sanity-check it, then give the timing recommendation. If rounding was applied, state that explicitly.
- Never state or imply a specific cost estimate unless the user has supplied the numbers needed to compute it (kWh and price) — don't assume typical EV consumption figures.

## Examples

**Tier 1**
- "When should I charge my EV tonight?" → cheapest available hours tonight, offer full-session optimization if a duration is given, no SOC/capacity questions asked.

**Tier 2**
- "I need the car ready by 7 AM." (no duration stated) → deadline used as search horizon only; no full plan constructed; asks for duration only if the user wants the whole session optimized.

**Tier 3**
- Follow-up after an EV timing request: "It usually takes about 4 hours to charge from 30% to 80%." → use the stated duration directly, no further questions.
- "I need 40 kWh and my charger does 11 kW — when should I charge?" → agent derives ≈3.6h, EV rounds up to a 4-hour search window and states both the calculated duration and the rounding, phrased as "optimizing across four hourly price slots," never as a sub-hour-optimal 3.6h window.
- "I'm at 30%, need 80% by 7 AM." with no capacity/power given → asks for usable battery capacity and charging power together in one question; if later supplied, presents the resulting duration as an estimate, not a guarantee.

**Negative (must route elsewhere, not answered by EV)**
- "What's the electricity price right now for my EV charger?" → PRICE, not EV — plain fact request.
- "Should I wait before charging?" (no device stated) → TIMING, not EV — domain not explicit.
- "My bill is high because I got an EV." → SAVE routes this; EV doesn't self-trigger on the complaint alone.

**Fleet/scale**
- "We run 12 EVs — when should we charge the fleet overnight?" → still EV, not WORKLOAD — the task needs EV-specific charging reasoning regardless of fleet size or business framing.

**Discipline checks**
- EV must never state a typical/assumed battery capacity, charging power, consumption, or duration figure on its own initiative.
- EV must never call `cheapest_hours` with a non-integer `hours` value or silently truncate a stated or derived duration without disclosing the rounding.
- "Ready by 7 AM" at the charging location must be resolved in the charging location's local time, converted to an hours-until-deadline horizon — never treated as UTC.
- A `best_window` response with `start: 21:00, end: 00:00` for a 4-hour request must be conveyed as the full ~4-hour coverage the slot count implies, never as a 3-hour span read naively from `start`/`end`.
