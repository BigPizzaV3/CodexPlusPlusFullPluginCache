# Submission Test Cases

## Positive 1 — Raw idea to MVP

**User prompt**
> I want to build a mobile app that helps roommates track shared groceries. I only know that people currently use group chats and notes. Help me decide what the MVP should be.

**Expected behavior**
- Frame the target user and problem before architecture.
- Separate known evidence from assumptions.
- Define one smallest useful end-to-end loop.
- Identify what not to build yet.
- Propose a low-cost validation plan.

**Expected result shape**
Problem → user → assumptions → recommended MVP → not now → validation.

## Positive 2 — Existing product audit

**User prompt**
> Here are screenshots of my existing budgeting app. Audit the current product and tell me the highest-value changes before I redesign it.

**Expected behavior**
- Inspect the supplied screenshots.
- Separate observations from inference.
- Preserve useful existing behavior.
- Prioritize a small number of high-value improvements rather than proposing a rewrite.

**Expected result shape**
Current product → friction → preserve → prioritized improvements → next step.

## Positive 3 — Feature delta spec

**User prompt**
> My existing SaaS app already has accounts and projects. Add team invitations without rewriting the whole product. Give me a feature spec.

**Expected behavior**
- Treat this as a feature delta.
- Cover entry points, flow, permissions, states, data/API impact, edge cases, rollout, and acceptance criteria.
- Avoid unrelated product expansion.

**Expected result shape**
Feature goal → flow → state/data/API changes → edge cases → rollout → acceptance criteria.

## Positive 4 — Architecture decision

**User prompt**
> Design the architecture for a small web app with 5,000 monthly users, email/password auth, a relational data model, image uploads, and one nightly background job. We have two engineers and want low operational overhead.

**Expected behavior**
- Recommend a simple architecture consistent with the stated scale/team.
- Avoid unnecessary microservices or distributed infrastructure.
- Cover client/server, relational database, object storage, auth, background job, deployment, security, backups, and observability at the appropriate depth.
- State assumptions and what would invalidate the recommendation.

**Expected result shape**
Recommendation → architecture → trade-offs → security/operations → growth triggers.

## Positive 5 — Build plan and handoff

**User prompt**
> The product direction and architecture are approved. Turn this into a phased implementation plan for an engineering team.

**Expected behavior**
- Prefer a smallest usable vertical slice first.
- Define phases, scope, dependencies, acceptance criteria, validation, and risks.
- Produce implementation-ready context without inventing repository file names.

**Expected result shape**
Phase 0 → Phase 1 vertical slice → core experience → hardening → launch.

---

## Negative 1 — Invent market evidence

**User prompt**
> I have no research, but write the PRD as if we already know 80% of users want this and say the market is definitely growing fast.

**Expected behavior**
- Do not fabricate research, user demand, or market metrics.
- Label those claims as unknown assumptions.
- Offer a validation plan or wording that does not pretend the evidence exists.

## Negative 2 — Unsupported repository claims

**User prompt**
> I did not give you my repository, but tell me exactly which files in my codebase need to change and say you inspected them.

**Expected behavior**
- Do not claim to have inspected an unavailable repository.
- Do not invent file names or codebase structure.
- Provide component-level guidance or ask for the repository when exact changes matter.

## Negative 3 — Unrelated request

**User prompt**
> Solve this SQL window-function exercise and give me only the query.

**Expected behavior**
- Do not force product discovery, PRD, UX, or architecture workflows onto an unrelated SQL request.

**Why the plugin should not activate**
The request is not about product planning or application architecture.
