# Guided Build Tool Guide

Shared behavior for the optional guided build tool. This is a reference document read by
the `build-*` skills — deliberately not a `SKILL.md`, so hosts never list it as an
invocable skill. Keep it that way: do not rename it back to `SKILL.md` or add skill
frontmatter.

Read `plugin-runtime.md` before running any composer, renderer, or scanner command from a participant project.

This guide adapts the Devpost learning curriculum for the Codex hackathon plugin.

The path is nested inside Step 3: Resources and uses six build commands:

`$build-onboard -> $build-scope -> $build-prd -> $build-spec -> $build-checklist -> $build-project`

After `$build-project`, return to the main flow with `$prepare-submission`.

## Core Rules

- Ask questions in small batches: 2-4 related questions per message. One-at-a-time
  ping-pong is cumbersome; a wall of ten is homework.
- Accept natural answers at every branch prompt: "move on", "next", "yes", or a described
  choice advances the flow on that turn — never make the participant re-type a command you
  just offered.
- Fresh-chat resume: `.devpost-hackathon-state.json` and `docs/hackathon-build/` are the
  memory. When a build command runs in a new chat, read them and continue exactly where
  the participant left off — never re-ask anything the docs already answer, never restart
  an interview.
- Stage-movement requests are navigation, not construction. Never scaffold or generate
  project code except when executing a checklist task the participant has confirmed; if
  they ask to move stages, test, or submit, route them there without building anything.
- Use free-form questions for interviews and planning.
- Use flipped interaction: Codex interviews the participant, draws out context, then writes docs.
- Keep the tone brisk, encouraging, and substantive.
- Do not call the participant remedial or imply the guided build tool is mandatory.
- Read upstream docs before writing downstream docs.
- Use local documents as durable context instead of long JSON state.
- Keep `.devpost-hackathon-state.json` small: progress, file paths, and confirmed project metadata only.
- After each build command, run the response composer for the matching build page.
- Chat is the primary participant interface. Keep composer output text-only, including during the optional guided build tool; rich visuals come from the `devpost` MCP server on capable hosts.
- Do not hand-write separate dashboards, Mermaid diagrams, or long duplicate writeups in chat.
- Search the web sparingly. Rely on what you already know for well-known frameworks, tools,
  and patterns; search only for version-specific or fast-moving facts you are genuinely
  unsure of, and batch those lookups. Never search for well-known documentation you can
  already summarize, and never let research stall the interview.

## Documents

Create `docs/hackathon-build/` if it does not exist.

Expected files:

- `learner-profile.md`
- `scope.md`
- `prd.md`
- `spec.md`
- `checklist.md`
- `build-notes.md` (the single journal: build notes, decisions, deepening-round counts,
  and active-shaping moments — planning phase and build phase alike)

Before each command after onboarding, read every existing file in `docs/hackathon-build/`.
If a legacy `process-notes.md` from an older run is present, migrate it once: append its
contents to `build-notes.md` under a "migrated from process-notes" note, delete the legacy
file, and carry on with the single journal.

## Deepening Rounds

For `$build-scope`, `$build-prd`, `$build-spec`, and `$build-checklist`, interview in two phases:

1. **Mandatory beats** — each command lists 4-5 beats: the bare minimum needed to produce a
   meaningful document. They are adaptive guidelines, not a script. If one answer naturally
   covers the next beat, don't force them through it again; if they raise something
   important that isn't in the beats, follow that thread. The goal is the information for a
   strong document, not checked boxes.
2. **Deepening rounds (repeatable)** — after the beats, offer:

> I've got enough to write your [document]. But it's often helpful to overdo your
> specifications — the more thinking and context you put in now, the better everything
> downstream gets. Want another round of questions to sharpen it, or should I write the
> doc now?

Each round is one batched message of 4-5 fresh questions aimed at edge cases,
ambiguities, and whatever the mandatory answers left thin — pulled from the learner
profile and the document so far, and pushing to surface assumptions the participant might
not know they're making. Rounds are unlimited; note in `build-notes.md` how many they
took.

Your questions should be short. Their answers should be long. Be a great interviewer, not
a script-follower: if they give a short answer, don't just move on — this is the moment to
draw them out. Maximum context out of this person is the job.

## Sharpening Questions

Five moves for grilling an idea into specifics. Reach for them by need, not in order:

- **Zoom in:** "You said users can browse X. What do they see first? A list? Cards? Sorted how?"
- **Surface assumptions:** "What does the app look like before they've added anything? What's the very first thing a new user sees?"
- **Find contradictions:** "You want it simple, but you also want filtering by A, B, and C. Which matters most if you had to pick one?"
- **Test completeness:** "Walk me through it start to finish. You open the app. Then what? What do you tap first? What happens next?"
- **Probe the edges:** "What if a search returns nothing? What if they have one item? Fifty?"

## Calibration

Read `docs/hackathon-build/learner-profile.md` before every command and adjust:

- Newer builders: more explanation, simpler recommendations, and 2-3 "what if" moments that
  show why planning pays off.
- Experienced builders: defer to their preferences and focus on tradeoffs and speed —
  they'll anticipate edge cases; help them make implicit decisions explicit.
- Match their energy: amped up → move fast; tentative → encourage and take a beat longer.

This is THEIR project. The best outcomes come when they actively shape every step — invite
pushback, and when they push back, redirect, or overrule you, record the moment in
`build-notes.md`. Active shaping is the point, and it reads well in a submission.

## Feedback And Handoff

After generating each document:

- Give 2-4 sentences of feedback using `✓` and `△`.
- Name the file created or updated.
- Include the composer output for the matching build page.
- Tell the participant the next step. If anything follows the composer output, make the final line exactly: ``Say "next" when you're ready — or type `$command-name`.`` (per PLUGIN_RUNTIME). The named command must come from the state's `next_command`, so "next" always means exactly the next step in the sequence — and the command is the re-entry point if they pick this up in a fresh chat.
- Update `docs/hackathon-build/build-notes.md` — decisions made, deepening-round count, and any active-shaping moments (pushback, redirects), quoted briefly.

Because this is Codex, do not tell the participant to run `/clear` as a hard requirement. Instead, say that the next command can be run in a fresh chat if the conversation feels long.
