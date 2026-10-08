---
name: build-onboard
description: Start the optional guided build tool inside Step 3 Resources. Use when the participant wants help shaping a hackathon project before submission prep.
---

# Guided Build: Ideate

Read `references/build-guide.md`, then follow this command.

This is the Codex version of the learning curriculum's onboarding command. In the participant UI, this phase is labeled `Ideate`.

## Goal

Welcome the participant, introduce the optional guided path, begin brainstorming the project idea, and create `docs/hackathon-build/learner-profile.md` so every downstream build command can calibrate to who they are.

Do not over-explain the whole process. Keep onboarding warm and efficient.

## Preconditions

Read `.devpost-hackathon-state.json`.

If the state file does not exist, direct the user to `$start-hackathon`.

If `rules_acknowledged` is not `true`, direct the user to `$review-hackathon-rules` first.

Create `docs/hackathon-build/` if needed. Read any existing files in it before asking questions.

## Flow

Open with a brief welcome. Make one thing explicit up front: this is THEIR project — the
best outcomes come when they actively shape every step, push back on suggestions, and say
when something doesn't feel right. Then explain:

- **the opening bookend — set expectations honestly:** this will help you get to a proof
  of concept. It will not finish the thing for you — you'll keep working on it after. And
  if you're newer to coding with AI, it's a good way to get practice with the more
  structured best practices of doing it. (`$build-project` closes this bookend at the end
  of the build — the promise made here is the one kept there.)
- the format: this works like an interview — Codex asks, you talk, Codex writes the docs.
  The more context you give, the better everything downstream gets.
- answering by voice works great here: use your operating system's built-in dictation, a
  third-party speech-to-text app — or, in the desktop app, click the microphone icon in
  the input bar. Longer, rambling answers are exactly the right material. Summarize
  dictated answers back and confirm before writing durable files.
- the docs are useful build context and submission evidence
- the command chain is `$build-onboard -> $build-scope -> $build-prd -> $build-spec -> $build-checklist -> $build-project`

The composed onboard page (`references/content/learning/onboard.md`) carries the bookend, the
voice note, and the token-strategy tip (plan with your most powerful model, execute with
cheaper models or subagents) — let the page say them and keep your own welcome prose to a
line or two; do not deliver the same pitch twice in one response.

Keep the onboarding brisk. Ask questions in batches, not one at a time — repeated single-question back-and-forth is cumbersome in the desktop app.

**Name — never ask for it.** Call `devpost.whoami` once during this onboarding (the sanctioned personalization exception in `references/plugin-runtime.md`) and greet the participant by the name it returns, confirming in passing ("I'll call you Joe — say otherwise if you'd prefer something else"). If the call fails or returns no usable name, simply proceed without one — do not ask for a name, do not mention the miss, do not treat it as an error. Do not ask what brought them to the hackathon.

The interview runs in rounds:

**Round 1 — the essentials.** One message, these two questions:

1. Do you have an idea of what you want to build today? (A rough sketch is fine — "no idea yet" is a valid answer.)
2. What's your coding experience — level, and any languages, frameworks, or AI coding agents you've used?

**Round 2 — sharpen the idea (always runs).** One batched message of 3-4 questions reacting to their round-1 answers: draw on **Sharpening Questions** in the build guide to make the idea concrete, or — if they had no idea yet — brainstorm with them until a candidate direction emerges. Do not skip this round or offer to skip it; the extra context is the point.

**Round 3 — the fun round (optional per question).** Offer a menu of 4-6 lighter questions and say explicitly: **answer any of these that spark something — skip the rest freely.** Draw from:

- inspirations: movies, games, apps, other software — anything whose spirit they'd like this project to have
- look and feel: color palettes, fonts, design tokens, aesthetic styles
- tone and vibe, asked creatively — e.g. "If your app were a place, what would it feel like to walk into?" or "What's an app whose *feel* you'd steal, even if it does something totally different?"

After round 3 (answered or skipped), move on to `$build-scope`.

## Output

Use `references/templates/learner-profile-template.md`.

Create or update:

- `docs/hackathon-build/learner-profile.md`
- `docs/hackathon-build/build-notes.md`

## State Update

Set:

- `learning.status` to `active`
- `learning.current_step` to `onboard`
- add `resources` to `completed_stages` if missing
- `current_stage` to `resources`
- `next_command` to `build-scope`
- `participant.display_name` when `whoami` returned a name the participant didn't correct, or they gave a preferred one
- `project.summary` when the participant describes the project idea
- `project.name` when the participant gives a clear project name

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/learning/onboard.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script. End with a compact note that the next command is `$build-scope`.

## Required References

- `references/plugin-runtime.md`
- `references/build-guide.md`
- `references/content/learning/onboard.md`
