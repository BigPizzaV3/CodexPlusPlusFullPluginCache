Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Funding routes, opportunities, and qualification

Execute only the current stage's slice of the funding-pathway method. Use the
approved objective, organization frame, use of funds, strategic angle, current
and lapsed supporters, accepted peer/project signals, durable relationship
knowledge, and stage-relevant evidence receipts.

## Case and funding architecture

At `case_funding_architecture`, map each cost or workstream to the source types
that can plausibly fund it: unrestricted/general support, program grants,
public funding, corporate or bank support, individual or DAF giving, earned
revenue, project capital, or in-kind support. State the role, timing,
restrictions, evidence basis, readiness, and dependency of each route. Propose
organization/operator, program/pilot, or sequenced routes; do not turn source
types into named prospects.

## Opportunity universe

At `opportunity_universe`, build a broad but bounded, reviewable candidate
universe. Begin with current and former supporters, then use peer-funder,
project-payer, co-funding, graph, warehouse, owned-source, network, donor,
sponsor, official opportunity, and capital signals in the prescribed order.
Keep grantmakers, individual/DAF leads, open opportunities, public finance,
capital providers, intermediaries, partners, and networks in separate lanes.

For every candidate preserve resolved identity, lane, organization-versus-
program scope, current/lapsed/covered/new status, discovery source and date,
direct-evidence-versus-lead status, route rationale, and unresolved checks.
Include known current supporters in review. A peer funding signal is a lead,
not verified fit; a network, regrantor, lender, or DAF sponsor is not silently
recast as a grantmaker.

## Qualification

At `qualification`, use current official materials to verify eligibility,
program and geography fit, amount or range basis, application cycle and dated
deadline, competition or invitation constraints, contact or next route,
currentness, and access state. For people leads, verify identity, relevant role,
credible capacity signal, and legitimate path. When a field is unverified,
place it in the validation queue; never fill it from inference.

Keep three judgments separate: evidence status, relationship/access status,
and strategic disposition (`pursue`, `learn`, `validate`, `steward`, `hold`, or
`exclude`). Present evidence and a recommended disposition before requesting
the human review decision and reason.

Retrieve retrievable facts before asking. Ask only for private current/lapsed
relationships, access knowledge, material classification corrections, or the
required strategic decision after public and internal lanes are terminal. If
evidence remains missing, obey the stage's missing-evidence behavior and keep
the gap visible. Return typed route/candidate/qualification results and bounded
section patches for the current stage, or `no_change` when nothing material
changed.
