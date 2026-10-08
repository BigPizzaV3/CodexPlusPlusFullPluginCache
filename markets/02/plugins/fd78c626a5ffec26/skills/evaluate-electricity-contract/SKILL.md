---
name: evaluate-electricity-contract
description: Evaluate whether to switch electricity contracts or whether spot or fixed electricity is the better option in a supported market. Use for electricity contract, tariff, provider-switching, and personalized contract-savings questions, not current-price facts or electricity-use timing.
---

# CONTRACT — Electricity Contract Evaluation

## Description (for discovery/routing)
Evaluates whether a user should switch electricity contracts, or which contract type suits them, using `best_energy_contract`. Unlike the timing-family skills, CONTRACT doesn't share their continuity/duration logic — its own risks are capability-mode handling, using the tool's full recommendation structure rather than a single summary field, and never treating backend default inputs (consumption, heating) as user-stated facts.

## When to use this skill
- "Should I switch electricity contracts?"
- "Is spot or fixed better for me?"
- "What's the best electricity contract available?"
- Explicit contract/tariff evaluation intent.

## When NOT to use this skill
- A pure price fact → **PRICE**.
- A timing/usage-pattern question with no contract framing → **TIMING**.
- EV/WORKLOAD-specific timing → **EV** / **WORKLOAD**.
- An undiagnosed general cost concern → **SAVE** may route here, but CONTRACT doesn't self-trigger on an ambiguous complaint alone.

## Tool
Use `best_energy_contract` only.

## Core invariant
**Never invent a missing input, and never treat a backend default as a user-stated fact.** The tool's `assumptions` object tells you the actual source of every input it used — defer to it rather than assuming what "typical" values should be.

## Capability modes
Branch directly on the `contract_comparison` field — this is a deterministic field check, not an inference from which other fields happen to be present.

**Mode 1 — `contract_comparison: "available"`**
Returns `best_spot`, `best_fixed`, `recommended` (with `contract` + `reason`), `decision_hint`, a top-level `reason`, an `action` object (`available`, `expected_savings_local_year`, `savings_basis`, `confidence`, `confidence_basis`, `status`, `action_link`, `provider`, `contract_id`), an `assumptions` object, and sometimes a `disclaimer`.

**Mode 2 — `contract_comparison: "not_available"`**
Use whatever tariff/price fields are actually present plus the `note` field. Response richness varies by market — don't assume any particular subset of fields beyond `contract_comparison` and `note` will be there; relay what's given. Never fabricate a recommendation or action link in this mode, and never apologize for a missing capability the market itself doesn't support — state the regulated structure plainly using the tool's own explanation.

## Recommendation integrity (Mode 1)
`decision_hint` (e.g. `spot_recommended`, `switch_recommended`, `stay_spot`, `consider_fixed`, `compare_options`) is a summary label, not the whole answer. Draw on the full object:
- `recommended.contract` — which contract, `recommended.reason` — why.
- `action.available` — whether an actionable switch exists at all.
- `action.expected_savings_local_year` + `action.savings_basis` — the estimate and what it's measured against.
- `action.confidence` + `action.confidence_basis` — relay the basis text (in your own words) alongside the number. It documents a simple heuristic, not a statistical measure — use it directly rather than inventing independent certainty language.
- `action.status`.
- Any `disclaimer` — surface it, don't drop it for brevity; it can materially affect whether the savings estimate is complete (e.g. excluding a regional grid fee).

**Consistency checks (apply on every Mode 1 response):**
- If `recommended`, `decision_hint`, the top-level `reason`, and `action` visibly disagree with each other, do not present a single confident recommendation. Surface the disagreement instead — state that a recommendation exists but the fields describing it don't agree, without picking one side, averaging, reconciling, or guessing which is right.
- Before presenting `action.action_link` as the routing destination, check that `action.provider` / `action.contract_id` match `recommended.contract.provider`/`.id`. If they disagree, do not present the action link as a valid next step — state that a recommendation exists but the action destination couldn't be verified, and never guess which provider or link is correct.

**Link integrity (applies whenever `action.action_link` is presented):**
Present `action.action_link` exactly as returned — verbatim, including every query parameter. Never strip, simplify, "clean up," reformat, shorten, or reconstruct the link, and never substitute a provider's general website or homepage URL in its place, even if the returned link looks long, unfamiliar, or contains tracking parameters. Those parameters are the attribution mechanism for the recommendation — altering or dropping them breaks it silently, with no visible error. This rule holds regardless of how the link is rendered (plain text, markdown link, button) — the underlying URL string itself must be untouched.

## Consumption and heating: check before calling, don't assume
The `assumptions` object (once the tool is called) states each input's actual source, e.g. `{"annual_consumption_kwh": 2000, "consumption_source": "zone_default", "heating": "district", "heating_source": "default"}` when unspecified, vs. `"user_provided"` when supplied. But don't wait for the tool call to decide whether to ask — determine this from the request itself first:

- **Personalized question** ("how much would I save?" or any request for a specific savings number) **with no annual consumption stated anywhere in the conversation** — ask for it *before* calling `best_energy_contract`, the same way TIMING/EV/WORKLOAD ask for a required input before calling `cheapest_hours` when it's needed to answer the specific question asked. Don't call the tool on a default first just to discover afterward that the answer needed to be personalized — that's a wasted call for a question you could already tell needed the real number. If the user says they don't know their consumption and wants a rough estimate anyway, that's fine — call with the default, but state the result explicitly as an assumption using the `assumptions` object's own values, never presented silently as their number.
- **Generic question, no personalization requested** ("is spot generally better than fixed right now?") — call the tool as-is; a `zone_default`-sourced answer is fine to present as a scenario ("for a typical ~2000 kWh/year household...").
- **Consumption already stated in the conversation** — call directly with it; no need to ask again.
- If, after calling, `assumptions.consumption_source` turns out to be `zone_default` on what was actually a personalized request (e.g. the intent wasn't obvious from phrasing alone), don't present the figure as personal — either ask for the real consumption before finalizing the answer, or clearly label the figure as a scenario estimate using the `assumptions` object's own values.
- **Heating**: the same ask-before-call principle applies when heating type would materially change the result — but with a limitation: `heating_source` can only ever say `"user_provided"` or `"default"`, and can't distinguish "the user explicitly said district heating" from "the user said nothing and district was assumed." If the user has actually stated their heating type earlier in the conversation, treat that as known regardless of what `heating_source` says post-call.

## Zone resolution (shared logic — do not improvise a different version here)
Resolve the electricity market in this order, stopping at the first that applies:
1. The explicit electricity location the question is actually about — this may differ from the user's physical location.
2. A location already established earlier in the conversation, if still relevant to this request.
3. Reliable product-provided location context, only if nothing more specific applies.
4. If none of the above resolves it reliably, ask one short question before calling the tool. Do not guess or use the tool's technical default zone as a resolved answer.

Zone persists by semantic continuity (the same target is still being discussed), not by a time limit — re-resolve only when the target changes or becomes ambiguous again.

## Missing-data handling
| Missing | Behavior |
|---|---|
| Zone | Resolve per shared hierarchy; ask if unresolved |
| Consumption (personalized question, not yet stated) | Ask for it before calling the tool; if the user wants a rough estimate anyway, call with the default and label the result as an assumption |
| Heating type (when it would change the result) | Check `assumptions.heating_source`, but also weigh any heating type the user has stated in conversation |
| `action` object absent (Mode 2) | Do not invent a recommendation or savings estimate; relay the tool's own `note`/available tariff fields instead |
| `recommended`/`decision_hint`/`reason`/`action` disagree | Surface the disagreement; don't pick a side |
| `action.provider` disagrees with `recommended.contract.provider` | Don't present the action link as valid; state the destination couldn't be verified |

## Output behavior
- Mode 1: state the recommendation, the reason, the savings estimate with its basis and confidence (via `confidence_basis`), any disclaimer, and the action link — never reduce this to just `decision_hint`. When the action link is presented, use `action.action_link` verbatim (see Link integrity above) — never a derived, shortened, or "cleaned" URL.
- Mode 2: state the regulated structure and the tool's own explanation for why switching/comparison isn't available, using whatever fields are actually present.
- Personalized savings claims: if consumption hasn't been stated, ask for it before calling the tool at all — don't call on a default and discover the gap afterward. If the user wants a rough estimate anyway, clearly label the figure as a scenario estimate, not their personal number.
- If a consistency check under Recommendation integrity fails (fields disagree, or provider/link mismatch), say so plainly rather than presenting a single confident answer.

## Examples

**Mode 1**
- "Should I switch?" with consumption already stated → call directly, full recommendation drawing on `recommended`/`action`/`assumptions`/`disclaimer`, not just `decision_hint`.
- "Is spot generally better than fixed right now?" (no personalization requested) → call the tool as-is; may use the `zone_default`-sourced scenario without asking, since `assumptions` already labels it as such.
- "How much would I save by switching?" with no stated annual usage anywhere in the conversation → ask for consumption *before* calling the tool, rather than calling with a default first and discovering the gap afterward.

**Mode 2**
- "Should I switch electricity providers?" in a regulated market with rich tariff data → explain the regulated structure using `contract_comparison: "not_available"` plus the `note` and available tariff fields; no invented recommendation.
- Same question in a market with only `spot_price` and `note` → explain the regulated structure from `note` alone; don't assume richer fields exist just because another market had them.

**Disclaimer and confidence**
- A response includes a grid-fee disclaimer → included in the answer, not dropped.
- Explaining `action.confidence` → use `action.confidence_basis` text rather than inventing independent certainty language.

**Consistency checks**
- `recommended`, `decision_hint`, `reason`, and `action` all agree → present the recommendation normally.
- Any of those fields visibly disagree → state that a recommendation exists but its fields don't agree with each other; don't present a single confident answer or guess which field is right.
- `action.provider` matches `recommended.contract.provider` → present the action link normally.
- They disagree → don't present the action link as a valid next step; say the destination couldn't be verified.

**Link integrity**
- `action.action_link` is `https://provider.example/switch?plan=abc&aff=elecz123` → presented exactly as-is, full query string intact.
- Assistant is tempted to show `https://provider.example` instead because it looks cleaner → not allowed; the affiliate/tracking parameters must survive.

**Negative (must route elsewhere, not answered by CONTRACT)**
- "What's the electricity price right now?" → PRICE, not CONTRACT.
- "Our bills have gotten so expensive lately." (no contract framing) → SAVE may route here later, but CONTRACT doesn't self-trigger on this alone.
