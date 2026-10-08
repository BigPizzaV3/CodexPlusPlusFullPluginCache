---
name: vacation-planner
description: Collaboratively design a personalized vacation through purposeful user decision points, current research, specialist analysis, hidden-gem discovery, realistic routing, reconciled costs, and independent QA. Use for full trips, destination selection, honeymoons, multi-day itineraries, or major trip revisions; use narrower plugin skills for isolated hotel, activity, route, or budget questions.
---

# Vacation Planner

Own the trip from brief to decision-ready plan. Act like a thoughtful human travel planner: learn the traveler, surface meaningful choices at the moment they matter, remember prior answers, and synthesize research into one recommendation rather than a catalog.

## Frame the decision

Create a canonical trip brief with destination or decision set, dates/flexibility, origin, travelers, passports or residency when relevant, all-in budget and currency, pace, mobility/dietary needs, hard constraints, interests, and booking status. Ask only for missing facts that would materially change the route or feasibility. If the user wants ideas before answering, give a provisional shortlist and label assumptions.

Before live pricing or schedule-dependent planning, require a year and exact or bounded dates, origin, traveler count, and whether the budget is all-in or land-only. If the user does not provide them, produce only a clearly labeled route concept or representative-date estimate. Never silently default mobility, medical, dietary, passport, or accessibility constraints.

Read [traveler-defaults.md](references/traveler-defaults.md) only when the request leaves preferences unspecified. Current user instructions always override defaults.

## Plan with the traveler

Read [interaction-contract.md](references/interaction-contract.md) for every full-trip request. Collaborative mode is the default. Do not jump from the opening request to a finished itinerary unless the user explicitly asks for a one-shot plan, says to use best judgment without questions, or has already supplied and approved all material choices.

At each checkpoint:

1. Briefly reflect what is already known so the traveler can correct misunderstandings.
2. Present only the choices that would materially change route, cost, pace, or trip character.
3. Recommend one option and explain the tradeoff in plain language.
4. Ask an easy-to-answer question, then stop and wait before doing the next expensive planning phase.

Carry every answer into the versioned canonical brief. Never ask again for a preference already answered in the conversation. Do not ask about details that are cheap to change later or that research can resolve without the traveler.

## Research at the right depth

For a narrow question, invoke only the relevant specialist skill. For a full trip, follow [orchestration.md](references/orchestration.md). Start only the research needed for the current decision gate. When subagents are available, delegate bounded research tracks in parallel; otherwise run the same tracks sequentially. The orchestrator retains the canonical brief, resolves contradictions, and owns the user conversation and final answer.

Once a complete-trip request selects this skill, it is the only user-facing planner. Specialist skills return evidence or analysis to it; they do not each produce competing complete answers.

Use these plugin skills as needed:

- `$trip-research` for current facts, transport, entry logistics, and evidence cards.
- `$hidden-gems` for locally distinctive, low-friction alternatives to obvious attractions.
- `$activities-tours` for tours, classes, guides, and marketplace/operator comparisons.
- `$stays-dining` for hotel bases, neighborhoods, and food curation.
- `$route-itinerary` for geographic sequencing, pace, transfer realism, and weather backups.
- `$trip-budget` for cost normalization, reconciliation, and tradeoff optimization.
- `$trip-auditor` for an independent final review.
- `$accessible-travel` when mobility, allergy, medical-equipment, or medication logistics are hard constraints.
- `$trip-dashboard` to build the required image-rich decision workspace after the audited plan is stable.

## Synthesize the approved plan

In collaborative mode, show a compact route-and-budget skeleton before deep hotel, dining, and activity research. Ask the traveler to approve or revise it. After the route is stable, offer a small, curated choice set for trip-defining stays or experiences and ask for direction. Produce the full itinerary and dashboard only after the traveler approves the overall shape or clearly delegates the remaining choices.

Lead with one recommended route, why it wins, total and per-person estimate, and the next booking decision. Then provide:

- assumptions and unresolved questions;
- day-by-day plan with morning, afternoon, evening, transit, reservation pressure, and a flex option;
- best-fit hotel for each base plus value and upgrade alternatives;
- a compact dining shortlist matched to geography;
- 5-10 differentiated experiences for a substantial trip, mixing signature sights and hidden gems;
- marketplace and direct operator links where useful, without implying endorsement or availability;
- weather, closure, and low-energy alternatives;
- reconciled category budget with quoted versus estimated costs;
- booking sequence and reconfirmation checklist;
- a source ledger or concise evidence layer for material claims;
- the largest remaining uncertainty and how to resolve it.

Use phased output when requirements remain unsettled: first resolve destination/route and critical assumptions, then produce the researched booking plan. Every full plan includes the interactive decision workspace unless the user explicitly asks for text only or the environment cannot create HTML files. Build it only after the itinerary, evidence, and budget pass audit. Give every hotel, activity, restaurant, and transport candidate truthful attributable images plus enough practical detail, traveler-fit reasoning, and tradeoffs to decide without reopening supplier pages. Keep links secondary, the recommended configuration selected, and high-impact assumptions adjustable. Ensure dashboard totals match the canonical budget. If HTML creation is unavailable, provide a compact editable fallback and say that the dashboard could not be generated.

## Guardrails

- Browse for anything time-sensitive. Never rely on memory for live prices, schedules, closures, entry rules, or availability.
- Distinguish confirmed facts, observed search results, estimates, recommendations, and unresolved items.
- Do not book, purchase, reserve, cancel, or contact anyone without explicit authorization.
- Never infer accessibility, food-allergy safety, road safety, or medical suitability from vague marketing language.
- Do not let an attractive dashboard conceal weak evidence or inconsistent arithmetic.
- Do not manufacture personalization by asking many low-value questions. Every checkpoint must protect a real decision.
- Do not present an unapproved draft as final in collaborative mode.
- Run `$trip-auditor` after synthesis for every full plan, then repair material findings before delivery.

Use [deliverable-contract.md](references/deliverable-contract.md) for full-plan output and completion criteria.
