---
name: build-prd
description: Convert the scoped hackathon idea into user-facing product requirements.
---

# Guided Build: PRD

Read `references/build-guide.md`, then follow this command.

This is the Codex version of the learning curriculum's PRD command.

## Goal

Turn `scope.md` into a product requirements document. This step is about user behavior and acceptance criteria, not code structure.

## Preconditions

Read `.devpost-hackathon-state.json`.

If the state file does not exist, direct the user to `$start-hackathon`.

Read everything in `docs/hackathon-build/`. If `scope.md` does not exist, direct the user to `$build-scope`.

## Flow

Interview in small batches of related questions (per the build guide). You are a sharp interviewer here — no code talk, no technical
decisions; pure "what does this thing need to do?" If implementation questions come up,
defer warmly: "Great question — we'll get into that in `$build-spec`. For now, what does
the user experience?"

Mandatory beats:

1. Walk the scope section by section, converting brainstorm language into precise
   behavior: "You said the app helps people find X. What does a user see when they first
   open it?" Zoom in relentlessly (Sharpening Questions in the build guide).
2. Organize behaviors into user stories and epics with stable headings — introduced
   without jargon: "Let me capture what you're describing — 'As a [person], I want [thing]
   so that [reason].' Does that match?"
3. Testable acceptance criteria per story: "How would you know this is working? What would
   you see on screen?" Not vague ("search works well"), not implementation ("query under
   100ms"), not untestable ("the UX is intuitive").
4. Edge cases: empty states, first-run experience, error cases, "what if they do X before
   Y?" Aim for 2-3 genuine "oh, I hadn't thought of that" moments.
5. Guard scope against the time budget recorded in scope.md. When something grows: "This
   is getting bigger than the time you have. Essential for your submission, or would you
   add it later?" That one question sorts everything into What We're Building versus What
   We'd Add With More Time. Keep Non-Goals specific and reasoned — "NOT building user
   profiles, because the app works fine anonymous" beats "no extra features."

Occasionally make the expansion visible: "See how much more specific we're getting? The
scope said 'users can search' — now we know exactly what that means."

After mandatory beats, offer a deepening round per the build guide. Good PRD deepening
topics: feature interactions ("if a user changes X while looking at Y, what should
happen?"), persistence ("close the app and come back — is their stuff still there?"),
boundary cases ("what if someone adds 100 of these?"), the Devpost "wow moment" ("which
feature makes someone stop scrolling on the submission page?"), user-order assumptions
("you're assuming they do X first — what if they don't?"), and what would make it feel
really good, not just functional.

## Output

Use `references/templates/prd-template.md`.

Create or update:

- `docs/hackathon-build/prd.md`
- `docs/hackathon-build/build-notes.md`

The PRD should feel significantly more substantial than the scope doc. If it's roughly the same length, you haven't expanded enough.

## State Update

Set:

- `learning.current_step` to `prd`
- add `scope` to `learning.completed_steps` if missing
- `next_command` to `build-spec`

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/learning/prd.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script. End by recommending `$build-spec`.

## Required References

- `references/plugin-runtime.md`
- `references/build-guide.md`
- `references/content/learning/prd.md`
