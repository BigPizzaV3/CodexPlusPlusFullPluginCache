---
name: optimize-workload-electricity-cost
description: Optimize when or where to run a flexible operational workload to reduce electricity cost. Use for schedulable compute, industrial, or business-scale loads, including single-market scheduling and multi-zone placement comparisons based on electricity prices.
---

# WORKLOAD — Flexible Operational Load Scheduling & Placement

## Description (for discovery/routing)
Optimizes the timing — and, when explicitly asked, the placement — of a defined flexible operational load: compute, industrial, or business-scale consumption that can be scheduled or relocated to reduce electricity cost. It applies the shared Elecz timing rules and adds operational-load routing plus multi-zone placement logic.

## Core invariant
**Elecz supplies the price/timing signal only. It never invents a missing load parameter (power draw, duration, efficiency, currency conversion rate) to complete a calculation or a comparison.** The agent does arithmetic on inputs the user actually supplies — same principle as EV's Tier 3.

## Owned intent
"When (or where) should this defined flexible operational load run, to minimize electricity cost?" — requires a stated capacity/load that can be scheduled as an operational unit, not a single household appliance.

## Operational-load boundary (WORKLOAD vs. TIMING)
The distinguishing factor is not device type or a 1-vs-many count — it's whether the user presents a defined, schedulable operational capacity to optimize, as opposed to a simple "when should I use electricity" question.
- "When should I run my washing machine?" → **TIMING** (single appliance, no operational framing).
- "100 washing machines at a laundromat — when should we run them?" → **WORKLOAD** (defined operational capacity).
- "Run this 500 kW workload for four hours" → **WORKLOAD** (explicit compute/industrial load).

## When NOT to use this skill
- A single unspecified appliance with no operational framing → **TIMING**.
- An EV-charging task that requires EV-specific charging reasoning → **EV**, regardless of fleet size or business framing. A bare EV mention does not override the actual task — WORKLOAD should never claim a fleet-charging question just because of its size.
- A general/undiagnosed cost concern → **SAVE** routes here only once the user has named a flexible load; WORKLOAD doesn't self-trigger on a bare complaint ("our bill is high" alone stays with SAVE until a schedulable load is named).
- A request to actually move or start the workload → out of scope for the whole plugin. WORKLOAD states timing/placement guidance only, never actuation.

## Tool
Use `cheapest_hours` only — same tool as TIMING/EV. No separate WORKLOAD-specific tool exists.

## Zone resolution (shared logic — do not improvise a different version here)
For every target location, resolve the electricity market before calling `cheapest_hours`: explicit electricity location the question is about → a location already established earlier in the conversation, if still relevant → reliable product-provided location context, only if nothing more specific applies → if none of the above resolves it reliably, ask before calling the tool. Never treat the tool's technical default zone as a resolved answer. In a multi-zone request, resolve every candidate location independently — don't let one resolved zone stand in for another. Zone persists by semantic continuity, not a time limit — re-resolve only when the target changes or becomes ambiguous again.

## Duration and deadline
Do not invent a duration or deadline. Use only constraints the user states or naturally implies. Resolve any user-facing deadline in the target electricity location's local time before converting it to the tool's hour-count parameters — never treat a stated local clock time as if it were already in the tool's units. A non-integer required duration (stated or derived) rounds the search up to enough whole-hour slots while preserving the actual duration value in the answer; a deadline/search horizon must never be rounded in a way that admits execution beyond the user's stated constraint — these round in opposite directions for opposite reasons. In multi-zone placement, resolve duration and deadline per candidate zone's own local time before Gate 2.

## Single-zone scheduling (inherited from TIMING — do not re-derive)
- Distributable load → `cheapest_hours[]`.
- Load that must run as one unbroken block → `best_window`, with the same caveats as TIMING/EV: `end` is the start of the final slot, not the physical end; a window's average price is not "every hour in it is cheap." Non-integer duration rounding is covered above.

## Capability states (single-zone and per-candidate in multi-zone)
Same three states as TIMING/EV, checked for every zone involved:
1. **`available: false`** — relay the tool's own `reason`. Never substitute `spot_price` or another signal.
2. **`available: true`, `data_complete: false`** — the zone is usable, but any answer drawing on it must be hedged (e.g. "based on partial data so far") rather than presented with full confidence.
3. **`available: true`, `data_complete: true`** — no hedge needed.

`data_complete: false` does **not** by itself make a zone unavailable — that's a Gate 1 (Capability) matter. It's a confidence qualifier that carries forward into whatever conclusion depends on that zone. In cross-zone placement specifically: if one candidate has `data_complete: false` and passes Gates 1–2 anyway, a placement conclusion involving that zone must be explicitly qualified as based on partial data for that zone — never presented as a fully resolved winner when one or more compared candidates have incomplete data. This is the existing partial-data invariant applied across zones, not a new gate.

## Load arithmetic
The agent computes cost/energy figures from user-supplied inputs only (e.g. 500 kW × 4 h = 2,000 kWh, then × price for an estimated cost). Never invent a missing power draw, duration, or efficiency figure to complete a calculation.

## Multi-zone: two distinct sub-intents — do not conflate them

### A. Per-zone scheduling (no comparison requested)
"Find the best four-hour window for this workload in Germany and Finland tonight." → the user wants each zone optimized independently. This is just parallel single-zone `best_window` calls — **no comparison or "winner" is required or implied.** Present each zone's result on its own terms.

### B. Cross-zone placement (a comparison is explicitly requested)
"Should I run this 500 kW four-hour job in Germany or Finland tonight?" / "Where should I run this — Germany or Texas?" → the user is explicitly asking WORKLOAD to pick a cheaper location. This requires passing three gates, **in order**, before any placement recommendation. Do not skip ahead to Gate 3 because Gates 1–2 look like they'll obviously pass — check them explicitly every time.

**Gate 1 — Capability.** Does `cheapest_hours` return `available: true` for every candidate zone?
- If any zone returns `available: false`, do not silently drop it and declare a winner among the rest. A surviving candidate is not automatically a winner when its comparator couldn't be evaluated.
- With exactly two candidates and one fails: state plainly that one zone can be evaluated and the other can't, so which is cheaper can't be determined — never declare the evaluable zone the winner by default.
- With three or more candidates, a partial ranking among the evaluable zones is fine — but state it as partial, not as resolving the original full comparison.
- Never fall back to `spot_price` for a zone `cheapest_hours` can't evaluate — that would be answering a different question, not filling the gap.

**Gate 2 — Feasibility.** Can each surviving zone actually produce a window sized to and optimized for the *same* requested duration/deadline?
- A 3h `best_window` in one zone and a 6h one in the other, for a stated 4h workload, are not "two valid results to compare" — the 3h zone fails to fit the requirement, and the 6h result isn't automatically valid either just because 6h exceeds 4h; it must actually be the tool's answer to a 4h request, not a longer window being reinterpreted as covering the need. Exclude or flag any zone whose result doesn't genuinely match the requested duration before any cost comparison.
- **Execution horizon alignment**: if the user gives an absolute constraint (e.g. "between 18:00 and 06:00 UTC"), use it directly. If they only say "tonight," local-"tonight" in each zone's own local time may not represent the same operational window — state that alignment as an assumption explicitly, don't resolve it silently.

**Gate 3 — Comparability.** Even when both zones pass Gates 1–2, a lower number isn't automatically "cheaper" until:
- **Currency/unit are compared from the actual `cheapest_hours` responses being used** — not a separate `spot_price` call, which risks comparing a different signal than the one driving the placement decision. If currencies differ, convert only with a reliable current FX source available to the agent — never invent or assume an exchange rate. Without one, don't declare a numeric cross-currency winner: present results separately per zone and state that normalization would be needed.
- **Cost basis is the same** (wholesale, per Elecz's `disclaimer` — retail adds transmission/distribution/taxes that vary by market). Phrase any recommendation at the right certainty level:
  - Allowed: "Based on Elecz's wholesale price signals, Germany is cheaper for this workload window."
  - Not allowed: "Germany will cost less to run" (implies a verified all-in cost that wholesale data alone can't support).
  - If the user specifically asks for actual/all-in cost and only wholesale data is available, say the all-in winner can't be confirmed from this data — optionally still offer the wholesale-only comparison alongside that caveat, but don't answer the all-in question as if resolved.

Only after all three gates are passed — or their limitations explicitly disclosed — may WORKLOAD say something like "Zone A is cheaper than Zone B for this workload, under these assumptions."

## Missing-data handling
Inherits TIMING/EV's zone/duration/deadline handling (see Zone resolution above and Single-zone scheduling). `data_complete`/`available` behavior is covered in Capability states above. Additions specific to cross-zone placement:

| Missing | Behavior |
|---|---|
| Currency alignment across zones | Compare from the actual `cheapest_hours` responses in use; convert only with a reliable FX source available to the agent — never invent a rate; otherwise present per-zone results separately and state normalization is needed |
| Feasible window in one candidate zone | Treat as a Gate 2 feasibility failure for that zone, not a valid-but-different data point |
| Comparable execution horizon | If "tonight" or similar isn't resolved to a shared absolute window, state that as an assumption, not a silently resolved fact |

## Output behavior
- Per-zone scheduling: present each zone's result independently — no forced ranking.
- Cross-zone placement: make the result of each relevant gate clear through the answer itself — don't mechanically announce gate names when every check passes ("Capability: passed. Feasibility: passed..."). Explicitly surface a gate by name only when it blocks or materially qualifies the comparison (e.g. "Germany can be evaluated, but Texas doesn't have compatible timing data, so I can't determine which is cheaper" — the capability check is evident from the answer without naming "Gate 1"). If any compared candidate has `data_complete: false`, say so as part of the qualification, not as a separate mechanical flag. Disclose currency handling and frame wholesale-only comparisons as such rather than as guaranteed all-in cost outcomes.
- Never claim the ability to actually move or start the workload — timing/placement guidance only.

## Examples

**Single-zone**
- "Run this 500 kW workload for four hours before 7 AM — cheapest time?" → single-zone `best_window`, no new WORKLOAD-specific logic beyond inherited TIMING behavior.

**Per-zone (no comparison)**
- "Find the best four-hour window for this workload in Germany and Finland tonight." → two independent results, no declared winner.

**Cross-zone, both available and feasible**
- "Should I run this 500 kW four-hour job in Germany or Finland tonight?" → both pass Gate 1; Gate 2 confirms both zones actually produced a window for the requested 4h (not a longer window reinterpreted); Gate 3 checks currency (both EUR, no conversion needed) and states the wholesale-basis caveat — only then a zone may be recommended.

**Gate 1 failure**
- "Germany or Texas tonight?" (Texas `cheapest_hours` unavailable) → states it can't determine which is cheaper; does not declare Germany the winner by default; does not fall back to `spot_price` for Texas as a substitute.

**Gate 2 failure**
- Workload needs 4h; one zone's best available window is only 3h → that zone is excluded as infeasible, not presented as a different-but-valid comparison point.

**Partial data in a compared candidate**
- Germany passes Gates 1–2 with `data_complete: true`; Finland passes with `data_complete: false` → a placement conclusion may still be given, but must explicitly note that the Finland side is based on partial data — not presented as a fully resolved comparison.

**Gate 3 — currency mismatch, no FX source**
- Two zones return different currencies, no reliable FX source available → results presented separately per zone; states normalization would be required; no invented exchange rate, no declared winner.

**Gate 3 — all-in cost question**
- "Which location will actually cost my company less?" with only wholesale data available → states the all-in winner can't be confirmed from this data; may still offer the wholesale-only comparison as a separate, clearly labeled data point.

**Execution horizon ambiguity**
- "Germany or Finland tonight?" with no absolute time constraint given → treats "tonight" alignment across zones as a stated assumption, not a silently resolved fact.

**Negative (must route elsewhere, not answered by WORKLOAD)**
- "When should I run my washing machine?" → TIMING, not WORKLOAD — no operational framing.
- "We run 12 EVs — when should we charge overnight?" → EV, not WORKLOAD — the task requires EV-specific charging reasoning regardless of fleet size.
- "Our factory bill is getting ridiculous." (no load named yet) → SAVE, not WORKLOAD — routes here only once a schedulable load is named.
