# Multi-agent orchestration

Use this workflow for a substantial multi-day trip. Keep the main agent as the single editor and decision owner.

## Canonical brief

Create one versioned brief and decision ledger using [interaction-contract.md](interaction-contract.md). Give every specialist the same dates, traveler count, origin, currency, budget scope, pace, confirmed choices, rejected options, constraints, interests, delegated decisions, and unresolved questions. Require specialists to state any departure from it.

Do not launch every research track immediately. In collaborative mode, research only enough to support the current decision gate, return to the traveler, update the brief, and then begin the next phase. This prevents extensive work around a route or trip style the traveler never chose.

## Parallel research tracks

When delegation is available, run up to three bounded tracks in parallel:

1. **Route and logistics:** destination fit, flights or arrival options, intercity transport, entry logistics, geography, and likely transfer friction.
2. **Experiences and hidden gems:** signature anchors, locally distinctive alternatives, tours, operators, seasonality, crowd risk, and weather substitutes.
3. **Stays, neighborhoods, and food:** base selection, hotel comparisons, neighborhood feel, dining fit, and price evidence.

Tell each agent to research only, preserve source URLs, make no bookings, and return compact evidence cards. Do not ask multiple agents to produce complete itineraries.

When accessibility, severe dietary risk, mobility equipment, or medication logistics are hard constraints, add an `$accessible-travel` feasibility overlay. Run it in parallel when capacity allows or sequentially before synthesis; do not drop needed route, activity, stay, or dining coverage. This overlay is a gate, not a soft preference score.

## Evidence card

Each material candidate should include:

- name and type;
- why it fits this brief;
- location and time cost;
- source URL and source type;
- observation date and applicable trip dates;
- price basis and currency, if relevant;
- confidence: high, medium, or lead-only;
- caveat or verification need.

## Reconciliation

The orchestrator must deduplicate the same attraction or operator across marketplaces, normalize currencies and party-size assumptions, resolve conflicting facts in favor of fresher primary sources, and explicitly retain unresolved conflicts. Build the route only after arrival/departure and base logistics are feasible.

When research exposes a consequential fork, the orchestrator creates a compact decision board: recommended choice, one or two real alternatives, the tradeoff, and the decision needed from the traveler. Specialist agents never ask the traveler directly and never treat a provisional preference as approval.

Wait for every selected track or record that it failed. Validate that each response uses the current brief version and contains the required evidence-card fields. If a track is incomplete, issue at most one bounded corrective follow-up; then either run that track sequentially or disclose the missing coverage and downgrade the plan. Never label a plan decision-ready while a feasibility-critical track is missing.

After the traveler approves the route-and-budget skeleton and delegates or chooses material booking decisions, give the finished draft, canonical brief, decision ledger, evidence cards, and canonical budget input to a fresh audit agent using `$trip-auditor`. The auditor flags issues but does not silently change priorities. The orchestrator repairs high-severity findings and records any accepted uncertainty. After material repairs, rerun budget reconciliation and a focused audit of the affected constraints. Do not deliver as decision-ready while critical findings remain.

If delegation is unavailable, perform these tracks sequentially. Do not pretend independent review occurred; apply the same audit rubric directly.
