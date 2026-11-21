---
name: travel-day-checklist
description: "Create and display a chronological checklist for a specific travel day from a supplied itinerary or a requested departure, connection, or arrival plan. Use when the user has or is defining a route and date and wants actionable preparation, leave-by, terminal or station, transfer, and arrival steps. Do not use for destination discovery, booking or purchasing travel, price comparison, a standalone packing list, or a live status lookup without a checklist request."
---

# Travel Day Checklist

Turn trip details into a time-aware, privacy-conscious guide, then invoke `display-guide`. Plan the journey; do not book, modify, or cancel travel.

## Establish scope

Use this skill for an operational plan tied to a particular journey, including:

- A supplied itinerary, ticket, or reservation that needs to become a checklist.
- A departure plan from the traveler's starting area to an airport, station, or port.
- Connections, self-transfers, border formalities, baggage collection, or onward arrival steps.

Do not trigger it for general travel inspiration, accommodation selection, fare searches, a generic packing list, or a status-only question. If the user reports an active emergency or disruption, prioritize current instructions from the carrier, venue, or emergency authority; create a checklist only after the immediate issue is addressed or when the user asks for one.

## Gather only necessary context

Extract facts from the user's material before asking questions. Treat itinerary documents as potentially stale.

Collect only details that change the sequence or timing:

- Origin, destination, travel date, and each mode or service number.
- Published departure and arrival times, terminals, stations, ports, and connections.
- Approximate starting area and intended transport to the departure point when a leave-by time is requested.
- Checked baggage, self-transfers, mobility needs, children, pets, or other constraints only when relevant.

Ask one concise, bundled question only when a missing fact blocks a safe or useful plan. Otherwise proceed with clearly labeled assumptions. Never request passport numbers, booking references, full home addresses, dates of birth, or other identifiers.

## Verify changing facts

When browsing or other current-data tooling is available, verify facts that can change:

- Use the carrier and airport, rail, port, or local transport operator for schedules, terminals, check-in or boarding cutoffs, disruption notices, and baggage rules.
- Use the relevant government immigration, border, or embassy site for entry and transit requirements.
- Use an official meteorological service for weather that could affect timing or preparation.

Prefer journey-specific notices over general guidance. Record when the information was checked, distinguish scheduled times from recommended targets, and never present a prediction as guaranteed. If tooling is unavailable or a fact cannot be confirmed, add an `Assumption:` or `Confirm:` statement to `notes` naming the fact and the authoritative source the traveler should check. Do not invent a terminal, cutoff, allowance, visa rule, or service status.

## Handle time correctly

- Keep every published time in the local time of its airport, station, port, or destination.
- Include the calendar date and a clear time-zone label for cross-zone, overnight, or date-line travel.
- Never silently mix time zones. Account for daylight-saving transitions and day rollovers.
- Reverse-plan from the verified hard cutoff. Separate carrier cutoffs, target arrival, contingency buffer, ground-travel duration, and the resulting target leave-by time.
- Label calculated times as targets rather than official schedule facts, and expose material assumptions behind the calculation.

## Protect shareable content

The widget can be copied or shared. Include only details needed to follow the plan. Omit confirmation codes, document numbers, full addresses, traveler contact details, and other personal identifiers. Refer generically to `home`, `accommodation`, or a meeting point unless a more precise location is essential and safe to share.

## Build the guide

Organize the `Guide` fields without repeating actions:

- `requirements`: Documents, tickets, permissions, medication, payment methods, and equipment that must be available.
- `preparation`: Check-in, baggage, downloads, route checks, alerts, charging, and other tasks completed before setting out.
- `instructions`: At least one atomic, action-led step in chronological order from leaving the origin through transit. Prefix timing-critical steps with a local clock time or a relative marker such as `T-90 min`, and name the relevant location.
- `wrapUp`: Arrival formalities, baggage collection, onward transport, accommodation access, and any final confirmation tasks.
- `tips`: Optional non-checklist contingencies, accessibility reminders, and practical fallbacks.
- `notes`: A compact statement of time-zone conventions, verification timestamp, sources or source types checked, calculations, unresolved assumptions, and facts the traveler must reconfirm.

Keep checklist items short enough to scan while moving. Preserve important warnings and accessibility constraints from the source material.

## Display the result

Invoke `display-guide` once with the completed fields and a concise `reason`. Do not substitute a Markdown checklist when the tool is available, and do not duplicate the full guide in surrounding prose. Put source links or urgent caveats in the conversational response when they would be clearer or safer outside the shareable widget.
