---
name: build-scope
description: Help the participant turn a rough hackathon idea into a focused scope document.
---

# Guided Build: Scope

Read `references/build-guide.md`, then follow this command.

This is the Codex version of the learning curriculum's scope command.

## Goal

Use flipped interaction to draw out the participant's idea, sharpen it, cut scope, and write `docs/hackathon-build/scope.md`.

This is the most important context-gathering conversation in the guided build tool. Do not rush to the document.

## Preconditions

Read `.devpost-hackathon-state.json`.

If the state file does not exist, direct the user to `$start-hackathon`.

If `learning.status` is not `active`, direct the user to `$build-onboard` first.

Read everything in `docs/hackathon-build/`, especially `learner-profile.md`.

## Flow

Interview in small batches of related questions (per the build guide). You are a brainstorm partner here: provocative, curious,
expanding before constraining. Do not rush to the document — the conversation IS the value.

Mandatory beats:

1. **The brain dump** — the most important question in the guided build. In your own words:
   "Tell me everything. What's the idea? What excites you about it? Who would use it? What
   inspired it? What does it look like in your head? Don't worry about organizing your
   thoughts — just dump it all out." If they need fuel: What's the vibe — playful, serious,
   minimal, rich? What would the finished thing look like if you close your eyes and
   imagine it? What part excites you most? (Suggest once that dictating with speech-to-text
   gets more of their thinking out than typing.)
2. **Research and reaction**: offer 2-3 inspiring examples in the same space from what you
   already know, explain why each might be relevant *to this participant*, and ask what
   resonates. Search the web only if you genuinely lack relevant examples — one quick pass
   at most.
3. **Time budget**: ask how much build time they actually have before the deadline. That
   number is the scope ruler for everything downstream — record it in the doc.
4. **Sharpen the gaps**: name the 2-3 biggest ambiguities their answers left thin and probe
   those specifically (use the Sharpening Questions in the build guide).
5. **Cut scope**: now cut. Challenge vague thinking — five mushy features versus one sharp
   one: which ships in the time they have? Help them kill their darlings, and ground it in
   what wins hackathons: a strong, clear concept beats scattered technical work every time.
   What's cut goes in the doc by name, with rationale.

After mandatory beats, offer a deepening round per the build guide. Good scope deepening
topics: aesthetic feel and emotional hook ("what would make you proud to show this to
someone?"), 3-5 possible directions from the spark (some ambitious, some focused, some
weird), what "done" looks like, and assumptions worth challenging ("You said X — but what
if Y?").

## Output

Use `references/templates/scope-template.md`.

Create or update:

- `docs/hackathon-build/scope.md`
- `docs/hackathon-build/build-notes.md`

## State Update

Set:

- `learning.current_step` to `scope`
- add `onboard` to `learning.completed_steps` if missing
- `learning.plan_file` to `docs/hackathon-build/scope.md`
- confirmed `project.name` and `project.summary` if chosen
- `next_command` to `build-prd`

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/learning/scope.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script. End by recommending `$build-prd`.

## Required References

- `references/plugin-runtime.md`
- `references/build-guide.md`
- `references/content/learning/scope.md`
