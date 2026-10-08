---
name: hackathon-map
description: Orient the participant — show the command map, current project progress, deadline/readiness context, and the next recommended command. Use when the user asks what commands are available or what this can do, asks how to get started with the hackathon or Devpost, seems confused, stuck, or unsure what to do next, wants to resume after context loss, or wants to know what to do next.
---

# Hackathon Map

## Purpose

Orient the participant. For a brand-new user this is the friendly tour: what this is, the commands, and where to start. For a returning user it reads the local state file, tells them where they are, and points to the next command in the main chat body.

Chat is the primary participant interface. Keep responses text-first so they render in any Codex host; the bundled `devpost` MCP server supplies rich inline visuals on hosts that support them.

Unlike the step commands, `$hackathon-map` does not mark workflow stages complete.

## Required Data Source

Official event data comes from the `devpost` MCP server — follow **Devpost MCP Server** in `references/plugin-runtime.md` (call only what you need, never verify or set up the server, degrade in one line on failure).

Draw on these only as needed: `devpost.get_hackathon_overview`, `devpost.get_key_dates`, `devpost.get_announcements`.

## Required References

Read:

- `references/plugin-runtime.md`
- `references/content/steps/map.md` (the page content when state exists)
- `references/content/steps/help.md` (the welcome tour when no state exists or the user asks for orientation)
- `.devpost-hackathon-state.json` when present
- `references/config/hackathon.json`

If the state file does not exist:

- do not create files from this skill alone unless the user explicitly asks
- present the welcome tour from `references/content/steps/help.md`: the entry point is
  `$find-hackathon` (see what's open in this app), then `$start-hackathon` (register and
  begin) and the rest of the five-step journey
- keep it warm and skimmable — a tour guide, not a wall of documentation

## Tailoring

Adapt to what prompted the command:

- **They asked a specific "how do I…" question:** answer that first in a sentence or two,
  name the command that handles it, then offer the map or tour compactly.
- **They seem stuck or frustrated:** acknowledge it, give the single most likely command or
  fix first, and keep the rest short.
- Do not call `devpost` MCP tools for a plain orientation response — only if the user's
  question also asks about dates, rules, or other event specifics, and then only what that
  question needs.

## State Shape

Expect the state file to stay small:

- `current_stage`
- `completed_stages`
- `rules_acknowledged`
- `registration`
- `project`
- `learning`
- `submission`
- `deadlines`
- `next_command`

If an older state file references removed prototype fields like `dashboard`, `reminders`, or `deadline-reminders`, treat them as legacy. Do not reintroduce those concepts into the participant-facing output.

## Presentation Output

When state exists, compose the recovery response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/steps/map.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script.

When no state exists (or the user asked for orientation), compose from `references/content/steps/help.md` the same way — trimming sections irrelevant to what the user asked is fine; do not invent commands that are not in the page content.

The response should show the current top-level stage, completed stages, optional guided build tool state, deadline status, and next command without marking anything complete.

## Chat Output

Keep chat output compact.

Do not hand-write a separate dashboard. Let the CLI composer render the response.

Respond with:

- current stage
- completed stages, summarized
- next recommended command — **unless the journey is complete** (every stage done and the
  submission verified submitted): then never print a next-command line at all ("Next
  command: None" reads as a dead end). Instead say plainly that the journey is complete,
  and list what they can still do before the deadline: improve the public project page,
  add screenshots or an optional video, invite teammates, share the project. Close with
  the anytime-offer line from `references/plugin-runtime.md` ("That's everything — type
  `$hackathon-map` anytime…").
- deadline status if known, otherwise `official deadline to be confirmed`
- **submission truth:** if the participant has been through `$prepare-submission` or
  `$submit-project` but `submission.status` is not `submitted`, include, verbatim, next to
  the deadline status, the ⏳ block from **Submission Status Blocks** in
  `references/plugin-runtime.md`.
  Local state never proves a submission — if the user asks whether they submitted,
  verify live via `devpost.get_project` / `devpost.list_my_projects` (AUTH-REQUIRED) and
  answer from that. Treat a legacy `submission` entry in `completed_stages` as the
  `submit-project` stage, not as proof of submission.

If state does not exist, respond with the welcome tour (from `references/content/steps/help.md`):

- one friendly line about what this is
- entry command: `$find-hackathon`
- the five-step command journey, compactly
- the optional guided build track, in one line

## Command Map

Entry point, before any state exists:

`$find-hackathon`

Core sequence:

`$start-hackathon -> $review-hackathon-rules -> $resources -> $prepare-submission -> $submit-project`

Optional build sequence inside Step 3:

`$build-onboard -> $build-scope -> $build-prd -> $build-spec -> $build-checklist -> $build-project -> $prepare-submission`

Only show the full command map when the user asks for commands or when no state exists. Otherwise show only the next recommended command.
