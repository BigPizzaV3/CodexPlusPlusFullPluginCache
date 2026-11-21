---
name: analyze-social-media-engagement
description: "Audit an artist's social performance from exported analytics: engagement by platform and format, top and bottom posts, patterns, and a short list of next experiments. Use when the user asks 'why is my content not working', 'which posts perform best', 'review my analytics', or 'what should I post next'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Content
  group: "Content & marketing"
  display_name: "Engagement Audit"
  website: https://www.artispreneur.com
---

# Engagement Audit

> See what's working, what's not, and what to post next.
> *Content desk · Content & marketing · about 25 minutes*

## When to use

- The artist has analytics exports or screenshots and no insight.
- After a release campaign to learn what worked.
- Before replanning the content calendar.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Analytics exports (CSV) or pasted numbers for each platform, and the date range.
- Posts and formats in the period (Reel, carousel, photo, text, video).
- Goals for the period (follows, streams, sign-ups).
- Known events that affected results (release, viral clip, paused posting).
- Which metric the artist wants to improve.

## Workflow

1. Check the data for completeness. Note gaps and small samples; do not draw strong conclusions from a handful of posts.
2. Define the metric explicitly (for example engagement rate = interactions divided by reach, or by followers when reach is not available) and use it consistently.
3. Rank posts by the chosen metric and list the top five and bottom five with a note on what they share (format, topic, hook, length, timing).
4. Compare formats and pillars. Report differences with the sample size and a caution when the sample is small.
5. Separate correlation from cause: list hypotheses, not facts.
6. Recommend 3 experiments for the next two weeks, each with a hypothesis, what to change, and how to judge it.
7. Update the content calendar suggestions.

## Deliverables

- Audit summary with the metric definition.
- Top and bottom posts table.
- Pattern findings with sample sizes.
- Three experiments.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Every number comes from the artist's data.
- [ ] Small samples are flagged.
- [ ] Findings are written as hypotheses where causes are unknown.
- [ ] No industry benchmarks are cited without a source.

## Guardrails

- Do not invent benchmarks or averages.
- Do not log in to accounts; use exports or pasted data.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-content-calendar`: apply the findings
- `generate-social-media-content`: write the experiment posts
- `weekly-win-plan`: fit changes into the week

## Start with

> Audit my social analytics. Here's the export for the last 60 days.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
