---
name: compliance-checklist
description: Turn retrieved legal provisions into a cited research checklist of obligations, applicability conditions, deadlines and potential evidence, including GDPR, NIS2 and the AI Act. Use for implementation planning or a gap analysis against information the user supplies. Missing facts remain questions; this does not certify compliance.
license: Proprietary
metadata:
  author: Augment Ltd
  version: "1.3.14"
  compatibility: Requires the connected and authorised EULEX.AI MCP server.
---

# Build an evidence-based compliance checklist

1. Establish activity, sector, jurisdiction, entity size/role and the relevant
   date. Mark missing applicability facts rather than assuming the broadest rule.
2. Identify the governing act with `get_regulation` or `resolve`, then retrieve
   definitions, scope, operative obligations, exceptions and application dates.
   Use `get_structure` for navigation. Confirm capabilities with `list_scopes`.
3. For directives, retrieve reported national measures with `eu_transposition`
   and read the operative national law when supported. Reporting a measure is
   not proof of correct implementation. Distinguish entry into force, application
   date, transposition deadline and a user's internal target date.
4. Turn only evidenced obligations into checklist rows: obligation, applicability
   condition, action, evidence to retain, legal deadline, article/version/source.
   Suggested owner and internal priority are planning suggestions, not legal facts.
5. For a gap analysis, compare only with user-provided evidence. Label rows
   evidenced, partially evidenced, not evidenced or not assessed; missing evidence
   does not prove non-compliance. Include open questions and retrieval gaps.

Do not provide an overall compliant/non-compliant certification. Do not invent
penalties or deadlines, and do not silently replace historical law with current
wording. Keep user confidential details out of retrieval queries.
