---
name: weekly-win-plan
description: "Rank the artist's top one to three actions for the week against their goals, name which skill handles each, and flag anything overdue or blocked with a way to unblock it. Use when the user asks 'what should I do this week', 'what's next', 'I'm stuck', or at the start of any work week."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Home Base
  group: "Career"
  display_name: "Weekly Win Plan"
  website: https://www.artispreneur.com
---

# Weekly Win Plan

> Your top 3 moves this week, ranked by what actually moves the needle.
> *Home Base desk · Career · about 5 minutes*

## When to use

- Start of the week or after a big event (release, show, campaign).
- The artist has a long to-do list and no priority.
- Something is blocked and the artist is unsure how to move.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Current goals (or read `goals.md`).
- What was planned last week and what got done.
- Hours available this week and any fixed commitments.
- Anything blocked or waiting on someone else.

## Workflow

1. Review last week: done, not done, and why.
2. List every candidate task, then score each by impact on the top goal (high/medium/low) and effort (hours).
3. Choose the top three. Prefer high impact and low effort; never more than three.
4. Map each pick to the skill that does it (for example `booking-outreach`, `create-content-calendar`).
5. List overdue or blocked items with the specific unblock: who to ask, what to decide, or what to drop.
6. End with one sentence: the single move that matters most.

## Deliverables

- `weekly-plan.md`: top 1 to 3 moves, ranked, each with the skill to run and the time needed.
- Overdue and blocked list with unblock steps.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Maximum three moves.
- [ ] Each move traces to a current goal.
- [ ] Total hours fit the time the artist has.
- [ ] Every blocked item has a concrete next action.

## Guardrails

- Do not pad the plan with busywork to look productive. A short list is correct.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `artist-goals`: if no goals exist yet
- `create-content-calendar`: content-heavy weeks
- `booking-outreach`: booking-heavy weeks

## Start with

> What are my top three moves this week? Here is what I got done last week and what's on my list.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
