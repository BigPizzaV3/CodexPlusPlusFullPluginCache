---
name: executive-brand-summary
description: Create comprehensive, portable executive summaries of a personal, company, product, or service brand strategy for use across AI models, advisors, teams, and brand systems.
---
# Executive Brand Summary

Use this skill to turn the approved brand strategy and available context into a clear, self-contained strategic brief that another person or AI model can understand without access to the original conversation. Identify the brand subject (person, company/organization, product/service, or combination) and do not force a company or product into a personal-brand hierarchy.

## Primary use cases
- Create a "master context" prompt for Claude, Grok, ChatGPT, or another AI model.
- Create an executive brand brief for collaborators, agencies, designers, editors, or marketers.
- Capture the current state of a brand before starting a new project.
- Convert scattered brand decisions into one coherent source of truth.
- Create shorter derivative summaries for specific AI tasks or channels.

## Required strategic distinctions
Clearly define and distinguish, when applicable:
- Person
- Personal Brand
- Market
- Niche
- Sub-niche
- Ideal Client
- Problem / Desire
- Transformation
- Value Proposition
- Differentiation
- Brand Positioning
- Brand Promise
- Brand Personality / Verbal Identity
- Visual Identity
- Messaging Pillars
- Customer Journey
- Solution / Offer
- Business Vehicle
- Business Opportunity

Do not collapse these concepts into interchangeable terms. If a concept has not been decided, label it as "Not yet defined" rather than inventing it.

## Source-of-truth rules
1. Use all relevant information already available in the conversation, approved brand materials, and established plugin context.
2. Distinguish approved decisions from working hypotheses, recommendations, and open questions.
3. Never invent credentials, proof, results, testimonials, audience data, market claims, financial claims, or personal history.
4. Preserve the hierarchy appropriate to the selected brand subject. For a personal brand, use: Personal Brand → Market → Niche → Sub-niche → Ideal Client → Problem/Desire → Transformation → Value Proposition → Solution → Business Vehicle/Opportunity. For a company/product/service brand, distinguish the organization, category, customer, job/problem, offer, value proposition, evidence, positioning, and customer journey.
5. Keep the person's reputation distinct from the company/product brand. Treat a business vehicle or opportunity as secondary only when the active strategy is specifically a personal brand.
6. If there are contradictions, surface them instead of silently choosing one.
7. Prefer concise, high-information language that another AI can reliably parse.

## Standard executive summary structure
Unless the user requests another format, produce:
1. Executive Overview
2. Brand Subject & Architecture (person, company/organization, product/service, or combination)
3. Relevant founder / organization context
4. Market / Category / Niche
5. Intended Customer / Ideal Client and evidence status
6. Problem / Desire / Job to Be Done
7. Value Proposition and Supported Transformation / Customer Value
8. Positioning & Differentiation
9. Brand Promise / Supportable Commitment
10. Brand Personality & Voice
11. Visual Brand Direction
12. Messaging Pillars
13. Customer Journey
14. Product / Service / Offer and capability status
15. Strategic Principles & Guardrails
16. Known Facts / Evidence and Source Scope
17. Open Decisions & Missing Information
18. AI Instructions: How another AI should use this context

Use personal-brand concepts such as transformation, business vehicle, and opportunity only when they fit the selected brand subject. For a company or product, document the offer, organizational role, supported customer value, and brand relationships without forcing personal-brand labels onto them.

## AI portability
When the user says the summary is for another AI, make it self-contained. Include enough context that the receiving model does not need the original conversation. Explicitly tell the receiving AI:
- what the brand is,
- who it serves,
- what it helps them with,
- how it is positioned,
- what it should and should not say,
- which decisions are fixed,
- which decisions remain open,
- and what role the receiving AI is expected to perform.

Do not include irrelevant personal information merely to make the summary longer.

## Output modes
Support:
- Full Master Brand Context
- Executive One-Pager
- AI Context Prompt
- Brand Strategy Brief
- Team / Agency Brief
- Channel-Specific Brand Context
- Update / Change Log

When creating an update, identify what changed, what remains unchanged, and which downstream brand assets may need review.

## Workflow
1. Gather and reconcile existing approved context.
2. Identify missing or contradictory information.
3. Ask one primary discovery question at a time only when the missing information materially affects the summary.
4. Build the structured summary.
5. Separate facts, approved decisions, recommendations, and open questions.
6. Perform a portability check: another AI should be able to understand and act on the brand without the original conversation.
7. Offer a compact version only when useful; never omit critical strategic distinctions merely to shorten it.

## Candid partnership and research standard
Be a candid strategic partner, not an echo chamber or cheerleader. Do not agree or praise merely to please. Challenge material assumptions, weak reasoning, gaps, contradictions, and meaningful risks; explain why they matter and offer a better-supported alternative when possible. Agree when the reasoning and evidence support it; do not invent objections or debate subjective preferences as facts.

For material business, customer, market, competitor, demand, pricing, performance, platform, regulatory, or feasibility claims, make relevant research and evidence the primary basis. Prefer direct/first-party evidence and current authoritative sources appropriate to the question; cite and scope sources, look for counterevidence, and state limitations. User or project preferences guide choices but do not prove factual claims. If evidence is missing or mixed, say so and keep the conclusion HYPOTHESIS or UNKNOWN. Purely creative work needs no unrelated research; factual claims in creative assets still need support.
