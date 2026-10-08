# PRD and Feature Spec Templates

## Purpose

Use these templates after the product direction is clear.

Requirements should create shared understanding and guide decisions. They should not freeze every implementation detail prematurely.

# 1. Lightweight Product Brief

## Problem
What user problem is being solved?

## User
Who is it for?

## Product promise
What will the product help the user accomplish?

## Goals
What outcomes matter?

## Non-goals
What is explicitly out of scope?

## Core experience
Describe the smallest end-to-end user loop.

## Requirements
List only meaningful functional requirements.

## Success signals
What observable behavior/result suggests value?

## Assumptions
What is not yet verified?

## Risks
Product, data, technical, legal, security, operational, or distribution risks.

## Open questions
Only questions that can change scope or implementation.

# 2. Full PRD

Use when multiple people/components need stronger alignment.

Include as relevant:
- summary;
- problem and evidence;
- target users/jobs;
- goals;
- non-goals;
- user journeys;
- functional requirements;
- UX states;
- data/content requirements;
- integrations;
- security/privacy;
- accessibility;
- nonfunctional requirements;
- analytics/success signals;
- rollout/migration;
- risks;
- assumptions;
- open questions;
- acceptance criteria.

Prioritize requirements as Must / Should / Could when useful.

# 3. Feature Delta Spec

Use for a feature added to an existing product.

## Feature
One-sentence description.

## User goal
Why would the user use it?

## Entry points
Where does the user encounter it?

## Flow
Step-by-step happy path.

## State changes
What changes in client, backend, or data?

## Permissions
Who can see/do what?

## Edge cases
Only meaningful cases.

## UI states
Loading, empty, success, error, partial/degraded, permission denied, destructive confirmation when relevant.

## Data model impact
New/changed entities, fields, relationships, retention.

## API/integration impact
New/changed contracts.

## Analytics
Events or outcomes needed to evaluate the feature.

## Rollout
Feature flag, migration, beta, compatibility, backfill if relevant.

## Acceptance criteria
Observable conditions for done.

## Out of scope
Prevent feature creep.

# 4. User story guidance

Use user stories only when they improve clarity.

Format:

**As a** `<user>`  
**I want** `<capability>`  
**So that** `<outcome>`

A story should describe user value, not dictate architecture.

# 5. Acceptance criteria

Prefer observable behavior.

Include:
- precondition;
- action;
- expected result;
- important error/permission behavior.

Avoid vague criteria such as “works well,” “fast,” or “user friendly.”

When performance matters, define a measurable target only when requirements or evidence support one.

# 6. Decision log

For consequential decisions capture:
- decision;
- context;
- options considered;
- reason;
- trade-off;
- date/version;
- what would cause reconsideration.
