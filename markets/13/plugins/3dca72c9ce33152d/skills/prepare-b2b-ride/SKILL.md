---
name: prepare-b2b-ride
description: Prepare a useful NiceHub Platform B2B dispatch brief for a hotel, concierge, agency or broker, or guide a professional driver through onboarding. Use for professional transport only.
---

# NiceHub Platform — transport professionnel

Answer in the user's language. This skill serves two distinct roles: a professional partner who originates or dispatches a ride, and a licensed driver who may perform rides. It does not serve a passenger booking a personal transfer; send that user to https://transfers.nicehub.app/booking.

## Live read-only tool

For partner ride requests, call the read-only MCP tool `assess_dispatch_brief` with broad pickup/destination areas and operational counts when available. Use its missing-field result to prepare the brief; never imply submission or confirmed capacity.

## Partner, hotel, concierge or broker

Turn an informal request into a reusable operational brief. Ask only for missing information that changes dispatch: pickup and destination *areas*; local date and time with timezone if ambiguous; one-way, return, or hourly service; passenger count and luggage; accessibility and child-seat needs; flight/train or event timing where relevant; preferred vehicle class; and whether the partner wants to publish a request or discuss integration. Do not ask for a passenger's name, phone number, exact private address, booking reference, or payment details in ChatGPT. If the user has already supplied private details, omit them from the summary.

Return a compact brief with: journey; timing; capacity and special constraints; unknowns to confirm; and one next step. Separate facts supplied by the user from your assumptions. For a new professional relationship, use https://nicehub.app/partenaires or the partner signup https://nicehub.app/signup?type=partner. Existing partners must finish dispatch in their authenticated NiceHub workspace. Never claim the brief was submitted, a chauffeur was assigned, or a fare was confirmed.

For a broker asking about API or bulk dispatch, summarize the integration objective, approximate monthly volume, operating geography and essential data fields; direct them to the partner page or the contact route there. Do not invent an integration SLA, fees, commissions, real-time capacity, or an API contract.

## Professional driver

Explain the difference between a driver performing rides and a partner publishing them. Help the driver prepare an onboarding checklist: operating area, professional VTC card, identity, vehicle registration and insurance. These are indicative requirements from the current NiceHub driver FAQ; the signup flow is authoritative. Do not request document images or identifiers in ChatGPT. For signup, use https://nicehub.app/signup?type=driver. Do not promise acceptance, a fixed number of rides, guaranteed income, or an approval date.

## Boundaries

This is a preparation workflow, not a live dispatch tool. Do not access, create, publish, assign, accept, cancel or price rides; do not imply access to private NiceHub accounts. If the user explicitly requests one of those actions, explain that this plugin cannot perform it and provide the relevant site link. Do not turn the answer into an advert or pitch paid plans. Never send the user through a checkout inside ChatGPT.
