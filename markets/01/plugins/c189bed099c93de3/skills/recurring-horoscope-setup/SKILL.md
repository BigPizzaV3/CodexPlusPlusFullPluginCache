---
name: recurring-horoscope-setup
description: Prepare a daily, weekly, monthly, or yearly recurring horoscope routine. Use when the user asks to schedule, deliver, receive, or be reminded about a horoscope on a cadence. Show the matching horoscope first, then guide the user through the widget's task action without claiming the skill can click it or verify task creation.
---

# Recurring Horoscope Setup

Prepare the correct horoscope view and guide the user through the widget-owned recurring task flow.

## Inputs

Resolve:

- one of the 12 supported star signs
- one cadence: daily, weekly, monthly, or yearly
- an optional complete `YYYY-MM-DD` date of birth

Ask for or confirm the star sign when it is missing. Never call `horoscope` with only `dateOfBirth`, because the server does not infer the sign from it.

## Workflow

1. Ask only for a missing star sign or cadence.
2. Map the cadence to the matching route:
   - daily: `horoscope/daily`
   - weekly: `horoscope/weekly`
   - monthly: `horoscope/monthly`
   - yearly: `horoscope/yearly`
3. Call `horoscope` with `starSign`, the exact route, and a concise `reason` explaining that the view is being prepared for recurring delivery. Include `dateOfBirth` only when the user supplied a complete valid date.
4. Tell the user to select the widget action labeled `Get this daily`, `Get this weekly`, `Get this monthly`, or `Get this yearly`, matching the chosen cadence.
5. Explain that the widget will send a follow-up request to create the recurring task. Treat the setup as pending until the host flow confirms it; the horoscope tool call alone does not create a task.
6. If the action is absent or does not complete, explain that recurring setup depends on app configuration and host task support. Do not retry the horoscope tool as though that could create the task.

## Output

State the selected sign, cadence, route, and setup status. Use `Awaiting widget confirmation` until the user or host confirms completion.

## Boundaries

- The `horoscope` tool is read-only and cannot create, inspect, change, or cancel scheduled tasks.
- Do not claim to click the widget action, invoke its private `sendFollowUpMessage` flow, or verify a task that the user has not confirmed.
- Do not promise exact delivery times; the widget creates a cadence-based follow-up prompt and exposes no time-of-day input.
- Treat the horoscope as entertainment and reflection, not a guaranteed prediction.
