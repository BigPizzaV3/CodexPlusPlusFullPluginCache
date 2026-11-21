---
name: write-a-business-plan
description: "Write a practical business plan for an artist or music venture: one-page summary, audience, offers and revenue streams, marketing plan, operations, team, milestones, and 12-month projections with explicit assumptions and low/base/high scenarios. Use when the user asks for a business plan, wants a lender or partner to take them seriously, or needs a plan for a label, studio, or touring operation."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Home Base
  group: "Finance"
  display_name: "Business Plan"
  website: https://www.artispreneur.com
---

# Business Plan

> A real plan with real numbers, for you, a partner, or a lender.
> *Home Base desk · Finance · about 30 minutes*

## When to use

- The artist is seeking funding, a partner, or a grant.
- The artist wants to treat the music as a business with a roadmap.
- Launching a label, studio, or service.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- What the business sells or provides, and to whom.
- Current income and costs, if any.
- Time, money, and team available.
- 12-month goals (from `artist-goals`).
- Who will read the plan and what decision they need to make.

## Workflow

1. Write the one-page summary: what you do, for whom, the goal, and the ask.
2. Describe the audience with evidence the artist has (email list, show attendance, listeners), not general market claims.
3. List offers and revenue streams (live, streaming, merch, sync, teaching, services, memberships) with a rough unit economics line for each.
4. Write the marketing plan from the channels that already work.
5. Describe operations, team, tools, and what is outsourced.
6. Set milestones by quarter.
7. Build a 12-month projection with explicit assumptions in a table. Provide low, base, and high scenarios. Every assumption is labeled ASSUMPTION.
8. Add risks and how each is handled, then the funding ask and use of funds if relevant.

## Deliverables

- Business plan document (summary plus sections).
- Assumptions table.
- 12-month projection with three scenarios.
- Milestone timeline.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Every number is either the artist's actual or labeled ASSUMPTION.
- [ ] No market-size or industry statistic appears without a source.
- [ ] The summary fits one page.
- [ ] Scenarios change assumptions, not just totals.

## Guardrails

- Do not invent market data, comparable artists' earnings, or growth rates.
- Do not promise returns to funders.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `budget-planning`: build the budget behind the projection
- `artist-goals`: if goals are unclear
- `create-llc`: if the venture needs an entity

## Start with

> Write a business plan for my music career. Here are my numbers and goals.

---
General information and planning help, not financial advice. Every figure is an estimate built from the numbers you provide.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
