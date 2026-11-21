---
name: natuurijs
description: Help users quickly find currently skateable natural ice in the Netherlands and submit a concise nature-ice report, using Natuurijs.nl as the primary source.
---

# Natuurijs.nl workflow

Use this skill whenever the user asks where they can skate on natural ice now, wants nearby natural-ice spots, asks for current ice reports, or wants to report natural ice.

## Core principle

Natuurijs is highly time-sensitive. Always seek current information from Natuurijs.nl before making claims about where skating is possible. If the source cannot be checked, say so explicitly and do not present old reports as current.

## Find where to skate

1. Determine the user's location from the conversation when available. If the user asks "near me", use the host's location context if available; otherwise ask for a town/postcode.
2. Search Natuurijs.nl for current reports and locations. Prefer reports from today or the most recent available date.
3. Distinguish between confirmed/positive skating reports, unsafe/not-yet-skateable reports, and old or unverified reports.
4. Give a short list of nearby locations, ordered by distance when distance can be established. Do not invent distances.
5. For each location, provide the report date/time when available and the practical status.
6. If conditions are uncertain, tell the user to verify locally before entering the ice.

## Report natural ice

When the user wants to submit a report, collect only what is needed: location or water/route name, municipality/area if useful, status, approximate ice quality or thickness if known, observation date/time, and optional notes such as weak spots or access.

Before submitting, summarize the report and ask for confirmation if an external submission action is available. Never fabricate an observation, ice thickness, or safety status.

If no direct submission tool is available, produce a ready-to-copy report formatted for Natuurijs.nl and provide the official Natuurijs.nl route when known.

## Safety

Natural ice can change rapidly. Never infer safety solely from temperature, nearby reports, or the presence of other skaters. Make uncertainty explicit and recommend checking local warnings and ice conditions.

## Response style

Keep answers fast and practical. Start with the answer, then give the evidence/date. For nearby searches, use a compact table with location, status, report date/time, and distance if known. Avoid claiming that a place is safe unless the source explicitly supports that conclusion.
