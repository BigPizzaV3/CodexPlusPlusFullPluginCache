---
name: build-a-skill
description: "Turn an artist's repeatable workflow into a complete, portable SKILL.md (name, trigger-rich description, inputs, steps, deliverables, quality checks, guardrails, hand-offs) with test prompts and packaging notes for AI skill harnesses. Use when the user asks to 'make a skill', 'turn this process into a reusable tool', or 'package my workflow'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Home Base
  group: "Build your own"
  display_name: "Build a Skill"
  website: https://www.artispreneur.com
---

# Build a Skill

> Turn your workflow into a skill you can reuse or share with your team.
> *Home Base desk · Build your own · about 20 minutes*

## When to use

- The artist keeps repeating the same multi-step task.
- The artist wants to reuse or share a playbook with collaborators.
- An existing prompt is long and fragile.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- The task, from trigger to finished deliverable.
- Who runs it and what they supply each time.
- What good output looks like (an example).
- Rules it must follow and mistakes to avoid.
- Target environment or assistant harness where the skill will run.

## Workflow

1. Walk through the task once with the artist and note every input, decision, and output.
2. Name the skill in lowercase with hyphens (for example `tour-settlement-check`). Keep it under 64 characters.
3. Write the description in third person with what it does and when to use it, including the phrases a user would actually say. Keep it under 1024 characters; this is what decides when the skill runs.
4. Write the body in this order: When to use, Ask first, Workflow, Deliverables, Quality checks, Guardrails, Hand-offs, Start with. Keep the main file focused and put long material in a `references/` folder.
5. Write quality checks as a checklist the agent runs before handing over.
6. Write three test prompts that should trigger the skill and three that should not. Run them and tighten the description if it misfires.
7. Add packaging notes: the folder structure, how to install it in each target tool, and a version number.
8. Review for safety: no secrets, no claims of actions it cannot take, and a clear human-approval point before anything leaves the conversation.

## Deliverables

- Complete `SKILL.md` in the standard template.
- Test prompt set (positive and negative).
- Packaging and install notes.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

```markdown
---
name: skill-name
description: What it does and when to use it, using the words a user would say. Under 1024 characters.
---
# Skill Name
## When to use
## Ask first
## Workflow
## Deliverables
## Quality checks
## Guardrails
## Hand-offs
## Start with
```

## Quality checks (run before handing over)

- [ ] The description says both what it does and when to use it.
- [ ] Triggers use the user's own words.
- [ ] Steps are specific enough that a stranger could follow them.
- [ ] Quality checks are testable.
- [ ] The skill states what it will not do.

## Guardrails

- Never include credentials, API keys, or personal data in a skill.
- A skill must not claim abilities the environment lacks.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `build-an-agent`: assemble skills into an agent
- `knowledge-ingestion`: extract the workflow from existing documents

## Start with

> Turn my process for planning a release show into a reusable skill.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
