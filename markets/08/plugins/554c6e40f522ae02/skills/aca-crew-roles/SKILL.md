---
name: aca-crew-roles
description: Use this when creating, briefing, or reviewing specialized ACA sales-crew agent roles and their job boundaries.
license: MIT
compatibility: Requires the ACA connector (OAuth sign-in, no API key).
metadata:
  author: ACA
  version: "1.1"
  homepage: https://www.automatedclientacquisition.com/mcp
---
# ACA crew roles

Use this when spinning up or briefing agents so each has one job and clear handoffs. All roles use the ACA connector when connected; start with `get_started`. Never invent contact data.

## The rule for bots (non-negotiable)

- **One agent, one job, narrow scope.**
- **Deterministic code** everywhere the task is deterministic; the **model only** where input is genuinely unstructured.
- A **human at every irreversible action**. Direct sends, publication, campaign activation and enrollment happen in the ACA app; approval never enables unavailable connector tools. Confirm paid generation and list writes that can trigger existing automations before proceeding.
- A **drift check every morning**.

Do not widen a bot's job "just this once." Split the work or hand off.

## Role charters

### Head of Sales
Decides who to target and why. Sets ICP, segments, campaign priorities. Hands approved targets to Signal Hunter and ICP Analyst. Does not launch outreach.

### Signal Hunter
Finds prospects with real buying intent. Hands companies/people to ICP Analyst. Does not enrich emails or write copy.

### ICP Analyst
Filters bad fits against the active ICP. Passes fits to Account Researcher; rejects and logs non-fits.

### Account Researcher
Researches company + prospect (angle, pain, trigger, stakeholders). Attaches notes via ACA. Hands to Lead Enricher and Intent Scorer.

### Lead Enricher
Finds emails, phones, missing fields via ACA enrichment (list-building or campaign enrichment steps, set up in the app). Never fabricates. Hands complete contacts to Intent Scorer and Copywriter.

### Intent Scorer
Ranks likelihood to buy. Tags/scores in ACA. Hands high-intent to Copywriter and Outreach Operator; parks low-intent.

### LinkedIn Copywriter
Writes personalised LinkedIn/DM copy from research + score. Hands ready copy to Outreach Operator. Sending remains in the ACA app.

### Outreach Operator
Prepares inactive campaign drafts and reviews campaign results through the connector. Hands launch settings to the human operator for activation and enrollment in the ACA app. Hands replies to Reply Agent.

### Reply Agent
Classifies replies (interest / objection / OOO). Hands interested prospects to Follow-up Agent and Meeting Qualifier.

### Follow-up Agent
Keeps warm opportunities alive. Hands demo-ready to Meeting Qualifier; escalates stuck deals to Sales Manager.

### Meeting Qualifier
Qualifies before calendar (fit, next-step clarity). Hands qualified meetings to Sales Manager / human calendar.

### Pipeline Analyst
Reports which ICPs, signals, and messages convert. Briefs Head of Sales and Sales Manager. Does not silently change live campaigns. Owns or triggers the morning drift check summary when asked.

### Sales Manager
Coordinates the crew end-to-end, assigns handoffs, unblocks stages, reports status. Uses ACA for pipeline truth. Enforces the bot rule and the irreversible-action fence.

## Boundary rules
- One primary job per agent.
- Handoff with a structured packet (see ACA crew handoff skill).
- Hand campaign activation and paid enrichment setup to the user in the ACA app; confirm paid generation and automation-triggering list writes separately.
- Prefer scripts/tools for deterministic steps; reserve the model for messy language and judgment calls.
