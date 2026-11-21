---
name: get-started
description: How to answer questions about a website's user behavior with FullSession (session replays, funnels, heatmaps, frustration signals, Lift AI recommendations and dashboards). Use whenever the user asks about their site's visitors, conversions, drop-offs, rage or dead clicks, errors, or wants to find or watch specific sessions.
---

# Using FullSession

FullSession records how visitors use a website: every session (with a replay), clicks and frustration signals, funnels, heatmaps, feedback, and Lift AI recommendations. The tools read the connected account's own data.

## Always start by knowing the site

- If the user hasn't named a site, call `list_sites`. If there is exactly one site, use it without asking. If there are several, ask which one, or match the name or URL they mentioned.
- Pass `siteId` explicitly to every tool after that.

## Time ranges

- Default to the last 7 days unless the user says otherwise. Say which range you used.
- Pass dates the way the user means them ("this week", "since January"), as ISO dates. Most tools accept ranges up to 365 days.
- When an answer is empty, say so plainly and suggest a wider range before concluding there is no data.

## Pick the right tool

| The user wants… | Use |
|---|---|
| A quick health check of a site | `get_site_overview` |
| Pages where users struggle | `compare_pages_by_frustration`, then `get_page_heatmap` (clicks) on a page |
| What's wrong with one element | `get_element_interactions` |
| Where a funnel loses people | `list_funnels`, then `get_funnel_analysis` |
| Who dropped off, to watch them | `get_funnel_sessions` |
| Sessions matching criteria | `search_sessions` |
| What happened in one session | `get_session` |
| One visitor's history | `get_user_sessions` (by userId or email) |
| A number, trend or breakdown | `get_metric`, `get_trend`, `get_breakdown`, `get_page_ranking` |
| What to fix to convert more | `list_ai_goals`, then `get_ai_recommendations` (Lift AI) |
| Saved dashboards and charts | `list_dashboards`, `get_dashboard_data`, `list_cards` |

For deeper workflows, see the `investigate-friction` and `analyze-funnel` skills.

## Presenting results

- Some tools show the user an interactive card (funnel chart, page ranking, session list, trend chart). When a card is shown, don't repeat its data as a table. Give the key insight in a few sentences and suggest the next step.
- Link to evidence. Session results include replay links; offer the most relevant 2–3 rather than listing everything.
- Be precise about units: funnels count sessions unless they're set to count unique users, and the tools say which.

## Visitor privacy

- Session lists show visitors' emails and names masked (e.g. `j***@acme.com`). This is intentional.
- When the user asks about a specific visitor or session, `get_session` and `get_user_sessions` return the full identity. Use them only when the question is about that person.
- Don't try to reconstruct masked identities from other fields.

## Things to know

- A funnel that was just created or had its steps changed is "processing" for a few minutes; its numbers are unavailable until it finishes.
- `generate_segment_from_prompt` and `generate_funnel_steps_from_prompt` only draft definitions with an AI model; they save nothing.
- These tools only read data. Segments, funnels, heatmaps, dashboards and charts are created and edited in the FullSession app; the `generate_*` tools can draft a definition for the user to paste there.
