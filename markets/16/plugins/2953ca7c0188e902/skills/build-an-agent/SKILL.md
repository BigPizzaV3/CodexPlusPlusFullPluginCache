---
name: build-an-agent
description: "Write a complete agent specification for a music project (mission, scope, soul, skills, tools, memory, hand-offs, guardrails, evaluation, manifest) so the artist can run it in any compatible agent harness. Use when the user asks to 'build an agent', 'make an assistant for my tour or label', or 'create a sub-agent for X'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Home Base
  group: "Build your own"
  display_name: "Build an Agent"
  website: https://www.artispreneur.com
---

# Build an Agent

> Spin up your own sub-agent for a project, with its own tools and memory.
> *Home Base desk · Build your own · about 30 minutes*

## When to use

- A recurring project (tour, release, label, fan community) needs a dedicated helper.
- The artist wants an agent with its own rules and memory.
- A team needs a shared agent specification.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- The agent's job in one sentence and who it serves.
- What it owns and what it must hand off.
- Skills and tools it should use (from this toolkit or others).
- What it needs to remember and what it must never store.
- What it must never do, and when it must ask first.

## Workflow

1. Write the **Soul**: mission, personality, how it thinks, and what it will never do.
2. List the **Skills** it owns (link to existing skills) and write any missing ones with `build-a-skill`.
3. List the **Tools** it uses and the permission each needs. Prefer read-only by default; anything that sends, posts, pays, or files requires explicit human approval.
4. Define **Memory**: what it stores in the artist profile or its own notes, and what is off-limits.
5. Define **Hand-offs**: which agent or human takes over, and the trigger.
6. Add **References**: documents and sources it must ground answers in.
7. Write the **Manifest** as JSON so other tools can load it.
8. Add an **Evaluation** set: three prompts it should handle, three it should refuse or escalate, and the pass criteria. Add a short log format for what it did and why, so problems can be traced.

## Deliverables

- Agent spec (soul, skills, tools, memory, hand-offs, references).
- Manifest JSON.
- Evaluation set.
- Log format.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

```json
{
  "name": "agent-slug",
  "mission": "one sentence",
  "skills": ["skill-slug"],
  "tools": [{"name": "tool", "permission": "read_only | draft_only | needs_approval"}],
  "memory": {"stores": ["artist-profile.md"], "never_store": ["passwords", "tax IDs", "account numbers"]},
  "handoffs": [{"to": "agent-or-human", "when": "trigger"}],
  "evaluation": {"should_do": [], "should_refuse_or_escalate": []}
}
```

## Quality checks (run before handing over)

- [ ] Mission fits in one sentence.
- [ ] Every tool has an explicit permission level.
- [ ] Actions with outside effects require human approval.
- [ ] The evaluation set includes refusal cases.
- [ ] Nothing in the spec stores sensitive identifiers.

## Guardrails

- This skill writes the specification; it does not deploy or run the agent.
- Do not grant an agent permission to send, post, pay, or file without human approval.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `build-a-skill`: write the skills the agent needs
- `artist-profile`: the shared memory
- `knowledge-ingestion`: teach it from existing documents

## Start with

> Design an agent to run my tour logistics. Here's what it should own.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
