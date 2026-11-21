---
name: budget-planning
description: "Build a plain-language budget for a release, tour, or year by category, calculate runway (months of cash at the current burn), compare scenarios, and set go/no-go thresholds. Use when the user asks 'how much should I spend on my release', 'budget my tour', 'how long can I keep doing this', or 'can I afford this'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Finance"
  display_name: "Budget & Runway"
  website: https://www.artispreneur.com
---

# Budget & Runway

> A plain-language budget and runway for your release, tour, or year.
> *Business desk · Finance · about 20 minutes*

## When to use

- Planning a release, tour, or video and costs are unclear.
- The artist wants to know how long their money lasts.
- Deciding between two ways to spend a limited budget.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- What is being budgeted (release, tour, video, or the whole year) and the time frame.
- Cash on hand and expected income, split into confirmed vs hoped-for.
- Known costs and quotes.
- Fixed monthly obligations.
- The most the artist is willing to lose on this project.

## Workflow

1. Set the scope and time frame.
2. List income in three tiers: confirmed, likely, hoped-for. Plan on confirmed income only.
3. List costs by category using quotes where available. Add a contingency line (a common planning buffer is 10 to 20 percent; the artist chooses).
4. Calculate net per period. Runway (months) = cash on hand divided by average net monthly spend (burn). Show the formula and inputs.
5. Run three scenarios: low, base, high.
6. Set decision thresholds: the point at which to cut scope, pause, or proceed.
7. Recommend the three highest-leverage cuts or priorities.

## Deliverables

- Budget table by category.
- Runway calculation with formula.
- Three-scenario comparison.
- Go/no-go thresholds.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

Formulas: Net = income - costs. Burn = average monthly net outflow. Runway (months) = cash on hand / burn. Break-even units = fixed costs / (price - variable cost per unit).

## Quality checks (run before handing over)

- [ ] The plan relies on confirmed income only; hoped-for income is shown separately.
- [ ] All costs have a source (quote or labeled estimate).
- [ ] Runway uses the artist's own numbers.
- [ ] A contingency line exists.

## Guardrails

- Do not assume income the artist has not named.
- Label every estimate.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `release-music-with-dsp`: budget a release
- `manage-business-expenses`: compare plan against actual spend
- `write-a-business-plan`: extend into a full plan

## Start with

> Budget my next release and tell me my runway. Here's what I have.

---
General information and planning help, not financial advice. Every figure is an estimate built from the numbers you provide.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
