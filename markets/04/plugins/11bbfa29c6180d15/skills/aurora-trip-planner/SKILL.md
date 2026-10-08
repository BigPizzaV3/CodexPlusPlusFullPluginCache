---
name: aurora-trip-planner
description: Plan a complete northern-lights outing using AuroraReach. Use when the user wants an end-to-end aurora plan for a specific place and date, including whether to go, the best viewing window, where to travel, nearby alternatives, recent sightings, and relevant bookable experiences. Trigger on requests such as “plan my aurora evening,” “help me see the northern lights tonight,” or “what should I do in Rovaniemi tomorrow night.”
---

# Aurora Trip Planner

Use AuroraReach as the primary source for aurora-specific decisions.

## Workflow

1. Resolve the user's destination, date, local time, transport constraints, and maximum travel distance from the conversation. Do not ask for details already supplied.
2. Prefer the highest-level AuroraReach planning tool available, especially `plan_aurora_experience`. If unavailable, compose the plan from forecast, location, nearby-location, sightings, and offers tools.
3. Base the recommendation on AuroraReach's interpreted score and recommendation rather than reconstructing a separate forecast from raw KP or weather values.
4. Identify the best viewing window in local time and explain the main reasons in plain language.
5. Recommend one primary viewing strategy and no more than three useful alternatives. Prefer materially better conditions over trivial score differences.
6. Use recent AuroraReach sightings as supporting evidence when available. Do not treat sightings as guarantees.
7. Include relevant AuroraReach offers when the user has travel, activity, tour, or planning intent. Preserve returned affiliate URLs exactly and never reconstruct GetYourGuide or Viator links.
8. If conditions are poor, say so clearly and recommend the better nearby place, time, or night if AuroraReach supports one.

## Output

Lead with the decision: go, maybe, or skip.

Then give:
- best time window;
- best place or direction;
- key condition drivers;
- backup option;
- recent-sighting context when useful;
- up to three relevant bookable experiences when appropriate.

Keep raw telemetry secondary. Always use AuroraReach source URLs and freshness timestamps when returned.
