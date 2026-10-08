---
name: find-best-electricity-time
description: Find the cheapest electricity hours or decide whether to use electricity now or wait in a supported market. Use for electricity timing and cheap/expensive judgments, not pure current-price facts, EV-specific charging decisions, workload scheduling, or contract questions.
---

# TIMING — Electricity Timing Decision

## Description (for discovery/routing)
Answers the electricity-price-relative decision: "is now a good time, or should I wait — and if so, for how long / until when?" This is a decision skill, not a data listing — always attempt an actionable answer to the timing question actually asked, without overstating certainty beyond what the data supports. Covers both present-moment judgment ("is it cheap now?") and forward-looking window-finding ("find me the cheapest hours"), as long as the requested task does not require reasoning owned by a more specific domain skill (such as EV or WORKLOAD) — a domain word alone, on a task that doesn't need that domain's reasoning, stays with TIMING.

## When to use this skill
- "Is electricity cheap/expensive right now?"
- "Should I use electricity now or wait?"
- "Is now a good time to run [a generic/unspecified appliance]?"
- "What are the cheapest hours today/tonight?"
- "Find me three cheap hours."
- "What's the cheapest N-hour window before [deadline]?"
- "When should I use electricity tomorrow?"

## When NOT to use this skill
- A pure current-price fact request with no relative judgment ("what's the price right now?") → **PRICE**.
- An explicit EV-charging context, where the task itself needs EV-specific reasoning (charging schedule, target SOC, departure time) → **EV**. A bare mention of "EV" on a task that doesn't actually need that reasoning (e.g. a generic timing question that happens to reference an EV in passing) stays with TIMING.
- A defined flexible operational load, where the requested task requires workload-specific scheduling reasoning (compute, industrial, business-scale scheduling) → **WORKLOAD**. A workload/domain mention alone does not override TIMING when the requested task only needs generic timing reasoning.
- A general/trend cost concern with no specific timing question ("bills have gotten so expensive") → **SAVE**.
- Contract or tariff questions → **CONTRACT**.
- A request to actually control or switch on a device → out of scope for the whole plugin. TIMING may state the best time to act, but must never imply it can carry out the action itself.

## Tool
Use `cheapest_hours` only. TIMING never calls `spot_price` — that's PRICE's tool.

## Core invariant
**Never invent a market, duration, deadline, or continuity requirement merely to complete an optimization.** Ask, or answer only what the available data actually supports — every rule below is an application of this.

## Zone resolution (shared logic — do not improvise a different version here)
Zone is a required input — TIMING cannot produce a meaningful answer without it, so resolve it before any tool call. Resolve in this order, stopping at the first that applies:
1. The explicit electricity location the question is actually about — this may differ from the user's physical location (e.g. asking about a home in Sweden while physically in Finland resolves to Sweden).
2. A location already established earlier in the conversation, if still relevant to this request.
3. Reliable product-provided location context, only if nothing more specific applies.
4. If none of the above resolves it reliably, ask one short question before calling the tool. Do not guess, and do not treat the tool's technical default zone as a resolved answer.

Zone persists by semantic continuity (the same target is still being discussed), not by a time limit — re-resolve only when the target changes or becomes ambiguous again.

## Duration, deadline, and continuity
- **Duration**: do not invent it. Ask only when a specific duration is required to answer the requested optimization. If the question can be answered usefully without assuming a task duration, do so without inventing one.
- **Deadline**: do not invent one — use only the horizon the request naturally implies ("tonight" → tonight, "tomorrow" → tomorrow). Ask only if an unstated deadline would materially change the optimization.
- **Continuity** (`cheapest_hours[]` vs. `best_window`): a distributable/interruptible task → `cheapest_hours[]`, never presented as a contiguous block. A task needing one continuous block of N hours → `best_window`, framed as "the lowest-cost available window for this duration," never as "N cheap hours" — if the window's average is high relative to the genuinely cheap hours, say so rather than calling it unconditionally cheap. If continuity is unspecified and doesn't materially affect the answer, default to `cheapest_hours[]`; if it would materially affect the answer, ask.

## `best_window` field handling
`best_window.end` is the start of the final slot, not the physical end of the covered interval (a 3-hour request returning `start: 21:00, end: 23:00` actually covers 21:00–00:00). Never present `end` as the session's physical end time — derive actual coverage from slot count. Resolve any user-facing clock time or deadline in the target zone's local time before converting it to the tool's hour-count parameters; never treat tool timestamps as already matching the user's stated local time.

## Capability states
1. **`available: false`** — relay the tool's own `reason` field. Do not improvise a reason, and do not fall back to `spot_price` as a substitute — if TIMING can't answer, say so rather than quietly answering a different question.
2. **`available: true`, `data_complete: false`** — give the best available answer, hedged (e.g. "based on partial data so far…"), not presented with full confidence.
3. **`available: true`, `data_complete: true`** — answer without the partial-data hedge.

## Present-moment decisions
Combine the current state with the next actionable option — never report the current state in isolation.
- Use `current_hour_is_cheap` / `current_hour_signal` / `current_hour_rank` for the "now" judgment.
- **Preserve the tool's own categorical state — don't upgrade it based on what's coming later.** `energy_state`/`current_hour_signal` values like `normal` or `medium` must not be reported as "expensive" merely because a cheaper hour exists later in the data. A cheaper time existing later is a *relative* fact (there's a better option ahead); the current price's own classification is a separate, *absolute* fact. Both can be said together ("prices are normal right now, but there's a cheaper window in about 3 hours") — but the categorical label itself must come from what the tool actually returned for the current hour, never inferred from the shape of the rest of the data.
- If now isn't good and the tool provides a next cheap period within the available data, use `hours_until_next_cheap` / `next_cheap_hour` to say when it starts. If the tool doesn't provide one within the published data window, say that the next better time can't be confirmed from the data available — never promise a next-cheap time the data doesn't actually cover.
- Apply the `data_complete` hedge above where relevant.
- Example shape: "Now isn't a great time — the next cheaper period starts in about 5 hours," not just "now is not cheap." Contrast: if `current_hour_signal` is `normal`, the correct shape is "prices are normal right now — there's a cheaper window later if you can wait," never "electricity is expensive right now."

## Output behavior
- State the resolved market on the first answer in a conversation, or whenever it changes or could otherwise be ambiguous. Don't repeat it on follow-ups clearly still about the same target.
- Make it clear through the content of the answer itself whether it's a present-moment judgment or a window recommendation — not with a separate meta-label ("This is a window recommendation..."). The phrasing should make the type obvious without announcing it.
- Never claim the ability to act (start/stop a device) — TIMING states timing only.
- The number of slots returned in `cheapest_hours[]` is a query/output choice controlled by the `hours` parameter, not evidence of the user's required duration — never imply "you should use electricity for these N hours" when no duration was requested; frame results as "these are the lowest-price hours available."

## Examples

**Positive**
- "Is electricity cheap right now?" → `cheapest_hours`, resolve zone, present-moment judgment + next-cheap-hour context if not currently cheap.
- "Find me three cheap hours tonight." → `cheapest_hours[]`, scoped to tonight, non-contiguous list.
- "What's the cheapest 4-hour window before 7 AM?" → `best_window`, framed as lowest-cost available window, not as four individually cheap hours.

**Negative (must route elsewhere, not answered by TIMING)**
- "What's the electricity price right now?" → PRICE, not TIMING.
- "Should I wait before charging my EV?" → EV, not TIMING (the requested task is EV-charging timing).
- "Electricity has gotten so expensive lately." → SAVE, not TIMING.

**Zone edge case**
- "I'm in Finland, but should I run the dishwasher at my apartment in Stockholm now?" → resolve to Sweden (the electricity location asked about), not Finland (the user's physical location); clarify the Swedish price zone if not otherwise resolvable.

**Data-quality / missing-input edge cases**
- No zone, no context at all → ask; never default to the tool's technical zone.
- `current_hour_is_cheap: false` → include next-cheap-hour context when the tool provides it within the available data window; otherwise state that the next better time can't be confirmed from the data available.
- `current_hour_signal: normal` (or `medium`) with a cheaper hour later in the data → report "normal," not "expensive." A better option existing later doesn't change what the current hour's own classification is.
- `best_window` requested at a size exceeding genuinely cheap hours → must not claim the whole window is "cheap."
- "Find me the cheapest time to run this job" with no stated duration → ask for duration rather than silently defaulting to `cheapest_hours[]`.
- "Cheapest hours today" → scope to today; do not silently substitute a 24h-forward default.
