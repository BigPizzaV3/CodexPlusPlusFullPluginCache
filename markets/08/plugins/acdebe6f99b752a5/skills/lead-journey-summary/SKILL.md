---
name: lead-journey-summary
description: Find a specific lead in LeadJourney and summarize their full journey from first touch to conversion, including which channel and campaign brought them in.
---

Use this skill when the user asks about a single lead: "where did this lead come from", "show me the journey of", "summarize lead X", or pastes a LeadJourney lead URL such as `?slug=lead-overview&lead_id=<uuid>`.

## Inputs to establish

1. **Workspace.** Call `get_current_workspace`; switch with `switch_workspace` if the user names another brand.
2. **Which lead.** Accept an email, phone number, name, or lead id.
   - If given an id or URL containing `lead_id`, go straight to `get_lead_journey`.
   - Otherwise call `get_leads` with the search term. If more than one lead matches, list them (name, email, created date) and ask the user to pick before continuing. Do not guess.

## Steps

1. Call `get_lead_journey` for the chosen lead.
2. Read the timeline in order. Identify:
   - First touch: channel, source/medium, campaign, landing page, timestamp.
   - Any later touches and what changed (returning via a different channel, a specific ad creative, a retargeting click).
   - Conversion event: form, call, purchase, or CRM stage, and when.
   - Revenue attributed, if present.

## Output

Present in this order:

1. One-line identity: name, email, company if available, date created.
2. **Journey**: a numbered list, one line per touchpoint, oldest first — `date · channel · campaign/creative · page`.
3. **Attribution**: which channel gets first-touch credit and which gets last-touch credit, in one sentence each.
4. **Status**: converted or not, revenue if any.

Keep the whole summary under 200 words unless the user asks for full detail.

## Do not

- Do not include raw internal ids, tokens, or debug fields from the tool response.
- Do not infer intent, sentiment, or buying stage that the data does not show.
- Do not modify the lead, add tags, or trigger agents unless the user explicitly asks.

Explicit user instructions override these defaults.
