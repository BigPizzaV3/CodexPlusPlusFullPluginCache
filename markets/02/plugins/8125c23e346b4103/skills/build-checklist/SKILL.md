---
name: build-checklist
description: Break the technical spec into sequenced build tasks with verification checkpoints.
---

# Guided Build: Checklist

Read `references/build-guide.md`, then follow this command.

This is the Codex version of the learning curriculum's checklist command.

## Goal

Turn the spec into a sequenced, verifiable build checklist. The checklist is the contract `$build-project` will execute.

## Preconditions

Read `.devpost-hackathon-state.json`.

If the state file does not exist, direct the user to `$start-hackathon`.

Read everything in `docs/hackathon-build/`. If `spec.md` or `prd.md` is missing, direct the user to the missing prior command.

## Flow

You are a build strategist. First, ask how involved they want to be, in language close to:

> Want to co-design the plan with me — sequencing, verification checkpoints? Or I can
> handle it. And either way: at times, I can stop and get you to look at what's been made
> so far. Or, I can run through this entire checklist myself and leave you with an MVP.
> It's up to you.

Two decisions come out of that answer: **who designs the plan** (co-design vs. hand it
off) and **whether they want look-at-it pauses** during the build (encoded as the
verification setting either way).

**If they co-design**, work through the mandatory beats (in small batches per the build
guide):

1. Sequencing logic — participant first: "Looking at the spec, what do you think we should
   build first?" Then fill the gaps: what blocks what? What's simplest to get running
   first? What's riskiest (build it early so there's time to pivot)?
2. Build mode: autonomous versus step-by-step. Recommend based on the learner profile, but
   the participant decides — and the choice locks once building starts.
3. Build preferences: verification pauses (optional — moments to stop and look at what's
   been made so far, or none at all and Codex runs straight through; both are legitimate),
   comprehension checks for step-by-step mode, git cadence (commits are revert points),
   and check-in cadence. Encode all of it in the checklist header so `$build-project`
   never re-asks.
4. Submission planning: "What's the wow moment — the single thing that makes someone stop
   and pay attention on the submission page?" Then story, screenshots, repo link, and
   handoff materials. The final checklist item is always the Devpost handoff.
5. Break the spec into 8-12 atomic items, each 15-30 minutes. If there are 15+ items for
   the time budget, consolidate; if 5, it's probably not granular enough. Then gut-check
   with the participant: "Does this feel like the right amount of work for the time you
   have?"

**If they hand it off**, skip the preference interview: sequence the checklist yourself
from the spec, select autonomous mode, set the verification pauses to whichever they chose
(occasional look-at-it stops, or a straight run to the MVP), and encode it all in the
checklist header. Still ask beat 4's wow-moment question — only they can answer it — and
still gut-check the finished checklist with them (beat 5's closing question) before
locking it in.

Each checklist item must use the five-field format:

```md
- [ ] **N. Title**
  Spec ref: `spec.md > Section > Subsection`
  What to build: Concrete description.
  Acceptance: Testable criteria from `prd.md`.
  Verify: Specific command or manual check.
```

After the initial checklist draft on the co-design path, offer a deepening round per the
build guide (on the hand-off path, skip deepening — the gut-check is their review). Good
checklist deepening topics: item size ("are any too big — could they split into more
atomic steps?"), hidden dependencies, verification quality ("would you actually know what
to look for?"), risk points ("should the risky items come earlier?"), autonomous ordering,
and whether the submission item is concrete enough.

## Output

Use `references/templates/checklist-template.md`.

Create or update:

- `docs/hackathon-build/checklist.md`
- `docs/hackathon-build/build-notes.md`

## State Update

Set:

- `learning.current_step` to `checklist`
- add `spec` to `learning.completed_steps` if missing
- `learning.checklist_file` to `docs/hackathon-build/checklist.md`
- `next_command` to `build-project`

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/learning/checklist.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script. End by recommending `$build-project`.

## Required References

- `references/plugin-runtime.md`
- `references/build-guide.md`
- `references/content/learning/checklist.md`
