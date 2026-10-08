---
name: build-project
description: Execute the guided build checklist with Codex while preserving verification pauses.
---

# Guided Build: Build

Read `references/build-guide.md`, then follow this command.

This is the Codex version of the learning curriculum's build command.

## Goal

Build from `docs/hackathon-build/checklist.md` according to the selected build mode.

The intelligence is in the checklist and spec. Do not improvise new items or skip verification preferences.

**Never build unprompted.** Generate code only when executing the current checklist item the participant has confirmed. If they ask to "move to the next stage," test, or submit, that is navigation — route them to the right command without scaffolding anything. When in doubt about whether they want you to build, ask.

## Preconditions

Read `.devpost-hackathon-state.json`.

If the state file does not exist, direct the user to `$start-hackathon`.

Read everything in `docs/hackathon-build/`. If `checklist.md` is missing, direct the user to `$build-checklist`.

If every checklist item is complete, go straight to **Completion**.

## Step-By-Step Mode

Each `$build-project` run handles exactly one unchecked checklist item.

For the first unchecked item:

1. Announce what you are building and why it is next.
2. Build only that item.
3. Verify according to the item's `Verify` field if verification is enabled — the participant runs the check with their own eyes ("run your dev server and tell me what you see when you click X"). The item isn't done until verification passes.
4. If comprehension checks are enabled, ask one precise question about what was built — single unambiguous answer ("which file handles incoming search requests in the code we just wrote?"), never an essay prompt. On a wrong answer, give a 2-3 sentence explanation pointing at the specific code — fill the gap, don't lecture.
5. Mark the item complete in `docs/hackathon-build/checklist.md`.
6. Append build notes to `docs/hackathon-build/build-notes.md`.
7. End by telling the participant to say "next item" when ready — or type `$build-project` again (works in a fresh chat too). If that was the last item, go to **Completion** instead.

## Autonomous Mode

If the checklist selects autonomous mode, work through the checklist in order.

Pause for verification every 3-4 items if verification is enabled, or sooner if risk rises. Each checkpoint: a short summary of what was built, one concrete thing for the participant to try ("run the dev server and search for something — you should see results appear"), and "everything look good?" before continuing.

If you use subagents, give each one the relevant checklist item, the full spec, the relevant PRD section, and the instruction that others may be working in the codebase.

## When Something Breaks

Stop immediately — don't try to be a hero. Explain what happened, what you tried, and why
it is not a quick fix. Propose reverting to the last clean state if one exists.

Then think holistically about the checklist, not just the broken item: propose concrete
edits ("I think item 5 splits into two smaller steps, and item 7 depends on an approach
that won't work anymore"), get the participant's agreement, update
`docs/hackathon-build/checklist.md`, and resume. The checklist is a living document —
plans meet reality and adapt, and that's worth saying out loud: "this is what happens in
real development."

## Completion

When the last checklist item completes — or a run finds every item already done:

1. **Render the stepper on this turn** (`active_step: resources`, `build_assistant: true`,
   `build_step: build`). Completion is worth showing even though the top-level stage has
   not changed — do not let the final turn be the one with no progress visual.
2. **Close the bookend opened at `$build-onboard`**, under the exact heading
   `### You have a proof of concept — not a finished project` (heading level `###`,
   nothing larger — as in `content/learning/build.md`; the header exists so this line
   cannot be skimmed past), in language close to: this is your
   proof of concept — now it's time for you to really work on it. You're in a freeform
   environment now: if you want to start a new chat and prompt this app some more to make
   new changes, you're only just getting started. This is the beginning. Make it your own,
   and if this planning sequence was useful, run it yourself on your next round of changes
   until you have the best version of your project you can imagine.
3. **Do not rush them to submit.** Recommend `$prepare-submission` only as the step for
   when the project feels ready — not as the immediate next action. On this turn, replace
   the standard callout with the when-ready phrasing (as in `content/learning/build.md`):
   ``When your project feels ready — not before — say so, or type `$prepare-submission`.``
   This is a sanctioned exception to the standard final-line format, like the resources
   two-path callout.

## Thumbnails And Screenshots

Build and verification steps sometimes produce a screenshot or image worth using as the Devpost project thumbnail. The `devpost` MCP server offers two upload services for that (both AUTH-REQUIRED) — pick by encoded size: `devpost.upload_project_thumbnail` sends a small image inline as base64 (target ≤ 50 KB encoded), while `devpost.prepare_thumbnail_upload` returns an upload URL plus a curl/PowerShell command that streams a larger file straight from disk without putting the bytes through the conversation. Both accept JPEG/PNG/GIF up to 5 MB.

Uploading is `$prepare-submission` / `$submit-project` work — do not upload during the build unless the participant explicitly asks. If they do ask, pick the service by size and confirm what was uploaded and where it went.

## State Update

Set:

- `learning.current_step` to `build`
- add `checklist` to `learning.completed_steps` if missing
- `next_command` to `build-project` until the checklist is complete
- when complete, add `build` to `learning.completed_steps`, set `learning.status` to `completed`, keep `current_stage` at `resources` (the build lives inside Step 3 — prepare hasn't run yet), and set `next_command` to `prepare-submission`

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/learning/build.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script. End with what changed, how it was verified, and the next step.

## Required References

- `references/plugin-runtime.md`
- `references/build-guide.md`
- `references/content/learning/build.md`
