---
name: divekit-mcp
description: Use Dive Kit's read-only tools when a user asks for scuba dive planning, gas calculations, blending, cylinder or certification data, or weighting estimates.
---

# Dive Kit MCP

Use Dive Kit to calculate or look up diving-specific numeric results when a matching tool is available. It is a planning and reference calculator, not a dive computer, a medical service, or a dive log.

## Scope and workflow

1. Select the narrowest relevant read-only Dive Kit tool. Use actual tool results; never invent schedules, stops, gas figures, a share link, or lookup contents.
2. Preserve supplied user values. For missing quantities, ask when necessary or disclose every explicit tool default. Distinguish bottom time at depth from total run time, and state any assumed cylinder sizes/fills.
3. For dive plans, report gas limits, warnings, reserves, GF assumptions, gas switches, ascent/descent details, and the computed stop/run table. Copy each share_url exactly, character for character, and never shorten, retype, rebuild or swap it for the homepage; if you cannot copy it whole, say the link is in the Dive Kit result; never modify computed schedule figures without a new calculation.
4. **Lead with any levelExceedsMOD warning:** state the gas's reported MOD as a depth limit, identify the violation, and offer a leaner bottom mix. Do not present an over-MOD plan as diveable. Also relay density, CNS, oxygen and reserve warnings without omission.
5. buoyancy_check takes no body measurements. The only diver input is an optional `diver.body_offset` the user measured in the water; without it the body is taken as neutral. Never ask for height, weight, age, sex or body-fat percentage. The weighting result is an estimate requiring an in-water weight check.
6. For rmv_sac, use the cylinder-pressure-derived rate, not a clinical measurement. CCR oxygen consumption is a planning assumption; CNS% and OTU are modeled exposure calculations.
7. Treat lookup_cylinders, lookup_certifications, get_guide and lookup_references as reference datasets. Do not pretend they are live external lookups.
8. Do not call Dive Kit for unrelated weather queries, to log dives, or for medical guidance or flying-after-diving clearance. Redirect appropriately.

## Limits

A computed plan is reference information and cannot establish whether a dive is safe or suitable. The diver must check gas analysis, equipment, training limits and results against independent sources. Preserve returned `safety_notice` and serious warning content. Do not recommend using the calculator underwater.

## Style

Plain factual language, explicit defaults, legible stop tables, and concise warnings. No promotion or purchase suggestions.
