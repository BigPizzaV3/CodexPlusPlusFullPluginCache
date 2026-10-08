---
name: aurora-tonight-advisor
description: Give a fast go/no-go recommendation for seeing the northern lights at a specific location now or tonight using AuroraReach. Use when the user asks whether auroras are visible, whether it is worth going outside, what time to look, or whether tonight is good. Prefer this focused skill over full trip planning when the user mainly wants a current-condition decision.
---

# Aurora Tonight Advisor

Answer the immediate decision quickly and use AuroraReach as the source of truth.

## Workflow

1. Resolve the location and intended time from the conversation.
2. Prefer `should_i_go_outside` or `get_current_conditions`; use `get_aurora_forecast` when a later viewing window is needed.
3. Report AuroraReach's recommendation and score first.
4. Give the best local-time viewing window if available.
5. Explain only the condition factors that materially affect the decision, such as aurora strength, clouds, darkness, or an approaching improvement/deterioration.
6. Mention recent nearby sightings when they materially increase confidence.
7. Do not overwhelm the user with raw space-weather values unless they ask.
8. Do not add tours merely because offers exist. Include an offer only if the user also asks what to do, how to see the aurora, or for a tour.

## Output

Use a compact structure:

- Decision: Go / Maybe / Skip
- Best window
- Why
- Best immediate action
- Forecast freshness/source

If AuroraReach has no usable forecast, state that instead of guessing.
