---
name: wordesk-analytics
description: Route general Wordesk analytics requests to the report-specific Wordesk skills. Use business-overview for a combined briefing, conversation-insights for conversations, team-performance for agents, sales-conversions for revenue, and marketing-performance for campaigns or automations. Read-only analysis only.
---

# Wordesk Analytics

Use the matching report-specific skill:

- [Business overview](../business-overview/SKILL.md): combined business briefings.
- [Conversation insights](../conversation-insights/SKILL.md): volumes, escalation, categories and channels.
- [Team performance](../team-performance/SKILL.md): AI and human agents, response times and busiest hours.
- [Sales and conversions](../sales-conversions/SKILL.md): Wordesk-attributed orders and revenue.
- [Marketing performance](../marketing-performance/SKILL.md): campaigns and automations.

Follow the selected skill's tool contract and the returned report definitions.
Period presets resolve in the company timezone. Use the server's comparison
period and never interpret AI handling as proof that a conversation was resolved.
These workflows are read-only; never change data or send messages.
