---
name: ololand-dd-deal-network
description: Use when the user asks to run the OloLand ololand-dd-deal-network workflow.
  Find Deal Network providers, draft a seller listing, and request an introduction
  on a match. Uses OloLand's Deal Network tools; the introduction is held for an OloLand
  admin's release unless the counterparty has consented to direct contact, in which
  case it is delivered immediately. This command never pastes contact details.
---


# Workflow for ololand-dd-deal-network

Follow the OloLand command instructions below when the user asks for `ololand-dd-deal-network` or the equivalent workflow.

# Deal Network

Use this command when the user asks for a fractional CFO, adviser, lender or reviewer for a deal, wants to list a business they are selling, or wants an introduction on an existing Deal Network match.

## Usage

```
ololand-dd-deal-network providers [participant_type] [region]
ololand-dd-deal-network list <deal_id>
ololand-dd-deal-network intro <match_id> [message]
```

## Arguments

- `providers [participant_type] [region]` — list visible providers (fractional_cfo, adviser, lender, reviewer), conflicts already filtered.
- `list <deal_id>` — create a DRAFT listing for a seller-side deal from bands the user confirms (sector, revenue band, EBITDA band, asking band, geography, structure, headline). Never exact figures.
- `intro <match_id> [message]` — request an introduction on a match the user is a party to. The introduction is held for an OloLand admin's release unless the counterparty has consented to direct contact, in which case it is delivered to them immediately.

## Execution

1. **providers** — call `list_network_participants(participant_type, specialties, region)`. Render name, type, firm, specialties, coverage. Do not invent availability or rates.
2. **list** — confirm each teaser band with the user, then call `create_network_listing(deal_id, teaser)`. Tell the user the listing is a draft and must be activated in-app with a source authorization.
3. **intro** — confirm the message (at most 2000 characters), then call `request_network_intro(match_id, message)`. Tell the user the introduction is held for an OloLand admin's release unless the counterparty has consented to direct contact, in which case it is delivered to them immediately.
4. For an engagement after an introduction is accepted, point the user to `ololand-dd-advisory <deal_id> list` — engagements are started in-app by the buyer on the accepted introduction, not by this command.
5. If a call returns `error_code` `FEATURE_LOCKED`, say the Deal Network needs the Pro tier or above (use the tier named in the error's `message` if the backend supplies one) and stop.

## Guardrails

- Never quote or invent a price for an introduction, an engagement, or a deal. The only pricing this command handles is the asking BAND the user confirms for their own draft listing; never an exact figure.
- Never imply a lender fee or a financing commitment; lender introductions are courtesy intros.
- Never describe the Deal Network as generally available; it is an early capability.
- Do not paste contact details from an intro into other tools; they are shown in-app only, after both parties consent.

## Output URL Conventions

Use tool-returned `view_url` values when present. Canonical surfaces:
- Network home: https://app.ololand.ai/network
- Deal network tab: https://app.ololand.ai/deals/{deal_id}/network


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
