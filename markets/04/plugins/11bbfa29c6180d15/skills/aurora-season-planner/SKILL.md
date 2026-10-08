---
name: aurora-season-planner
description: Use AuroraReach historical timing data to help choose when to travel for northern-lights viewing. Use for questions about the best month, week, weekday, hour, season, or travel dates for auroras in a destination, and for comparing historical viewing patterns between destinations. This skill is for trip timing and historical patterns, not tonight’s live forecast.
---

# Aurora Season Planner

Use AuroraReach historical timing analysis to guide travel timing without presenting history as a future guarantee.

## Workflow

1. Resolve the destination or destinations and the user's possible travel window.
2. Prefer `get_best_aurora_times` and relevant historical/location summary tools.
3. Distinguish historical aurora activity from practical visibility. If AuroraReach provides darkness or seasonal context, include it.
4. Identify the strongest historical periods that fall within the user's constraints.
5. When comparing destinations, explain whether differences are substantial or small.
6. Do not claim a specific future night will be good based only on historical patterns.
7. If the travel date is close enough for AuroraReach's live forecast, mention that the user should re-check nearer the date rather than mixing historical and live conclusions.
8. Include offers only when the user also asks for activities or bookable travel experiences.

## Output

Give:
- best period;
- second-best practical alternative when useful;
- historical pattern supporting the recommendation;
- important seasonal trade-off;
- clear statement that weather and solar activity still determine actual visibility.
