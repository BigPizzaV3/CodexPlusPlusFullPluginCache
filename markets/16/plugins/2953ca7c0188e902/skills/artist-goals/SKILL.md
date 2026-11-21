---
name: artist-goals
description: "Convert vague ambitions into one to three measurable, dated music-career goals with a first concrete step and a parked-goals list. Use when the user says 'set my goals', 'what should I focus on', 'I want to grow my fanbase', 'plan my year', or has too many priorities and needs focus."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Home Base
  group: "Career"
  display_name: "Goal Setting"
  website: https://www.artispreneur.com
---

# Goal Setting

> Turn 'I want to blow up' into 1 to 3 dated goals you can actually hit.
> *Home Base desk · Career · about 10 minutes*

## When to use

- The artist has big ambitions but no measurable target.
- A new quarter, release cycle, or year is starting.
- The artist is overwhelmed by options and needs to pick.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- What does success look like in 12 months, in the artist's own words?
- Current baseline for the metric that matters (listeners, email list, show income, revenue).
- Time available per week and any budget limit.
- Hard deadlines (release dates, tours, festival submissions).

## Workflow

1. Restate the ambition and separate outcomes (what you want) from activities (what you do).
2. Pick the one metric that proves each outcome. Prefer metrics the artist controls: email subscribers, shows booked, releases shipped, revenue.
3. Write 1 to 3 goals as: **[verb] [metric] from [baseline] to [target] by [date]**.
4. Stress-test each goal: is the baseline known, is the target reachable in the time and hours available, what is the first step this week.
5. Move everything else to a parked list with a revisit date. Three goals is the maximum.
6. Write the first concrete step for the top goal and the weekly check-in question.

## Deliverables

- `goals.md`: 1 to 3 dated, measurable goals with baseline, target, date, and first step.
- Parked-goals list with revisit dates.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

```markdown
## Goal 1: [verb] [metric] from [baseline] to [target] by [date]
- Why it matters:
- First step (this week):
- Weekly check-in question:
- Risk to watch:
## Parked goals
| Goal | Revisit date |
```

## Quality checks (run before handing over)

- [ ] Each goal has a baseline, a target, and a date.
- [ ] Targets are realistic for the hours and budget the artist stated.
- [ ] No more than three active goals.
- [ ] The first step can be done this week.

## Guardrails

- Do not set targets from invented industry averages. Use the artist's own baseline or mark the target as a hypothesis.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `weekly-win-plan`: turn the top goal into this week's three moves
- `budget-planning`: check the goal is affordable
- `release-music-with-dsp`: if the goal is a release

## Start with

> Help me set my goals for the next 12 months. Ask me where I am right now first.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
