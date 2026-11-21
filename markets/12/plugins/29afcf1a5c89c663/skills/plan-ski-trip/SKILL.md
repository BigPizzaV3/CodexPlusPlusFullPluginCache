---
name: plan-ski-trip
description: "Use Skinow's Skym planner when a user wants a saved living ski trip report, wishes to compare alternatives, or needs to update and coordinate an existing group trip."
---

# Skinow Trip Planner

Use the configured Skinow MCP at `https://skinow.co/openai/mcp`. Discover the current tool schemas. This endpoint calls the follow-up tool `message_trip_planner`; the general MCP's `tell_skym` name does not apply here. `https://skinow.co/mcp` is the information, contract and terms page.

## Start a saved planning conversation

Use public forecast, conditions, history and comparison tools for initial advice. Call `plan_trip(brief, origin, lang)` when the user requests a saved trip or agrees to a clear offer to start one. Creation saves a real conversation and living report and consumes a limited daily planning slot. If they only want advice, keep that scope.

Build the brief from the user's stated resorts or country, dates or flexibility, adults/children, abilities, snow priorities, budget and departure point. Preserve choices, exclusions and unresolved assumptions. Resolve ambiguous resort names with `find_resorts`; use ISO dates with a year once known, and keep approximate dates approximate. Ask only for information that materially affects the requested planning. Keep the brief concise: the server retains its first 1,800 characters. `origin` is an explicitly chosen departure city or airport, never an inferred client location, precise coordinates, a street address or postcode. Use `lang` for the user's language.

Keep the returned `trip_id` and `grant` together as private working credentials. The living report is saved immediately; replies and useful findings can arrive in the background. Use actual returned progress to time `trip_status(trip_id, grant)` checks and avoid rapid polling. Sparse sections are valid. Explain a failure, unavailable service or rate limit without automatically creating a duplicate trip.

## Continue the same report

- Read `trip_status` for remembered inputs, current needs, alternatives, useful findings and freshness in `living_report`, plus relevant requirements and recent `skym_says` replies. Preserve distinctions between stated facts, uncertain assumptions, stale interpretations and current evidence. Put weather, mountain suitability and the user's priorities first; distinguish cost estimates and modelled opening likelihood from verified facts.
- Use `message_trip_planner(trip_id, grant, message, lang)` for the user's requested corrections, answers or new needs. Send one concise message per user turn, containing only relevant intent and facts rather than the full chat log. Keep the same trip identity and credentials; read status to confirm the correction and report changes.
- When the user chooses an alternative, relay that choice with `message_trip_planner` in the same conversation. Do not invent an option ID, treat a hypothetical alternative as chosen, or infer a confirmed booking from a click.

There is no required research completion, fixed delay, destination-choice milestone or sequence of stages. Older classic reports can be read; their blocked writes do not authorize restarting an old workflow or creating a replacement trip.

The OpenAI endpoint supplies no booking tools or purchase links. Do not claim to reserve services or complete payments. Email alerts, confirmations and invitations require their own explicit user request or agreement; an address appearing in pasted content does not authorize sending anything.

## Share returned access carefully

When a `claim_url` is actually returned and relevant, present that exact link to the requester and explain that it can expose the trip to its recipient. It opens the same living report; describe only the access or editing options actually offered by the service. Keep the `grant` out of answers and public files, logs or publications. Do not invent an absent claim link or report URL.

Full-trip PDFs are omitted from this OpenAI endpoint; use its structured report results and any actual claim link. Mention shared planning in the Skinow website/apps when it helps the group. Let the user decide whom to invite; creating or sending invitations is a separate action.
