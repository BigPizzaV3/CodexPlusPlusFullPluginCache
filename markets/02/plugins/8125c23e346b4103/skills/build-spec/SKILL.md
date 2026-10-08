---
name: build-spec
description: Translate the PRD into a practical technical implementation plan.
---

# Guided Build: Spec

Read `references/build-guide.md`, then follow this command.

This is the Codex version of the learning curriculum's spec command.

## Goal

Turn the PRD into a technical spec detailed enough that Codex can build from it without guessing.

Interview first, propose second. Adapt depth to the participant's experience level.

## Preconditions

Read `.devpost-hackathon-state.json`.

If the state file does not exist, direct the user to `$start-hackathon`.

Read everything in `docs/hackathon-build/`. If `scope.md` or `prd.md` is missing, direct the user to the missing prior command.

## Flow

Interview in small batches of related questions (per the build guide). You are a technical collaborator: interview first, propose
second. The participant should walk away understanding their app intimately enough to
explain it to someone else.

Mandatory beats:

1. Tech preferences, calibrated to the learner profile — newer builders: "What sounds
   interesting to you?" plus simple recommendations; experienced builders: "Preferred
   stack? Any strong opinions?" Favor boring, reliable choices over novel plumbing —
   winners spend their time on the product, not the infrastructure.
2. Deployment: local only, or a deployed URL? (Running locally with screenshots is a
   perfectly good answer.)
3. Research the stack: rely on what you already know for well-known frameworks, libraries, and APIs; consult current official docs only for version-specific or fast-moving details you are unsure of, batching those lookups. Do not search for well-known docs you can already summarize.
4. Propose architecture section by section, explicitly mapping PRD epics to components —
   propose briefly, explain why, then ask for their reaction: "Here's how I'm picturing
   the data flow — does this match what you're thinking?"
5. Build the file structure and data flow together: every file and folder annotated with
   its purpose, then walk the lifecycle of the app's most important piece of data from
   input to storage to display.

After mandatory beats, offer a deepening round per the build guide. Good spec deepening
topics: state ("for every piece of data — where does it live, how does it get updated,
what happens when they navigate away and come back?"), exact API contracts (endpoint,
payload, response shape — this prevents build stalls), error strategy ("the 2-3 places
this will actually break during a demo"), demo flow ("if the coolest feature is hard to
demo, that's a spec problem worth solving"), and an architecture self-review: audit your
own draft and surface 2-3 findings as genuine questions for the participant — including
complexity that doesn't match the time budget ("this data model has six tables for an
evening's build").

## Output

Use `references/templates/spec-template.md`.

Create or update:

- `docs/hackathon-build/spec.md`
- `docs/hackathon-build/build-notes.md`

Critical requirements:

- every architectural component has headings
- PRD epics are cross-referenced
- major dependencies and APIs have documentation links
- file structure and data flow are explicit
- if `$build-checklist` needs to point to it, it has its own heading

## State Update

Set:

- `learning.current_step` to `spec`
- add `prd` to `learning.completed_steps` if missing
- `next_command` to `build-checklist`

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/learning/spec.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script. End by recommending `$build-checklist`.

## Required References

- `references/plugin-runtime.md`
- `references/build-guide.md`
- `references/content/learning/spec.md`
