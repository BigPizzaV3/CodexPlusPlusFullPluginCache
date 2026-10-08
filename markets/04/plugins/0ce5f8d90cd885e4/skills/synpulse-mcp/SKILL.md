---
name: synpulse-mcp
description: Operate SynPulse for targeted, user-directed B2B outreach to specific contacts: workspace setup, contact enrichment, reviewed sequence drafting, sending, monitoring, and control. Do not use for spam, indiscriminate bulk messaging, scraped or purchased lists, or autonomous mass outreach.
---

# SynPulse MCP

Use the connected `synpulse` MCP server as the authority for the user's current workspace state. This skill explains how to operate that server safely. It does not invent campaign strategy, qualify prospects, perform broad prospect discovery, or turn a general conversation into permission to contact people.

## Scope and safety boundary

SynPulse supports targeted business outreach to contacts the user has specifically selected or identified. It is not a bulk blasting or mass-prospecting tool.

Do not use SynPulse to:

- send or queue indiscriminate, high-volume, or repetitive unsolicited messages;
- contact scraped, harvested, purchased, or otherwise mass-collected recipient lists;
- discover or enumerate large recipient lists for the purpose of outreach;
- split a prohibited bulk request into smaller batches to approximate mass messaging;
- run autonomous research-to-enrichment-to-send loops across many people;
- bypass suppression, unsubscribe, rate-limit, sender-readiness, or host-confirmation safeguards;
- create deceptive outreach, impersonate another person or business, or misrepresent an existing relationship.

For multiple recipients, each recipient must be explicitly supplied or selected by the user, and the outreach must remain targeted and individually reviewable. If a request is ambiguous between targeted outreach and mass messaging, do not launch anything; ask the user to narrow the recipient set or keep the result at draft stage.

## Choose the feature

- **Setup and readiness:** Check billing, connected senders, defaults, compliance details, and next actions. Read [references/setup-and-outreach.md](references/setup-and-outreach.md).
- **Enrichment:** Enrich one specific, user-identified business contact from a LinkedIn URL. Read [references/setup-and-outreach.md](references/setup-and-outreach.md).
- **Outreach sequences:** Create literal per-contact drafts, launch reviewed revisions for the selected contacts, monitor progress and replies, or pause/resume/stop future actions. Read [references/setup-and-outreach.md](references/setup-and-outreach.md).

Read only the reference needed for the requested feature.

## Operating rules

1. Start with the smallest relevant read. If sender or workspace readiness is unknown, use `get_onboarding_status`; use `get_outreach_context` before constructing sequences when supported step shapes or limits are unknown.
2. Use IDs, revision numbers, limits, and supported values returned by SynPulse. Do not invent workspace, sender, sequence, prospect, or contact IDs.
3. Treat every non-read tool as a state-changing action. State the concrete target and effect so the host can present meaningful confirmation. Do not bypass a host confirmation or interpret unrelated prior approval as authorization for a new target or effect.
4. Use a fresh top-level `request_id` for each new mutation. Retry the exact same input with the same ID only when recovering from an uncertain response. Never reuse an ID with different input. Do not silently create a new ID to retry a completed enrichment miss or failure.
5. Enrichment is for one specific contact the user identified. Never use enrichment to scrape, enumerate, or build a mass recipient list.
6. Drafting and launching are separate. `create_sequence_drafts` stores exact literal copy and never sends. Preserve one sequence per contact and keep every recipient individually reviewable.
7. Launch only when the user clearly asks to send or launch the specific reviewed sequence or sequences. A request to research, enrich, draft, prepare a campaign, or "reach out" generally is not authorization to launch an unspecified or expanding recipient set.
8. Never repeat launches in a loop or across successive batches to increase volume. If the user asks to contact a broad, indiscriminate, scraped, purchased, or mass-collected audience, do not use SynPulse to send it.
9. Explain that launch and resume may cause external email or LinkedIn actions. Pause and stop prevent future SynPulse work but cannot recall an action already accepted by a provider. Stop is permanent; pause preserves progress for a later resume.
10. Respect suppression, unsubscribe, compliance, rate-limit, and sender-readiness results returned by SynPulse. Do not work around them.
11. MCP does not offer subscription checkout or activation. Report `subscription_required` neutrally when returned. Provider authorization is completed by the user through returned secure URLs or the SynPulse extension. Never ask for card details, mailbox passwords, OAuth tokens, LinkedIn passwords, cookies, `li_at`, or session values.
12. Keep tool inputs task-relevant. Do not send research notes, source dumps, hidden reasoning, or ICP analysis. `approval_rationale`, when useful, must be a short user-visible explanation rather than private reasoning.
13. On a scope, entitlement, readiness, validation, stale-revision, or rate-limit error, report the returned code and actionable next step. Do not broaden scope, switch workspaces, or repeat a charged/external action speculatively.

## Present results

Summarize what SynPulse actually returned: readiness and next actions; credit outcome; created or changed IDs and revisions; scheduled effects; or current status and reply state. Preserve exact draft copy for review. Do not claim that a message was sent merely because a draft was saved or a sequence was queued.
