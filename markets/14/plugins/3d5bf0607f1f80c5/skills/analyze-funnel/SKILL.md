---
name: analyze-funnel
description: How to analyze a conversion funnel in FullSession, find the biggest drop-off, see who dropped and why, compare audiences, and get Lift AI recommendations. Use when the user asks about conversion, drop-off, checkout or signup completion, or a specific funnel.
---

# Analyzing a funnel

## 1. Find the funnel

`list_funnels` returns the site's funnels with their step names. Match the user's wording ("checkout", "signup") to a funnel name; if several fit, ask. If no funnel exists for what they describe, say so: the user can create it in the FullSession app, and `generate_funnel_steps_from_prompt` can draft its steps.

## 2. Read the funnel

`get_funnel_analysis` returns, per step, how many sessions (or users) reached it, the drop-off from the previous step, and the median time between steps, plus the overall conversion rate.

- Lead with the **biggest drop** (the step pair losing the most people) and the overall conversion rate.
- Say the unit: funnels count sessions unless they count unique users.
- If the funnel says it is **processing**, it was just created or changed; ask the user to try again in a few minutes.

## 3. See who dropped and why

`get_funnel_sessions` with `outcome: "dropped"` and the step **before** the drop returns the sessions that reached that step but never the next, with replay links. Offer 2–3 replays.

To learn why, look for patterns: run `get_session` on a few dropped sessions, or check the drop step's page with `compare_pages_by_frustration` / `get_page_heatmap` (see `investigate-friction`).

## 4. Compare audiences

- By device, country, browser or OS: `get_funnel_analysis` with `breakdown`. A drop that exists only on mobile is a much clearer lead.
- By saved segment: `get_funnel_analysis` with `segments` (from `get_segments`), for example new vs returning visitors.

Breakdown and segment comparison can't be combined in one call.

## 5. Recommendations

If the site uses Lift AI, `list_ai_goals` finds goals built on funnels, and `get_ai_recommendations` returns ranked issues with the predicted lift from fixing each. `get_recommendation_sessions` gives the sessions behind a recommendation. Present the top 2–3 with their predicted impact.

## Notes

- Compare like with like: when comparing periods, use the same length of time (`get_trend` with `comparePreviousPeriod` works for overall traffic).
- Small numbers are noisy. If a step has only a handful of sessions, say the result isn't reliable yet.
