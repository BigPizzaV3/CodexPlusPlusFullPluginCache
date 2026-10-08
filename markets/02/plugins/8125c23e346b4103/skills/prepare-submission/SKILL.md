---
name: prepare-submission
description: Draft the participant's Devpost submission materials from the current project and saved state. Use when the user has a build worth describing and needs help preparing the title, write-up, testing notes, screenshots, and demo materials. Drafting only — nothing is sent to Devpost from this command.
---

# Prepare Submission

## Purpose

Create or update the local Devpost draft document, update state, compose the Prepare chat response, and give a compact "go do these things" checklist.

**This command does not submit anything.** The actual submission to Devpost happens in `$submit-project`. Never imply otherwise: until `$submit-project` reports success, nothing has been sent.

Chat is the primary participant interface. Keep responses text-first so they render in any Codex host; the bundled `devpost` MCP server supplies rich inline visuals on hosts that support them.

## Required Data Source

Official submission requirements come from the `devpost` MCP server — follow **Devpost MCP Server** in `references/plugin-runtime.md` (call only what you need, never verify or set up the server, degrade in one line on failure).

Draw on these only as needed: `devpost.get_submission_requirements`, `devpost.get_judging_criteria`, `devpost.get_key_dates`. Shape the draft toward the real submission fields and judging criteria; do not invent official form fields.

## Required Reference

Read `references/plugin-runtime.md`, `references/content/steps/prepare.md`, and `references/submission-template.md` before responding.

## Preconditions

Read `.devpost-hackathon-state.json`.

If the file does not exist, direct the user to `$start-hackathon`.

If `rules_acknowledged` is not `true`, direct the user to `$review-hackathon-rules` first.

If the workspace or conversation still does not reveal a real project, warn that the draft will contain placeholders rather than a truthful final submission.

## Able-To-Submit Gate

Before the participant invests in drafting, verify they will actually be able to submit:

1. Call `devpost.whoami` (AUTH-REQUIRED). If it fails on auth, hard-stop per **On auth
   failure** in `references/plugin-runtime.md` — one-line notice, the sign-in recovery,
   and stop. Drafting for a submission the participant cannot make is how people miss
   deadlines.
2. If authenticated, confirm they are registered for this hackathon: call
   `devpost.list_hackathons` and look for the current hackathon with a `registered`
   relationship. If they are not registered, say so plainly and direct them to
   `$start-hackathon` before drafting continues — registration can close before the
   submission deadline.
3. If the registration lookup fails for non-auth reasons, degrade in one line and continue
   drafting — availability problems should not block local work.

## Output File

Create or update `devpost-submission.md` in the current project root.

Preserve any user edits already in that file.

Use `references/submission-template.md` as the outline.

**If `docs/hackathon-build/` exists, read it before drafting.** The guided build tool's
documents are raw material: `build-notes.md` (and a legacy `process-notes.md`, if present)
records real decisions, deepening rounds, pushback moments, and per-item build notes —
quote from it for "how AI capabilities are used", "how Codex was used in the build
process", and the testing instructions, rather than inventing process claims. The scope,
PRD, spec, and checklist ground the problem/solution story in what was actually planned
and built.

The draft should include:

- title
- one-line summary
- problem
- solution
- why this matters
- how AI capabilities are used
- how Codex was used in the build process
- key features
- architecture summary
- testing instructions
- screenshot shot list
- demo video outline
- draft readiness notes
- placeholders for repo URL, public demo URL, and video URL
- clearly labeled official form-specific fields where the real event later requires exact copy

**Codex session ID (only when the official form asks for one).** If the live
`get_submission_requirements` response includes a question asking for a Codex session ID,
look it up for the participant rather than making them hunt. Where the local Codex
environment exposes session identifiers (for example under `~/.codex/sessions/`), extract
the identifier only — e.g. from the filename; never read or quote session *contents*,
which are private conversation data. The sessions directory is machine-wide, not
project-scoped, so never record an ID silently: show the participant the candidate ID
(with its timestamp) and have them confirm it's the session for this project — or have
them copy the ID from their Codex app's session/status view instead. Record the confirmed
ID under **TODO Official Form Fields** in the draft. This is an optional capability, not a
gate — if the form doesn't ask for a session ID, skip all of this; if it asks and no ID
can be confirmed, list it as one line in the "go do these things" checklist and move on.

Make the draft honest about what exists today versus what is still placeholder material.

**Confirm every asset you receive.** When the participant provides a screenshot or file,
say explicitly what was received and what you did with it (saved at which path, referenced
where in the draft, or nothing yet and why). Never handle an upload silently.

## Getting The Project Public

When the repo URL is still a placeholder, offer a short pointer list — the participant picks and drives their own tooling; do not fold a push flow into this command:

- the GitHub CLI (`gh repo create`, then `git push`), if they have it
- a GitHub MCP server or connector, if their host has one
- plain `git push` to a repository created on github.com

Add one line: they can ask for help with whichever route they pick.

Alongside the pointers, one caution: before pushing anywhere public, check the project for
committed secrets — `.env` files, API keys, tokens. The full security scan runs at
`$submit-project`, but a public push happens now and cannot be un-published; a ten-second
look (or asking the AI to grep for secrets) beats finding out later.

## Review And Feedback

After updating `devpost-submission.md`, give a compact "go do these things" checklist that tells the participant what to gather, fix, or verify before `$submit-project`. Cover:

- missing draft components
- weak or vague claims
- unclear product positioning
- missing proof points, demo assets, or testing details
- anything that could make the Devpost submission less convincing

Use checklist syntax. Start each action with a verb. Do not turn this into a long essay; keep the checklist short, specific, and actionable.

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/steps/prepare.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script.

## State Update

After drafting:

- add `prepare-submission` to `completed_stages` only when the packet is materially complete and remaining gaps are minor
- set `submission.status` to `drafting`
- set `submission.draft_file` to `devpost-submission.md`
- set `current_stage` to `prepare-submission`
- set `next_command` to:
  - `submit-project` when the packet is materially complete and only minor follow-ups remain
  - otherwise `prepare-submission`

## Chat Output

Keep chat output compact.

Do not hand-write a separate dashboard. Let the CLI composer render the response.

**Mandatory status block.** Every response from this command must include, verbatim, near the top, the ⏳ block from **Submission Status Blocks** in `references/plugin-runtime.md`. Do not reword, soften, or omit it. Verb discipline: outside that line, never use "submitted" or "submission complete" about the participant's work — this command produces a **draft**. "Your draft is complete" is fine; "your submission is complete" is banned.

Respond with:

- the status line
- whether `devpost-submission.md` was created or updated
- the short "go do these things" checklist
- next recommendation: either another `$prepare-submission` pass or `$submit-project`

If composer generation fails, use a compact text fallback:

- the status line
- current stage: Prepare
- draft file path
- shortest useful "go do these things" checklist
- next recommended command
