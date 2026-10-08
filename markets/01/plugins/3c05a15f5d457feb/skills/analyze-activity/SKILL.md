---
name: analyze-activity
description: Analyze a completed run, ride, or swim in depth. Use when the user asks to analyze a workout or activity, asks how their run/ride/swim went, or wants a breakdown of pacing, power, heart rate, or execution for a session. Defaults to the most recent activity if none is specified. Do not use for daily readiness questions (use checkin) or for planning future workouts (use replan).
---

Analyze one completed activity in depth and compare it against the user's recent training.

Finding the activity:

1. Determine the sport and which activity to analyze. If the user named a date or activity, use that. If they said "my last activity" or gave no specifics, fetch recent activities with `getRunningActivity`, `getCyclingActivity`, and/or `getSwimmingActivity` (limit to the sports the user actually does if known from context) and pick the most recent one.
2. Fetch the full data for the chosen activity with the matching detail tool: `getRunningActivityDetail`, `getCyclingActivityDetail`, or `getSwimmingActivityDetail`. Start with the default low resolution; request medium or high resolution only if the analysis needs finer time-series detail (for example short intervals).
3. Keep the recent-activity list from step 1 (or fetch it) so the session can be compared to the user's other recent activities of the same sport.

What to analyze (adapt to the sport and to what the data actually contains):

- For runs: how did pace hold up relative to heart rate (if present) through the workout, and how does the session compare to other recent runs? Did it meet its intended purpose versus what was planned? Where relevant, check whether any effort was near a recent best, and how pace held up as the run wore on (fade over distance).
- For rides: look at power and heart rate (if present). Was the user pacing well or fading? Pull the power data to see whether any effort was near a recent best and how power held up after accumulated work. Compare against other recent rides and the session's intended purpose.
- For swims: how did pacing hold up (and heart rate, if present), how does it compare to recent swims, and did the session meet its intended purpose?
- If the user logs HRV, note how internal drift during the session compared to their usual durability trend.
- Note how the session was structured (long blocks versus scattered efforts).
- If weather data is present in the activity, factor in how conditions (temperature, humidity) compared to recent sessions.
- If the activity has device laps, break the effort down lap by lap: how consistent were the splits, and how was execution across any intervals?

Call out whatever stands out most about this particular session rather than working through a fixed checklist. Lead with the one or two most notable findings, then the supporting detail.
