---
name: aca-crew-handoff
description: Use this when coordinating the ACA multi-agent sales crew handoffs from signal to meeting.
license: MIT
compatibility: Requires the ACA connector (OAuth sign-in, no API key).
metadata:
  author: ACA
  version: "1.1"
  homepage: https://www.automatedclientacquisition.com/mcp
---
# ACA crew handoff

Use this when running or coordinating a multi-agent ACA outbound crew so work moves stage-to-stage without skipping gates.

## The rule for bots (non-negotiable)

- **One agent, one job, narrow scope.**
- Use **deterministic code** everywhere the task is deterministic; use the **model only** where the input is genuinely unstructured.
- Keep a **human at every irreversible action**. Direct sending, publishing, activation and enrollment remain in the ACA app, even after approval. Confirm paid generation and automation-triggering list writes before using those supported tools.
- Run a **drift check every morning** (ICP, prompts, campaign settings, mailbox health, handoff packet quality).

Reading, researching and drafting can run within the user's scope. Sending, publishing, campaign activation and direct enrollment are handed to the human operator in the ACA app. Never invent a connector action or report an app-only action as completed.

## Chain (default)
1. **Head of Sales**: who to target and why (ICP, segments, priorities)
2. **Signal Hunter**: find real buying intent (funding, hiring, competitor engagement, launches, leadership moves)
3. **ICP Analyst**: filter bad fits against the active ICP
4. **Account Researcher**: company + prospect angle, pain, trigger, stakeholders
5. **Lead Enricher**: emails, phones, missing fields (never invent contacts; enrichment runs in ACA at /list-building or as campaign steps)
6. **Intent Scorer**: rank likelihood to buy; park low-intent
7. **LinkedIn Copywriter**: personalised messages from research + score
8. **Outreach Operator**: prepare inactive drafts and review results; the human operator launches and enrolls leads in the ACA app
9. **Reply Agent**: classify replies (interest / objection / OOO)
10. **Follow-up Agent**: keep warm opportunities alive
11. **Meeting Qualifier**: qualify before calendar
12. **Pipeline Analyst**: what ICPs, signals, and messages convert
13. **Sales Manager**: unblock stages, assign handoffs, report status

## Handoff rules
- Pass a short structured packet: who, company, signal/source, ICP fit, research notes, contact confidence, score, next owner.
- Do not skip ICP or enrichment before outreach.
- Do not fabricate emails or phone numbers.
- Use ACA MCP for leads, lists, sequences, campaigns, and reply status when available.
- Hand activation and enrichment setup to the user in the ACA app. Review list automation before any membership write and confirm paid generation separately.
- Sales Manager owns stuck work; Pipeline Analyst advises, does not silently rewrite live campaigns.

## Example path
Signal Hunter finds competitor engagement → ICP Analyst fit-checks → Account Researcher finds angle → Lead Enricher gets contact data → Intent Scorer ranks → Copywriter writes → Outreach Operator prepares draft → human operator activates in ACA → Reply Agent handles response → Meeting Qualifier moves toward demo.
