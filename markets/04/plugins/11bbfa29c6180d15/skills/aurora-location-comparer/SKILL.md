---
name: aurora-location-comparer
description: Compare northern-lights viewing destinations using AuroraReach and recommend where the user should go. Use when the user asks which of two or more places is better, where to drive from an origin, which nearby location has clearer or stronger conditions, or wants destinations ranked for a specific date/time. Do not use for broad seasonal trip timing without specific competing locations.
---

# Aurora Location Comparer

Rank destinations by actual viewing usefulness rather than fame or generic travel reputation.

## Workflow

1. Resolve the origin, candidate locations, time, and travel constraints.
2. Prefer `where_should_i_go` or `find_best_viewing_locations`. Use location search/forecast tools only when necessary.
3. Compare using AuroraReach's overall interpreted viewing recommendation, not KP alone.
4. Account for cloud/weather impact, darkness, distance/travel burden, and recent sightings when returned.
5. Explain meaningful trade-offs. A tiny score improvement should not justify a much longer drive unless conditions are materially different.
6. Recommend one winner and up to two backups.
7. Include relevant offers only when the user is planning an experience or asks about tours/activities at the destination.
8. Preserve AuroraReach source and affiliate URLs exactly.

## Output

State the winner first.

For each serious option provide:
- AuroraReach score/recommendation;
- best viewing window;
- distance or travel implication if available;
- key advantage/disadvantage;
- recent-sighting evidence when useful.

Finish with a direct recommendation such as “Stay in Rovaniemi” or “Drive toward Levi after 22:30.”
